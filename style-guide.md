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
- Break-even ≈ Month 16–19 (monthly operating break-even), full payback Year 4–5 base case.
- Funding ask: **$2.6 M** (Phase 1 capex + working capital + contingency), staged tranches.

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

## 4. Cross-referencing

Refer to other volumes as "see Volume 7, Chapter 4". Do not duplicate large blocks of another
volume's content; summarize in one paragraph and cross-reference.

## 5. Page arithmetic

Target ≈ 380–420 words per finished page (dense tables count ~60% of their line count).
Volume word targets are set in `volumes/README.md`. Do not pad; add depth (procedures, tables,
worked examples, calculations) rather than repetition.
