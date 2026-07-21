# RC WORLD — Master Development Plan: Front Matter

**RC WORLD — Master Development Plan** · Volume 0 (Front Matter) of 14 volumes
**Revision 1.0 — July 2026** · Status: Living document — bump revision on material change

**Purpose of this volume.** This volume is the reader's entry point to the entire Master Development Plan. It carries the title page and document-control record, tells each class of reader — bootstrapping founder, investor, lender, architect, operator, technician, franchisee — which volumes to read and in what order, defines the living-document maintenance workflow that keeps fourteen separately maintained volumes consistent, presents the master table of contents with a synopsis of every volume, and fixes the glossary of canonical terms used identically throughout the plan. Nothing in this volume introduces new facts; where a number appears here, its source of truth is `style-guide.md` and the volume cited.

**Intended readers.** Everyone who opens any part of the Master Development Plan, before they open it.

**Chapters**

1. Title Page
2. Document Control & Revision History
3. How to Use This Master Plan
4. Living-Document Maintenance Workflow
5. Master Table of Contents
6. Glossary of Canonical Terms
7. Volume Summary & Cross-References

---

## 1. Title Page

**RC WORLD**
**MASTER DEVELOPMENT PLAN**

*Investor Prospectus • Operations Manual • Engineering Handbook*

A complete plan for the design, financing, construction, and operation of a large multi-zone radio-controlled vehicle theme park — a **miniaturized industrial complex** spanning motorsport racing, open-pit mining and construction simulation, commercial agriculture, aviation, and marine operations, supported by in-house telemetry hardware (the **RCW Node**), a custom enterprise platform (**RC WORLD OS**), and a central engineering facility (**The Works**).

Fourteen volumes plus this front matter. Approximately 470–520 finished pages. The plan operates on two horizons: the self-funded **Micro-Park** launch ($10,000, 300 m² — Volume 14) and the full investor-funded park (Volumes 1–13), unchanged as the growth target.

Internal project codename: *Omni-Zone* (legacy; reference only).
Prepared: **July 2026**. Currency: USD. Units: metric first, imperial in parentheses.
Funding ask: **$2.6 M**, staged tranches (Volume 1, Chapter 6; Volume 10).

*Confidential. Prepared for investors, lenders, design professionals, staff, and prospective franchisees. Distribution restricted; see document control below.*

## 2. Document Control & Revision History

### 2.1 Control record

| Field | Value |
|---|---|
| Document title | RC WORLD — Master Development Plan |
| Document set | 14 volumes + front matter, one markdown file per volume in `volumes/` |
| Canonical style & numbers | `style-guide.md` (single source of canonical facts) |
| Source material | `source-material/original-notes-digest.md` (founder's three planning PDFs + brief) |
| Build | `python3 build/assemble.py` → single combined document (`.md`, `.docx`, `.pdf` if pandoc present) |
| Owner | Founder / Managing Director, RC WORLD |
| Review unit | One volume = one file = one independent review and revision unit |
| Classification | Confidential — investor and internal distribution only |

### 2.2 Revision history

| Rev | Date | Scope | Author | Notes |
|---|---|---|---|---|
| 1.0 | July 2026 | Initial complete issue of all volumes | Founder + drafting team | Baseline for Phase 1 financing round |
| — | — | *(next entries added per-volume; see Chapter 4)* | — | — |

Each volume carries its own revision line in its header block: the *set* revision is the table above; a *volume's* revision is its header. A combined build lists both.

## 3. How to Use This Master Plan

This plan serves six end uses at once: the self-funded launch, investor presentations, financing applications, architect/contractor guidance, employee training and daily operations, and future franchising. No reader needs all ~500 pages; each needs a defined path through them.

### 3.1 The founder, bootstrapping

Read **Volume 14 (Bootstrap Launch Plan)** first — the day-to-day operating plan for the $10,000 / 300 m² Micro-Park. Its technical backing is **Volume 4** (the Construction Division doctrine the Micro-Park inherits) and **Volume 7** (maintenance and rebuild skills, scaled down in Volume 14, Chapter 7). Volumes 1–13 become active at the external-raise milestone — Rung 5 of Volume 14's upgrade ladder — as the prospectus, unchanged.

### 3.2 Investors (equity)

Read **Volume 1** in full — the whole business in one volume, including the $2.6 M ask, tranche structure, phase gates, and returns summary. Then **Volume 10 (Finance)** for the full model and sensitivities, and **Volume 2 (Market Research)** for the demand case and competitive landscape. Volumes 3–6 are your diligence layer: each division volume shows what the money builds and how it earns. Volume 13 explains the technology moat.

### 3.3 Lenders and grant bodies

Start with Volume 1, Chapters 6–9 (ask, phases, financial overview, risk summary), then **Volume 10** for debt-service coverage and break-even (canonically operating Month 16–19, where operating Month 1 = the opening month), then **Volume 11 (Architecture & Park Design)** for the fixed-asset base and **Volume 1, Chapter 9** plus the per-volume risk registers for the risk picture. The staged-tranche structure in Volume 1, Chapter 6 maps onto milestone-based drawdowns.

### 3.4 Architects, engineers, and contractors

**Volume 11** is your primary document: site plan, zone-by-zone civil specification, utilities, drainage, netting and pond engineering, and CAD-style layout concepts. Read it alongside the division volumes for functional requirements — Volume 3 (tracks), Volume 4 (mining circuit and haul roads, maximum 15° incline; field grid), Volume 5 (netted airfield), Volume 6 (pond complex) — and Volume 13 for cabling, Wi-Fi mesh, and the charging bunker's electrical load.

### 3.5 Operations staff and managers

Your induction sequence: Volume 1, Chapters 1–5 (what RC WORLD is), then **Volume 9 (Customer Experience & Loyalty)** for the customer journey, License tiers, and service standards, then the division volume for your assignment and its SOPs, checklists, and emergency procedures alongside **Volume 7**. Managers add Volume 10 (budgets, KPI definitions) and Volume 13 (RC WORLD OS role-based interfaces).

### 3.6 Technicians (Artisans)

**Volume 7 (Engineering & Workshop Manual)** is your handbook: maintenance schedules, rebuild procedures, failure catalogues, trade hacks, custom-build instruction, and the preventive-maintenance matrices. Pair it with **Volume 8 (Procurement Handbook)** for parts sourcing and spares, the maintenance chapters of your division volume, and Volume 13 for logging work in RC WORLD OS.

### 3.7 Franchisees

**Volume 12 (Franchise Manual)** is the contract-adjacent document: what the RC WORLD franchise includes, localization method, fees, and support model. Volumes 1, 9, and 10 give you the business logic; Volume 8 the supply chain you inherit; Volume 13 the multi-site RC WORLD OS architecture that makes a franchise operable from day one.

> **Investor Note.** The plan is deliberately modular. A financing application, a contractor tender pack, and a staff handbook can each be assembled from whole volumes without editing — which is also why canonical numbers live in one place and are never restated with local variations.

## 4. Living-Document Maintenance Workflow

The plan is a living document. Suppliers change models, prices drift, and phase experience will correct assumptions. The workflow that keeps fourteen volumes coherent:

1. **One volume = one review unit.** Any volume may be revised independently. On material change, bump that volume's revision line (e.g. 1.0 → 1.1); the set-level table in Chapter 2 records set-wide reissues only.
2. **Canonical numbers change in one place first.** Pricing anchors, fleet counts, capex, phase definitions, and headline financials live in `style-guide.md`. To change one: update the style guide, sweep every volume that cites it, bump affected revisions. Never patch a canonical number in a single volume.
3. **Supersession is explicit.** Where a volume extends or overrides a decision recorded in the source-material digest, it must say so in the text ("this supersedes…"). Silent divergence is a defect.
4. **Rebuild after every sweep.** Run `build/assemble.py` to regenerate the combined document; the combined build is the only artifact distributed externally.
5. **Ownership.** Each volume has a natural owner (division lead, finance lead, CTO for Volume 13); the founder/MD owns the style guide and arbitrates conflicts.

## 5. Master Table of Contents

| # | Volume | Words (target) |
|---|---|---|
| 0 | Front Matter (this volume) | 2,500 |
| 1 | Executive Master Plan | 14,000 |
| 2 | Market Research & Competitive Landscape | 15,000 |
| 3 | RC Motorsport Division | 16,000 |
| 4 | RC Construction Division | 14,000 |
| 5 | Aviation Division | 12,000 |
| 6 | Marine Division | 12,000 |
| 7 | Engineering & Workshop Manual | 20,000 |
| 8 | Procurement Handbook | 18,000 |
| 9 | Customer Experience & Loyalty | 12,000 |
| 10 | Finance | 15,000 |
| 11 | Architecture & Park Design | 18,000 |
| 12 | Franchise Manual | 13,000 |
| 13 | IT, IoT & ERP Systems (RC WORLD OS) | 16,000 |
| 14 | Bootstrap Launch Plan ($10K / 300 m² Micro-Park) | 12,000 |

**Volume 1 — Executive Master Plan.** The whole business in one volume: the miniaturized-industrial-complex thesis, mission and values, the revenue engines and high-utilization business model with worked vehicle-hour economics, the park at a glance, the $2.6 M investment opportunity with staged tranches and use of funds, the three development phases with gating criteria, the headline five-year financials, a top-10 risk summary, and the expansion roadmap. It is the only volume that summarizes every other volume, and the first document any external reader receives.

**Volume 2 — Market Research & Competitive Landscape.** Sizes the global RC industry (cited as ranges per the style guide), profiles the Chinese, Japanese, European, and US ecosystems, and delivers the commissioned special study on Chinese diorama and miniature-equipment manufacturers. It then analyzes the experience economy RC WORLD actually competes in, every adjacent venue format, customer segmentation with a TAM/SAM/SOM model reconciled to Year-1 revenue, and market risks.

**Volume 3 — RC Motorsport Division.** The complete specification for Tracks A (asphalt/drift), B (baja/rally), and C (crawler trail): fleet classes and counts within the 64-car Phase 1 baseline, the standardized-chassis doctrine with lap-time parity within 2–3% and personality-through-tuning, track construction, race formats and championships, timing and telemetry integration, marshaling, maintenance, and the division's KPI dashboard.

**Volume 4 — RC Construction Division.** Build-out and operating specification for the Mining Zone and Agriculture Zone: machine catalogue, the electromechanical-rental versus hydraulic-premium doctrine, fleet-balancing mathematics behind the 1:3 excavator-to-dump-truck ratio, haul-road and pit design (maximum 15° incline), the field grid and implement library, earthmoving competitions, maintenance, and safety.

**Volume 5 — Aviation Division.** The Phase 2 netted airfield: 30 m runway, helipads, high-tensile enclosure engineering, the ~20-aircraft fleet (fixed-wing trainers through FPV), flight-line procedures, instruction programs, airspace and regulatory compliance, and weather doctrine.

**Volume 6 — Marine Division.** The Phase 2 pond complex: pond engineering and water management, the ~24-vessel fleet from scale tugs to fast electrics and sailing one-designs, retrieval systems, event formats, and winterization.

**Volume 7 — Engineering & Workshop Manual.** The Artisans' handbook for The Works: workshop layout and tooling, maintenance schedules and preventive-maintenance matrices, FMEA-driven failure catalogues, rebuild procedures, battery doctrine and charging-bunker operation, RCW Node installation, trade hacks, and complete instruction on building custom RC cars.

**Volume 8 — Procurement Handbook.** The purchasing manual: supplier landscape and vetting, direct-from-China wholesale channels, the full fleet purchasing matrix with cost bands, the high-turnover spares inventory, batteries and chargers, quality-assurance inspection protocols, landed-cost calculation, and reorder automation through RC WORLD OS.

**Volume 9 — Customer Experience & Loyalty.** The customer journey end to end: Toolbox Talk induction, Shift booking and queueing, the tiered **RC WORLD License** driver-progression program, badges and skill mastery, **Gears** loyalty currency, memberships (Apprentice/Operator/Foreman), season passes, parties and corporate events, and service-recovery standards.

**Volume 10 — Finance.** The source of truth for all financial figures: full five-year P&L and cash flow, capex schedules per phase, unit economics, sensitivity and scenario analysis, break-even (operating Month 16–19), funding structure for the $2.6 M ask, investor returns, and local-adaptation methodology.

**Volume 11 — Architecture & Park Design.** The physical park on 4.8 ha (~12 acres): master site plan and CAD-style layout concepts, zone-by-zone civil and landscape specification, buildings (entry pavilion, The Works, charging bunker, restaurant, indoor arena), utilities and drainage, circulation and sightlines, accessibility, and the phased construction sequence.

**Volume 12 — Franchise Manual.** The replication playbook: the franchise package, site-selection criteria, localization of pricing and fleet, fee structure, training and opening support, brand standards, and the multi-site operating model — activated by the Phase 3 franchise pilot.

**Volume 13 — IT, IoT & ERP Systems (RC WORLD OS).** The technology volume: RCW Node hardware (ESP32-C3, Micro-Node and Heavy-Node), kill-switch logic, Wi-Fi mesh, and the full ERP covering finance, HR/payroll, payments, bookings, fleet, live telemetry, POS/retail, F&B, inventory, CRM, events, access control, reporting/BI, and franchise multi-site support — Supabase (PostgreSQL) + Kotlin services, Kotlin Multiplatform / Compose Multiplatform apps on **both Android and iOS**, role-based interfaces for each user class.

**Volume 14 — Bootstrap Launch Plan ($10K / 300 m² Micro-Park).** The self-funded launch that precedes Phase 1, leaving Volumes 1–13 unchanged as the growth-target and investor documentation: an exact $10,000 line-item budget, the 300 m² layout, the all-electromechanical fleet doctrine (no hydraulics — the first hydraulic machine is the first upgrade bought from proceeds), the solo-operator playbook, micro-scale pricing, shoestring marketing, the milestone-gated upgrade ladder climbing from reinvested proceeds to master-plan Phase 1 (Rung 5 = the external raise), and the risk register with explicit stop-loss criteria.

## 6. Glossary of Canonical Terms

| Term | Definition |
|---|---|
| **RC WORLD** | The park brand (all caps in headings; "RC World" acceptable in prose). Successor to internal codename *Omni-Zone*. |
| **Omni-Zone** | Legacy internal project codename from the original blueprint; reference only. |
| **Division** | Top-level operating unit: Motorsport Division; Construction Division (incl. Mining & Agriculture zones); Aviation Division; Marine Division. |
| **The Works** | The central engineering and workshop facility; home base of the Artisans. |
| **Artisan** | Customer-facing title for RC WORLD technicians ("technician" acceptable in technical prose). |
| **Shift** | The billing unit: one 20-minute operating block, decoupled from battery life (~30% buffer returned). |
| **Casual Shift** | One-block session; vehicle returned with buffer intact. Anchor price $15 standard / $22 premium. |
| **Operator Shift** | Two or more blocks with a mandatory Artisan battery-swap pit stop at 20 minutes. $26 / $38. |
| **Top-Up Session** | Instant in-app Shift extension offered at T-5 minutes when no one queues for that class. |
| **RCW Node** | In-house telemetry PCBA (ESP32-C3) between receiver and ESC; monitors voltage and GPS, executes remote kill. **Micro-Node** ~25×25 mm; **Heavy-Node** ~40×30 mm. |
| **RC WORLD OS** | The custom ERP running the entire business — finance, HR/payroll, payments, bookings, fleet, live telemetry, and all other functions — with role-based interfaces per user class. Supabase + Kotlin backend; Kotlin Multiplatform apps on Android and iOS. Volume 13. Deferred at Micro-Park scale. |
| **Toolbox Talk** | The digital induction module completed in-app before first booking; doubles as the signed legal waiver. |
| **RC WORLD License** | The tiered driver-license progression program (levels, badges, equipment endorsements). Volume 9. |
| **Gears** | The loyalty currency: points earned through visits, performance, and milestones. |
| **Tow-Truck Retrieval Protocol** | Breakdown gameplay: customers never walk onto live tracks; they pilot a 1/10 winch-equipped recovery crawler to retrieve their dead vehicle. |
| **Charging bunker** | Fire-isolated cinderblock/sandbag room where all LiPo charging occurs, on multi-port smart balance chargers. |
| **Battery doctrine** | 2S/3S LiPo, XT60 standard (Deans legacy acceptable), 3:1 battery-to-vehicle ratio, 3.4–4.2 V/cell operating window. |
| **1:3 ratio** | Canonical excavator-to-dump-truck fleet ratio in the Mining Zone. |
| **Rental vs premium fleet** | Rental construction machines are electromechanical (lead-screw); hydraulic machines (Kabolite class) are reserved for premium supervised experiences and display. The bootstrap fleet (Volume 14) contains no hydraulics at all. |
| **Micro-Park** | The self-funded bootstrap launch format: 300 m², $10,000 all-in, Construction Division only, electromechanical machines only. Volume 14. |
| **Phase 1 / 2 / 3** | "Core Park" (project Months 0–12); "Full Park" (project Months 13–30); "Destination & Beyond" (project Months 31–60). Build phasing uses *project* months (park opens at project Month 12); financials and division opening schedules use *operating* months (M1 = opening month). |

## 7. Volume Summary & Cross-References

This front matter established the document set, its control and maintenance rules, the reading path for each audience, the master table of contents, and the canonical vocabulary. Begin with **Volume 1** for the business as a whole; founders bootstrapping begin with **Volume 14**, the Micro-Park operating plan. Consult `style-guide.md` whenever a number or name is in question — it, not any individual volume, is the source of canonical facts, with **Volume 10** the source of truth for financial detail and **Volume 13** for the technology stack. The reading paths in Chapter 3 are the fastest route to any specific answer.
