# منابع وب: سایت‌های پرینت سه‌بعدی و قوانین اتصال

> مکمل `research.md`. جمع‌آوری 2026-10-29.
> کیفیت منبع: **A** = داده‌ی تست‌شده/راهنمای مرجع، **B** = راهنمای معتبر، **C** = بلاگ/جامعه.
> در سیستم سطح‌بندی افزونه (`build-plan.md`): A ≈ tier B، B ≈ tier C، C ≈ tier D. هیچ‌کدام «استاندارد» نیستند.
> در دسترس نبودند: All3DP، Sculpteo، Printables/MakerWorld (403)، Xometry (429)، PDFهای اصلی Stratasys (403؛ از نسخه‌ی ژاپن و آینه‌ی دانشگاهی استفاده شد).

## ۱. فهرست سایت‌ها

| سایت | صفحه‌های مرتبط | به درد چه می‌خورد | Q |
|---|---|---|---|
| CNC Kitchen | [insert datasheets wrong?](https://cnckitchen.com/blog/are-our-heat-set-insert-datasheets-wrong)، [tips for heat-set inserts](https://cnckitchen.com/blog/tips-and-tricks-for-heat-set-inserts)، [cheap vs expensive](https://www.cnckitchen.com/blog/threaded-inserts-for-3d-prints-cheap-vs-expensive)، [helicoils/inserts/nuts strength](https://cnckitchen.com/blog/helicoils-threaded-insets-and-embedded-nuts-in-3d-prints-strength-amp-strength-assessment) | جدول سوراخ مهره‌ی حرارتی، تست بیرون‌کشیدن و گشتاور | A |
| Bayer guide (نسخه‌ی MIT) | [Plastic_Snap_fit_design.pdf](https://fab.cba.mit.edu/classes/S62.12/people/vernelle.noel/Plastic_Snap_fit_design.pdf) | معادلات snap و کرنش مجاز | A |
| Ricoh 3D | [threaded inserts guide](https://www.ricoh-europe.com/media/ricoh-3d_threaded-inserts-guide_tcm100-115105.pdf) | جدول سوراخ و بوس مهره‌ی حرارتی | A |
| SPIROL | [inserts for 3D printed assemblies](https://www.spirol.com/assets/files/inserts-for-3d-printed-assemblies-us.pdf) | تست مهره‌ی حرارتی بر حسب دیواره و infill | A |
| Stratasys / GrabCAD | [FDM best practice assemblies](https://www.stratasys.co.jp/)، [FDM design guidelines](https://grabcad.com/tutorials/fused-deposition-modeling-fdm-design-guidelines)، [inserting hardware](https://print.grabcad.com/tutorials/inserting-hardware-post-build) | جدول لقی print-in-place، مهره‌ی حرارتی | A/B |
| UT Austin (SFF 2016) | [Balderrama-Armendariz](https://utw10945.utweb.utexas.edu/sites/default/files/2016/188-Balderrama-Armendariz.pdf) | تست سیکل لولای زنده | A |
| OpenAT Design Guide | [صفحه‌ی اصلی](https://makersmakingchange.github.io/OpenAT_Design_Guide/) — Snap Fits، Twist Lock، Screw Posts، Cotter Pins، Capturing a PCB، Threads، Battery Covers، Captured Buttons، M3 Nut | ابعاد Enclosure آزموده در محصول واقعی (CC BY-SA) | B+ |
| Hubs (Protolabs Network) | [snap-fit](https://www.hubs.com/knowledge-base/how-design-snap-fit-joints-3d-printing/)، [enclosure guide](https://www.hubs.com/knowledge-base/enclosure-design-3d-printing-extensive-guide/)، [living hinges](https://www.hubs.com/knowledge-base/how-design-living-hinges-3d-printing/)، [threaded fasteners](https://www.hubs.com/knowledge-base/how-assemble-3d-printed-parts-threaded-fasteners/) | snap، Enclosure، لولا، مهره | B |
| Fictiv | [snap-fit components](https://www.fictiv.com/articles/how-to-design-snap-fit-components) | جدول کرنش، انطباق | B |
| Formlabs | [snap-fit enclosures](https://formlabs.com/blog/designing-3d-printed-snap-fit-enclosures/) | قوانین snap، کاهش Z | B |
| Hydra Research | [design rules](https://www.hydraresearch3d.com/design-rules) | قوانین خلاصه‌ی FFF | B |
| Markforged | [heat-set inserts](https://markforged.com/blog/heat-set-inserts) | روش حفره‌ی مهره‌ی حرارتی | B |
| Prusa KB | [modeling with 3D printing in mind](https://help.prusa3d.com/article/modeling-with-3d-printing-in-mind_164135) | لقی، دیواره | B |
| Bambu wiki | [XY hole compensation](https://wiki.bambulab.com/en/software/bambu-studio/xy-hole-contour-compensation)، [shrinkage](https://wiki.bambulab.com/en/knowledge-sharing/3d-prints-shrinkage) | جبران سوراخ | B |
| MIT CBA | [3D printing group report](https://fab.cba.mit.edu/classes/863.20/CBA/people/group/reports/3d.html) | لقی print-in-place اندازه‌گیری‌شده | B |
| Rahix | [design for 3D printing](https://blog.rahix.de/design-for-3d-printing/) | crush rib، سوراخ، پیچ | B |
| LBL | [part interfaces](https://3dprinting.lbl.gov/3d-printing-knowledge-base/part-interfaces) | تست سوراخ مهره‌ی حرارتی | B |
| UZH / Protolabs | Design-Guideline-FDM (amf.uzh.ch)، [protolabs FDM](https://www.protolabs.com/services/3d-printing/fused-deposition-modeling/) | حداقل ابعاد | B |
| Slant 3D | بخش ۲ پایین | قوانین طراحی برای تولید انبوه | B |
| Hackaday | [Oh Snap!](https://hackaday.com/2022/11/11/oh-snap-3d-printing-snapping-parts-without-breakage/) (Engineers Grow)، crush ribs | نسبت کرنش، crush rib | C |
| Instructables | [3D printed snap-fits](https://www.instructables.com/3D-printed-Snapfits/) | نسبت خمش | C |
| Wevolver / Unionfab / Qidi / Craftcloud | [wevolver](https://www.wevolver.com/article/how-to-3d-print-snap-fit-joints)، [unionfab](https://www.unionfab.com/blog/2025/06/3d-print-snap-fit)، [qidi](https://qidi3d.com/blogs/news/how-to-3d-print-interlocking-parts-and-assemblies)، craftcloud | جدول لقی (بدون داده‌ی تست) | C |

Teaching Tech، Ellis، UltiMaker، Simplify3D، MatterHackers، Polymaker: محتوای کالیبراسیون دارند ولی عدد اتصال ندارند (برای پروژه‌ی اسلایسر مفیدند).

## ۲. Slant 3D

سایت جدید slant3d.com (۲۶ پست) تقریباً **هیچ قانون مکتوبی برای اتصال ندارد**؛ پست‌های ویدیویی فقط توضیح و فصل‌بندی دارند. راهنماهای قدیمی (/design-guide، /resources، /learn) حذف شده‌اند (404). قوانین عددی از slantpod.com (سایت چاپ سفارشی Slant 3D) و کد ابزارهای create.slant3d.com آمده:

| موضوع | قانون | منبع |
|---|---|---|
| تلرانس عمومی | ±0.5% اندازه، **حداقل ±0.5 mm** | [How to design for Teleport](https://www.slantpod.com/post/how-to-design-for-teleport) #10 |
| لقی قطعه‌های متحرک/متصل | **حداقل 0.5 mm** | همان #7 |
| جای تنگ (سوراخ) | به‌جای لقی کم، **compliant feature** (grip fin / flexure) — بدون عدد | همان #7 |
| پین و سوراخ | سوراخ ≥ Ø2، پین ≥ Ø3، کوچک‌ترین جزء 2 mm | همان #6، #8، #9 |
| دیواره | حداقل 0.8 mm (توصیه ≥ 1 mm) | همان #1–2 |
| overhang | حداکثر 45° بدون ساپورت | همان #3 |
| پل | حداکثر 10 mm | همان #5 |
| متن | عرض ≥ 0.6 mm، ارتفاع ≥ 2 mm؛ نه روی کف | همان #4 |
| لبه‌ها | همه‌ی لبه‌های **عمودی** فیلت؛ به‌جای overhang افقی پخ؛ پخ کف | همان #2–4 |
| سوراخ پیچ (ابزار Enclosure) | M2: 2.2، **M3: 3.2**، M5: 5.3، M6: 6.4 mm | create.slant3d.com/tools/enclosure (کد) |
| درب (ابزار Enclosure) | دیواره 4 mm، شعاع گوشه 4.5، لبه‌ی درب **دقیقاً هم‌اندازه‌ی حفره (لقی 0)**؛ دور پست‌ها 0.25 mm هر طرف | همان — ثابت‌های کد، نه قانون منتشرشده |
| جنس | PLA، PETG، CF-PETG، OPM (PCTG، Tg 80°C) — **ASA چاپ نمی‌کنند** | slant3d.com/faq |

تضاد با قوانین فعلی: لقی 0.3–0.4 mm (از یادداشت ویدیو و OpenAT) کمتر از حداقل مکتوب Slant (0.5 mm) است؛ ولی راه‌حل خود Slant برای جای تنگ compliant feature است نه عدد لقی. ابزار Enclosure خودشان لقی 0 تا 0.25 به کار برده.

## ۳. قوانین عددی بر اساس موضوع

### لقی و سوراخ
| قانون | منبع | Q |
|---|---|---|
| سوراخ چاپی 0.25 mm کوچک‌تر (Prusa CORE One L، PLA) و 0.1 mm (MK2.5) | CNC Kitchen | A |
| XY hole compensation را با گام 0.1 mm تنظیم کن؛ جبران خودکار دایره فقط برای دایره‌ی افقی ≤ 50 mm؛ فیلامنت خشک لق‌تر چاپ می‌کند | Bambu wiki | B |
| سوراخ افقی: قطره‌ای 90° یا سقف صاف 0.4 mm بالای دایره؛ هر سطح ±0.1 mm | Rahix | B |
| سوراخ افقی هشت‌ضلعی؛ overhang ≥ 45° | OpenAT | B |
| پخ کف ~0.3 mm؛ سوراخ ≥ Ø2؛ پل < 10 mm؛ overhang < 50° | Hydra | B |
| print-in-place: لقی XY ≥ یک عرض خط (~0.45 برای نازل 0.4)، لقی Z ≥ یک لایه | Stratasys | A |
| print-in-place: 0.1–0.3 تست شد؛ > 0.2 کار می‌کند | MIT CBA | B |

### Enclosure
| قانون | منبع | Q |
|---|---|---|
| دیواره ≥ 2 mm؛ 0.5 mm دور قطعات داخلی؛ سوراخ عبور +0.25 Ø؛ سوراخ پیچ‌خور −0.25 Ø؛ lug ≥ 5 mm عرض؛ rib ‏75–80% دیواره | Hubs | B |
| فاصله‌ی PCB تا دیواره 1.5–2.0 mm؛ پورت +2.0 mm دورتادور؛ lug عمق 3 mm | Formlabs | B |

### Snap hook
| قانون | منبع | Q |
|---|---|---|
| `y = 0.67·ε·l²/h`؛ مخروطی تا h/2: `1.09`؛ تکراری = 60% یک‌باره؛ PC 4%، PC/ABS 2.5%؛ پیچشی `γ ≈ 1.35·ε`؛ µ ABS 0.50–0.65 | Bayer (نسخه‌ی MIT) | A |
| کرنش PLA 4–8%، ABS 7%؛ هوک ساخته‌شده در Z: کرنش ÷2؛ زاویه‌ی برگشت 90° = دائمی | Fictiv، Formlabs | B |
| فیلت ریشه ≥ 0.5·t؛ عرض ≥ 5 mm؛ t ≥ 1 mm؛ undercut ≥ 1 mm؛ لقی FDM 0.5؛ مخروطی؛ lug | Hubs | B |
| لقی فین تا سوراخ 0.4؛ overhang بازو ≥ 45° | OpenAT | B |
| کلیپ PCB: ضخامت ≈ ¼ ارتفاع بازو، طول 6–13 mm، زاویه‌ی ورود ≥ 70° | OpenAT | B |
| خمش:طول ≈ 1:8؛ infill 100% در ناحیه‌ی snap | Instructables | C |

### قفل پیچشی، پین، دکمه
| قانون | منبع | Q |
|---|---|---|
| Twist lock: ۲ تا ۴ تب، هر کدام ≥ 3 mm عرض × ≥ 1.2 mm ارتفاع؛ برآمدگی گیر 0.4–1 mm روی وجه کناری | OpenAT | B |
| Cotter pin: مقطع هشت‌ضلعی ≥ Ø2؛ دم ≥ 45° | OpenAT | B |
| دکمه‌ی محبوس: لقی 0.4–0.8؛ اهرم 2.4–6 mm عرض، ≥ 6 mm طول، روی بستر چاپ شود | OpenAT | B |

### لولای زنده
| قانون | منبع | Q |
|---|---|---|
| تست تا شکست: **PLA ‏163 سیکل**، نایلون 199، PETG 857، PP > 1 میلیون، TPU > 2 میلیون؛ بهترین با raster 0° | UT Austin | A |
| FDM: 0.4–0.6 mm، ≥ 2 لایه، ~25 سیکل | Hubs | B |
→ برای PLA/ASA فقط نمونه‌ی اولیه.

### مهره‌ی حرارتی (Heat-set insert)
| قانون | منبع | Q |
|---|---|---|
| **قطر واقعی سوراخ:** M2×3: 3.2 · M2.5×4: 4.0 · **M3×5.7 / M3×3: 4.0** · M3×5×4 (Voron): 4.4 · M4: 5.7 · M5: 6.5 · M6: 8.1 · M8: 9.7 · M10: 12.0. حداقل دیواره: 1.3/1.6/1.6/1.6/2.1/2.6/3.3/4.5/6.0. عمق ≥ L+1 mm؛ سوراخ صاف، بدون پخ | CNC Kitchen | A |
| M3 در PLA: حداکثر ~1400 N. سوراخ 4.2 در CAD (≈ 4.0 واقعی) → ~90% حداکثر بدون پلیسه؛ بالای 4.1–4.2 واقعی استحکام شدیداً افت می‌کند. **در CAD ‏0.2–0.3 mm اضافه کن** | CNC Kitchen | A |
| نصب: دمای هویه = دمای چاپ +10–20°C (PLA ‏225، PETG ‏245، ABS ‏265)؛ 90% را ذوب کن، بقیه را فشار بده | CNC Kitchen | A |
| بیرون‌کشیدن: Ruthex 181 kg، eBay 157 kg، ارزان 39 kg؛ همه 3–4 Nm تحمل کردند | CNC Kitchen | A |
| M3: سوراخ 4.0 / بوس 7.4 / دیواره 1.7 · M4: 5.6/10.9/2.5 · M5: 6.4/12.2/2.85 · M6: 8/14.6/3.2؛ عمق L+5 mm | Ricoh | A |
| بوس ≥ 1.5× قطر آج (کامل در 2×)؛ infill > 50% (استحکام خطی با infill)؛ FDM ‏70–80% قطعه‌ی تزریقی | SPIROL | A |

### پیچ مستقیم (Self-tapping)
| قانون | منبع | Q |
|---|---|---|
| M3 مستقیم در سوراخ 2.7: بیرون‌کشیدن 142 kg در PLA، 118 kg در PETG؛ هرز در ~1 Nm | CNC Kitchen | A |
| پیش‌سوراخ برای 75–80% درگیری رزوه؛ دیواره دور پیچ ≥ قطر پیچ | Hubs | B |
| پیچ #4 ورق: پیش‌سوراخ 2.7، عبور 3.2، کانتر بور 6×2.6، عمق 10؛ rib پست 1.6 mm (4 دیواره)، طول 2–3× قطر پست؛ فیلت ریشه 0.8–1.6 | OpenAT | B |

### مهره‌ی محبوس (Captive nut)
| قانون | منبع | Q |
|---|---|---|
| M3: شیار 5.7 mm (فاصله‌ی تخت‌ها)، عمق 2.8، پوشش 1.0، دیواره ≥ 1.6، برآمدگی نگه‌دارنده Ø0.5؛ دهانه رو به بالا | OpenAT | B |
| جیب در کف 166 kg در برابر جیب کناری 86 kg؛ مهره در ~2 Nm می‌بُرد | CNC Kitchen | A |
| لایه‌ی پل قربانی: لایه‌ی اول = 1 لایه، دوم = 2 لایه | Hydra | B |

### رزوه‌ی چاپی، press fit، آهنربا
| قانون | منبع | Q |
|---|---|---|
| رزوه‌ی چاپی فقط ≥ M5؛ نه در سوراخ افقی | Hubs، Hydra، OpenAT | B |
| برای press fit سوراخ گرد نه (شش‌ضلعی/مربع)؛ crush rib ‏0.2 کوچک‌تر با سوراخ 0.4 بزرگ‌تر، فقط یک بار مونتاژ؛ برای استفاده‌ی مکرر grip fin | Rahix | B |
| پین < Ø5 ضعیف است: فیلت یا پین فلزی | Hubs | B |
| آهنربا: سوراخ +0.2 Ø (PLA) / +0.3 (PETG) | کاربران MakerWorld | C |

## ۴. اختلاف بین منابع

| موضوع | مقادیر |
|---|---|
| لقی snap (FDM) | Hubs 0.5 · OpenAT 0.4 (تست‌شده) · Fictiv 0.3 · Wevolver 0.2–0.4/طرف · Unionfab 0.2–0.5 · Qidi 0.10–0.20 روی سطح گیر · Slant 3D حداقل 0.5 |
| انطباق عمومی | Hydra 0.1/0.2 · Fictiv 0.2/0.4 · Prusa ≥ 0.3 · GrabCAD 0.4–0.5 · Hubs/UZH 0.5 · Craftcloud 0.15–0.3 |
| print-in-place | MIT > 0.2 · Rahix/Prusa 0.3 · Qidi 0.3–0.4 · Stratasys ≥ یک عرض خط |
| کرنش مجاز PLA | Fictiv 4–8% · Engineers Grow 0.8–1.2% · روش Bayer: ~نصف کرنش تسلیم، ×0.6 مکرر، ×0.5 برای هوک Z |
| سوراخ مهره‌ی حرارتی M3 | CNC Kitchen 4.0 واقعی (= 4.2 در CAD) · Hydra 98% قطر بیرونی (≈ 4.5 → در ناحیه‌ی ضعیف CNC Kitchen) · LBL قطر بیرونی +0.3 |
| عمق سوراخ مهره‌ی حرارتی | CNC Kitchen L+1 · Ricoh L+5 |
| دیواره/بوس مهره‌ی حرارتی M3 | CNC Kitchen 1.6 · Ricoh 1.7 (بوس 7.4) · SPIROL بوس 1.5–2× آج (~6.9–9.2) · Markforged ≥ 2 |
| پیش‌سوراخ پیچ مستقیم M3 | EJOT 2.4 (تزریقی) · CNC Kitchen 2.7 (تست‌شده) · Hubs 2.75 · Hydra 2.88 |
| overhang بدون ساپورت | Hubs/Slant 45° · Hydra < 50° · Prusa 75° (Nextruder) |
| طول بازوی snap | Unionfab 2–3× ضخامت — **با محاسبه‌ی Bayer و نسبت 1:8 Instructables تضاد دارد** |

## ۵. نتیجه برای افزونه

1. **لقی هیچ‌وقت عدد ثابت از یک سایت نیست.** پیش‌فرض‌ها از منبع A/B با بالاترین کیفیت (OpenAT 0.4 برای snap، Stratasys «≥ یک عرض خط» برای print-in-place)، ولی **مقدار نهایی از نمونه‌ی تست لقی کاربر** — همه‌ی منابع روی وابستگی به پرینتر/فیلامنت توافق دارند.
2. **مهره‌ی حرارتی:** جدول CNC Kitchen (A) با تصحیح CAD +0.2 mm؛ در گزارش، دیتاشیت سازنده‌ی همان مهره اولویت دارد.
3. **پیچ مستقیم M3:** پیش‌سوراخ 2.7 (تست CNC Kitchen) — ولی هرز شدن در ~1 Nm → برای بیش از چند بار باز و بسته، مهره‌ی حرارتی.
4. **کرنش PLA:** روش Bayer (research.md §4) با سقف؛ Fictiv 4–8% به‌نظر **غیرمحافظه‌کارانه** است و استفاده نمی‌شود؛ Engineers Grow به‌عنوان مقایسه در گزارش.
5. **لولای زنده برای PLA/ASA رد** (163 سیکل، UT Austin).
6. **روش‌های جدید برای Advisor:** grip fins و crush ribs (Rahix، Slant)، twist lock (OpenAT ابعاد دارد).
