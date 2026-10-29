# تحقیق: افزونه‌ی SolidWorks برای انتخاب و ساخت اتصال (Snap fit و ...)

> قطعه‌ها: Enclosure (جعبه یا بدنه‌ی مکانیزم)، پرینت FDM با PLA / ASA روی Elegoo Neptune 4 Plus.
> **اصل اول پروژه: هر عدد و فرمول باید منبع مهندسی قابل ردیابی داشته باشد.**

## راهنمای برچسب‌ها

| برچسب | معنی |
|---|---|
| **[V-DER]** | با استخراج از تئوری تیر/مکانیک تأیید شد |
| **[V-SEC]** | در متن منبع (از طریق نقل در نتایج جستجو) دیده شد — باید با نسخه‌ی اصلی چک شود |
| **[UNV]** | تأیید نشده — **تا چک با منبع اصلی وارد کد نشود** |
| **[JDG]** | قضاوت مهندسی / تجربی — در خروجی با برچسب «بدون پشتوانه‌ی استاندارد» نشان داده شود |

> محدودیت: PDFهای اصلی Bayer از محیط تحقیق باز نشدند. نسخه‌ی رسمی Covestro این‌جاست و **اولین کار روی کامپیوتر خودت باز کردن و چک کردن آن است**:
> https://solutions.covestro.com/-/media/covestro/solution-center/brands/downloads/imported/1556891135.pdf

---

## ۱. استانداردها و مراجع

**برای طراحی Snap fit هیچ استاندارد ISO / DIN / VDI وجود ندارد** (VDI 2019 درباره‌ی TPE است، نه snap fit). مراجع پذیرفته‌شده:

| مرجع | نوع |
|---|---|
| Bayer/Covestro, *Snap-Fit Joints for Plastics – A Design Guide* | راهنمای سازنده (اصلی‌ترین) |
| BASF, *Snap-Fit Design Manual* (جدول کرنش و اصطکاک ص IV-4) | راهنمای سازنده |
| Bonenberger, *The First Snap-Fit Handbook*, 3rd ed., Hanser 2016, ISBN 978-1-56990-595-1 | کتاب مرجع |
| Klahn, Singer, Meboldt, Procedia CIRP 50 (2016) 264–269 | مقاله‌ی snap fit در ساخت افزایشی |

استانداردهای رسمی برای بقیه‌ی بخش‌ها:

| استاندارد | کاربرد در افزونه |
|---|---|
| ISO/ASTM 52900:2021 | نام‌گذاری جهت ساخت (XY, XZ, ZX) |
| ISO/ASTM 52910:2018 | چک‌لیست بازبینی طراحی AM (عدد نمی‌دهد) |
| VDI 3405 Blatt 3.4 (2021) | قوانین هندسی طراحی برای FDM |
| ISO/ASTM 52927:2024 | ساخت و گزارش نمونه‌ی تست AM (جایگزین ISO 17296-3) |
| ISO 527-1:2019، ISO 527-2:2025 (+ ISO 20753) | مدول، کرنش تسلیم (نمونه‌ها: A1/A2) |
| ISO 178 / ASTM D790 | خمش — نزدیک‌ترین به حالت تیر snap |
| ISO 899-1/-2 | خزش (press fit، پیچ در بوس) |
| ISO 286-1/-2 | کلاس‌های انطباق |
| ISO 2768-1 | تلرانس عمومی (برای FDM فقط توصیه‌ای) |
| ISO 273 | سوراخ عبور پیچ |
| ISO 4032:2023 (M3 در Annex A) | ابعاد مهره (جیب مهره) |
| ISO 4762 | ابعاد سر پیچ آلن (کانتر بور) |
| EJOT PT / EVO PT (راهنمای سازنده) | پیچ مستقیم در پلاستیک |
| IEC 60529 | درجه‌ی IP — فقط با **تست** تأیید می‌شود، قابل محاسبه نیست |
| ISO 3601-2:2025 (بند 6.1.3) / Parker ORD 5700 | شیار O-ring |
| VDI 2230 | **برای قطعه‌ی پلاستیکی استفاده نشود** (فقط سمت پیچ فلزی) |

---

## ۲. Snap hook (تیر یک‌سرگیردار)

نمادها: `t` ضخامت ریشه، `l` طول، `b` عرض، `y` عمق گیر (undercut)، `ε` کرنش، `E_s` مدول سکانت، `μ` ضریب اصطکاک، `α` زاویه‌ی ورود، `α'` زاویه‌ی برگشت.

| فرمول | وضعیت |
|---|---|
| مقطع ثابت: `y = 0.67·ε·l²/t` ⇔ `ε = 1.5·y·t/l²` | [V-DER] |
| ضخامت مخروطی تا t/2 در نوک: `y = 1.09·ε·l²/t` | [V-SEC] Bayer Table 1 |
| عرض مخروطی تا b/4: ضریب 0.86 | [UNV] |
| نیروی خمش: `P = (b·t²/6)·(E_s·ε/l)` | [V-DER] |
| نیروی جا زدن: `W = P·(μ + tanα)/(1 − μ·tanα)` | [V-SEC] Bayer |
| نیروی جدا کردن: همان فرمول با `α'` | [V-SEC] |
| اگر `μ·tanα' ≥ 1` ⇒ قفل دائمی (جدا نمی‌شود) | [V-DER] |
| کرنش تکراری = 60% کرنش یک‌باره | [V-SEC] از مثال Bayer (نه جدول عمومی) |
| شعاع ریشه `r/t ≥ 0.5` (نمودار Bayer حدود 0.6 صاف می‌شود) | [V-SEC] ثانویه |
| `l ≥ 5t`، هدف ~`10t` | [JDG] |
| زاویه‌ی ورود 20–30°؛ برگشت 30–45° قابل باز شدن، ~90° دائمی | [V-SEC] منابع ثانویه |

## ۳. Snap حلقوی و پیچشی

| فرمول | وضعیت |
|---|---|
| حلقوی: `ε ≈ y/d`؛ `P = y·d·E_s·X` (X از نمودار Bayer: X_N یا X_W) | [V-SEC] — نمودار X باید از منبع اصلی دیجیتال شود |
| پیچشی: `γ = φ·r/l`، `γ_perm ≈ (1+ν)·ε_perm`، `G = E_s/(2(1+ν))` | [UNV] — از Bayer بخش 3.1 چک شود |

## ۴. داده‌های جنس

### کرنش مجاز Bayer (قطعه‌ی تزریقی، یک‌باره، 23°C)
| جنس | ε | وضعیت |
|---|---|---|
| PC (Makrolon) | 4.0% | [V-SEC] |
| PC/ABS (Bayblend) | 2.5% | [V-SEC] |
| ASA (Centrex) | 1.9% | [V-SEC] OCR ناقص |
| ABS (Lustran) | ~1.8% | [V-SEC] OCR ناقص |
| PA6 خشک / شرطی‌شده | 4.0% / 6.0% | [V-SEC] OCR ناقص |
| POM، PP، PBT | — | [UNV] |

### ضریب اصطکاک Bayer (پلاستیک روی فولاد؛ ضریب برای پلاستیک روی همان پلاستیک)
PTFE 0.12–0.22 · PE سخت 0.20–0.25 (×2.0) · PP 0.25–0.30 (×1.5) · POM 0.20–0.35 (×1.5) · PA 0.30–0.40 (×1.5) · PBT 0.35–0.40 · PS 0.40–0.50 (×1.2) · SAN 0.45–0.55 · PC 0.45–0.55 (×1.2) · PMMA 0.50–0.60 (×1.2) · ABS 0.50–0.65 (×1.2) — [V-SEC]
مثال Bayer: PC روی PC → `0.5 × 1.2 = 0.6`.
PLA چاپی: در جدول نیست → از ABS استفاده کن یا اندازه بگیر [JDG].

### داده‌ی فیلامنت (TDS سازنده، ISO 527 — مقدار «نمونه»، نه مقدار طراحی)
| فیلامنت | E XY / Z (MPa) | استحکام XY / Z (MPa) | کرنش XY / Z | وضعیت |
|---|---|---|---|---|
| Prusament PLA | 2300 | تسلیم 51±3 | تسلیم 2.9% | [V-SEC] — ستون «vertical» آن XZ است نه Z |
| PolyLite PLA V5.4 | 3427 / 3065 | 52.3 / 40.5 | 6.3% / 1.8% | [V-SEC] |
| PolyLite ASA V5.4 | 2379 / 1965 | 43.8 / 32 | 6.7% / 1.65% | [V-SEC] — نسخه‌ی TDS ثبت شود |

### ناهمسانی FDM (anisotropy)
- ABS چاپی: استحکام کششی 65–72% نسخه‌ی تزریقی — Ahn et al., Rapid Prototyping J. 8(4) 2002 [V-SEC]
- کاهش 50–75% استحکام در جهت Z رایج است — مرور PMC6414919 [V-SEC]
- برای ASA مقاله‌ی داوری‌شده درباره‌ی ناهمسانی پیدا نشد.

### قانون اصلی برای پرینت (از ISO/ASTM 52910 و VDI 3405-3.4 + داده‌های بالا)
**تیر snap باید در صفحه‌ی XY خم شود (لایه‌ها در امتداد طول تیر).** اگر خمش از روی لایه‌ها (Z) بگذرد: کرنش Z (~1.6–1.8%) با کاهش شدید، یا طراحی رد شود و جهت چاپ دیگری پیشنهاد شود.

**دام رایج Enclosure:** هوکی که ادامه‌ی دیواره‌ی جعبه به سمت بالاست و جعبه دهانه‌رو‌به‌بالا چاپ می‌شود، از روی لایه‌ها خم می‌شود → راه‌حل‌ها به ترتیب: هوکی که در XY خم شود، چاپ درب به پهلو، کلیپ جداگانه.

### کرنش مجاز برای FDM
```
ε_allow = min( ε_ref × k_orient × k_rep / SF ,  ε_Bayer(رزین معادل) )
```
- `ε_ref`: کرنش تسلیم **اندازه‌گیری‌شده** روی نمونه‌ی چاپ‌شده با تنظیمات خودت (ISO 527 / ISO 178)؛ تا قبل از تست: TDS
- `k_rep = 0.6` برای باز و بسته‌ی مکرر (Bayer)
- `k_orient = 1` در XY؛ در غیر این صورت نسبت کرنش Z/XY
- `SF ≥ 1.5` [JDG]
- سقف: مقدار Bayer برای رزین تزریقی معادل (ASA 1.9%، ABS ~1.8%)
- PLA: Tg ≈ 55–60°C → بالای ~40°C برای press fit و پیچ هشدار خزش (ISO 899)

---

## ۵. اتصالات دیگر

| روش | قانون | منبع / وضعیت |
|---|---|---|
| پیچ PT در پلاستیک | سوراخ 0.80·d، OD بوس 2.0·d، درگیری 2.0·d، کانتر بور لازم | EJOT PT (ABS، ABS/PC) [V-SEC] |
| پیچ EVO PT | سوراخ 0.85·d ± 0.05، کانتر بور 1.05·d، OD ‏2·d، عمق ≥ 2·d | EJOT EVO PT [V-SEC] — فقط پیچ PT، نه ST طبق ISO 1478 |
| سوراخ عبور M3 | 3.2 / 3.4 / 3.6 (fine/medium/coarse) | ISO 273 [V-SEC] |
| مهره‌ی M3 | s = 5.5 max (5.32 min)، m = 2.4 max (2.15 min) | ISO 4032:2023 Annex A [V-SEC] |
| مهره‌ی حرارتی M3 | **از دیتاشیت همان مهره**؛ مثلاً Ricoh: سوراخ 4.1، بوس ≥ 7.4؛ CNC Kitchen: سوراخ 4.0، دیواره ≥ 1.6 | دیتاشیت سازنده — استاندارد ندارد |
| O-ring | از جدول‌های ISO 3601-2:2025 بند 6.1.3 / Parker Chart 4-3 (نه یک درصد ثابت) | [UNV] تا چک جدول |
| Lip/Groove، Dovetail، آهنربا | استاندارد ندارند → انطباق ISO 286 + نمونه‌ی لقی چاپی | [JDG] + تست |
| Living hinge | با PLA/ASA توصیه نمی‌شود (PETG < 900 سیکل) | [V-SEC] Hubs، UT Austin |

استحکام بیرون‌کشیدن M3 در PLA (CNC Kitchen): مهره‌ی حرارتی خوب ~157–181 kg؛ سوراخ کوچک 2.7mm → 39 kg [V-SEC].

---

## ۶. انتخاب نوع اتصال

### مرحله‌ی الف — فیلترهای قطعی (از قوانین منابع بالا)
- آب‌بندی لازم → فقط Lip/Groove + واشر/O-ring همراه با پیچ؛ snap تنها کافی نیست
- باز و بسته‌ی مکرر → press fit، پیچ مستقیم در پلاستیک و living hinge حذف؛ snap با `k_rep`
- کرنش لازم snap > `ε_allow` → snap رد (یا تیر بلندتر / جهت چاپ دیگر)
- ضخامت یا فضای موضعی کمتر از ابعاد بوس/مهره‌ی حرارتی (از دیتاشیت) → آن روش حذف
- جهت جا زدن باید جهت آزاد جدا شدن دو قطعه باشد
- دمای کاری بالا با PLA → هشدار خزش

### مرحله‌ی ب — امتیازدهی [JDG]
امتیازها و وزن‌ها قضاوت مهندسی‌اند و باید در گزارش با برچسب «بدون پشتوانه‌ی استاندارد» نشان داده شوند. (جدول اولیه در `build-plan.md`.)

### قانون ترکیب
همیشه یک روش «جاانداز» (Lip/Groove یا Dovetail) + یک روش «نگه‌دارنده» (snap، پیچ، ...).

---

## ۷. پروژه‌های موجود

- هیچ ابزاری پیدا نشد که **نوع اتصال را خودکار پیشنهاد دهد** — این بخش کار جدید است.
- کتابخانه‌ها: [BOSL2](https://github.com/BelfrySCAD/BOSL2) (joiners.scad)، [SnapFit_Calculator](https://github.com/Mechanical-Python/SnapFit_Calculator)
- SolidWorks API: [xCAD.NET](https://github.com/xarial/xcad)، [codestack](https://github.com/xarial/codestack)، [SolidDNA](https://github.com/CAD-Booster/SolidDNA)، [آینه‌ی راهنمای API](https://github.com/kilwizac/solidworks-api-mcp)
- Fusion 360: [Fusion360SnapFitGenerator](https://github.com/dwragon/Fusion360SnapFitGenerator)

### ویدیوهای یوتوب (منبع تجربی — سطح D، برای ایده‌ی طراحی، نه عدد)

> زیرنویس ۱۰ ویدیو خوانده شد (نتایج در بخش بعد). بقیه را یوتوب از سرور ابری با «bot check» مسدود کرد — Claude Code روی کامپیوتر کاربر می‌تواند با `yt-dlp --write-auto-subs --skip-download --cookies-from-browser chrome` بقیه را بخواند.

#### نکات استخراج‌شده از زیرنویس‌ها [سطح D — تجربی؛ هر جا با فرمول/راهنما می‌خواند ذکر شده]

| # | نکته | ویدیو @ زمان | ارتباط با قوانین |
|---|---|---|---|
| 1 | هوک عمودی (در Z) از روی خط لایه **ترد می‌شکند**؛ هوک خوابیده (XY) **تغییر شکل پلاستیک** می‌دهد ولی نمی‌شکند | Send to Print @01:14–02:37؛ Forerunner @00:33–01:53 | تأیید قانون جهت چاپ §4 |
| 2 | اگر مجبوری عمودی چاپ کنی، بزرگ‌ترین شعاع ممکن در ریشه — «باز هم دیر یا زود می‌شکند» | Forerunner @01:26 | → Advisor در این حالت هشدار قطعی بدهد |
| 3 | دو برابر کردن طول هوک (5→10 mm) تنش را ~75% کم کرد | Ultimate Tool Changer @00:00–00:26 | **با `ε = 1.5·y·t/l²` دقیقاً می‌خواند** (ε ∝ 1/l²) |
| 4 | کم کردن undercut (4→1 mm) شکست را حل کرد، ولی گیر ضعیف شد | Ultimate Tool Changer @00:41 | ε ∝ y |
| 5 | هوک 0.5 mm شکست چون اسلایسر دور پیوسته نساخت؛ قطعه‌ی تزریقی با همان ضخامت سالم می‌ماند | Ultimate Tool Changer @01:17 | قانون FDM: `t ≥ 2–3 × عرض خط` (≥ ~1.2 mm) |
| 6 | شعاع ریشه ≥ 0.5·t؛ مخروطی کردن تیر برای پخش تنش | Rapid Direct @04:16 | **با Bayer می‌خواند** |
| 7 | پروفیل «فلشی»: زاویه‌ی ورود کم، زاویه‌ی برگشت تند → جا زدن نرم، گیر محکم | Send to Print @03:51–04:43 | با `W = P·(μ+tanα)/(1−μ·tanα)` می‌خواند |
| 8 | پخ ورودی روی **سوراخ/جای گیر** مثل قیف، نیاز به هم‌راستایی دقیق را حذف می‌کند | Send to Print @04:43 | Generator: پخ خودکار روی قطعه‌ی مقابل |
| 9 | پخ لبه‌های پایین برای جلوگیری از elephant's foot | Send to Print @03:01 | Generator |
| 10 | زبانه/lug جاانداز بگذار تا نیروی برشی از روی کلیپ‌ها برداشته شود | Rapid Direct @04:45 | با قانون ترکیب §6 می‌خواند |
| 11 | هوک فقط **حین جا زدن** خم شود، نه در حالت بسته (بدون پیش‌بار) | Rapid Direct @04:45 | خزش (ISO 899) → قانون: تغییر شکل باقی‌مانده در حالت بسته = 0 |
| 12 | snap حلقوی: «بیشتر هنر تا علم» — چند نسخه‌ی آزمایشی چاپ کن؛ نیروی جا زدن زیاد است، فیکسچر/پرس بساز | Forerunner @07:05–08:24 | → نمونه‌ی تست؛ هشدار نیروی W |
| 13 | لقی FDM به **پرینتر، تنظیمات و فیلامنت** بستگی دارد: 0.2 mm روی یک پرینتر آزاد، روی دیگری 0.3–0.5؛ جوش خوردن در محل شروع/پایان دور (seam) | Maker's Muse @01:44–05:28 | → لقی از نمونه‌ی تست کاربر، نه عدد ثابت |
| 14 | زبانه‌ی بدون ساپورت: پخ 45° + حدود 1 mm بخش صاف در نوک (نوک تیز بد چاپ می‌شود) | Joseph Willis @05:05–06:07 | Generator |
| 15 | قفل پیچشی (twist-lock): شیار 25° برای زبانه‌ی 20° (لقی)، لقی 0.1–0.2 mm، فیلت 1 mm، برآمدگی گیر Ø1 mm | Joseph Willis @06:38–13:01 | الگوی Generator برای قطعه‌ی گرد |
| 16 | Enclosure جعبه‌ای: لبه = نصف ضخامت دیواره، لقی 0.2 mm، درب 1 mm بیرون‌زده، کلیپ‌ها قرینه روی دو ضلع بلند | HyperMakx (Fusion) | الگوی اولیه‌ی Lip/Groove (لقی از تست) |
| 17 | Enclosure دور مکانیزم متحرک: Assembly را Save as Part (چندبدنه)، بدنه‌های متحرک را در کل محدوده‌ی حرکت Pattern کن، دور آن اسکچ بزن | GoEngineer @00:00–02:56 | **ایده برای افزونه:** چک لقی با پوش حرکت مکانیزم |

#### Slant 3D و منابع مکتوبِ مبتنی بر ویدیوهایش [سطح D]

زیرنویس ویدیوهای Slant 3D از سرور ابری قابل دریافت نبود (bot check). منابع زیر **خلاصه‌ی مکتوب** یا راهنمای مبتنی بر همان ویدیوها هستند:

| # | نکته | منبع | ارتباط |
|---|---|---|---|
| 18 | لقی به رنگ، جنس، نوع/جهت infill، رزولوشن لایه، نازل و پرینتر بستگی دارد → **راه‌حل در طراحی است، نه تنظیمات** | Slant 3D، [Perfect Tolerance](https://www.youtube.com/watch?v=XKrDUnZCmQQ) (via [یادداشت از زیرنویس](https://weavingwords.pages.dev/notes/2026-05-21_how-to-design-a-print-with-perfect-tolerance-every-time/)) | تأیید #13 |
| 19 | لبه‌های بیرونی گرد (گوشه‌ی تیز = تغییر جهت ناگهانی نازل = خطای ابعادی؛ دیواره‌ی صاف دقیق‌ترین سطح است)؛ پخ پایین؛ گوشه‌ی داخلی حفره گرد | همان | Generator |
| 20 | لبه‌ی جلوی درب زاویه‌دار (گُوه) تا همیشه بتواند وارد شود | همان | با #8 |
| 21 | دیواره‌ی نازک (فقط perimeter) به‌جای infill توپر در سطح‌های جفت‌شونده — ابعاد قابل پیش‌بینی‌تر | همان | Generator / توصیه‌ی اسلایس |
| 22 | فقط **چهار گوشه** یا فقط **دیواره‌های صاف** تماس داشته باشند؛ در جای گیر، گوشه‌ها را خالی کن | همان | Lip/Groove Generator |
| 23 | **Compliant features:** فاصله‌ی زیر بخش انعطاف‌پذیر **حداقل 0.3 mm، حداکثر ~0.5 mm** (کمتر: اسلایسر آن را می‌بندد؛ بیشتر: هندسه تغییر شکل می‌دهد) | همان | قانون عددی Generator (سطح D، با نمونه‌ی تست) |
| 24 | فنر U شکل («thumb») که به دیواره فشار می‌آورد + جاانداز مربعی پایین | همان | الگوی درب compliant |
| 25 | شکاف در گوشه‌های جای گیر برای کمی باز شدن — **موازی لایه‌هاست، خطر جدا شدن لایه**؛ فقط به‌عنوان حاشیه‌ی اطمینان کوچک | همان | هشدار جهت لایه |
| 26 | **Grip fins:** آرایه‌ای از انگشتی‌های انعطاف‌پذیر روی دیواره‌ی داخلی؛ تغییر شکل کم در هر فین → خزش کم؛ نیروی جا زدن/درآوردن مستقل از پرینتر و تنظیمات — «قابل‌اعتمادترین» | همان | روش جدید برای Advisor |
| 27 | لقی بین فین‌های snap و سوراخ: **0.4 mm** تعادل خوب بین راحتی جا زدن و سفتی | [OpenAT Design Guide](https://makersmakingchange.github.io/OpenAT_Design_Guide/Design_Elements_For_3D_Printed_Parts/Snap_Fits.html) (CC BY-SA، مبتنی بر Slant 3D [Joining Features](https://www.youtube.com/watch?v=RTQjvYENR7w)) | مقدار اولیه، با نمونه‌ی تست |
| 28 | تب‌ها نباید هم‌صفحه با لایه‌ها خم شوند؛ overhang تب ≥ 45° از افق؛ تب را به بستر نرسان (لایه‌ی اول پیچیده) | همان | تأیید #1 و قانون overhang |
| 29 | قلاب «خاری» (barb) = دائمی؛ زاویه در هر دو طرف = قابل جدا شدن | همان | با زاویه‌ی برگشت §2 |
| 30 | کرنش طراحی ≈ **10–15% ازدیاد طول در شکست** (PLA ~8%، ABS ~10%، PETG ~24%، نایلون ~100%) | Engineers Grow / Ultimate Tool Changer via [Hackaday](https://hackaday.com/2022/11/11/oh-snap-3d-printing-snapping-parts-without-breakage/) | برای PLA → 0.8–1.2% — **محافظه‌کارانه‌تر** از روش §4؛ فقط برای مقایسه |
| 31 | PLA زیر بار دائم (مثلاً کلیپ زیر آب) ظرف یک روز تغییر شکل دائمی داد | نظر کاربر در همان صفحه‌ی Hackaday | تأیید قانون #11 (بدون پیش‌بار) و هشدار خزش |
| 32 | snapهای دوطرفه‌ی معمولی تنش را روی مرز لایه متمرکز می‌کنند → **snap چهارطرفه** | Slant 3D «Avoid Vertical Breaks with 4 Way Snaps» (فقط عنوان، از نتایج جستجو) | باید دیده شود |

**فهرست تکنیک‌های اتصال Slant 3D** (از فصل‌بندی ویدیوها — محتوا خوانده نشد): پین الماسی، slab & slot کم‌ارتفاع، snap با S-bracket و C-clamp، tongue & slot ساده / T / I با grip fins، تب قفل دوطرفه، شیار چسب، پین افقی و عمودی، پین/شیار صلیبی، fins برای حذف overhang، fins انعطاف‌پذیر برای لقی، micro-features برای پین عمودی محکم. — [Ultimate Guide to Connecting 3D Printed Parts](https://www.youtube.com/@slant3d) و [Joining Features](https://www.youtube.com/watch?v=RTQjvYENR7w)

**ویدیوهایی که کاربر فرستاد و هنوز خوانده نشده‌اند** (عنوان از oEmbed یوتوب):
- [6 Ways To Make Snap Fits for 3D Printing](https://youtube.com/watch?v=rsfZgT3ZEI8) — Slant 3D
- [Design Compliant Lids for Perfect Tolerance Every Time (Lids Vol. 2)](https://youtube.com/watch?v=IZKh6lo9SP4) — Slant 3D
- [Snap Fit Tinkercad Sketch Tool Dove Tail](https://youtube.com/watch?v=eF9v8q6XakA) — HL ModTech
- [Design Snap Fits for Mass Production 3D Printing](https://youtube.com/watch?v=6DkCCOc5O1Y) — Slant 3D
- کانال: [@slant3d](https://youtube.com/@slant3d)

→ روی کامپیوتر کاربر: `yt-dlp --skip-download --write-auto-subs --sub-langs en <URL>` (از اینترنت خانگی معمولاً bot check نمی‌خورد).

**ترفندهای طراحی برای FDM** (مرتبط با Generatorها):
- [SECRET Revealed to Design SNAP FIT JOINTS with 3D Printing](https://www.youtube.com/watch?v=wl6TDwBqkgs) — جلوگیری از شکستن هوک
- [SNAPS that CLICK in and NEVER BREAK with 3D Printing!](https://youtube.com/watch?v=-jgbd8RUhhY) — وقتی هوک می‌شکند چه کنیم
- [How to Design a Print with Perfect Tolerance EVERY Time](https://m.youtube.com/watch?v=XKrDUnZCmQQ) — press fit، snap fit، گوشه‌ی گرد، پخ، compliant features، grip fins (Geometry Media / Slant 3D)
- [Design Snap Fits for Mass Production 3D Printing](https://www.youtube.com/watch?v=6DkCCOc5O1Y)
- [Designing Snap Closures For 3D Printed Parts](https://www.youtube.com/watch?v=m_-d8xcSDQs)
- [How to Design a Stronger Snap-Fit Pin for 3D Printing](https://www.youtube.com/watch?v=wXB3VfBBcdU) — پین snap برای اتصال چرخشی
- [3D Printing Snap Fits for Beginners](https://www.youtube.com/watch?v=wv6idwuD7k8)
- [How to Design Snap Fits, Interlocking Features, and More for SLS](https://www.youtube.com/watch?v=uECIGfCyPSI)
- [Maker's Muse Tolerance Test](https://www.youtube.com/watch?v=TYuLVN3YHw8) — ایده‌ی نمونه‌ی تست لقی

**SolidWorks** (برای توسعه‌دهنده، دیدن روش دستی که افزونه باید خودکار کند):
- [Fastening Features — Mounting Boss, Vent, Snap Hook, Lip/Groove](https://www.youtube.com/watch?v=S-YHxPdqeP0)
- [How to Create a Snap Hook in SolidWorks](https://youtube.com/watch?v=X94TKUNi0oE)
- [SNAP BOX SERIES (lid)](https://www.youtube.com/watch?v=KulqI6Evi1I)
- [Snap-fit fan guard in SOLIDWORKS](https://www.youtube.com/watch?v=2OU0arYbTMQ)
- [Enclosure Design Around Moving Parts](https://www.youtube.com/watch?v=CuzPIiyWUj8) — مرتبط با Enclosure مکانیزم
- [Twist-Snap Design Tutorial](https://www.youtube.com/watch?v=75uswjVayrs) — snap پیچشی

**Fusion 360** (ایده‌ی گردش کار Enclosure):
- [Snap 3D prints together with cantilever joint](https://www.youtube.com/watch?v=mrOPCyK12k0) — به راهنمای snap joint MIT ارجاع می‌دهد
- [Design Snap-Fit Enclosures with Ease](https://www.youtube.com/watch?v=nhoU-SZvKKA)
- [Snap Fit Joint — Raspberry Pi case](https://www.youtube.com/watch?v=dahn-9FePeM)
- [Playlist: Design 3D Printed Snap Fit Joints](https://www.youtube.com/playlist?list=PLrZ2zKOtC_-B40OCy15MRRXtsBTjgVR44)

**مقدماتی:** [Plastic Parts Design: What Is Snap Fit?](https://www.youtube.com/watch?v=GYVBIZJ2AMI) — انواع، مزایا/معایب، best practices.

نکته‌ای که از نتایج جستجو (نقل از Bayer) تأیید شد: زاویه‌ی برگشت 0–60° قابل جدا شدن، 60–90° عملاً غیرقابل جدا شدن (مگر با دکمه/زبانه‌ی آزادکننده یا شکاف ابزار)؛ زاویه‌ی ورود معمولاً 15–30° و بیش از ~45° نه. [V-SEC]

⚠️ یک متن پتنت فرمول `f = ε·L²/(3h)` را نقل کرده که با استخراج ما (`0.67·ε·L²/h = 2εL²/(3h)`) نمی‌خواند — احتمالاً خطای استخراج یا تعریف متفاوت؛ **استفاده نشود**.

## ۸. قبل از انتشار باید با منبع اصلی چک شود

1. Bayer Table 1 (ضریب 0.86 و بقیه‌ی مقاطع)
2. Bayer جدول کرنش مجاز (POM، PP، PBT، و اعداد OCR‌شده‌ی ASA/ABS/PA)
3. فرمول‌های snap پیچشی و نمودار X حلقوی
4. نمودار تمرکز تنش ریشه
5. جدول‌های O-ring در ISO 3601-2:2025
6. جدول کامل ISO 273
