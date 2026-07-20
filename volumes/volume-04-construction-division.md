# Volume 4 — RC Construction Division

**RC WORLD — Master Development Plan** · Volume 4 of 12
**Revision:** 1.0 · **Date:** July 2026 · **Status:** Living document — bump revision on material change

**Purpose of this volume.** This volume is the complete build-out and operating specification for the RC WORLD Construction Division: the Mining Zone and Agriculture Zone that open with Phase 1 (Months 0–12) as one of the park's two anchor attractions. It defines the division concept, the full machine catalogue with fleet counts and duty ratings, the engineering doctrine that splits the fleet into electromechanical rental machines and hydraulic premium machines, the fleet-balancing mathematics behind the 1:3 excavator-to-dump-truck ratio, the physical design of the open-pit mining circuit and the agricultural field grid, the competition and gamification layer that converts earthmoving into repeatable revenue, and the maintenance and safety programs that keep thirty earthmovers and twelve tractors in daily service. It is written to be handed, chapter by chapter, to the people who will build and run the division: the civil contractor gets Chapter 6, the Artisans get Chapters 3, 4 and 10, the events team gets Chapter 8, and the investor gets all of it.

**Intended readers.** Investors and lenders assessing Phase 1; the General Manager and Construction Division Lead; Artisans assigned to the heavy fleet; the civil/landscape contractor building the Mining and Agriculture zones (with Volume 11); the events and marketing team designing competition formats (with Volume 9).

**Chapters**

1. Division Concept: The Miniaturized Industrial Complex
2. Machine Catalogue & Fleet Specification
3. Hydraulic Systems Engineering (Premium Fleet)
4. Electromechanical Lead-Screw Machines (Rental Fleet)
5. Fleet Planning, Utilization Mathematics & Battery Logistics
6. Mining Zone: Site & Circuit Design
7. Agriculture Zone: Field Grid & Tractor Operations
8. Earthmoving Competitions & Events
9. Gamification & Telemetry Interface
10. Maintenance Program
11. Safety
12. KPIs & Division Dashboard
13. Volume Summary & Cross-References

---

## 1. Division Concept: The Miniaturized Industrial Complex

### 1.1 Not a sandbox — a working mine at 1/14 scale

The Construction Division is the clearest expression of the founding thesis recorded in the original Omni-Zone blueprint: RC WORLD is a **miniaturized industrial complex, not a hobby sandbox**. A sandbox gives a customer an excavator and a pile of sand and leaves the rest to imagination. RC WORLD gives the customer a *job*. The Mining Zone is a simulated open-pit operation with a production circuit that actually functions: excavators loading at the pit face, articulated dump trucks hauling on engineered roads with a maximum 15° incline, a central processing hopper that weighs and swallows every load, a wheel loader keeping the haul roads dressed, and a live tonnage leaderboard that turns twenty minutes of digging into a measurable shift of production. The Agriculture Zone applies the same logic to farming: pre-tilled fields, crop rows, implements that hitch and unhitch, and seasonal harvest campaigns with their own scoring.

The difference matters commercially, not just aesthetically. A sandbox experience exhausts itself in one visit; a production system generates goals, and goals generate return visits. A customer who has moved 38 kg of aggregate in their first Shift knows exactly what they want to do next time: move 50.

### 1.2 Why construction RC is the signature differentiator

Motorsport is the park's volume engine (Volume 3), but the Construction Division is its **signature** — the thing competitors cannot easily copy and customers cannot experience anywhere else. Four structural reasons:

1. **Almost no competition.** RC racing tracks exist in most large cities in some form — club tracks, indoor carpet ovals, hobby-shop lots. Public-access RC *earthmoving* operations are close to nonexistent worldwide. A handful of hobby clubs run private construction dioramas; virtually nobody rents a working 1/14 excavator to a walk-in customer. In competitive-landscape terms (Volume 2), the Mining Zone opens with an effectively empty field.
2. **High dwell time and low skill floor.** An excavator is the rare machine that is *more* satisfying when operated slowly. A first-timer is productive within two minutes — swing, curl, dump — and the skill ceiling (smooth multi-channel blending, precise bucket placement, clean truck loading without spillage) is high enough to hold hobbyists for years. Session-length data from hobby operators and our own pilot testing consistently show construction operators using their full 20-minute Shift, while racing customers often burn out (or crash out) earlier. Longer dwell means more F&B capture, more spectating, more Top-Up Sessions.
3. **The widest demographic of any division.** Racing skews young and male. Earthmoving draws three distinct audiences at once: families with children who recognize excavators before they can read; adult hobbyists and trades-adjacent enthusiasts (operators, builders, farmers) for whom the machines are professionally familiar; and corporate groups, because "run a mine together for two hours" is a genuinely novel team event (Chapter 8.5). The division is also the park's most weather-tolerant and most photogenic — a loaded 1/14 dump truck climbing a haul road at golden hour is the park's single best marketing image.
4. **It monetizes patience, not adrenaline.** Because billing is the 20-minute Shift decoupled from battery life, and because construction machines draw far less current than racing machines, the Construction Division has the best battery economics and the lowest crash-damage rate per Shift in the park. Revenue per machine is comparable to Motorsport; maintenance cost per Shift is materially lower (Chapter 10).

> **Investor Note.** The division's Phase 1 fleet capex is small — roughly $9,000–11,000 wholesale for all thirty earthmovers and twelve tractors *excluding* the single premium hydraulic showcase machine, which alone costs as much as the rest of the fleet combined (Chapter 2). The expensive parts of this division are civil works and the hopper/telemetry infrastructure, which last a decade. The machines customers actually wear out are cheap, repairable, and stocked three-deep in spares.

### 1.3 The two zones and the operating doctrine

The division comprises two adjacent zones built in Phase 1:

- **Mining Zone** (~2,400 m²): open-pit dig faces, graded haul-road loop, central processing hopper, operator stations on the rim. Fleet: 6 excavators, 18 dump trucks, 3 wheel loaders, 2 dozers, 1 premium hydraulic showcase machine — 30 assets (canonical fleet, Volume 1).
- **Agriculture Zone** (~1,500 m²): field grid with crop-row simulation, irrigation trenches, barn/silo receiving point. Fleet: 12 tractors (Double E E351 class, 1/16) plus a shared implement library.

Two doctrine points from the style-guide canon govern everything in this volume and must never be contradicted:

- **Excavator : dump truck = 1 : 3.** An excavator is a stationary loading plant; a dump truck is a circulating hauler. Three circulating trucks keep one excavator continuously loading without queue collapse (the full queueing argument is Chapter 5.1).
- **The rental fleet is electromechanical (lead-screw), not hydraulic.** Hydraulic machines — the Kabolite class — are reserved for premium supervised experiences and display. This is the division's single most important engineering decision, and Chapters 3 and 4 exist to justify and operationalize it.

### 1.4 The customer journey through the division

A Casual Shift in the Mining Zone, end to end: the customer books in RC WORLD OS and completes the Toolbox Talk induction (once, digitally, before first visit — Volume 9). At the zone gate an Artisan scans the booking QR, issues a transmitter bound to a specific machine, and walks the customer to a numbered operator station on the pit rim. The machine is already positioned — excavator at a dig face, or dump truck staged in the loading queue. The 20-minute Shift clock starts at first stick input. Telemetry (Heavy-Node, Chapter 9) streams voltage and position; the tonnage system credits every hopper delivery to the customer's account. At T-5 minutes the app offers a Top-Up if no one is queued. At Shift end the machine parks itself under Artisan direction, the customer sees their production stats — tonnage, loads, spillage penalty, license progress — and the machine turns around for the next customer with ~30% battery buffer remaining, per the billing doctrine. If a machine dies mid-Shift, the customer does not walk onto the pit floor; the **Tow-Truck Retrieval Protocol** converts the breakdown into gameplay (Chapter 9.4).

---

## 2. Machine Catalogue & Fleet Specification

### 2.1 How to read this catalogue

Every machine class below is specified with: the selected model and the reasoning; verified 2026 specs; wholesale (direct-from-factory, Shantou/Guangdong supply chain — Volume 8 carries supplier detail) versus Western retail pricing, because the gap is itself a business insight; and an **RCW duty rating**:

| Duty rating | Meaning |
|---|---|
| **RD-1** | Rental, unrestricted — issued to any inducted customer, continuous daily duty |
| **RD-2** | Rental, gated — requires a license tier (Volume 9) or staff spot-check before issue |
| **PD** | Premium/display — supervised sessions only, Artisan present, premium pricing |
| **SD** | Service/staff — never issued to customers (grooming, recovery, utility) |

Scale doctrine: **1/14 for earthmoving, 1/16 for tractors and light dozers**. 1/14 is where the Chinese construction-model industry concentrates its engineering (Huina, Kabolite, LESU, JDModel all anchor on 1/14), which means the deepest spare-parts pools, the widest attachment ecosystems, and the best payload-to-cost ratio. Going larger (1/8, 1/10 hydraulics) doubles cost for little experiential gain; going smaller (1/24) collapses payload and durability.

### 2.2 Excavators — the rental workhorse: Huina 1580 V4

The **Huina 1580 (V4, 2025/2026 production)** is the canonical rental excavator, and it is worth recording why it wins the seat. It is the only machine in its price band that is *genuinely all-metal* — tracks, undercarriage, slew deck, boom, stick and bucket are alloy castings and pressings — while remaining **entirely electromechanical**: every boom, stick and bucket motion is driven by a motor-and-lead-screw actuator, not fluid. Verified 2026-market specs:

| Parameter | Huina 1580 V4 |
|---|---|
| Scale / configuration | 1/14 crawler excavator, 360° continuous slew (slip-ring equipped) |
| Channels | 23 (independent proportional tracks, boom, stick, bucket, slew, lights, sound, smoke) |
| Dimensions | ~700 mm reach length × 180 mm width × 480 mm max boom height |
| Weight | ~7–8 kg |
| Battery | 2S 7.4 V 2,000 mAh (park fleet: XT60-converted, 3:1 pool) |
| Stock runtime | ~40 min per charge (comfortably covers one 20-min Shift + 30% buffer) |
| Attachments | Standard bucket; factory grapple and jackhammer in the case (park: bucket only for rentals; attachments reserved for events) |
| Wholesale (direct) | **$350–420** |
| Western retail (2026) | $560–800 |
| Duty rating | **RD-1** — this is the machine the division is built around |

Fleet count: **6** (fleet canon). Two are positioned at dig faces at any time in normal operations, three in rotation/charge/maintenance, one as event/competition reserve — the deployment logic is Chapter 5.

> **Field Note.** The V4's LCD transmitter includes a password lock and a play-timer. We disable both — Shift timing lives in RC WORLD OS, not in the transmitter — but the 23-channel layout is kept factory-standard across all six units so that any transmitter can bind to any excavator after an Artisan swap. Never let transmitter configs drift per-machine; config drift is how a fleet quietly becomes six unique machines.

### 2.3 The premium showcase: Kabolite hydraulic class

**Kabolite** is Huina's premium hydraulic marque (same Shantou industrial group, entirely different engineering tier). The 2026 lineup, verified July 2026, spans:

| Model | Type | Scale | Weight | Street/retail (2026) | Notes |
|---|---|---|---|---|---|
| K336GC | Hydraulic excavator (CAT 336 GC replica) | 1/16 | ~9.2 kg | ~$1,700–1,900 | Entry hydraulic; 24-ch; 7.4 V 10,000 mAh; the "first real hydraulic" upgrade path |
| K961 / K963 | Hydraulic excavator / loader | 1/16 | ~8–10 kg | ~$1,750–1,900 | Canon reference tier (digest); K963-100 loader variant new for 2026 |
| K350 (-200, 3-arm) | Hydraulic excavator | 1/14 | ~18–19 kg | $4,500–5,000 retail; direct-dealer pricing seen as low as ~$3,850 in mid-2026 | Flysky PL18 EV Lite radio, sound/light, 10,000 mAh |
| K980 | Hydraulic excavator (SY980H replica) | 1/14 | ~20 kg | ~$4,600–5,000 | 2026 addition to the lineup |
| K988-100S | Hydraulic wheel loader (988K replica) | 1/14 | ~23.5 kg | ~$3,800–5,000 | 3S power, 15–25 kg lift force, 6-ch valve block |
| **K970 (-100 / -100S / -100S Pro)** | Flagship hydraulic excavator | 1/14 | **31 kg** | **$10,500–12,500 retail** (canon); direct/dealer channels observed $6,500–9,000 for base/100S trims in 2026 | Brushless drive + brushless pump, 18-ch Flysky Paladin touch-screen radio, ~3.5 MPa system with cab pressure gauge, 80 kg track thrust, quick-coupler on 100S |
| K5701 | Hydraulic dump truck | 1/14 | ~8 kg | ~$670 | Companion hauler for hydraulic demos |

The park's Phase 1 premium showcase machine is **one K970-class excavator** (fleet canon: "1 premium hydraulic showcase machine, Kabolite class"). It exists for three reasons: it is the **premium supervised experience** ($22 Casual / $38 Operator Shift, always Artisan-supervised, license-gated — Chapter 5.4); it is the **display anchor** that makes the whole division legible ("that's what the real hydraulics feel like"); and it is the **aspirational top rung** of the license ladder — customers grind tonnage on the 1580 fleet partly to earn K970 seat time. A second premium machine (K988-100S loader or K350) is the division's first Phase 2 fleet addition if premium-session occupancy sustains above 70% (Chapter 12).

For completeness of the competitive map: **LESU** (Aoue) builds 1/14 hydraulic excavators from roughly $2,000 (compact PC30-class) to $7,000+ (LR960-class), plus hydraulic backhoe loaders (BL71 2-in-1, ~$3,600), skid-steers and specialty loaders; **JDModel** occupies similar territory with hydraulic excavators and wheel loaders in the $2,500–6,000 band. Both are credible alternate sources for the premium tier and for hydraulic spares (pumps, valves, cylinders), and Volume 8 carries them as second-source suppliers. For the *rental* tier, nothing in the LESU/JDModel catalogues competes with Huina 15xx economics — which is precisely the point of the two-tier doctrine.

### 2.4 Dump trucks — the circulation fleet: Huina 1582 / 1573

Eighteen trucks — the largest single machine population in the park — sized by the 1:3 ratio against six excavators. Two models share the pool deliberately:

| Parameter | Huina 1582 | Huina 1573 |
|---|---|---|
| Scale / layout | 1/14, Arocs-pattern rigid dump truck | 1/14 rigid dump truck (previous generation) |
| Construction | Metal cab, metal tipping bed, metal linkage | Metal bed, more ABS in cab/chassis |
| Channels | 10 (drive, steer, tip, lights, sound) | 10 |
| Payload (rated) | ~4 kg per load | ~3 kg per load |
| Dimensions | 450 × 150 × 190 mm | similar footprint |
| Weight | ~3.6 kg | ~3.2 kg |
| Battery | 7.4 V Li-ion/LiPo (park: XT60 pool) | 7.4 V |
| Stock runtime | ~45 min | ~30 min |
| Wholesale | **$150–200** (canon range covers both) | $120–160 within canon band |
| Duty rating | RD-1 | RD-1 |

Fleet split: **12 × 1582 + 6 × 1573**. The 1573s are the "training haulers" issued to younger children and absorb the roughest treatment; the 1582s are the production fleet whose bed geometry is correctly scaled to receive a Huina 1580 bucket without spillage — the founder's notes flag this load-match explicitly, and it is real: a 1580 bucket pass drops cleanly between the 1582's bed rails with ~15 mm clearance each side, which is what makes clean loading a learnable skill rather than a lottery.

### 2.5 Wheel loaders — Huina 1583

| Parameter | Huina 1583 (2026 model) |
|---|---|
| Scale / layout | 1/14 articulated wheel loader, die-cast metal body |
| Channels | 10; proportional bucket; 40 m range |
| Capability | Carries up to ~10 kg over the front axle; pushes ~1.5 kg; 570 mm long, ~8 kg |
| Battery / runtime | 7.4 V 2,000 mAh, ~40–45 min |
| Wholesale | **$180–220** |
| Duty rating | RD-2 (rental, license-gated) **and** SD (one unit reserved as the grooming machine) |

Fleet count: **3**. Two rentable, one permanently assigned to haul-road dressing and hopper-apron cleanup (Chapter 6.8). The loader is gated behind the second license tier because an articulated machine with a 10 kg carry capability can genuinely hurt a finger — it is the strongest machine in the rental pool.

### 2.6 Dozers — Huina 1554/1569 class

The dozer class is deliberately light. The **Huina 1554** (1/16, ~350 mm, 11 functions, functional blade and rear ripper, ~30–40 min runtime, wholesale $45–70, retail $60–110) and its heavier sibling the **1569** (1/16, 8-ch, scarifier-equipped) are ABS-bodied machines: cheap, charming, and expendable. Fleet count: **2**, duty rating RD-1, issued mostly to children as the entry machine of the whole division. Park units receive an Artisan-fitted aluminum blade wear-edge and metal-gear service pack on first refurbishment (Chapter 4.4). The dozer's operational job is real but modest: back-blading spill drifts in designated push boxes — it is a *toy that does a job*, and it converts four-year-olds into future excavator customers.

### 2.7 Graders and specialty machines — the honest gap

As of July 2026 **no mass-market grader exists in the Huina rental class**; motor graders in 1/14 are boutique hydraulic builds (LESU/JDModel custom territory, typically $3,000–5,000 landed). The division therefore does not carry a rentable grader. Haul-road grading is performed by the SD-assigned 1583 wheel loader with a straight-blade attachment fabricated in The Works (drawing in Volume 7), which does the job for $40 of aluminum. A display-grade hydraulic motor grader is on the Phase 2 wish list as a second premium machine *only if* the K970 premium program saturates first — the grader is a want, not a need, and this volume says so plainly.

### 2.8 Mining fleet composition — master table

| Class | Model | Scale | Drive type | Count | Wholesale each | Fleet wholesale | Duty |
|---|---|---|---|---|---|---|---|
| Excavator | Huina 1580 V4 | 1/14 | Electromechanical (lead-screw) | 6 | $350–420 | ~$2,300 | RD-1 |
| Dump truck | Huina 1582 | 1/14 | Electromechanical | 12 | $150–200 | ~$2,100 | RD-1 |
| Dump truck | Huina 1573 | 1/14 | Electromechanical | 6 | $120–160 | ~$850 | RD-1 |
| Wheel loader | Huina 1583 | 1/14 | Electromechanical | 3 | $180–220 | ~$600 | RD-2 / SD |
| Dozer | Huina 1554/1569 class | 1/16 | Electromechanical | 2 | $45–90 | ~$150 | RD-1 |
| Premium showcase | Kabolite K970 class | 1/14 | **Hydraulic** (brushless pump) | 1 | $6,500–9,000 direct ($10.5–12.5k retail) | ~$8,000 | PD |
| **Mining subtotal** | | | | **30** | | **~$14,000** | |
| Tractor | Double E E351 class | 1/16 | Electromechanical | 12 | $80–120 | ~$1,200 | RD-1 |
| Implements | Plows, discs, trailers (Ch. 7.3) | 1/16 | Towed/PTO-less | ~20 pcs | $15–60 | ~$700 | — |
| **Division total** | | | | **42 powered** | | **~$15,900** | |

Spares provisioning on top of this table — one full "ghost machine" of high-turnover parts per six fleet units — is specified in Chapter 10.6 and priced in Volume 8.

> **Investor Note.** Read the table twice: the single hydraulic showcase machine costs more than the other 29 mining machines combined. That asymmetry *is* the rental doctrine, expressed in dollars. The Kabolite earns premium fees under supervision; the Huina fleet earns volume fees unsupervised and gets rebuilt for $30 in parts when a lead-screw wears. Reversing this — renting hydraulics to walk-ins — is how an operator turns a $14,000 fleet line into a $90,000 one with worse uptime.

---

## 3. Hydraulic Systems Engineering (Premium Fleet)

This chapter is the Artisan's grounding in how miniature hydraulics actually work, why they are magnificent, and why they are quarantined to the premium tier. Even though only one Phase 1 machine is hydraulic, every heavy-fleet Artisan must understand the system: the K970 is the division's most expensive asset, its most fragile revenue line, and the machine most likely to be examined closely by exactly the customers whose opinion travels furthest.

### 3.1 Anatomy of a 1/14 hydraulic system

A scale hydraulic machine is a real hydraulic machine with the decimal point moved. The K970-class circuit contains every element of a full-size excavator's:

1. **Reservoir (tank).** 150–400 ml of hydraulic oil in the counterweight area, with a filler, a sight window for level checks (the K970 has one), and a coarse suction filter. Miniature tanks are proportionally *smaller* relative to flow than full-size tanks, which means the oil works harder and runs hotter per liter — the root cause of half the maintenance schedule below.
2. **Pump.** A miniature **gear pump** — two hardened steel gears meshing inside a machined stainless housing — driven by a **brushless motor** with its own ESC. Gear pumps dominate the scale world because they are simple, flat-efficiency-curve devices that tolerate dirt better than piston pumps. Representative spec (LESU Y-1528 class, verified 2026): rated to 10 MPa, flow ~400 ml/min, relief valve mandatory above ~5 MPa. The pump motor is the "engine": the operator hears it load up under digging effort, which is a large part of the sensory magic.
3. **Relief valve.** Spring-loaded bypass that caps system pressure. This is the component that decides whether a stalled cylinder is "realistic engine lug" or "burst hose." It is set at commissioning and lock-witnessed (SOP-CD-003 sets the check).
4. **Directional valve block.** A bank of miniature spool valves — one spool per function (boom, stick, bucket, auxiliary/quick-coupler) — each spool shifted by a micro servo. The K970 runs a six-way block; aftermarket blocks run 2–8 ways. Proportionality comes from spool position: the servo meters flow, so stick-input finesse translates directly into cylinder speed. This servo-on-spool architecture is why hydraulic machines *feel* alive: flow, not position, is being commanded.
5. **Cylinders.** Honed-tube rams with piston seals (typically NBR O-rings + PTFE backup) and rod wipers. Bore sizes in 1/14 run 8–16 mm; a 12 mm bore at 20 bar develops ~23 kgf of rod force — which is how a 31 kg model excavator genuinely digs compacted ground.
6. **Hose and hard line.** Nylon or polyurethane tube (3–4 mm OD) with brass compression or push-fit fittings; premium builds run scale-appearance braided hose on the boom.
7. **Gauge.** The K970 carries a factory pressure gauge behind a service door — the single most useful diagnostic instrument on the machine, and the anchor of the weekly health check.

### 3.2 Operating pressures, flow, and what they mean

Typical 1/14 systems idle at low pressure and work between roughly **8 and 30 bar (0.8–3.0 MPa)**, with flagship systems like the K970 running up to ~35 bar (the factory gauge is scaled to 3.5 MPa); component ratings (pump housings, hose) carry headroom to ~100 bar (10 MPa) but relief valves keep working pressure far below that. For intuition: 20 bar is about ten times road-bicycle tire pressure, delivered through hoses the diameter of spaghetti. Two design consequences:

- **Heat is the enemy, not pressure.** At these pressures nothing bursts if the relief valve is healthy; instead, sustained relief-valve bypass (operator holding a function against its stop) converts the entire pump power into oil heat. A 40-minute premium session of enthusiastic digging can raise tank temperature 20–25 °C above ambient. Above ~60 °C oil viscosity collapses, internal leakage rises, seals age fast. The premium-session supervision script therefore includes teaching the customer to *feather off* at end-of-stroke — a genuine operator skill that also protects the machine.
- **Cleanliness is everything.** The pump gears run micron-scale clearances. One grain of the Mining Zone's own 0–2 mm sand inside the circuit will score the pump in minutes. This is the engineering core of the premium doctrine: the K970 works on the *same dirt* the rental fleet works, but with an Artisan present whose job is partly to keep the filler cap, quick-coupler and rod wipers clean.

### 3.3 Oil selection

Scale hydraulic OEMs and the practitioner consensus (verified 2026) standardize on **ISO VG 32 anti-wear hydraulic oil** (Mobil DTE 25 class or equivalent) as the default: low enough viscosity for miniature gear pumps to prime instantly, high enough for film strength at 30 bar. Operators in sustained hot climates (tank temps >55 °C) step to **ISO VG 46**. Absolute prohibitions, posted on the workshop wall: **never** brake fluid (glycol chemistry swells NBR seals), **never** motor oil (detergent additives foam and corrode), **never** silicone shock oil (wrong lubricity, wrecks pump gears). RC WORLD stocks ISO VG 32 in 1 L bottles, dyed with a trace of red tracer dye so that any leak on the machine or the pit floor is instantly attributable (a Trade Hack borrowed from full-size fleet maintenance).

> **Trade Hack.** Keep a white ceramic tile in the K970's parking bay. The machine parks over it every night. Any red-tinged drop on the tile at morning inspection localizes a developing leak *before* the reservoir level moves — sight-glass level is a lagging indicator; the tile is a leading one.

### 3.4 Leak management

Every hydraulic machine leaks eventually; the discipline is making leaks *scheduled events* rather than surprises. The leak hierarchy, in descending frequency observed across the scale-hydraulics community:

| Leak site | Cause | Fix | Typical interval |
|---|---|---|---|
| Cylinder rod seal | Rod wiper wear, dust ingestion | Seal kit (~$8–15/cylinder), 30-min bench job | 150–300 run-hours |
| Hose push-fit | Vibration walk-out, heat cycling | Re-cut tube end, re-seat; replace tube every 2nd service | 100–200 h |
| Valve spool O-rings | Heat aging | Spool seal kit | 300–500 h |
| Pump shaft seal | Normal wear | Pump rebuild or swap (~$120–180) | 400–600 h |
| Tank filler/gauge threads | Over-torque, missing PTFE tape | Re-tape, torque to spec | Commissioning errors only |

Leak response doctrine: any visible external leak takes the machine out of service *immediately* (status → `maintenance` in `fleet_inventory`), because at 200–400 ml total volume, a "small" leak is a large fraction of the charge, and running a starved gear pump destroys it in minutes.

### 3.5 Why hydraulics are premium-only: the doctrine in full

The founder's fleet doctrine — "prioritize electromechanical durability and rapid artisan repair over premium leak-prone hydraulic systems" for the rental fleet — is now defensible in numbers:

1. **Capital at risk per Shift.** A rental 1580 puts ~$500 (landed, prepped) in a stranger's hands; a K970 puts ~$9,000+. At equal damage probability the expected loss per Shift differs by 18×.
2. **Failure modes are asymmetric.** An abused lead-screw machine strips a $6 gear or kills a $3 micro-switch — a 20-minute Artisan fix. An abused hydraulic machine ingests grit, scores a pump, or cooks its oil — a multi-day, $150–400 event that also takes the park's flagship off display.
3. **Turnaround time.** Rental machines must flip between customers in under 5 minutes. A hydraulic machine wants a rod-wipe, level glance and temperature check between sessions — exactly what a supervised premium format provides and a walk-up format destroys.
4. **The premium *is* the scarcity.** Because only one machine in the park is hydraulic, K970 seat time is a sellable aspiration at $22/$38 with an Artisan included — a better margin than renting it cheap and repairing it often.

### 3.6 Hydraulic maintenance schedule (premium fleet)

| Interval | Task |
|---|---|
| Every session | Rod wipe-down; visual hose scan; quick-coupler cleaned and capped; park over leak tile |
| Daily (open) | Reservoir level at sight window; gauge sanity check (idle + relief pressure); cycle all functions to stops once, gently |
| Weekly | Tank temperature log after last session; fastener torque scan on valve block and cylinder clevises; track tension (shared SOP-CD-001) |
| Monthly | Oil condition check (color/odor against reference vial); filter/strainer inspection; servo-linkage wear check on all spools |
| 100 run-hours or 6 months | **Full fluid change (SOP-CD-003)**; cylinder rod-seal inspection; relief-valve setting verified against gauge |
| Annually | Pump flow test (timed cylinder full-stroke vs commissioning baseline; >20% slowdown = pump rebuild); full hose replacement on the boom set |

### 3.7 Upgrade path

The hydraulic tier grows in a defined ladder, each rung triggered by the KPI dashboard (Chapter 12), never by enthusiasm: (1) K970 attachment set — hydraulic quick-coupler buckets, ripper, grapple — extends the premium session menu for ~$300–600; (2) second premium machine, a **K988-100S wheel loader** (~$3,800–4,600 direct), chosen over a second excavator because a loader-plus-excavator premium duo enables the "master pair" corporate format (Chapter 8.5); (3) K350 or K980 excavator as the third machine and competition flagship; (4) only in Phase 3, a boutique grader or LESU specialty machine for display. Every added hydraulic machine adds ~0.25 FTE of Artisan load — the dashboard prices that in before approving the purchase.

---

## 4. Electromechanical Lead-Screw Machines (Rental Fleet)

### 4.1 The mechanism

Open a Huina 1580's boom actuator and you find the whole rental doctrine in one assembly: a brushed 380/540-class motor, a small reduction gearbox, and a **lead screw** — a threaded steel rod turning inside a bronze or steel nut attached to the boom linkage. Motor spins, screw turns, nut travels, boom rises. Where the Kabolite meters oil, the Huina meters *rotation*. At each end of travel a **micro-switch** (limit switch) cuts motor power so the actuator cannot drive itself past its mechanical stop.

The lead screw is mechanically self-locking at these helix angles: back-driving force from the bucket cannot rotate the screw. This gives lead-screw machines their signature party trick — an excavator holding a loaded bucket mid-air indefinitely, drawing zero current — and their signature limitation: motion speed is fixed by screw pitch and motor RPM, so movements are steady and deliberate rather than proportionally fluid. For a rental audience this is a feature. The machine is *predictable*.

### 4.2 Durability advantages — why this is the rental architecture

- **No fluid, no leaks, no contamination pathway.** The Mining Zone's dust cannot enter a sealed screw tube the way it enters a hydraulic circuit. Actuators run for hundreds of hours with a grease refresh as the only intervention.
- **Every failure is a discrete, cheap part.** Motors ($4–8), micro-switches ($0.50–1.50), gears ($3–10), screws/nuts ($8–15). The complete drivetrain of a 1580 actuator costs less than one hydraulic seal kit *installation*.
- **Abuse-tolerant by design.** Stall the bucket against bedrock and the limit switch or the ESC current fold-back intervenes; worst case a nylon gear strips — sacrificially, protecting the metal train. This is the machine equivalent of a shear pin.
- **Field-repairable in Shift-scale time.** The refurbishment procedure below returns a machine to service in 20–45 minutes. Rental economics live and die on this number.

### 4.3 Common failure modes

Three failure modes account for an estimated 80%+ of rental-fleet defects (the division FMEA in Chapter 10.7 formalizes this):

1. **Micro-switch limit failures.** The switches live at the actuator travel ends and eat a mechanical click every cycle — tens of thousands of cycles per season. Failure presents two ways: *fail-open* (function stops before end of travel — annoying) or *fail-closed/welded* (motor drives past the stop until the gearbox stalls — destructive if not caught). Dust ingress accelerates both. This is the #1 consumable on the heavy fleet; the digest's spares doctrine lists micro-switches at MEDIUM turnover and we stock them by the hundred (Chapter 10.6). Replacement is SOP-CD-002.
2. **Bushing wear.** Boom, stick and bucket pivots ride on plain bushings. Grit acts as lapping compound; worn bushings present as bucket slop (>2–3 mm play at the teeth), then as misaligned lead-screw side-loading, which then eats the screw nut — a cheap defect cascading into a moderate one. The weekly PM slop-check exists to break that cascade.
3. **Gearbox stripping.** The reduction stages mix metal and nylon gears. Shock loads (dropped boom, bucket slammed into the pit wall, truck driven off a berm) strip nylon teeth. Symptom: motor audibly spinning, function dead or clicking. The fix is a gear set; the *prevention* is the berm-and-geometry design of the site itself (Chapter 6), which is deliberately shaped so that the highest-energy mistakes customers can make are within the fleet's shock tolerance.

Secondary modes: brushed-motor brush wear (~300–500 h, presents as weak/sparky function), track-pin walk-out on excavators and dozers (daily visual, pins re-staked), steering-servo failures on trucks (the 1582's steering servo is the truck's hardest-worked part), connector fatigue (solved fleet-wide by the XT60 standard and JST XH telemetry connectors), and slip-ring oxidation in the 1580's continuous-rotation slew (annual clean).

### 4.4 Refurbishment procedure — the 45-minute turnaround

Every rental machine cycles through **The Works** for refurbishment either on PM schedule (Chapter 10) or on defect. The standard flow, staged so that one Artisan completes it inside 45 minutes with parts from the ghost-machine bins:

1. Intake: scan asset QR; RC WORLD OS pulls `maintenance_logs` history and open defect notes; photograph as-received condition.
2. Blow-down (dry compressed air, ≤2 bar, outdoors) — never wet-wash an electromechanical machine; water carries fines *into* screw tubes.
3. Function test on the bench PSU at 7.4 V: run every actuator end-to-end, listening — a healthy lead screw hums; a dry one squeals; a worn nut knocks.
4. Open the failed/scheduled actuator only (do not shotgun-open everything; every opening is a dust opportunity). Replace the discrete failed part: switch, gear set, motor, or screw/nut pair.
5. Re-grease: lithium grease (NLGI 2) on screws and gears — the same continuous-turnover consumable the digest mandates; silicone grease on switch plungers.
6. Pivot pass: check bushing slop at bucket teeth (<2 mm), re-pin tracks, torque scan.
7. Electrical pass: XT60 pull-test, wire chafe scan, Heavy-Node JST XH connectors seated and latched, conformal-coating visual on the node.
8. Close, run 5-minute load test in the workshop dig box (a 1 m² sand tray kept for exactly this), log parts to `maintenance_logs` (parts_used JSONB), status → `active`.

> **Trade Hack.** Keep every actuator's screws in a magnetic parts tray *per actuator*, photographed before disassembly on the intake phone. The 1580 uses four visually similar screw lengths; a long screw in a shallow boss cracks the casting — the single most common self-inflicted workshop injury to these machines.

---

## 5. Fleet Planning, Utilization Mathematics & Battery Logistics

### 5.1 The 1:3 ratio, derived

The canonical excavator : dump truck ratio of **1:3** is not a style choice; it is elementary queueing arithmetic applied to the physical circuit, and it must survive every future fleet decision, so here is the derivation.

Measure the Mining Zone cycle (timings from pilot testing on the Chapter 6 geometry, rounded to be conservative):

| Circuit element | Time |
|---|---|
| Excavator loads one truck (4–6 bucket passes at ~25–35 s/pass incl. spillage cleanup) | ~2.5–3.0 min |
| Truck hauls loaded to hopper (~45 m haul at scale speed, incl. ramp) | ~1.5 min |
| Truck queues + tips at hopper + weighs | ~1.0 min |
| Truck returns empty | ~1.5 min |
| **Truck round trip (excluding loading)** | **~4.0 min** |

An excavator can start loading a new truck every ~3 minutes. Each truck is away from the face for ~4 minutes per cycle. Trucks required to keep the face continuously served = (loading interval + away time) / loading interval = (3 + 4)/3 ≈ 2.3 — call it 3 with human variance, spillage stops, and the fact that customers are *supposed* to be having fun, not hitting takt time. Fewer than three and the excavator operator stands idle waiting for a bed to load (the most expensive boredom in the division, since the excavator is the experience customers came for). More than three and trucks stack at the face, which reads as congestion and invites bumper-car behavior. **Three circulating trucks per active excavator keeps every seat busy.**

Fleet-wide: 6 excavators × 3 = 18 trucks. In practice the division runs **4 active pods** (4 excavators + 12 trucks = 16 simultaneous customers) at peak, holding 2 excavators and 6 trucks in the swap/charge/maintenance rotation — a 33% reserve that lets the zone absorb a machine failure without a visible hole in the circuit.

### 5.2 Duty cycles

Construction machines are the gentlest duty in the park electrically and the harshest mechanically. An excavator's drive motors idle most of the Shift (the machine walks perhaps 10 m total); its actuator motors run intermittent 2–8 s bursts at modest current. Net battery draw per 20-minute Shift: typically 25–40% of a 2,000 mAh 2S pack — which is exactly why the canonical Shift returns the machine with ~30% buffer intact and why one pack safely covers consecutive Shifts *only* on paper: doctrine says swap at every Operator Shift pit stop and at every second Casual Shift, keeping every issued machine inside the LiPo window of **3.4–4.2 V/cell** with margin. Dump trucks draw more evenly (continuous driving) and get swapped every second Shift without exception. The telemetry kill-switch (PWM intercept) enforces the floor: under 3.4 V/cell the node throttles to 20% and orders the machine to the pit; this protects packs from the one failure customers cannot see coming.

### 5.3 Utilization mathematics — the worked example

The honest arithmetic every fleet decision hangs from. Definitions: operating day 10:00–20:00 (10 h); Shift = 20 min; turnaround (transmitter hand-off, battery decision, stage machine) budgeted 5 min.

- **Design capacity per machine:** 60/(20+5) = 2.4 sellable Shifts/hour → **24 Shifts/machine/day**.
- **Peak-day reality (weekend/holiday):** the 4-pod circuit (16 customer seats) sustained across the 6 busiest hours plus half-loaded shoulders ≈ 15–18 sold Shifts/machine — i.e., peak days genuinely approach capacity, which is why the reserve pod matters.
- **Blended annual reality:** weekday daytime is school time; the honest planning number, consistent with the park-wide Year 1 model (Volume 10: ≈$1.28 M total revenue across all streams), is a **blended average of ~1.5–2.0 paid Shifts/machine/day across the 360-day year** for the standard fleet, rising toward 3+ in Year 2 as memberships and leagues build weekday base load.

Revenue per machine per day at canon pricing (**$15 Casual / $26 Operator standard; $22/$38 premium**), taking Operator Shifts as ~25% of sales (2 blocks at $26 = $13/block):

| Scenario | Paid blocks/day | Effective $/block | Revenue/machine/day | Standard fleet (29 machines)/yr |
|---|---|---|---|---|
| Year 1 blended base | 1.75 | $14.50 | **$25** | ~$264,000 |
| Year 2 target | 3.0 | $14.50 | $44 | ~$455,000 |
| Peak day (capacity check) | 16 | $14.50 | $232 | — (not annualizable) |

The premium K970 runs a different model: max 8 supervised sessions/day (each needs Artisan time and a cool-down), realistically 3–5 sold at $22–38 → **$90–150/day**, ~$35–50k/year from one machine — roughly matching the *entire* rest of the fleet's per-unit revenue on 2% of the fleet's maintenance staffing but 50% of its capital. Add Agriculture (12 tractors at child-heavy, party-heavy utilization ≈ $15–20/machine/day blended ≈ $70–85k/yr) and division events (Chapter 8, budgeted $40–60k Year 1), and the **Construction Division Year 1 revenue target is ≈ $410–470k** — roughly a third of park revenue, consistent with Volume 10's model. Machine-level payback is almost embarrassing: a $500 landed Huina 1580 at even the Year 1 blended $25/day returns its capital in under a month of operation; the division's real capital risk is civil works, not fleet.

> **Investor Note.** The gap between 24 Shifts/day capacity and ~2 blended is not waste — it is *option value*. It means the division can absorb 10× demand growth (leagues, school programs, corporate weekdays) with zero additional fleet capex. Volume 10's upside case is built on filling exactly this gap.

### 5.4 Premium session protocol (K970)

Premium Shifts are bookable only at listed times (4–8 slots/day), require the second license tier (Volume 9), and always run one-on-one with an Artisan at a dedicated premium pad beside the main pit (Chapter 6.5). The Artisan runs a 3-minute machine orientation (pump start, gauge, function tour), supervises hands-on, and closes with the maintenance micro-ritual (rod wipe, level glance) *performed in front of the customer* — the ritual is part of the product; premium customers are buying membership in the machine's care, not just stick time.

### 5.5 Battery logistics — the 3:1 swap engine

Canon: **3 batteries per vehicle minimum — one in the machine, one charging, one rested and ready**; 2S 7.4 V (heavy fleet standard) with **XT60** connectors (Deans legacy acceptable on acquired stock); charging only in the bunkered charging room (cinderblock/sandbag construction, Volume 11) on SkyRC T1000/ISDT K4-class multi-port balance chargers.

Division pack pool: 42 powered assets × 3 = **126 packs minimum** (excavator/truck/loader/dozer 2S 2,000–3,000 mAh; tractors 2S 1,500–2,200 mAh; the K970 runs its own 3S 11.1 V 10,000–15,000 mAh pair outside the common pool). Every pack carries a QR and a cycle log in RC WORLD OS.

**Swap workflow (the pit-stop, 90 seconds):** machine arrives at the swap bench inside the service spine (Chapter 6.6) → Artisan checks pack voltage on the go/no-go meter → pulls pack, racks it in the *outbound* crate (never straight onto a charger warm) → fits a *rested* pack from the ready rack (rested ≥ 30 min post-charge) → XT60 firm-click check, hatch closed, machine re-staged. Outbound crates travel to the bunker on the hour; charged packs return to the ready rack tagged with charge-completion time. The three-state discipline (in-machine / charging / rested) is what makes the 20-minute Shift billing safely independent of battery state — no customer ever receives a machine below the buffer line, and no pack ever fast-cycles hot.

**Checklist — battery bench, per swap:**

- [ ] Inbound pack voltage read and logged (flag if any cell < 3.5 V — machine was over-run, investigate)
- [ ] Pack body inspected: no puffing, no dented corners, XT60 pins bright
- [ ] Outbound pack rested ≥ 30 min and ≥ 4.15 V/cell balanced
- [ ] Battery hatch latched; wiring clear of pinch line
- [ ] Swap logged to pack QR + machine asset tag in RC WORLD OS

---

## 6. Mining Zone: Site & Circuit Design

### 6.1 Design intent

The Mining Zone must read, at first sight and from 40 m away, as a *working mine*: benches, haul roads, a headwall, a hopper with a conveyor, dust in the light. Every design decision below serves three masters in fixed priority order: (1) customer sight lines and separation (safety), (2) circuit throughput (the 1:3 logistics), (3) scenography. Where they conflict, that is the order.

### 6.2 CAD-style layout (text description)

Overall envelope: **60 m × 40 m (2,400 m²)**, long axis east–west, sited per the Volume 11 master plan with the 2–4% natural grade falling to the southwest corner (drainage exploits this). Coordinates below are meters from the southwest corner (x east, y north).

- **Operator Rim (y = 36–40, full width):** the elevated customer edge. A continuous compacted-gravel terrace 4 m deep, raised 600 mm above pit-floor datum, faced with timber sleepers. Twelve numbered **operator stations** at 4 m centers (x = 6 to 50), each: 1.2 m standing rail (42 mm galvanized pipe), transmitter shelf, shade sail coverage (4 m × 4 m HDPE sails, 3.2 m posts), and a sight line to its assigned dig face at a viewing angle of 15–25° downward — steep enough to see into the truck beds (judging fill is the skill), shallow enough to read machine attitude at 20 m.
- **Main Pit (x = 4–44, y = 8–32):** the excavation. Two benches: upper bench at −300 mm datum, lower pit floor at −600 mm, connected by the in-pit ramp. Six **dig faces** (DF1–DF6) cut into the north wall of the benches directly below their operator stations, each face 3 m wide with a truck spot marked beside it. Faces are re-cut nightly (Section 6.9) so every morning presents fresh, diggable material at a 30–40° face angle.
- **Haul Road Loop (perimeter of pit, ~110 m lap):** engineered per Section 6.4, running from the faces along the south wall, up the **main ramp** (x = 44–54, rising −600 mm → +400 mm over 4.0 m of run — a 14° grade, inside the 15° canon limit with margin) to the hopper apron, and back down the **return ramp** on the north side (same 14°).
- **Central Processing Hopper (x = 50–56, y = 18–26):** the zone's landmark, Section 6.5, with its tipping apron facing west and its conveyor discharging east onto the stockpile at x = 57.
- **Premium Pad (x = 50–58, y = 30–38):** the K970's own fenced 8 m × 8 m dig cell with a dedicated hardstand, leak tile, and a rail-side viewing edge — the showcase digs where everyone can watch.
- **Service Spine (y = 0–6, full width):** staff-only strip behind a 1.1 m fence: swap bench, machine staging racks, the SD wheel loader's parking bay, tool locker, and the marshal gate at x = 30 (the only customer-adjacent opening, interlocked per Chapter 11).
- **Dozer Push Boxes (x = 8–16, y = 8–12):** two 4 m × 4 m sand cells for the RD-1 dozers, inside the pit but fenced from the haul loop so the youngest operators cannot enter traffic.

### 6.3 Aggregate specification — what the pit is made of

The dig medium is a designed material system, not "sand." Three graded materials in mapped areas, selected on the tension between **diggability** (bucket penetration at 1/14 breakout forces), **dust** (the enemy of bearings, lungs and cameras), and **drainage** (the zone must reopen 2 hours after rain):

| Material | Spec | Where | Why |
|---|---|---|---|
| Washed coarse sand | 0–2 mm, <3% fines, slightly moist | Dig faces DF1–DF4, dozer boxes | Best bucket penetration and heap behavior; washed spec kills airborne dust; holds a 35° face overnight |
| Pea gravel | 5–8 mm rounded | DF5–DF6 ("hard rock" faces), hopper surge bed | Satisfying rattle-and-pour physics for skilled operators; free-draining; too coarse to blow |
| Crushed stone | ≤10 mm angular, compacted | Haul roads, ramps, aprons (structure, not dig medium) | Interlocks under compaction into a firm running surface; the canonical "loose sand to 10 mm crushed stone" ceiling |

Materials are deliberately *not* mixed: sand migrating into the pea-gravel faces (and vice versa) is re-segregated during nightly grooming with the loader's screen bucket. Total initial fill ≈ 55 m³ (sand 30, pea 10, crushed 15), ≈ $2,200–3,500 delivered in most markets — one of the cheapest square meters of attraction surface in the industry.

> **Field Note.** Moisture is a tool. The sand faces run best at 4–6% moisture — dark, cohesive, dust-free, holding clean vertical cuts like real ground. The nightly grooming procedure includes a misting pass, and the morning checklist verifies "face holds a bucket-cut without slumping." Bone-dry sand is the mark of a lazy operator; it digs worse and coats every machine in fines.

### 6.4 Haul road engineering

The haul roads are the division's civil signature and are built like real ones, scaled:

- **Width:** a 1/14 rigid hauler (Huina 1582) is ~150 mm wide. Single-lane running width = 3 vehicle widths = **450 mm**; the main loop is two-lane, **900 mm formed width**, plus berms.
- **Berms:** continuous windrows of compacted crushed stone, **60 mm high** (≈ 40% of truck wheel height — the real-world mine standard is half wheel height; ours is slightly under to keep them climbable by the recovery crawler), on every edge with a drop >100 mm. Berms are the passive barrier that keeps a mis-driven truck on the road; they absorb the highest-frequency customer error (drifting off-edge) with zero damage.
- **Grade:** **maximum 15° (≈27%)** — canonical, and derived from the fleet's continuous-duty limit: brushed 540-class drive motors on a loaded 1582 sustain 14–15° indefinitely, but stall-current heating rises steeply beyond; the canon exists to prevent continuous motor burnout, and the built ramps run 14° to leave margin. Grades are constant-slope (no roller-coaster profiles that shock-load gearboxes) with 300 mm vertical curves at top and bottom.
- **Surface:** 40 mm compacted crushed stone over geotextile, crowned 2% to shed water to the inside drain. The loader re-dresses the crown weekly.
- **Intersections:** the loop is one-way (counter-clockwise); the only two-way segment is the hopper apron, marshaled by painted give-way lines. One-way circulation halves the child-driver conflict rate and is non-negotiable.

### 6.5 The central processing hopper

The hopper is scenography, scoring system and traffic anchor in one structure — a functional scale plant, not a prop:

- **Receiving bin:** 600 mm × 600 mm steel grizzly opening at apron level, with 20 mm bar spacing (passes all aggregate, stops buckets, phones and hands), over a 0.15 m³ surge bin.
- **Weighing:** the surge bin hangs on four **50 kg load cells** (HX711-class amplifiers into an ESP32 on the park mesh). Every tip is weighed to ±20 g and credited within 2 s to the delivering customer via the machine's Heavy-Node identity — this is the tonnage leaderboard's ground truth (Chapter 9.2).
- **Conveyor:** a 2.5 m inclined belt conveyor (200 mm belt, geared 24 V motor, variable 0.1–0.3 m/s) lifts weighed material from the surge bin to the **stockpile tower** discharge at +1.4 m, building a real conical stockpile that the SD loader periodically reclaims back to the faces — the zone's material cycle is closed and visibly honest.
- **Lockout:** the conveyor and bin carry a captive-key lockout (Chapter 11.3); the grizzly is the only customer-machine-accessible interface and is fenced to be reachable by trucks, not by people.
- **Scenography:** corrugated cladding, warning livery, stack light (green = accepting loads, amber = weighing, red = locked out) — the stack light doubles as genuine traffic control for the apron queue.

Build cost: ≈ $6,000–9,000 including load cells, conveyor drive and cladding, fabricated in The Works to Volume 7 drawings.

### 6.6 Operator stations, sight lines and spectating

Each of the twelve rim stations is a designed workplace: rail height 1.1–1.2 m (comfortable forearm rest for adults, chest rail for children on the fold-down 250 mm step), transmitter shelf angled 15°, station number and assigned-face placard, and a QR that opens that station's live telemetry card in the customer app. Shade sails cover all stations (transmitter LCDs and summer dwell time both demand it). Behind the operator line, a 2 m spectator terrace with lean rails — construction is the park's best spectator product and the terrace is deliberately generous. Sight-line rule from the safety review: every operator must see their machine *and* the whole segment of haul road their trucks use, unaided, from their station; no station may require operating a machine behind the hopper's visual shadow — this constraint fixed the hopper's position at the east end.

### 6.7 Drainage and dust control

Water is managed in three layers: (1) the pit floor slopes 1.5% to a gravel-filled sump at the SW corner (the natural low point) with a 100 mm drain line to the park's swale network (Volume 11); (2) haul-road crowns shed to a perimeter French drain; (3) the operator rim and service spine are self-draining compacted gravel. Reopening target after a 20 mm rain event: **2 hours** (pea and crushed areas immediately; sand faces after one grooming pass). Dust control: washed aggregate spec (the main measure), 4–6% face moisture maintained by the misting pass, a hose-end misting ring on the hopper surge bin (tipping is the dustiest event), and a hard rule that the blow-down gun lives in The Works, never in the zone.

### 6.8 The service loader and daily dressing

The SD-assigned Huina 1583 (with fabricated straight blade and screen bucket) is the zone's groundskeeper, operated by Artisans between customer waves: crown dressing, berm repair, spill-drift recovery on the apron, stockpile reclaim. It is deliberately *visible* doing this work — a staff machine working the site reads as authenticity, and customers routinely ask to be taught what it is doing, which is a license-program conversion moment.

### 6.9 Nightly re-grooming

**SOP-CD-004 — Mining Zone Nightly Re-Grooming**
**SOP ID:** SOP-CD-004 · **Revision:** 1.0 · **Owner:** Construction Division Lead · **PPE:** gloves, safety glasses, dust mask during dry raking · **Tools:** SD loader + blade/screen bucket, landscape rake, misting hose, face-cut template board, torque driver (hopper grizzly bolts) · **Frequency:** nightly at close, 40–55 min, 2 staff

1. Confirm zone clear of customers; close marshal gate; set hopper stack light to red and apply conveyor lockout (captive key to pocket).
2. Sweep the pit for foreign objects (dropped items, track pins, bucket teeth); log any fleet hardware found against the day's machine roster.
3. Loader pass 1: reclaim spill drifts from apron and haul loop back to their source material areas (sand to sand, pea to pea — use the screen bucket where materials have mixed).
4. Loader pass 2: re-dress haul-road crown and repair berms to the 60 mm gauge board.
5. Re-cut all six dig faces to the template: 30–40° face angle, 150–250 mm of loose won material heaped at the toe of each face (tomorrow's first customers must succeed in their first minute).
6. Reclaim stockpile overflow: if the conveyor stockpile exceeds the 0.5 m³ mark, loader-carry material back to faces per the material map.
7. Misting pass on all sand areas to 4–6% moisture (dark, cohesive, no standing water).
8. Hopper: empty and brush the surge bin, verify load-cell zero (±50 g) on the maintenance screen, torque-check grizzly bolts weekly (log).
9. Rake operator rim and spectator terrace; empty station bins.
10. Walk the drainage sump and French-drain outlets; clear debris.
11. Log completion in RC WORLD OS grooming register with photos of faces DF1–DF6; release lockout only on next morning's opening checklist.

**Checklist — Mining Zone morning opening (marshal, 15 min):**

- [ ] Grooming register signed off from previous night; faces DF1–DF6 hold a clean bucket-cut without slumping
- [ ] Haul-road walk: crown intact, berms to 60 mm gauge, no washouts, one-way arrows visible
- [ ] Hopper: lockout released by key holder, load-cell zero verified, stack light green, conveyor test-run 30 s
- [ ] Operator stations: rails tight, shelves clear, shade sails tensioned, station QRs scanning
- [ ] Fleet staging: 4 pods staged (4 excavators + 12 trucks), reserve pod status confirmed in RC WORLD OS
- [ ] All staged machines: track/tire visual, battery ≥ rested-pack spec, Heavy-Node heartbeat live on the admin map
- [ ] Premium pad: K970 leak tile clean, reservoir level in window, gauge sanity check passed
- [ ] Recovery crawler charged and staged at the marshal gate; buzzer test on one machine
- [ ] Weather call logged (wind/dust, rain radar); misting pass if faces have dried overnight

---

## 7. Agriculture Zone: Field Grid & Tractor Operations

### 7.1 Concept

The Agriculture Zone is the Mining Zone's calmer sibling: **1,500 m² (50 m × 30 m)** modeled on a commercial tobacco/maize operation per the founder's notes — fields, not gardens. Where mining sells production, agriculture sells *husbandry*: plowing a straight furrow, discing a field to tilth, hauling a tandem-trailer load to the barn without shedding it. It is the division's best fit for younger children, its best photographic contrast (green rows against the pit's ochre), and the home of the park's most distinctive seasonal event, the Harvest Campaign.

### 7.2 Field grid design

The zone is a grid of **eight field cells, each 9 m × 5.5 m**, separated by 600 mm compacted access lanes (tractor roads), with a **barn/silo receiving complex** on the east edge and irrigation trenches as working scenery:

- **Field cells F1–F4 (tillage fields):** 100 mm depth of the same washed 0–2 mm sand as the pit (one aggregate supply chain, deliberate), kept at 4–6% moisture. These are the plowing and discing fields, re-groomed flat every night so morning customers cut first furrows into clean ground.
- **Field cells F5–F6 (row-crop fields):** permanent simulated crop rows at 250 mm spacing. Row material selection (tested for durability against 1/16 wheel strikes): rows of UV-stable artificial boxwood/turf strip for "young maize", and bundled natural-look plastic raffia in drilled timber battens for mature tobacco/maize — robust, replaceable in 1 m sections, and convincing at spectator distance. Between-row lanes are exactly 1.4 tractor widths: threading them clean is the zone's core skill.
- **Field cells F7–F8 (harvest/haul fields):** where campaign events stage crop tokens (Section 7.5).
- **Irrigation trenches:** 150 mm wide × 80 mm deep formed channels along the grid's spines, dry by default, flooded from a hose valve for events; crossed by four timber culvert bridges sized single-tractor.
- **Barn & silo:** the receiving point — a 2.4 m × 1.8 m scale barn with a drive-through weighbridge bay (same HX711 load-cell architecture as the mining hopper, 20 kg cells) and a silo tower that trailer loads are "delivered" against. All deliveries score to the customer account.
- **Operator line:** along the south edge, six stations built to the same rail/shade/sight-line standard as the mining rim; the whole grid is visible from every station.

### 7.3 The implement library

Tractors are the platform; implements are the content. The **Double E E351-class 1/16 tractors** (12 units, high-torque 4WD, ~$80–120 wholesale) are fitted at The Works with the park-standard **pin hitch** (3 mm clevis pin on a 20 mm plate) so every implement fits every tractor. The library (~20 pieces, $15–60 each wholesale, several shop-fabricated):

| Implement | Qty | Function | Gameplay |
|---|---|---|---|
| Single/dual-bottom plow | 4 | Cuts real furrows in F1–F4 | Straightness scored against chalk line |
| Disc harrow | 3 | Breaks furrows to tilth | Coverage scoring (photo overlay) |
| Tipping trailer (single-axle) | 5 | Haulage | Load/deliver cycles to barn |
| Tandem trailer set | 2 | Advanced haulage (canon: tandem trailers) | License-gated; jackknife = retrieval event |
| Water bowser | 2 | Fills from irrigation valve, wets fields | Staff + campaign use |
| Bale/crop flatbed | 2 | Carries crop tokens | Harvest Campaign core |
| Front blade (fits E351 loader arms) | 2 | Lane dressing | Staff grooming + skill badge |

### 7.4 Tractor operations gameplay

A standard Agriculture Shift issues a tractor plus one implement chosen at booking. The zone marshal assigns a field cell and a task card: *plow F2 north-south*, *disc F3 to full coverage*, *haul six trailer loads from F7 to the barn*. Task completion, straightness scores and delivered weights post to the customer profile exactly like mining tonnage — same telemetry, gentler physics. The zone runs 8 concurrent customers comfortably (6 field tasks + 2 haul circuits) against 12 tractors, holding the same 33% rotation reserve as the pit.

### 7.5 Seasonal Harvest Campaigns

Twice per year (spring planting, autumn harvest — inverted in southern-hemisphere deployments) the zone runs a two-week **Harvest Campaign**: F5–F8 are dressed with crop tokens (weighted 40 mm "maize bundle" and "tobacco bale" pucks, ~200 g each, RFID-tagged), and every Shift's deliveries accrue to a park-wide campaign total with a public silo-gauge display. Individual contributions earn campaign badges (Volume 9); the campaign finale weekend crowns a Harvest Champion per age class and feeds the events calendar (Chapter 8.6). Token cost ≈ $400 per campaign set; the campaign reliably doubles zone utilization for its fortnight in comparable seasonal-event benchmarks, and is the single cheapest utilization lever in this volume.

---

## 8. Earthmoving Competitions & Events

### 8.1 Why competition matters here

Racing has a century of borrowed formats; earthmoving has none — which means RC WORLD gets to *invent* its competitive canon, and owning formats is owning the community that plays them. Construction competition also solves the division's weekday problem: leagues and corporate bookings are scheduled demand that fills the utilization gap identified in Chapter 5.3. Every format below runs on standard rental machines (parity doctrine, as in Motorsport: skill decides, not hardware) with scoring through the hopper load cells, RFID tokens and Heavy-Node telemetry — no manual judging beyond a marshal's penalty flag.

### 8.2 Precision events

- **Golf-Ball Pickup (the signature).** Six golf balls on 60 mm tees in a 2 m arc around a 1580. Score = balls placed unbroken into a bucket-width target box; time is tiebreaker only. Championship variant: balls swapped for eggs, boiled for juniors, raw for finals night — theatrical, photogenic, and a genuine multi-channel finesse test.
- **Bucket Curling.** Push a 500 g puck along a 3 m painted lane with the excavator bucket; nearest-to-target rings score 5/3/1. Team relay format.
- **Trench & Backfill.** Cut a 400 mm trench to a depth template, lay the "pipe" (a 300 mm dowel, placed by grapple), backfill and dress flat. Judged on template gauge fit + surface flatness under a straightedge. The trade-skill event — real operators enter this one.

### 8.3 Load-and-haul time trials

One excavator + one truck per team of two (or solo iron-man with transmitter hand-offs). Move **20 kg net through the hopper** from a marked face; clock stops at the twentieth weighed kilogram. Spillage is not swept — it is simply tonnage you no longer have. Current course-record pace from pilot testing: ~11 minutes; the leaderboard lives permanently in the app and on the zone display. Variants: uphill-only routing (the 14° ramp both ways), night format under work lights (Phase 3), loader class (1583 direct to hopper).

### 8.4 Team mining campaigns — the league core

The flagship league format, and the reason the hopper has load cells. Teams of four (2 excavator seats rotating, 2 truck seats) run **45-minute campaign sessions**; every kilogram weighed at the hopper credits the team via machine RFID/Heavy-Node identity. The **tonnage leaderboard** is seasonal: an 8-week league, one campaign session per team per week, table on aggregate tonnage with a playoff weekend. Penalties are automated where possible (geofence breach = 60 s machine timeout via the kill-switch's throttle-limit mode; hopper mis-tip logged by the marshal tablet). League fee $120/team/season against ~$60 of Shift value consumed — competition is margin-accretive by design, and an 8-team league fills 32 otherwise-dead weekday-evening machine-hours.

### 8.5 Corporate site-simulation challenges

The premium B2B product (from **$1,400 / 2 h / 20 pax**, canon): the group becomes a contractor. A brief is issued — *deliver 60 kg to the hopper, cut and backfill one trench, keep zero safety flags* — roles are assigned (operators, logistics planner, site foreman with the marshal tablet's read-only dashboard), and the debrief hands each participant their personal telemetry card. Add-ons: K970 demo session with the Artisan ($150), catered Toolbox Talk boardroom brief, branded hi-vis. The format sells because it is a genuine operations-management exercise wearing a toy's clothes — the same 1:3 queueing logic in Chapter 5 becomes the customer's problem for two hours, and mixed-seniority groups discover their best crane-brain is the intern.

### 8.6 Scoring systems and league structure

All scoring runs on three primitives, so every new format is a configuration, not a build: **weight events** (hopper/barn load cells, ±20 g), **token events** (RFID pucks and crop tokens, read at delivery points), and **telemetry events** (zone dwell, geofence penalties, smoothness index from voltage-sag analysis — the F1-style power-management canon applied to digging). League structure mirrors the park-wide three-tier ladder defined in Volume 9: **Open evenings** (casual, monthly, any license) → **Division League** (seasonal, 8 weeks, second license tier) → **RC WORLD Championship events** (annual, cross-division, invitational). Construction contributes three championship disciplines: Precision (8.2), Load-and-Haul (8.3), and the Team Campaign final (8.4).

---

## 9. Gamification & Telemetry Interface

### 9.1 Heavy-Node fitment

Every division machine carries an **RCW Heavy-Node** (~40 × 30 mm, ESP32-C3 + ATGM336H GPS, conformal-coated, unit cost < $15 — full hardware spec in the digest and Volume 7): inline PWM intercept between receiver and ESC, battery-voltage divider, park-mesh Wi-Fi. The Heavy-Node form factor exists *for this fleet*: **JST XH (2.5 mm) positive-latch connectors** on all signal lines so an Artisan swaps a node in two minutes during refurbishment without soldering (battery sense leads remain soldered per the hardware doctrine). Nodes power downstream of the machine's main switch — a parked fleet draws nothing overnight.

Construction telemetry earns its keep differently from racing telemetry: speed matters less; **identity, position, voltage and load events** matter more. The node is what binds a hopper weight to a customer, a geofence to a penalty, and a voltage sag to the kill-switch doctrine (<3.4 V/cell → remote throttle to 20% → order to pit).

### 9.2 Tonnage as currency

Every weighed kilogram a customer delivers — mining hopper or agriculture weighbridge — posts to their profile as **career tonnage**, the division's headline progression stat. Tonnage drives license progression (next section), feeds leaderboards (daily, seasonal, all-time), earns **Gears** loyalty points at the park-standard rate, and unlocks cosmetic flair (machine nameplates on the booking screen at 1 t, 5 t, 25 t career milestones). Tonnage is deliberately *additive and unlosable* — construction progression rewards accumulation and care, in contrast to racing's volatile lap-time ladder; the two progressions are designed as complementary personalities of the same RC WORLD License system (see Volume 9, Chapter 3, for the full tier/badge matrix).

### 9.3 Licenses and badges (division view)

The division gates and rewards through the park license ladder: tier 1 (post-Toolbox-Talk) unlocks RD-1 machines; tier 2 (earned via tonnage + a 5-minute practical: load a truck with < 10% spillage) unlocks the 1583 loader, tandem trailers and league entry; tier 3 plus a booked assessment unlocks **premium K970 sessions**. Division-specific badges: *First Furrow*, *Clean Loader* (10 spill-free truckloads), *Ramp Master* (100 loaded ramp climbs without a retrieval), *Night Shift* (Phase 3), *Tow-Truck Hero* (see below). Badge logic runs entirely on telemetry primitives already collected — no marshal data entry.

### 9.4 The Tow-Truck Retrieval Protocol as gameplay

When a machine dies mid-Shift — flat pack, stripped gear, stuck on a berm — the canonical protocol converts the division's worst moment into its most-remembered one: the machine's node fires the **85 dB localized buzzer**; the customer surrenders their transmitter at the marshal gate and receives the controls of a **1/10 winch-equipped recovery crawler**; under marshal guidance they drive out, rig the winch (Artisan-supervised hook-up at the machine — customers never step past the gate), and tow their casualty to the service spine, then receive a fresh machine with the Shift clock paused during recovery. The protocol closes the safety loop (customers never walk onto live circuits — canon), earns the *Tow-Truck Hero* badge on first completion, and pilot feedback is unambiguous: a meaningful share of children *try* to get recovered. The division holds one of the park's four recovery crawlers permanently at the marshal gate.

---

## 10. Maintenance Program

### 10.1 Philosophy

The division's maintenance doctrine in one sentence: **electromechanical machines are maintained by replacement of cheap discrete parts on schedule; the hydraulic machine is maintained by condition monitoring and cleanliness.** Everything below implements that sentence. All work is logged to `maintenance_logs` (vehicle, mechanic, parts_used JSONB, description, date_resolved); predictive flags fire from `fleet_inventory.total_hours_run` per the RC WORLD OS admin doctrine.

### 10.2 Preventive maintenance matrix

| Task | 1580 excavator | 1582/1573 truck | 1583 loader | 1554/69 dozer | E351 tractor | K970 (adds Ch. 3.6) |
|---|---|---|---|---|---|---|
| Visual + function test, connector check | Daily | Daily | Daily | Daily | Daily | Every session |
| Blow-down, track/tire debris pick | Daily | Daily | Daily | Daily | Daily | Daily |
| Track tension check (SOP-CD-001) | Weekly | — | — | Weekly | — | Weekly |
| Steering linkage & servo check | — | Weekly | Weekly (articulation) | — | Weekly | — |
| Pivot-bushing slop gauge (<2 mm at teeth/blade) | Weekly | — | Weekly | Weekly | — | Weekly (pins) |
| Lead-screw lubrication (SOP-CD-005, §10.4) | Monthly / 40 h | — | Monthly (lift arms) | Monthly | — | n/a |
| Gearbox open-inspect, gear wear | Quarterly / 120 h | Quarterly | Quarterly | Quarterly | Quarterly | Annual (drive/slew) |
| Motor brush / current-draw baseline | Quarterly | Quarterly | Quarterly | Quarterly | Quarterly | Annual (brushless: bearing feel) |
| Micro-switch test bank (all limits) | Monthly | Monthly (tip limit) | Monthly | Monthly | — | — |
| Slip-ring clean (continuous slew) | Annual | — | — | — | — | — |
| Full refurbishment pass (§4.4) | 150 h or on defect | 200 h | 150 h | 100 h | 200 h | OEM service protocol |
| Battery pack pool audit | Weekly (shared, by pack QR rotation) | | | | | own 3S pair, weekly |

Run-hours come from telemetry, not guesswork — `total_hours_run` increments on live PWM activity, so a machine that sat staged all day accrues nothing.

### 10.3 SOP-CD-001 — Track Tension Check & Adjustment (tracked fleet)

**SOP ID:** SOP-CD-001 · **Revision:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** none beyond shop standard · **Tools:** 3 mm steel rule, hex driver set, lithium grease, torque driver (0.6 N·m) · **Frequency:** weekly per tracked machine, or after any thrown track

1. Bench the machine, power off, bucket/blade grounded.
2. Clean track run with a stiff brush; pick embedded stones from between pads (the #1 cause of false tension readings and pad wear).
3. Measure sag at mid-span between idler and sprocket, pressing with one finger (~10 N): specification **3–5 mm** on 1580/1583-class, 2–4 mm on 1/16 dozers.
4. Out of spec: slacken idler-yoke lock screws, adjust tension screw quarter-turn at a time, re-measure. Never tension to drum-tight — over-tension multiplies drive-motor current ~15–20% and eats sprocket bushings; the telemetry current baseline will betray you at the quarterly check.
5. Check track-pin staking along both runs; re-stake any proud pin (track pins are a CONTINUOUS-turnover consumable — bin any pin that walks twice).
6. Torque idler lock screws to 0.6 N·m; grease idler axle port (one shot).
7. Run 60 s figure-eight in the workshop dig box; confirm no track walk-off in tight turns.
8. Log measured sag before/after to `maintenance_logs`.

### 10.4 SOP-CD-005 — Lead-Screw Lubrication

**SOP ID:** SOP-CD-005 · **Revision:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** nitrile gloves · **Tools:** lithium grease (NLGI 2), grease brush, lint-free wipes, isopropyl alcohol, bench PSU · **Frequency:** monthly or 40 run-hours per lead-screw actuator

1. Open the actuator access cover (boom, stick, bucket in turn on the 1580; lift arms on 1583; blade screw on dozers).
2. Run the actuator to full extension on bench power; wipe the exposed screw with IPA wipe — inspect the wipe: gray paste = normal wear; glitter = nut shedding, replace nut pair now rather than mid-season.
3. Brush a rice-grain bead of lithium grease along the full thread; do not pack the tube (excess grease is a dust magnet — thin film, full coverage).
4. Cycle full travel 3× to distribute; verify both limit switches click and cut at the ends.
5. Wipe squeeze-out, close cover, log.

### 10.5 SOP-CD-002 — Micro-Switch Replacement (limit switches)

**SOP ID:** SOP-CD-002 · **Revision:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** safety glasses (spring-loaded parts) · **Tools:** soldering iron + 60/40 or SAC solder, heat-shrink, flush cutters, multimeter (continuity), replacement switch (park-standard KW11-3Z-class, stocked ×200) · **Frequency:** on defect or monthly test-bank failure

1. Diagnose first: with the actuator cover open, actuate the suspect switch by hand under continuity meter — confirm fail-open (no click-through) or fail-closed (welded) before touching solder. If the switch tests good, the fault is the actuator crush-stop misadjusted; fix that instead.
2. Photograph wire routing. Note the switch's lever type (plain / roller) and throw direction — Huina uses both orientations in one machine.
3. Desolder or cut back to bright copper; strip 3 mm; slide heat-shrink on *now* (the step everyone forgets).
4. Solder the new switch NO/NC/COM exactly per photo; shrink the joints.
5. Set the mechanical trip point: switch must click **1–2 mm before** the hard mechanical stop of the travel — this margin is the whole point of the switch; verify by hand-cranking the screw to the stop.
6. Bench-run five full cycles; confirm clean cut-off both ends with no motor stall audible.
7. Log switch position (e.g. "boom, upper limit") in parts_used — position-level data is what lets the FMEA table below stay honest.

### 10.6 Spare parts stocking & reorder points

The division's shelf in The Works, sized to keep any single failure from becoming downtime (par levels assume the 42-machine fleet; Volume 8 carries suppliers and pricing):

| Part | Par stock | Reorder at | Turnover | Notes |
|---|---|---|---|---|
| Micro-switches (KW11-class) | 200 | 80 | Medium-high | #1 heavy-fleet consumable |
| Excavator track pins + pads | 300 pins / 40 pads | 120 / 15 | Continuous | Canon consumable |
| Nylon + metal gear sets (per actuator model) | 12 sets each type | 5 | High | Stock both: nylon for RD-1 sacrificial role |
| Lead screw + nut pairs (1580 boom/stick/bucket) | 6 each | 2 | Medium | |
| Brushed 380/540/550 motors | 15 | 6 | Medium | Canon spares line |
| Steering servos 15/25 kg digital | 10 | 4 | High | Trucks + tractors |
| ESCs (brushed, fleet-standard) | 6 | 2 | Medium | |
| XT60 pairs, JST XH housings/pins | 100 / 200 | 40 / 80 | Continuous | |
| 2S LiPo packs (pool replenishment) | 12 | 4 | Continuous | Pool attrition ~15%/yr |
| Lithium grease, Loctite blue, IPA | 4 / 6 / 4 units | 1 / 2 / 1 | Continuous | Canon consumables |
| Hydraulic: cylinder seal kits (K970 set) | 2 full sets | 1 | Low | Long lead — never zero |
| Hydraulic: ISO VG 32 oil (dyed) | 4 L | 1 L | Low | |
| Hydraulic: hose/tube + fittings kit | 1 kit | open | Low | |
| Tractor hitch pins, trailer axles | 30 / 6 | 10 / 2 | Medium | Party-day attrition |

Reorder discipline: RC WORLD OS decrements stock from `parts_used` logging; reorder alerts fire automatically at the levels above with the 4–8 week China-direct lead time already priced in (Volume 8, Chapter 5).

### 10.7 FMEA-lite: excavator and dump truck

Scored 1–5 (severity × occurrence × detection difficulty = RPN; act on RPN ≥ 27):

| Machine | Failure mode | Effect | S | O | D | RPN | Mitigation |
|---|---|---|---|---|---|---|---|
| 1580 | Limit switch fail-closed (welded) | Gearbox stall, possible gear strip mid-Shift | 3 | 4 | 3 | 36 | Monthly test bank (§10.2); ESC current fold-back; SOP-CD-002 |
| 1580 | Lead-screw nut wear | Boom droop under load, function slop | 2 | 3 | 2 | 12 | SOP-CD-005 wipe-inspect; nut pairs on shelf |
| 1580 | Gearbox nylon gear strip (shock) | Function dead, Shift refund | 3 | 3 | 1 | 9 | Site geometry limits drop energy; 20-min gear-set swap |
| 1580 | Track thrown in pivot turn | Machine immobile in pit → retrieval event | 2 | 3 | 1 | 6 | SOP-CD-001 tension spec; retrieval is gameplay, not crisis |
| 1580 | Slip-ring oxidation | Intermittent slew/electrics | 3 | 2 | 4 | 24 | Annual clean; symptom triage card in The Works |
| 1580 | Pack over-discharge (customer runs hidden) | LiPo damage, fire risk in storage | 4 | 2 | 2 | 16 | Node kill-switch at 3.4 V/cell (canon); bench inbound check |
| 1582/73 | Steering servo failure | Truck uncontrollable → circuit blockage | 3 | 4 | 2 | 24 | Weekly linkage check; servo par stock; marshal pulls to shoulder |
| 1582/73 | Tip-linkage bent (overload + slam) | Bed won't seat, spillage all lap | 2 | 3 | 2 | 12 | 4 kg load discipline via bucket-pass counting; straighten/replace linkage |
| 1582/73 | Drive gearbox strip (berm jump) | Truck dead on ramp | 3 | 3 | 1 | 9 | Berm geometry caps launch energy; gear sets on shelf |
| 1582/73 | XT60/wiring chafe at bed pivot | Intermittent power, phantom "dead battery" | 2 | 3 | 4 | 24 | Refurb electrical pass (§4.4 step 7) targets this loom explicitly |
| 1582/73 | Wheel bearing seizure (fines ingress) | Dragging wheel, motor heat | 2 | 3 | 3 | 18 | Daily blow-down; bearing swap at refurb |

### 10.8 Grease points and service diagram (text description)

The laminated bench card for the 1580 (equivalents exist per model) describes a side-elevation outline with eleven numbered points: (1–3) boom, stick, bucket lead-screw tubes — lithium grease, monthly; (4–6) boom-base, stick and bucket pivot bushings — oil pen, weekly; (7) slew-ring gear rim — grease film, quarterly; (8–9) left/right idler axles — grease port, weekly with SOP-CD-001; (10) sprocket bushings — quarterly at gearbox inspection; (11) door/hatch hinges — dry PTFE, as needed. Rule on the card, printed red: *nothing gets grease that touches sand directly* — exposed pivots get oil-pen film only, because grease on an open pivot is grinding paste by lunchtime.

---

## 11. Safety

### 11.1 Hazard picture

The Construction Division's honest hazard list is short but real: **pinch points** (bucket linkages, articulation joints, the 1583's 10 kg-capable loader arms, tipping beds), **the hopper's conveyor and surge bin**, **LiPo handling**, and **people walking where machines run**. Nothing in the rental fleet can seriously injure a supervised customer at operator-station distance — the entire safety architecture exists to *keep* everyone at that distance.

### 11.2 Separation doctrine

Customers operate from the rim and field-line stations, full stop. The pit floor, haul loop and field grid are machine space. The three enforcement layers: physical (rails, fences, the single interlocked marshal gate), procedural (Toolbox Talk module, marshal authority, the Tow-Truck Retrieval Protocol replacing every "can I just grab it" impulse), and technical (geofence on every Heavy-Node: a machine that crosses the customer line gets PWM-killed before it reaches a shoe). Children under 8 operate with a guardian at the station — the station step and dual-shelf design assumes this pairing.

### 11.3 Hopper lockout

The hopper is the division's only powered fixed plant and carries the division's only formal lockout: a captive-key system where the conveyor cannot run unless the key sits in the control station, and the surge-bin access panel cannot open unless that same key is *removed* and inserted in the panel lock. One key, two mutually exclusive locks — cleaning and running are mechanically impossible to combine. Applied nightly in SOP-CD-004, released on the morning checklist, audited weekly.

### 11.4 Premium session supervision

K970 sessions are 1:1 Artisan-supervised at the premium pad — the machine that can genuinely hurt (31 kg, 20+ bar, real breakout force) is never customer-operated without a professional beside the transmitter and the pad fence between machine and audience.

**Checklist — premium hydraulic session (Artisan, per session):**

- [ ] Customer license tier 3 verified; supervised-session waiver acknowledged in app
- [ ] Pad fence gates latched; spectators behind the rail line
- [ ] Reservoir level in sight window; gauge idle + relief reading normal; leak tile clean
- [ ] Function tour delivered (pump start, feathering at stops, temperature awareness)
- [ ] Artisan holds the bind-plug/kill authority for the full session
- [ ] Post-session: rod wipe, level glance, temperature log — performed with the customer watching
- [ ] Session + condition notes logged to `maintenance_logs`

> **Safety Warning.** The most dangerous machine in the division is not the K970 — it is a *charging LiPo*. All charging occurs in the bunkered charging room without exception; no pack charges unattended in the zone, the workshop bench included. The battery-bench checklist and the 3.4–4.2 V/cell window are safety controls first and asset controls second.

### 11.5 SOP-CD-003 — Hydraulic Fluid Change (Premium Fleet)

**SOP ID:** SOP-CD-003 · **Revision:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** nitrile gloves, safety glasses · **Tools:** ISO VG 32 oil (dyed park stock), catch tray, syringe/filler bottle, lint-free wipes, IPA, thread tape, torque driver, white tile · **Frequency:** 100 run-hours or 6 months, and on any contamination event

1. Run the machine 5 minutes at light load to warm and suspend contaminants; park over the catch tray; power off, transmitter secured.
2. Photograph gauge readings warm (idle pressure reference for post-change comparison).
3. Clean the tank filler area *before* opening — the filler neck is the contamination gateway; this step is the SOP's soul.
4. Drain the reservoir via drain port or extraction syringe into the catch tray. Inspect the drained oil against the reference vial: darkening = normal aging; milkiness = water ingress (find it — check rod wipers and filler seal); glitter = metal, stop and escalate to pump inspection before refill.
5. Extend all cylinders fully to push residual oil back to tank; extract again. Do not attempt full-system flush unless contamination was found — over-servicing opens more entry points than it closes.
6. Inspect and clean the suction strainer; replace tank breather element if fitted.
7. Refill with fresh dyed ISO VG 32 to the sight-window line; run pump at idle 60 s; cycle every function slowly to stops twice to purge air (spongy motion = air remaining; repeat).
8. Top to line; verify idle and relief pressures against step 2 photo (±10%); investigate any relief-pressure drift before release.
9. Wipe down, new leak tile under the parking bay, dispose of waste oil per the park's environmental procedure (Volume 11), log volumes and condition notes.

---

## 12. KPIs & Division Dashboard

The division reports weekly on one screen in RC WORLD OS. Targets are Year 1 steady-state; the finance model behind them is Volume 10.

| KPI | Definition | Year 1 target | Red line |
|---|---|---|---|
| Paid Shifts / machine / day (standard fleet) | Sold blocks ÷ fleet-days available | ≥ 1.75 blended | < 1.2 rolling month |
| Division revenue / week | All Shifts + premium + events + campaigns | ≈ $8,000 | < $5,500 |
| Premium session occupancy | Sold ÷ offered K970 slots | ≥ 55% | < 35% (or > 70% → trigger 2nd premium machine review) |
| Fleet availability at open | Machines `active` ÷ fleet | ≥ 90% (38/42) | < 80% |
| Mean turnaround (defect → active) | From `maintenance_logs` | ≤ 24 h rental fleet | > 72 h any machine |
| Maintenance cost / Shift | Parts + consumables ÷ paid Shifts | ≤ $0.90 | > $1.50 |
| Retrieval events / 100 Shifts | Tow-truck deployments | 3–6 (some is *good* — it's gameplay) | > 10 (fleet health) or < 1 (check buzzer/logging) |
| Tonnage / week through hopper | Load-cell total | growth trend | flat 4 weeks with rising Shifts (scoring fault) |
| League + campaign participation | Active team-seats + campaign players | 60+ by Month 9 | — |
| Safety flags / week | Geofence kills + marshal flags | trend only | any customer-contact incident = immediate review |
| Battery pool health | Packs in service ÷ pool; avg internal-resistance drift | ≥ 92% | < 85% |

---

## 13. Volume Summary & Cross-References

The Construction Division is RC WORLD's signature: a working 1/14 open-pit mine and a 1/16 farm, run as a real production system. Its engineering doctrine is a two-tier fleet — 29 cheap, rugged, lead-screw Huina machines earning volume revenue at $15–26 per 20-minute Shift, and one Kabolite K970-class hydraulic flagship earning premium supervised fees at $22–38 — bound together by the 1:3 excavator-to-truck ratio, 15°-max haul roads, a load-cell hopper that turns digging into scores, and a maintenance program built on discrete-part replacement, lithium grease, and micro-switches by the hundred. Division fleet capex is ~$16k wholesale; civil works and the hopper are the real build; Year 1 division revenue target is ≈ $410–470k inside the park's $1.28 M canon.

Cross-references: park-wide fleet and phasing canon — **Volume 1**; competitive landscape for construction RC and diorama suppliers — **Volume 2**; the Motorsport parity doctrine this division's competition rules borrow — **Volume 3**; The Works, custom fabrication (hopper, blades, hitches), RCW Node hardware detail and build tutorials — **Volume 7**; suppliers, wholesale channels, spares pricing and reorder mechanics — **Volume 8**; licenses, badges, Gears, Toolbox Talk and the full progression matrix — **Volume 9, Chapter 3**; division financials, sensitivity and the utilization upside case — **Volume 10**; site master plan, drainage network, charging bunker and fencing standards — **Volume 11**; franchising the Mining Zone as the flagship differentiator — **Volume 12**.

