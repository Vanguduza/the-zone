# Volume 3 — RC Motorsport Division

**RC WORLD — Master Development Plan** · Volume 3 of 13
**Revision 1.0 — July 2026** · Status: Living document — bump revision on material change

**Purpose of this volume.** This volume is the complete engineering and operating specification for the RC WORLD Motorsport Division: the Phase 1 fleet of **64 racing cars** across seven vehicle classes, the three-track Speed & Off-Road Hub (Tracks A and B in Motorsport scope; Track C belongs to the crawler program in Volume 4's adventure annex), and the race-operations business built on top of them. It codifies the division's founding doctrine — **standardized chassis, personalities created through tuning, races decided by driver skill, lap-time parity within 2–3% across every car in a class** — and turns that doctrine into working engineering: platform selection, parts commonality, fleet blueprinting and balancing procedures, ESC programming tables, suspension setup sheets, gearing mathematics, corner-weighting procedure, rental-hardening specifications, RCW Node integration, Shift turnaround workflow, and race-day operations. A competent race engineer hired into RC WORLD should be able to run this division from this volume plus the workshop practices in Volume 7.

**Intended readers.** The Motorsport Lead and race director; Artisans assigned to the racing fleet; the General Manager; investors and lenders assessing the largest single revenue engine of Phase 1; procurement staff executing the fleet purchase (with Volume 8); the RC WORLD OS development team implementing telemetry and timing features.

**Chapters**

1. Division Concept & Fleet Philosophy
2. The Class Ladder: Vehicle Classes & Fleet Composition
3. Standard Chassis Strategy & Parts Commonality
4. Performance Balancing: The Parity Engineering Method
5. ESC Programming & Powertrain Electronics
6. Suspension Tuning Guide
7. Weight Distribution & Corner Weighting
8. Gearing, Rollout & Thermal Management
9. Drift Program Deep-Dive
10. Surface-Specific Setup: Touring, Rally & Short-Course
11. Formula RC & Drag Racing Programs
12. Rental Fleet Engineering & the Shift Turnaround
13. Race Operations
14. Division KPIs & Dashboard
15. Volume Summary & Cross-References

---

## 1. Division Concept & Fleet Philosophy

### 1.1 What the Motorsport Division sells

The Motorsport Division sells the feeling of being a racing driver — not the feeling of owning a fast toy. A customer who buys a Casual Shift ($15, one 20-minute block) steps into a complete motorsport frame: a pit lane, a scrutineered car with an asset tag and live telemetry, a professional timing loop, a leaderboard with their name on it, a setup sheet clipped to the car stand. The car is deliberately *not* the hero. The hero is the lap time, and the lap time must be earned.

This is why the division's founding doctrine, inherited directly from the original RC Racing Experience Park strategy, reads as it does:

> **Doctrine.** One or two standardized 1/10 hobby-grade chassis platforms per class, with common electronics and common batteries. Vehicle "personalities" are created through tuning — ESC profiles, gearing, suspension, weight distribution, drive layout — never through different hardware. Races are decided primarily by driver skill. Lap times across every car in a class stay within **2–3%** of each other, verified weekly.

Every clause carries operational weight. *Standardized chassis* means an Artisan who can rebuild one touring car can rebuild all fourteen, and the spares shelf holds one suspension-arm SKU instead of five. *Common electronics and batteries* means one ESC programming procedure, one connector standard (XT60, per park-wide battery doctrine), and a 3:1 battery pool shared across the class. *Personalities through tuning* means a customer choosing between "GT Stable" and "Touring Agile" is choosing spring rates, drag brake, and ballast placement — dialed in or reverted in fifteen minutes — not choosing between inventories. *Decided by driver skill* is the commercial promise the RC WORLD License progression (Volume 9) monetizes. And *2–3% parity* is the falsifiable engineering claim that holds the promise together; Chapter 4 defines how it is measured and maintained.

### 1.2 Rental-grade durability doctrine

Hobby-grade RC cars are designed for owners who crash their own property. RC WORLD's cars are crashed by strangers, forty times a day, into other people's cars. The fleet therefore follows a **rental-grade durability doctrine** that intervenes at four levels:

1. **Platform level.** Select chassis with proven crash architecture: shaft-drive tub chassis over exposed belt-drive carbon plates for the standard classes; foam bumpers oversized one grade; steel driveline components where the aftermarket offers them. A rental car's Bill of Materials is optimized for **mean time between failures and mean time to repair**, not for the last 0.2 seconds of pace. We give away laptime headroom deliberately and claw parity back with tuning (Chapter 4).
2. **Hardening level.** Every car receives a standard hardening pass before entering service (Section 12.2): metal drive gears where plastic is marginal, threadlock on all metal-to-metal fasteners, silicone-sealed electronics, reinforced body mounts, skid plates on off-road classes, and the RCW Micro-Node soldered inline with strain relief.
3. **Electronic level.** Rental ESC profiles cap punch, lock timing at zero, limit reverse, and enforce soft low-voltage cutoffs (Chapter 5). Transmitter end-point adjustment (EPA) caps steering throw and throttle percentage by customer license tier. The RCW Node adds the park-side kill-switch, geofence, and under-voltage intercept.
4. **Procedural level.** The 20-minute Shift turnaround (Section 12.5), the daily fleet-readiness checklist (Section 12.6), and the weekly parity audit (SOP-MS-002) catch degradation before customers do.

> **Field Note.** The single most damaging failure mode in a rental race fleet is not the spectacular crash — it is the *slow* car that nobody notices. A car 6% off the pace poisons every race it enters: the customer driving it concludes the game is rigged, and they are right. Treat "car feels slow" reports from staff or customers with the same urgency as a broken suspension arm. The parity audit exists because slow cars hide.

### 1.3 Where Motorsport sits in the park

Phase 1 gives the division two of the three Speed & Off-Road Hub tracks:

- **Track A (Asphalt/Drift)** — polished concrete/fine asphalt circuit, ~180 m racing line, 3.5–4.5 m lane width, with a dedicated drift annex and a straight long enough to double as the drag strip (Section 11.5). Home surface for entry 1/14, 1/10 touring/GT, drift, Formula RC, and drag.
- **Track B (Baja/Rally)** — packed-dirt circuit, ~160 m line, controlled jumps (≤0.5 m landing-matched tabletops), bermed corners, watered and rolled daily. Home surface for buggy/rally and short-course.

Track C (Crawler Trail) is operationally part of the crawler/adventure program and is covered with the Construction Division's outdoor experiences in Volume 4; its 16-crawler fleet is *not* part of the 64-car Motorsport count. Physical track engineering — subgrade, drainage, barriers, driver rostrums, pit lane geometry — is specified in Volume 11; this volume states only the requirements racing imposes on those designs (Sections 9.6, 10.4, 11.5, 13.2).

The division also owns the racing calendar (Section 13.6), the leaderboard and license integrations in RC WORLD OS, and the pit-lane theatre — the Artisan battery swap that turns an Operator Shift's mid-session pause into a Formula 1 pit stop.

### 1.4 Commercial logic

At the pricing anchors set in the style guide (Casual Shift $15; Operator Shift $26; race-event entries priced per event), motorsport is the highest-throughput revenue engine of Phase 1: 64 cars against two tracks and a structured queue means the division's ceiling is set by track slots, not fleet size. The financial model (Volume 10) carries the consolidated projections; the division-level operating targets it assumes are in Chapter 14.

> **Investor Note.** The parity doctrine is margin protection, not engineering vanity. A parity fleet lets any car serve any customer in its class, pushing utilization toward the theoretical maximum — roughly 15% fewer cars for the same throughput than a "personality hardware" fleet where specific cars are demanded and others idle. It also collapses spares inventory: Section 3.4 holds the racing spares catalogue to ~130 SKUs for 64 cars.

## 2. The Class Ladder: Vehicle Classes & Fleet Composition

### 2.1 Design of the ladder

The class ladder serves three masters: the **customer journey** (an eight-year-old's first Shift and a club racer's Tuesday night must both find their class), the **RC WORLD License progression** (each rung is a license gate — Volume 9), and **fleet economics** (each class must justify its spares line and training hours). Seven classes ride on effectively four chassis platforms (Chapter 3) — that is how the ladder stays affordable.

The canonical Phase 1 motorsport fleet is **64 cars**, allocated as follows. The 24-car touring/GT allocation spans two rungs — the 1/14 entry class and the 1/10 standard class — per the park-wide fleet canon.

| # | Class | Scale | Fleet | Platform (primary) | Track | Speed (rental cap / capability) | Skill gate |
|---|---|---|---|---|---|---|---|
| 1 | Entry / Academy | 1/14 | 10 | MJX Hyper Go 14301/14210-class; LDRC entry scale | A (+ B paddock loop) | 30 km/h / ~55 km/h | Learner (age 8+, Toolbox Talk) |
| 2 | Touring / GT | 1/10 | 14 | Shaft-drive 4WD touring (TT-02 Type-S / Carten T410 class) | A | 40 km/h / ~55 km/h | Apprentice |
| 3 | Drift | 1/10 | 12 | MST RMX 2.5 S+ (RWD) | A drift annex | 25 km/h / ~35 km/h | Apprentice |
| 4 | Buggy / Rally | 1/14 | 12 | WLtoys 144010-class, upgraded | B | 50 km/h / ~75 km/h | Apprentice |
| 5 | Short-Course | 1/10 | 8 | 2WD/4WD SCT (Slash-class; ZD Racing value alternative) | B | 40 km/h / ~55 km/h | Apprentice |
| 6 | Formula RC | 1/10 | 4 | F104/TRF103-class pan car, 21.5T spec | A | 45 km/h / ~55 km/h | Foreman + Motorsport Master endorsement (supervised) |
| 7 | Drag | 1/10 | 4 | Touring-derived no-prep drag conversion | A straight (40.2 m strip) | event only / 100+ km/h | Any license (staged launch); Foreman + endorsement for free-brake passes |
| | **Total** | | **64** | | | | |

Skill gates use the RC WORLD License tiers (Learner → Apprentice → Operator → Foreman → Site Manager → Legend — Volume 9), enforced twice: the OS refuses a transmitter pairing above the customer's license tier (Section 12.1), and each tier maps to a locked **transmitter profile** — Rookie (Learner/Apprentice), Standard (Operator), Licensed (Foreman+), per Volume 9 §3.6 — that caps EPA and throttle curve regardless. Electronics stack per class is consolidated in Section 3.3; per-class detail follows.

Classes 6 and 7 (8 cars combined) are **special-event classes**: they do not run walk-up Shifts but anchor scheduled events, exhibitions, and top-tier license experiences (Chapter 11).

### 2.2 Class 1 — Entry / Academy (1/14, 10 cars)

**Role.** The first rung: walk-up customers, children 8+, birthday parties, the Learner license test bed. Everything about this class minimizes the cost of a mistake — kinetic energy at 30 km/h in a 1.4 kg car is about 49 J, roughly a tenth of a 1/10 buggy at speed.

**Hardware.** The MJX Hyper Go 1/14 family is the reference platform: metal chassis, 4WD, oil-filled shocks, 2845/2852-class brushless motor with 45 A independent ESC, 2S LiPo. The 14301/14302 rally-pattern cars suit Track A duty; the 14210 truck variant tolerates paddock abuse. Manufacturer speed claims reach 55 km/h on 2S; RC WORLD caps the class at ~30 km/h via throttle EPA and ESC profile (Chapter 5). LDRC's entry-scale line is the secondary source for licensed-body variety (supplier detail in Volume 8). Wholesale cost per car including spares kit: $90–140.

**Fleet notes.** Ten cars support the highest churn in the park; the class runs a 4-car hot-spare rotation because turnaround damage is concentrated here. Batteries: 2S 3000 mAh packs from the shared 2S pool, XT60 (factory connectors replaced at induction).

### 2.3 Class 2 — Touring / GT (1/10, 14 cars)

**Role.** The signature class: the "real racing car" a customer graduates into, the backbone of league racing, and the class where the parity doctrine is most visible. GT-styled polycarbonate bodies (Killerbody / Pandora RC catalogue) give the fleet its showroom face.

**Hardware.** Shaft-drive 4WD 1/10 touring chassis, 257–258 mm wheelbase, 190 mm width — the club-racing standard geometry. Platform selection analysis is Chapter 3; the short version: a TT-02 Type-S-class tub chassis or the factory-assembled Carten T410-class rolling chassis, fitted with a sensored 13.5T motor (Surpass Hobby Rocket 3650 class), Hobbywing QuicRun 10BL120 G2 sensored ESC, 15 kg metal-gear digital servo, and 2S 5000 mAh hard-case LiPo (Gens Ace / CNHL). Control tire: one spec 24 mm pre-glued touring slick for the whole class (Section 4.5). Rental cap 40 km/h; race profile ~55 km/h.

**Cost.** $220–320 per car complete depending on platform mix, before the hardening pass.

### 2.4 Class 3 — Drift (1/10, 12 cars)

**Role.** The style class — the park's strongest social-media surface and the anchor of evening programming. Drift rewards throttle finesse over speed; it flatters intermediate drivers and photographs beautifully under lights.

**Hardware.** MST RMX 2.5 S+ RWD chassis — the current generation of the industry's reference rear-drive drift platform (257 mm wheelbase, adjustable 6/8/10/12° caster, switchable RMX/RRX gearbox modes). Sensored 13.5T motor for smooth low-RPM torque, QuicRun 10BL120 G2, high-torque low-profile steering servo (25 kg class — drift steering loads are constant), drift-specific gyro, and spec HDPE/ABS drift rings. Full drift engineering is Chapter 9. Cost: $260–340 per car complete.

### 2.5 Class 4 — Buggy / Rally (1/14, 12 cars)

**Role.** The adrenaline class on dirt: jumps, berms, and the fastest sensation-per-dollar in the park. This is the class most first-time adult customers pick second, after one touring Shift.

**Hardware.** WLtoys 144010-class 1/14 4WD buggy — 2845 4300KV brushless, 60 A ESC on current versions, metal differentials and driveshafts, oil shocks, ~75 km/h capability — upgraded per the hardening pass: metal steering knuckles and servo saver, steel main gears, upgraded body posts, factory battery replaced by pool 2S 2200–3000 mAh XT60 packs. At $70–110 wholesale plus ~$30 hardening, the class is cheap enough to run 12 cars with 4 sealed donor units in crates.

**Fleet notes.** Rally-pattern bodies over buggy chassis give Track B a visual identity distinct from short-course. Rental cap 50 km/h (dirt forgives; barriers on Track B are engineered for this energy — Volume 11). The platform's stock metal diff cups and CVD front driveshafts are retained; hardening replaces only what fleet experience proves marginal, and shielded bearings swap to rubber-sealed at first bearing service (dirt duty).

### 2.6 Class 5 — Short-Course (1/10, 8 cars)

**Role.** The contact-tolerant "truck racing" class: bigger, softer, bouncier — the best class for group events where beginners and intermediates share a grid, because short-course bodies shrug off door-to-door contact.

**Hardware.** 1/10 short-course truck with full-perimeter body protection. The Slash-class 2WD architecture remains the durability reference with an unmatched spares ecosystem; ZD Racing's SC-class trucks are the direct-from-China value alternative — Volume 8 carries the trade-off (landed cost vs. parts lead time). Spec: 3650-size sensored 17.5T motors for controllable power, QuicRun 10BL120 G2, 2S 5000 mAh pool packs. Rental cap 40 km/h.

### 2.7 Class 6 — Formula RC (1/10, 4 cars)

**Role.** Special events and top-license experiences: open-wheel pan cars that look like Formula 1, reward precision, and punish clumsiness — the graduation class. Class rules and event formats are Section 11.1–11.2.

**Hardware.** F104/TRF103-class pan chassis, 21.5T sensored "blinky" (zero-timing) spec, foam or spec-rubber F1 tires, 2S LiPo shorty packs. Four cars support exhibition grids and the Formula Experience (guided, instructor-supervised Shifts).

### 2.8 Class 7 — Drag (1/10, 4 cars)

**Role.** Pure spectacle in 3-second doses: two cars, a Christmas tree, a 40.2 m strip (the scale 132-foot no-prep standard), and a crowd. Drag racing anchors event nights and monetizes as head-to-head bracket entries rather than Shifts (Sections 11.4–11.6).

**Hardware.** Touring-derived drag conversions on the standard 1/10 electronics stack, with wheelie bars, drag-specific gearing, and (for exhibition passes only) 3S packs under Artisan control. Rental customers never free-drive drag cars; launches are staged and speed-limited by profile.

### 2.9 Fleet capacity arithmetic

A class's revenue ceiling is `cars on track × Shifts per hour × operating hours`. With 20-minute Shifts plus 5-minute turnarounds in a 25-minute cycle (Section 12.5), each car supports up to 2.4 Shifts/hour; practical scheduling yields 2.0. Track A runs 8 concurrent touring/entry cars plus 6 in the drift annex; Track B runs 8 off-road. The binding constraint is therefore **track slots (~22 concurrent) rather than the 56 Shift-serving cars** — exactly where a rental fleet wants to be: cars queue for customers, not customers for cars, and turnaround/maintenance can breathe.

## 3. Standard Chassis Strategy & Parts Commonality

### 3.1 Selection criteria

Platform selection for a rental race fleet is a different exercise from platform selection for a racer. RC WORLD scores candidate chassis against seven weighted criteria; the weights are the doctrine in numeric form.

| Criterion | Weight | What "good" looks like for a rental fleet |
|---|---|---|
| Parts availability & ecosystem depth | 25% | Every wear part orderable from ≥3 suppliers; aftermarket metal upgrades exist for known weak points; parts still available 5 years after purchase |
| Crash architecture / MTBF | 20% | Tub or protected chassis; sacrificial cheap parts break before expensive ones; no exposed belts; foam bumper standard |
| Mean time to repair (MTTR) | 15% | Front-end rebuild < 15 min; motor/pinion access without teardown; modular gearbox |
| Unit cost incl. hardening | 15% | Complete car ≤ $350 at fleet quantities |
| Tunability envelope | 10% | Enough adjustment (camber, toe, droop, oils, gearing) to create personalities AND to equalize slow cars back to parity |
| Setup consistency car-to-car | 10% | Molded-tub repeatability; cars built from the same kit measure the same |
| Wholesale/direct sourcing viability | 5% | Factory-direct or distributor pricing at 12–24 unit volume (Volume 8) |

Two consequences deserve emphasis. First, **competition chassis lose**: a belt-drive carbon-plate touring car out-corners a TT-02 by seconds a lap but fails criteria 1–3 catastrophically in rental service — exposed belts eat gravel, carbon plates delaminate at customer crash rates, MTTR triples. Second, **orphan bargains lose**: a cheap chassis with no parts ecosystem becomes disposable the day its donor stock runs out; the WLtoys 144010 passes only because its ecosystem is enormous and the whole car costs less than a competition chassis's spare drivetrain.

### 3.2 Recommended platforms (verified July 2026)

**Touring/GT — two-platform strategy.** The class runs a deliberate split:

- **Tamiya TT-02 Type-S class (8 cars).** The TT-02 remains, in 2026, the world's default club-racing entry tub: shaft-drive 4WD, enclosed drivetrain, molded bathtub chassis, and the broadest spare-parts network in the hobby (B-parts arms #51528, A-parts uprights #51527, driveshafts #51006 are stocked by effectively every hobby retailer on earth). The Type-S adds the better suspension package out of the box. Its known rental weaknesses — kit-plastic bearings on the base model, soft friction shocks, plastic steering — are solved by a standardized $45 hop-up pass (full bearings, oil shocks, aluminum steering set, metal motor mount) at induction.
- **Carten T410-class ARTR rolling chassis (6 cars).** The T410/T410R arrives factory-assembled with oil dampers, CVDs, full bearings and metal-gear diffs on the same 258 mm / 190 mm club geometry — a stronger race base with near-zero build labor at a moderate premium. Running both platforms in one class hedges supply risk and lets the weekly parity audit prove the doctrine works across chassis makes. 3Racing's Sakura line is the tracked third option and standing price benchmark; not stocked in Phase 1, protecting SKU discipline.

**Drift — MST RMX 2.5 S+ (single platform).** MST's RMX 2.5 family superseded the long-running RMX 2.0S and is the current RWD reference: switchable RMX/RRX gearbox modes, adjustable caster uprights, HT short rear lower arms, and MST's unrivalled drift option-parts catalogue. The S+ kit (532205, ~$170–220 street) is the fleet spec, built with fleet-standard electronics (Section 3.3). MST's TCR platform is a FWD touring design, explicitly out of scope for the drift fleet.

**Buggy/Rally — WLtoys 144010-class.** Selected on overwhelming value: metal-drivetrain 4WD brushless at $70–110 wholesale with a giant parts ecosystem. Run as a *consumable platform*: harden at induction, cannibalize retired cars, keep four sealed donor units per twelve fleet cars.

**Short-course — Slash-class 2WD primary.** Chosen for the deepest durability record and spares network in the category; ZD Racing SC-class held as the value alternative if landed-cost pressure demands it (decision matrix in Volume 8).

**Formula — F104/TRF103-class pan car.** Chosen because pan-car simplicity (two diffs' worth of drivetrain fewer than a touring car) suits a 4-car special-events micro-fleet.

> **Trade Hack.** When qualifying any chassis for fleet duty, buy two units and give one to your roughest staff driver for a week with instructions to drive like a customer. Strip both cars side by side afterwards. The delta between the two teardowns is your real hardening list — manufacturer weak-point folklore from forums is usually one product generation out of date.

### 3.3 The common electronics stack

Every 1/10 car in the division, regardless of class, carries the same electronic architecture:

| Component | Fleet standard | Rationale |
|---|---|---|
| ESC | Hobbywing QuicRun 10BL120 Sensored G2 | 120 A continuous; sensored smoothness at zero throttle (critical for drift and novice control); 12 programmable items incl. punch, drag brake, timing (Chapter 5); programmable by LCD program box in seconds per car |
| Motor | Surpass Hobby Rocket 3650 sensored: 13.5T (touring, drift), 17.5T (short-course 2WD), 21.5T (formula) | One motor family, three windings; interchangeable sensor boards and bearings |
| Servo | 15 kg·cm metal-gear digital standard; 25 kg low-profile for drift | Two SKUs total |
| Receiver | Fleet transmitter system's 4-ch receiver (Section 12.1) | Model-memory binding, EPA lockout |
| Telemetry | RCW Micro-Node (~25×25 mm, ESP32-C3, soldered pads, conformal coated) | Voltage, GPS, kill-switch PWM intercept, lap beacons |
| Battery | 2S 5000 mAh hard-case LiPo, XT60 (Gens Ace / CNHL) | Shared pool, 3:1 ratio, bunker-charged |

The 1/14 classes keep their factory 45–60 A ESCs (adequate and cheap to replace whole) but standardize batteries to the pool and receive the same Micro-Node.

### 3.4 Parts commonality matrix

The matrix below is the inventory argument for standardization, expressed as SKU counts. "Shared" means one stock line serves multiple classes.

| Spares category | Touring (14) | Drift (12) | Buggy (12) | SCT (8) | Entry (10) | F/Drag (8) | SKU lines |
|---|---|---|---|---|---|---|---|
| Motors (3650 family) | 13.5T | 13.5T | factory | 17.5T | factory | 21.5T | 3 + 2 factory |
| ESC | 10BL120 G2 | shared | factory 60 A | shared | factory 45 A | shared | 1 + 2 factory |
| Servos | 15 kg std | 25 kg LP | 15 kg mini | 15 kg std | factory | 15 kg std | 3 |
| Batteries | 2S 5000 pool | shared | 2S 2200–3000 pool | shared | shared w/ buggy | shared + 3S event | 3 |
| Bearings | 5×10, 10×15 sets | largely shared | 144010 set | Slash set | MJX set | shared w/ touring | 5 |
| Suspension arms | TT-02 B-parts; T410 NHA402 | MST arm sets | 144010 arms | Slash arms | MJX arms | pan-car links | 6 |
| Driveshafts/CVDs | 2 types | 1 | 1 | 1 | 1 | 1 | ~6 |
| Spur/pinion (48P std where possible) | 48P range | 48P | factory Mod | 32P/48P | factory | 48P/64P | ~10 |
| Tires (control spec) | 1 slick | 1 drift ring | 1 knobby | 1 SCT | 1 | 2 | 7 |
| Body posts/clips/hardware | shared M3 hardware system park-wide | | | | | | ~8 |

Total racing spares catalogue: **≈130 active SKUs for 64 cars**. The equivalent unstandardized fleet (seven unrelated platforms with per-class electronics) models out at 320–380 SKUs — roughly 2.7× the working capital in spares and bin locations, and an Artisan training matrix that never converges. High-turnover lines (arms, knuckles, shock shafts, pinions, tires, bearings — Volume 7's failure catalogue) are stocked at min/max levels driven by the parts-per-100-Shifts KPI (Chapter 14).

### 3.5 Training leverage

Standardization compounds in labor. The Artisan certification path (Volume 7) requires a full teardown-rebuild sign-off per platform; with four core platforms instead of seven-plus, a new Artisan reaches full fleet coverage in roughly half the training hours, and any on-shift Artisan can service any car that rolls into the pit lane. That is what makes the 5-minute Shift turnaround (Section 12.5) staffable with two Artisans per track instead of a specialist per class.

### 3.6 Sample procurement specification

Fleet purchases are executed by Volume 8's procedures against specifications written in this format. The touring-class example below is the template; every class has an equivalent sheet as a controlled document in RC WORLD OS.

**Procurement spec MS-PS-02 — Touring/GT fleet car (extract)**

| Line | Specification | Qty | Target landed cost |
|---|---|---|---|
| Chassis kit | 1/10 shaft-drive 4WD touring, 257–258 mm WB, 190 mm width, tub chassis, enclosed drivetrain; TT-02 Type-S class or Carten T410-class ARTR per fleet split (Section 3.2) | 14 + 2 donor | $95–165/unit |
| Hop-up pass | Full ball-bearing set, oil dampers (if kit lacks), aluminum steering set, steel motor mount, spare B-parts arms ×2 sets/car | 14 kits | $45/car |
| Motor | Sensored 13.5T 3650, ROAR-legal wind, replaceable sensor board (Surpass Hobby Rocket class) | 16 (2 bench spares) | $30–45/unit |
| ESC | Hobbywing QuicRun 10BL120 Sensored G2 (P/N 30125002) + 2 × LCD Program Box Pro | 16 + boxes | $45–60/unit |
| Servo | 15 kg·cm metal-gear digital, 6.0 V, standard case | 16 | $15–25/unit |
| Body | 190 mm polycarbonate GT shells, 1.0 mm (Killerbody / Pandora RC catalogue), unpainted | 21 (1.5/car) | $25–45/unit |
| Tires | Spec 24 mm pre-glued touring slick, single compound, single supplier lot | 40 sets | $12–18/set |
| Batteries | 2S 5000 mAh hard-case LiPo, XT60, ≥50C (Gens Ace / CNHL) | 42 (3:1) | $25–40/unit |

Acceptance terms on every spec: goods inspected at The Works within 14 days; motors bench-tested on arrival (Section 4.3), >4%-off-median units rejected as a lot-quality signal; one full spares assortment per 6 cars in the same consignment (Volume 8, spares-with-fleet rule).

## 4. Performance Balancing: The Parity Engineering Method

### 4.1 What "2–3% parity" means, precisely

For each class, on its home track, a **reference driver** (a designated staff driver, rotated to prevent drift in the reference itself) drives every car for a 5-lap flying run on control tires. For each car, take the **best 3-lap average** (discarding the out-lap and any incident-flagged lap). The class parity statistic is:

`parity spread = (T_slowest − T_fastest) / T_fastest × 100%`

**Pass: spread ≤ 3.0%. Target: ≤ 2.0%. Action threshold: any single car > 1.5% off the class median** goes to the balancing bench even if the class as a whole passes. On a 22-second touring lap, 3% is 0.66 s — noticeable to a good driver over a race, invisible within the noise of a novice's driving, which is exactly the tolerance the customer promise requires.

Lap-time parity, not component parity, is the governing metric: components are balanced only as the *means* to the lap-time end. The audit is SOP-MS-002 (Section 4.8), run weekly per class and after any car's major repair.

### 4.2 The five balancing levers

A car's lap time decomposes into power, rolling stock, mass, gearing, and chassis condition. The balancing method attacks them in a fixed order — cheapest and most-determinative first:

1. **Control tires (Section 4.5)** — one spec tire per class, age-tracked. Tires are 40–60% of lap-time variance in a spec fleet; nothing else is worth measuring until tires are equalized.
2. **Motor blueprinting (Section 4.3)** — bench-test every motor; bin into performance groups; pair strong motors with heavy chassis.
3. **ESC profile equalization (Chapter 5)** — identical firmware parameters per class, verified by LCD program box readback, not by memory.
4. **Ballast to equal mass (Section 4.4)** — all cars in a class ballasted to the heaviest car's mass +0/−5 g, placed to also equalize static distribution (Chapter 7).
5. **Gearing trim (Chapter 8)** — final ±1 pinion-tooth adjustments to close residual straight-line deltas.

Suspension settings are deliberately *not* a parity lever — they are the personality lever. Parity is achieved with the five levers above at a neutral baseline setup; personalities (Section 5.3) are then layered on top and verified not to break parity.

### 4.3 Motor blueprinting and binning

Mass-produced motors vary. Two "identical" 13.5T sensored motors can differ 3–5% in output from winding tolerance, magnet strength (zeta), bearing drag, and sensor-timing offset. The Works maintains a motor bench (detail in Volume 7, Chapter 6) and every fleet motor is characterized at induction and at every 200-Shift service:

**Bench procedure (no dyno required).** With a charged reference pack, a bench PSU log, and a phototach:
1. Measure **free-run RPM** at a fixed 7.60 V supply with a spec pinion-mass flywheel. Record RPM and free-run current.
2. Measure **loaded current** driving the spec test fixture (a fan-brake disc) at fixed throttle.
3. Check bearing drag by spin-down time from 10,000 RPM; reject or re-bearing below spec.
4. Record all values to `fleet_inventory` (motor sub-asset) in RC WORLD OS.

**Binning.** Sort the class's motors by free-run RPM into three bins — **A (top third), B (middle), C (bottom)** — and pull any motor >4% below the class median for inspection (typically worn bearings or a damaged sensor board; replace, don't shim). Bins are assigned to chassis to *cancel* variance: A-bin motors to the cars that weighed heaviest or tested slowest as rollers; C-bin to the freest chassis. A true motor dyno (Fleet Analyzer class) is a justified Year-2 purchase; the bench method holds parity well inside 3% without it.

### 4.4 Ballast equalization

Weigh every car race-ready (body, battery of median pool mass, transponder, Node). The heaviest car defines class minimum weight, rounded up to the next 5 g; every other car is ballasted up to that figure with self-adhesive 5 g/10 g plates placed per the class ballast map (Chapter 7). Mass equality does double duty: it equalizes acceleration (`a = F/m`) and removes the temptation to "fix" a slow car by stripping weight, which would silently break corner-weight balance.

### 4.5 The control tire rule

> **Doctrine.** One tire specification per class. No exceptions, including staff cars used in customer races. Tires are lifed in Shifts and retired on schedule or on wear indicator, whichever first.

Tires are bought in bulk lots, each sample-tested (three cars, reference driver) before release; a lot shifting lap times >1% against the incumbent triggers a full-class re-audit on changeover day. Tire age is tracked by a paint-dot code on the wheel: touring slicks life at 60 Shifts, buggy knobbies 80, drift rings 150 (wear-driven), SCT 80. Mixed-age *sets* are forbidden; cars re-tire as sets.

### 4.6 Worked example: bringing three cars into parity

Three touring cars from the fleet, audited on Track A (reference driver, 5-lap runs, best-3 average). Baseline audit:

| Car | Chassis | Best-3 avg | Δ vs. fastest | Race-ready mass | Motor free-run @7.60 V | Tire age |
|---|---|---|---|---|---|---|
| T-04 | TT-02 S | 22.14 s | — | 1,512 g | 31,800 RPM (A-bin) | 22 Shifts |
| T-09 | T410 | 22.61 s | +2.1% | 1,478 g | 30,450 RPM (B-bin) | 41 Shifts |
| T-11 | TT-02 S | 23.05 s | +4.1% | 1,530 g | 29,150 RPM (C-bin, −8.3% vs. T-04) | 58 Shifts |

Class spread = (23.05 − 22.14)/22.14 = **4.1% — audit fail**, with T-11 the actionable outlier and T-09 marginal.

**Step 1 — Tires.** T-11's tires are at 58 of 60 Shifts — end of life. New control set fitted to T-11; T-09's 41-Shift set retained (mid-life is the fleet norm and the parity target must hold across normal tire life). Re-run: T-11 improves to 22.71 s (tires alone recovered ~0.34 s, 1.5%).

**Step 2 — Motor.** T-11's motor free-run is 8.3% below the class fastest — outside the 4% bin rule. Inspection finds rough motor bearings; bearings replaced, re-bench: 30,900 RPM (B-bin). Motors stay in place post-repair; ballast does the cancelling in the next step.

**Step 3 — Mass.** Heaviest car is T-11 at 1,530 g → class minimum set at 1,530 g. T-04 receives +18 g (two 5 g plates at the rear cross-brace, one 5 g plate + 3 g trim on the battery tray fore position, per the touring ballast map to hold 50/50 — Chapter 7). T-09 receives +52 g (30 g low-center battery-tray plates, 22 g split front/rear to preserve its measured 49.8/50.2 distribution). Note the deliberate effect: the fastest car gained the most mass.

**Step 4 — ESC readback.** Program-box readback on all three: T-09 found with punch at Level 6 versus the rental-standard Level 3 — a leftover from an event night, and the explanation for its strong baseline launches. Reset to the Touring RENTAL profile (Table 5.2); profiles now identical.

**Step 5 — Gearing trim.** Post-correction straight-line trap speeds (RCW Node telemetry over the main-straight sector): T-04 38.9 km/h, T-09 38.1 km/h, T-11 38.4 km/h. T-09 gets +1 pinion tooth (27T → 28T, FDR 6.16 → 5.94, +3.7% top-end, negligible on a 22 s lap's single straight but closes the trap gap; motor temp check after 10 min shows 71 °C — inside the 85 °C ceiling, accepted).

**Verification audit:**

| Car | Best-3 avg | Δ vs. fastest |
|---|---|---|
| T-04 | 22.31 s | — |
| T-09 | 22.48 s | +0.8% |
| T-11 | 22.63 s | +1.4% |

Class spread **1.4% — pass, inside target**. Bench time: ~2.5 Artisan-hours for three cars; parts cost one bearing set and one tire set, both scheduled consumables. Note that T-04 got *slower* (+0.17 s from ballast): parity engineering levels down as well as up, deliberately. The customer promise is a fair race, not the fastest possible car.

### 4.7 Continuous parity monitoring between audits

The weekly audit is the calibrated measurement; the RCW Node makes the other six days observable too. Every customer lap generates a telemetry lap record tagged with car ID, driver license tier, battery pack ID, and ambient. Raw customer lap times are useless for parity directly — driver skill variance swamps car variance — but two derived statistics are not:

- **Per-car best-decile drift.** RC WORLD OS tracks each car's 90th-percentile-best lap by *Foreman-and-above* drivers over a rolling 14 days, normalized to the class's same-day median. A car drifting >1% slow over a week is flagged for the bench before the weekly audit would catch it. The filter matters: good drivers find a car's real pace; novices find their own.
- **Straight-line sector consistency.** The Node's speed trace over the main-straight geofence sector is driver-insensitive at full throttle. A car whose trap-speed distribution shifts down 2%+ against class peers has a powertrain problem regardless of what its lap times say.

Both statistics render on the fleet dashboard (Chapter 14) as per-car sparklines. They do not replace the audit — telemetry cannot control for tires, traffic, or track state the way a reference driver can — but they turn the weekly snapshot into a continuous control loop, and they usually name the guilty subsystem before the car reaches the bench.

### 4.8 SOP-MS-002 — Weekly Fleet Parity Audit

| | |
|---|---|
| **SOP ID** | SOP-MS-002 |
| **Revision** | 1.0 (July 2026) |
| **Owner** | Motorsport Lead |
| **PPE** | None beyond track-standard (closed shoes, hi-vis on live track) |
| **Tools** | Reference transmitter; charged reference packs (storage-rotated); timing system live; LCD Program Box Pro; scales; pit thermometer/IR gun; tablet with RC WORLD OS fleet audit form |
| **Frequency** | Weekly per class (rolling schedule, one class per weekday); additionally after any major repair, motor/ESC swap, or tire-lot changeover |

1. Close the track to customers for the audit window (schedule pre-opening; ~45 min per 12-car class).
2. Verify conditions: surface dry, ambient within 10 °C of last audit (log both); sweep/blow the racing line.
3. Stage all class cars race-ready: control tires within life, pool battery at full charge, bodies on, Nodes reporting.
4. Reference driver runs each car: 1 out-lap + 5 flying laps. Timing system records automatically via transponder ID.
5. RC WORLD OS computes best-3 averages and class spread; the audit form flags cars >1.5% off median.
6. For each flagged car, execute the balancing ladder in order (tires → motor bench → ESC readback → mass → gearing) and re-run.
7. If ambient/surface shifted mid-audit (>0.3 s drift in the reference car re-baseline), re-baseline and re-run affected cars.
8. Sign off the audit in RC WORLD OS; cars failing after balancing go to maintenance status and out of the rental pool.
9. File exceptions to the Motorsport Lead same-day; two consecutive weekly failures for the same car mandates a full teardown (Volume 7).

### 4.9 Quarantine rules for out-of-spec cars

A car that cannot be balanced back inside 1.5% of class median at the bench enters **quarantine** — a formal state, not a shelf:

- **Status flip.** The car goes to `maintenance` in RC WORLD OS with reason code `PARITY-FAIL`, its transponder and transmitter pairings are voided, and its stand gets a red quarantine tag. A quarantined car physically leaves the ready line; it is never "kept handy just in case" — busy Saturdays are exactly when a slow car sneaks back into service.
- **Diagnosis before parts.** Quarantine work follows the balancing-ladder evidence already collected, plus a corner-weight check and a full drivetrain teardown if free-roll spin-down is >15% below class median. The rule is *find the watt, don't mask it*: re-gearing a car with a dragging diff hides the fault and moves the heat somewhere else.
- **Exit criteria.** Release requires: fault identified and logged (`maintenance_logs` with parts used), bench free-roll within spec, and a solo parity re-run landing within 1.5% of the last full audit's class median (ambient-corrected). The closing Artisan and the Motorsport Lead both sign.
- **Escalation.** Two quarantines in 60 days on the same subsystem escalates to The Works for full rebuild and a pattern review (chronic crasher assignment, bad donor batch, old-impact chassis tweak). Three unexplained quarantines retire the car to the parts-harvest bench (Section 12.8) regardless of age — fleet math never justifies a car the engineers cannot trust.

## 5. ESC Programming & Powertrain Electronics

### 5.1 Why the ESC is the division's most powerful tuning tool

The ESC is software-defined drivability. On the fleet-standard Hobbywing QuicRun 10BL120 Sensored G2 (~$45–70 street, verified July 2026), twelve programmable items govern how the same motor, gearing, and chassis *feel*: running mode, low-voltage cutoff, punch (9 steps), drag brake force (8 steps), maximum brake force (4 steps), initial brake force, maximum reverse force, neutral range, timing (8 steps), overheat protection, BEC voltage (6.0/7.4 V switchable), and motor rotation. Three of these — punch, drag brake, and timing — do most of the personality and safety work in a rental fleet, and one of them (timing) is permanently locked at zero in rental profiles.

**Parameter physics, briefly:**

- **Punch** (Levels 1–9) rate-limits how fast the ESC ramps current against throttle input. Low punch converts a novice's throttle stab into a progressive launch; high punch delivers the input verbatim. Punch is the single biggest "feel" lever in the fleet and the first line of defense against novice spin-outs and stripped spur gears.
- **Drag brake** (0–100% in 8 steps) applies braking torque at neutral throttle, simulating brushed-motor coast-down. It defines corner-entry character: touring cars run modest drag brake for stable entry; drift cars run higher values as a weight-transfer tool (Chapter 9); buggies on loose dirt run little to none so the rear doesn't step out on lifted throttle. Drag brake generates motor heat — every step up must be checked against the temperature ceiling (Section 8.3).
- **Timing** (8 steps on the 10BL120 G2, roughly 0–30° of electronic advance) trades top-end RPM for heat, consumption, and abrupt top-of-band delivery. In rental service added timing is pure liability: **timing step 0, locked**, verified at every profile audit. Race-night profiles for licensed leagues may run modest timing (steps 1–2) under Artisan supervision only, always paired with a motor-temperature check (Section 8.3). Dynamic boost/turbo advance — the XeRun-class competition feature that ramps additional degrees with RPM and full-throttle dwell — is not present on the fleet ESC by design; "blinky" (zero-timing) running is both the formula class rule and the fleet's default posture.
- **Cutoff voltage** is set to 3.4 V/cell fleet-wide — deliberately above the ESC's available lower options and aligned with the park's LiPo doctrine (3.4–4.2 V/cell). The RCW Node enforces the same threshold independently by PWM intercept, so battery protection survives an ESC misconfiguration. Two independent guards, one doctrine.

### 5.2 Fleet ESC profiles

Profiles are written to cars with the LCD Program Box Pro from a laminated parameter card kept at the programming bench; RC WORLD OS stores the canonical table and the per-car last-write log. **Readback, not memory, is the verification standard** (see the worked example in Section 4.6 for why).

**Table 5.2 — Hobbywing QuicRun 10BL120 G2 fleet profiles**

| Parameter | Touring RENTAL | Touring RACE | Drift RENTAL | Drift RACE | SCT RENTAL | Buggy RENTAL (factory 60 A ESC equiv.) | Formula SPEC |
|---|---|---|---|---|---|---|---|
| Running mode | Fwd/Brake | Fwd/Brake | Fwd/Rev/Brake | Fwd/Rev/Brake | Fwd/Rev/Brake | Fwd/Rev/Brake | Fwd/Brake |
| Cutoff voltage | 3.4 V/cell | 3.4 V/cell | 3.4 V/cell | 3.4 V/cell | 3.4 V/cell | 3.4 V/cell | 3.4 V/cell |
| Punch | Level 3 | Level 6 | Level 4 | Level 5 | Level 3 | Level 3 (soft start) | Level 5 |
| Drag brake | 10% | 5% | 40% | 60% | 10% | 0–5% | 5% |
| Max brake force | 50% | 75% | 75% | 100% | 50% | 50% | 75% |
| Max reverse force | n/a | n/a | 25% | 25% | 25% | 25% | n/a |
| Neutral range | 9% | 6% | 6% | 6% | 9% | 9% | 6% |
| Timing | step 0 (locked) | step 0–2 (Lead sign-off) | step 0 (locked) | step 0 | step 0 (locked) | n/a | step 0 ("blinky" class rule) |
| BEC voltage | 6.0 V | 6.0 V | 7.4 V (25 kg servo) | 7.4 V | 6.0 V | factory | 6.0 V |

Rationale notes: rental punch Level 3 gives a ~0.4 s softer 0–30 km/h ramp than race Level 6 — enough to protect drivetrains and dignity without feeling numb. Reverse is enabled on off-road and drift rentals (self-recovery reduces Tow-Truck Protocol events) but *disabled* on touring and formula, where reversing on a live circuit is a collision generator. The wider 9% neutral range on rentals absorbs transmitter centering noise; race profiles tighten to 6%.

### 5.3 Motor pairing and the "personality" overlay

Personalities are published, named setups layered *on top of* a parity-verified baseline — never hardware differences:

| Personality (touring example) | Punch | Drag brake | Spring set | Ballast map | Character sold to customer |
|---|---|---|---|---|---|
| GT Stable | 3 | 15% | +1 step front stiff | neutral | Planted, forgiving, easy to place |
| Touring Neutral (baseline) | 3 | 10% | baseline | neutral | The reference car |
| Touring Agile | 4 | 5% | +1 step rear stiff | 10 g rearward | Pointier turn-in, livelier rear |

Each personality must re-pass the parity audit as configured (the reference driver's best-3 within 1.5% of class median). If a personality can't pass, it's a gimmick, not a setup, and it doesn't ship.

### 5.4 Throttle curves at the transmitter

Punch shapes *how fast* the ESC delivers current; the transmitter's throttle curve shapes *how much* throttle a given trigger position requests. The two are tuned together, and the curve lives in the locked transmitter profiles (Section 12.1; license-tier mapping Volume 9 §3.6), which is why it belongs to fleet configuration rather than per-car setup. Fleet curves, as output % at 25/50/75/100% trigger travel:

| Transmitter profile (Volume 9 §3.6) | 25% | 50% | 75% | 100% | Character |
|---|---|---|---|---|---|
| Rookie — Learner/Apprentice (expo −30%, EPA 60%) | 10% | 25% | 42% | 60% | Long, gentle lower band; a nervous full pull still lands at the class rental cap |
| Standard — Operator (expo −15%, EPA 80%) | 16% | 36% | 58% | 80% | Progressive but honest; the default customer feel |
| Licensed — Foreman+ (linear, EPA 100%) | 25% | 50% | 75% | 100% | Verbatim input inside class gearing caps |
| Drift all profiles (expo −20%) | 14% | 33% | 56% | profile EPA | Widens the partial-throttle band where wheelspeed control lives |

Design logic: negative expo flattens the curve through the first half of trigger travel — where novices actually drive — so small hand movements make small speed changes, while the top of the band is reachable deliberately rather than accidentally. Drift keeps moderate expo at every tier because partial-throttle modulation *is* the class skill. Brake-side curves stay linear on all profiles (nobody should meet a nonlinear brake in an emergency), with authority set by the ESC's max-brake-force parameter. Curve revisions are fleet-configuration changes: Motorsport Lead sign-off, OS config log entry, and a spot parity re-run.

### 5.5 SOP-MS-001 — ESC Profile Write & Verification

| | |
|---|---|
| **SOP ID** | SOP-MS-001 |
| **Revision** | 1.0 (July 2026) |
| **Owner** | Motorsport Lead |
| **PPE** | None (bench task); car on stand, wheels free |
| **Tools** | Hobbywing LCD Program Box Pro; laminated profile card (current revision); charged bench pack; RC WORLD OS asset scanner |
| **Frequency** | At car induction; after any ESC replacement; at every 200-Shift service; on any parity-audit flag; before/after event-night profile swaps |

1. Scan the car's asset tag; open its ESC profile record in RC WORLD OS. Confirm which profile the car *should* hold.
2. Power the car on stand (wheels clear of the bench). Connect the program box to the ESC's programming port.
3. **Read before writing:** page through all 12 parameters and record actuals. Any mismatch with the recorded profile is logged as a deviation (who/when investigated later — deviations are a process failure signal, not just a fix).
4. Write the target profile parameter by parameter from the laminated card. Save.
5. Power-cycle the ESC. Read back all 12 parameters and verify against the card. Two-person check for RACE→RENTAL reversions after event nights.
6. Function test on stand: throttle ramp (punch behavior), neutral (drag brake engagement audible), brake, reverse lockout as applicable.
7. Update the RC WORLD OS profile record (profile name, revision, Artisan ID, timestamp). The car may not re-enter the rental pool with an unverified profile record.

> **Safety Warning.** Never program an ESC with the car on the ground or with the pinion engaged and wheels loaded. Programming sequences can command unexpected throttle. Stand, wheels free, hands clear — every time, including "quick" changes on race night.

## 6. Suspension Tuning Guide

### 6.1 The tuning stack and how to think about it

Suspension turns chassis motion into tire grip. For fleet purposes the tuning stack is, from largest effect to smallest: tires (fixed by the control rule) → springs → damper oil → geometry (camber, caster, toe) → droop → ride height → anti-roll bars. The division's working rules: **change one variable at a time; three laps minimum before judging; write everything on the setup sheet.** RC WORLD OS stores every car's current setup digitally; the paper sheet on the car stand is the working copy.

### 6.2 Springs and damper oils

Springs carry the chassis; oil controls how fast weight transfers. Fleet damper oils are silicone, specified in **cSt (centistokes)** — the unambiguous international scale — with WT equivalents noted for staff raised on them:

| Silicone oil | ~WT equiv. | Fleet use |
|---|---|---|
| 200–300 cSt | ~17.5–25 | Buggy/SCT big-bore, rough dirt |
| 350–450 cSt | ~30–35 | Buggy smooth dirt; SCT baseline (400) |
| 500–600 cSt | ~40–45 | Touring baseline (500); drift front (550) |
| 700–900 cSt | ~50–60 | Touring high-grip; drift rear (700); Formula side dampers |

Effects, memorized by every Artisan: **stiffer springs** = less roll, quicker response, less mechanical grip on that axle, better on smooth high-grip surfaces; **softer** = the reverse. **Thicker oil** slows weight transfer — planted mid-corner, lazy in direction changes; **thinner** transfers faster — responsive but nervous. On bumpy dirt, thick oil makes the car skip; go thinner and let the springs work. Oil thins as it heats, which is why baselines are set at operating temperature and the parity audit logs ambient.

### 6.3 Geometry: camber, caster, toe, droop, ride height, bars, roll centers, anti-squat

- **Camber** (top of tire leaning in = negative): compensates for body roll so the outside tire stays flat under load. Touring baseline −1.5° front / −1.5° rear on spec slicks; more negative front camber adds mid-corner steering until the contact patch shrinks on the straights. Verify with a camber gauge on a flat setup board, wheels at ride height.
- **Caster** (kingpin tilted rearward at top): more caster = more straight-line stability and more camber gain on the steered wheel = stronger mid-corner front grip, at the cost of heavier initial turn-in. Touring 4–6°; drift runs high caster (Chapter 9); buggies run higher still for jump stability.
- **Toe:** front toe-out (0 to −1°) sharpens turn-in; front toe-in calms it. **Rear toe-in is stability medicine** — touring 2.5–3°, buggy 3°, never toe-out at the rear of anything a customer drives.
- **Droop** (downtravel beyond static ride height): more droop = more weight transfer available = more grip on the *opposite* end under load transfer, and better bump absorption; less droop = flatter, more responsive on smooth asphalt. Measured with droop blocks and gauge; touring baseline 4 mm front / 5 mm rear.
- **Ride height:** lower = lower CG = less roll, until the chassis scrubs. Touring 5.5–6 mm on our asphalt; buggy 22–25 mm; SCT 28–32 mm. Always set with the battery installed at pool-median mass.
- **Anti-roll bars:** tune roll stiffness without touching bump behavior. Stiffer bar on one end reduces grip on that end in steady-state cornering. Touring runs 1.2 mm front / 1.3 mm rear as baseline; buggies on our Track B run none (bar-free compliance wins on dirt this loose).
- **Roll centers:** set by the inner/outer heights of the suspension links (camber-link tower position, arm-mount shims). Raising a roll center toward the CG reduces body roll on that end — quicker but edgier response; lowering it rolls the chassis more and builds grip progressively. Fleet doctrine: roll centers are a **baseline decision, not a turnaround adjustment** — link positions are recorded as tower-hole coordinates and changed only with Motorsport Lead sign-off, because a one-hole change on one car is invisible to the eye and audible in the parity audit.
- **Anti-squat / kick-up** (off-road): anti-squat is the rearward tilt of the rear inner hinge pins — more (2–3°) resists squat under throttle for crisper on-power steering and better jump takeoffs on packed dirt, at the cost of rear traction on bumpy acceleration; less (0–1°) plants the rear on loose surfaces. Kick-up is the front-end equivalent: more absorbs landings and square-edged bumps but slows steering response. Track B baseline: buggies 2° anti-squat, ~10° kick-up (platform fixed); SCT 3° anti-squat via pill inserts. On-road classes run effectively zero of both and tune the same behaviors with droop and oils.

### 6.4 Setup-change effects table

The laminated pit-lane card every Artisan carries:

| Change (one step) | Turn-in | Mid-corner steering | Corner-exit stability | Straight-line | Bumps/jumps | Watch out for |
|---|---|---|---|---|---|---|
| Softer front springs | + | + | − | 0 | + | Sluggish transitions |
| Stiffer rear springs | + | + | − | 0 | − | Snap oversteer on cold tires |
| Thinner front oil | + | 0 | − | 0 | + | Nervous on high grip |
| Thicker rear oil | 0 | + | + (smooth) | 0 | − | Kicks on square bumps |
| More front camber (−) | 0 | + | 0 | − (drag) | 0 | Inner-shoulder tire wear |
| More caster | − (initial) | + | + | + | + (jumps) | Heavy steering feel |
| Front toe-out | + | 0 | 0 | − (wander) | 0 | Twitchy on the straight |
| More rear toe-in | − | − | + | − (drag) | 0 | Scrubs speed; use ≤3° |
| More rear droop | 0 | 0 | + (traction) | 0 | + | Roll into corner-exit wobble |
| Lower ride height | + | + | + | + | − | Chassis scrub, bottoming |
| Stiffer rear bar | + | + | − | 0 | − | Loose on power |

### 6.5 Baseline setup sheets

Baselines are the parity-audited neutral configurations. Personalities and race setups are recorded as deltas from these sheets.

**Table 6.5a — Touring/GT baseline (Track A asphalt, spec slick)**

| Parameter | Front | Rear |
|---|---|---|
| Springs | medium (silver) | medium (silver) |
| Damper oil | 500 cSt | 500 cSt |
| Camber | −1.5° | −1.5° |
| Toe | 0° | 3.0° in |
| Caster | 4° | — |
| Droop | 4 mm | 5 mm |
| Ride height | 5.5 mm | 6.0 mm |
| Anti-roll bar | 1.2 mm | 1.3 mm |
| Diff | gear diff 3,000 cSt | gear diff 1,000 cSt |
| FDR / mass / distribution | 6.16 · 1,530 g · 50/50 (Ch. 7–8) | |

**Table 6.5b — Drift baseline (MST RMX 2.5 S+, RWD — full rationale Ch. 9)**

| Parameter | Front | Rear |
|---|---|---|
| Springs | soft | medium |
| Damper oil | 550 cSt | 700 cSt |
| Camber | −6° | −1° |
| Caster | 10° | — |
| Toe | (Ackermann-dominated; ~0° static) | 0° |
| Ride height | 5 mm | 5.5 mm |
| Steering angle | ~65° effective | — |
| Gyro gain | 60% rental / 45% race | — |
| Mass / distribution | 1,450 g · 46/54 | |

**Table 6.5c — Buggy/Rally baseline (WLtoys 144010-class, Track B packed dirt)**

| Parameter | Front | Rear |
|---|---|---|
| Springs | factory +10% (upgrade set) | factory +10% |
| Damper oil | 300 cSt | 350 cSt |
| Camber | −1° | −1.5° |
| Toe | 0° | 3° in |
| Ride height | 22 mm | 24 mm |
| Mass / distribution | 1,050 g · 45/55 | |

**Table 6.5d — Short-course baseline (2WD, Track B)**

| Parameter | Front | Rear |
|---|---|---|
| Springs | medium | medium-soft |
| Damper oil | 400 cSt | 350 cSt |
| Camber | −1° | −1° |
| Toe | 0° | 3° in |
| Ride height | 28 mm | 30 mm |
| Mass / distribution | 2,050 g · 42/58 | |

> **Trade Hack.** Build shock pairs on the bench to *matched rebound*: after filling and bleeding, compress both shocks fully and time the rebound stroke side by side. A mismatched pair (one seal dragging, one aerated) is the most common invisible setup fault in a rental fleet — it steers the car under braking and no geometry change will fix it. Rebuild shocks as axle pairs, never singly.

## 7. Weight Distribution & Corner Weighting

### 7.1 Static distribution targets

Where the mass sits determines which tires do the work. Class targets, race-ready (battery in, body on):

| Class | Front/Rear target | Cross-weight tolerance | Rationale |
|---|---|---|---|
| Touring/GT | 50/50 (±1) | ±1.0% | Neutral 4WD balance; equal tire duty on a flowing circuit |
| Drift (RWD) | 46/54 (±1) | ±1.0% | Rear bias for traction under constant wheelspin; enough nose weight to keep steered-wheel authority |
| Buggy/Rally | 45/55 (±2) | ±1.5% | Rear bias plants forward drive on loose dirt and stabilizes jump attitude |
| Short-course 2WD | 42/58 (±2) | ±1.5% | Motor-over-axle traction; high body mass makes cross-weight drift with body damage — recheck after body swaps |
| Formula | 46/54 (±1) | ±1.0% | Pan-car convention: rear traction, front handled by tire compound |
| Drag | 30/70 launch bias (ballast forward as needed to control wheelies with the wheelie bar as backstop) | — | Launch traction is everything on a 40 m strip |

### 7.2 Corner-weighting procedure

Four-scale corner weighting, standard bench task (15 minutes once practiced):

1. Level the setup board (bubble level, shim the board not the scales). Zero all four scales.
2. Car race-ready: pool-median battery, body, transponder, Node. Shocks settled — roll the car back and forth, then lift and set down twice.
3. Record FL, FR, RL, RR. Compute: front % = (FL+FR)/total; **cross-weight % = (FR+RL)/total** (should be 50% ± class tolerance).
4. Correct *distribution* by moving ballast/battery position fore-aft along the ballast map; correct *cross-weight* by spring pre-load collars in diagonal pairs (small turns — 0.5 mm at a time), never by bending anything.
5. Re-settle and re-measure after every change. Log final corners to the setup record.

**Ballast maps.** Ballast lives low and central by default: touring — battery-tray floor first, then the chassis centerline fore/aft trim positions; drift — rear of battery slot (bias) and over the front axle line (steering authority trim); buggy — under-receiver-box plate; drag — nose plate. Ballast is self-adhesive lead-free plate (5/10 g), covered with a taped label showing grams and date so audits can reconcile mass records at a glance.

> **Field Note.** Cross-weight ("wedge") is the setup fault customers can feel but never name — the car that turns left better than right. Any car reported as "pulls one way" goes to the corner scales *before* anyone touches the steering trim. Nine times out of ten it's a tweaked shock collar or a post-crash bent arm loading one diagonal.

### 7.3 Worked example: ballasting a touring car to target

Car MS-T-07, corner-weighed race-ready after a front-end rebuild:

| | Left | Right | Axle total |
|---|---|---|---|
| Front | FL 362 g | FR 371 g | 733 g |
| Rear | RL 391 g | RR 382 g | 773 g |
| **Total** | | | **1,506 g** |

Derived numbers: front % = 733/1,506 = **48.7%** (target 50 ± 1 — out of spec); cross-weight = (FR + RL)/total = (371 + 391)/1,506 = **50.6%** (inside the ±1.0% tolerance); class minimum mass = 1,530 g, so the car is also **24 g light**.

The ballast requirement solves both problems at once. At 50.0% front and 1,530 g final mass, the front axle must carry 0.500 × 1,530 = 765 g — a gain of 32 g while the rear gains −8 g, impossible by addition alone. So the battery first shifts one tray position forward (measured effect on this chassis: +14 g front / −14 g rear), giving 747/759. The 24 g of ballast then lands as: +18 g front (10 g + 5 g + 3 g trim at the front tray edge), +6 g rear (5 g ahead of the rear brace + 1 g lead tape), all on the centerline and split left/right so cross-weight is untouched. Re-weigh confirms 765/765 (50.0/50.0), cross 50.3%, total 1,530 g. Bench time: 12 minutes. Plate positions and grams go to the setup record — the audit trail is what lets next month's Artisan trust the sheet instead of re-deriving it.

## 8. Gearing, Rollout & Thermal Management

### 8.1 The arithmetic

Three formulas govern everything in this chapter:

- **Final Drive Ratio:** `FDR = (spur ÷ pinion) × internal transmission ratio`
- **Rollout** (distance per motor revolution): `rollout = (π × tire Ø) ÷ FDR`
- **Theoretical top speed:** `v = motor RPM × rollout ÷ 60` (m/s), where loaded motor RPM ≈ Kv × sagged pack voltage × ~0.85 drivetrain/load factor.

Worked touring example: spur 64T, pinion 27T, internal ratio 2.6 (TT-02 class) → FDR = (64/27) × 2.6 = **6.16**. Tire Ø 63 mm → rollout = (π × 63)/6.16 = **32.1 mm/rev**. A 13.5T sensored motor at ~3,100 Kv on a sagged 7.4 V under load: 3,100 × 7.4 × 0.85 ≈ 19,500 RPM → v ≈ 19,500 × 0.0321/60 ≈ 10.4 m/s ≈ **37.5 km/h** — which is why the rental cap of 40 km/h for this class is enforced primarily by gearing and only secondarily by throttle EPA. Gearing caps cannot be un-clicked by a customer.

(The Carten T410-class cars run internal ratio 2.53; their pinion spec is adjusted one tooth to land within 1% of the same rollout — parity is a rollout number, not a pinion number.)

### 8.2 FDR tables per class and track

Fleet gears standardize on 48P for the 1/10 classes (tooth-strength vs. adjustability sweet spot; 64P reserved for formula fine-trim; the 1/14 classes keep factory Mod-0.7).

| Class / duty | Tire Ø | Internal ratio | Spur/pinion | FDR | Rollout | Est. top speed |
|---|---|---|---|---|---|---|
| Touring RENTAL, Track A | 63 mm | 2.6 | 64/27 | 6.16 | 32.1 mm | ~38 km/h |
| Touring RACE, Track A | 63 mm | 2.6 | 64/31 | 5.37 | 36.9 mm | ~44 km/h |
| Drift (all duty) | 64 mm | 2.6 (RMX mode) | 64/24 | 6.93 | 29.0 mm | ~33 km/h (wheelspeed higher) |
| Buggy RENTAL, Track B | 90 mm | factory | factory −1 pinion | ~8.5 eff. | 33 mm | ~50 km/h |
| SCT RENTAL, Track B | 108 mm | 2.72 | 86/22 (48P) | 10.6 | 32.0 mm | ~40 km/h |
| Formula SPEC, Track A | 62 mm | direct (1.0 axle) | 96/33 (64P) | 2.91 | 66.9 mm | ~48 km/h (21.5T) |
| Drag EXHIBITION, 40.2 m | 66 mm | 2.6 | 64/38 | 4.38 | 47.3 mm | 100+ km/h (3S) |

Gearing changes for heat or track layout move in single pinion teeth: one 48P tooth ≈ 3–4% rollout — conveniently, about one parity-spread unit, which is why gearing is the *last* trim lever in the balancing ladder.

**Touring pinion sweep chart (64T spur, 48P, internal 2.6, tire Ø 63 mm)** — the bench card for Track A trim decisions:

| Pinion | FDR | Rollout | Δ speed vs. 27T | Motor temp tendency | Duty |
|---|---|---|---|---|---|
| 24T | 6.93 | 28.6 mm | −11% | coolest | Heat-wave rental fallback; new-driver events |
| 25T | 6.66 | 29.7 mm | −7% | cool | Summer afternoon rental state |
| 26T | 6.40 | 30.9 mm | −4% | cool-normal | Shoulder-season rental |
| **27T** | **6.16** | **32.1 mm** | **baseline** | **normal** | **Rental baseline (Table 8.2)** |
| 28T | 5.94 | 33.3 mm | +4% | warm | Parity trim ceiling for rentals |
| 30T | 5.55 | 35.7 mm | +11% | hot — check at 10 min | League race state |
| 31T | 5.37 | 36.9 mm | +15% | hot — mandatory temp check | Race profile (Table 8.2), finals only |

Operational rule: rentals may move within 25–28T on turnaround Artisans' authority under the thermal rules below; anything beyond requires the Motorsport Lead, because it changes the class speed envelope rather than the trim. Equivalent sweep cards for the other classes hang at each class bench as controlled documents in RC WORLD OS.

### 8.3 Motor temperature management

The fleet thermal ceiling is **85 °C at the motor can**, measured by IR gun at the endbell within 60 seconds of the car stopping; 90 °C+ demags rotors and cooks sensor boards. Standing rules:

- Turnaround Artisans spot-check the hottest recent runner each cycle; any car over 85 °C is pulled, geared **down** one pinion tooth (higher FDR runs cooler), and its drag-brake setting reviewed (drag brake is hidden heat).
- Summer afternoons on Track A: pre-emptive −1 tooth across touring when ambient exceeds 32 °C, reverted in the evening — logged as a fleet-wide gearing state in RC WORLD OS so parity math stays coherent.
- ESC temperatures are watched via the ESC's own thermal protection plus the Node's battery-side telemetry; an ESC hitting thermal cutback in normal rental duty indicates wrong gearing or a dragging drivetrain, not a bad ESC — bench-roll the car before swapping electronics.

## 9. Drift Program Deep-Dive

### 9.1 Why drift gets its own chapter

Drift is the only class where the customer is *supposed* to exceed the grip limit at all times. That inverts most of Chapter 6's tuning logic and makes the class disproportionately dependent on geometry, electronics, and surface. Done well, RWD drift is the stickiest repeat-visit product in the division — progressing from "spins instantly" to "links three corners" takes exactly the handful of visits a membership wants it to take.

### 9.2 RWD drift geometry

**RWD versus AWD/CS.** The hobby ran for years on AWD "counter-steer" (CS) chassis — 4WD drivetrains overdriven at the rear (CS ratio ≈ 1.3–2.0, rear wheels turning 30–100% faster than the fronts) so the car breaks traction predictably while the driven front axle keeps it recoverable. CS is easier for a first-timer, and the fleet platform's switchable gearbox could support it if ever needed. The division standardizes on **RWD with gyro** anyway: it is what modern drift competition runs, so the product reads as authentic; the skill ceiling is higher, which the license ladder monetizes; and the rental gyro (Section 9.3) gives novices the recoverability CS hardware used to provide — software solving what gearing once did. AWD/CS exists in this volume only as a documented fallback, not a stocked class.

Modern RC drift is RWD with gyro assistance, mimicking full-size technique. The MST RMX 2.5 S+ fleet spec:

- **Steering angle:** ~65° effective lock. The fronts' job while drifting is to point along the direction of travel (countersteer) while the rear drives the car sideways; insufficient lock is the hard ceiling on drift angle. The RMX's uprights and rack deliver this out of the box.
- **Ackermann:** near-parallel steering (low Ackermann) keeps both fronts at consistent slip when countersteered far beyond normal ranges. Fleet spec sets rack position for slight anti-Ackermann at full lock.
- **Caster & KPI:** 10° caster (adjustable 6–12°) with 6° KPI gives progressive camber gain across the huge steering sweep, keeping the front contact patch usable at full countersteer. High caster also self-centers the steering, cooperating with the gyro rather than fighting it.
- **Weight transfer:** drift initiation is a weight-transfer event. The 46/54 static bias, soft front springs, and heavier rear oil (700 cSt) let throttle lift rotate the car and throttle application settle it — the front/rear damping *split* is the personality dial for how aggressively the chassis initiates.

### 9.3 Gyro doctrine

The gyro applies countersteer faster than any human; the tuning question is how much authority to give it.

| Duty | Gyro gain | Behavior |
|---|---|---|
| Rental / novice | 55–65% | Car self-catches almost every over-rotation; customer learns line and throttle first |
| Intermediate (license-gated) | 45–55% | Customer supplies most countersteer; gyro cleans up |
| Race / competition nights | 30–45% | Judge-visible driver input; club-standard feel |

Gains are set on the (locked) transmitter profile per license tier, not on the car, so any drift car serves any tier. Gyro mounting is standardized (same orientation, foam-tape isolation, loom dressed clear of the spur) because a vibrating gyro oscillates the servo and eats servo gears — a known fleet-killer in drift rentals.

### 9.4 Tires and surface interaction

Drift rings are the one place the control-tire rule meets materials science. Fleet spec: **HDPE rings on the polished-concrete annex** (consistent low grip, ~150-Shift life, cheap), with **ABS as the alternate compound** if the annex is ever refinished smoother — grippier, faster-wearing, more progressive on very slick sealed concrete. Compounds are never mixed in service; a compound change is a class-wide event with a parity re-audit. Surface doctrine: the annex is sealed, dust-mopped before open and between event heats (dust on polished concrete acts as ball bearings), and *never* treated with traction compound. Fronts may run a slightly grippier ring than rears if the class needs steering authority — the one permitted front/rear asymmetry, fixed class-wide.

### 9.5 Drift electronics character

Sensored 13.5T + the drift ESC profiles (Table 5.2) exist for one reason: **wheelspeed control at partial throttle is the entire skill**. High drag brake (40–60%) gives the "off-throttle rotation" that drift technique is built on; sensored commutation removes the low-RPM cogging that makes cheap sensorless systems undriveable sideways. Punch stays moderate — drift launches are irrelevant, but transient throttle response mid-drift matters.

### 9.6 Drift annex requirements (interface to Volume 11)

Racing imposes on the architects: ≥250 m² sealed polished concrete; painted clipping-point dots and outline curbs (no raised curbs — drift cars slide into them side-on); perimeter kick-rail 80 mm high; spectator rail on the long side (drift is a spectator product); lighting to 300 lux minimum for night events; power and mounting for the timing bridge and two fixed cameras (leaderboard replays).

### 9.7 Drift competition scoring

Drift is judged, not timed, and the quarterly competitions run the three-judge club format scaled to a rental fleet:

- **Judged criteria (100 points):** **line** (40) — proximity to the painted clipping points and outside zones on the published judged course; **angle** (30) — sustained drift angle without corrections; **style/commitment** (30) — initiation speed, transition fluidity, no straightening moment. A spin, stalled drift, or two wheels off course zeroes the run.
- **Format:** two qualifying runs per driver (best counts), top 16 into **tandem battles** — lead-and-chase pairs, judges scoring the chase car's ability to mirror the lead; one "one more time" rerun per battle on a split decision.
- **Fleet fairness:** competition cars are drawn by lot from the parity-verified drift fleet, race-profile flashed and readback-verified; drivers may adjust gyro gain within the competition band (30–45%) and nothing else. The battle is between drivers.
- **Scoring capture:** judges score on tablets into the RC WORLD OS events module; scores render live on the leaderboard screens with camera replay, and results feed Gears and license credit like any race (Volume 9).

## 10. Surface-Specific Setup: Touring, Rally & Short-Course

### 10.1 Touring on Track A asphalt

Track A's fine asphalt/polished concrete is a **medium-grip, low-abrasion** surface, which drives the touring baseline in Table 6.5a. Operating guidance beyond the baseline:

- **Grip evolution:** the racing line rubbers in through the day; expect 0.3–0.5 s of "free" laptime by afternoon and a nervous rear in the first morning Shifts. The parity audit runs pre-opening precisely so cars are compared on the green track.
- **Temperature:** spec slicks peak around 35–50 °C surface temperature. Below ~15 °C ambient, add one step of drag brake and advise league drivers to run a heat lap; above 35 °C, watch for greasy mid-corner push and drop ride height 0.5 mm as the standard response.
- **Rain:** Track A drains (Volume 11 crossfall spec) but wet running is a program decision, not a setup decision: rental touring Shifts pause in standing water (electronics are splash-resistant, not submersible; Node conformal coating is not a hull).
- **The racing line:** Track A's reference line — painted faintly at the apexes and taught in coaching — is classic outside-inside-outside geometry: enter wide, apex late on the two corners feeding the main straight (exit speed beats entry speed wherever a straight follows), sacrifice the line only in traffic. The reference driver's telemetry lap is the line's definition of record; coaching (Section 13.7) overlays a customer's Node trace on it corner by corner.
- **Tire management on control tires:** with every car on the identical spec slick, tire condition *is* the remaining tire variable — managed, not tuned: sets stay as sets (Section 4.5), wear dots checked at every turnaround, a damp-cloth wipe at re-tire only. No traction additives, league included; a caught additive is a disqualification, because one treated set breaks parity for everyone racing against it.

### 10.2 Rally/buggy on Track B dirt

Packed dirt watered and rolled daily is a **variable-grip, high-contamination** surface. Standing setup doctrine: chase compliance, not stiffness — thin oils (300/350 cSt), bar-free, full droop, and the 45/55 bias doing the traction work. Operationally:

- **Moisture window:** the track crew waters to "dark but not shiny." Dry-slick afternoons lower grip 20%+; the class response is a −1 pinion (cooler motors working harder against wheelspin) and nothing else — customers adapt faster than setups on dirt.
- **Jump discipline:** rental buggies fly flat off the tabletops at cap speed by design (landing-matched profiles, Volume 11). Cars returning with bent hinge pins or tweaked arms feed the corner-scale check (Section 7.2) at turnaround.
- **Dust:** air filters don't exist on electric cars, but bearings suffer; Track B cars run on the accelerated 150-Shift bearing schedule vs. 300 for Track A (maintenance matrices in Volume 7).

### 10.3 Short-course on Track B

The SCT setup (Table 6.5d) accepts body roll as a feature: the class's forgiving, truck-like motion is what lets mixed grids race door-to-door. The only setup rule that is enforced rigidly is rear toe-in ≥3° — a loose short-course truck at 40 km/h on a crowded grid is the division's highest collision-energy scenario.

### 10.4 Track requirements summary (interface to Volume 11)

| Track | Racing needs (this volume) | Design authority |
|---|---|---|
| A — Asphalt | ~180 m line, 3.5–4.5 m width, drift annex per 9.6, drag straight ≥55 m incl. braking area, timing loop conduit at S/F, rostrum for 10 drivers, 300 lux night lighting (Phase 3 uprated) | Volume 11 |
| B — Baja/Rally | ~160 m line, landing-matched jumps ≤0.5 m, berms, watering system, timing bridge mounts, splash-safe marshal posts | Volume 11 |

## 11. Formula RC & Drag Racing Programs

### 11.1 Formula RC class rules

Formula is run as a strict spec class — the point is precision, not development war:

1. Chassis: fleet F104/TRF103-class pan cars only; no customer chassis in fleet events.
2. Motor: 21.5T sensored, fleet-sealed. ESC: fleet profile "Formula SPEC" (Table 5.2) — **zero timing ("blinky")**, verified by readback before finals.
3. Tires: spec F1 rubber, fleet-issued per event; no additives.
4. Weight: class minimum per current parity sheet; ballast maps only.
5. Contact: open-wheel contact rules — any avoidable contact is a position penalty; two = black flag. (This rule is the driver-education payload of the class.)

### 11.2 Formula event formats

- **Formula Experience** (weekly; gated at Foreman + Motorsport Master endorsement, instructor-supervised): 30-minute guided session — briefing, 2 practice Shifts' worth of track time, 8-minute sprint with grid and podium. Priced as a premium experience, not a Shift.
- **Formula Cup** (monthly): qualifying + two 8-minute finals, grid of 8 (4 fleet cars double-stinted across two semis), championship points into the annual calendar (Section 13.6).

### 11.3 Energy-allocation racing (the power-management format)

The formula program turns the park's founding "F1-style power management" doctrine into an actual race format, built entirely on the RCW Micro-Node's voltage telemetry and PWM intercept:

- **The allocation.** Each race entry buys an **energy budget**, expressed as a percentage of a healthy pack's usable capacity for the race distance (e.g. 85% for a standard final). The Node streams per-car voltage to RC WORLD OS; the race module integrates voltage sag against time-at-throttle into a live consumption estimate, rendered as a shrinking energy bar beside the driver's name on the leaderboard screens.
- **The physics is honest.** Aggressive throttle produces deeper sag and higher integrated draw; a smooth driver genuinely covers the same laps on less budget. The format is a thin scoring layer over real electrochemistry, which is why it teaches real technique.
- **The consequences.** At 100% consumed, the Node's intercept steps the car to a 40% throttle "limp" cap for the remainder — running out of fuel on the last lap, visible and dramatic without stranding the car. Budget remaining at the flag converts to bonus points, so the strategy space is push-versus-conserve.
- **Where it runs.** Standard in Formula Cup finals and as a touring league-night variant ("Eco-GP"). Deliberately *not* used in walk-up Shifts — novices should learn throttle before strategy — but the same telemetry drives the smoothness statistics on every customer's post-Shift report (Volume 9).

> **Field Note.** Energy racing quietly solves an operations problem too: it is the only format where the *slower* driving style wins races, which makes it the best teaching format for customers who arrive throttle-happy and the cheapest race night on the fleet — motor temperatures and crash rates both drop measurably.

### 11.4 Drag racing class rules

1. Strip: **40.2 m (scale 132 ft)** measured, plus ≥15 m braking runoff; paired lanes 1.2 m wide; centerline no-cross rule (crossing = loss).
2. Cars: fleet drag cars only for open events; "run what you brung" exhibition nights for member-owned cars under scrutineering (wheelie bar mandatory, battery ≤3S, LiPo condition inspected — park battery doctrine applies to guest packs without exception).
3. Starts: staged on the Christmas tree per Section 11.5; red light = loss.
4. Rental format: customers never free-drive; a staged launch with speed-limited profile lets any license tier take a pass safely.

### 11.5 The strip, staging and reaction timing

Track A's main straight doubles as the strip: 40.2 m race distance fits inside the ≥55 m straight with braking area (Section 10.4). Timing: staged beams at launch, mid, and trap connected to the timing system's drag module; the RCW Node's telemetry provides trap-speed corroboration and the kill-switch covers a brake failure into the runoff (geofence hard-stop at the barrier line).

**Staging procedure.** Cars are placed by the lane marshal (never the customer) with the nose breaking the pre-stage beam, then rolled forward to stage — both beams lit, both lanes staged, tree armed. The fleet runs a **sportsman tree** (three ambers at 0.5 s intervals, then green); leaving before green trips the red light and forfeits the run. **Reaction time** is measured from green to the launch beam clearing and published alongside elapsed time (ET) on every slip — anticipation and release is a skill requiring zero throttle talent, so the format works at every license tier. League drag runs **bracket rules** (dial-in your predicted ET; breakout = loss) so mismatched cars and drivers still produce close racing — the drag program's own version of the parity doctrine.

### 11.6 Why these programs exist at 4 cars each

Neither class earns walk-up Shift revenue; both earn **event nights, license aspirations, and media**. Eight special-event cars generate the imagery that sells the other 56 — Volume 10 treats them as marketing-adjacent assets with event-revenue offset, and Chapter 14's utilization KPI excludes them from the denominator.

## 12. Rental Fleet Engineering & the Shift Turnaround

### 12.1 Transmitter standardization and lockout

The transmitter is the customer's entire interface with the division, and it is fleet property, never customer property, for Shift rentals. Standards:

- **One transmitter model park-wide for surface vehicles** (4-channel 2.4 GHz surface radio with model memory, EPA, dual rate, physical menu lockout — procurement spec in Volume 8). One model means one Toolbox Talk diagram, one battery type, one spare pool.
- **Menu lockout is physical and procedural:** menu access disabled on customer units (button combination set and taped internally where supported; units audited weekly). Customers get steering wheel, throttle trigger, and nothing else that changes state.
- **Rate limiting by license tier is a transmitter profile, not a car change.** Steering EPA and throttle EPA/curve are pre-programmed per transmitter profile (Volume 9 §3.6): Rookie for Learner/Apprentice (steering 75%, throttle 60%, softened center), Standard for Operator (90/80), Licensed for Foreman+ (100/100 within class caps). The transmitter binds to the car at the counter by QR scan (RC WORLD OS pairs `asset_tag` to transmitter ID and writes the session to the queue roster) and refuses a pairing whose profile exceeds the customer's license tier.
- **The RCW Node is the enforcement backstop.** Whatever the transmitter commands, the Micro-Node's PWM intercept enforces the park-side rules: under-voltage throttle-back at 3.4 V/cell, geofence kill at track boundaries, remote kill from the director's console, and telemetry streaming to RC WORLD OS over the Wi-Fi mesh. Transmitter EPA shapes the *experience*; the Node guarantees the *limits*. Gyro-stability aids, where a class uses them (drift gyro; optional steering assist on entry class), are configured on the car and license-gated the same way.

### 12.2 The hardening pass (car induction)

Every car entering the fleet receives the standard hardening pass at The Works before its first Shift. Per class it varies in detail (Chapter 2 notes); structurally it is always:

1. Full fastener pass with threadlock on metal-to-metal; nylon-insert nuts on suspension pivots.
2. Known-weak-point upgrades fitted (per platform list in Volume 7, Chapter 5: TT-02 bearing/steel-pinion/oil-shock set; 144010 metal knuckles and steel main gear; SCT servo-saver spring uprated).
3. Electronics: fleet ESC/servo installed (1/10 classes), connectors converted to XT60, wiring loomed and strain-relieved, RCW Micro-Node soldered inline with conformal coat verified, receiver bound to the fleet radio system.
4. Body prep per Section 12.3; asset tagging per Section 12.4.
5. ESC profile written and verified (SOP-MS-001), baseline setup sheet applied (Chapter 6), corner-weighted (Chapter 7), motor benched and binned (Chapter 4).
6. Induction parity run: the car must land within 1.5% of class median before its first customer.

### 12.3 Damage-resistant body strategy

Bodies absorb the first hit, so bodies are engineered as consumables with a service life, not decorations:

- **Material:** polycarbonate (Lexan) only — 1.0 mm standard, 1.5 mm on SCT/buggy where available. No hard-plastic display bodies on rental cars, ever.
- **Reinforcement at prep:** shoe-goo/mesh laminate on nose and wheel arches; polycarbonate doublers and rubber grommets at body-post holes; front splitters trimmed back 5 mm for curb clearance.
- **Paint:** backside-painted (scratches don't show), fleet livery with class color coding and large car numbers readable at 30 m.
- **Wheelie bars** where apt: mandatory on drag cars, fitted to SCT and buggy rentals where the platform accepts them — they save rear body sections and stop novice throttle-stab flips.
- **Life and rotation:** bodies are tagged assets in RC WORLD OS; a body retires at the third structural repair or when cracks reach a wheel arch. Two spare painted bodies per 4 cars per class sit prepped in The Works, so a body swap is a 90-second turnaround action.

### 12.4 Asset tagging and telemetry integration

Every car carries three identities that must always agree: the **physical asset tag** (laser-etched QR + human-readable ID, e.g. `MS-T-04`, on chassis and body), the **RCW Node MAC** (the telemetry identity in `fleet_inventory`), and the **timing transponder ID** (Section 13.3). RC WORLD OS is the master record: lifecycle status (seven states: available → bound → on_track → pit → maintenance → charging → retired; see Volume 13 §6.3), total Shifts run, motor/ESC/tire sub-asset histories, last parity result, last profile write. The Node makes the car self-reporting: voltage and position land in `live_telemetry`, lap crossings corroborate the timing system, and the maintenance module opens flags on runtime thresholds (Volume 7; KPI hooks in Chapter 14).

### 12.5 The Shift turnaround

The Shift is the park's 20-minute billing block; motorsport runs a **25-minute wheel: 20 minutes on track, 5 minutes turnaround**. The turnaround is a pit crew operation with a fixed sequence — two Artisans per track handle 8+ concurrent cars because the sequence never varies:

**Checklist 12.5 — Between-Shift turnaround (per car, target ≤4 minutes)**

- [ ] Receive car and transmitter; scan asset tag to close the session in RC WORLD OS
- [ ] Battery out → voltage check → to charging bunker trolley (LiPo doctrine: ~30% buffer expected on a Casual Shift; log any pack below 3.5 V/cell as an over-drain event against the session)
- [ ] 20-second visual: wheels/tires (wear dots, glue joints), arms/knuckles/links (grab-and-wiggle), body damage grade (A/B/C), loose fasteners
- [ ] IR temp spot-check on motor if the car ran hard (>85 °C = pull and re-gear, Section 8.3)
- [ ] Blow down chassis (Track B cars: bearing dust check)
- [ ] Fresh pool battery in; connector fully seated; strap secure
- [ ] Node handshake confirmed in OS (voltage reporting, geofence armed)
- [ ] Radio function check: steering left-right, throttle blip on stand, brake, kill-switch ping
- [ ] Setup sheet still matches (springs/tires haven't been "borrowed" — it happens)
- [ ] Status flip to *active* in OS → car to the ready line; or *maintenance* with a one-line fault note → car to The Works trolley

Cars flagged C-grade body or any mechanical fault leave the pool immediately; the 64-car fleet against ~22 track slots exists precisely so a pulled car never cancels a booking (Section 2.9).

**Battery logistics inside the wheel.** The turnaround runs the park's 3:1 battery doctrine made physical: one pack in the car, one charging in the bunker, one rested on the pit-lane ready rack. Packs are pooled *per class*, not per car, and each pack's ID is scanned into the session record at installation, so Node voltage telemetry is always attributable to a specific pack's history. Two hard rules bound the flow: **no pack charges anywhere except the bunker** (the pit-lane rack is staging only), and **no pack rests less than 20 minutes between charge completion and installation** (warm packs sag differently and would quietly break parity). The Operator Shift's theatrical mid-session battery swap draws from the same rack under the same rules — the theatre is real logistics performed in view. Pack retirement, internal-resistance tracking, and bunker fire procedures are Volume 7's jurisdiction.

> **Safety Warning.** A pack returning from a session below 3.4 V/cell means two independent guards failed or were bypassed. That is never treated as a battery event only: the car's ESC cutoff and its Node are both bench-verified before the car re-enters the pool, and the session log is reviewed to establish how it happened. Chronic over-drain clustering on one car is an electronics fault; clustering on one *customer* is a Toolbox Talk and license-tier conversation (Volume 9).

### 12.6 Daily fleet-readiness

**Checklist 12.6 — Motorsport daily opening (fleet portion, before first Shift)**

- [ ] Charging bunker log reviewed: overnight storage-charge state confirmed, no swollen/hot packs, day's first rotation staged at 3:1 ratio
- [ ] Every ready-line car: tire life check against Shift ledger, wheel-nut torque pass, battery-strap and connector inspection
- [ ] One reference car per class driven 3 laps by opening Artisan — track and car sanity check; time logged (drift >0.5 s from yesterday's reference = investigate surface or car before opening)
- [ ] All Nodes reporting on the mesh (OS fleet map shows green for every ready-line car); any silent Node = car pulled
- [ ] Transmitter pool: count, battery trays swapped, tier profiles spot-audited on two random units
- [ ] Timing system self-test: decoder up, test transponder pass registered on both tracks
- [ ] Track walk: Track A swept/dust-mopped (drift annex mandatory), Track B watered and rolled, barriers seated, marshal points equipped (hooks, flags, spare body clips)
- [ ] Tow-Truck Retrieval crawlers: charged, winches function-checked (customers meet these on their worst moment — they must always work)
- [ ] Maintenance queue reviewed: yesterday's pulls triaged with The Works; today's expected returns confirmed
- [ ] Parity audit due today? (rolling schedule, SOP-MS-002) — if yes, completed before opening

### 12.7 Weekly deep-check

**Checklist 12.7 — Weekly fleet deep-check (per class, alongside the parity audit)**

- [ ] Corner-weight verification on 3 random cars per class (full fleet monthly)
- [ ] Shock pairs rebound-matched on any car reported "inconsistent" during the week
- [ ] Drivetrain free-roll test: chassis on stand, timed spin-down; outliers get bearing/diff inspection
- [ ] ESC profile readback on 25% of the class (full class after any event night)
- [ ] Transmitter EPA/profile audit across the pool (menu-lockout integrity check)
- [ ] Tire ledger reconciliation: paint-dot ages vs. OS Shift counts; retire due sets
- [ ] Body fleet review: regrade, pull third-repair bodies, restock prepped spares to 2-per-4-cars
- [ ] Battery pool: internal-resistance spot check on 10% of packs; retire per battery doctrine (Volume 7)
- [ ] Spares min/max review against parts-per-100-Shifts consumption (Chapter 14 KPI feed)
- [ ] Node firmware/telemetry health report reviewed with the OS team

### 12.8 Damage triage, retirement and parts harvesting

**Damage triage classes.** Every incident-returned car is triaged at the turnaround bench into one of three classes, logged against the session:

| Class | Definition | Disposition | Target resolution |
|---|---|---|---|
| **A — Cosmetic** | Body scuffs/cracks short of a wheel arch, bent body clips, scraped bumper foam, tire scrub marks | Stays in service; body regrade noted; swap to prepped spare body at next natural pause | Same wheel cycle |
| **B — Serviceable** | Bent steering link, popped ball cup, torn arm, stripped servo saver, suspected shock leak, any "feels wrong" report | Pulled to *maintenance*; pit-lane repair if <10 min from stocked spares, else to The Works trolley | Same day |
| **C — Structural** | Cracked chassis/tub, bent motor mount or bulkhead, drivetrain lock, water ingress, any electronics fault, post-crash geometry that fails the corner-scale check | Out of pool; work order in RC WORLD OS; parity re-run mandatory before return | ≤72 h or retirement review |

Class B/C events feed the MTBF KPI (Chapter 14); Class A does not. A car with three Class C events in a rolling 90 days triggers the same retirement review as a triple quarantine (Section 4.9).

**Retirement criteria.** A car retires when any of the following holds: (1) cumulative repair spend reaches **60% of replacement landed cost** (tracked per asset by the OS); (2) structural tub/chassis damage on a platform where the tub is the car (touring, drift); (3) triple quarantine or triple Class C review concludes "cannot be trusted"; (4) platform end-of-life — spares supply below two active sources (the WLtoys consumable doctrine reaches this by design and answers it with donor stock); or (5) fleet refresh economics — Volume 10's depreciation assumes a 3-year/2,000-Shift service life for 1/10 classes and 18-month/1,200-Shift for the 1/14 classes.

**Parts harvesting.** Retired cars go to the harvest bench at The Works, never to a skip whole: electronics (ESC, servo, receiver, Node) are re-flashed and re-tagged; motors re-benched and binned or stripped for sensor boards and bearings; unworn suspension and drivetrain parts return to stock as *used-serviceable* (marked, never mixed with new in min/max counts); batteries join the pack-retirement stream (Volume 7); bodies and tires are binned. A harvested touring car typically returns $60–90 of stock value, closed against the asset as a salvage credit in Volume 10's depreciation model. Bare chassis with life left become training mules for Artisan certification builds (Volume 7).

**Transmitter management and hygiene.** Transmitters live on a numbered charging wall behind the counter, checked out per session with a wrist lanyard. Between sessions every unit gets a 30-second wipe-down (alcohol-free disinfectant on grips, wheel, trigger — alcohol clouds polycarbonate and perishes foam) and a drop inspection; the pool carries 20% spare units so cleaning or damage never shortens the ready line. Foam wheel covers are consumables, replaced monthly or immediately when torn. Any unit with a suspected fault (glitchy steering report, drop onto concrete) is bench-checked against a reference receiver before rejoining the wall — radio faults masquerade as car faults and waste bench hours if the pool is not policed.

## 13. Race Operations

### 13.1 Race formats

The division runs four customer-facing competition formats, tiered to the license ladder:

- **Sprint races** (daily, walk-up): 6–8 minute heats inside a standard Shift slot, grid formed from the queue, class-locked. Results post to the leaderboard and earn Gears — any Apprentice-or-higher customer's Shift can become a race.
- **Endurance events** (monthly): 30–60 minute team races (2–3 drivers per car) with mandatory pit windows for the Artisan battery swap. Endurance sells memberships: it requires teammates.
- **Ladder leagues** (six-week seasons): weekly heats, points, promotion/relegation between Rookie/Clubman/Pro divisions per class — the retention backbone (Volume 9 ties standing to license tier and Gears multipliers).
- **Special-event formats:** Formula Cup and drag brackets (Chapter 11), drift competitions judged on line/angle/style (three-judge club format), and the seasonal championship (Section 13.6).

### 13.2 Race-day track configuration

Racing overlays the rental layout rather than replacing it: sprint races run the standard circuits; league and championship nights may invert Track A's direction (a cheap "new track" — barriers and rostrum sightlines are designed for bidirectional running, Volume 11) and add the chicane kit on the main straight. The drag strip build (Christmas tree, staging beams, lane dots) is a 20-minute crew task documented as a rigging checklist in the race director's binder.

### 13.3 Timing systems

Verified against the July 2026 market, the division runs a two-tier timing architecture:

- **Tier 1 (both tracks, permanent): MYLAPS RC4** — the industry-standard inductive-loop system: detection loop embedded at start/finish (conduit cast at construction — Volume 11), RC4 decoder per track, 0.001 s resolution, rated beyond any fleet speed. Every fleet car carries a wired RC4-class transponder powered from the receiver rail; transponder ID is a field on the asset record. MYLAPS ships no scoring software; the division runs a compatible package (LiveTime Scoring / RC Scoring Pro class) feeding RC WORLD OS leaderboards via API.
- **Tier 2 (drift annex + drag module + backup): EasyLap-class IR** — the low-cost infrared system (transponder LED in the car, receiver bridge over the line, Zround/LiveTime software). IR needs line-of-sight, so transponders mount under the body window. The drag strip's staged beams integrate here.
- **Corroboration:** RCW Node geofenced lap detection provides a third, park-owned lap record — not race-grade timing, but enough to sanity-check the leaderboard and to keep casual Shift lap counts flowing when a customer's car runs outside race sessions.

**Options evaluated and rejected.** UHF **RFID timing** (passive tags, reader antenna at the line — the architecture of running events and some kart tracks) was evaluated as a cheap middle tier: tags cost cents and survive crashes, but read reliability degrades at RC closing speeds with multiple cars in the window, and ~0.1 s-class resolution is marginal against a 22-second lap where podium gaps run hundredths. It stays on file for paddock asset-tracking only. Relying on the **RCW Node alone** was also rejected for race duty: GPS geofencing is meters-class and Wi-Fi hand-off jitter adds tens of milliseconds — fine for Shift lap counts, not for declaring a winner by 0.02 s. The doctrine: **the Node observes every lap; MYLAPS-class timing declares race results.**

Cost note for the financial model: the RC4-class system is the expensive tier (system-plus-transponders is a four-figure system cost and transponders run ~$100-class each across 64 cars — Volume 8 carries the negotiated numbers); the IR tier is an order of magnitude cheaper. The split architecture buys race-grade credibility where customers see it and economy where they don't.

### 13.4 Marshaling

Marshals are staff (customers never walk onto live tracks — park doctrine; a dead car in a rental session triggers the Tow-Truck Retrieval Protocol instead). Race sessions run two marshal posts per track at the designed refuge points, equipped with recovery hooks (reach, don't step), spare body clips, and a radio to the race director. Rules of engagement: recover *between* packs, never into traffic; a car that can't be made safe in 5 seconds is lifted out and rejoins from pit lane; any barrier breach red-flags the session pending reseat.

### 13.5 SOP-MS-003 — Race Director: Session Operations

| | |
|---|---|
| **SOP ID** | SOP-MS-003 |
| **Revision** | 1.0 (July 2026) |
| **Owner** | Motorsport Lead (delegable to certified Race Director on duty) |
| **PPE** | Track-standard; marshals hi-vis |
| **Tools** | Director console (RC WORLD OS race module + timing software + Node kill-switch panel), PA, flag set, two charged marshal radios |
| **Frequency** | Every competition session |

1. Pre-session (T−30): confirm class car pool parity-current (last audit ≤7 days); ESC profiles per class rules verified by readback sample (2 cars minimum, all finalists before finals); timing decoder test pass; marshal posts staffed and radio-checked.
2. Drivers' briefing (T−10): format, flags, contact rules, pit-lane direction, where marshals are, what the kill-switch means. Every driver confirms Toolbox Talk induction current in OS.
3. Grid formation: OS race module assigns cars and transponder IDs to drivers; scan-pair transmitters; stage on grid.
4. Session start: timing armed → grid released per format (standing start touring; rolling for SCT mixed grids; tree for drag).
5. During session: director monitors timing feed + Node telemetry map; enforces flags (yellow = local hazard, no passing between posts; red = all stop, throttle-kill via Node panel if not obeyed within 3 s).
6. Incidents: log every red flag and every contact penalty in the OS incident register during the session, not after.
7. Session end: results confirmed in timing software → published to leaderboard → Gears/license credits post automatically. Announce podium; direct cars to parc fermé for post-race spot checks (profile readback on winners — the parity promise is audited *at the podium*, visibly).
8. Post-session (T+15): cars to turnaround; RACE→RENTAL profile reversions executed and two-person verified (SOP-MS-001 step 5); director's session report closed in OS.

### 13.6 Championship calendar and night racing

The annual calendar gives the leagues somewhere to go: four **six-week league seasons** per year per major class, punctuated by monthly endurance rounds, the Formula Cup series, quarterly drift competitions, two drag bracket nights per quarter, and a season-ending **RC WORLD Championship weekend** that doubles as the park's flagship marketing event (Volume 2). **Night racing** is a Phase 3 unlock (permanent track lighting is Phase 3 capex per park canon); until then, two "twilight league" pilots per year run under temporary event lighting to build the case and the content. Drift under lights is the priority night product.

### 13.7 Coaching and spectator products

Two adjacencies round out race operations. **Coaching:** thirty-minute one-on-one sessions with a certified staff driver, priced at a premium over a normal Shift and structured around telemetry the customer already generates — the coach overlays the driver's Node speed trace on the class reference lap, sets one corner as the objective, and re-measures at the end. It converts the park's data exhaust into a product and is the natural upsell for a league driver stuck mid-division. **Spectating:** sprint heats and league nights are free from the rails (spectators become customers); championship weekends and drift/drag nights ticket the Phase 2 grandstand. The director's live-timing feed mirrors to the public screens with a 10-second delay, so an incident is marshaled before it is broadcast.

> **Investor Note.** Competition revenue is deliberately modeled as secondary to Shift revenue (entries, spectator F&B uplift, event sponsorship — Volume 10), but its strategic value is retention: league drivers pre-book the same night for six weeks, and the license ladder they climb is priced in memberships. The division's racing calendar is a subscription engine wearing a sporting costume.

## 14. Division KPIs & Dashboard

### 14.1 KPI definitions

Five numbers, defined precisely so they cannot be gamed, reviewed weekly by the Motorsport Lead and monthly at park level:

1. **Utilization per car** = billed Shifts ÷ available Shift slots per car (operating hours × 2.0 practical Shifts/hour, cars in *active* status). Fleet target ≥ 55% weekday, ≥ 80% weekend. Special-event cars (formula/drag) are excluded from the denominator (Section 11.6).
2. **Cost per Shift** = (division direct labor + parts consumed + battery amortization + fleet depreciation) ÷ billed Shifts. Target ≤ $4.10 at Year-1 volumes against the $15 Casual Shift anchor. Illustrative build-up: labor ~$1.90, parts ~$0.85, battery amortization ~$0.45, fleet depreciation ~$0.70 (landed cost + hardening over a 3-year/2,000-Shift life), consumables ~$0.20. Full costing model in Volume 10; the division owns the levers (labor via turnaround efficiency, parts via MTBF, batteries via over-drain discipline).
3. **MTBF (Shifts)** = billed Shifts ÷ failures requiring a car pull. Class targets: touring ≥ 120, entry ≥ 90, drift ≥ 150, buggy ≥ 70, SCT ≥ 100. Buggy's lower target is priced into its consumable-platform doctrine.
4. **Parts cost per 100 Shifts** = spares consumed (at landed cost) × 100 ÷ billed Shifts, per class. Feeds spares min/max (Checklist 12.7) and the procurement forecast (Volume 8).
5. **Parity spread** (SOP-MS-002 weekly result) — the doctrine number itself, trended per class.

### 14.2 Mini dashboard

The RC WORLD OS motorsport dashboard renders the weekly view in exactly this shape (illustrative Year-1 steady-state values):

| Class | Cars active | Utilization | Cost/Shift | MTBF (Shifts) | Parts $/100 Shifts | Parity spread |
|---|---|---|---|---|---|---|
| Entry 1/14 | 10 | 78% | $2.60 | 95 | $18 | 2.4% |
| Touring/GT | 14 | 71% | $3.90 | 130 | $31 | 1.6% |
| Drift | 12 | 64% | $3.40 | 160 | $22 | 1.9% |
| Buggy/Rally | 12 | 74% | $3.10 | 75 | $38 | 2.7% |
| Short-course | 8 | 61% | $4.30 | 105 | $34 | 2.2% |
| Formula/Drag | 8 (event) | event-based | per event | n/a | per event | 1.4% |
| **Division** | **64** | **≥65% blended** | **≤$4.10** | **per class** | **trend ↓** | **≤3.0% all classes** |

Red lines: any class parity >3.0% (immediate re-audit), utilization <45% for two consecutive weeks (pricing/queue review with the GM), MTBF trending down 20% month-over-month (engineering review with The Works), parts $/100 Shifts up 25% (failure-mode investigation before reorder).

## 15. Volume Summary & Cross-References

The Motorsport Division converts a standardized 64-car fleet into the park's highest-throughput revenue engine by holding one engineering promise: any car a customer is handed is within 2–3% of the fastest car in its class, so the race is theirs to win. This volume specified the class ladder; the four-platform standardization strategy and its ~130-SKU spares consequence; the parity engineering method (control tires, motor binning, ESC readback discipline, ballast equalization, gearing trim) with a worked three-car example landing at 1.4% spread and formal quarantine rules; the full tuning apparatus — ESC profile tables, suspension baselines and effects tables, corner weighting with a worked ballast calculation, rollout mathematics and thermal rules; the drift, touring, rally and special-event programs including energy-allocation racing; the rental hardening, transmitter lockout, RCW Node enforcement, Shift turnaround and lifecycle machinery; race operations from sprint heats to the championship weekend; and the five-KPI dashboard the division is managed by.

**Maintenance interface note.** This volume defines *what* the fleet must do and *how it is configured*; Volume 7 defines *how it is kept doing it* — preventive-maintenance matrices, teardown/rebuild procedures per platform, the motor bench build-out (Section 4.3), battery pool management, failure-mode catalogue and FMEA, and Artisan training. The hard handshake: every car pull recorded at turnaround (Checklist 12.5) opens a work order in RC WORLD OS that The Works must close against Volume 7's procedures, and no car returns to *active* without the closing Artisan's sign-off plus, after major work, a parity re-run under SOP-MS-002. See **Volume 7, Chapters 4–5**.

**Cross-references.**

- **Volume 2** — market sizing and competitor scan behind the class ladder's demand assumptions; marketing/sponsorship programs the racing calendar feeds.
- **Volume 4** — Construction Division; Track C crawler program and the recovery-crawler fleet that executes the Tow-Truck Retrieval Protocol on motorsport tracks.
- **Volume 7** — Engineering & Workshop Manual (see maintenance interface note above); custom-build practices behind the drag conversions.
- **Volume 8** — Procurement Handbook: supplier negotiations and landed costs for MST, MJX/LDRC, WLtoys, Carten/Tamiya-class chassis, Hobbywing/Surpass electronics, Gens Ace/CNHL batteries, MYLAPS/EasyLap timing.
- **Volume 9** — Customer Experience & Loyalty: the RC WORLD License tiers that gate transmitter profiles (Section 12.1), Gears earning from races, league-membership mechanics.
- **Volume 10** — Finance: division revenue model, cost-per-Shift build-up, timing-system and fleet capex lines.
- **Volume 11** — Architecture & Park Design: Tracks A/B construction, drift annex and drag straight geometry, barriers, rostrums, timing-loop conduits, lighting phases.
- **Volume 12** — Franchise Manual: which parts of this volume are franchise-mandatory doctrine (parity method, safety architecture) versus locally adaptable (class mix, calendar).



