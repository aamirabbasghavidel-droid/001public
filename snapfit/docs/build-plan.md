# نقشه‌ی ساخت — افزونه‌ی SolidWorks «Joint Advisor»

> این فایل را Claude Code روی کامپیوتر ویندوزی کاربر می‌خواند و افزونه را می‌سازد.
> قوانین مهندسی و منابع: `snapfit/docs/research.md`.

## هدف

افزونه‌ای داخل **SolidWorks 2025** که:
1. Part چندبدنه (بدنه + درب به‌صورت دو Solid Body) — یا Assembly، یا Part تک‌بدنه — را تحلیل کند
2. بر اساس قوانین مهندسی با منبع، بهترین روش اتصال را پیشنهاد دهد: snap hook، snap حلقوی/پیچشی، Lip/Groove، پیچ مستقیم، مهره‌ی حرارتی، پیچ و مهره، dovetail، آهنربا، ...
3. ابعاد را حساب کند و **گزارش محاسبات** با منبع هر عدد بدهد
4. هندسه را خودش در مدل بسازد (قابل ویرایش)
5. جهت چاپ مناسب را پیشنهاد دهد

کاربر: SolidWorks 2025، قطعه‌ها Enclosure (جعبه یا بدنه‌ی مکانیزم)، پرینت FDM با PLA/ASA روی Neptune 4 Plus.

## اصول غیرقابل‌مذاکره

1. **هیچ عددی بدون منبع وارد کد نمی‌شود.** همه‌ی قوانین در فایل‌های داده (`rules/*.json`) با فیلدهای ردیابی هستند، نه عدد ثابت داخل کد.
2. هر خروجی یک «برچسب منبع» دارد؛ اگر به ورودی سطح C یا D وابسته باشد، بنر «بدون پشتوانه‌ی استاندارد» نشان داده می‌شود.
3. موارد [UNV] در `research.md` تا وقتی با منبع اصلی چک نشده‌اند **غیرفعال** می‌مانند (`verification: UNVERIFIED` → موتور از آن استفاده نمی‌کند).
4. مقادیر جنس به‌طور پیش‌فرض از TDS؛ ولی کاربر می‌تواند نتیجه‌ی تست خودش را وارد کند و آن اولویت دارد.

### ساختار رکورد قانون
```json
{
  "rule_id": "cantilever.rect.deflection",
  "formula": "y = 0.67 * eps * l^2 / t",
  "units": {"y": "mm", "l": "mm", "t": "mm", "eps": "-"},
  "applies_to": {"process": ["IM", "FDM"], "materials": "*"},
  "source_type": "DERIVED",
  "doc": "Bayer MaterialScience, Snap-Fit Joints for Plastics",
  "edition": "2013",
  "locator": "Table 1, type 1",
  "verification": "SECONDARY_ONLY",
  "tier": "A",
  "fdm_adjustment": "ε_allow طبق research.md §4",
  "reviewed_on": "2026-10-29"
}
```
- `source_type`: `STD | MFR_GUIDE | PEER | TDS | DERIVED | TEST | JUDGEMENT | COMMUNITY`
- `verification`: `ORIGINAL_CHECKED | SECONDARY_ONLY | UNVERIFIED`
- `tier`: A = استاندارد/استخراج چک‌شده، B = راهنمای سازنده/مقاله، C = TDS یا فقط ثانویه، D = تجربی/قضاوت

## فناوری

- **C#، .NET Framework 4.8، x64**، کتابخانه‌ی کلاس (SDK-style csproj با `net48`)
- **xCAD.NET** (`Xarial.XCad.SolidWorks`) برای Add-in، CommandManager، PropertyManager page و Macro Feature
  - قالب: `dotnet new install Xarial.XCad.Templates`
- DLLهای interop از `<SW install>\api\redist` با `Embed Interop Types = false`
- موتور قوانین در یک پروژه‌ی **جدا و بدون وابستگی به SolidWorks** تا با xUnit/NUnit تست شود

### پیش‌نیاز روی کامپیوتر
- Visual Studio 2022 Community با «.NET desktop development» و targeting pack 4.8
- SolidWorks 2025 (Professional/Premium برای Thickness Analysis)

### ساخت و ثبت (Claude Code می‌تواند اجرا کند)
```
dotnet build JointAdvisor.sln -c Release
%windir%\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /codebase JointAdvisor.dll
```
- regasm نیاز به **Administrator** دارد (ترمینال با Run as administrator).
- قبل از build، SolidWorks را ببند (DLL قفل می‌شود).
- گزینه‌ی «Register for COM interop» در VS مناسب نیست (بدون /codebase).
- برای دیباگ: Start program = `SLDWORKS.exe`.

## واقعیت‌های API (از آینه‌ی راهنمای API — روی 2025 یک بار چک شود)

- ⚠️ **Fastening Featureهای داخلی (Snap Hook، Lip/Groove، Mounting Boss، Vent) با API ساخته نمی‌شوند** — نه در `CreateDefinition`، نه متد `Insert...`، نه `RunCommand`. → **هندسه را خودمان می‌سازیم**:
  - اسکچ + `FeatureExtrusion3` / `FeatureCut4` / Sweep / Fillet
  - یا Library Feature (`.sldlfp`) با `CreateDefinition(swFmLibraryFeature)`
  - بهترین: **Macro Feature** (`InsertMacroFeature3`، با xCAD ساده‌تر) تا در درخت فیچر قابل ویرایش بماند
  - تأیید روی 2025: یک Macro ضبط کن موقع درج Lip/Groove و ببین چیزی ثبت می‌شود یا نه
- **Bodyها:** `IPartDoc.GetBodies2(swSolidBody, true)`؛ تشخیص بدنه/درب با حجم، `GetBodyBox` و موقعیت در امتداد محور باز شدن
- **سطح‌های تماس:** `IModeler.CheckInterference3(target, tool, 2|4, ...)` (۲ = شامل سطح‌های هم‌منطبق، ۴ = برگرداندن سطح‌ها)
- **سطح‌های با فاصله‌ی کم:** پیش‌فیلتر با `IFace2.GetBox` سپس `IEntity.GetDistance`
- **اعمال فیچر فقط روی یک Body:** `UseFeatScope=true, UseAutoSelect=false` و انتخاب Body با **mark 8** (`ISelectionMgr.CreateSelectData` + `IBody2.Select2`)
- **ضخامت دیواره:** `IThicknessAnalysis` از `GetAddInObject("Utilities.UtilitiesApp")` (افزونه‌ی Utilities باید فعال باشد)؛ جایگزین: `IModelDocExtension.RayIntersections` یا سطح‌های تخت روبه‌رو
- **حلقه‌ی لبه (rim):** `IFace2.GetLoops`، `ILoop2.IsOuter`
- **Lip/Groove دستی:** `SketchUseEdge3` روی لبه → `SketchOffset2` → extrude نازک روی درب (scope) → cut با لقی در بدنه (scope)
- **Part تک‌بدنه (حالت فرعی):** تشخیص پوسته (حجم ≪ جعبه‌ی محیطی، فیچر Shell، سطح لبه با حلقه‌ی داخلی) → `PreSplitBody2` / `PostSplitBody2`
- **Assembly:** `InterferenceDetectionManager` با `TreatCoincidenceAsInterference=true`؛ `ClearanceVerificationManager`
- **پیش‌نمایش:** بدنه‌ی موقت با `IModeler.CreateBodyFromBox3` و `IBody2.Display3`
- **جرم:** `IMassProperty2`
- واحدهای API همه **متر** هستند.

## ساختار پروژه

```
snapfit/
  JointAdvisor.sln
  src/
    JointAdvisor.Rules/        # بدون SolidWorks — قابل تست
      Rules/                   # rules/*.json با فیلدهای ردیابی
      Materials/               # PLA، ASA (TDS + نتایج تست کاربر)
      Calculators/             # Cantilever، Annular، Torsion، Boss، Insert، NutTrap، LipGroove
      Advisor/                 # فیلترهای قطعی + امتیازدهی + قانون ترکیب
      Report/                  # برگه‌ی محاسبات (HTML/PDF) با منابع
    JointAdvisor.SolidWorks/   # Add-in (xCAD)
      Analysis/                # Bodyها، تماس، لبه، ضخامت، جهت باز شدن، فضای آزاد
      Generators/              # ساخت هندسه‌ی هر روش (Macro Feature)
      UI/                      # CommandManager، Task Pane، PropertyManager
    JointAdvisor.TestCoupons/  # تولید نمونه‌های تست (ISO 527 A1، هوک تست، نمونه‌ی لقی)
  tests/
    JointAdvisor.Rules.Tests/  # تست با مثال‌های حل‌شده‌ی Bayer
```

## ورودی‌هایی که از کاربر پرسیده می‌شود
- تعداد باز و بسته: دائمی / گاه‌به‌گاه (<10) / مکرر
- بار: کشش، برش، ضربه/افتادن (تقریبی، N)
- آب‌بندی لازم؟ (IP هدف — با تذکر نیاز به تست IEC 60529)
- ابزار مجاز؟ (بدون ابزار / پیچ‌گوشتی)
- دمای کاری
- جنس و (اختیاری) نتیجه‌ی تست کرنش خودش

## امتیازدهی اولیه [JDG — باید در گزارش برچسب بخورد]

وزن‌ها: سیکل 0.2، بار 0.2، آب‌بندی 0.15، بدون ابزار 0.1، فضا 0.1، قابلیت چاپ 0.15، هزینه/پیچیدگی 0.1.

| روش | سیکل | بار کششی | برش | آب‌بندی | بدون ابزار | فضا | چاپ |
|---|---|---|---|---|---|---|---|
| Snap hook | 3 | 2 | 2 | 1 | 5 | 3 | 3 |
| Snap حلقوی | 3 | 3 | 3 | 2 | 5 | 2 | 3 |
| Snap پیچشی | 4 | 2 | 2 | 1 | 5 | 2 | 2 |
| Lip/Groove (فقط جاانداز) | 5 | 0 | 4 | 3 (5 با واشر) | 5 | 4 | 5 |
| Press fit | 0 | 3 | 3 | 2 | 3 | 5 | 2 |
| Dovetail | 4 | 3 | 3 | 1 | 5 | 3 | 4 |
| پیچ مستقیم (PT) | 2 | 3 | 4 | 4 | 0 | 4 | 5 |
| مهره‌ی حرارتی + پیچ | 5 | 5 | 5 | 5 | 0 | 3 | 4 |
| پیچ + مهره‌ی محبوس | 5 | 5 | 5 | 5 | 0 | 2 | 3 |
| آهنربا | 5 | 1 | 1 | 0 | 5 | 3 | 3 |

## ترتیب ساخت

1. **چک منابع:** PDF رسمی Covestro (لینک در research.md) را دانلود کن؛ موارد بخش ۸ research.md را چک کن و `verification` را به‌روز کن. هر چیزی که چک نشد `UNVERIFIED` بماند.
2. **JointAdvisor.Rules** + تست‌ها: ماشین‌حساب Cantilever را با **مثال حل‌شده‌ی Bayer** (PC/ABS، ε=2.5%) تست کن تا عدد به عدد یکی شود.
3. فیلترها + امتیازدهی + گزارش محاسبات (HTML) — قابل اجرا بدون SolidWorks.
4. Add-in خالی با xCAD: دکمه در CommandManager، ثبت با regasm، دیده شدن در SolidWorks.
5. تحلیل Part چندبدنه: لیست Bodyها، سطح‌های تماس، لبه، ضخامت، جهت باز شدن — نمایش در Task Pane.
6. Generatorها به ترتیب: Lip/Groove → Snap hook → بوس مهره‌ی حرارتی → جیب مهره → بقیه.
7. PropertyManager با پیش‌نمایش؛ پیشنهاد جهت چاپ و هشدار خمش در جهت Z.
8. نمونه‌های تست چاپی و ورود نتیجه‌ی تست کاربر.
9. Assembly و Part تک‌بدنه.
