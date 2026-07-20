# RC WORLD — Source Material Digest

This file distills the three original planning PDFs and the founder's brief. Every volume of the
Master Development Plan must remain consistent with the decisions recorded here. Where a volume
extends or supersedes a decision, it must say so explicitly.

---

## Source 1 — "Omni-Zone RC Play Park: Master Business Strategy & Technical Engineering Blueprint" (v2.0)

### Concept
- Large-scale, multi-zone remote-controlled (RC) vehicle park operating as a **miniaturized
  industrial complex**, not a hobby sandbox.
- Immersive experiences across civil construction, commercial agriculture, high-speed racing,
  and aviation.
- Core thesis: **high utilization of commercial-grade, modifiable RC equipment**, achieved through
  direct wholesale sourcing, proprietary in-house telemetry hardware, an automated Kotlin/Supabase
  ERP, and gamified customer mechanics.

### Operational zones
1. **Heavy Civil & Mining Site** — simulated open-pit operation; varying aggregate grades (loose
   sand to 10 mm crushed stone); deep excavation pits; graded haul roads with **maximum
   15-degree incline** (prevents continuous motor burnout); central processing hopper.
   Customers operate 1/14 excavators loading articulated dump trucks that haul to the hopper.
2. **Commercial Agricultural Zone** — grid-based farm simulation (commercial tobacco/maize
   model); pre-tilled fields with crop rows, irrigation trenches, central barn/silo; tractors
   perform plowing, discing, hauling with tandem trailers.
3. **Speed & Off-Road Hub** — three tracks:
   - Track A (Asphalt/Drift): polished concrete or fine asphalt for 1/14 & 1/10 drift + touring.
   - Track B (Baja/Rally): packed dirt, controlled jumps and berms, 4WD buggies + short-course.
   - Track C (Crawler Trail): technical rock-crawling, natural stone, wooden bridges, water hazards.
4. **The Airfield** — 30 m paved runway, elevated helipads, fully enclosed in high-tensile
   netting for flyaway prevention and spectator safety.

### Fleet doctrine
- Prioritize **electromechanical durability and rapid artisan repair** over premium leak-prone
  hydraulic systems (for the rental fleet).
- 1/14 and 1/16 scales for earthmoving (best payload-to-cost balance).
- **Critical logistics ratio — Excavator : Dump Truck = 1 : 3** (excavators have high stationary
  time; three circulating dump trucks per active excavator prevents bottlenecks).
- Primary fleet matrix (wholesale, direct-from-China):

| Zone / Category | Model | Scale | Est. wholesale cost | Notes |
|---|---|---|---|---|
| Mining: Excavator | Huina 1580 (V4) | 1/14 | $350–420 | Full metal, lead-screw driven booms, no fluid leaks |
| Mining: Dump truck | Huina 1582 / 1573 | 1/14 | $150–200 | Metal bed, high payload, scaled to receive 1580 loads |
| Mining: Wheel loader | Huina 1583 | 1/14 | $180–220 | Metal construction, hopper loading, haul-road smoothing |
| Agriculture: Tractor | Double E E351 / Siku | 1/16 | $80–120 | High-torque 4WD, standard hitch for modular implements |
| Racing: Buggy | WLtoys 144001 / 144010 | 1/14 | $60–90 | Brushless options, metal chassis, ~60 km/h, cheap parts |
| Crawler: Trail | MN99S / WPL C24 | 1/12 | $45–60 | Metal gear upgrades, unbeatable value |

### Battery doctrine
- Standardize on **2S (7.4 V) and 3S (11.1 V) LiPo** with **XT60 or Deans T-plug**; no
  proprietary casings.
- **3:1 battery-to-vehicle ratio** (one in vehicle, one charging, one rested/ready).
- Safe operating window **3.4 V – 4.2 V per cell**; over-discharge destroys cells; charging is a
  fire risk.
- Industrial multi-port smart balance chargers (SkyRC T1000 / ISDT K4 class) in a **fire-proof
  cinderblock/sandbag bunker**.

### High-turnover spares (permanent inventory)
- Transmission/drive: brass pinions, spur gears (metal + nylon), CVD driveshafts — HIGH turnover.
- Suspension/steering: A-arms, steering knuckles, shock shafts, 15 kg/25 kg digital servos — HIGH.
- Electromechanical: brushed 540/550 motors, brushless ESCs, micro-switches for boom limits — MEDIUM.
- Consumables: tires (knobby + drift slicks), excavator track pins, Loctite blue, lithium grease — CONTINUOUS.

### Customer experience & monetization mechanics
- **Digital induction ("Toolbox Talk")** in the Android app before booking — interactive module on
  battery limits, collision liability, track rules; doubles as signed legal waiver.
- **"Industrial Shift" pricing** — billing decoupled from max battery life; standard billable unit
  = **20-minute block**. Casual Shift (1 block) returns vehicle with ~30% buffer; Operator Shift
  (2+ blocks) forces pit stop at 20 min for an artisan battery swap ("refueling" immersion).
- **F1-style power management & penalties** — telemetry reads voltage sag in real time; aggressive
  throttle use drains allocation faster; software can trigger remote kill-switch; smooth drivers win.
- **Live queue management & top-ups** — at T-5 minutes the app queries the Supabase `queue_roster`;
  if nobody waits for that class, a "Top-Up Session" button appears for instant wallet extension.
- **Breakdown & Tow-Truck Retrieval Protocol** — dead vehicle triggers a localized 85 dB buzzer;
  customers may NOT walk onto active fields; they hand in their transmitter and receive controls
  for a **1/10 RC recovery crawler with functional electric winch**; they pilot the tow truck to
  retrieve their dead vehicle (friction point converted into gameplay); fresh vehicle then issued.

### Telemetry hardware (custom PCBA)
- **ESP32-C3** node sits inline between RC receiver and ESC; monitors battery voltage, GPS
  location; executes remote kill commands.
- Unified schematic, two footprints, fabricated in China (JLCPCB class):
  - **Form Factor A "Micro-Node"** (racing buggies): ~25×25 mm, direct solder pads (vibration),
    silicone strain relief.
  - **Form Factor B "Heavy-Node"** (mining/construction): ~40×30 mm, JST XH (2.5 mm) positive-latch
    connectors for field service; battery leads soldered.
- BOM highlights: ESP32-C3-MINI-1 (or SuperMini ~$3), ATGM336H GPS (BDS/GPS dual, ~$4.50),
  voltage divider 10 kΩ/2.2 kΩ, TPS54202 buck (or LM2596 ~$1) 7.4/11.1 V → 3.3 V.
- **Mandatory conformal coating** (acrylic or epoxy spray) on finished PCBA for moisture/dust.
- Unit cost target **< $15 per node**.
- Node powered downstream of the vehicle's main switch — no parasitic drain overnight.

### ERP / software architecture
- **Kotlin + Jetpack Compose native Android app**; single codebase, modularized
  Admin/Mechanic vs Customer features.
- **Supabase (PostgreSQL)** backend; Row Level Security separates admin/user views; Supabase
  Realtime for live tracking; Mapbox/Google Maps SDK for live vehicle map.
- Schema: `fleet_inventory` (id, mac_address, asset_tag, model_id, status ENUM
  active/maintenance/charging, total_hours_run), `live_telemetry` (high-frequency inserts: lat,
  lng, voltage, speed, timestamp), `maintenance_logs` (vehicle_id, mechanic_id, parts_used JSONB,
  description, date_resolved).
- Customer app: digital wallet, QR-scan on transmitter to bind vehicle, live battery/session
  dashboard, geofenced lap timers, global leaderboard.
- Admin app: real-time grid map; automated voltage alerts (<3.4 V/cell → push notification,
  remote throttle to 20%, order back to pit); predictive maintenance from logged runtime hours
  (gear greasing, motor commutator inspection flags).
- **Wi-Fi mesh** (TP-Link Omada class outdoor mesh) blankets park; ESP32 2.4 GHz nodes hand off
  between APs without dropping telemetry.
- **Kill-switch logic**: PWM intercept between receiver and ESC; KILL command over Supabase
  Realtime on under-voltage (<3.4 V/cell) or GPS geofence breach → ESC forced to neutral/brake.

---

## Source 2 — "RC Racing Experience Park — Business Strategy and Plan"

- **Vision**: premium RC motorsport experience where customers choose cars with distinct driving
  personalities while races are decided primarily by **driver skill**.
- **Fleet strategy**: one or two standardized **1/10 hobby-grade chassis platforms** with common
  electronics and batteries. Differentiate through tuning (ESC profiles, gearing, suspension,
  weight distribution, AWD/RWD) rather than different hardware.
- **Recommended suppliers**: MST (premium drift chassis), RGT Racing (value touring/crawlers),
  MJX Hyper Go (performance/value), LDRC (entry scale), Double Eagle (licensed scale), Killerbody
  & Pandora RC (body shells), Hobbywing (ESCs), Surpass Hobby (motors), Gens Ace & CNHL (LiPo).
- **Best practices**: standardize components, spare-parts inventory, daily inspections, battery
  rotation, repair logs, identical tires within each class, technician rebuild training.
- **Common failure points**: tires, body mounts, suspension arms, steering links, wheel bearings,
  gears after impacts, driveshafts, shock seals, ESC cooling, connectors, LiPo damage.
- **Critical spares**: control arms, hubs, shock shafts/seals, springs, silicone oils, gears,
  differentials, bearings, wheel hexes, driveshafts, body posts, motors, ESCs, servos, batteries,
  chargers, tires, wheels, screws/fasteners.
- **Tuning strategy**: keep lap times within **2–3% across the fleet**; create personalities with
  small ESC changes, spring rates, shock oil, ballast, gearing, differential settings.
- **Revenue ideas**: timed races, championships, memberships, corporate events, birthday parties,
  driver rankings, coaching, night racing, drift competitions, retail shop, repair service, F&B.
- **Customer experience**: professional timing system, digital leaderboards, themed vehicle
  classes, realistic pit lane, driver briefing, safety marshals, telemetry displays, seasonal events.
- **Implementation**: begin with **20–30 cars**, standardized maintenance, documented setup
  sheets, preventive servicing every fixed number of battery cycles, continuous failure-data
  collection.

---

## Founder's brief (this commission)

- Title: **RC WORLD — Master Development Plan. Investor Prospectus • Operations Manual •
  Engineering Handbook.**
- ~12 volumes, 350–500 pages total, book-quality, modular, living document.
- Must include: engineering calculations, fleet balancing methodology, maintenance schedules,
  SOPs, checklists, purchasing manuals, staff manuals, workshop manuals, CAD-style layout
  concepts, risk registers, FMEA analyses, preventive maintenance matrices, KPI dashboards,
  operating procedures, emergency procedures, marketing strategy, sponsorship strategy,
  five-year growth roadmap.
- Volume 2 must additionally research **Chinese diorama suppliers and manufacturers, including
  makers of miniature equipment replicating real work environments**.
- Volume 7 must include detailed instructions, tutorials, best-practice behaviours and skills,
  RC trade hacks, and notes on **how to build custom RC cars**.
- Volume 9 must specify a **tiered reward system**: levels based on performance and repeat
  visits; badges for mastering skills or specific equipment; driver licenses; season passes.
- End uses: investor presentations, financing applications, architect/contractor guidance,
  employee training, day-to-day operations, future franchising.
- **Volume 13 (added by founder)** — IT & IoT volume detailing how the ERP application (RC WORLD
  OS) manages ALL sectors of the business: finance, HR and payroll, online payments, fleet
  management, bookings, live telemetry, plus every other function the business needs (POS/retail,
  F&B, inventory/procurement, CRM/marketing, events, access control, CCTV/safety, reporting/BI,
  franchise multi-site support). Must detail how to develop the ERP with **different interfaces
  for different users based on access level** (role-based access control: executive, finance,
  HR, operations manager, artisan/technician, marshal, front-of-house, franchisee, customer).
  **Client apps must be supported on both Android and iOS.**

---

## Established naming and canon (use consistently across volumes)

- Park brand: **RC WORLD** (working title; the original concept name "Omni-Zone RC Play Park"
  may be referenced as the project's internal codename).
- Divisions: Motorsport, Construction (incl. Mining & Agriculture), Aviation, Marine,
  Engineering & Workshop ("The Works"), plus commercial functions.
- Staff roles: technicians are called **Artisans** in customer-facing contexts.
- Billing unit: the 20-minute **Shift**.
- Telemetry node: **RCW Node** (Micro-Node and Heavy-Node form factors).
- ERP/app platform: **RC WORLD OS** (Kotlin/Jetpack Compose + Supabase).
- Currency: USD throughout. Baseline financial model assumes a mid-size international city;
  local adaptation handled in Volume 10 sensitivity analysis and Volume 12 franchise localization.

## Research anchors already verified (July 2026)

- Global RC car market estimates range **$1.5 B – $6.2 B (2025)** depending on scope, growing
  5.8–7.5% CAGR; hobby radio control (all categories) ≈ **$3.2–7.0 B**, 6–7.5% CAGR; toy-grade
  segment declining in share, hobby-grade rising. Cite ranges, not single figures.
- Kabolite (premium hydraulic sub-brand of Huina, Shantou, Guangdong): K970 1/14 full-hydraulic
  excavator ≈ **$10,500–12,500 retail, 31 kg, brushless + 18-ch radio**; K350 ≈ $4,500–5,000;
  K961/K963 ≈ $1,750–1,900; K5701 dump ≈ $670. Use as the premium tier vs Huina 15xx rental tier.
