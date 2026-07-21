# RC WORLD Master Development Plan — Style Guide & Canon

All volumes MUST follow this guide. It exists so that twelve separately-drafted volumes read as
one coherent book and never contradict each other on facts, names, or numbers.

---

## 1. Voice and format

- Professional, confident, investor-and-operator grade. Write like a top consulting firm's
  deliverable crossed with a workshop manual: precise, practical, no filler.
- Markdown source. One file per volume in `volumes/`. Level-1 heading = volume title only.
  Level-2 = chapters (numbered `1.`, `2.` …). Level-3 = sections (`1.1`, `1.2` …).
- Every volume opens with: a one-paragraph "Purpose of this volume", an "Intended readers" line,
  and a chapter list. Every volume closes with a "Volume summary & cross-references" section
  pointing to related volumes.
- Use tables liberally for specifications, budgets, schedules, matrices. Use blockquotes for
  "Field Note", "Trade Hack", "Safety Warning", and "Investor Note" callouts.
- Checklists use `- [ ]` task syntax. SOPs use numbered steps with a standard header block
  (SOP ID, revision, owner, PPE, tools, frequency).
- Cite external market data as ranges with the source category (e.g. "industry analysts
  (2025–2026) place the global RC car market between $1.5 B and $6.2 B depending on scope").
  Never invent a fake precise citation.
- Currency: USD. Units: metric first, imperial in parentheses where useful.
- Dates: the plan is written July 2026. "Year 1" = first full operating year.

## 2. Canonical naming

| Term | Canonical usage |
|---|---|
| Park brand | **RC WORLD** (all caps in headings; "RC World" acceptable in prose) |
| Internal project codename | Omni-Zone (legacy, reference only) |
| Divisions | Motorsport Division; Construction Division (incl. Mining & Agriculture zones); Aviation Division; Marine Division |
| Workshop | **The Works** — central engineering & workshop facility |
| Technicians | **Artisans** (customer-facing title); "technician" acceptable in technical prose |
| Billing unit | The **Shift** — one 20-minute operating block |
| Session types | Casual Shift (1 block); Operator Shift (2+ blocks with pit-stop battery swap) |
| Telemetry hardware | **RCW Node** (Micro-Node ~25×25 mm; Heavy-Node ~40×30 mm) |
| Software platform | **RC WORLD OS** — the ERP covering finance, HR/payroll, payments, bookings, fleet management, live telemetry and all other business functions. Backend: Supabase (PostgreSQL) + Kotlin services. Client apps: **Kotlin Multiplatform / Compose Multiplatform targeting both Android and iOS** (staff and customer apps), plus a web admin console. Role-based access control gives each user class (executive, finance, HR, operations, artisan/technician, marshal, front-of-house, franchisee, customer) its own interface. Full detail: Volume 13. |
| Customer program | **RC WORLD License** (tiered driver-license progression, see Volume 9) |
| Recovery gameplay | **Tow-Truck Retrieval Protocol** |
| Induction | **Toolbox Talk** digital induction |
| Loyalty currency | **Gears** (earned points) |

## 3. Canonical facts and numbers (do not contradict)

### Site & phasing
- Reference site: **4.8 hectares (~12 acres)** leased peri-urban land, mid-size international
  city, flat with 2–4% natural grade, road frontage, municipal power + water.
- **Phase 1 (Months 0–12, "Core Park")**: Motorsport Division (Tracks A/B/C), Construction
  Division (Mining Zone + Agriculture Zone), The Works, pit lane, charging bunker, entry
  pavilion with F&B kiosk and small retail counter. Wi-Fi mesh + RC WORLD OS v1.
- **Phase 2 (Months 13–30, "Full Park")**: Aviation Division (netted airfield), Marine Division
  (pond complex), full restaurant, expanded retail, grandstand viewing, events lawn.
- **Phase 3 (Months 31–60, "Destination & Beyond")**: indoor all-weather arena, RC Academy
  classrooms, corporate event centre, franchise pilot, night-racing lighting.
- Capex: **Phase 1 ≈ $1.85 M; Phase 2 ≈ $1.15 M; Phase 3 ≈ $0.9 M; five-year total ≈ $3.9 M**
  (detail in Volume 10; Volume 1 carries the summary).

### Fleet (Phase 1 baseline, ~150 powered assets)
- Motorsport: 64 cars — 24 touring/GT (LDRC/MJX 1/14 entry + 1/10 standard), 12 drift (MST-based),
  12 buggy/rally (WLtoys 144010-class upgraded), 8 short-course, 8 formula/drag special events.
- Construction & Mining: 30 — 6 excavators (Huina 1580 class), 18 dump trucks (1:3 ratio),
  3 wheel loaders (Huina 1583), 2 dozers, 1 premium hydraulic showcase machine (Kabolite class).
- Agriculture: 12 tractors (Double E E351 / 1/16) + implement library.
- Crawler park: 16 (MN99S / WPL C24 class + 4 premium 1/10 TRX-4 class).
- Recovery fleet: 4 × 1/10 winch-equipped recovery crawlers.
- Utility/marshal vehicles, plus Phase 2 adds aviation (~20 aircraft) and marine (~24 vessels).
- Batteries: 3:1 per vehicle minimum, 2S/3S LiPo, XT60 standard (Deans legacy acceptable).

### Pricing anchors (Year 1, adjust locally)
- Casual Shift: **$15** (standard classes) / $22 (premium classes: hydraulics, FPV, big crawlers).
- Operator Shift (2 blocks + battery-swap pit stop): $26 / $38.
- Day Pass: $59. Family bundle (4 drivers × 2 shifts): $89.
- Membership: Apprentice $29/mo; Operator $59/mo; Foreman $99/mo (details Volume 9).
- Corporate events: from $1,400 (2 h, 20 pax). Birthday parties: from $349 (10 children).

### Financial headline canon (Volume 10 is the source of truth)
- Year 1 revenue ≈ **$1.28 M**; Year 3 ≈ $2.6 M; Year 5 ≈ $3.4 M (base case).
- Steady-state EBITDA margin ≈ 24–28% from Year 3.
- Break-even ≈ operating Month 16–19 (monthly operating break-even), full payback Year 4–5 base case.
- Funding ask: **$2.6 M** = $1,850 K Phase 1 capex (pre-opening and 10% contingency capitalized
  inside it) + $130 K working capital + $350 K operating funding through break-even + $90 K
  corporate/legal + $180 K unallocated reserve. Tranches: $1.2 M at close / $850 K ≈ operating
  Month −5 / $550 K at opening (Volume 10, Chapter 3 gates).
- Base-case investor outcome ≈ **1.6–2.0× MOIC** over a five-year hold; ambitious case ≈ 2.2–2.9×.
- Second-visit KPI (90-day): operating target ≥22% Year 1 / ≥28% Year 3 (home: Volume 10 §10.4);
  Phase 2 gate floor ≥20%. Fleet availability: operating target ≥92% (Y1) / ≥94% (Y3); gate floor ≥90%.
- Year 1 establishment ≈ **18.5 FTE** plus casuals (Volume 10, Chapter 5).

### Month-numbering convention
- **Project frame** for build phasing: Phase 1 = project Months 0–12 (park opens at project
  Month 12), Phase 2 = project Months 13–30, Phase 3 = project Months 31–60.
- **Operating frame** for all financial statements and division opening schedules: operating
  Month 1 (M1) = the opening month. Break-even Month 16–19, aviation staged opening Months 16–24
  (sim lab M16, fixed-wing M19–20, full program M23–24), marine opening Months 20–24 are all
  OPERATING months. When ambiguity is possible, label the frame explicitly.

### Built-form canon (Volume 11 is the source of truth for geometry)
- Aviation cage: **60 × 40 m footprint, 15 m clear flight ceiling**, 16–17 m masts, 25 mm
  knotless HDPE mesh; 12 × 8 m Whoop Arcade (13 mm mesh); two helipads 1.5 × 1.5 m at 1.0 m.
- Marine: two hydraulically independent ponds — harbour 30 × 18 m + speed 60 × 25 m,
  400–600 mm working depth, 6 × 4 m submarine bay at 1.5 m (sole exception); civil ≈ $212 K
  inside Volume 10's $231 K marine line.
- The Works: **450 m² GFA** (workshop core ~180 m², battery room 24 m², charging bunker 30 m²
  internal, parts store, QC lane, viewing window). Entry pavilion 490 m² (retail 120 m²).
  Restaurant 380 m², 120 + 60 covers. Parking 88 bays Phase 1 → 132 + 4 bus.
- Aviation Phase 2 allocation ≈ $364 K (enclosure $190 K, civil $85 K, sim lab $45 K, fleet $32 K,
  timing/AV $12 K) — Volume 10 carries this within the $1.15 M Phase 2 envelope.

### Operating doctrine (from source PDFs — must be honoured everywhere)
- Excavator : dump truck ratio **1:3**.
- Haul road max incline **15°**.
- LiPo operating window **3.4–4.2 V/cell**; 3:1 battery:vehicle ratio; bunkered charging room.
- 20-minute Shift billing decoupled from battery life; ~30% buffer returned.
- Telemetry kill-switch on under-voltage or geofence breach (PWM intercept).
- Customers never walk onto live tracks; Tow-Truck Retrieval Protocol instead.
- Rental construction fleet = electromechanical (lead-screw) machines, NOT hydraulic;
  hydraulic (Kabolite class) reserved for premium supervised experiences and display.
- Racing fleet: standardized chassis, personalities via tuning, lap-time parity within 2–3%.

### Bootstrap edition canon (Volume 14 is the source of truth)

The founder launches self-funded BEFORE the master plan's Phase 1: the **RC WORLD Micro-Park**.
The 13-volume master plan is unchanged and remains the growth/investor documentation; Volume 14
adapts its doctrine to bootstrap scale.

- Budget: **$10,000 all-in** (fleet, batteries, site works, tools, admin, contingency).
- Site: **300 m²** leased/borrowed space (indoor warehouse bay or fenced yard).
- Scope: **Construction Division only** — metal, electric, electromechanical (lead-screw)
  machines. **No hydraulics anywhere in the bootstrap fleet**: hydraulic equipment (Kabolite
  class) is explicitly deferred as the first major upgrade purchased from operating proceeds.
- Doctrine retained at micro scale: 20-minute Shift billing, excavator:dump-truck 1:3 ratio,
  LiPo 3.4–4.2 V/cell window, 3:1 battery ratio, XT60 standard, customers never enter the dig
  zone, daily inspections, spares-with-fleet ordering.
- Doctrine deferred: RCW Node telemetry and RC WORLD OS (replaced by manual/spreadsheet +
  phone-timer operation), Wi-Fi mesh, all other divisions, buildings.
- Upgrade ladder: reinvested proceeds climb Micro-Park → expanded micro fleet → hydraulic
  premium tier → multi-zone mini-park → master plan Phase 1 (with external investors, using
  Volumes 1–13 as the prospectus).

## 4. Cross-referencing

Refer to other volumes as "see Volume 7, Chapter 4". Do not duplicate large blocks of another
volume's content; summarize in one paragraph and cross-reference.

## 5. Page arithmetic

Target ≈ 380–420 words per finished page (dense tables count ~60% of their line count).
Volume word targets are set in `volumes/README.md`. Do not pad; add depth (procedures, tables,
worked examples, calculations) rather than repetition.
