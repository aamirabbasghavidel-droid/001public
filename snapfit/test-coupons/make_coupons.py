"""Generate FDM test coupons for the Joint Advisor add-in.

Coupons:
  1. snap_strain_comb (+ _Z variant) and snap_strain_catch:
     8 cantilever arms with the same hook and deflection but different
     lengths, so each arm reaches a different root strain
     (Bayer Table 1, design 1, shape A: eps = 1.5 * y * t / l^2).
  2. clearance_plate + clearance_key_square + clearance_pin_round:
     holes with 0.10 ... 0.60 mm clearance per side.
  3. insert_screw_coupon: heat-set insert holes (M3) and self-tapping pilot
     holes (M3) in a range of diameters.

Run:  python make_coupons.py      (needs: pip install cadquery)
Output goes to ./out as STEP (for SolidWorks) and STL (for the slicer).
"""

import json
import math
from pathlib import Path

import cadquery as cq

OUT = Path(__file__).parent / "out"
FONT = "DejaVu Sans"  # any installed font works; only affects the labels

# ---------------------------------------------------------------------------
# 1. Snap strain comb
# ---------------------------------------------------------------------------
T_ARM = 1.2          # beam thickness in bending direction (mm) = 3 perimeters
B_ARM = 6.0          # beam width (print height, mm)
DEFLECTION = 1.0     # deflection forced at the hook (mm) -> y in Bayer Table 1
SIDE_CLEAR = 0.25    # clearance between hook crest path and catch edge (mm)
HOOK_H = DEFLECTION + SIDE_CLEAR   # hook height above beam face
LEAD_ANGLE = 30.0    # deg, measured from insertion direction (Bayer alpha)
RETURN_ANGLE = 45.0  # deg, releasable (mu*tan(45) = 0.6 < 1)
CREST_FLAT = 0.5     # flat land on hook crest (mm)
PLATE_T = 3.0        # catch plate thickness (mm)
GAP = 0.2            # axial play when snapped -> no preload in closed state
ROOT_R = 0.5 * T_ARM  # root fillet r/t = 0.5 (Hubs; Bayer Fig. 9 optimum ~0.6)
STEM_SIDE = 1.5      # rigid stem extends this far beyond the beam on each side
PITCH = 10.0

# Target root strains (%) -> arm length from eps = 1.5*y*t/l^2
TARGET_STRAIN_PCT = [4.0, 3.0, 2.5, 2.0, 1.6, 1.3, 1.0, 0.8]


def arm_lengths():
    return [math.sqrt(1.5 * DEFLECTION * T_ARM / (e / 100.0)) for e in TARGET_STRAIN_PCT]


def snap_comb_and_catch():
    lengths = arm_lengths()
    y_rb = PLATE_T + GAP                                       # return ramp base
    y_c = y_rb + HOOK_H / math.tan(math.radians(RETURN_ANGLE))  # crest start = load point
    y_tip = y_c + CREST_FLAT + HOOK_H / math.tan(math.radians(LEAD_ANGLE))
    roots = [y_c - l for l in lengths]
    y_back = min(roots) - 6.0

    n = len(lengths)
    x_min = -STEM_SIDE - 4.0
    x_max = (n - 1) * PITCH + T_ARM + STEM_SIDE + 4.0
    comb = cq.Workplane("XY").box(x_max - x_min, 9.0, B_ARM, centered=False).translate(
        (x_min, y_back - 9.0, 0))

    for i, (l, y_root) in enumerate(zip(lengths, roots)):
        x0 = i * PITCH
        stem = cq.Workplane("XY").box(T_ARM + 2 * STEM_SIDE, y_root - y_back + 0.01, B_ARM,
                                      centered=False).translate((x0 - STEM_SIDE, y_back - 0.01, 0))
        beam = cq.Workplane("XY").box(T_ARM, y_tip - y_root + 0.01, B_ARM,
                                      centered=False).translate((x0, y_root - 0.01, 0))
        hook = (cq.Workplane("XY")
                .polyline([(x0 + T_ARM - 0.01, y_rb), (x0 + T_ARM + HOOK_H, y_c),
                           (x0 + T_ARM + HOOK_H, y_c + CREST_FLAT), (x0 + T_ARM - 0.01, y_tip)])
                .close().extrude(B_ARM))
        arm = stem.union(beam).union(hook)
        # root fillets on both re-entrant corners
        for cx, sx in ((x0, -1), (x0 + T_ARM, +1)):
            sq = cq.Workplane("XY").box(ROOT_R, ROOT_R, B_ARM, centered=False).translate(
                (cx if sx > 0 else cx - ROOT_R, y_root, 0))
            cyl = cq.Workplane("XY").circle(ROOT_R).extrude(B_ARM).translate(
                (cx + sx * ROOT_R, y_root + ROOT_R, 0))
            arm = arm.union(sq.cut(cyl))
        comb = comb.union(arm)
        # arm number engraved on the backbone
        label = (cq.Workplane("XY").workplane(offset=B_ARM)
                 .center(x0 + T_ARM / 2, y_back - 4.5).text(str(i + 1), 4.0, -0.4, font=FONT))
        comb = comb.cut(label)

    # catch plate (assembled frame: occupies Y 0..PLATE_T)
    slot_z0, slot_h = 1.0, B_ARM + 0.4
    plate_h = slot_z0 + slot_h + 1.6
    plate = cq.Workplane("XY").box(x_max - x_min, PLATE_T, plate_h, centered=False).translate(
        (x_min, 0, 0))
    for i in range(n):
        x0 = i * PITCH
        sx0 = x0 - (DEFLECTION + 0.5)        # room for the beam to bend away from the hook
        sx1 = x0 + T_ARM + SIDE_CLEAR        # catch edge: hook crest must pass this
        slot = cq.Workplane("XY").box(sx1 - sx0, PLATE_T + 2, slot_h, centered=False).translate(
            (sx0, -1, slot_z0))
        plate = plate.cut(slot)
        label = (cq.Workplane("XZ").workplane(offset=0)   # front face (Y=0)
                 .center(x0 + 4.0, plate_h - 0.9).text(str(i + 1), 1.3, -0.3, font=FONT))
        plate = plate.cut(label)
    plate = plate.translate((0, 0, -slot_z0))  # align slot floor with the comb (assembled frame)

    comb_z =comb.rotate((0, 0, 0), (1, 0, 0), 90)  # arms point up: strain across layers
    table = [{"arm": i + 1, "length_mm": round(l, 2),
              "strain_pct": round(1.5 * DEFLECTION * T_ARM / l ** 2 * 100, 2)}
             for i, l in enumerate(lengths)]
    return comb, comb_z, plate, table


# ---------------------------------------------------------------------------
# 2. Clearance plate
# ---------------------------------------------------------------------------
NOMINAL = 10.0
CLEARANCES = [0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]  # per side, mm
CHAMFER = 0.4   # bottom-edge chamfer against elephant's foot


def clearance_parts():
    n = len(CLEARANCES)
    pitch = 15.0
    w = n * pitch + 5
    plate = cq.Workplane("XY").box(w, 42, 5, centered=False)
    for i, c in enumerate(CLEARANCES):
        x = 10 + i * pitch
        sq = NOMINAL + 2 * c
        plate = (plate.cut(cq.Workplane("XY").box(sq, sq, 12).translate((x, 10, 2.5)))
                 .cut(cq.Workplane("XY").circle(sq / 2).extrude(12).translate((x, 27, -3))))
        plate = plate.cut(cq.Workplane("XY").workplane(offset=5)
                          .center(x, 37.5).text(f"{c:.2f}", 3.2, -0.4, font=FONT))
    # bottom-edge chamfers on every hole
    for i, c in enumerate(CLEARANCES):
        x = 10 + i * pitch
        sq = NOMINAL + 2 * c
        cone = cq.Solid.makeCone(sq / 2 + CHAMFER, sq / 2, CHAMFER,
                                 pnt=cq.Vector(x, 27, 0), dir=cq.Vector(0, 0, 1))
        plate = plate.cut(cq.Workplane("XY").add(cone))
        frust = (cq.Workplane("XY").rect(sq + 2 * CHAMFER, sq + 2 * CHAMFER)
                 .workplane(offset=CHAMFER).rect(sq, sq).loft().translate((x, 10, 0)))
        plate = plate.cut(frust)

    key = (cq.Workplane("XY").box(NOMINAL, NOMINAL, 14, centered=(True, True, False))
           .edges("|Z").fillet(0.3).faces(">Z or <Z").edges().chamfer(0.6))
    pin = (cq.Workplane("XY").circle(NOMINAL / 2).extrude(14)
           .faces(">Z or <Z").edges().chamfer(0.6))
    return plate, key, pin


# ---------------------------------------------------------------------------
# 3. Heat-set insert and self-tapping coupon (M3)
# ---------------------------------------------------------------------------
INSERT_HOLES = [3.9, 4.0, 4.1, 4.2, 4.3, 4.4]  # CAD diameter; CNC Kitchen: 4.2 CAD ~ 4.0 real
INSERT_DEPTH = 6.7                             # M3x5.7 insert, depth L + 1 (CNC Kitchen)
INSERT_BOSS = 8.0                              # wall (8-4.4)/2 = 1.8 >= 1.6 (CNC Kitchen)
PILOT_HOLES = [2.5, 2.6, 2.7, 2.8, 2.9]        # M3 self-tap; CNC Kitchen tested 2.7
PILOT_DEPTH = 10.0
PILOT_BOSS = 9.0                               # wall >= screw diameter (Hubs)


def insert_coupon():
    base = cq.Workplane("XY").box(6 * 13 + 4, 34, 3, centered=False)
    part = base
    for row, (holes, depth, boss, y) in enumerate(
            [(INSERT_HOLES, INSERT_DEPTH, INSERT_BOSS, 9.0),
             (PILOT_HOLES, PILOT_DEPTH, PILOT_BOSS, 24.0)]):
        h = depth + 1.5
        for i, d in enumerate(holes):
            x = 8 + i * 13
            b = cq.Workplane("XY").circle(boss / 2).extrude(h).translate((x, y, 3))
            hole = cq.Workplane("XY").circle(d / 2).extrude(depth + 0.01).translate(
                (x, y, 3 + h - depth))
            part = part.union(b).cut(hole)
            part = part.cut(cq.Workplane("XY").workplane(offset=3)
                            .center(x + (6.2 if row == 0 else 6.6), y - 4.2)
                            .transformed(rotate=(0, 0, 90))
                            .text(f"{d:.1f}", 2.6, -0.4, font=FONT))
    return part


def export(shape, name):
    OUT.mkdir(exist_ok=True)
    cq.exporters.export(shape, str(OUT / f"{name}.step"))
    cq.exporters.export(shape, str(OUT / f"{name}.stl"), tolerance=0.01, angularTolerance=0.1)


def main():
    comb, comb_z, catch, table = snap_comb_and_catch()
    export(comb, "snap_strain_comb")
    export(comb_z, "snap_strain_comb_Z")
    export(catch, "snap_strain_catch")
    plate, key, pin = clearance_parts()
    export(plate, "clearance_plate")
    export(key, "clearance_key_square")
    export(pin, "clearance_pin_round")
    export(insert_coupon(), "insert_screw_coupon")
    params = {
        "snap": {"t_mm": T_ARM, "b_mm": B_ARM, "deflection_mm": DEFLECTION,
                 "hook_height_mm": HOOK_H, "lead_angle_deg": LEAD_ANGLE,
                 "return_angle_deg": RETURN_ANGLE, "root_fillet_mm": ROOT_R,
                 "formula": "eps = 1.5*y*t/l^2 (Bayer Table 1, design 1, shape A)",
                 "arms": table},
        "clearance_per_side_mm": CLEARANCES,
        "insert_holes_cad_mm": INSERT_HOLES, "pilot_holes_cad_mm": PILOT_HOLES,
    }
    (OUT / "coupon_parameters.json").write_text(json.dumps(params, indent=2))
    for row in table:
        print(row)


if __name__ == "__main__":
    main()
