# Volume 4 — RC Construction Division

**RC WORLD — Master Development Plan** · Volume 4 of 14
**Revision:** 1.0 — July 2026 · **Status:** Living document — bump revision on material change

**Purpose of this volume.** This is the handbook of the RC WORLD Construction Division: the Mining Zone and the Agriculture Zone that open with Phase 1 as one of the park's two anchor attractions. It specifies every machine class the division operates — from the Huina 1580 rental excavators to the single Kabolite-class hydraulic flagship — with anatomy, operating envelopes, verified 2026 market pricing and duty ratings; it derives the 1:3 excavator-to-dump-truck logistics ratio with worked queueing arithmetic; it engineers the haul roads, the open-pit material recirculation loop, the agricultural field grid, and the operator stations customers stand at; it defines the competition formats that convert earthmoving into repeat revenue; and it closes with the division-specific maintenance program, preventive-maintenance matrix and FMEA table that keep forty-two machines in daily public service. It is written to be handed out chapter by chapter: the civil contractor gets Chapters 5, 6 and 10, the Artisans get Chapters 2, 8 and 12, the events team gets Chapter 11, and the investor reads all of it.

**Intended readers.** Investors and lenders assessing Phase 1; the General Manager and Construction Division Lead; Artisans assigned to the heavy fleet; the civil/landscape contractor building the Mining and Agriculture zones (with Volume 11); the events and marketing team designing competition formats (with Volume 9).

**Chapters**

1. Division Overview & Philosophy
2. Excavators
3. Bulldozers & Graders
4. Wheel Loaders
5. Dump Trucks & Haul Logistics
6. The Mining Fleet System
7. The Agriculture Zone
8. Hydraulics Deep-Dive
9. Fleet Planning & Capacity
10. Site & Track Design for Construction Play
11. Earthmoving Competitions & Skill Programs
12. Maintenance & Reliability

---

## 1. Division Overview & Philosophy

### 1.1 The miniaturized industrial complex

The Construction Division is the purest expression of the founding thesis recorded in the original Omni-Zone blueprint: RC WORLD is a **miniaturized industrial complex, not a hobby sandbox**. A sandbox hands a customer an excavator and a pile of sand and leaves the rest to imagination. RC WORLD hands the customer a *job*. The Mining Zone is a simulated open-pit operation whose production circuit actually functions: excavators loading at bench faces, articulated dump trucks hauling on engineered roads that never exceed the canonical 15° incline, a central processing hopper that weighs and swallows every load, a wheel loader keeping the haul roads dressed, and a live tonnage leaderboard that turns twenty minutes of digging into a measurable shift of production. The Agriculture Zone applies the same logic to farming: pre-tilled fields, crop rows at scale spacing, implements that hitch and unhitch, irrigation trenches, a barn-and-silo receiving point, and seasonal harvest campaigns with their own scoring.

The distinction is commercial, not cosmetic. A sandbox exhausts itself in one visit. A production system generates goals, and goals generate return visits: the customer who moved 38 kg of aggregate through the hopper on their first Shift knows exactly what they want to do next time — move 50.

### 1.2 Simulation-of-work as entertainment

The division's product is best described as **simulation-of-work**: the satisfaction of competent labour, compressed into a 20-minute Shift and stripped of consequence. Four properties make this an unusually strong entertainment format:

1. **Low skill floor, high skill ceiling.** A first-timer is productive within two minutes — swing, curl, dump. The ceiling (smooth multi-channel blending, spill-free truck loading, clean trench walls) holds hobbyists for years. Pilot testing consistently shows construction operators using their full Shift while racing customers often crash out early; longer dwell means more F&B capture, more spectating, more Top-Up Sessions.
2. **The widest demographic in the park.** Racing skews young and male. Earthmoving draws families with children who recognize excavators before they can read; adult hobbyists and trades-adjacent enthusiasts for whom the machines are professionally familiar; and corporate groups, because "run a mine together for two hours" is a genuinely novel team exercise (Chapter 11.4).
3. **Almost no competition.** Club racing tracks exist in most large cities; public-access RC *earthmoving* is close to nonexistent worldwide. In Volume 2's competitive-landscape terms, the Mining Zone opens into an effectively empty field.
4. **It monetizes patience, not adrenaline.** Construction machines draw far less current than racing machines and crash less. The division has the park's best battery economics and lowest damage rate per Shift; revenue per machine is comparable to Motorsport while maintenance cost per Shift is materially lower (Chapter 12).

### 1.3 The two-tier fleet doctrine: electromechanical rentals, hydraulic premium

The single most important engineering decision in this volume is inherited directly from the founder's doctrine and must never be reversed: **the rental fleet is electromechanical — motor-and-lead-screw actuation — and hydraulics are reserved for premium supervised experiences and display.**

The reasoning, developed in full in Chapters 2 and 8, compresses to four lines:

- **Capital at risk.** A rental Huina 1580 puts roughly $500 (landed, prepped) in a stranger's hands. A Kabolite K970-class machine puts $8,000–12,000 there. At equal mishandling probability, expected loss per Shift differs by an order of magnitude.
- **Failure asymmetry.** An abused lead-screw machine strips a $6 gear or kills a $1 micro-switch — a 20–45 minute Artisan fix from shelf stock. An abused hydraulic machine ingests grit, scores a pump, or cooks a seal — a multi-day, $150–400 event.
- **Turnaround.** Rental machines must flip between customers in under five minutes. Hydraulic machines want a rod wipe, level glance and temperature check between sessions — exactly what a supervised premium format provides and a walk-up format destroys.
- **Scarcity is the product.** Because only one machine in the park is hydraulic, K970 seat time is a sellable aspiration at premium pricing ($22 Casual / $38 Operator, Artisan always present) rather than a maintenance liability.

> **Investor Note.** The division's fleet asymmetry is the doctrine expressed in dollars: the single hydraulic showcase machine costs more than the other 29 mining machines combined (Chapter 9.1). The cheap machines earn volume fees and are rebuilt for $30 in parts; the expensive machine earns premium fees under professional supervision. Reversing this — renting hydraulics to walk-ins — is how an operator turns a $14,000 fleet line into a $90,000 one with worse uptime.

### 1.4 The customer journey

A Casual Shift in the Mining Zone, end to end: the customer books in RC WORLD OS and completes the Toolbox Talk digital induction once, before first visit (Volume 9). At the zone gate an Artisan scans the booking QR, issues a transmitter bound to a specific machine, and walks the customer to a numbered operator station on the pit rim. The machine is already staged — excavator at a dig face, or dump truck in the loading queue. The 20-minute Shift clock starts at first stick input. The machine's RCW Heavy-Node streams voltage and position; the hopper's load cells credit every delivery to the customer's account. At T-5 minutes the app offers a Top-Up Session if nobody is queued for the class. At Shift end the customer sees their production stats — tonnage, loads, spillage penalty, license progress — and the machine turns around with ~30% battery buffer intact, per the park's billing doctrine. If a machine dies mid-Shift, the customer does not walk onto the pit floor — the **Tow-Truck Retrieval Protocol** converts the breakdown into gameplay (Chapter 10.5).

### 1.5 Scale doctrine

**1/14 for earthmoving, 1/16 for tractors and dozers.** 1/14 is where the Chinese construction-model industry concentrates its engineering — Huina, Kabolite, LESU and JDModel all anchor on 1/14 — which means the deepest spare-parts pools, the widest attachment ecosystems, and the best payload-to-cost ratio. Going larger (1/8 hydraulics) doubles cost for little experiential gain; going smaller (1/24) collapses payload, presence and durability. The founder's notes are explicit and the market confirms them.

---

## 2. Excavators

### 2.1 The rental workhorse: Huina 1580 V4 anatomy

The **Huina 1580 (V4, 2025/2026 production)** is the canonical rental excavator — six units, fleet canon — and it is worth recording exactly why it wins the seat. It is the only machine in its price band that is *genuinely all-metal*: tracks, undercarriage, slew deck, boom, stick and bucket are alloy castings and pressings, while every working motion remains **entirely electromechanical**. Verified 2026-market specification:

| Parameter | Huina 1580 V4 |
|---|---|
| Scale / configuration | 1/14 crawler excavator, 360° continuous slew (slip-ring equipped) |
| Channels | 23 (independent proportional tracks, boom, stick, bucket, slew; lights, sound, smoke) |
| Dimensions | ~700 mm max reach length × 180 mm width × 480 mm max boom height; track frame ~290 mm |
| Weight | ~7–8 kg |
| Battery | 2S 7.4 V 2,000 mAh LiPo (park fleet: XT60-converted, 3:1 pool) |
| Stock runtime | ~40 min per charge — comfortably one 20-min Shift plus the ~30% buffer |
| Attachments (factory case) | Bucket, wood grapple, jackhammer (park: bucket only for rentals; grapple/hammer reserved for events) |
| Wholesale (direct, Volume 8 channel) | **$350–420** |
| Western retail (observed 2026) | $560–800 (typical dealer ~$580; some markets to $860+) |
| Duty rating | RD-1 — rental, unrestricted (duty codes: Chapter 9.1) |

**Lead-screw boom actuation.** Open a 1580 actuator and you find the whole rental doctrine in one assembly: a brushed 380/540-class motor, a small reduction gearbox, and a **lead screw** — a threaded steel rod turning inside a bronze/steel nut pinned to the boom linkage. Motor spins, screw turns, nut travels, boom rises. Where a Kabolite meters oil, the Huina meters *rotation*. At each end of travel a **micro-switch** cuts motor power before the mechanical stop. Three actuators (boom, stick, bucket) plus the slew motor and two track motors complete the drivetrain; a slip ring carries power and signal through the continuously rotating turret.

Two mechanical properties define the machine's character. First, the lead screw is **self-locking** at these helix angles: bucket load cannot back-drive the screw, so the machine holds a loaded bucket mid-air indefinitely, drawing zero current — a party trick no hydraulic machine can match without a counterbalance valve. Second, motion speed is fixed by screw pitch and motor RPM, so movements are steady and deliberate rather than proportionally fluid. For a rental audience this is a feature: the machine is *predictable*, and predictable machines survive strangers.

**Servo and motor layout** (bench card, The Works): boom actuator under the boom root cover; stick actuator inside the stick; bucket actuator on the stick head; slew motor and pinion under the turret deck driving the slew ring; two brushed track motors with steel final drives in the undercarriage; main PCB, sound module, smoke unit and battery bay in the counterweight. The park adds one RCW Heavy-Node inline between receiver and ESC, on JST XH latching connectors for two-minute swaps.

### 2.2 Operating envelope and digging-force expectations

Honest numbers, from pilot testing and community consensus rather than any laboratory claim:

- **Dig depth:** ~150–200 mm below track datum before geometry runs out — which sets the pit-floor bench heights in Chapter 10.
- **Bucket payload:** 150–300 g per pass in the park's washed 0–2 mm sand; 4–6 passes fill a Huina 1582 truck to its ~4 kg working load.
- **Breakout force at the teeth:** of the order of 2–3 kgf — enough to cut a moist sand face cleanly, not enough to self-injure against the pit's timber edging. The face material spec (Chapter 6.4) is tuned so the machine always *feels* strong.
- **Cycle time:** a relaxed swing-dig-swing-dump cycle runs 25–35 s for a casual operator, under 20 s for a skilled one — the numbers the 1:3 ratio derivation in Chapter 5.2 is built on.
- **Travel:** walking speed is deliberately slow (~0.1 m/s class); an excavator walks perhaps 10 m in a whole Shift. Drive current is trivial; actuator current is intermittent 2–8 s bursts. Net pack draw per Shift: 25–40% of 2,000 mAh.

> **Field Note.** The V4 transmitter has an LCD with password lock and play-timer. Both are disabled fleet-wide — Shift timing lives in RC WORLD OS, not in the transmitter — but the 23-channel layout stays factory-standard on all six units so any transmitter binds to any excavator after an Artisan swap. Never let transmitter configs drift per machine; config drift is how a fleet quietly becomes six unique machines.

### 2.3 The premium tier: Kabolite 'Master Operator' experience

**Kabolite** is Huina's premium hydraulic marque (same Shantou industrial group, different engineering universe). Two models matter to this division:

| Parameter | Kabolite K336GC | Kabolite K970 (-100S / -100S Pro) |
|---|---|---|
| Prototype | CAT 336 GC replica | Flagship 1/14 hydraulic excavator |
| Scale / weight | 1/16, ~9.2 kg | 1/14, **31 kg**, 944 × 315 × 334 mm |
| Drive | Brushless motor, hydraulic pump + planetary travel drives | Brushless drive + brushless pump |
| Radio | 24-channel 2.4 GHz | 18-ch FlySky Paladin PL18 EV Lite touch-screen |
| Hydraulics | Entry hydraulic circuit | ~3.5 MPa working pressure, 6–8 MPa limit, cab pressure display, 6-way valve, quick-coupler (Pro adds powered-attachment contacts) |
| Battery | 7.4 V 10,000 mAh (~40–45 min) | 11.1 V 3S 15,000 mAh |
| Street price (verified July 2026) | ~$1,400–1,900 (MSRP $1,900) | Dealer/direct $6,500–9,000; Western retail to $10,500–12,500 (canon range) |
| Park role | Phase 2 candidate: second premium machine / technician trainer | **The Phase 1 premium showcase machine** |

The park's single premium machine is a **K970-class excavator**, and it carries three jobs: it is the **'Master Operator' experience** — a supervised, license-gated, one-on-one session at the premium pad ($22 Casual / $38 Operator, Artisan present throughout); it is the **display anchor** that makes the whole division legible ("that's what the real hydraulics feel like"); and it is the **top rung of the license ladder** — customers grind tonnage on the 1580 fleet partly to earn K970 seat time. The K336GC is the designated second premium machine if Master Operator occupancy sustains above 70% (growth trigger, Chapter 9.5): at ~$1,700 it adds a second supervised seat for a fifth of the flagship's capital, and doubles as the technician-education hydraulic trainer in Chapter 8.

For the competitive map: **LESU** (Aoue) builds 1/14 hydraulic excavators from roughly $2,000 (compact PC30-class) to $7,000+ (LR960-class) plus hydraulic backhoes and skid-steers; **JDModel** occupies the $2,500–6,000 hydraulic band with excavators and wheel loaders. Both are credible second sources for premium machines and hydraulic spares (Volume 8 carries them); neither competes with Huina 15xx economics in the rental tier — which is precisely the point of the two-tier doctrine.

### 2.4 Operator controls tutorial (staff teaching script)

The division teaches the **ISO excavator pattern**, matching the Huina factory layout, and the tutorial below is the standard 90-second station brief every first-timer receives. Artisans deliver it verbatim until it is muscle memory.

1. **Left stick.** Left/right = **slew** (turret swing). Up/down = **stick** (the middle arm): push away to reach out, pull back to curl in. "Push to reach, pull to bring home."
2. **Right stick.** Up/down = **boom**: pull back to raise, push to lower. Left/right = **bucket**: left curls (fills), right dumps. "Pull up, curl left, dump right."
3. **Tracks.** Two shoulder controls, one per track, like a tank. Both forward = drive straight. Opposite = pivot. Move the machine only when the marshal light is green.
4. **The dig cycle.** Boom down, stick out, bucket cut, curl, boom up, slew to the truck, dump *low over the bed* — spilled material is tonnage you don't get paid for.
5. **The golden rule.** Slow is smooth; smooth scores. Voltage-sag telemetry rewards smooth operators with longer effective allocations (F1-style power doctrine, Volume 9); jerky sticks drain the allocation and dent the smoothness index.

Skill progression from this baseline — two-function blending, grading with the bucket back, trench walls — is packaged into the badge tasks of Chapter 11.5.

---

## 3. Bulldozers & Graders

### 3.1 Fleet dozers: Huina 1554/1569 class

The dozer class is deliberately light: two machines, both 1/16, both cheap, charming and expendable — the entry drug of the whole division, issued mostly to children.

| Parameter | Huina 1554 | Huina 1569 |
|---|---|---|
| Scale / build | 1/16, ABS body, ~350 mm | 1/16, semi-metal, heavier blade gear |
| Functions | 11-function, proportional blade lift/tilt, rear ripper | 8-channel, blade + rear scarifier |
| Runtime | 40–50 min on 7.4 V pack | ~35–40 min |
| Street price (2026) | ~$100–130 retail; wholesale $45–70 | ~$110–150 retail; wholesale $60–90 |
| Duty rating | RD-1 | RD-1 |

Park units receive an Artisan-fitted aluminium blade wear-edge and a metal-gear service pack at first refurbishment (Chapter 12); blade edges on ABS machines are the first thing the Mining Zone's crushed-stone areas eat.

### 3.2 Blade control as a taught skill

Dozer work is one control dimension harder than it looks, and the division teaches it as such: **the blade is a metering device, not a shovel**. The station brief teaches three moves — *carry* (blade just above grade, walking material forward), *cut* (blade 5–10 mm into loose material, short passes), and *back-blade* (reverse with blade floated to dress a surface flat). Children discover within minutes that a full blade stalls the tracks; the machine itself teaches load management, which is exactly the sort of embedded lesson the simulation-of-work format sells.

### 3.3 Haul-road maintenance duty — dozers as track-grooming assets

The dozers are not just toys with jobs; they are **rostered grooming assets**. Between customer waves and at close, Artisans use them for spill-drift back-blading in the dozer boxes and along haul-road shoulders — work that is deliberately performed in public view, because a staff machine visibly working the site reads as authenticity and reliably triggers "what is it doing?" conversations that convert into license-program interest. The heavy grooming (crown re-dressing, berm repair) belongs to the service wheel loader (Chapter 4.3); the dozers handle the fine work between waves. This dual duty is why the PM matrix (Chapter 12.2) gives two RD-1 machines a weekly track-tension check normally reserved for higher-duty assets.

### 3.4 Graders — the honest gap

As of July 2026 **no mass-market grader exists in the Huina rental class**; 1/14 motor graders are boutique hydraulic builds (LESU/JDModel custom territory, typically $3,000–5,000 landed). The division therefore carries no rentable grader, and this volume says so plainly rather than padding the catalogue. Haul-road grading is performed by the service-duty 1583 wheel loader wearing a straight-blade attachment fabricated in The Works for roughly $40 of aluminium (drawing in Volume 7). A display-grade hydraulic grader enters the wish list only in Phase 3, and only after the premium program saturates — it is a want, not a need.

> **Trade Hack.** The loader's fabricated grading blade is drilled to the same pin pattern as its bucket, so blade-for-bucket swaps take under two minutes. Any attachment The Works fabricates for the division must use the standard pin pattern — one machine, many tools, zero adapters. Volume 7 carries the pattern drawing.

---

## 4. Wheel Loaders

### 4.1 Huina 1583 class

| Parameter | Huina 1583 (2026 model) |
|---|---|
| Scale / layout | 1/14 articulated wheel loader, die-cast alloy + ABS, ~570 mm long |
| Channels | 10; proportional bucket; 2.4 GHz, ~30 m range |
| Capability | Carries up to ~10 kg over the front axle; push force ~1.5 kg; weight ~4.6–5 kg |
| Battery / runtime | 7.4 V 2,000 mAh, ~40–45 min |
| Street price (2026) | $285–320 retail; wholesale **$180–220** |
| Duty rating | RD-2 (rental, license-gated) and SD (one unit reserved for service) |

Fleet count: **3** (canon). Two rentable, one permanently assigned to grooming and hopper-apron duty. The loader is gated behind the second license tier because an articulated machine that can carry 10 kg can genuinely hurt a finger — it is the strongest machine in the rental pool, and the only rental machine whose issue requires either a license tier or a staff spot-check.

### 4.2 The hopper-loading cycle and bucket technique

The loader's core gameplay is the **V-cycle**, taught exactly as real operators run it: approach the stockpile square, bucket flat on the ground; drive in until the wheels just begin to slip; **crowd** (curl) the bucket while lifting slightly — curling while stationary is what fills a bucket, pushing harder is what spins tires; reverse out along one leg of the V; steer to the truck or hopper along the other leg; dump low and centred. Score-relevant technique points, which the telemetry smoothness index and marshal spot-scoring both reward:

- **Fill factor:** a properly crowded bucket carries 300–500 g of sand; a flat-pushed one carries half that and spills on articulation.
- **The articulation trap:** an articulated frame mid-turn with a raised loaded bucket is the least stable state in the whole rental fleet. The taught rule is *"low and level until lined up"* — bucket below axle height except during the final approach.
- **Apron discipline:** at the hopper the loader gives way to trucks (trucks are on the billing clock of other customers; the loader isn't).

### 4.3 The service loader

The SD-assigned 1583 — with the fabricated straight blade and a screen bucket — is the zone's groundskeeper: haul-road crown dressing, berm repair to the 60 mm gauge, spill reclaim on the apron, stockpile management, and re-segregation of mixed aggregates (sand back to sand faces, pea gravel back to the coarse faces) during nightly grooming (SOP-CD-004, Chapter 6.6). One machine, roughly 90 minutes of Artisan operation per day, keeps the entire circuit within spec — the cheapest site-maintenance department in the amusement industry.

---

## 5. Dump Trucks & Haul Logistics

### 5.1 The circulation fleet: Huina 1582 / 1573

Eighteen trucks — the largest single machine population in the park — sized by the 1:3 ratio against six excavators. Two models share the pool deliberately:

| Parameter | Huina 1582 | Huina 1573 |
|---|---|---|
| Scale / layout | 1/14 rigid dump truck, alloy cab, metal tipping bed and linkage | 1/14 rigid dump truck, ABS-dominant, metal bed floor |
| Channels | 10 (drive, steer, tip, lights, sound) | 10 |
| Working payload | ~4 kg per load (self-tips at 4 kg; chassis rated well above) | ~3 kg working; self-tips ~4 kg max |
| Dimensions / weight | ~450 × 150 × 190 mm; ~3.6–7 kg depending on trim | ~450 × 140 × 190 mm; ~3.2–3.6 kg |
| Battery / runtime | 7.4 V (park: 2S LiPo XT60 pool), ~30–45 min | 7.2 V stock (park-converted to pool standard), ~30 min |
| Street price (2026) | ~$200–300 retail; wholesale **$150–200** | ~$165 retail; wholesale $120–160 |
| Duty rating | RD-1 | RD-1 |

Fleet split: **12 × 1582 + 6 × 1573**. The 1573s are the training haulers issued to younger children and absorb the roughest treatment; the 1582s are the production fleet whose bed geometry is correctly scaled to receive a 1580 bucket pass — the bucket drops between the bed rails with ~15 mm clearance per side, which is what makes clean loading a learnable skill rather than a lottery.

### 5.2 The 1:3 ratio, derived

The canonical **excavator : dump truck = 1 : 3** ratio is elementary queueing arithmetic applied to the physical circuit, and every future fleet decision must survive this derivation. Measured cycle elements (pilot testing on the Chapter 10 geometry, rounded conservative):

| Circuit element | Time |
|---|---|
| Excavator loads one truck (4–6 bucket passes at 25–35 s) | ~2.5–3.0 min |
| Loaded haul to hopper (~45 m at scale speed, incl. 14° ramp) | ~1.5 min |
| Queue + tip at hopper + weigh | ~1.0 min |
| Empty return | ~1.5 min |
| **Truck away-time per cycle (excluding loading)** | **~4.0 min** |

An excavator can start loading a new truck every ~3 minutes. Each truck is away ~4 minutes per cycle. Trucks required for continuous face service:

> N = (loading interval + away time) ÷ loading interval = (3 + 4) ÷ 3 ≈ **2.3 → round to 3**

Round *up*, because customers are supposed to be having fun, not hitting takt time: human variance, spillage stops and photo pauses all inflate away-time. With **two** trucks the excavator operator stands idle waiting for a bed — the most expensive boredom in the division, since the excavator seat is the experience most customers came for. With **four** trucks they stack at the face, which reads as congestion and invites bumper-car behaviour. Three keeps every seat busy and every queue short. Fleet-wide: 6 excavators × 3 = **18 trucks**, canon.

### 5.3 Worked utilization calculation — payload per Shift

The arithmetic every capacity claim in Chapter 9 hangs from. Assume one **pod** (1 excavator + 3 trucks, four customers) running a casual-pace 20-minute Shift:

- Truck cycle time = loading (3.0 min) + away (4.0 min) = **7.0 min** → each truck completes **2–3 cycles per Shift** (2.86 theoretical; call it 2.5 with start/stop losses).
- Payload per cycle ≈ 3.5 kg blended (1582s at ~4 kg, 1573s at ~3 kg).
- **Per truck per Shift: ~8.5–10.5 kg. Per pod per Shift: ~26–31 kg through the hopper.**
- Excavator-side check: 2.5 truckloads × 3 trucks = 7.5 loads × ~5 bucket passes = ~38 bucket cycles in 20 min — one pass every ~32 s. Consistent with the observed casual cycle time; the circuit is balanced, with the excavator as the governing resource exactly as a real pit is planned.
- Skilled-pace ceiling (competition data, Chapter 11.3): ~20 kg in 11 minutes for a two-person team — roughly double casual throughput, which is the headroom that makes timed contests meaningful.

Utilization ratio: at casual pace the excavator is loading ~85% of the Shift, each truck is moving ~90% — no seat spends more than a couple of minutes waiting. That number *is* the product; guard it.

### 5.4 Haul-road design standard

The haul roads are the division's civil signature, built like real ones at 1/14:

- **Maximum incline 15° — canonical, and engineering-derived.** Brushed 540-class drive motors hauling a loaded 1582 sustain 14–15° indefinitely; beyond that, stall-current heating climbs steeply and continuous duty burns motors. All built ramps run **14°** (rising 1.0 m over 4.0 m of run) to leave margin under the canon ceiling. Grades are constant-slope — no roller-coaster profiles that shock-load gearboxes — with 300 mm vertical curves top and bottom.
- **Width for passing.** A 1/14 hauler is ~150 mm wide. Single-lane running width = 3 vehicle widths = 450 mm; the main loop is **two-lane, 900 mm formed width**, so a bogged or dawdling truck never blocks the circuit. Ramps stay two-lane; only the final hopper-apron approach necks to marshalled single-lane.
- **Berms.** Continuous compacted windrows, **60 mm high** (~40% of truck wheel height; real mines use 50% — ours is slightly under so the recovery crawler can climb them), on every edge with a drop over 100 mm. Berms passively absorb the highest-frequency customer error — drifting off-edge — with zero damage.
- **Surface.** 40 mm of compacted ≤10 mm crushed stone over geotextile, crowned 2% to shed water inward to the drain. The service loader re-dresses the crown weekly. Dig faces are loose sand; roads are never sand — the full surface-grade map from loose sand to 10 mm crushed stone is Chapter 6.4.
- **Circulation.** One-way, counter-clockwise. One-way running halves child-driver conflicts and is non-negotiable; painted arrows every 2 m and a give-way line at the apron are part of the nightly grooming checklist.

### 5.5 Payload cycles per Shift — the customer-facing number

Marketing and the app express hauling in honest, physical numbers: a Casual Shift in a 1582 moves **~10 kg through the hopper in 2–3 deliveries**; an Operator Shift (two blocks with a pit-stop battery swap) moves ~20–22 kg in 5–6. Career tonnage accumulates from exactly these weighed deliveries (±20 g load-cell resolution, Chapter 6.5) — no estimates, no inflation. The division's unit of progress is the kilogram, and the hopper is its notary.

> **Field Note.** Resist the temptation to "help" small children by overfilling their trucks at the face. An overloaded 1573 on the 14° ramp is the single most common motor-heat event in the fleet. The excavator brief teaches four passes for a 1573, five for a 1582 — counting passes is load discipline made child-legible.

---

## 6. The Mining Fleet System

### 6.1 Open-pit simulation: how the system reads

The Mining Zone must read, at first sight and from 40 m away, as a *working mine*: benches, haul roads, a headwall, a hopper with a conveyor, controlled dust in the light. This chapter specifies the production system — benches, hopper, material loop, medium management; the civil dimensions and safety architecture around it are Chapter 10.

### 6.2 Bench levels and pit-floor rotation

The pit is cut as a real open-pit in miniature, two benches deep:

- **Upper bench** at −300 mm below site datum; **lower pit floor** at −600 mm, connected by the in-pit ramp. Bench heights match the 1580's ~150–200 mm effective dig depth so a machine on each level always has a workable face below its tracks.
- **Six dig faces (DF1–DF6)**, each 3 m wide, cut into the bench walls directly below their assigned operator stations, with a marked truck spot beside each. Faces hold a 30–40° angle in the moist-sand spec and are re-cut nightly to the template so every morning presents fresh, diggable material with 150–250 mm of loose won material heaped at the toe — first-minute success for the day's first customers is a designed property, not luck.
- **Pit-floor rotation.** Faces retreat as customers dig. On a ~2-week cadence the active face set rotates around the pit walls: as DF1–DF3 approach their retreat limit (500 mm from the bench crest guard line), grooming shifts new cuts to the rested wall sections and the loader backfills the worked-out faces from the stockpile. Rotation keeps every face inside its station's sight line, evens wear on the pit geometry, and means the pit *visibly changes* week to week — regulars notice, and noticing is retention.

### 6.3 Central hopper metering

The hopper is scenography, scoring system and traffic anchor in one structure — a functional scale plant, not a prop:

- **Receiving grizzly:** 600 × 600 mm steel bar grate at apron level, 20 mm bar spacing — passes all aggregate grades, stops buckets, phones and hands — over a 0.15 m³ surge bin.
- **Weighing:** the surge bin hangs on four 50 kg load cells (HX711-class amplifiers into an ESP32 on the park mesh). Every tip is weighed to **±20 g** and credited within ~2 s to the delivering customer via the truck's Heavy-Node identity. This is the tonnage leaderboard's ground truth and the settlement layer for every competition in Chapter 11.
- **Metering conveyor:** a 2.5 m inclined belt (200 mm belt, geared 24 V motor, variable 0.1–0.3 m/s) lifts weighed material to the stockpile discharge at +1.4 m. Belt speed is the system's metering valve: run slow on quiet days so the stockpile grows theatrically; run fast ahead of grooming so the surge bin is empty at close.
- **Traffic control:** a stack light (green = accepting, amber = weighing, red = locked out) doubles as apron queue control. Lockout is a captive-key system — the conveyor cannot run while the bin access panel is open (Chapter 10.4).

Build cost ≈ $6,000–9,000 including load cells, conveyor drive and corrugated cladding, fabricated in The Works to Volume 7 drawings.

### 6.4 Aggregate grades — the designed medium

The dig medium is a material system, not "sand." Three grades in mapped areas, spanning the canonical range from loose sand to 10 mm crushed stone, each selected on the tension between diggability at 1/14 breakout forces, dust, and drainage:

| Material | Spec | Where | Why |
|---|---|---|---|
| Washed coarse sand | 0–2 mm, <3% fines, kept slightly moist | Dig faces DF1–DF4, dozer boxes, tillage fields (Ch. 7) | Best bucket penetration and heap behaviour; washed spec kills airborne dust; holds a 35° face overnight |
| Pea gravel | 5–8 mm rounded | DF5–DF6 ("hard rock" faces), hopper surge bed | Satisfying rattle-and-pour physics for skilled operators; free-draining; too coarse to blow as dust |
| Crushed stone | ≤10 mm angular, compacted | Haul roads, ramps, aprons — structure, never dig medium | Interlocks under compaction into a firm running surface; the canon ceiling grade |

Total initial fill ≈ 55 m³ (sand 30, pea 10, crushed 15), ≈ $2,200–3,500 delivered in most markets — among the cheapest attraction surfaces per square metre in the industry, and (unlike track asphalt) infinitely repairable with a loader.

### 6.5 The material recirculation loop

The zone's material cycle is **closed and visibly honest** — nothing is trucked in or out after commissioning:

1. Customers dig sand/pea from the faces and haul it to the hopper.
2. The hopper weighs it and the conveyor lifts it onto the **conical stockpile** — the zone's growing "product" landmark.
3. When the stockpile passes its 0.5 m³ mark, the service loader reclaims it and carries it back to the worked-out faces per the material map (sand to sand faces, pea to pea faces — the screen bucket re-segregates any mixing).
4. Nightly grooming re-cuts the replenished faces to template.

One loop, roughly 1.5 t of material in perpetual rotation, driven entirely by customer labour plus ~30 minutes of loader time per day. Spillage is the loop's only leak: drifts on the apron and haul loop are reclaimed nightly to their source areas so the grade map stays true.

### 6.6 Dust and moisture management of the medium

Moisture is a tool, and the sand faces run best at **4–6% moisture** — dark, cohesive, dust-free, holding clean vertical cuts like real ground. Controls, in order of importance:

1. **Washed aggregate spec** (<3% fines) — the structural fix; dust you never buy is dust you never breathe.
2. **Nightly misting pass** to 4–6% (dark and cohesive, no standing water), verified each morning by the opening test: *a face must hold a bucket-cut without slumping*. Bone-dry sand is the mark of lazy grooming — it digs worse, scores worse and coats every machine in fines.
3. **Hopper misting ring** — a hose-end ring on the surge bin, because tipping is the dustiest event in the zone.
4. **Hard rule:** the compressed-air blow-down gun lives in The Works, never in the zone. Blowing a machine down in the pit just relocates fines into the next machine's bearings.

**SOP-CD-004 — Mining Zone Nightly Re-Grooming**
**SOP ID:** SOP-CD-004 · **Rev:** 1.0 · **Owner:** Construction Division Lead · **PPE:** gloves, safety glasses, dust mask during dry raking · **Tools:** SD loader + blade/screen bucket, landscape rake, misting hose, face-cut template board, torque driver · **Frequency:** nightly at close, 40–55 min, 2 staff

1. Confirm zone clear; close marshal gate; hopper stack light to red; apply conveyor captive-key lockout.
2. Sweep the pit for foreign objects (dropped items, track pins, bucket teeth); log any fleet hardware found against the day's machine roster.
3. Loader pass 1: reclaim spill drifts from apron and haul loop to their source material areas (screen bucket where grades have mixed).
4. Loader pass 2: re-dress haul-road crown; repair berms to the 60 mm gauge board; refresh one-way arrows if scuffed.
5. Re-cut all six faces to template: 30–40° face angle, 150–250 mm loose toe heap; advance the face-rotation plan if any face is at its retreat limit.
6. Reclaim stockpile above the 0.5 m³ mark back to faces per the material map.
7. Misting pass on all sand areas to 4–6% moisture.
8. Hopper: empty and brush the surge bin; verify load-cell zero (±50 g); torque-check grizzly bolts (weekly, logged).
9. Rake operator rim and spectator terrace; empty station bins; walk the drainage sump and clear debris.
10. Log completion in RC WORLD OS grooming register with photos of DF1–DF6; lockout key stays pocketed until the morning opening checklist releases it.

---

## 7. The Agriculture Zone

### 7.1 Concept

The Agriculture Zone is the Mining Zone's calmer sibling: **1,500 m² (50 m × 30 m)** modelled on a commercial tobacco/maize operation per the founder's notes — *fields, not gardens*. Where mining sells production, agriculture sells **husbandry**: plowing a straight furrow, discing a field to even tilth, threading a tandem trailer between crop rows without shedding the load. It is the division's best fit for younger children, its best photographic contrast (green rows against the pit's ochre), and home of the park's most distinctive seasonal event, the Harvest Campaign.

### 7.2 The tractor fleet: Double E E351 class

| Parameter | Double E E351 (E351-003), park-spec |
|---|---|
| Scale / build | 1/16, ABS body, ~375 × 170 × 210 mm, ~1.1 kg stock |
| Drive | Rear-wheel drive stock; park units upgraded to 4WD-motor spec where available, high-torque gearing |
| Radio | 2.4 GHz, proportional drive/steer; horn, engine sound, lights; controls compatible powered accessories via rear data socket |
| Battery | Stock 4.8 V 300 mAh NiCd — **replaced fleet-wide** with 2S-compatible park packs and XT60 during prep (the single most important prep step; stock packs would die mid-Shift) |
| Street price (2026) | $50–90 retail; **park landed cost $80–120** each including battery conversion, standard hitch, Heavy-Node fitment |
| Duty rating | RD-1 (tandem trailers RD-2) |

Fleet count: **12** (canon). Why the E351 wins the seat: it is the only widely available 1/16 RC tractor with a powered-accessory ecosystem (tipping trailer, tedder) at a toy-grade price, and its market saturation means bodies, wheels and gearboxes are perpetually cheap. The German alternative — **Siku Control** (Fendt/John Deere/Claas, €99–172 retail, superb detail) — runs at 1:32 scale in its RC line, too small for outdoor field work and incompatible with the park's 1/16 implement library; it is noted for the retail shop (Volume 8), not the fleet.

### 7.3 The implement library

Tractors are the platform; implements are the content. Every tractor is fitted at The Works with the park-standard **pin hitch** (3 mm clevis pin on a 20 mm plate) so every implement fits every tractor. The library (~20 pieces, $15–60 each wholesale, several shop-fabricated to Volume 7 drawings):

| Implement | Qty | Function | Gameplay |
|---|---|---|---|
| Single/dual-bottom plow | 4 | Cuts real furrows in tillage fields | Straightness scored against chalk line |
| Disc harrow | 3 | Breaks furrows to tilth | Coverage scoring (photo overlay) |
| Tipping trailer (single-axle) | 5 | Haulage to the barn | Load/deliver cycles, weighed |
| Tandem trailer set | 2 | Advanced haulage (canon: tandem trailers) | RD-2, license-gated; a jackknife is a retrieval event |
| Water bowser | 2 | Fills at the irrigation valve, wets fields | Staff grooming + campaign use |
| Bale/crop flatbed | 2 | Carries crop tokens | Harvest Campaign core |
| Front blade (loader-arm fit) | 2 | Lane dressing | Staff grooming + skill badge task |
| Rake/tedder (Double E powered accessory) | 2 | Row dressing, campaign theatre | Powered via tractor data socket |

### 7.4 Field grid layout

The zone is a grid of **eight field cells, each 9 m × 5.5 m**, separated by 600 mm compacted access lanes, with the barn/silo complex on the east edge:

- **F1–F4 — tillage fields:** 100 mm depth of the same washed 0–2 mm sand as the pit (one aggregate supply chain, deliberate), held at 4–6% moisture, re-groomed flat nightly so morning customers cut first furrows into clean ground.
- **F5–F6 — row-crop fields:** permanent simulated crop rows at 250 mm spacing. Row materials (durability-tested against 1/16 wheel strikes): UV-stable artificial boxwood strip for "young maize"; bundled natural-look raffia in drilled timber battens for mature tobacco/maize — convincing at spectator distance, replaceable in 1 m sections. Between-row lanes are exactly 1.4 tractor widths: threading them clean is the zone's core skill.
- **F7–F8 — harvest/haul fields:** where campaigns stage crop tokens.
- **Irrigation trenches:** 150 mm wide × 80 mm deep formed channels along the grid spines — dry by default, hose-flooded for events — crossed by four single-tractor timber culvert bridges. The trenches are working scenery: a wheel dropped into one is a taught recovery lesson, not a design flaw.
- **Barn & silo:** a 2.4 m × 1.8 m scale barn with a drive-through **weighbridge bay** (same HX711 load-cell architecture as the mining hopper, 20 kg cells) and a silo tower deliveries are credited against. Same scoring backbone as mining, gentler physics.
- **Operator line:** six stations along the south edge, built to the same rail/shade/sight-line standard as the mining rim (Chapter 10.3); the whole grid is visible from every station.

### 7.5 Crop-row simulation and task cards

A standard Agriculture Shift issues a tractor plus one implement chosen at booking. The marshal assigns a field cell and a **task card**: *plow F2 north–south*, *disc F3 to full coverage*, *haul six trailer loads from F7 to the barn*. Completion, straightness scores and delivered weights post to the customer profile exactly like mining tonnage. The zone runs 8 concurrent customers comfortably (6 field tasks + 2 haul circuits) against 12 tractors — the same ~33% rotation reserve as the pit.

### 7.6 Seasonal Harvest Campaign events

Twice a year (spring planting, autumn harvest; inverted for southern-hemisphere deployments) the zone runs a two-week **Harvest Campaign**: F5–F8 are dressed with crop tokens — weighted 40 mm "maize bundle" and "tobacco bale" pucks, ~200 g each, RFID-tagged — and every Shift's deliveries accrue to a park-wide campaign total on a public silo-gauge display. Individual contributions earn campaign badges (Volume 9); the finale weekend crowns a Harvest Champion per age class. Token set cost ≈ $400 per campaign; comparable seasonal-event benchmarks reliably show a campaign fortnight doubling zone utilization, making this the cheapest utilization lever in the volume.

> **Field Note.** The Agriculture Zone is the park's birthday-party engine. A tractor is the machine parents trust a six-year-old with unsupervised-feeling (it isn't — geofenced, marshalled, 10 km/h scale speed), and eight children on eight tractors with task cards is a self-running party format. Book parties into agriculture by default; upsell the pit for the second visit.

---

## 8. Hydraulics Deep-Dive

This chapter serves two audiences: the Artisans who maintain the premium tier, and the technician-education program (Volume 7) that uses the K336GC trainer to teach fluid power. Even though only one Phase 1 machine is hydraulic, every heavy-fleet Artisan must understand the system — the K970 is the division's most expensive asset, its most fragile revenue line, and the machine most closely examined by exactly the customers whose opinions travel furthest.

### 8.1 Anatomy of a 1/14 hydraulic system

A scale hydraulic machine is a real hydraulic machine with the decimal point moved. The K970-class circuit contains every element of a full-size excavator's:

1. **Reservoir.** ~200–400 ml of hydraulic oil in the counterweight area, with filler, sight window and coarse suction strainer. Miniature tanks are proportionally *smaller* relative to flow than full-size tanks, so the oil works harder and runs hotter per millilitre — the root cause of half the maintenance schedule below.
2. **Pump.** A miniature **gear pump** — two hardened steel gears meshing in a machined housing — driven by a **brushless motor** with its own ESC. Gear pumps dominate the scale world: simple, flat efficiency curve, dirt-tolerant relative to piston pumps. Representative aftermarket spec (LESU-class, 2026): housings rated ~10 MPa, flow ~400 ml/min, relief mandatory well below rating. The pump motor is the "engine": the operator hears it load up under digging effort, which is a large part of the sensory magic customers pay premium rates for.
3. **Relief valve.** Spring-loaded bypass that caps system pressure — the component that decides whether a stalled cylinder is "realistic engine lug" or "burst hose." Set at commissioning, verified at every fluid change (SOP-CD-003).
4. **Directional valve block.** A bank of miniature spool valves — the K970 runs a **6-way block** — each spool shifted by a micro servo. Proportionality comes from spool position: the servo meters *flow*, so stick finesse translates directly into cylinder speed. This servo-on-spool architecture is why hydraulic machines feel alive.
5. **Cylinders.** Honed-tube rams with NBR piston seals (often PTFE backup) and rod wipers. Bores in 1/14 run 8–16 mm: a 12 mm bore at 20 bar develops ~23 kgf of rod force — how a 31 kg model genuinely digs compacted ground.
6. **Hose and hard line.** 3–4 mm OD nylon/polyurethane tube with brass compression or push-fit fittings; braided scale-appearance hose on premium boom sets.
7. **Instrumentation.** The K970 carries an in-cab display showing pressure, oil temperature and system voltage — the single most useful diagnostic on the machine and the anchor of the weekly health check.

### 8.2 Operating pressures and the two real enemies

Verified factory figures for the K970-100S: **~3.5 MPa (35 bar) working pressure, 6–8 MPa limit pressure**, ~80 kg track thrust, 60 kg-class slew torque. For intuition: 35 bar is about fifteen times road-bicycle tire pressure, delivered through hoses the diameter of spaghetti. Two engineering consequences dominate:

- **Heat, not pressure, is the enemy.** With a healthy relief valve nothing bursts; instead, sustained relief bypass (an operator holding a function against its stop) converts full pump power into oil heat. A 40-minute enthusiastic session can lift tank temperature 20–25 °C over ambient; above ~60 °C viscosity collapses, internal leakage rises and seals age fast. The Master Operator supervision script therefore teaches customers to **feather off at end-of-stroke** — a genuine operator skill that also protects the machine.
- **Cleanliness is everything.** Pump gears run micron-scale clearances; one grain of the zone's own 0–2 mm sand inside the circuit scores the pump in minutes. This is the engineering core of the premium doctrine: the K970 works the *same dirt* as the rental fleet, but with an Artisan present whose job is partly to keep the filler cap, quick-coupler and rod wipers clean.

### 8.3 Fluid selection

Scale-hydraulic OEMs (Kabolite's own manuals included) standardize on **ISO VG 32 anti-wear hydraulic oil**, stepping to **ISO VG 46** in sustained hot climates (tank temps >55 °C). Absolute prohibitions, posted on the workshop wall: **never brake fluid** (glycol swells NBR seals), **never motor oil** (detergent packages foam and corrode), **never silicone shock oil** (wrong lubricity; wrecks pump gears). RC WORLD stocks VG 32 in 1 L bottles dyed with a trace of red tracer so any drop on a machine or the pit floor is instantly attributable.

> **Trade Hack.** Keep a white ceramic tile in the K970's parking bay and park the machine over it every night. A red-tinged drop on the tile at morning inspection localizes a developing leak *before* the reservoir level moves — the sight glass is a lagging indicator; the tile is a leading one.

### 8.4 Common leak points

Every hydraulic machine leaks eventually; the discipline is making leaks *scheduled events* rather than surprises. The leak hierarchy, in descending frequency across the scale-hydraulics community:

| Leak site | Cause | Fix | Typical interval |
|---|---|---|---|
| Cylinder rod seal | Rod wiper wear, dust ingestion | Seal kit ($8–15/cylinder), 30-min bench job | 150–300 run-hours |
| Hose push-fit fitting | Vibration walk-out, heat cycling | Re-cut tube end, re-seat; replace tube at every 2nd service | 100–200 h |
| Valve spool O-rings | Heat aging | Spool seal kit | 300–500 h |
| Pump shaft seal | Normal wear | Pump rebuild/swap ($120–180) | 400–600 h |
| Tank filler / gauge threads | Over-torque, missing PTFE tape | Re-tape, torque to spec | Commissioning errors only |

Leak doctrine: any visible external leak takes the machine out of service immediately (`fleet_inventory` status → `maintenance`). At 200–400 ml total charge, a "small" leak is a large fraction of the system, and a starved gear pump destroys itself in minutes.

### 8.5 Bleeding procedure and fluid change

**SOP-CD-003 — Hydraulic Fluid Change & Air Bleed (Premium Fleet)**
**SOP ID:** SOP-CD-003 · **Rev:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** nitrile gloves, safety glasses · **Tools:** dyed ISO VG 32, catch tray, extraction syringe/filler bottle, lint-free wipes, IPA, PTFE tape, torque driver, fresh leak tile · **Frequency:** 100 run-hours or 6 months, and after any contamination event

1. Run the machine 5 minutes at light load to warm the oil and suspend contaminants; park over the catch tray; power off; transmitter secured by the Artisan.
2. Photograph the in-cab gauge at idle (pressure reference for post-change comparison).
3. **Clean the filler area before opening** — the filler neck is the contamination gateway; this step is the SOP's soul.
4. Drain/extract the reservoir into the catch tray. Inspect against the reference vial: darkening = normal aging; milkiness = water ingress (find it — check rod wipers and filler seal); glitter = metal — **stop and escalate** to pump inspection before any refill.
5. Extend all cylinders fully to push residual oil back to tank; extract again. Do not full-system flush unless contamination was found — over-servicing opens more entry points than it closes.
6. Clean the suction strainer; replace the breather element if fitted.
7. Refill to the sight-window line; run the pump at idle 60 s; then **bleed**: cycle every function slowly to both stops, twice, in circuit order (boom → stick → bucket → auxiliary). Spongy or juddering motion = air remaining; repeat the slow cycles and re-top the tank (the purged air's volume is replaced by oil).
8. Verify idle and relief pressures against the step-2 photo (±10%); investigate any relief drift before release.
9. Wipe down; new leak tile; dispose of waste oil per the park environmental procedure (Volume 11); log volumes and condition to `maintenance_logs`.

### 8.6 Maintenance schedule — Kabolite-class machines

| Interval | Task |
|---|---|
| Every session | Rod wipe-down; visual hose scan; quick-coupler cleaned and capped; park over leak tile |
| Daily (open) | Reservoir level at sight window; gauge sanity check (idle + relief); cycle all functions gently to stops once |
| Weekly | Log tank temperature after last session; torque scan on valve block and cylinder clevises; track tension (SOP-CD-001) |
| Monthly | Oil condition vs reference vial; strainer inspection; servo-linkage wear check on all spools |
| 100 run-hours / 6 months | Full fluid change + bleed (SOP-CD-003); rod-seal inspection; relief setting verified |
| Annually | Pump flow test (timed full-stroke vs commissioning baseline; >20% slowdown = pump rebuild); full boom hose-set replacement |

### 8.7 Why hydraulics stay out of the rental fleet — the math

The doctrine, now in numbers rather than principle. Compare one rental-duty year (assume 600 Shifts/year/machine at Year 2 volumes) for a hypothetical hydraulic rental against a 1580:

| Line | Huina 1580 (electromech.) | Hydraulic machine on rental duty |
|---|---|---|
| Capital landed | ~$500 | ~$8,000 (K970-class) — or ~$2,000 even for a K336GC |
| Consumable failure, typical | $1 micro-switch, $6 gear set | $12 seal kit + oil, $150 pump events |
| Maintenance cost/Shift (observed class data) | $0.50–0.90 | $3–6 conservatively, before pump events |
| Turnaround between customers | < 5 min (none needed beyond battery logic) | 5–10 min rod-wipe/level/temp check *every session* |
| Downtime per major failure | 20–45 min (shelf parts) | Days (seal kits, pump parts, oil flush) |
| Annual maintenance @600 Shifts | ~$400 | ~$2,500–4,000 + one pump event likely |
| Capital + Year 1 maintenance at risk | ~$900 | ~$11,000+ |

An 18× capital-at-risk gap and a 5–7× maintenance-per-Shift gap, for an experience difference most casual customers cannot articulate past "it sounds cooler." The premium format captures that difference honestly instead: the customer who *can* articulate it pays $22–38 for a supervised session, the Artisan's presence protects the machine, and scarcity does the marketing. This table is the division's constitutional law; any future proposal to rent hydraulic machines unsupervised must first defeat it in writing.

---

## 9. Fleet Planning & Capacity

### 9.1 Canonical fleet table

Duty ratings: **RD-1** rental unrestricted · **RD-2** rental, license-gated · **PD** premium/display, supervised · **SD** service/staff only.

| Class | Model | Scale | Actuation | Count | Wholesale each | Fleet line | Duty |
|---|---|---|---|---|---|---|---|
| Excavator | Huina 1580 V4 | 1/14 | Electromechanical (lead-screw) | 6 | $350–420 | ~$2,300 | RD-1 |
| Dump truck | Huina 1582 | 1/14 | Electromechanical | 12 | $150–200 | ~$2,100 | RD-1 |
| Dump truck | Huina 1573 | 1/14 | Electromechanical | 6 | $120–160 | ~$850 | RD-1 |
| Wheel loader | Huina 1583 | 1/14 | Electromechanical | 3 | $180–220 | ~$600 | RD-2 / SD |
| Dozer | Huina 1554/1569 class | 1/16 | Electromechanical | 2 | $45–90 | ~$150 | RD-1 |
| Premium showcase | Kabolite K970 class | 1/14 | **Hydraulic** (brushless pump) | 1 | $6,500–9,000 direct ($10.5–12.5k Western retail) | ~$8,000 | PD |
| **Mining subtotal** | | | | **30** | | **~$14,000** | |
| Tractor | Double E E351 class | 1/16 | Electromechanical | 12 | $80–120 | ~$1,200 | RD-1 |
| Implement library | Plows, discs, trailers, rakes | 1/16 | Towed / data-socket powered | ~20 pcs | $15–60 | ~$700 | — |
| **Division total** | | | | **42 powered** | | **~$15,900** | |

Spares provisioning on top — one "ghost machine" of high-turnover parts per six fleet units — is specified in Chapter 12.4 and priced in Volume 8.

### 9.2 Session capacity per zone per hour

Definitions: Shift = 20 min; turnaround (transmitter hand-off, battery decision, staging) budgeted 5 min → **2.4 sellable Shifts/seat/hour**.

| Zone | Concurrent customer seats (peak config) | Shifts/hour | Shifts/day (10 h) |
|---|---|---|---|
| Mining — standard | 16 (4 pods: 4 excavators + 12 trucks) + 2 loader/dozer seats = 18 | ~43 | ~430 |
| Mining — premium pad | 1 (supervised) | max 2, practical 1 (cool-down) | 4–8 offered slots |
| Agriculture | 8 (6 field tasks + 2 haul circuits) | ~19 | ~190 |
| **Division ceiling** | **27 seats** | **~62–64** | **~620** |

The reserve (2 excavators, 6 trucks, 4 tractors, 1 loader) is not idle capital: it is the 33% rotation pool that absorbs battery swaps, PM slots and defects without a visible hole in the circuit.

### 9.3 Utilization targets and the worked revenue check

Blended reality against theoretical ceiling, consistent with Volume 10's Year 1 canon (≈$1.28 M park revenue):

- **Year 1 target: ~1.75 paid Shifts/machine/day blended** across the 360-day year (weekday daytime is school time); **Year 2: 3.0** as leagues and memberships build weekday base load.
- Effective revenue per block at canon pricing ($15 Casual / $26 Operator, Operator ≈ 25% of sales at $13/block): ~$14.50.
- **Standard fleet (41 machines): 1.75 × $14.50 × 360 ≈ $9,100/machine/year → ~$375,000.** Realistically discounted for the tractor fleet's child-heavy pricing mix: **$330–380k**.
- **Premium K970:** 3–5 sold sessions/day at $22–38 → $90–150/day → **$35–50k/year** — from one machine, matching roughly a tenth of the whole standard fleet on 2% of its Shift volume.
- **Events and campaigns** (Chapter 11): $40–60k Year 1.
- **Division Year 1 total: ≈ $410–470k** — about a third of park revenue, per the Volume 10 model.

> **Investor Note.** The gap between the ~620-Shift/day ceiling and the ~75-Shift/day Year 1 blended reality is not waste — it is option value. The division can absorb roughly 8× demand growth (leagues, school programs, corporate weekdays) with zero additional fleet capex. Volume 10's upside case is built on filling exactly this gap.

### 9.4 Battery logistics — the 3:1 doctrine applied

Canon: **3 packs per vehicle minimum** — one in the machine, one charging, one rested and ready; 2S 7.4 V heavy-fleet standard, XT60 connectors (Deans legacy acceptable on acquired stock); LiPo window **3.4–4.2 V/cell** enforced by the Heavy-Node kill-switch; all charging in the bunkered charging room on SkyRC T1000 / ISDT K4-class multi-port balance chargers.

Division pool: 41 common-pool assets × 3 = **123 packs** (excavators/trucks/loaders/dozers on 2S 2,000–3,000 mAh; tractors on 2S 1,500–2,200 mAh), plus the K970's own pair of 3S 11.1 V 15,000 mAh packs outside the common pool. Every pack carries a QR and a cycle log in RC WORLD OS.

Swap cadence from measured duty: excavators draw 25–40% per Shift → swap at every Operator pit stop and every second Casual Shift; trucks draw evenly (continuous driving) → swap every second Shift without exception; tractors ≈ trucks. The 90-second pit-stop swap at the service-spine bench:

- [ ] Inbound pack voltage read and logged (any cell < 3.5 V → machine was over-run; investigate before reissue)
- [ ] Pack body inspected: no puffing, no dented corners, XT60 pins bright
- [ ] Outbound pack rested ≥ 30 min post-charge and ≥ 4.15 V/cell balanced
- [ ] Battery hatch latched; wiring clear of the pinch line
- [ ] Swap logged against pack QR + machine asset tag in RC WORLD OS

### 9.5 Growth triggers for adding machines

Fleet additions are triggered by the dashboard, never by enthusiasm. Each trigger must hold for a rolling month:

| Trigger | Threshold | Action |
|---|---|---|
| Standard-fleet blended utilization | > 4.5 paid Shifts/machine/day | Add one pod (1 × 1580 + 3 × 1582) — **always in ratio**; never add excavators or trucks alone |
| Peak-day queue abandonment | > 10% of mining queue walks | Same as above, or extend hours first (cheaper) |
| Premium occupancy | > 70% of offered K970 slots sold | Add second premium machine (K336GC or K988-100S loader, ~$1,700–4,600); budget +0.25 FTE Artisan |
| Agriculture party bookings | > 80% weekend slot occupancy | Add 4 tractors + implement set (~$500 total) |
| League demand | Waitlist > 4 teams | Add evening league night before adding machines |
| Any addition | — | Pack pool grows 3:1 with the machine, same purchase order, no exceptions |

---

## 10. Site & Track Design for Construction Play

### 10.1 Zone dimensions and layout

**Mining Zone: 60 m × 40 m (2,400 m²)**, long axis east–west, sited per the Volume 11 master plan with the site's 2–4% natural grade falling to the southwest corner (drainage exploits this). Coordinates in metres from the southwest corner (x east, y north):

- **Operator Rim (y = 36–40, full width):** elevated customer terrace, Section 10.3.
- **Main Pit (x = 4–44, y = 8–32):** two benches (−300 mm and −600 mm), six dig faces DF1–DF6 under their stations, in-pit ramp.
- **Haul loop (~110 m lap):** faces → south wall → main ramp (x = 44–54, −600 mm → +400 mm over 4.0 m run = 14°) → hopper apron → return ramp (north side, 14°) → faces. All per the Chapter 5.4 standard.
- **Central Processing Hopper (x = 50–56, y = 18–26):** tipping apron west, conveyor discharging east to the stockpile.
- **Premium Pad (x = 50–58, y = 30–38):** the K970's fenced 8 × 8 m dig cell with hardstand, leak tile and a rail-side viewing edge — the showcase digs where everyone can watch.
- **Service Spine (y = 0–6, full width):** staff-only strip behind a 1.1 m fence — swap bench, staging racks, SD loader bay, tool locker, and the single marshal gate at x = 30.
- **Dozer Push Boxes (x = 8–16, y = 8–12):** two 4 × 4 m sand cells inside the pit but fenced from the haul loop, so the youngest operators never enter traffic.

**Agriculture Zone: 50 m × 30 m (1,500 m²)** adjacent, per the Chapter 7.4 grid, sharing the service spine's swap bench.

### 10.2 Pit depths safe for retrieval

Maximum excavation depth is **600 mm below datum** — set not by the machines (a 1580 bottoms out at ~200 mm below its own tracks) but by **retrieval**: the 1/10 recovery crawler must be able to reach, rig and winch any casualty, and its practical climb limit against the pit's 30–40° faces bounds the geometry. Design rules:

- No point on the pit floor may be more than 600 mm below an adjacent surface reachable by the recovery crawler at ≤ 35°.
- Bench crests carry a 500 mm guard line: faces are never cut closer than this to the crest, preventing undercuts that could slump onto a machine below.
- The in-pit ramp always connects both bench levels to the haul loop — no machine can ever be geometrically stranded.
- Nothing in the zone requires a human to step below datum during operating hours; every retrieval is machine-performed (Section 10.5) or, at day's end, an Artisan task behind a closed gate.

### 10.3 Operator stations and sight lines

Twelve numbered stations at 4 m centres along the rim — a designed workplace, not a fence gap:

- Standing rail at 1.1–1.2 m (comfortable forearm rest for adults; chest rail for children on the fold-down 250 mm step — the under-8-with-guardian pairing the station is dimensioned for).
- Transmitter shelf angled 15°; station number and assigned-face placard; QR opening that station's live telemetry card in the customer app.
- Shade sails over every station (4 × 4 m HDPE, 3.2 m posts): transmitter LCDs and summer dwell both demand it.
- **Sight-line rule (non-negotiable):** every operator must see their machine *and the entire haul-road segment their trucks use*, unaided, from their station, at a 15–25° downward viewing angle — steep enough to see into truck beds (judging fill is the skill), shallow enough to read machine attitude at 20 m. No station may operate into the hopper's visual shadow; this constraint fixed the hopper at the east end.

### 10.4 Netting, barriers and separation

Customers operate from the rim and the field line, full stop; pit floor, haul loop and field grid are machine space. Three enforcement layers:

1. **Physical.** Rails and fences per above; the single interlocked marshal gate; the hopper's captive-key lockout — one key, two mutually exclusive locks, so the conveyor cannot run while the bin access panel is open, and cleaning and running are mechanically impossible to combine. Unlike the Aviation Division, no overhead netting is required — nothing in this division leaves the ground; barriers are waist-height and sight-friendly. Low mesh (300 mm) along the rim toe catches the one projectile the zone produces: spilled aggregate kicked by a track.
2. **Procedural.** Toolbox Talk induction, marshal authority, and the Retrieval Protocol replacing every "can I just grab it" impulse.
3. **Technical.** Geofence on every Heavy-Node: a machine crossing the customer line is PWM-killed before it reaches a shoe; under-voltage (<3.4 V/cell) throttles to 20% and orders the machine to the pit.

**Spectator viewing:** a 2 m-deep lean-rail terrace behind the operator line, deliberately generous — construction is the park's best spectator product, and a loaded 1/14 truck climbing the ramp at golden hour is its single best marketing image. The premium pad's viewing edge doubles as the crowd magnet during Master Operator sessions.

> **Safety Warning.** The most dangerous object in this division is not the 31 kg K970 — it is a *charging LiPo*. All charging occurs in the bunkered charging room without exception; no pack charges unattended anywhere in the zone, workshop bench included. The 3.4–4.2 V/cell window and the battery-bench checklist are safety controls first and asset controls second.

### 10.5 Retrieval, ergonomics and the marshal gate

A dead machine triggers its Heavy-Node's **85 dB localized buzzer**. The customer surrenders their transmitter at the marshal gate and receives the controls of the division's permanently staged **1/10 winch-equipped recovery crawler**; under marshal guidance they drive out, rig the winch (Artisan-supervised hook-up — customers never pass the gate), and tow the casualty to the service spine. Shift clock pauses during recovery; a fresh machine is issued; the *Tow-Truck Hero* badge posts on first completion. Pilot feedback is unambiguous: a meaningful share of children try to get recovered on purpose. The friction point is the feature.

Ergonomics addendum from pilot testing: transmitters hang on station lanyard hooks (dropped-transmitter rate fell to ~zero), the rim surface is compacted gravel rather than pavers (standing comfort over a full Operator Shift), and stations 1–2 nearest the gate are reserved for accessibility — wheelchair-height rail section and a widened terrace bay.

---

## 11. Earthmoving Competitions & Skill Programs

### 11.1 Why competition matters here

Racing has a century of borrowed formats; earthmoving has none — RC WORLD gets to *invent* its competitive canon, and owning formats means owning the community that plays them. Competition also solves the division's weekday problem: leagues and corporate bookings are scheduled demand aimed exactly at the utilization gap in Chapter 9.3. Every format below runs on standard rental machines (the parity doctrine borrowed from Motorsport: skill decides, not hardware) and scores automatically through the hopper load cells, RFID tokens and Heavy-Node telemetry — no manual judging beyond a marshal's penalty flag.

### 11.2 Precision digging challenges

- **Golf-Ball Pickup (the signature event).** Six golf balls on 60 mm tees in a 2 m arc around a 1580. Score = balls placed unbroken into a bucket-width target box; time is tiebreaker only. Championship variant swaps balls for eggs — boiled for juniors, raw for finals night. Theatrical, photogenic, and a genuine multi-channel finesse test.
- **Bucket Curling.** Push a 500 g puck along a 3 m painted lane with the bucket; nearest-to-rings scores 5/3/1; team relay format.
- **Trench & Backfill.** Cut a 400 mm trench to a depth template, place the "pipe" (300 mm dowel, grapple attachment), backfill and dress flat. Judged on template fit plus surface flatness under a straightedge. The trade-skill event — real operators enter this one.

### 11.3 Timed load-and-haul contests

One excavator + one truck per two-person team (or solo iron-man with transmitter hand-offs). Move **20 kg net through the hopper** from a marked face; the clock stops at the twentieth weighed kilogram. Spillage is not swept — it is simply tonnage you no longer have. Course-record pace from pilot testing: ~11 minutes (versus ~26–31 kg per *four-person pod* per casual Shift — the skill headroom is the sport). Variants: uphill-only routing, loader class (1583 direct to hopper), and Phase 3 night format under work lights.

### 11.4 'Site foreman' team scenarios — corporate events

The premium B2B product (from **$1,400 / 2 h / 20 pax**, canon): the group becomes a contractor. A brief is issued — *deliver 60 kg to the hopper, cut and backfill one trench, zero safety flags* — and roles are assigned: operators, logistics planner, and a **site foreman** holding the marshal tablet's read-only dashboard. The debrief hands every participant their personal telemetry card. Add-ons: K970 demo with the Artisan ($150), catered boardroom Toolbox Talk, branded hi-vis. The format sells because it is a genuine operations-management exercise wearing a toy's clothes — the 1:3 queueing logic of Chapter 5 becomes the customer's problem for two hours, and mixed-seniority groups reliably discover their best operator is the intern.

### 11.5 Skill-badge tasks (feeding Volume 9)

The division contributes a defined badge set to the park-wide RC WORLD License ladder; each badge is a machine-verified task, not a marshal's opinion:

| Badge | Task | Verification |
|---|---|---|
| First Furrow | Plow one field pass within 100 mm of the chalk line | Marshal photo overlay |
| Clean Loader | 10 truckloads with < 10% spillage | Hopper weight vs bucket-pass count |
| Ramp Master | 100 loaded ramp climbs without a retrieval | Heavy-Node geofence + retrieval log |
| Steady Hands | Golf-Ball Pickup: 6/6 in under 5 min | Event scoring |
| Tow-Truck Hero | Complete one supervised retrieval | Protocol log |
| Harvest Hand | 50 kg delivered in one Harvest Campaign | Weighbridge ledger |
| Master Operator | K970 assessment session passed | Artisan sign-off (tier 3 license) |

License gating (division view): tier 1 (post-Toolbox-Talk) unlocks RD-1 machines; tier 2 (tonnage + the Clean Loader practical) unlocks the 1583, tandem trailers and league entry; tier 3 plus a booked assessment unlocks premium K970 sessions. Full tier/badge matrix: Volume 9, Chapter 3.

League structure mirrors the park ladder: **Open evenings** (casual, monthly) → **Division League** (8-week season, tier 2; teams of four running 45-minute campaign sessions, aggregate-tonnage table, playoff weekend; $120/team/season against ~$60 of Shift value consumed — margin-accretive by design) → **RC WORLD Championship** (annual, invitational), to which the division contributes three disciplines: Precision, Load-and-Haul, and the Team Campaign final.

---

## 12. Maintenance & Reliability

### 12.1 Division doctrine

One sentence governs everything: **electromechanical machines are maintained by scheduled replacement of cheap discrete parts; the hydraulic machine is maintained by condition monitoring and cleanliness (Chapter 8.6).** All work logs to `maintenance_logs` (vehicle, mechanic, parts_used JSONB, description, date_resolved); predictive flags fire from `fleet_inventory.total_hours_run`, which increments on live PWM activity only — a machine that sat staged all day accrues nothing. Park-wide workshop standards, tooling and training live in Volume 7; this chapter is the division-specific layer.

### 12.2 Daily / weekly / monthly PM matrix

| Task | 1580 excavator | 1582/1573 truck | 1583 loader | 1554/69 dozer | E351 tractor |
|---|---|---|---|---|---|
| Visual + function test, connector check | Daily | Daily | Daily | Daily | Daily |
| Blow-down (in The Works), track/tire debris pick | Daily | Daily | Daily | Daily | Daily |
| Track tension (SOP-CD-001) | Weekly | — | — | Weekly | — |
| Steering/articulation linkage & servo check | — | Weekly | Weekly | — | Weekly |
| Pivot-bushing slop gauge (< 2 mm at teeth/blade) | Weekly | — | Weekly | Weekly | — |
| Lead-screw lubrication (SOP-CD-005) | Monthly / 40 h | — | Monthly (lift arms) | Monthly | — |
| Micro-switch test bank (all limits) | Monthly | Monthly (tip limit) | Monthly | Monthly | — |
| Gearbox open-inspect, gear wear | Quarterly / 120 h | Quarterly | Quarterly | Quarterly | Quarterly |
| Motor brush / current-draw baseline | Quarterly | Quarterly | Quarterly | Quarterly | Quarterly |
| Slip-ring clean (continuous slew) | Annual | — | — | — | — |
| Full refurbishment pass (§12.6) | 150 h or defect | 200 h | 150 h | 100 h | 200 h |

K970 follows the Chapter 8.6 schedule; battery pool audits run weekly by pack QR rotation, fleet-wide.

### 12.3 Sand ingress management

Sand is the division's business model and its universal solvent of machinery. The ingress-control stack, cheapest layer first:

1. **Material spec** — washed <3% fines aggregate and 4–6% face moisture (Chapter 6.6) prevent most airborne fines at source.
2. **Grease discipline** — printed in red on every bench card: *nothing gets grease that touches sand directly.* Exposed pivots get oil-pen film only; grease on an open pivot is grinding paste by lunchtime. Grease belongs inside screw tubes, gearboxes and sealed ports.
3. **Dry blow-down only, in The Works** (≤ 2 bar, outdoors) — never wet-wash an electromechanical machine; water carries fines *into* screw tubes and switch bodies.
4. **Bearing quarantine** — any wheel or idler bearing with grit-crunch is binned, never cleaned and re-oiled; a $0.60 bearing is not worth a $60 axle.
5. **Connector hygiene** — XT60s and JST XH latches wiped at every swap; the refurbishment electrical pass pull-tests every connector.

### 12.4 Spares stocking and reorder points

The division's shelf in The Works, sized so no single failure becomes downtime (par levels for the 42-machine fleet; suppliers and pricing in Volume 8, with 4–8 week China-direct lead times already priced into the reorder points):

| Part | Par stock | Reorder at | Turnover |
|---|---|---|---|
| Micro-switches (KW11-class limit switches) | 200 | 80 | Medium-high — the #1 heavy-fleet consumable |
| Excavator track pins + pads | 300 / 40 | 120 / 15 | Continuous (canon consumable) |
| Gear sets, nylon + metal, per actuator model | 12 each type | 5 | High — nylon stocked for its sacrificial role |
| Lead screw + nut pairs (1580 boom/stick/bucket) | 6 each | 2 | Medium |
| Brushed 380/540/550 motors | 15 | 6 | Medium |
| Steering servos 15/25 kg digital | 10 | 4 | High (trucks + tractors) |
| Brushed ESCs, fleet standard | 6 | 2 | Medium |
| XT60 pairs / JST XH housings + pins | 100 / 200 | 40 / 80 | Continuous |
| 2S LiPo packs (pool attrition ~15%/yr) | 12 | 4 | Continuous |
| Lithium grease (NLGI 2), Loctite blue, IPA | 4 / 6 / 4 units | 1 / 2 / 1 | Continuous |
| Hydraulic seal kits (K970 full set) | 2 sets | 1 | Low — long lead, never zero |
| ISO VG 32 oil (dyed) | 4 L | 1 L | Low |
| Tractor hitch pins / trailer axles | 30 / 6 | 10 / 2 | Medium (party-day attrition) |

RC WORLD OS decrements stock from `parts_used` logging and fires reorder alerts automatically at the levels above.

### 12.5 Key procedures

**SOP-CD-001 — Track Tension Check & Adjustment (tracked fleet)**
**SOP ID:** SOP-CD-001 · **Rev:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** shop standard · **Tools:** 3 mm steel rule, hex drivers, lithium grease, torque driver (0.6 N·m) · **Frequency:** weekly per tracked machine, or after any thrown track

1. Bench the machine, power off, bucket/blade grounded.
2. Brush the track runs; pick embedded stones from between pads (the #1 cause of false tension readings and pad wear).
3. Measure mid-span sag under one-finger pressure (~10 N): spec **3–5 mm** on 1580/1583-class, 2–4 mm on 1/16 dozers.
4. Adjust the idler-yoke tension screw a quarter-turn at a time. Never tension drum-tight — over-tension raises drive current 15–20% and eats sprocket bushings; the quarterly current baseline will betray you.
5. Check pin staking both runs; re-stake proud pins; bin any pin that walks twice.
6. Torque idler lock screws 0.6 N·m; one grease shot to the idler axle port.
7. Run a 60 s figure-eight in the workshop dig box; confirm no walk-off in tight turns; log sag before/after.

**SOP-CD-005 — Lead-Screw Lubrication**
**SOP ID:** SOP-CD-005 · **Rev:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** nitrile gloves · **Tools:** lithium grease (NLGI 2), brush, lint-free wipes, IPA, bench PSU · **Frequency:** monthly or 40 run-hours per actuator

1. Open the actuator access cover (boom, stick, bucket in turn on the 1580; lift arms on the 1583; blade screw on dozers).
2. Run to full extension on bench power; wipe the exposed screw with IPA and *read the wipe*: gray paste = normal wear; glitter = nut shedding — replace the screw/nut pair now, not mid-season.
3. Brush a rice-grain bead of grease along the full thread. Do not pack the tube — excess grease is a dust magnet; thin film, full coverage.
4. Cycle full travel three times; verify both limit switches click and cut at the ends.
5. Wipe squeeze-out, close, log.

**SOP-CD-002 — Boom Micro-Switch Replacement**
**SOP ID:** SOP-CD-002 · **Rev:** 1.0 · **Owner:** Heavy Fleet Artisan Lead · **PPE:** safety glasses · **Tools:** soldering iron, solder, heat-shrink, flush cutters, multimeter, replacement KW11-class switch · **Frequency:** on defect or monthly test-bank failure

1. **Diagnose first.** Actuate the suspect switch by hand under a continuity meter — confirm fail-open (no click-through) or fail-closed (welded contacts) before touching solder. If the switch tests good, the fault is a misadjusted crush-stop; fix that instead.
2. Photograph the wire routing; note lever type (plain/roller) and throw direction — Huina uses both orientations in one machine.
3. Desolder or cut back to bright copper; strip 3 mm; slide heat-shrink on *now* (the step everyone forgets).
4. Solder the new switch NO/NC/COM exactly per photo; shrink the joints.
5. Set the trip point: the switch must click **1–2 mm before** the hard mechanical stop — that margin is the entire purpose of the switch. Verify by hand-cranking the screw to the stop.
6. Bench-run five full cycles; clean cut-off both ends, no stall audible.
7. Log the switch position ("boom, upper limit") in parts_used — position-level data keeps the FMEA below honest.

**Gearbox servicing** (quarterly open-inspect): photograph gear train before touching; check nylon gears for tooth-root cracks under magnification (they crack before they strip); re-grease metal meshes sparingly; verify output-shaft end-float < 0.5 mm; replace any gear showing polished wear-through of the molding line. A stripped-gear symptom in the field — motor audibly spinning, function dead — is a 20-minute gear-set swap from shelf stock.

### 12.6 The 45-minute refurbishment turnaround

Every rental machine cycles through The Works on PM schedule or defect. Staged so one Artisan finishes inside 45 minutes from ghost-machine bins: intake scan and photo → dry blow-down → bench function test at 7.4 V (a healthy lead screw hums, a dry one squeals, a worn nut knocks) → open *only* the failed/scheduled actuator (every opening is a dust opportunity) → replace the discrete part → re-grease → pivot/track/torque pass → electrical pass (XT60 pull test, chafe scan, JST XH latches, conformal-coating visual on the Heavy-Node) → 5-minute load test in the workshop dig box → log and release to `active`.

> **Trade Hack.** Keep each actuator's screws in their own magnetic tray, photographed before disassembly. The 1580 uses four visually similar screw lengths, and a long screw in a shallow boss cracks the casting — the single most common self-inflicted workshop injury to these machines.

### 12.7 FMEA — excavators and dump trucks

Scored 1–5 (severity × occurrence × detection difficulty = RPN; act on RPN ≥ 27):

| Machine | Failure mode | Effect | S | O | D | RPN | Mitigation |
|---|---|---|---|---|---|---|---|
| 1580 | Limit switch fail-closed (welded) | Gearbox stall, possible gear strip mid-Shift | 3 | 4 | 3 | **36** | Monthly test bank; ESC current fold-back; SOP-CD-002 |
| 1580 | Slip-ring oxidation | Intermittent slew/electrics, hard to reproduce | 3 | 2 | 4 | 24 | Annual clean; symptom triage card in The Works |
| 1580 | Lead-screw nut wear | Boom droop under load, slop | 2 | 3 | 2 | 12 | SOP-CD-005 wipe-read; nut pairs on shelf |
| 1580 | Nylon gear strip (shock load) | Function dead, Shift refund | 3 | 3 | 1 | 9 | Site geometry caps drop energy; 20-min gear swap |
| 1580 | Thrown track in pivot turn | Machine immobile → retrieval event | 2 | 3 | 1 | 6 | SOP-CD-001 tension spec; retrieval is gameplay |
| 1580 | Pack over-discharge (hidden by customer) | LiPo damage; storage fire risk | 4 | 2 | 2 | 16 | Node kill at 3.4 V/cell (canon); inbound bench check |
| 1582/73 | Steering servo failure | Truck uncontrollable → circuit blockage | 3 | 4 | 2 | 24 | Weekly linkage check; servo par stock; marshal pulls to shoulder |
| 1582/73 | XT60/wiring chafe at bed pivot | Intermittent power; phantom "dead battery" | 2 | 3 | 4 | 24 | Refurb electrical pass targets this loom explicitly |
| 1582/73 | Wheel bearing seizure (fines) | Dragging wheel, motor heat | 2 | 3 | 3 | 18 | Daily blow-down; bearing quarantine rule |
| 1582/73 | Tip-linkage bent (overload + slam) | Bed won't seat; spillage all lap | 2 | 3 | 2 | 12 | Bucket-pass-count load discipline; linkage on shelf |
| 1582/73 | Drive gearbox strip (berm jump) | Truck dead on ramp | 3 | 3 | 1 | 9 | Berm geometry caps launch energy; gear sets on shelf |

The two highest-RPN items — welded limit switches and steering servos — are exactly the two parts stocked deepest in Section 12.4. That is not a coincidence; it is the FMEA doing its job. Escalation, tooling standards, technician training and the cross-park failure database live in **Volume 7** (see especially its workshop layout and rebuild-training chapters), which treats this chapter's SOPs as division-local instances of the park-wide system.

---

## Volume summary & cross-references

The Construction Division is RC WORLD's signature: a working 1/14 open-pit mine and a 1/16 commercial farm, run as a genuine production system. Its engineering constitution is the two-tier fleet — 29 rugged, lead-screw Huina earthmovers and 12 Double E tractors earning volume fees at $15–26 per 20-minute Shift, plus one Kabolite K970-class hydraulic flagship earning supervised premium fees at $22–38 — bound together by the 1:3 excavator-to-truck ratio (derived, Chapter 5.2), 15°-max haul roads built at 14°, a closed material-recirculation loop metered through a load-cell hopper, and a maintenance program built on discrete-part replacement, lithium grease, and micro-switches stocked by the hundred. Division fleet capex is ~$16k wholesale; the civil works and hopper are the real build cost; Year 1 division revenue target is ≈$410–470k inside the park's $1.28 M canon, with roughly 8× demand headroom on the existing fleet.

*Scope note (living document):* Volume 3 references a crawler-program "adventure annex" under this volume (Track C, the 16-machine crawler park). That annex is deferred to Revision 1.1 of this volume; until then the crawler fleet is governed by the canon fleet table (Volume 1) and the Track C specification in Volume 3.

**Cross-references:** park-wide fleet, phasing and capex canon — **Volume 1**. Competitive landscape and Chinese diorama/miniature-equipment suppliers — **Volume 2**. The Motorsport parity doctrine this division's competition rules borrow — **Volume 3**. The Works: fabrication drawings (hopper, grading blade, pin hitch), RCW Heavy-Node hardware, rebuild training and the hydraulic technician curriculum — **Volume 7** (which should honour this volume's SOP numbering CD-001…CD-005). Suppliers, wholesale channels, spares pricing and the 4–8 week reorder mechanics — **Volume 8** (LESU and JDModel carried as second-source hydraulic suppliers; Siku Control as retail stock, not fleet). Licenses, badges, Gears, Toolbox Talk and the tier matrix this division's gates plug into — **Volume 9, Chapter 3**. Division financials and the utilization upside case — **Volume 10**. Site master plan, drainage, charging bunker and fencing standards — **Volume 11**. Franchising the Mining Zone as the flagship differentiator — **Volume 12**.
