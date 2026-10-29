# نقشه‌ی ساخت — برای Claude Code روی کامپیوتر خودت

> این فایل را Claude Code روی ویندوز می‌خواند و برنامه را می‌سازد.
> تحقیق کامل و جدول تنظیمات در `docs/research.md` است.

## هدف

یک برنامه‌ی **exe ویندوز** که:
1. فایل مدل (STL / 3MF) را می‌گیرد + فیلامنت (PLA / ASA) + کیفیت (ریز / متعادل / سریع) + «محفظه دارم؟»
2. مدل را تحلیل می‌کند (ارتفاع، ابعاد، overhang، سطح تماس با بستر، لایه‌های کوچک)
3. تنظیمات را با فرمول‌های `docs/research.md` حساب می‌کند، روی پایه‌ی پروفایل خود Elegoo برای Neptune 4 Plus
4. با **OrcaSlicer نصب‌شده روی همان کامپیوتر** (حالت خط فرمان) اسلایس می‌کند و G-code می‌دهد
5. (اختیاری) G-code را از طریق Moonraker به پرینتر می‌فرستد

موتور اسلایس از صفر نوشته نمی‌شود؛ OrcaSlicer موتور است و برنامه‌ی ما «مغز» تنظیمات.

## کاربر

- پرینتر: Elegoo Neptune 4 Plus، نازل 0.4، **محفظه دارد**
- اسلایسر فعلی: ElegooSlicer (فورک OrcaSlicer — پروفایل‌های N4 Plus در هر دو یکی است)
- فیلامنت: PLA، و ASA

## پیشنهاد فنی

- Python 3.12، رابط گرافیکی tkinter (بدون وابستگی سنگین)، خواندن STL با numpy
- ساخت exe با PyInstaller (`--onefile --windowed`)
- تست با pytest (موتور قوانین و حل وراثت پروفایل باید تست واحد داشته باشند)

## واقعیت‌های تأییدشده از سورس OrcaSlicer (main، اکتبر 2026)

### محل پروفایل‌ها
- در نصب ویندوز: `C:\Program Files\OrcaSlicer\resources\profiles\Elegoo\` (مسیر را از کاربر بپرس / خودکار پیدا کن)
- ساختار: `machine/EN4SERIES/`، `process/EN4SERIES/`، `filament/EN4SERIES/`، `filament/BASE/`، و فایل‌های پایه مثل `fdm_process_common.json`
- هر فایل: `type`، `name`، `inherits` (اسم والد)، `from`، `instantiation`، و مقادیر **رشته‌ای**؛ مقادیر per-extruder آرایه‌ی رشته‌اند: `"nozzle_temperature": ["270"]`

### زنجیره‌های وراثت (همه داخل پوشه‌ی Elegoo پیدا می‌شوند)
- machine: `Elegoo Neptune 4 Plus 0.4 nozzle` ← `Elegoo Neptune 4 0.4 nozzle` ← `fdm_elegoo_3dp_001_common` ← `fdm_machine_common`
- process: `0.20mm Standard @Elegoo N4Plus 0.4 nozzle` ← `fdm_process_elegoo_04020` ← `fdm_process_elegoo_common` ← `fdm_process_common`
- filament: `Elegoo PLA @EN4 Series` ← `Elegoo PLA @base` ← `fdm_filament_pla` ← `fdm_filament_common`
- filament: `Elegoo ASA @EN4 Series` ← `Elegoo ASA @base` ← `fdm_filament_asa` ← `fdm_filament_common`

**روش:** همه‌ی JSONها را با کلید `(type, name)` ایندکس کن، زنجیره را از ریشه به پایین `dict.update` کن، بعد `inherits` را حذف کن و `"from": "User"` بگذار. طبق `tests/cli/test_cli_strict.sh`: «پریست بدون inherits را CLI همان‌طور که هست می‌خواند».

### دستور CLI (از `tests/cli/*.sh`)
```
orca-slicer --datadir DIR --load-settings "machine.json;process.json" --load-filaments "filament.json" --slice 0 --outputdir OUT model.stl
```
خروجی‌ها و `result.json` را در OUT بخوان. کد خروج 0 = موفق. `--help` را روی نسخه‌ی نصب‌شده اجرا کن و فلگ‌ها را چک کن. اگر ElegooSlicer هم CLI داشت می‌شود همان را استفاده کرد (تأیید نشده).

### مقادیر پیش‌فرض N4 Plus (resolve شده)
- process 0.20 Standard: `wall_loops 2`، `wall_sequence "inner wall/outer wall"`، `seam_position "aligned"`، `seam_slope_type "none"`، `outer_wall_speed 160`، `inner_wall_speed 200`، `top_surface_speed 200`، `precise_outer_wall 0`، `wall_generator classic`، `top_shell_layers 5`، `ironing_type "no ironing"`، `draft_shield disabled`، `default_acceleration 5000`، `outer_wall_acceleration 2500`، `top_surface_acceleration 2000`
- machine: `printable_height 385`، بستر 325×325، شتاب XY 8000، `min/max_layer_height 0.08/0.28`، `gcode_flavor klipper`، `host_type elegoolink`
- filament ASA: `nozzle_temperature 270`، `filament_max_volumetric_speed 12`، `fan_min/max_speed 10/80`، `overhang_fan_speed 80`، `textured_plate_temp 90`، `slow_down_layer_time 3`، `close_fan_the_first_x_layers 3`

### اسم کلیدها و مقدارهای مجاز (enum) — تأییدشده در `src/libslic3r/PrintConfig.cpp`
| کلید | مقادیر |
|---|---|
| `wall_sequence` | `inner wall/outer wall`، `outer wall/inner wall`، `inner-outer-inner wall` |
| `seam_position` | `nearest`، `aligned`، `aligned_back`، `back`، `random` |
| `seam_slope_type` (scarf) | `none`، `external`، `all` |
| `ironing_type` | `no ironing`، `top`، `topmost`، `solid` |
| `draft_shield` | `disabled`، `enabled` |
| `brim_type` | `no_brim`، `outer_only`، `inner_only`، `outer_and_inner`، `auto_brim`، `brim_ears`، `painted` |
| `wall_generator` | `classic`، `arachne` |
| `overhang_fan_threshold` | `0%`، `10%`، `25%`، `50%`، `75%`، `95%` |
| `curr_bed_type` | `Cool Plate`، `Engineering Plate`، `High Temp Plate`، `Textured PEI Plate`، ... |

کلیدهای دیگری که وجودشان تأیید شد: `pressure_advance`، `enable_pressure_advance`، `filament_shrink` (درصد اندازه‌ی بعد از انقباض، مثلاً `99.4%` — نه مقدار انقباض!)، `seam_slope_conditional`، `scarf_angle_threshold`، `seam_slope_start_height`، `seam_slope_entire_loop`، `seam_slope_min_length`، `seam_slope_steps`، `seam_slope_inner_walls`، `inner_wall_acceleration`، `brim_width`، `skirt_loops`، `skirt_distance`، `skirt_height`، `overhang_1_4_speed`..`overhang_4_4_speed`، `only_one_wall_top`، `ironing_flow`، `ironing_spacing`، `ironing_speed`، `top_shell_thickness`، `precise_outer_wall`، `slow_down_layer_time`، `fan_min_speed`، `fan_max_speed`، `overhang_fan_speed`، `hot_plate_temp`، `textured_plate_temp`.

## ساختار پیشنهادی کد

```
neptune_tuner/
  profiles.py      # پیدا کردن پوشه‌ی پروفایل OrcaSlicer، ایندکس، حل وراثت
  model.py         # خواندن STL (باینری و ASCII)، ابعاد، نرمال‌ها، overhang، سطح تماس
  rules.py         # موتور قوانین: ورودی‌ها → دیکشنری تغییرات روی پروفایل
  materials.py     # داده‌های PLA / ASA (دما، فن، فلو، PA، انقباض)
  slicer.py        # نوشتن JSONها، اجرای orca-slicer، خواندن result.json
  moonraker.py     # (اختیاری) آپلود و شروع چاپ: POST http://IP:7125/server/files/upload با print=true
  gui.py           # پنجره‌ی tkinter
tests/
build_exe.bat      # PyInstaller
```

## قوانین اصلی (از research.md)

- ارتفاع لایه: مضرب 0.04، بین 0.08 و 0.28
- سقف سرعت: `v = k·Q / ((w−h)·h + π·h²/4)`؛ k=0.5–0.6 دیواره‌ی بیرونی، 0.85 داخلی
- کیفیت ریز/متعادل: 3 دیواره، `inner-outer-inner wall` + `precise_outer_wall 1` (برای ASA یا مدل با overhang تند > ~40°: `inner wall/outer wall`)، scarf `external`
- ASA با محفظه: نازل 255–265، بستر 100 (سقف 100)، فن 0–15% و overhang 40–60%، brim 5–8mm، `filament_shrink ≈ 99.4%`، بدون draft shield (چون محفظه هست)
- قطعه‌ی بلند و باریک (ارتفاع / کوچک‌ترین بُعد کف > 3) → brim
- لایه‌های رویی: `ceil(1.0 / h)` برای ریز، `ceil(0.8 / h)` برای متعادل
- هشدار ایمنی ASA: تهویه

## ترتیب پیشنهادی ساخت

1. `profiles.py` + تست (حل وراثت روی پروفایل‌های واقعی نصب‌شده)
2. `rules.py` + `materials.py` + تست
3. `slicer.py` — اسلایس یک مکعب ساده و چک کردن G-code
4. `model.py` — تحلیل مدل و وصل کردن به قوانین
5. `gui.py` و ساخت exe
6. Moonraker و حلقه‌ی بازخورد (بعداً)
