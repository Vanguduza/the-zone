# Volume 10 — Finance

**RC WORLD — Master Development Plan** · Volume 10 of 13
**Revision 1.0 — July 2026** · Status: Living document — bump revision on material change

**Purpose of this volume.** This volume is the financial source of truth for the entire Master Development Plan. Every capex figure, revenue projection, cost assumption, and return metric quoted anywhere in Volumes 1–13 reconciles to the models built here. It constructs, line by line, the Phase 1 startup budget of ≈$1.85 M; the $2.6 M funding ask and its tranche structure; a bottom-up revenue engine that lands on the canonical Year 1 ≈$1.28 M, Year 3 ≈$2.6 M, and Year 5 ≈$3.4 M; the operating cost stack that yields a 24–28% EBITDA margin from Year 3; the monthly cash model that shows operating break-even at Month 16–19; and the profitability, sensitivity, and scenario apparatus an investor's analyst will want to stress. Every major claim is carried by a table, with the assumptions stated above it and the arithmetic shown so a CFO can audit it with a calculator. Where this volume and any other volume disagree on a number, this volume governs, and the other volume must be corrected.

**Intended readers.** Investors and lenders performing diligence on the $2.6 M ask; the founder and General Manager, who own this model and update it monthly against actuals; the finance/administration hire, for whom Chapters 4–7 are the operating manual of the company's numbers; franchise developers, who will rebuild Chapter 4's engine with local inputs (see Volume 12, Chapter 3); the RC WORLD OS team, who implement Chapter 10's KPI dashboard (see Volume 13).

**Chapters**

1. Financial Summary & Reading Guide
2. Startup Budget — Phase 1 Capex
3. Funding Plan
4. Revenue Model
5. Operating Cost Model
6. Cash Flow & Break-Even
7. Profitability & ROI
8. Pricing Strategy & Elasticity
9. Sensitivity Analysis
10. Growth Scenarios
11. Volume summary & cross-references

---

## 1. Financial Summary & Reading Guide

### 1.1 The headline dashboard

Everything an investor needs to hold in their head about RC WORLD's finances fits in one table. Every figure below is derived — not asserted — in the chapter cited, and each derivation reconciles to the canonical numbers fixed in the park's style guide.

| Metric | Base-case value | Derived in |
|---|---|---|
| Phase 1 capex ("Core Park", Months 0–12) | **≈ $1.85 M** ($1,850 K) | Chapter 2 |
| Phase 2 capex ("Full Park", Months 13–30) | **≈ $1.15 M** ($1,150 K) | §2.12 |
| Phase 3 capex ("Destination & Beyond", Months 31–60) | **≈ $0.9 M** ($900 K) | §2.12 |
| Five-year program capex | **≈ $3.9 M** | §2.12 |
| Funding ask (equity/quasi-equity, staged tranches) | **$2.6 M** | Chapter 3 |
| Year 1 revenue | **≈ $1.28 M** | Chapter 4 |
| Year 3 revenue | **≈ $2.6 M** | §4.9 |
| Year 5 revenue | **≈ $3.4 M** | §4.9 |
| EBITDA margin, Year 3 onward | **24–28%** (24.2% Y3 → 27.4% Y5) | Chapter 7 |
| Monthly operating break-even | **operating Month 16–19** (base model: Month 16) | Chapter 6 |
| Full payback of invested capital | **Year 4–5** (base: operating Month ~53 on Phase 1 capital) | §7.4 |
| Minimum modelled cash position | $476 K (Month 14) vs $250 K policy floor | §6.4 |

> **Investor Note.** The single most important structural fact in this volume: RC WORLD is an **infrastructure-light, fleet-cheap, labor-and-experience business**. The entire Phase 1 powered fleet — roughly 150 vehicles including batteries, radios, and opening spares — costs $80 K, i.e. **4.3% of Phase 1 capex**. The expensive things (earthworks, buildings, tracks) last 10–20 years; the things customers wear out (cars, gears, tires, batteries) are cheap, sourced wholesale from China, and replaced from operating cash flow. This inversion — durable capex, disposable fleet — is why the model survives the stress tests in Chapter 9.

### 1.2 Modelling conventions

Stated once here; they apply to every table in this volume.

| Convention | Value | Rationale |
|---|---|---|
| Currency | USD throughout, **nominal** (no inflation indexing) | Style-guide canon; nominal keeps tables auditable. Local-currency conversion is a franchise-localization task (Volume 12) |
| Geography baseline | Mid-size international city, metro 1.0–2.5 M (worked at 1.5 M), peri-urban 4.8 ha leased site | Canon; demand analysis in Volume 2, Chapter 9 (§9.4–9.5) |
| Month frames | Build phasing uses the **project frame** (Phase 1 = project Months 0–12, park opens at project Month 12; Phase 2 = project Months 13–30; Phase 3 = project Months 31–60). All financial statements and division opening schedules in this volume use the **operating frame**: M1 = the opening month. Frames are labelled wherever ambiguity is possible | Style-guide month-numbering convention |
| "Year 1" | First full operating year, opening assumed **Month 1 = March** (northern-temperate seasonality; shift the curve, not the totals, for other climates) | Style guide dating: plan written July 2026 |
| Operating calendar | 360 operating days/year (5 maintenance closure days), 8 revenue hours/day average (10 weekend, 6–7 midweek) | Division operating doctrine, Volumes 3–6 |
| Tax | **25% flat placeholder — verify locally.** Loss carryforward assumed available | Corporate rates in candidate jurisdictions span ~15–35%; the placeholder is deliberately mid-range and flagged in every after-tax table |
| Units of account | Tables in **$ thousands ($K)** unless stated | Readability |
| Rounding | Line items rounded to $0.1–1 K; columns are constructed to sum exactly as printed | Auditability |
| Depreciation | Fleet & RCW Nodes 2–3 yr; IT 4 yr; software 5 yr; FF&E 6 yr; tracks 10 yr; site works 15 yr; buildings 18 yr | §7.3 policy table |
| Payment mix | ~85% card/app, ~2.2% blended processing fee | Carried in software/payments opex line, §5.5 |

### 1.3 How this volume reconciles — a reading guide

The volume is a single connected model, and the joins are explicit. Chapter 2 builds capex bottom-up to $1,850 K and shows the Phase 2/3 envelopes summing the five-year program to $3,900 K. Chapter 3 shows the $2.6 M ask as Phase 1 capex plus $750 K of working capital, operating funding, and reserve — the same $750 K that appears as opening cash in Chapter 6's monthly cash model. Chapter 4's revenue engine multiplies visitor volumes by the canonical price card and reconciles monthly to $1,280 K in Year 1 and annually to the five-year canon; its Year-1 visit base also reconciles with Volume 2's independent ~37,000–43,000-visit Year-1 demand estimate (Chapter 9). Chapter 5's cost stack subtracts from Chapter 4's revenue to give the EBITDA row that Chapter 6 spreads monthly (break-even Month 16) and Chapter 7 carries into the P&L (margins 24.2–27.4% from Year 3, payback Year 4–5). Chapters 8–10 stress the same model rather than building new ones. A reader with one hour should read §1.1, §2.1, §3.1, §4.9, §6.3, and §7.1.

---

## 2. Startup Budget — Phase 1 Capex

### 2.1 Summary build-up to ≈$1.85 M

Assumptions: 4.8 ha flat peri-urban leased site with municipal power and water at the boundary (site brief, Volume 11, Chapter 2); construction in a mid-cost international market (blended civil rates ~$55–90/m² for external works, light industrial building rates ~$450–560/m²); fleet and electronics sourced wholesale from China per Volume 8; all pre-opening costs capitalized. Contingency is held at 10.0% of the subtotal, consistent with a design-complete, competitively-tendered civil package.

| # | Category | $K | % of total | Detail |
|---|---|---|---|---|
| A | Site works & earthworks (per zone) | 455 | 24.6% | §2.2 |
| B | Track & operating surfaces | 172 | 9.3% | §2.3 |
| C | Buildings (entry pavilion, The Works, charging bunker) | 418 | 22.6% | §2.4 |
| D | Fleet acquisition (~150 powered assets + batteries + spares) | 80 | 4.3% | §2.5 |
| E | RCW Node telemetry program | 25 | 1.4% | §2.6 |
| F | Wi-Fi mesh & IT infrastructure | 87 | 4.7% | §2.7 |
| G | RC WORLD OS v1 development | 165 | 8.9% | §2.8 |
| H | FF&E, workshop equipment & theming | 118 | 6.4% | §2.9 |
| I | Pre-opening (staff, training, marketing, licences) | 162 | 8.8% | §2.10 |
| | **Subtotal** | **1,682** | 90.9% | A+…+I |
| J | Contingency @ 10.0% of subtotal | 168 | 9.1% | §2.11 |
| | **Phase 1 capex total** | **1,850** | 100.0% | **≈ $1.85 M ✓ canon** |

Arithmetic check: 455 + 172 + 418 + 80 + 25 + 87 + 165 + 118 + 162 = 1,682; 1,682 × 10.0% = 168.2 → 168; 1,682 + 168 = **1,850**.

### 2.2 Site works & earthworks — $455 K

Assumptions: flat site with 2–4% natural grade (canon) minimizes cut/fill; the Mining Zone pit is the only deep excavation and its spoil is reused for Track B berms and spectator mounds (a deliberate double-use that Volume 11 details); haul roads graded to the canonical ≤15° maximum incline; drainage sized for the pond-free Phase 1 (the Marine pond is Phase 2).

| Line | Scope | $K |
|---|---|---|
| Bulk earthworks & grading | Whole-site strip, cut/fill balance, Mining Zone pit excavation & benching, compaction | 118 |
| Drainage, stormwater & utilities | Perimeter swales, culverts, detention basin; power/water/data trenching from boundary to all zones | 96 |
| Internal roads, paths & parking | Gravel service road loop, pedestrian paths, 88-bay gravel car park (Phase 1; expands to 132 bays + 4 bus bays in Phase 2, §2.12, per Volume 11), entrance apron | 62 |
| Mining Zone civil fit-out | Graded haul roads (≤15°), aggregate beds (loose sand → 10 mm crushed stone), central hopper foundation & load-cell pad | 54 |
| Agriculture Zone civil fit-out | Field grading, imported soil & row formation, irrigation trenches, barn/silo slab | 48 |
| Fencing, gates & landscape | Full perimeter fence, zone barriers, spectator berms dressing, planting | 47 |
| Survey, geotech, permits & design fees | Topographic survey, geotechnical investigation, civil/structural design, planning fees | 30 |
| **Site works total** | | **455** |

Check: 118 + 96 + 62 + 54 + 48 + 47 + 30 = **455**.

### 2.3 Track & operating surfaces — $172 K

Assumptions: Track A is the premium surface (fine asphalt, machine-laid, the park's most exacting civil spec — drift and touring parity in Volume 3 depends on it); Tracks B and C are shaped-earth and placed-rock works riding on §2.2 earthworks, so their line items are surfacing and features only.

| Line | Scope | $K |
|---|---|---|
| Track A (asphalt/drift), ~2,200 m² | Fine asphalt wearing course on prepared base, kerbing, run-off zones, paint | 88 |
| Track B (baja/rally) | Packed-dirt surfacing, engineered jumps & berms, geotextile under high-wear corners | 34 |
| Track C (crawler trail) | Placed natural stone, timber bridges, water-hazard liner, anchor points | 28 |
| Pit lane & marshaling surfaces | Concrete pit apron, transmitter-handover counters, marshal walkways | 22 |
| **Track surfaces total** | | **172** |

Check: 88 + 34 + 28 + 22 = **172**.

### 2.4 Buildings — $418 K

Assumptions: areas per the built-form canon (Volume 11 is the geometry authority): entry pavilion **490 m² GFA** (including the 120 m² retail area) at a blended ≈$425/m² pavilion-grade shell-and-fit-out rate → $208 K; The Works **450 m² GFA** (workshop core ~180 m², parts store, QC lane, viewing window, plus the 24 m² battery room and **30 m² charging bunker, both internal** to the building) at a blended ≈$350/m² industrial-shell rate → $158 K. The engineering judgement: Volume 11's areas are larger but simpler than earlier massing studies — bigger clear-span shells at lower unit rates, with the services-dense zones priced separately — so the tendered category total is unchanged. The third line is not a building: it is the specialized fire-rated **fit-out** of the internal bunker and battery room to Volume 7's doctrine (masonry lining, sand-topped charge bays, forced ventilation, thermal monitoring, rated doors).

| Line | Scope | m² | $K |
|---|---|---|---|
| Entry pavilion | Reception/POS, Toolbox Talk briefing room, F&B kiosk, 120 m² retail, toilets, first aid | 490 GFA | 208 |
| The Works (shell & standard fit-out) | Workshop core ~180 m², parts store, QC lane, test bench row, staff room, GM/admin office, viewing window | 450 GFA | 158 |
| Charging bunker & battery-room fit-out | Fire-rated fit-out of the 30 m² bunker + 24 m² battery room *within* The Works, per Volume 7 fire doctrine | (internal) | 52 |
| **Buildings total** | | 940 GFA | **418** |

Check: 490 × $425 = $208.25 K → 208; 450 × $350 = $157.5 K → 158; 208 + 158 + 52 = **418**.

### 2.5 Fleet acquisition — $80 K

Assumptions: quantities are the canonical Phase 1 fleet (~150 powered assets); unit costs are **landed** (wholesale ex-China per the Volume 8 procurement handbook + ~22–28% freight/duty/QC blended in); batteries at the canonical 3:1 ratio (450 packs for 150 assets, blended $23/pack across 2S/3S sizes); opening spares inventory sized to Volume 7's high-turnover spares doctrine at ~90 days' cover. Rental construction machines are electromechanical (lead-screw) per canon; the single hydraulic showcase machine is the Kabolite-class flagship.

| Class | Qty | Unit landed $ | $K | Notes |
|---|---|---|---|---|
| Touring/GT — entry 1/14 (LDRC/MJX class) | 12 | 110 | 1.32 | Motorsport, Vol 3 |
| Touring/GT — standard 1/10 | 12 | 230 | 2.76 | Motorsport |
| Drift (MST-based) | 12 | 340 | 4.08 | Premium chassis class |
| Buggy/rally (WLtoys 144010-class, upgraded) | 12 | 125 | 1.50 | Metal-gear/bearing upfit included |
| Short-course | 8 | 270 | 2.16 | |
| Formula/drag (special events) | 8 | 300 | 2.40 | Event & media fleet, Vol 3 Ch 14 |
| Excavators (Huina 1580 class) | 6 | 520 | 3.12 | Landed incl upfit; 1:3 ratio anchor |
| Dump trucks (Huina 1582/1573 class) | 18 | 230 | 4.14 | 3 per excavator ✓ canon |
| Wheel loaders (Huina 1583) | 3 | 270 | 0.81 | |
| Dozers | 2 | 330 | 0.66 | |
| Premium hydraulic showcase (Kabolite class) | 1 | 11,800 | 11.80 | K970-class flagship; supervised premium sessions only |
| Tractors (Double E E351 / 1/16) | 12 | 135 | 1.62 | Agriculture |
| Implement library (hitches, trailers, discs, plows) | 1 lot | 2,600 | 2.60 | Custom fab share in Vol 7 |
| Crawlers — standard (MN99S/WPL C24 class) | 12 | 80 | 0.96 | |
| Crawlers — premium 1/10 (TRX-4 class) | 4 | 430 | 1.72 | |
| Recovery crawlers (1/10, winch-equipped) | 4 | 390 | 1.56 | Tow-Truck Retrieval Protocol fleet |
| Utility/marshal vehicles | 4 | 360 | 1.44 | Track service |
| Spare rolling hulls (rotation pool) | 18 | — | 2.82 | 10 × $150 + 4 × $250 + 4 × $80 |
| **Batteries** (3:1 canon: 450 packs, 2S/3S, XT60) | 450 | 23 | 10.35 | Consumable thereafter (§5.2) |
| Smart balance chargers (SkyRC T1000/ISDT K4 class) + bunker racks | 1 lot | 4,540 | 4.54 | |
| Standardized transmitters (rental-hardened) | 30 | 45 | 1.35 | Fleet radios beyond bundled units |
| Opening spares inventory (~90 days) | 1 lot | 16,000 | 16.00 | Gears, arms, servos, motors, ESCs, tires — Vol 7/8 lists |
| Commissioning consumables | 1 lot | 290 | 0.29 | Loctite, grease, coating, labels |
| **Fleet acquisition total** | ~150 powered + spares | | **80.00** | |

Check (in $K): 1.32 + 2.76 + 4.08 + 1.50 + 2.16 + 2.40 + 3.12 + 4.14 + 0.81 + 0.66 + 11.80 + 1.62 + 2.60 + 0.96 + 1.72 + 1.56 + 1.44 + 2.82 + 10.35 + 4.54 + 1.35 + 16.00 + 0.29 = **80.00**. Powered-asset count: 12+12+12+12+8+8+6+18+3+2+1+12+12+4+4+4 = 130 fleet vehicles + 4 utility + 18 spare hulls ≈ **~150 powered assets ✓ canon**.

> **Investor Note.** Note the shape of this table: the **single Kabolite-class showcase machine costs more than the other 29 construction machines combined** ($11.8 K vs $8.7 K), and opening spares plus batteries ($26.4 K) cost more than the entire motorsport fleet ($14.2 K). Both are deliberate. The showcase machine is a marketing asset earning premium supervised fees (Volume 4); the spares depth is what keeps 150 assets at rental duty-cycle actually running (Volume 7). A competitor who "saves" on spares buys downtime, not margin.

### 2.6 RCW Node telemetry program — $25 K

Assumptions: every revenue vehicle carries an RCW Node (ESP32-C3 + GPS, PWM-intercept kill-switch, per canon); production unit cost lands under the $15 canonical target; the budget is dominated by firmware/backend engineering and installation labor, not the PCBAs themselves.

| Line | Scope | $K |
|---|---|---|
| Firmware & telemetry-backend engineering | Node firmware, OTA update path, Supabase Realtime ingest, kill-switch logic integration | 9.00 |
| PCBA design, NRE & prototype runs | Unified schematic, two footprints (Micro-Node ~25×25 mm; Heavy-Node ~40×30 mm), 3 prototype spins (JLCPCB class) | 2.70 |
| Production run — 220 units @ $14.50 landed | 130 installs + growth/attrition stock; < $15/unit ✓ canon | 3.19 |
| Harnesses, connectors, conformal coating, mounts | JST-XH sets (Heavy), silicone strain relief (Micro), acrylic coating per canon | 2.31 |
| Installation & commissioning — 190 installs @ $28 labor | Fleet + spare hulls + utility vehicles; bench test + geofence verification each | 5.32 |
| Test jigs, calibration rigs & program spares | Go/no-go jig, voltage-calibration rig, RMA float | 2.48 |
| **RCW Node program total** | | **25.00** |

Check: 9.00 + 2.70 + 3.19 + 2.31 + 5.32 + 2.48 = **25.00**.

### 2.7 Wi-Fi mesh & IT infrastructure — $87 K

Assumptions: outdoor mesh (TP-Link Omada class) blanketing all Phase 1 zones so ESP32 nodes hand off between APs without dropping telemetry (canon); CCTV coverage of all customer areas and the charging bunker; POS/kiosk hardware for the pavilion.

| Line | Scope | $K |
|---|---|---|
| Outdoor Wi-Fi mesh | 14 outdoor APs, poles, fiber backhaul ring, controller | 33 |
| Core network, servers, UPS & CCTV | Rack, switches, on-prem edge server, UPS, 24-camera CCTV incl bunker thermal camera | 32 |
| POS, kiosks, screens & timing | 4 POS stations, 2 self-serve kiosks, leaderboard screens, lap-timing loops | 22 |
| **Wi-Fi & IT total** | | **87** |

Check: 33 + 32 + 22 = **87**.

### 2.8 RC WORLD OS v1 development — $165 K

Assumptions: v1 scope is the opening-day minimum defined in Volume 13 — bookings & wallet, Toolbox Talk induction/waiver, queue roster & top-ups, fleet inventory & maintenance logs, live telemetry map with kill-switch, POS integration, and the web admin console — on the canonical stack (Supabase/PostgreSQL + Kotlin services; Kotlin Multiplatform/Compose Multiplatform apps for Android **and iOS**). Budget: 14 developer-months blended at $9.5 K (mixed senior contract + founder-team rates) = $133 K, plus $32 K for design, security review, device lab, app-store and tooling costs. Post-launch development is an opex line (§5.5), not capex.

| Line | $K |
|---|---|
| Development — 14 dev-months @ $9.5 K blended | 133 |
| UX design, security review, device lab, tooling & launch costs | 32 |
| **RC WORLD OS v1 total** | **165** |

> **Investor Note.** $165 K is modest for an ERP because v1 is scope-disciplined: it ships only what opening day needs and rides on Supabase primitives rather than custom infrastructure (Volume 13, Chapter 3). The strategic payoff is out-of-proportion: RC WORLD OS is the moat competitors cannot buy off the shelf, and it is the franchisable asset priced in Volume 12. Treat this line as protected — it is the last line to cut in any value-engineering exercise.

### 2.9 FF&E, workshop equipment & theming — $118 K

| Line | Scope | $K |
|---|---|---|
| Entry pavilion fit-out & F&B kiosk equipment | Counters, coolers, coffee machine, warmers, retail shelving, briefing-room AV | 46 |
| The Works equipment | Benches, ESD stations, soldering/rework, compressor, parts bins, battery test rigs, hand tools ×4 sets | 38 |
| Shade, furniture & viewing | Shade sails, spectator benches, picnic sets, bag storage | 22 |
| Signage & theming | Wayfinding, zone theming (scale props per Volume 11 world-building spec), safety signage | 12 |
| **FF&E total** | | **118** |

Check: 46 + 38 + 22 + 12 = **118**.

### 2.10 Pre-opening — $162 K

Assumptions: core team hired 8 weeks before opening (GM 16 weeks) for build supervision, SOP training (Volume 7), fleet commissioning, and soft-opening rehearsals; launch marketing per Volume 9's launch plan; licences and insurance from first occupation.

| Line | Scope | $K |
|---|---|---|
| Pre-opening staff & training | Salaries before Day 1 (GM 16 wks; ops/workshop leads 10 wks; 12 staff 8 wks), training materials, soft-opening events | 62 |
| Launch marketing | Brand assets, launch campaign, creator/media program, opening event | 55 |
| Licences, insurance & professional | Public-entertainment licence, LiPo storage compliance, legal, accounting setup, insurance from occupation | 45 |
| **Pre-opening total** | | **162** |

Check: 62 + 55 + 45 = **162**.

### 2.11 Contingency — $168 K (10.0%)

Held as a single unallocated line under GM + founder joint control, releasable only against documented scope events (latent ground conditions, tender overruns, FX movement on the fleet order). Ten percent is appropriate for a design-complete package on a flat serviced site; Chapter 9 stresses the case where it is not enough (capex +20%).

### 2.12 Phase 2 and Phase 3 envelopes; five-year program — ≈$3.9 M

Phase 2/3 budgets are planning envelopes (±15%), refined to line-item level in the Phase 2 investment memo gated at operating Month 12 (§3.5). They carry the division volumes' own build-ups: the aviation line is Volume 5's bottom-up budget (enclosure $190 K + runway/apron civil $85 K + sim lab $45 K + fleet & radios $32 K + timing/AV $12 K = **$364 K**, including the ~20-aircraft fleet), and the marine line carries the pond civil work at ≈$212 K inside its $231 K (Volumes 6 and 11). The aviation uplift versus earlier drafts (+$128 K, plus its fleet moving inside the division line) is funded by value-engineering the restaurant/grandstand/retail/lawn package (−$64 K, per Volume 11's staged fit-out sequence) and by trimming Phase 2 contingency from ~10% to ~6.2% — defensible because the largest Phase 2 line is now a bottom-up engineering budget rather than an envelope.

| Phase 2 line (project Months 13–30) | $K | | Phase 3 line (project Months 31–60) | $K |
|---|---|---|---|---|
| Aviation Division (Volume 5 build-up: enclosure 190, runway/apron civil 85, sim lab 45, fleet & radios 32, timing/AV 12) | 364 | | Indoor all-weather arena (~1,200 m² hall, indoor track, lighting, HVAC) | 452 |
| Marine Division (pond civil ≈212, decks/stations, water treatment, theming) | 231 | | Corporate event centre | 132 |
| Full restaurant (build 208, kitchen 58, furniture 24) | 290 | | RC Academy classrooms | 108 |
| Grandstand viewing | 96 | | Night-racing lighting | 78 |
| Expanded retail | 50 | | Franchise pilot support (systems, documentation, pilot fit-out share) | 48 |
| Events lawn & parking expansion (+44 bays + 4 bus bays, Volume 11) | 34 | | | |
| Marine fleet (~24 vessels ≈ 8) + Phase 2 RCW Nodes, batteries & spares (10) | 18 | | | |
| Subtotal | 1,083 | | Subtotal | 818 |
| Contingency @ ~6.2% | 67 | | Contingency @ ~10% | 82 |
| **Phase 2 total** | **1,150** | | **Phase 3 total** | **900** |

Checks: 364+231+290+96+50+34+18 = 1,083; +67 = **1,150 ✓ canon**. Aviation internal: 190+85+45+32+12 = 364 ✓. Restaurant internal: 208+58+24 = 290 ✓. Phase 3: 452+132+108+78+48 = 818; +82 = **900 ✓ canon**. Five-year program: 1,850 + 1,150 + 900 = **3,900 ≈ $3.9 M ✓ canon**.

---

## 3. Funding Plan

### 3.1 The $2.6 M ask — uses of funds

The ask is Phase 1 capex plus everything needed to reach sustained monthly break-even (Month 16–19) without a further raise, plus an unallocated reserve. The non-capex components below reappear, to the dollar, as the $750 K opening cash position in Chapter 6's monthly model.

| Use | $K | Basis |
|---|---|---|
| Phase 1 capex | 1,850 | Chapter 2 (includes its own 10% construction contingency) |
| Working capital at opening | 130 | F&B/retail opening stock, consumables float, deposits, till/wallet float |
| Operating funding through break-even | 350 | Covers the cumulative Year 1–2 EBITDA trough of −$118 K (Month 15, §6.2) plus sustaining capex ($3 K/month Y1, $6 K/month Y2) with margin for a slow ramp |
| Corporate, legal & transaction costs | 90 | Entity setup, raise legals, audit/tax setup, founder-office overhead pre-opening |
| Unallocated reserve | 180 | Board-controlled; released only against Chapter 9 downside triggers |
| **Total funding ask** | **2,600** | **✓ canon** |

Check: 1,850 + 130 + 350 + 90 + 180 = **2,600**. Non-capex funds at opening: 130 + 350 + 90 + 180 = **750** (= opening cash, §6.2).

### 3.2 Tranche structure with milestone gates

Capital is drawn in three tranches so investors never fund the next stage of risk before the previous one has been retired. Gates are objective and verifiable in a site visit plus an RC WORLD OS data pull.

| Tranche | $K | Timing | Milestone gate (all must be true) | Risk retired |
|---|---|---|---|---|
| T1 | 1,200 | At close (≈ operating Month −12, i.e. project Month 0) | Lease executed; planning permits granted; civil tender within budget; GM contracted | Site & permitting risk |
| T2 | 850 | ≈ operating Month −5 | Buildings weathertight; Tracks A/B/C substantially complete; ≥80% of fleet landed and commissioned; RC WORLD OS beta operating end-to-end (booking → telemetry → kill-switch demo); opening date fixed | Construction & technology risk |
| T3 | 550 | At opening (operating Month 1) | Soft opening complete; safety sign-off (Volume 7 audit); first 1,000 paid Shifts sold; insurance in force | Launch risk |
| **Total** | **2,600** | | | |

Check: 1,200 + 850 + 550 = **2,600**. If a gate fails, the tranche pauses and the pre-agreed remediation ladder applies (descope per §2.11 hierarchy, re-tender, or — worst case — orderly wind-down with land improvements as residual value).

### 3.3 Instrument options

The model is instrument-agnostic; three structures bracket the negotiation space. All returns math in §7.5 uses Structure A for clarity.

| Structure | Composition | Investor economics | Founder economics | When it fits |
|---|---|---|---|---|
| A — Straight equity | $2.6 M common/preferred | 65% fully diluted (see §3.4); pro-rata dividends from Year 4 | 30% + control provisions | Single lead investor or small syndicate wanting clean alignment |
| B — Convertible + equity | $1.6 M equity + $1.0 M convertible note (8% PIK, converts at Phase 2 gate at 15% discount) | Downside seniority on ~40% of capital; equity upside on conversion | Less immediate dilution; conversion priced on Year-1 actuals | Investors wanting Year-1 proof before pricing the whole position |
| C — Equity + asset debt | $2.0 M equity + $0.6 M equipment/fit-out facility (9%, 4-yr amortizing, secured on buildings/FF&E) | Smaller equity cheque for same park | More dilution-efficient; adds fixed service cost from Year 1 | Markets with accessible venue-finance; note Chapter 6 already models a separate $0.6 M Phase 2 facility — Structure C would replace, not stack with, it |

> **Investor Note.** The plan deliberately does **not** assume venture-style follow-on rounds. The $2.6 M is sized to reach self-funding: Phase 2 ($1.15 M) is financed from operating cash flow plus an optional $0.6 M facility (§3.5), and Phase 3 ($0.9 M) from cash flow alone. An investor's exposure is therefore capped at the ask in every scenario except the deep-downside cases of Chapter 9, where the pre-agreed responses are descoping and the cost-flex ladder (§6.5) — not a rescue round priced against the existing holders.

### 3.4 Illustrative cap table (Structure A)

Pre-money value of $1.4 M reflects contributed IP: the complete Master Development Plan, RC WORLD OS architecture and codebase progress, RCW Node designs, and the supplier network of Volume 8 — assets a competitor would need ~$300–500 K and 18 months to replicate, valued here with a market-entry premium.

| Holder | Basis | Post-money % |
|---|---|---|
| Investor(s) | $2.6 M new money into $4.0 M post ($1.4 M pre) | 65.0% |
| Founder | Contributed IP, plan, and execution role | 30.0% |
| Employee option pool | Reserved at close (GM and early key hires) | 5.0% |
| **Total** | | **100.0%** |

### 3.5 Funding Phases 2 and 3

Phase 2 ($1,150 K — project Months 13–30 in the phasing canon; in this model's cash flow the spend lands in **operating** Months 13–30, §6.1) is funded by: retained operating cash flow (cumulative EBITDA turns positive during Year 2 — $154 K generated in Year 2, §7.1) plus an optional **$600 K equipment-and-fit-out facility** (modelled at 9% p.a., drawn in four $150 K tranches Months 15–21, amortizing over Years 4–5 — the exact draws, interest, and repayments appear in Chapter 6 and §7.1). The Phase 2 commitment itself is **gated on Year-1 actuals**: revenue ≥ 80% of plan and 90-day second-visit rate ≥ 20% — the gate **floor**, deliberately set below the KPI's operating targets of ≥22% Year 1 / ≥28% Year 3 (the KPI's home is §10.4). Below gate, Phase 2 compresses to a "Marine-first" descope (~$620 K) or delays 6–12 months — the conservative scenario of Chapter 10. Phase 3 ($900 K, spent operating Months 37–60) is funded entirely from operating cash flow and is optionality, not obligation: each Phase 3 element must clear a standalone hurdle (≥25% ROIC on incremental EBITDA) at the operating Month-30 review (§10.2).

---

## 4. Revenue Model

### 4.1 Architecture of the engine

Revenue is built bottom-up in four stages — (1) visitor volume by day-type and season, (2) capacity and utilization from canonical fleet counts, (3) yield from the canonical price card, (4) attach and program revenue — and then reconciled three ways: monthly to Year 1's $1,280 K, annually to the five-year canon, and externally against the demand side: Volume 2's Chapter 9 works from catchment and per-visit spend to a Year-1 estimate of **~37,000–43,000 visits at a blended $30–35 per visitor-visit**, and this engine's 38,920 paid visits (≈42,000 gate visits) at $30.0 blended sit inside that band — the agreement you want from two models built from opposite ends.

### 4.2 Visitor volume by day-type and season

Assumptions: 360 operating days; Year 1 opens March (operating M1); day-types calibrated to ~110 visitors/operating-day average — the midpoint of Volume 2's ~37–43 K-visit Year-1 estimate (Chapter 9, §9.4) — with peak days 220–300 and midweek 40–60.

| Day-type | Days/yr | Avg paid visitors/day | Paid visits |
|---|---|---|---|
| Peak (weekends, public/school holidays) | 118 | 195 | 23,010 |
| Midweek standard | 190 | 55 | 10,450 |
| Shoulder & event days (league nights, twilight events, corporate blocks) | 52 | 105 | 5,460 |
| **Total individual paid visits** | **360** | **108 avg** | **38,920** |

Check: 118×195 = 23,010; 190×55 = 10,450; 52×105 = 5,460; sum = **38,920** (÷360 = 108/day; inside Volume 2's ~37–43 K band ✓). Member visits, party guests, and corporate attendees add ≈3,100 gate visits → **≈42,000 total visits**. Blended on-site spend = (1,280 − 6 sponsorship − 14 education) ÷ 42.0 = **$30.0/visitor-visit**, at the conservative bottom edge of Volume 2's $30–35 band (Chapter 9).

### 4.3 Capacity and utilization from fleet counts

Assumptions: capacity is **concurrent operating stations**, not fleet size (cars queue for customers, not customers for cars — Volume 3, Chapter 2 doctrine); 2 Shift-slots per station-hour (20-min Shift + turnaround inside a 25–30 min cycle); 8 average revenue hours across 360 days.

| Division | Concurrent stations | Basis (fleet canon) |
|---|---|---|
| Motorsport (Tracks A/B) | 22 | 64 cars; track slots bind: 8 touring + 6 drift (Track A), 8 off-road (Track B) — Volume 3 |
| Construction — Mining | 12 | 30 machines; 3–4 excavator stations (of 6) + circulating dump trucks + loaders — 1:3 ratio |
| Agriculture | 8 | 12 tractors, implement-limited |
| Crawler park (Track C) | 13 | 16 crawlers, trail-section-limited |
| Premium supervised (Kabolite showcase + premium crawler line) | 2 | Artisan-supervised |
| **Phase 1 total** | **57** | |

Annual slot capacity = 57 stations × 8 h × 2 slots/h × 360 d = **328,320 Shift-slots**. Year 1 consumes 57,720 blocks (§4.4) → **17.6% slot utilization** — deliberately low, leaving ~5× headroom so growth to Year 3–5 requires marketing and retention, not capex (the Volume 4 "option value" argument, park-wide).

### 4.4 Shift & session revenue — Year 1 build

Assumptions: canonical price card (Casual $15/$22; Operator $26/$38; Day Pass $59; Family bundle $89); premium share of casual volume ~14% (hydraulics, FPV-prep, big crawlers); operator-conversion ~25% of session buyers; blocks per product as shown. Volumes follow from §4.2 visits × observed products-per-visit (~0.9 sessions/visit for individual visitors, the rest arriving inside passes/bundles/groups).

| Product | Unit price $ | Units sold | Revenue $K | Blocks consumed |
|---|---|---|---|---|
| Casual Shift — standard | 15 | 21,400 | 321.0 | 21,400 |
| Casual Shift — premium | 22 | 3,500 | 77.0 | 3,500 |
| Operator Shift — standard (2 blocks + pit stop) | 26 | 7,200 | 187.2 | 14,400 |
| Operator Shift — premium | 38 | 1,250 | 47.5 | 2,500 |
| Day Pass (avg 4 blocks used) | 59 | 1,440 | 85.0 | 5,760 |
| Family bundle (4 drivers × 2 shifts) | 89 | 770 | 68.5 | 6,160 |
| Member/party/corporate included blocks | in other lines | — | — | 4,000 |
| **Shift & session revenue / blocks** | | | **786.2** | **57,720** |

Checks: 321.0 + 77.0 + 187.2 + 47.5 + 85.0 + 68.5 = **786.2** ($84,960 and $68,530 shown rounded to 85.0/68.5). Blocks: 21,400 + 3,500 + 14,400 + 2,500 + 5,760 + 6,160 + 4,000 = **57,720** ✓ §4.3. Average yield = 786.2 ÷ 53.72 K revenue-bearing blocks = **$14.6/block** ($13.6/block across all blocks including bundled).

### 4.5 Membership MRR build

Assumptions: canonical tiers (Apprentice $29, Operator $59, Foreman $99); sales start Month 2; net adds accelerate with the license ladder and league seasons (Volume 9); churn 3.5%/month netted within the adds shown.

| Milestone | Apprentice | Operator | Foreman | Members | MRR $K |
|---|---|---|---|---|---|
| End Month 3 | 45 | 10 | 2 | 57 | 2.1 |
| End Month 6 | 105 | 30 | 7 | 142 | 5.5 |
| End Month 9 | 160 | 52 | 13 | 225 | 9.0 |
| End Month 12 | 240 | 82 | 22 | 344 | 14.0 |

Check (Month 12): 240×29 + 82×59 + 22×99 = 6,960 + 4,838 + 2,178 = $13,976 ≈ **$14.0 K MRR**. Year 1 recognized membership revenue (monthly curve in §4.8) = **$70 K**; exit run-rate $167 K/yr, which is why Year 2 membership revenue steps to $160 K. Year 3 assumes ~620 average members (mix 420/150/50 → $25.98 K MRR) → **≈$300 K** ✓ §4.9.

### 4.6 Corporate, parties, education

Assumptions: canonical anchors (corporate from $1,400 for 2 h/20 pax; parties from $349 for 10 children); group-demand pools sized from the catchment segmentation in Volume 2, Chapter 9 (employers of 20+ staff, children turning 7–13, addressable schools in a 1.5 M metro); averages exceed anchors because packages upsell (catering, extra Shifts, premium classes).

| Program | Year 1 volume | Avg ticket $ | Revenue $K | Catchment-pool sanity band |
|---|---|---|---|---|
| Corporate events | 45 events | 1,600 | 72 | $70–140 K ✓ |
| Birthday parties & groups | 190 parties | 420 | 80 | $80–150 K ✓ |
| Education/schools | 35 visits | 400 | 14 | $8–25 K ✓ |
| **Program revenue** | | | **166** | |

### 4.7 F&B, retail, repairs, sponsorship

Assumptions: F&B kiosk-only in Phase 1 at **$3.76/gate visit** (42.0 K visits — 52% purchase incidence × $7.20 average ticket); retail counter at $2.00/visit; paid repair/upgrade services for customer-owned vehicles priced per Volume 7's service menu; sponsorship is deliberately token in Year 1 (two local partners) and grows with audience (Volume 9 sponsorship strategy).

| Line | Driver arithmetic | Revenue $K |
|---|---|---|
| F&B | 42.0 K visits × $3.76 | 158 |
| Retail | 42.0 K visits × $2.00 | 84 |
| Repairs & services | ≈ 490 jobs × $20 avg | 9.8 |
| Sponsorship | 2 local partners | 6.0 |
| **Attach & other revenue** | | **257.8** |

### 4.8 Year 1 monthly ramp — reconciles to $1,280 K

Assumptions: March opening; ramp Months 1–4; July–August peak; September–November shoulder; December spike from holiday demand plus corporate party season; January–February soft but cushioned by memberships, leagues, and the maturing corporate pipeline. All figures $K.

| Month | Shifts & sessions | Memberships | Corporate/parties/education | F&B + retail | Repairs + sponsorship | **Total** |
|---|---|---|---|---|---|---|
| M1 (Mar) | 59.6 | 0.0 | 8.0 | 15.9 | 0.5 | **84** |
| M2 (Apr) | 66.1 | 1.0 | 10.0 | 18.1 | 0.8 | **96** |
| M3 (May) | 70.3 | 2.0 | 11.0 | 19.7 | 1.0 | **104** |
| M4 (Jun) | 74.6 | 3.0 | 12.0 | 21.2 | 1.2 | **112** |
| M5 (Jul) | 83.8 | 4.0 | 13.0 | 23.8 | 1.4 | **126** |
| M6 (Aug) | 79.5 | 5.0 | 13.0 | 23.1 | 1.4 | **122** |
| M7 (Sep) | 59.6 | 6.0 | 14.0 | 18.9 | 1.5 | **100** |
| M8 (Oct) | 54.9 | 6.5 | 15.0 | 18.1 | 1.5 | **96** |
| M9 (Nov) | 49.6 | 7.5 | 16.0 | 17.4 | 1.5 | **92** |
| M10 (Dec) | 73.8 | 9.5 | 22.0 | 25.0 | 1.7 | **132** |
| M11 (Jan) | 56.2 | 11.5 | 15.0 | 19.7 | 1.6 | **104** |
| M12 (Feb) | 58.2 | 14.0 | 17.0 | 21.1 | 1.7 | **112** |
| **Year 1** | **786.2** | **70.0** | **166.0** | **242.0** | **15.8** | **1,280** |

Checks: column sums — 786.2 ✓ §4.4; 70.0 ✓ §4.5; 166.0 ✓ §4.6; 242.0 = 158 F&B + 84 retail ✓ §4.7; 15.8 = 9.8 + 6.0 ✓. Every row sums across (e.g. M10: 73.8 + 9.5 + 22.0 + 25.0 + 1.7 = 132.0). Grand total = **$1,280 K ≈ $1.28 M ✓ canon**.

### 4.9 Five-year revenue — reconciles to canon

Assumptions by year (all months **operating** frame): **Y2** — frequency growth (leagues, licenses), membership base ×2.3, aviation opens in stages across operating Months 16–24 (sim lab M16, fixed-wing M19–20, full program M23–24) and marine across operating Months 20–24, per the canonical opening schedule; **Y3** — first full year of the complete Phase 2 park (Aviation + Marine + restaurant: F&B steps up, per-cap rises); **Y4–Y5** — Phase 3 elements (indoor arena from operating Month ~44 removes weather ceiling; Academy scales education; night racing lifts peak yield). All figures $K.

| Revenue line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Shifts & sessions | 786 | 1,120 | 1,390 | 1,585 | 1,730 |
| Memberships | 70 | 160 | 300 | 370 | 430 |
| Corporate events | 72 | 115 | 170 | 205 | 240 |
| Parties & groups | 80 | 112 | 150 | 170 | 190 |
| Education & Academy | 14 | 32 | 60 | 80 | 100 |
| F&B | 158 | 220 | 310 | 360 | 410 |
| Retail | 84 | 112 | 150 | 170 | 190 |
| Repairs & services | 10 | 18 | 30 | 38 | 45 |
| Sponsorship & media | 6 | 16 | 40 | 52 | 65 |
| **Total revenue** | **1,280** | **1,905** | **2,600** | **3,030** | **3,400** |

Column checks: Y1 786+70+72+80+14+158+84+10+6 = **1,280** ✓; Y2 1,120+160+115+112+32+220+112+18+16 = **1,905**; Y3 1,390+300+170+150+60+310+150+30+40 = **2,600 ✓ canon**; Y4 1,585+370+205+170+80+360+170+38+52 = **3,030**; Y5 1,730+430+240+190+100+410+190+45+65 = **3,400 ✓ canon**. Growth sanity: Y2 exit run-rate (Months 23–24 at $186–204 K/month, §6.2) annualizes to ≈$2.3–2.4 M, making Y3's $2.6 M a ~10% step on Phase 2 completion — frequency and new divisions, not a larger catchment (consistent with the frequency assumptions in Volume 2, §9.5).

Division attribution (Year 1, Shift + program revenue of $952 K): Motorsport ≈ $470 K, Construction & Agriculture ≈ $430 K, Crawler park & recovery ≈ $52 K — honouring both Volume 3's "highest single revenue engine" and Volume 4's "≈$410–470 K, roughly a third of park revenue" (430 ÷ 1,280 = 34%). Day-pass and bundle value is attributed by observed block consumption in RC WORLD OS.

> **Investor Note.** Three properties make this revenue model conservative rather than optimistic. First, **utilization is 17.6% of slot capacity in Year 1** and only ~24% by Year 3 — the park never needs to be busy in absolute terms to hit canon. Second, **recurring revenue compounds quietly**: memberships grow from 5% to 13% of revenue across five years, and every point of that mix shift stabilizes the winter months that drive break-even timing. Third, the model **excludes franchise income entirely** (royalties, fees, and the Volume 12 program are upside outside canon, pointed to in §10.3).

---

## 5. Operating Cost Model

### 5.1 Staffing plan & payroll

Assumptions: salaries are full-year costs in $K for a mid-size international city (adjust locally with the Volume 12 localization index); **on-costs 15%** (employer taxes, workers' compensation, basic benefits) applied to base; casual/seasonal flex staff cover peak days and are shown as a separate line; headcounts step with phases. Artisans are the customer-facing technician corps (canon).

**Year 1 establishment (18.5 FTE):**

| Role | FTE | Base $K each | Base $K total |
|---|---|---|---|
| General Manager | 1 | 70 | 70 |
| Operations Manager | 1 | 52 | 52 |
| Workshop Lead (Head Artisan) | 1 | 48 | 48 |
| Artisans (technicians) | 4 | 36 | 144 |
| Track Marshals | 5 | 26 | 130 |
| Front-of-house / bookings | 3.5 | 24 | 84 |
| F&B kiosk staff | 2 | 24 | 48 |
| Marketing & community | 1 | 38 | 38 |
| Admin / bookkeeper | 1 | 30 | 30 |
| **Base payroll** | **18.5** | | **644** |
| On-costs @ 15% | | | 97 |
| Casual peak flex + recruitment & training | | | 26 |
| **Year 1 people cost** | | | **767** |

Check: 70+52+48+144+130+84+48+38+30 = 644; 644 × 1.15 = 740.6 ≈ 741; 741 + 26 = **767**.

**Year 3 establishment (≈24.5 FTE + restaurant team):** GM 74; Ops Manager 56; Workshop Lead 52; Artisans 6 × 37 = 222; Marshals 6 × 26 = 156; Front-of-house 4 × 24 = 96; restaurant/F&B team 125; Marketing 48; Admin/finance 38 → base 867; × 1.15 = 997; + casual flex 43 = **1,040**. Headcount growth over five years tracks divisions, not overhead: the Year 5 additions are marshals for Aviation/Marine, restaurant staff, and two Artisans — management stays at three salaried leaders plus the GM.

| People cost ($K) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Total people | 767 | 940 | 1,040 | 1,217 | 1,351 |
| As % of revenue | 59.9% | 49.3% | 40.0% | 40.2% | 39.7% |

The people ratio falling from 60% to 40% is the core of the margin story (§7.2): a safety-credible venue must be fully staffed on Day 1, so revenue growth outruns headcount growth.

### 5.2 Fleet maintenance, parts & batteries

Assumptions: Year 1 fleet duty = 57,720 blocks × 20 min = 19,240 vehicle-hours + ~760 staff/test/practice hours ≈ **20,000 vehicle-hours**. Parts cost per vehicle-hour is derived from the failure-rate table below (component MTBF from the Volume 7 failure library and Source-2 failure-point lists), then cross-checked top-down. Batteries are consumables costed on the merged cycle-life model shared with Volume 7: one pack-cycle per block; retirement at **200–250 logged cycles or on breaching the internal-resistance threshold**, whichever comes first; ≈**40–50% of the pool replaced per year**.

| Component class (examples) | MTBF (veh-h) | Landed cost/event $ | Cost per veh-h $ |
|---|---|---|---|
| Tires & wheels (knobby, drift slicks) | 60 | 14 | 0.23 |
| Suspension & steering (arms, knuckles, shock shafts, links) | 45 | 11 | 0.24 |
| Drivetrain (pinions, spurs, CVDs, diffs, bearings) | 55 | 16 | 0.29 |
| Servos (15/25 kg digital) | 220 | 24 | 0.11 |
| Motors & ESCs (540/550, brushless ESC events) | 400 | 52 | 0.13 |
| Bodies, mounts & cosmetic | 90 | 12 | 0.13 |
| Construction-specific (track pins, lead-screws, micro-switches) | 150 | 20 | 0.13 |
| Fasteners, lubricants, coating, misc consumables | — | — | 0.84 |
| **Blended parts cost per vehicle-hour** | | | **2.10** |

Check: 0.23+0.24+0.29+0.11+0.13+0.13+0.13+0.84 = **2.10** (motorsport runs ≈$2.60/h, construction ≈$1.30/h, crawlers ≈$1.10/h; the blend reflects the block mix). Battery math (merged model, per Volume 7): Year 1 throughput of 57,720 pack-cycles spreads across the ~450-pack pool as **≈128 cycles per pack per year** (57,720 ÷ 450); with retirement at 200–250 cycles or the internal-resistance threshold, ≈40–50% of the pool retires each year — 180–225 packs × $23 = **$4.1–5.2 K** (budgeted $6 K including crash-damaged packs). The ~2-year average pack life this implies matches the 2–3-year fleet depreciation policy (§7.3).

| Fleet cost line ($K) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Parts (veh-h × $/veh-h) | 42 | 64 | 78 | 92 | 104 |
| Batteries (cycle-life consumption) | 6 | 9 | 11 | 13 | 15 |
| Tires/consumables uplift & event wear | 10 | 15 | 18 | 22 | 25 |
| Tools, warranty freight, external services | 8 | 10 | 11 | 13 | 14 |
| **Fleet maintenance total** | **66** | **98** | **118** | **140** | **158** |

Check Y1: 42+6+10+8 = **66**. Maintenance cost per vehicle-hour (total basis) = 66,000 ÷ 20,000 = **$3.30/veh-h** — a headline KPI (§10.4). Fleet *renewal* (replacing worn-out vehicles) is sustaining **capex**, not opex: $36 K (Y1), $72 K, $150 K, $170 K, $190 K — rising with Phase 2/3 fleet size and utilization.

### 5.3 Occupancy & utilities

Assumptions: land lease at **$2.20/m²/yr × 48,000 m² = $105.6 K/yr** (peri-urban serviced-land band $1.50–3.50/m²/yr; verify locally — Chapter 9 stresses this). Utilities note the counterintuitive fact: fleet charging energy is trivial — 57,720 charge cycles × ~0.055 kWh ≈ 3.2 MWh ≈ **$640/year**; utility spend is actually F&B refrigeration, workshop power, lighting, offices, water/irrigation.

| Occupancy line ($K) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Land lease | 106 | 110 | 114 | 118 | 122 |
| Utilities (power, water, comms, gas) | 52 | 68 | 80 | 88 | 94 |
| Waste, security, site services | 32 | 40 | 38 | 40 | 42 |
| **Occupancy total** | **190** | **218** | **232** | **246** | **258** |

Check Y1: 106+52+32 = **190** (lease shown with modest contractual escalation).

### 5.4 Cost of goods sold (F&B, retail, events direct)

Assumptions: F&B COGS at the ~30% food-cost norm (32% Y1 kiosk, 34% from Y3 with the restaurant's broader menu); retail COGS 52% (hobby-retail keystone-minus); repairs parts at 50% of service revenue; direct event costs (catering, consumables, party hosts' variable hours) at ~15% of program revenue in Year 1, peaking ~20% in Year 2 (Phase 2 launch events and a heavier catered corporate mix), then declining with scale and in-house restaurant catering (12% → 10% → 7%).

| COGS line ($K) | Y1 arithmetic | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|---|
| F&B COGS | 158 × 32% | 50.6 | 70 | 105.4 | 122.4 | 139.4 |
| Retail COGS | 84 × 52% | 43.7 | 58 | 78.0 | 88.4 | 98.8 |
| Repairs parts | 9.8 × 50% | 4.9 | 9 | 15.0 | 19.0 | 22.5 |
| Events direct | 166 × 15% | 24.8 | 51 | 45.6 | 44.2 | 39.3 |
| **COGS total** | | **124** | **188** | **244** | **274** | **300** |

Check Y1: 50.6+43.7+4.9+24.8 = 124.0 ✓. Check Y3: 310×34% + 150×52% + 30×50% + (170+150+60)×12% = 105.4 + 78.0 + 15.0 + 45.6 = **244** ✓.

### 5.5 Marketing, insurance, software, admin

Assumptions: marketing at 8% of revenue Year 1 (launch-heavy) declining to ~5% at maturity — never below 4.5%, because Chapter 9 shows visitor volume is the model's biggest lever; insurance covers public liability (the dominant premium for a participation venue), property, and specialty lines (drone/aviation endorsement from Phase 2, open-water endorsement per Volume 6); software/hosting includes payment processing at 2.2% of the ~85% card share, RC WORLD OS hosting, and continuing development (post-v1 development is expensed here, not capitalized).

| Line ($K) | Y1 arithmetic | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|---|
| Marketing | 8.0% of revenue | 102 | 133 | 140 | 155 | 168 |
| Insurance | liability 26 + property 12 + specialty 10 | 48 | 56 | 60 | 64 | 68 |
| Software, hosting & payments | processing 24 + hosting/SaaS 19 + continuing dev 14 | 57 | 78 | 96 | 108 | 119 |
| Admin & misc (accounting, legal, bank, office) | | 26 | 40 | 40 | 44 | 48 |

Check Y1 payments line: 1,280 × 85% × 2.2% = 23.9 ≈ 24; 24+19+14 = **57** ✓.

### 5.6 Consolidated operating cost stack

| Opex category ($K) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| People (§5.1) | 767 | 940 | 1,040 | 1,217 | 1,351 |
| Occupancy & utilities (§5.3) | 190 | 218 | 232 | 246 | 258 |
| Fleet maintenance & batteries (§5.2) | 66 | 98 | 118 | 140 | 158 |
| COGS (§5.4) | 124 | 188 | 244 | 274 | 300 |
| Marketing (§5.5) | 102 | 133 | 140 | 155 | 168 |
| Insurance (§5.5) | 48 | 56 | 60 | 64 | 68 |
| Software, hosting & payments (§5.5) | 57 | 78 | 96 | 108 | 119 |
| Admin & misc (§5.5) | 26 | 40 | 40 | 44 | 48 |
| **Total operating costs** | **1,380** | **1,751** | **1,970** | **2,248** | **2,470** |
| **EBITDA (revenue §4.9 − opex)** | **−100** | **154** | **630** | **782** | **930** |
| **EBITDA margin** | −7.8% | 8.1% | **24.2%** | **25.8%** | **27.4%** |

Column checks: Y1 767+190+66+124+102+48+57+26 = **1,380**; Y3 1,040+232+118+244+140+60+96+40 = **1,970**; Y5 1,351+258+158+300+168+68+119+48 = **2,470**. EBITDA: 1,280−1,380 = −100; 2,600−1,970 = 630 (24.2%); 3,400−2,470 = 930 (27.4%) — **EBITDA margin 24–28% from Year 3 ✓ canon**.

> **Investor Note.** The Year 1 EBITDA of −$100 K is a **feature of honest modelling, not a flaw of the business**: the park opens fully staffed and fully insured against a revenue base that takes 12–16 months to build its membership and corporate layers. The funding plan carries this loss explicitly (§3.1's $350 K operating-funding line). Beware any comparable plan showing positive EBITDA in the opening year of a staffed venue — it is usually understaffing safety roles or amortizing pre-opening costs into later years.

---

## 6. Cash Flow & Break-Even

### 6.1 Conventions of the monthly model

All months in this chapter are **operating** months (M1 = opening; §1.2 convention). Opening cash = $750 K (the $2.6 M ask less $1,850 K Phase 1 capex, per §3.1 — all Phase 1 capex assumed spent by opening day). Sustaining fleet-renewal capex $3 K/month in Year 1 and $6 K/month in Year 2. Phase 2 capex spends $55 K/month in operating Months 13–18 and $75 K/month in operating Months 19–24 ($780 K in Year 2; the remaining $370 K falls in operating Months 25–30). The optional Phase 2 facility (§3.5) draws four $150 K tranches in Months 15, 17, 19, 21; interest at 0.75%/month (9% p.a.) on the drawn balance, paid monthly in arrears. Working-capital movements are treated as neutral (membership prepayments and gift-wallet float offset inventory growth; stated as a simplification). Tax: no cash tax in Years 1–2 (losses; §7.1).

### 6.2 Monthly cash flow, Years 1–2 ($K)

| Mo | Revenue | Cash opex | EBITDA | Sust. capex | Ph 2 capex | Facility draw | Interest | Net cash | Closing cash |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 84 | 110 | −26 | −3 | — | — | — | −29 | 721 |
| 2 | 96 | 111 | −15 | −3 | — | — | — | −18 | 703 |
| 3 | 104 | 112 | −8 | −3 | — | — | — | −11 | 692 |
| 4 | 112 | 114 | −2 | −3 | — | — | — | −5 | 687 |
| 5 | 126 | 117 | 9 | −3 | — | — | — | 6 | 693 |
| 6 | 122 | 117 | 5 | −3 | — | — | — | 2 | 695 |
| 7 | 100 | 114 | −14 | −3 | — | — | — | −17 | 678 |
| 8 | 96 | 114 | −18 | −3 | — | — | — | −21 | 657 |
| 9 | 92 | 115 | −23 | −3 | — | — | — | −26 | 631 |
| 10 | 132 | 119 | 13 | −3 | — | — | — | 10 | 641 |
| 11 | 104 | 118 | −14 | −3 | — | — | — | −17 | 624 |
| 12 | 112 | 119 | −7 | −3 | — | — | — | −10 | 614 |
| **Y1** | **1,280** | **1,380** | **−100** | **−36** | — | — | — | **−136** | **614** |
| 13 | 118 | 128 | −10 | −6 | −55 | — | — | −71 | 543 |
| 14 | 124 | 130 | −6 | −6 | −55 | — | — | −67 | **476 (min)** |
| 15 | 134 | 136 | −2 | −6 | −55 | 150 | — | 87 | 563 |
| 16 | 156 | 144 | **12** | −6 | −55 | — | −1.1 | −50.1 | 512.9 |
| 17 | 166 | 147 | 19 | −6 | −55 | 150 | −1.1 | 106.9 | 619.8 |
| 18 | 176 | 150 | 26 | −6 | −55 | — | −2.2 | −37.2 | 582.6 |
| 19 | 160 | 151 | 9 | −6 | −75 | 150 | −2.2 | 75.8 | 658.4 |
| 20 | 152 | 150 | 2 | −6 | −75 | — | −3.4 | −82.4 | 576.0 |
| 21 | 154 | 151 | 3 | −6 | −75 | 150 | −3.4 | 68.6 | 644.6 |
| 22 | 175 | 153 | 22 | −6 | −75 | — | −4.5 | −63.5 | 581.1 |
| 23 | 186 | 154 | 32 | −6 | −75 | — | −4.5 | −53.5 | 527.6 |
| 24 | 204 | 157 | 47 | −6 | −75 | — | −4.5 | −38.5 | 489.1 |
| **Y2** | **1,905** | **1,751** | **154** | **−72** | **−780** | **600** | **−26.9** | **−124.9** | **489** |

Checks: Year 1 revenue column sums to 1,280 ✓ §4.8; opex to 1,380 ✓ §5.6; EBITDA to −100 ✓. Year 2: revenue 1,905 ✓, opex 1,751 ✓, EBITDA 154 ✓; facility draws 4 × 150 = 600 ✓; interest 1.1+1.1+2.2+2.2+3.4+3.4+4.5+4.5+4.5 = 26.9 ✓ (0.75% on the stepped balance). Every closing-cash cell = prior cell + net cash. The Year-2 revenue ramp carries the staged Phase 2 openings (all operating months): aviation sim lab from Month 16, fixed-wing Months 19–20, marine from Months 20–24, and the aviation full program in Months 23–24 adding ≈$25–35 K/month — the bridge to Year 3's full-park revenue.

### 6.3 Break-even — shown and explained

Monthly operating break-even = the month from which monthly EBITDA is positive **and stays positive**. Two arithmetic facts drive its timing. First, the steady Year-2 cost stack is ≈$118–125 K/month of effectively fixed cost (people, lease, insurance, software, base marketing) plus ≈17–19% of revenue in variable cost (COGS, fleet wear, payment fees, casual labor) — so break-even revenue ≈ 122 ÷ 0.82 ≈ **$149 K/month**. Second, the revenue ramp (membership MRR compounding, corporate pipeline maturing, league base load) crosses that line at **Month 16** ($156 K revenue vs $144 K opex = +$12 K) and never goes negative again in the base model (the shallowest subsequent month is Month 20 at +$2 K, the post-summer shoulder). The canonical band **Month 16–19** exists because the crossing month is sensitive to opening-date seasonality and ramp speed: an autumn opening, or a ramp 10% slower, slides the crossing to Months 18–19 without changing annual totals materially. (First *isolated* positive months occur earlier — Months 5–6 in the summer peak — but the plan does not call that break-even; sustained coverage of the winter trough is the test.)

### 6.4 Cumulative cash curve and minimum-buffer policy

The cash curve has three regimes visible in §6.2: a **shallow Year-1 glide** from $750 K to $614 K (the −$136 K Year-1 burn: −$100 K EBITDA − $36 K sustaining capex); a **Phase-2 construction trough** in early Year 2, bottoming at **$476 K in Month 14**, with the facility draws deliberately timed after the trough so equity cash never falls further; and a **self-funding climb** from Month 22 as monthly EBITDA outruns Phase 2 spend. Policy: **minimum cash ≥ $250 K at all times** — approximately three months of the survival-floor cost stack (§6.5) — with a board-notification trigger at $350 K. The base model's worst point ($476 K) holds a $226 K cushion above the floor; Chapter 9's downside scenarios are tested against exactly this policy.

### 6.5 The cost-flex ladder (downside machinery)

If revenue underperforms, costs flex in pre-agreed stages rather than ad-hoc cuts. The survival floor (≈$0.9 M/year) is the minimum annualized cost stack that keeps the park open safely, ~$74 K/month; it is the reference line for the downside cases in Volume 2's demand analysis (Chapter 9) and the master risk register (Volume 1, Chapter 8).

| Stage (trigger) | Actions | Annualized stack $K |
|---|---|---|
| Plan (base) | Full Year-1 establishment | 1,380 |
| Flex 1 (revenue <85% of plan for 8 rolling weeks) | Freeze hiring; casual hours −30%; marketing remixed not cut; defer non-safety maintenance projects | ≈ 1,250 |
| Flex 2 (<75% for 8 weeks) | Midweek hours compressed; F&B menu simplified; sustaining capex paused; one FOH and one F&B role held vacant | ≈ 1,100 |
| Survival floor (<60%, board decision) | Skeleton crew 8 FTE (~420), lease 106 + minimum utilities/site 69, insurance 45, software 40, fleet safety-minimum 45, marketing 55, COGS at reduced volume ~90, admin 20 | **≈ 890 (the "$0.9 M line")** |

Check (floor): 420+106+69+45+40+45+55+90+20 = **890**. Even the survival floor keeps every safety-critical function (marshals within the 8 FTE, insurance, battery-room compliance) fully funded.

---

## 7. Profitability & ROI

### 7.1 Five-year P&L

Assumptions: revenue §4.9; opex §5.6; D&A per the §7.3 policy applied to Chapter 2 asset categories plus phased and sustaining capex; interest on the Phase 2 facility (drawn $600 K by Month 21, interest-only through Year 3, amortizing $300 K/year across Years 4–5); tax at the **25% placeholder (verify locally)** with loss carryforward.

| P&L ($K) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenue | 1,280 | 1,905 | 2,600 | 3,030 | 3,400 |
| Operating costs | 1,380 | 1,751 | 1,970 | 2,248 | 2,470 |
| **EBITDA** | **−100** | **154** | **630** | **782** | **930** |
| EBITDA margin | −7.8% | 8.1% | 24.2% | 25.8% | 27.4% |
| Depreciation & amortization | 268 | 289 | 354 | 402 | 461 |
| **EBIT** | **−368** | **−135** | **276** | **380** | **469** |
| Interest expense | 0 | 27 | 54 | 40 | 14 |
| **Earnings before tax** | **−368** | **−162** | **222** | **340** | **455** |
| Tax (25% placeholder, after carryforward) | 0 | 0 | 0 | 8.0 | 113.8 |
| **Net income** | **−368** | **−162** | **222** | **332.0** | **341.2** |

Checks: EBIT = EBITDA − D&A each year (e.g. Y3: 630 − 354 = 276); EBT = EBIT − interest (276 − 54 = 222). Tax: cumulative losses 368 + 162 = 530 carried forward; Y3's 222 fully sheltered (remaining carryforward 308); Y4 taxable = 340 − 308 = 32 → tax 8.0; Y5 taxable 455 → 113.8. Interest ties to §6.2 (Y2 = 26.9 ≈ 27) and the amortization schedule (Y3 full-drawn $600 K × 9% = 54; average balances of $450 K and $150 K give 40 and 14). D&A ties to §7.3's schedule.

### 7.2 EBITDA bridge, Year 1 → Year 3

The move from −$100 K to +$630 K decomposes exactly; the striking feature is that **revenue grows $1,320 K while costs grow only $590 K** — operating leverage from a venue staffed and insured for capacity on Day 1.

| Bridge element | $K effect | Running EBITDA $K |
|---|---|---|
| Year 1 EBITDA | | **−100** |
| Revenue growth (frequency, memberships, Phase 2 divisions, restaurant) | +1,320 | 1,220 |
| People (restaurant team, +2 Artisans, +1 marshal, +0.5 FOH, wage drift) | −273 | 947 |
| COGS (scales with F&B/retail/events volume) | −120 | 827 |
| Fleet maintenance (utilization + Phase 2 fleet) | −52 | 775 |
| Occupancy & utilities (escalation + restaurant load) | −42 | 733 |
| Software, hosting & payments (volume-linked fees) | −39 | 694 |
| Marketing (absolute growth; falls as % of revenue, 8.0% → 5.4%) | −38 | 656 |
| Insurance (Phase 2 endorsements) | −12 | 644 |
| Admin & misc | −14 | 630 |
| **Year 3 EBITDA** | | **630 (24.2%) ✓ canon** |

Check: −100 + 1,320 − (273+120+52+42+39+38+12+14 = 590) = **630**.

### 7.3 Depreciation policy

Canonical split: **fleet-class assets 2–3 years; infrastructure 10–20 years**. The policy per category, applied to Chapter 2 costs (contingency capitalized pro-rata as a 10-year line for simplicity):

| Asset class | Cost $K | Life (yrs) | Annual D&A $K |
|---|---|---|---|
| Site & civil works | 455 | 15 | 30.3 |
| Track surfaces | 172 | 10 | 17.2 |
| Buildings | 418 | 18 | 23.2 |
| Fleet (vehicles, batteries, radios, spare hulls) | 80 | 2.5 | 32.0 (Y1–2), 16.0 (Y3) |
| RCW Node program | 25 | 2 | 12.5 (Y1–2) |
| Wi-Fi & IT | 87 | 4 | 21.8 (Y1–4) |
| RC WORLD OS v1 (capitalized software) | 165 | 5 | 33.0 |
| FF&E & theming | 118 | 6 | 19.7 |
| Pre-opening (amortized) | 162 | 3 | 54.0 (Y1–3) |
| Contingency (as spent, blended) | 168 | 10 | 16.8 |
| **Year 1 D&A from Phase 1 assets** | 1,850 | | **260.5** |

Check: 30.3+17.2+23.2+32.0+12.5+21.8+33.0+19.7+54.0+16.8 = 260.5; plus sustaining-fleet capex depreciating from mid-Year 1 (+7.2) = **268 ✓ §7.1**. Later years add the growing sustaining-fleet layer (annual charges 7.2 / 28.8 / 73.2 / 122.8 / 166.0 as the renewal program scales at 2.5-year life, half-year convention), Phase 2 assets (in service ~Month 27; full-year charge ≈$117.4 K: civil/buildings/FF&E ≈$1,098 K at a blended ~11.4-yr life ≈ 96.6, + fleet & nodes ≈$52 K incl. contingency share ÷ 2.5 = 20.8), and Phase 3 assets (first elements in service early Year 5; part-year charge ≈$37 K), while the original fleet (fully depreciated Month 30), Nodes (Month 24), Wi-Fi/IT (Month 48), and pre-opening (Month 36) roll off — producing the **268 / 289 / 354 / 402 / 461** sequence. Checks: Y3 = 232.0 remaining Phase 1 + 73.2 sustaining + 48.8 part-year Phase 2 (117.4 × 5/12) = 354; Y5 = 140.2 remaining Phase 1 + 166.0 sustaining + 117.4 Phase 2 + 37.4 Phase 3 = 461. The short fleet life is honest economics, not conservatism: a rental car at Year-3 utilization genuinely is consumed in 2–3 years, and the sustaining-capex line (§5.2) is its cash twin.

### 7.4 Payback

Cumulative EBITDA runs −100 → 54 → 684 → 1,466 → 2,396 ($K) across Years 1–5 (each year adds §7.1's EBITDA row; e.g. 684 = −100 + 154 + 630). Against **Phase 1 invested capital ($1,850 K)**: the crossing occurs when 1,850 − 1,466 = 384 of Year 5's 930 has accrued → 384 ÷ 930 × 12 ≈ 5 months into Year 5 = **operating Month ~53, early Year 5**. Against **capital actually consumed** (the $2.6 M ask less the ~$221 K still held as cash at end-Year 5, §7.6 — i.e. $2,379 K): 2,379 − 1,466 = 913 ÷ 930 × 12 ≈ 12 months → **Month ~60, end of Year 5**. The ambitious scenario (§10.1) pulls Phase-1 payback to **Month ~44 (Year 4)**; the conservative case pushes it beyond Year 5. Hence the canonical statement: **full payback Year 4–5, base case** — Year 5 on the base numbers, Year 4 achievable on the upside case, with Phase 2/3 self-funded throughout so payback is never diluted by follow-on equity.

### 7.5 Investor returns — IRR / MOIC ranges

Assumptions: Structure A cap table (investor 65%, §3.4); exit at end of Year 5 (≈6 years from close, which precedes opening by ~12 months); exit value = EV/EBITDA multiple × Year-5 EBITDA + closing cash − debt (facility fully repaid by end-Year 5); LBE/FEC venue transactions historically clear 6–9× EBITDA for proven single sites (industry transaction ranges, 2024–2026) — 6.5×/7.5×/8.5× used. Franchise value (Volume 12) excluded.

| Scenario (Y5 EBITDA / closing cash) | 6.5× exit | 7.5× exit | 8.5× exit |
|---|---|---|---|
| Conservative (520 / 100, no cash tax paid): equity value $K | 3,480 | 4,000 | 4,520 |
| — investor proceeds (65%) / MOIC / IRR | 2,262 / 0.87× / −2.3% | 2,600 / 1.00× / 0.0% | 2,938 / 1.13× / +2.1% |
| **Base (930 / 221): equity value $K** | **6,266** | **7,196** | **8,126** |
| — investor proceeds (65%) / MOIC / IRR | 4,073 / 1.57× / 7.8% | **4,677 / 1.80× / 10.3%** | 5,282 / 2.03× / 12.5% |
| Ambitious (1,280 / 560): equity value $K | 8,880 | 10,160 | 11,440 |
| — investor proceeds (65%) / MOIC / IRR | 5,772 / 2.22× / 14.2% | 6,604 / 2.54× / 16.8% | 7,436 / 2.86× / 19.1% |

Check (base/7.5×): 7.5 × 930 = 6,975 + 221 = 7,196; × 65% = 4,677; ÷ 2,600 = 1.80×; 1.80^(1/6) − 1 = 10.3%. **Stated ranges for cross-volume citation (Volume 1 quotes these exactly): base case ≈ 1.6–2.0× MOIC / ≈ 8–12.5% IRR; ambitious case ≈ 2.2–2.9× MOIC / ≈ 14–19% IRR; conservative case ≈ 0.9–1.1× MOIC.** Two upsides sit outside this table deliberately: **dividend capacity** of ~$300–400 K/year from Year 4 (post-facility-amortization free cash) adds ≈2–4 points of IRR if distributed rather than reinvested, and the **franchise program** (§10.3) is pure option value on the same equity.

> **Investor Note.** Read the base case honestly: **1.6–2.0× MOIC and high-single to low-double-digit IRR** is an infrastructure-flavored return, not a venture return — earned with real assets, a self-funding expansion path, capped follow-on exposure, and Year-4 dividend capacity. What makes the risk-reward attractive is the shape: the conservative case still returns ~0.9–1.1× (assets, cash, and a functioning business retain value), while the ambitious case and the franchise option carry venture-like upside. Investors seeking >20% IRR should price the franchise program into their thesis (Volume 12) or negotiate Structure B's downside seniority.

### 7.6 Five-year sources & uses (integrity check)

| Sources $K | | Uses $K | |
|---|---|---|---|
| Equity ask | 2,600 | Program capex (Phases 1–3) | 3,900 |
| Phase 2 facility drawn | 600 | Sustaining fleet capex (36+72+150+170+190) | 618 |
| Cumulative EBITDA Y1–Y5 | 2,396 | Facility interest (0+27+54+40+14) | 135 |
| | | Facility repayment | 600 |
| | | Cash taxes (8.0 + 113.8, §7.1) | 122 |
| | | **Closing cash, end Year 5** | **221** |
| **Total** | **5,596** | **Total** | **5,596** |

Check: 2,600 + 600 + 2,396 = 5,596 = 3,900 + 618 + 135 + 600 + 122 + 221. The model is closed: every dollar in is a dollar out or a dollar held. (The $221 K closing position sits below the $250 K policy floor only because the model repays the full facility inside Year 5; in practice the final $150 K amortization payment slides one quarter, an immaterial timing choice.)

---

## 8. Pricing Strategy & Elasticity

### 8.1 How the canonical prices were set

The price card was benchmarked against the competitor and precedent set of Volume 2, Chapter 8, positioned on a simple rule: **price the Casual Shift below a karting heat and above a trampoline hour, because the experience sits between them in intensity and above both in novelty** — then let premium classes, time-extension, and bundles do the yield work.

| Benchmark (Volume 2, Ch 8) | Typical price | RC WORLD position |
|---|---|---|
| Karting, single heat (10–15 min) | $25–35 | Casual Shift $15 undercuts at 20 min — deliberate trial-friendly entry |
| Trampoline/adventure park, per hour | $15–25 | Operator Shift $26 ≈ 40+ min of operation + pit-stop theatre |
| VR venue, per session/hour | $30–60 | Premium Operator $38 with physical, photographable machines |
| RC rental venues (small format), 15–20 min | $10–20 | $15 at radically higher production value; $22 premium classes above the band |
| Dig This-class real-machinery experience | $170–330 | Premium construction Shifts deliver the fantasy at 1/14 scale for ~1/10 the price |
| Cinema family night (4 people) | $60–80 | Family bundle $89 for a two-hour active outing — the head-to-head the marketing plan targets |

### 8.2 Price ladders and bundle logic

Every step of the ladder is priced off the $15 base with a visible, defensible ratio — customers should *feel* the logic, and staff should be able to explain it in one sentence.

| Product | Price | Ratio logic (arithmetic) |
|---|---|---|
| Casual Shift — standard | $15 | Base unit: 1 block |
| Casual Shift — premium | $22 | 1.47× base: premium classes carry supervision and higher-value machines (hydraulics, FPV, big crawlers) |
| Operator Shift — standard | $26 | 2 blocks à la carte = $30; bundle saves $4 (13%) and includes the battery-swap pit stop — rewards commitment, smooths queues |
| Operator Shift — premium | $38 | 2 × $22 = $44 − $6 (14%) — same discount discipline |
| Day Pass | $59 | ≈ 5–6 casual blocks of value for 3.9× base; average redemption 4 blocks (§4.4) keeps per-block yield at $14.75 while capping the customer's spend anxiety |
| Family bundle | $89 | 4 drivers × 2 shifts = 8 blocks; à la carte $120; 26% family discount targets the highest-LTV segment |
| Memberships $29/$59/$99 | monthly | Priced at ≈2/4/6.6 casual blocks; pays back for the customer at 2–3 visits/month, exactly the frequency Volume 9's loyalty ladder engineers |
| Corporate from $1,400 | 2 h / 20 pax | = $70/head against a $90–150/head corporate-event market norm; catering and premium classes upsell to the $1,600 realized average (§4.6) |
| Parties from $349 | 10 children | = $34.90/child vs $25–45 party-market band; includes host, blocks, and party room |

### 8.3 Dynamic and peak pricing options

Phase 1 opens with **fixed prices** (trust-building and operational simplicity), with three instrumented options held ready in RC WORLD OS, activated only on evidence: (1) **peak/off-peak spread** — ±$3 on the Casual Shift (Sat-afternoon $18, midweek-morning $12), projected +4–6% Shift revenue at neutral volume based on observed FEC peak-pricing outcomes; (2) **Top-Up dynamic offers** — the existing T-5-minute top-up mechanic (canon) priced 10–20% below counter rate when the queue roster is empty, converting perishable slot inventory; (3) **event-yield pricing** — league entries and night events priced by demand tier. Elasticity beliefs used in Chapter 9 (category benchmarks, to be replaced by A/B evidence from Month 6): casual/family segments ≈ −0.8 around the $15 anchor; enthusiast/premium ≈ −0.4; corporate/parties ≈ −0.3.

### 8.4 Discount governance

Discounting is the fastest way to destroy a yield model, so it is governed: **headline prices never discount** (no "50% off Shifts" — it reprices the anchor permanently); all discounts flow through **defined channels with owners and caps** — schools/education 20% (owner: GM), corporate volume tiers to 15% (sales), member benefits as *included blocks* rather than % off (product design, Volume 9), promotional trials as time-boxed bundles (marketing, ≤500 units/quarter). Every comp and discount posts to a **comp register in RC WORLD OS** reviewed monthly against a ceiling of **2.5% of gross revenue**; Gears loyalty redemptions are budgeted separately at ≤1.5% of revenue as a marketing cost (Volume 9 mechanics).

> **Investor Note.** The pricing architecture is built so that **yield grows without headline price rises**: premium-class mix, operator conversion, day-pass redemption depth, membership penetration, and (later) peak spreads are five independent yield levers, each worth 2–6% of Shift revenue. The plan needs none of them heroically; Chapter 9 shows what ±15% on price itself would do, and §8.3's elasticity beliefs are why the model prefers mix to price.

---

## 9. Sensitivity Analysis

### 9.1 Method

Each stress is applied to the base model in isolation (ceteris paribus), then read out on the two management-critical outputs: **break-even month** (base: Month 16, band 16–19) and **Year 3 EBITDA** (base: $630 K, 24.2%). Flow-through logic: revenue-volume changes carry ≈82% contribution (variable costs ≈18% scale away); price changes carry ≈95% contribution net of payment fees, before elasticity feedback; volume-linked share of revenue ≈92% (memberships and sponsorship lag volume in-year).

### 9.2 Tornado table

| Scenario | Mechanics ($K arithmetic on Year 3) | Y3 EBITDA ($K / margin) | Break-even month |
|---|---|---|---|
| **Visitors +20%** | Rev +20% × 92% × 2,600 = +478; × 82% contribution → **+392** | 1,022 / 33% | ~Month 12–13 |
| **Visitors −20%** | Mirror: −478 revenue → **−392** | 238 / 11% | ~Month 24–28 |
| **Price +15%** (elasticity −0.4 enthusiast-weighted) | Price-bearing rev 2,360 × 15% = +354; volume gives back 2,360 × 6% × 82% ≈ −116 → **+238** | 868 / ~30% | ~Month 13–14 |
| **Price −15%** | Mirror with weaker volume recovery (families don't fully backfill): **−260** | 370 / ~16% | ~Month 20–23 |
| **Fleet maintenance +25%** | §5.2 Y3 line 118 × 25% = **−30** | 600 / 23.1% | +1 month (~17–20) |
| **Capex overrun +20%** (Phase 1 +$370) | No P&L effect; cash effect −370: opening cash 750 → 380; Month-14 trough 476 → 106, **breaching the $250 K floor** | 630 / 24.2% (unchanged) | Unchanged — but funding action required (§9.4) |
| **FX/shipping shock +30% on China sourcing** | Opex: parts+batteries+consumables ≈ 107 of Y3 fleet line × 30% ≈ **−32**/yr; capex: sustaining fleet 150 → ~195 (cash, not EBITDA) | 598 / 23.0% | +1 month (~17–20) |

Ordering confirms the tornado shape: **visitor volume (±$392 K) > price (±$238–260 K) > FX (−$32 K) ≈ maintenance (−$30 K)**, with capex overrun a *cash* risk rather than a P&L risk. This is why marketing spend is protected in the cost-flex ladder (§6.5) while maintenance over-run is absorbed: the model is demand-fragile and cost-robust — the right shape for a venue, and the reason the KPI dashboard (§10.4) leads with demand indicators.

### 9.3 Compound downside

The honest nightmare is correlated: −20% visitors *and* +25% maintenance *and* a capex overrun (a rushed build causing quality problems suppressing demand). Stacked: Year 3 EBITDA ≈ 630 − 392 − 30 ≈ $208 K (8%); break-even drifts to Months 26–30; the Month-14 cash trough breaches the floor. Survival mechanics: the cost-flex ladder holds the stack near Flex-2 (~$1.1 M) buying ≈$180 K/year back; Phase 2 defers per its gate (releasing the $780 K Year-2 spend and its facility); the $180 K unallocated reserve deploys. Modelled through, the park survives at roughly the conservative scenario of Chapter 10 with Phase 2 delayed 12 months — impaired returns (≈1× MOIC), not insolvency. That resilience is bought by three design choices: phase gating, the fixed-cost-light fleet, and the reserve inside the $2.6 M.

### 9.4 Downside triggers and mitigations

| Trigger (monitored in RC WORLD OS, monthly board pack) | Threshold | Pre-agreed mitigation |
|---|---|---|
| Rolling 8-week revenue vs plan | <85% / <75% / <60% | Cost-flex Stages 1/2/floor (§6.5); marketing remix before any price action |
| Month-end cash vs policy floor | <$350 K notify / <$250 K act | Freeze sustaining capex; draw reserve; if pre-opening: descope ladder (§2.11) — theming → grandstand-class scope → never OS, safety, or spares |
| Capex committed vs budget (pre-opening, monthly) | >95% of category budget with work remaining | Contingency release protocol; re-tender remaining packages; T2/T3 gate review with investors |
| Maintenance cost per vehicle-hour | >$4.00 for 2 consecutive months | Volume 7 failure-data review; supplier/QC audit (Volume 8); fleet-class retirement review |
| Price test results (any §8.3 experiment) | Contribution-negative at 95% confidence | Revert within one week; elasticity belief updated in this chapter's next revision |
| FX (USD-RMB) or freight index | ±15% vs plan | Forward-order 2 quarters of spares (≈$25 K working capital); re-quote across Volume 8's second-supplier matrix |

---

## 10. Growth Scenarios

### 10.1 Conservative / base / ambitious — five-year view

Assumptions differ only on the demand side and phasing pace; the cost machinery (Chapter 5) and cost-flex ladder (§6.5) apply in all three. The base case **is** the canon of Chapters 4–7.

| Assumption | Conservative | Base | Ambitious |
|---|---|---|---|
| Year 1 visits | ≈31 K (−20%) | ≈39 K | ≈46 K (+18%) |
| 90-day second-visit rate | 17% | 22% | 28% |
| End-Y1 members | 220 | 344 | 470 |
| Phase 2 timing | Gated: delayed to Months 19–36, Marine-first descope | Months 13–30 | On schedule, restaurant pulled forward 3 months |
| Phase 3 | Deferred indefinitely (arena case fails hurdle) | Months 37–60 selective | Full program + franchise pilot at Month 36 |
| Blended per-cap spend trend | Flat $28 | $30 → $33 | $31 → $36 |

| Output ($K) | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Conservative** — revenue | 1,020 | 1,450 | 1,950 | 2,250 | 2,500 |
| — EBITDA (margin) | −230 | 20 (1%) | 330 (17%) | 430 (19%) | 520 (21%) |
| **Base (canon)** — revenue | 1,280 | 1,905 | 2,600 | 3,030 | 3,400 |
| — EBITDA (margin) | −100 | 154 (8%) | 630 (24%) | 782 (26%) | 930 (27%) |
| **Ambitious** — revenue | 1,450 | 2,300 | 3,200 | 3,900 | 4,500 |
| — EBITDA (margin) | −40 | 320 (14%) | 870 (27%) | 1,090 (28%) | 1,280 (28%) |

Derived markers: break-even Month 22–26 / **16–19** / 12–14; Phase-1 payback beyond Year 5 / **Month ~53** / Month ~44 (ambitious cumulative EBITDA: −40+320+870 = 1,150 by end-Y3; 1,850−1,150 = 700 ÷ 1,090 × 12 ≈ 8 months into Year 4). Note the conservative case still reaches a **21% margin business worth roughly its invested capital** — the downside is mediocrity, not wipeout — while the ambitious case is deliberately *not* heroic: +18% Year-1 visits (≈46 K) barely exceeds the top of Volume 2's ~37–43 K demand band (Chapter 9), and its margins are capped at 28% (canon) rather than allowed to inflate.

### 10.2 Phase 3 optionality

Phase 3 is a menu, not a bundle: each element clears a standalone hurdle (incremental EBITDA ÷ element capex ≥ 25%) at the operating Month-30 review, funded from cash flow only. Planning estimates: **indoor arena** ($452 K) — removes the weather ceiling on ~30% of currently-lost days and unlocks winter leagues; projected +$260–340 K revenue at ~45% incremental margin → ROIC ≈ 26–34%, the strongest and most strategic case (it is also the structural fix for the weather-compression risk carried in the master risk register, Volume 1, Chapter 8). **Night-racing lighting** ($78 K) — +$60–90 K high-margin event revenue → ROIC ≈ 35–55%, cheapest yes. **Academy classrooms** ($108 K) — education line 60 → 100+ with school-day utilization of empty midweek capacity → ROIC ≈ 20–30%, borderline standalone but strategically loaded (feeds licensing and franchise training). **Corporate event centre** ($132 K) — corporate 205 → 240+ at high margin → ROIC ≈ 20–26%. Elements failing their hurdle at operating Month 30 are re-tested annually; the base case assumes all four proceed across operating Months 37–60 within the $900 K envelope.

### 10.3 Franchise upside (pointer to Volume 12)

Nothing in this volume's canon includes franchising, deliberately. Volume 12 develops the model — franchise fee, royalty on gross revenue, RC WORLD OS SaaS fee per site, and procurement margin via the Volume 8 supply chain — with its pilot gated on three Volume-10 facts being demonstrated at the flagship: sustained 24%+ EBITDA margin (Year 3), a documented operating system (Volumes 3–9 SOPs live in RC WORLD OS), and a replicable capex bill of materials (Chapter 2 of this volume, which doubles as the franchise build budget template). For scale: each franchised site paying a mid-single-digit royalty on revenues comparable to this park's Year-3 canon would contribute high-five to low-six figures of near-pure-margin annual royalty — economics equivalent to adding a division for zero capex. Treat every franchise dollar as upside to §7.5's returns, not as plan.

### 10.4 KPI dashboard definition

The park is managed on ten numbers, computed continuously by RC WORLD OS (implementation: Volume 13, Chapter 9; review cadence: weekly ops, monthly board). Definitions are fixed here so every volume and every site computes them identically.

| KPI | Definition (exact) | Y1 target | Y3 target |
|---|---|---|---|
| RevPASH (revenue per available Shift-hour) | Shift & session revenue ÷ (concurrent stations × operating hours). Y1: 786.2 K ÷ (57 × 8 × 360) = **$4.79** | ≥ $4.75 | ≥ $6.50 (74 stations post-Phase 2: 1,390 K ÷ 213,120 = $6.52) |
| Slot utilization | Blocks consumed ÷ slot capacity (§4.3). Y1: 57,720 ÷ 328,320 = **17.6%** | ≥ 17% | ≥ 24% |
| Membership count / churn | Active members at month-end / cancellations ÷ opening members | 344 / ≤3.5%/mo | ~620 avg / ≤2.5%/mo |
| 90-day second-visit rate | First-time visitors returning within 90 days (cohort-tracked). This table is the KPI's canonical home; the Phase 2 gate uses a **floor of ≥ 20%** (§3.5) | ≥ 22% | ≥ 28% |
| Maintenance cost per vehicle-hour | Total §5.2 fleet cost ÷ telemetry-logged vehicle-hours. Y1: 66,000 ÷ 20,000 = **$3.30** | ≤ $3.50 | ≤ $3.40 |
| Fleet availability | Fleet-hours in `active` status ÷ scheduled fleet-hours (from `fleet_inventory`); gate floor ≥ 90% | ≥ 92% | ≥ 94% |
| F&B attach | F&B revenue ÷ gate visits. Y1: 158 K ÷ 42 K = **$3.76** | ≥ $3.75 | ≥ $4.40 (restaurant) |
| Per-cap spend | (Total revenue − sponsorship − education) ÷ gate visits | ≥ $30 | ≥ $33 |
| Labor ratio | People cost ÷ revenue (§5.1) | ≤ 60% | ≤ 41% |
| NPS | Standard survey, pushed post-visit via app | ≥ 55 | ≥ 60 |

> **Investor Note.** Insist on this dashboard in the monthly pack from opening week, and on the definitions above rather than management-friendly variants. The first two KPIs (RevPASH and utilization) are the earliest honest indicators of whether the Chapter 4 engine is performing — they move weeks before revenue misses become visible — and the second-visit rate is the single best predictor of whether Year 2–3 canon is reachable, because everything in the growth model (§4.9) is frequency, not reach.

---

## 11. Volume summary & cross-references

This volume built RC WORLD's complete financial system and reconciled every output to the canonical headlines. **Capex:** Phase 1 builds bottom-up to $1,850 K across nine audited categories plus 10% contingency, with the striking structural fact that the entire ~150-asset fleet is only $80 K (4.3%) of it; Phase 2 ($1,150 K) and Phase 3 ($900 K) envelopes complete the ≈$3.9 M five-year program. **Funding:** the $2.6 M ask = $1,850 K capex + $750 K of working capital, operating funding, and reserve, drawn in three milestone-gated tranches ($1,200/$850/$550 K), with Phases 2–3 self-funded from cash flow plus an optional $600 K facility. **Revenue:** a bottom-up engine (39 K paid visits, 57 stations, 17.6% utilization, the canonical price card) lands Year 1 at $1,280 K monthly-reconciled, and the five-year table at $1,905 K / **$2,600 K** / $3,030 K / **$3,400 K** — sitting inside Volume 2's independent ~37,000–43,000-visit, $30–35-per-visit demand estimate (Chapter 9). **Costs and margin:** an $1,380 K Year-1 stack (60% people-weighted) grows only $590 K while revenue grows $1,320 K to Year 3, delivering EBITDA of −$100 K / $154 K / $630 K / $782 K / $930 K and the canonical **24–28% margin from Year 3**. **Cash:** the monthly model shows sustained operating break-even at **Month 16** (canonical band 16–19), a minimum cash of $476 K against a $250 K policy floor, and a closed five-year sources-and-uses at $5,596 K. **Returns:** payback **Year 4–5** (base Month ~53 on Phase 1 capital), base-case investor MOIC 1.6–2.0× / IRR 8–12.5% with conservative-case capital protection and ambitious-plus-franchise upside to ≈2.9× / ≈19%.

Line items other volumes must treat as fixed (change them here first, then sweep): the Chapter 2 capex categories and totals; the $750 K opening cash and tranche gates (Chapter 3); the §4.4 price-volume table and §4.9 annual revenue lines; the §5.1 staffing establishment and §5.6 opex stack; the operating-Month-16 break-even mechanics and §6.5 survival floor (≈$0.9 M); the §7.3 depreciation policy; and the §10.4 KPI definitions (including the second-visit operating targets ≥22%/≥28% with the ≥20% Phase 2 gate floor).

Cross-references: market and demand inputs — **Volume 2** (Chapter 8's competitor and precedent benchmarks feed §8.1; Chapter 9's demand analysis, §9.4–9.5, feeds §4.2 and reconciles with Chapter 4's visit totals; the master risk register lives in Volume 1, Chapter 8). Division revenue capacity and operating doctrine — **Volumes 3–6** (station counts in §4.3; division attribution in §4.9). Maintenance failure data and spares doctrine behind §5.2 — **Volume 7**. Procurement costs, landed-cost build-ups, and FX mitigation behind §2.5 and §9.4 — **Volume 8**. Membership, loyalty, parties, and the retention machinery that drives §4.5 and the second-visit KPI — **Volume 9**. Site works, buildings, and the world-building scope priced in §§2.2–2.4 — **Volume 11**. Franchise economics and localization of this model — **Volume 12** (Chapter 3 rebuilds Chapter 4 with local inputs). RC WORLD OS scope capitalized in §2.8 and the KPI dashboard implementation — **Volume 13**.
