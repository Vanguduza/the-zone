# Volume 7 — Engineering & Workshop Manual

**RC WORLD — Master Development Plan** · Volume 7 of 13
**Revision:** 1.0 · **Date:** July 2026 · **Status:** Living document — bump revision on material change

**Purpose of this volume.** This is the technician's handbook for **The Works**, RC WORLD's central engineering and workshop facility, and the single most operationally load-bearing document in the master plan. Roughly 150 powered assets take the field in Phase 1, each crashed, over-driven and rained on by strangers up to a dozen times a day; the difference between a park that feels like a precision motorsport operation and a park that feels like a broken toy bin is entirely decided at the workbench. This volume specifies the workshop itself (floor plan, benches, ESD, air, ventilation), the tools at three investment tiers, the craft standards every Artisan is trained and audited against, a compendium of RC trade hacks, the full library of Standard Operating Procedures, the preventive-maintenance matrices driven by RC WORLD OS telemetry, repair scheduling mathematics, inventory management, FMEA-based failure analysis, the battery and charging rooms operated under the park's LiPo doctrine (3.4–4.2 V/cell operating window, 3:1 battery ratio, bunkered charging), the QC lane, a complete tutorial on building custom RC cars — required reading by founder's brief — and the bench-side of the RCW Node telemetry program. A competent RC hobbyist hired as a trainee Artisan should be able to reach productive competence from this volume plus supervised bench time.

**Intended readers.** Every Artisan and the Workshop Lead (this is their primary manual); the General Manager; procurement staff executing the tool and spares purchases (with Volume 8); division leads whose fleets this workshop keeps alive (Volumes 3–6); the RC WORLD OS team implementing the maintenance, inventory and telemetry modules (Volume 13); investors assessing whether the fleet-availability assumptions in Volume 10 are engineered or hoped for.

**Chapters**

1. The Works — Workshop Design
2. Tool Lists: Three Investment Tiers
3. Workshop Behaviours & Craft Standards
4. RC Trade Hacks
5. Standard Operating Procedures
6. Preventive Maintenance System
7. Repair Scheduling & Workflow
8. Inventory & Parts Management
9. Failure Analysis & FMEA
10. The Battery Room
11. The Charging Room
12. Quality Control
13. Building Custom RC Cars
14. Telemetry Hardware Bench Work
15. Volume Summary & Cross-References

---

## 1. The Works — Workshop Design

### 1.1 Design philosophy: a service department, not a hobby bench

The Works is sized and organized like a small vehicle dealership's service department, because that is functionally what it is: a fleet of revenue-earning vehicles arrives broken and must leave billable. Three principles govern the layout:

1. **Flow, not rooms.** A vehicle enters at intake, moves through triage, repair, QC and back to the fleet staging shelf in one direction. No vehicle ever moves "backwards" past the QC lane without a new job ticket. One-way flow is what makes the RC WORLD OS fleet status trustworthy — the physical position of a vehicle always matches its database state (a seven-state machine: available → bound → on_track → pit → maintenance → charging → retired; see Volume 13 §6.3).
2. **Segregation of energy.** Batteries are the park's dominant fire risk and are physically segregated: a **Battery Room** for storage and logging (Chapter 10) and a separate bunkered **Charging Room** (Chapter 11), both isolated from the main workshop by masonry. No LiPo is ever charged at a repair bench.
3. **Visibility as theatre.** The Works has a public-facing **guest viewing window (6.0 × 1.5 m)** along the pit lane. Customers watching an Artisan rebuild a differential is free marketing, reinforces the "miniaturized industrial complex" brand, and — usefully — keeps bench discipline honest. The glazing is specified in Volume 11, Chapter 6; this volume only requires that the wrenching bays face it.

### 1.2 Floor plan and zone schedule

Volume 11 (Chapter 6), the geometry authority, fixes The Works at **450 m² GFA (≈4,840 ft²)**. Inside that envelope, this volume's working layout is a **~180 m² wrenching/electronics core** — the zones an Artisan moves between hourly — wrapped by the larger support rooms whose dimensions Volume 11 owns. Core allocation:

| Core zone (~180 m² total) | Area | Function | Key requirement |
|---|---|---|---|
| Intake & triage | 20 m² | Receiving shelf, triage bench, wash-down sink, air-blow station | Door to the intake yard off the pit lane; RC WORLD OS kiosk terminal |
| Wrenching bays (×4) | 48 m² | Mechanical repair benches, one Artisan each | 1.8 m benches, tool shadow boards, parts trays; face the viewing window |
| Electronics bench (×2) | 24 m² | Soldering, ESC/servo work, RCW Node assembly & flashing | ESD-protected area, fume extraction |
| Machining corner | 18 m² | Lathe, drill press, grinder, rotary tool, vice work | Separated by partition; chip containment; eye-wash |
| 3D printing & jig shelf | 8 m² | 2 printers, filament drybox, jig library | Ventilated enclosure exhaust |
| Paint & gluing booth corner | 12 m² | Spray booth, body prep, batch tire gluing | Ducted extraction (§1.7) |
| Fleet staging shelves | 20 m² | QC-passed vehicles awaiting return to service | Adjacent to QC lane exit |
| Circulation, lockers, docs | 30 m² | Artisan lockers, manual library, whiteboard, coffee | — |

Support rooms inside the 450 m² GFA, per Volume 11 Chapter 6:

| Support room | Area | Key requirement |
|---|---|---|
| Parts store | 45 m² | Bin shelving, kanban racks, consumables cabinet; adjacent to wrenching bays; single controlled entry |
| Battery Room | 24 m² | Storage-charge LiPo racks, IR/logging bench; masonry separation (Chapter 10) |
| Charging Room (bunker) | 30 m² internal (6.0 × 5.0 m) | **Inside the building**: filled-cell CMU, blast venting, FD90 door (Chapter 11) |
| QC lane | 35 m² | Rolling-road bench, scales, radio range check; direct exit to a 25 m fenced test strip |
| Intake yard access, plant, ancillary + wall/GFA allowance | ≈136 m² | Balance of the 450 m² GFA — Volume 11 carries the dimensioned plan |

The four wrenching bays are the capacity constraint of the whole park (see the loading math in Chapter 7); Volume 11's 450 m² shell reserves core floor area for a Phase 2 expansion to six bays without structural change.

### 1.3 Bench specification

All repair benches are built to one standard so any Artisan can work at any bay:

- **Dimensions:** 1,800 × 750 mm work surface, 900 mm working height (standing/high-stool), load rating ≥150 kg.
- **Surface:** 25 mm laminated hardwood or phenolic top, overlaid with a replaceable 600 × 900 mm cutting/soldering mat at each station. Electronics benches add a grounded ESD rubber mat (see 1.4).
- **Under-bench:** one 5-drawer roller cabinet per bay (personal kit lives here), one shelf for the in-progress vehicle's tote.
- **Over-bench:** shadow board for shared tools (outline-painted so a missing tool is visible at a glance), LED task light, power rail with 6 outlets + 2 USB-C PD, magnetic strip for hex drivers.
- **Each bay carries:** a bench vice (100 mm jaws, machining corner gets the 125 mm), a car stand (rotating, e.g. the ubiquitous 1/10 aluminum stands, $10–15), two magnetic parts trays, and a labelled "job tote" system — one plastic tote per vehicle under repair, so a job can be shelved mid-repair without losing parts.

### 1.4 ESD protection

Everything downstream of the receiver — ESCs, gyros, RCW Nodes, telemetry PCBAs — is static-sensitive. The two electronics benches are run as an ESD-protected area to the intent (not full certification) of ANSI/ESD S20.20:

- Grounded dissipative rubber bench mats (Bertech or SCS class, $40–80 per bench) bonded to building earth through a 1 MΩ resistor.
- Wrist straps at both benches; wearing one is mandatory whenever a bare PCBA (RCW Node, ESC with case opened) is handled. Handling a cased, plugged ESC during mechanical work does not require a strap.
- Field-service parts (spare ESCs, receivers, Nodes) stored and transported in metallized shielding bags, never in pink poly alone.
- No polystyrene cups, cling film, or tape dispensers on the electronics benches — the classic hidden charge generators.
- Humidity in the electronics zone kept ≥40% RH where climate allows; dry-season operation adds an ionizing fan ($150–300) if RH cannot be held.

> **Safety Warning.** ESD damage is almost never immediate failure — it is latent damage that kills an ESC three weeks later on a customer Shift. You will never trace that failure back to the day someone handled the board in a fleece jacket. Follow the strap rule even though you have "never had a problem".

### 1.5 Lighting

Lighting is specified by task, following general illumination-engineering practice for fine bench work:

| Area | Maintained illuminance | Fixture guidance |
|---|---|---|
| General circulation & stores | 300 lux | LED battens, 4000 K |
| Wrenching bays | 750–1,000 lux at bench surface | Overhead + adjustable task lamp per bay |
| Electronics benches | 1,000–1,500 lux at work point | Task lamp with diffuser; add a lighted magnifier (3-diopter ring light, $40–80) |
| Machining corner | 750 lux + machine-mounted lamp | No stroboscopic flicker near rotating machinery — specify high-frequency LED drivers |
| QC lane | 750 lux, high CRI (≥90) | Paint/body inspection needs honest color rendering |

Choose 4000 K neutral white throughout; 6500 K "cool daylight" causes eye fatigue on long shifts and 3000 K hides solder-joint defects.

### 1.6 Compressed air

A quiet workshop compressor feeds a ring main with drops at intake (blow-down station), each wrenching bay, the machining corner and the QC lane:

- **Compressor:** 1.0–1.5 kW ultra-quiet unit, ≥30 L receiver, e.g. California Air Tools 8010 class ($180–280). Two smaller units beat one large one for redundancy.
- **Treatment:** water trap + coalescing filter at the manifold, regulator per drop. Vehicle blow-down at **max 3 bar (≈45 psi)** with a rubber-tipped nozzle — full pressure drives grit *into* bearings instead of off them.
- **Uses:** dust blow-down at intake (always outdoors or at the extracted intake station, never over an open bench), drying after wash, airbrush supply in the paint corner, clearing drilled holes in the machining corner.

> **Trade Hack.** Fit a cheap inline "dust gun" with a fan nozzle at intake and keep a stiff 25 mm paintbrush hanging next to it. Brush-agitate while blowing and a post-Shift buggy is clean in 90 seconds; blow alone takes five minutes and redistributes half the dust into the electronics tray.

### 1.7 Ventilation: soldering and paint

Two extraction problems, two systems:

1. **Solder fume.** Rosin flux fume is a sensitizer; chronic exposure causes occupational asthma. Each electronics bench gets a fume extractor — either a filtered bench unit (Hakko FA-400 class, $60–110, filters replaced monthly) or, preferred, an extracted arm ducted outdoors (Weller/Quick fume arm systems, $250–600). The RCW Node assembly bench, which solders daily, must have the ducted option.
2. **Paint & solvents.** Polycarbonate body spraying, conformal coating and CA-glue tire work all release solvents. The paint corner is a bench with a spray booth — a hobby extraction booth with ducting to outside (Vevor/Master Airbrush class, $90–180) is adequate for rattle-can and airbrush volumes. Bulk tire gluing happens at this bench, not at the wrenching bays. Conformal coating spray (Chapter 14) always happens in the booth.

The machining corner adds a shop-vac with cyclone separator for chips and grinding dust; never blow grinding dust with compressed air near the electronics zone.

### 1.8 Services summary for the architect

Hand Volume 11's designer this checklist:

- [ ] 450 m² GFA per Volume 11 Chapter 6, one-way flow intake → QC around a ~180 m² wrenching/electronics core; guest viewing window (6.0 × 1.5 m) to the pit lane at the wrenching bays; intake yard access
- [ ] Masonry-separated Battery Room (24 m²) and internal bunkered Charging Room (30 m² internal, 6.0 × 5.0 m: filled-cell CMU, blast venting, FD90 door)
- [ ] 3-phase power to machining corner and Charging Room; 20+ double outlets distributed
- [ ] Dedicated circuits: charging banks (Chapter 11 load calc), compressor, extraction
- [ ] Ducted extraction: solder arm (electronics), spray booth (paint corner), printer enclosure
- [ ] Compressed-air ring main, 5 drops; compressor in acoustic cupboard
- [ ] Wash-down sink with silt trap at intake; eye-wash station at machining corner
- [ ] Floor: sealed concrete, light grey (dropped M2 screws must be findable)
- [ ] Wi-Fi mesh AP inside The Works (RC WORLD OS kiosks, Node flashing, telemetry bench)
- [ ] Door widths ≥1.2 m throughout (fleet trolleys), no steps on the vehicle flow path

---

## 2. Tool Lists: Three Investment Tiers

### 2.1 How the tiers work

The tool budget is split into three tiers with different ownership and replacement rules:

- **Tier 1 — Per-Artisan personal kit.** Issued to each Artisan on hiring, engraved/color-banded, kept in their bay drawer. The Artisan is accountable for it; a complete kit is checked at quarterly audit. Budget **$420–600 per Artisan**.
- **Tier 2 — Shared bench equipment.** Lives on shadow boards and the electronics benches; anyone may use it, everyone returns it to its outline. Budget **$4,500–6,500** for Phase 1.
- **Tier 3 — Capital equipment.** Machines with asset tags in RC WORLD OS `fleet_inventory` (yes — machines are assets too, with maintenance logs). Budget **$6,000–9,000** Phase 1.

Prices below are July 2026 street-price ranges for the named class of product; procurement executes actual purchasing per Volume 8 and may substitute equivalents that meet spec.

### 2.2 The metric sizes that dominate RC

Before the lists: RC is a **metric hex world**. Better than 90% of fasteners across the RC WORLD fleet fall on seven tool sizes. Buy depth in these; everything else is occasional.

| Tool size | Typical use across the fleet |
|---|---|
| 1.5 mm hex | M3 set screws (pinions, drive cups), micro linkages, 1/14 fleet body hardware |
| 2.0 mm hex | M2.5/M3 cap screws — the single most-used driver in the building |
| 2.5 mm hex | M3 cap/button screws on 1/10 platforms, shock caps, motor mounts |
| 3.0 mm hex | M4 hardware on crawlers, construction fleet frames, tractor hitches |
| 4.0 mm nut driver | M2 lock nuts (small linkages) |
| 5.5 mm nut driver | M3 lock nuts — suspension pivots, servo horns |
| 7.0 mm nut driver | M4 wheel nuts on 1/10 fleet (the daily driver of the tire bench) |

Add 5.0 mm and 8.0 mm nut drivers for the construction and crawler heavy hardware, and 4 mm/5 mm/5.5 mm turnbuckle wrenches for camber/toe links. Phillips: PH1 and JIS #1 (Japanese-standard cross-head — many Far-East fasteners cam out under a Western PH1; a JIS driver grips them correctly).

### 2.3 Tier 1 — Per-Artisan personal kit ($420–600)

| Item | Example product | Price range |
|---|---|---|
| Hex driver set 1.5/2.0/2.5/3.0 mm | MIP Gen 2 metric set ($51–55) + 3.0 mm, or ProTek "TruTorque SL" 4-pc ($50–60) | $55–110 |
| Ball-end hex 2.0/2.5/3.0 mm | MIP Gen 2 ball set | $55–60 |
| Nut drivers 4.0/5.5/7.0 mm (+5.0/8.0) | MIP, ProTek or Arrowmax | $45–90 |
| Turnbuckle wrench set | ProTek or Yeah Racing multi-size | $10–20 |
| JIS #1 + PH1 screwdrivers | Vessel or Hozan JIS drivers | $12–25 |
| Precision side cutters (flush) | Knipex 78 61 125 or Hakko CHP-170 | $12–45 |
| Needle-nose + bent-nose pliers | Knipex or generic ESD | $20–50 |
| Hobby knife + blades | Excel/X-Acto #1 with #11 blades | $8–15 |
| Curved lexan scissors | ProTek/Dubro body scissors | $10–18 |
| Body reamer (0–14 mm) | ProTek or HPI | $10–15 |
| Digital calipers 150 mm | iGaging ($30–40) or Mitutoyo 500-196-30 ($120–170) — one Mitutoyo per shop minimum | $30–60 |
| Shock/E-clip tools | Dental pick set + shock shaft pliers | $15–30 |
| Magnetic parts trays ×2 | Generic 100 mm round | $8–14 |
| Small steel rule 150 mm, thread files | Generic | $10–15 |
| Headband magnifier or clip loupe | Generic 3.5× | $10–20 |
| Tweezers set (straight, curved, reverse) | ESD stainless set | $8–15 |
| Kit bag/roll + engraving | — | $15–30 |

> **Field Note.** Do not cheap out on the four hex drivers. A $6 hex set rounds the first over-tightened M3 it meets, and every rounded screw costs 15 minutes and a drill-out. The MIP/ProTek tips are hardened tool steel and last years; this is the highest-leverage $100 in the entire tool budget.

### 2.4 Tier 2 — Shared bench equipment ($4,500–6,500)

**Electronics benches:**

| Item | Example product | Price range | Qty |
|---|---|---|---|
| Soldering station 70–100 W | Hakko FX-888DX ($110–150) or Weller WE1010 ($150–190); budget alternative YIHUA 939D+ ($70–90) | $110–190 | 2 |
| High-power iron for XT60/battery leads | Hakko FX-601 or 100 W cartridge station; chisel tips ≥D24 | $60–120 | 1 |
| Hot-air rework station | Quick 861DW ($230–300) or YIHUA 959D ($80–120) | $80–300 | 1 |
| Bench power supply 30 V/10 A | RIDEN RD6006 ($100–130) or Korad KA3005D ($80–110) | $80–130 | 2 |
| Multimeter — reference | Fluke 117 ($290–310) | $290–310 | 1 |
| Multimeter — bench spares | Fluke 101 or ANENG/UNI-T class | $25–60 | 3 |
| Battery checker / cell meters | ISDT BattGo BG-8S or SkyRC cell checker | $25–40 | 4 |
| Servo tester + PWM signal source | Generic CCPM testers ($8–12) + one G.T.Power digital servo analyzer ($30–50) | $50–80 | 3+1 |
| Watt meter / inline power analyzer | G.T.Power 130 A or generic 150 A watt meter | $20–35 | 2 |
| ESC programming cards | Hobbywing LED program card + brand cards for fleet ESCs | $10–20 ea | 4 |
| Motor analyzer | SkyRC BMA-01 (KV, RPM, timing, current) | $85–110 | 1 |
| USB-UART flashing rigs (RCW Node) | CP2102/CH340 adapters + pogo-pin jig (Chapter 14) | $10–20 | 2 |
| Fume extraction | Ducted arm (Node bench) + Hakko FA-400 class (second bench) | $60–600 | 2 |
| Solder & consumables | 63/37 leaded for bench work (0.8 mm), SAC305 where lead-free required; flux pens, wick, tip tinner | $150/yr | — |
| PCB vice / third hand | Panavise 201 ($40–55) + silicone-arm third hands | $60–90 | 2 |

**Wrenching bays (shared, on shadow boards):**

| Item | Example product | Price range |
|---|---|---|
| Torque screwdriver 0.1–1.2 N·m | Wiha TorqueVario-S or Wera Series 7400 with hex bits | $110–180 |
| Pinion puller / gear puller | Robinson Racing or generic puller set | $15–30 |
| Bearing press/removal kit | Stepped-drift set + arbor blocks | $25–50 |
| Shock oil stand, syringes, cups | Generic + graduated cups | $20–35 |
| Digital scale 0.1 g (setup/ballast) | Generic 3 kg jewelry class | $15–25 |
| Corner scales (parity program, Vol. 3) | SkyRC corner weight system | $80–120 |
| Camber gauge + setup wheels 1/10 | ProTek or Arrowmax setup system | $60–150 |
| Ride-height gauge, droop blocks | ProTek stepped gauge | $15–40 |
| Tire truer (optional Phase 2) | Hudy or generic truer | $150–400 |
| Heat gun (heat-shrink, body work) | Wagner/Steinel class | $25–50 |
| Threadlock: blue (243) — bulk | Loctite 243 10 ml ×6 | $60–90 |
| Retaining compound (609/638) | Loctite 638 10 ml | $15–25 |
| CA glue thin/medium + activator | Bob Smith Industries range | $30/mo |
| Greases & oils | See lubrication chart §6.5 | $150 initial |
| Ultrasonic cleaner 3 L | Generic 40 kHz heated | $60–120 |
| Drybox cabinet + silica | Sealed cabinet, indicating silica gel bulk | $60–100 |
| Label printer | Brother P-touch PT-D610 or Zebra class | $70–140 |

### 2.5 Tier 3 — Capital equipment ($6,000–9,000)

| Item | Example product | Price range | Purpose |
|---|---|---|---|
| Benchtop lathe 180–400 mm between centers | Sherline 4400 package ($730–1,300) or SIEG SC2/7×14 class ($700–1,000) with metric change gears | $700–1,300 | Custom driveshafts, spacers, shock pistons, hex adapters, boring wheel hexes, facing motor mounts |
| Commutator lathe (brushed fleet) | Hudy professional comm lathe or equivalent dedicated comm skimmer | $250–400 | Skimming 540/550 brushed motor commutators — the construction and tractor fleets run brushed motors; a $6 skim revives a $25 motor |
| Drill press 350–500 W | WEN 4208 class or bench Bosch | $130–250 | Accurate holes in chassis plates, jigs, servo mounts |
| Bench grinder + wire wheel | 150 mm, 250–400 W | $60–120 | Dressing tools, cleaning shafts, shaping steel links |
| Rotary tool + stand | Dremel 4300 kit | $100–150 | Cutting, porting, cleanup — the RC workshop's universal tool |
| 3D printers ×2 | Bambu Lab P1S ($370–700 depending on promo) ×2 | $740–1,400 | Jigs, fixtures, body posts, custom mounts, prototype parts; two printers so a failed unit never blocks the jig library |
| Filament drybox + stock | PLA+ / PETG / ABS/ASA, ~20 kg rolling stock | $250–400 | PETG for functional park parts (UV + toughness), ASA for outdoor fixtures |
| Air compressor (×2 small) | California Air Tools 8010 class | $360–560 | §1.6 |
| Spray booth + airbrush kit | Extraction booth + Iwata Eclipse or NEO | $200–400 | Body painting (Chapter 13), conformal coating |
| Charging infrastructure | See Chapter 11 (charger bank is costed there) | — | — |
| Rolling-road / dyno bench (QC) | Custom-built rollers + brake, or SkyRC chassis dyno if available locally | $150–500 | Post-repair load test without track time (Chapter 12) |
| Fleet trolleys ×3 | 3-shelf workshop trolleys | $180–300 | Moving 6–8 vehicles between pit lane and The Works |

> **Investor Note.** Total Phase 1 tooling — five Artisan kits (4 Artisans + Workshop Lead) plus one uncommitted float kit as training/loaner stock, shared benches, capital equipment, charging infrastructure — lands at **$28,000–38,000** including the charger bank costed in Chapter 11. This is under 2% of Phase 1 capex and is the least discretionary line in the budget: every dollar of fleet availability flows through these benches.

### 2.6 What we deliberately do not buy in Phase 1

CNC mill (jigs come off the printers; true machining is jobbed out), laser cutter (fire risk in a LiPo facility; outsource), injection molding (fantasy at this scale), a second lathe, and any tool that exists to make one specific job slightly faster before that job has proven its frequency in the RC WORLD OS repair data. The failure-analysis loop (Chapter 9) tells us what to buy in Phase 2.

---

## 3. Workshop Behaviours & Craft Standards

This chapter is the skills curriculum. Every Artisan is trained against it during onboarding, and the monthly bench audit (Chapter 12) samples work against these standards. The standards are not preferences; a repair that violates them fails QC even if the vehicle runs.

### 3.1 Bench discipline: how a professional RC tech works

**One vehicle, one tote, one tray-map.** Every job gets a labelled tote. Screws go into **magnetic parts trays**, and they go in *mapped*: tray positions mirror the vehicle — front-left screws in the tray's front-left quadrant, shock hardware grouped, diff hardware grouped. For deep teardowns, use a printed **screw map** — a laminated exploded-view card per fleet platform with adhesive-magnet zones — or the low-tech version: a strip of masking tape, sticky-side up, screws in removal order with pencil notes. An Artisan who dumps thirty screws into one tray is signalling that reassembly will be archaeology.

**Photograph before you disturb.** Two phone photos into the RC WORLD OS job ticket before teardown: linkage geometry, wire routing, shock positions. Thirty seconds now saves twenty minutes of "which hole was the camber link in".

**Clean before you open.** Never open a gearbox on a dusty chassis. Blow down at intake, brush, then crack cases. One grain of Track B grit inside a fresh diff undoes the whole rebuild.

**Finish the state, not just the job.** A job ends when: the vehicle passes QC, the tote is empty, the tools are back on their outlines, the parts used are logged in `maintenance_logs` (parts_used JSONB — this drives reordering, Chapter 8), and the vehicle status flips out of `maintenance`. Half-logged repairs poison the failure data that Chapter 9 and fleet purchasing depend on.

### 3.2 Torque discipline on small fasteners

RC fasteners are small enough that wrist-feel spans a 4:1 error band, which is the difference between loose and stripped. The Works' rules:

1. **Feel is calibrated, not assumed.** Every trainee spends a session with the Wiha/Wera torque screwdriver on scrap chassis until their "snug" reliably lands in band. Re-check yearly.
2. **The torque table.** Nominal values for steel screws; **into plastic or aluminum threads, use the lower bound and stop at first firm seat**:

| Fastener | Into metal (nut/steel insert) | Into aluminum | Into plastic (self-tap or molded boss) |
|---|---|---|---|
| M2 | 0.15–0.20 N·m | 0.12–0.15 N·m | seat + 1/8 turn max |
| M2.5 | 0.35–0.45 N·m | 0.25–0.35 N·m | seat, no extra |
| M3 | 0.55–0.80 N·m | 0.45–0.60 N·m | seat, no extra |
| M4 | 1.2–1.6 N·m | 0.9–1.2 N·m | seat, no extra |
| M4 wheel nut (nylock) | 0.9–1.1 N·m | — | — |

3. **Plastic threads are consumable.** A self-tapper into ABS survives perhaps 10 cycles before the boss strips. On high-service fasteners (body mounts, gearbox cases on the WLtoys fleet), the hardening pass converts to machine screws with threaded inserts or nuts wherever the platform allows.
4. **Torque-critical points get the torque driver, not feel:** motor mount screws (thermal cycling loosens them), pinion grub screws, flywheel/slipper nuts, and anything into a $50+ aluminum part.

> **Trade Hack.** When a plastic boss does strip, don't bin the part: a drop of thin CA in the hole, let cure fully, re-drive the screw — the CA shell re-forms a thread good for several more cycles. For a permanent fix, drill and fit the next screw size or a brass insert set with a soldering iron.

### 3.3 Threadlock rules: blue, not red

- **Blue (Loctite 243 or equivalent medium-strength) on every metal-into-metal joint**: grub screws on drive cups and pinions, motor screws, steel screws into aluminum bulkheads, shock caps with metal threads, wheel hex grub screws. One small drop on the leading threads; more is not better — excess migrates into bearings.
- **Red (Loctite 263/271) is banned from the fleet.** Red is a permanent grade that needs >230 °C to release; on an M3 in an aluminum part you will destroy the part before the bond lets go. There is no fastener on an RC vehicle that legitimately needs it. The one red-adjacent exception: **green retaining compound (Loctite 638)** for bearing outer races spinning in worn aluminum bores — applied by the Workshop Lead only, logged on the ticket.
- **Never threadlock into plastic.** Most anaerobic threadlockers stress-crack polycarbonate, ABS and nylon. Plastic joints rely on correct torque and nylock nuts.
- **Purple (222) for M2 and smaller** where blue's breakaway torque would round the tiny socket before the bond releases.

### 3.4 Bearing craft

- **Seat with a press, never a hammer.** Use the stepped-drift kit; press on the race being fitted (outer race into a housing, inner race onto a shaft) — pressing through the balls brinells the races and the bearing is dead before it turns.
- **Square is everything.** Start the bearing by hand, feel it sit square, then press. A bearing that goes in crooked and is forced will gall an aluminum bore permanently.
- **Cleaning protocol:** post-water/mud Shifts, bearings out, dunk-and-swish in isopropyl or the ultrasonic cleaner, spin-dry with air at low pressure (hold the races — free-spinning a dry bearing with an air jet over-revs and pits it), then re-oil (light bearing oil for racing fleet, marine grease pack for boats and anything in the water-splash zone).
- **Rubber-sealed (2RS) for the fleet, metal-shielded (ZZ) only indoors.** The 0.5% drag penalty of rubber seals is irrelevant in a rental fleet; the grit exclusion is not.

### 3.5 Gear mesh: the paper-strip method

Pinion-to-spur mesh is the most frequently botched adjustment in RC. Too tight destroys bearings and eats the spur; too loose strips teeth on the first jump landing.

1. Cut a strip of ordinary printer paper (~80 gsm, ≈0.1 mm).
2. Lay it between pinion and spur; rotate the gears to feed it into the mesh.
3. Set the motor position so the gears **lightly grip** the paper, tighten the motor screws (blue threadlock).
4. Remove the paper. Correct mesh has *just perceptible* backlash — rock the spur with the pinion held; you should feel a tick of free play, not a clunk, not silence.
5. **Check at four points around the spur.** Spurs are seldom perfectly concentric; set mesh at the tightest point or the tight spot will bind.

Metal-gear transmissions on the construction fleet run slightly looser mesh (two paper thicknesses) with grease; sealed lead-screw actuator gears are set at the factory and are not adjusted, only inspected and greased.

### 3.6 Servo craft: center before you install

The cardinal rule: **a servo is centered electronically before the horn goes on, every time.**

1. Connect the servo to the bench servo tester, set to neutral (1,500 µs).
2. Fit the horn as close to the required angle as the spline allows; correct residual error with the tester's sub-trim display, and record the offset on the job ticket if it exceeds ±3°.
3. Install, connect linkage, then set end points (EPA) on the transmitter/receiver so the servo **never stalls against a mechanical stop** — a stalled 25 kg servo draws amps until something (gear teeth, BEC, wiring) gives.
4. Steering servos on the rental fleet get a **servo saver** verified at every service: compress by hand; if it doesn't give before the servo does, re-shim or replace the spring.

Construction fleet note: boom/bucket functions on the lead-screw machines use limit micro-switches, not servo EPA — test both limits under no load before buttoning up (SOP-WS-011).

### 3.7 Wiring craft

**Strain relief is the standard, not the exception.** Every wire that leaves a PCB or connector gets mechanical support within 20 mm: a zip-tie anchor, a dab of silicone (Shoe Goo/E6000 class — never CA, which wicks and embrittles), or heat-shrink bridging onto the harness. The RCW Micro-Node spec mandates silicone strain relief at the solder pads (Chapter 14) because vibration kills solder joints by fatigue, not by force.

**Polarity conventions — park-wide law:**

- Battery main: **XT60**, red/positive to the beveled corners per Amass standard; Deans T-plug legacy packs accepted at intake but converted to XT60 at first service.
- Silicone wire colors: red = positive, black = negative, **never repurposed**. Signal wiring follows JR/Futaba servo convention: brown/black = ground, red = center positive, orange/white/yellow = signal.
- Balance leads: JST-XH, keyed; never extended with unkeyed pin headers.
- RCW Heavy-Node field connectors: JST-XH 2.5 mm positive-latch per the telemetry spec.

**Heat-shrink standards:** 2:1 ratio adhesive-lined shrink on every splice and battery-lead joint; wall thickness matched so the shrunk sleeve grips the insulation, not just the joint; shrink extends ≥5 mm past exposed conductor each side; heat gun, not lighter (soot hides inspection). No electrical tape anywhere on the fleet — it unwraps in heat and marks an amateur repair.

**Routing:** power (battery/ESC/motor) and signal (receiver/Node) looms separated where the chassis allows; wires never touch the motor can (it hits 70–90 °C); no wire crosses a pivoting suspension member without a service loop.

### 3.8 Solder-joint quality criteria

A joint passes if **all** are true:

- [ ] Bright (leaded) or uniformly satin (lead-free) surface — a grainy, lumpy joint is disturbed or cold
- [ ] Concave fillet wetted to both surfaces — solder flowed, not blobbed
- [ ] Conductor outline faintly visible through the solder on wire-to-pad joints
- [ ] No wicking of solder up stranded wire beyond the joint (stiffened wire fatigues and snaps at the wick line — this is the #1 field failure of amateur battery-lead repairs)
- [ ] No flux charring, no melted insulation, no stray strands
- [ ] Passes a firm tug (wire joints) — the tug test is mandatory, not optional

Technique standards: 63/37 leaded at 320–350 °C for bench work on wiring and Nodes (easier inspection, lower temp); chisel tip sized to the joint — **XT60 and 12 AWG battery leads take the 100 W iron with a ≥5 mm chisel**, never the fine-tip station (a small iron held on for 20 seconds heats the whole connector, melts the housing and cooks the wire; a big iron finishes the joint in 3 seconds). Tin both parts first; join; hold still through solidification.

> **Safety Warning.** Battery-lead soldering is the one soldering job with a short-circuit hazard. One lead at a time, the other lead's connector taped or capped; never cut both battery leads in one scissor stroke — the cutter blades become a dead short across a charged pack.

### 3.9 The Artisan skill ladder

The craft standards above map to the three-grade internal ladder (HR detail in Volume 1; customer-facing titles unchanged — everyone is an "Artisan"):

| Grade | Gate (assessed at bench audit) |
|---|---|
| Artisan I (trainee) | Tier-1 kit fluency; daily inspections; tire, body, servo, wheel/hub swaps; solder joints pass §3.8 on wire splices |
| Artisan II | Full drivetrain rebuilds (diff, shocks, transmission); ESC programming; battery-lead work; RCW Node installation; owns SOPs solo |
| Artisan III (lead) | Lathe work; FMEA facilitation; QC sign-off authority; custom builds (Chapter 13); Node assembly QC (Chapter 14); trains I & II |

---

## 4. RC Trade Hacks

Everything in this chapter is a sanctioned, field-proven technique. Each entry states *when* to use it and *why it works*. Hacks marked ⏱ are pit-lane legal (fast enough for a 20-minute Shift turnaround); the rest are bench hacks. None of them replaces the proper repair when the SOP calls for one — a hack buys time or saves a part; it does not close a job ticket unless the ticket says so.

1. **Toothbrush + low-pressure air for dust.** ⏱ Agitate with a stiff toothbrush while blowing at ≤3 bar. *Why:* the brush breaks static cling and packed dust in corners the air jet skates over; low pressure avoids driving grit past bearing seals.
2. **Dental picks for e-clips.** Hook-pattern dental pick to roll e-clips off shock shafts and hinge pins — roll them *around* the groove, don't pry outward. *Why:* prying launches the clip into orbit; rolling keeps it captive on the tool.
3. **Fit e-clips inside a clear bag.** Cheap insurance for the smallest clips: work inside a zip-lock; when the clip pings, it hits plastic, not the floor. *Why:* a lost 2 mm e-clip is a 10-minute search or a stalled job.
4. **Fuel tubing as a screw gripper.** Slip 20 mm of silicone fuel tubing over a driver tip; it grips the screw head enough to start screws in deep recesses one-handed. *Why:* friction sleeve beats magnetizing drivers near sensored motors and receivers.
5. **Fuel tubing as shock-shaft protector.** Slide tubing over the shock shaft threads before pushing through the seal head. *Why:* threads cut seals; tubing gives the seal a smooth ramp.
6. **CA + baking soda structural fill.** ⏱ Pack baking soda into a crack (chassis brace, body post base), drip thin CA — it flashes off *instantly* into a hard, sandable composite. *Why:* the soda accelerates cure and bulks the CA into a gap-filler; a field repair strong enough to finish the day. Ventilate — the flash reaction fumes sting.
7. **Shoe Goo tire saves.** A torn tire sidewall or unglued section re-attached with Shoe Goo/E6000, zip-tie or rubber-band clamped overnight. *Why:* stays flexible, unlike CA which makes a hard hinge point that re-tears; saves $15 tires by the dozen in a rental fleet.
8. **Zip-tie temporary body mounts.** ⏱ Snapped body post → zip-tie loop through the shell hole to any chassis anchor; foam pad under the shell. *Why:* returns the vehicle to the Shift roster instantly; proper post fitted at end-of-day.
9. **Drybox with indicating silica for electronics.** Any receiver, ESC, servo or Node that took water goes into the silica cabinet overnight *after* an isopropyl rinse of accessible boards. *Why:* IPA displaces water from board surfaces; silica finishes trapped moisture. Rice is a myth — it barely absorbs.
10. **Pencil graphite on sliding plastics.** Rub a soft pencil on battery-strap slides, body-clip channels, telescoping antenna tubes. *Why:* dry graphite lubricates without attracting the dust that grease-lubed slides collect in a dirt park.
11. **Freezer trick for stuck bearings/pins.** Frozen assembly (−18 °C, 30 min) shrinks the steel inner components faster than the aluminum housing warms — press the part out immediately on removal. Reverse trick: warm the aluminum hub with the heat gun to 80–100 °C to drop bearings out. *Why:* differential thermal expansion, ~2× coefficient difference between aluminum and steel.
12. **O-rings as shock preload spacers.** ⏱ No clip-on spacers at hand? Stretch appropriately sized O-rings over the shock body. *Why:* instant, reversible ride-height tweak in ~1 mm steps; also quiets a rattling preload collar.
13. **Wheel nut in a nut driver, wheel-first.** ⏱ Drop the nylock into the 7 mm driver, offer the driver to the axle. *Why:* one-handed wheel changes; the driver holds the nut captive so pit-stop tire swaps take seconds and nuts stop vanishing in the pit-lane gravel.
14. **Masking-tape screw timeline.** For unfamiliar teardowns: screws stuck to sticky-side-up tape in removal order with pencil notes. *Why:* reassembly is the tape in reverse; beats memory on a machine you see twice a year.
15. **Body shell as a parts bowl — never.** Anti-hack that earns a mention because everyone does it: shells flex, screws slide to the floor. Totes and magnetic trays exist. *Why listed:* audit item.
16. **Turnbuckle length by calipers, not counting flats.** Set one side's link, measure center-to-center with calipers, clone to the other side. *Why:* faster and more accurate than counting turns; keeps toe/camber symmetric to <0.5°.
17. **Hot-glue balance weights.** Stick-on chassis weights secured with a hot-glue bead over the top. *Why:* stick-on adhesive fails at the first wet Shift; hot glue peels off cleanly when re-balancing.
18. **Heat-shrink servo-lead labels.** ⏱ White heat-shrink + fine marker on every servo/Node/receiver lead ("ST", "TH", "NODE"). *Why:* five seconds at build time saves every future disconnect/reconnect from the plug-swap lottery.
19. **Grease the balance-plug rubber.** A whisper of dielectric grease on JST-XH balance plugs. *Why:* they seize into charger boards and the wires pull out of the housing when yanked; grease means the housing comes out, not the pins.
20. **The "second pair of hands" is a vice + tape.** Solder XT60s with the connector mated to a scrap opposite-gender plug held in the Panavise. *Why:* the mated plug heat-sinks the pins in correct alignment — no melted housings, no misaligned pins.
21. **Diff fluid by scale, not eye.** Fill diffs by grams on the 0.1 g scale (record per platform, e.g. "1/10 touring gear diff: 1.3 g of 3,000 cSt"). *Why:* repeatable across the fleet; "fill to the gears" varies ±30% by Artisan.
22. **Old spur gears become paint stands.** Screw a used spur to a stick — instant rotating mount for painting small parts. *Why:* free fixtures from the scrap bin; the machining corner keeps a jar.
23. **CA-hardened thread rescue.** Stripped plastic boss → drop of thin CA, cure, re-tap with the screw (see §3.2). *Why:* CA shell re-forms a serviceable thread; costs nothing.
24. **Toothpaste as plastic polish.** Non-gel toothpaste polishes scuffed polycarbonate windscreens and lexan. *Why:* it's a fine abrasive paste; mild cutting compound in a pinch, and it's already in the staff kitchen.
25. **Velcro battery "gate".** ⏱ Adhesive hook-and-loop strip on the battery tray floor plus the strap. *Why:* stops pack sliding under crash loads that a strap alone allows; ejected packs rip their own leads.
26. **Track-pin keeper wire.** On excavator tracks, a 0.8 mm stainless safety wire twisted through the master-pin hole. *Why:* Huina-class master pins walk out under side-load; the wire converts a track-throw field failure into a QC-lane observation.
27. **Sacrificial XT60 "keys".** A box of XT60 plugs with the leads cut short and soldered into a loop, painted red, hung at the charging room door. *Why:* inserted into every stored pack as a "this pack is at storage charge" flag that's visible from across the room — process state made physical.
28. **Hot water for tight tires.** Soak new tires/inserts in hot (~70 °C) water for 2 minutes before mounting on rims. *Why:* softened carcass seats into the bead channel without stretching or tearing; also helps remove glued tires non-destructively along with a heat-gun pass.
29. **Motor-spray nothing — use IPA and air.** "Motor spray" solvents strip commutator lubricant films and attack some insulation. Brushed motor cleaning = IPA dip for accessible parts, air, then re-oil bushings; real restoration = comm skim on the lathe. *Why:* the aggressive aerosol shortcut costs motor life; the lathe pays for itself (§2.5).
30. **Binder clips as wing/wire clamps.** Small binder clips clamp glued tire sections, hold wiring looms while silicone cures, and act as third hands on body work. *Why:* $3 buys twenty clamps sized perfectly for RC-scale work.

> **Field Note.** The hacks list is a living document. Any Artisan may propose a new hack; the Workshop Lead trials it, and accepted hacks get a number, an entry here, and — the real prize — the proposer's name in the revision log. Rejected hacks get a line in the "do not do" appendix with the reason, which is how institutional scar tissue is supposed to work.

---

## 5. Standard Operating Procedures

### 5.1 SOP system rules

- SOP IDs: `SOP-WS-###` (workshop), owned by the Workshop Lead; revisions logged in RC WORLD OS; the printed laminate at the bench must show the current revision number or it is invalid.
- Every SOP execution that touches a vehicle creates/updates a `maintenance_logs` row. No log, no work.
- PPE baseline everywhere in The Works: safety glasses at any bench with rotating machinery, cutting, springs/clips under load, soldering or chemicals. SOP blocks list only *additional* PPE.
- Steps marked **QC** require sign-off by a second Artisan (grade II+) before the vehicle leaves `maintenance` status.

### 5.2 SOP-WS-001 — Vehicle Intake & Triage

> **SOP-WS-001** · Rev 1.0 · Owner: Workshop Lead · PPE: baseline · Tools: air station, brush, cell checker, RC WORLD OS kiosk · Frequency: every vehicle entering The Works

1. Scan asset tag; kiosk opens a job ticket and flips status to `maintenance`.
2. Remove battery; check per-cell voltage. <3.4 V/cell → tag pack and route to Battery Room quarantine shelf with the ticket number (over-discharge protocol, §10.4).
3. Blow down and brush at the intake station (≤3 bar).
4. 2-minute triage: wheels/steering free, visible damage, radio bind check, drivetrain rotation by hand, telemetry last-fault review from the Node feed (under-voltage events, kill-switch triggers, impact G if reported).
5. Assign triage class A/B/C (Chapter 7 definitions) and estimated bench minutes; place vehicle + tote on the matching queue shelf.
6. Photograph damage into the ticket.

### 5.3 SOP-WS-002 — Daily Fleet Inspection (pre-open)

> **SOP-WS-002** · Rev 1.0 · Owner: Duty Artisan · PPE: baseline · Tools: Tier-1 kit, cell checker, transmitter · Frequency: daily, before park open; ~90 s per vehicle, split across Artisans by zone

Per vehicle:

- [ ] Asset tag legible; body clips present; shell crack-free at mounts
- [ ] Wheel nuts snug (7 mm driver pass); tires glued, no tears; wheel hexes not wallowed
- [ ] Steering: full lock both ways under power, returns to center, no servo buzz at neutral
- [ ] Drivetrain: hand-roll — smooth, no clicking (clicking = CVD or diff, pull it)
- [ ] Suspension: drop test — settles without binding; shock shafts not bent, no oil film
- [ ] Battery bay: strap + velcro secure; XT60 housing intact, no browned pins
- [ ] Radio: bind, throttle/steering direction, failsafe holds neutral on TX power-off
- [ ] Node heartbeat visible on the RC WORLD OS grid map; voltage telemetry matches cell checker ±0.05 V/cell
- [ ] Construction fleet add: boom/bucket full travel, limit switches stop the lead-screw at both ends; tracks tensioned (excavators: 5–8 mm sag mid-span)
- [ ] Log pass/fail; failures open a ticket automatically

### 5.4 SOP-WS-003 — Post-Crash Inspection

> **SOP-WS-003** · Rev 1.0 · Owner: any Artisan II+ · PPE: baseline · Tools: Tier-1 kit, setup gauges · Frequency: after any marshal-reported major impact or Node impact flag

1. Confirm battery seated and leads undamaged **before** any power-on test.
2. Squeeze-test each suspension arm and knuckle (hairline cracks whiten under flex on nylon).
3. Check hinge pins straight (arms swing free), shock shafts straight (extend/compress by eye), turnbuckles straight (roll on the bench).
4. Wheel run-out check on a spin; bent hexes/axles replaced, not straightened.
5. Chassis flex test: hold diagonal corners, twist gently, watch for tub cracks at bulkhead screws.
6. Gear mesh re-check (impacts shift motor mounts): paper-strip method §3.5.
7. Steering trim on the bench ±: if sub-trim needed >5 µs from the setup sheet, geometry is bent somewhere — find it.
8. **QC** if any structural part replaced; otherwise return to service and log "post-crash, NFF" (no fault found) — NFF rates per platform feed Chapter 9.

### 5.5 SOP-WS-004 — Brushed Motor Replacement (540/550 fleet)

> **SOP-WS-004** · Rev 1.0 · Owner: Artisan I+ · PPE: baseline · Tools: 2.0/2.5 mm hex, torque driver, watt meter, blue threadlock · Frequency: on failure or PM flag (§6)

1. Photograph wire routing; desolder or unplug motor tabs (note polarity — swapped tabs on brushed = reversed rotation).
2. Remove pinion (note tooth count on ticket), motor screws, motor.
3. New/refurbished motor: bench-spin at 3 V on the PSU — current draw within table (§12.3) confirms brushes seated; if refurbished, comm was skimmed and bushings oiled per §2.5.
4. Fit pinion at recorded position (grub screw on the shaft flat, blue threadlock, 1.5 mm hex).
5. Mount motor, set mesh (paper strip), torque motor screws 0.55–0.8 N·m with threadlock.
6. Reconnect; full-throttle free-rev ≤5 s with watt meter inline — log free current.
7. **QC**: load test on rollers, temperature by IR gun after 2 min ≤ 45 °C above ambient.

### 5.6 SOP-WS-005 — ESC Replacement & Programming

> **SOP-WS-005** · Rev 1.0 · Owner: Artisan II+ · PPE: baseline; ESD strap when case open · Tools: 100 W iron, program card, laptop, watt meter · Frequency: on failure

1. Pull the fleet ESC profile sheet for the platform from the RC WORLD OS platform register (racing profiles are specified in Volume 3, Chapter 5; construction profiles in Volume 4, Chapter 4).
2. Replace unit; battery-lead and motor-lead joints per §3.8 (100 W iron, adhesive shrink; one lead at a time).
3. Program: cell-count/LVC **hard cutoff 3.4 V/cell** (park doctrine — the ESC is the last line behind the Node's soft intervention), punch/drag-brake/reverse per profile, thermal cutoff ON.
4. Calibrate throttle range to the transmitter (full/neutral/brake endpoints).
5. Verify Node PWM intercept still in circuit — receiver → Node → ESC, not receiver → ESC (Chapter 14 wiring).
6. **QC**: rollers under load; confirm LVC triggers at 3.4 V/cell using the bench PSU ramped down through the threshold; confirm kill command from RC WORLD OS drops throttle to neutral <1 s.

### 5.7 SOP-WS-006 — Servo Replacement

> **SOP-WS-006** · Rev 1.0 · Owner: Artisan I+ · PPE: baseline · Tools: servo tester, Tier-1 kit · Frequency: on failure or PM flag

1. Center new servo on the tester (§3.6); confirm current draw at neutral <10 mA (buzzing/hunting servo = reject).
2. Match spline horn; transfer servo-saver; install with rubber isolation grommets and brass eyelets correctly stacked (eyelet flange *under* the grommet, screw torque to seat only).
3. Connect linkage; set EPA so neither lock stalls the servo; verify at full lock the current draw <1.5 A on the bench PSU.
4. Heat-shrink label the lead; route clear of the motor.
5. **QC** only if steering geometry parts were also replaced; otherwise self-check drive test on the strip.

### 5.8 SOP-WS-007 — Differential Rebuild (gear diff, 1/10 fleet)

> **SOP-WS-007** · Rev 1.0 · Owner: Artisan II+ · PPE: nitrile gloves (silicone fluid) · Tools: Tier-1 kit, 0.1 g scale, diff fluid set, paper towels · Frequency: 100-cycle PM or on failure

1. Pull diff per platform manual; totes and tray-mapping mandatory — diff shims are position-critical.
2. Open case; inspect: gear teeth (chipping = replace set), cross-pins (grooving), O-rings and gasket (always replace — $0.40 parts protecting a 45-minute job).
3. Clean all parts in the ultrasonic; dry.
4. Refill by weight from the platform sheet (e.g. touring gear diff 1.3 g of 3,000 cSt; buggy front 2.0 g of 5,000 cSt — see register). Pump the gears to burp air, top to weight.
5. Reassemble with new gasket; torque case screws in a cross pattern to lower-bound M2.5 values (plastic case).
6. Reinstall; reset ring/pinion shims to factory backlash where applicable; grease outdrives' CVD cups (black CV grease).
7. **QC**: wheels-off spin test — both wheels drive, diff action smooth; road test on the strip with two tight figure-8s; no clicking.

### 5.9 SOP-WS-008 — Shock Rebuild

> **SOP-WS-008** · Rev 1.0 · Owner: Artisan I+ (pair build with II first time) · PPE: nitrile gloves · Tools: shock pliers, fuel-tubing shaft sleeve, oil stand, dental pick · Frequency: 100-cycle PM (racing), season (crawler/construction), or leak

1. Shocks off in pairs (front pair / rear pair — never mix rebuilt with unrebuilt on one axle).
2. Strip: cap, spring, seal cartridge; e-clip technique §4-hack-2; sleeve the shaft threads (hack 5) before pulling through seals.
3. Inspect shafts (pitting/bend = replace), pistons (wear ovality), seals & O-rings (replace every rebuild — kit cost $1–2).
4. Fill: platform oil weight from the register (e.g. touring 400 cSt, buggy 550 front/450 rear, crawler 300); bleed method per shock type (emulsion vs bladder); set rebound per setup sheet (touring: 2–3 mm rod push-out).
5. Match the pair: both shocks compressed slowly side-by-side must feel identical; if not, re-bleed.
6. Refit; drop-test the corner; ride height check against setup sheet.

### 5.10 SOP-WS-009 — Tire Mounting & Gluing

> **SOP-WS-009** · Rev 1.0 · Owner: Artisan I+ · PPE: nitrile gloves, ventilation (paint bench), glasses · Tools: CA thin, activator, rubber bands, hot-water bath · Frequency: continuous (highest-volume SOP in the building)

1. Wash rims and tire beads with IPA; dry fully (CA + damp = white bloom and weak bond).
2. Insert foams seam-opposite the tire seam; hot-water soak for tight carcasses (hack 28).
3. Seat tire; check bead fully home all round both sides.
4. Glue in 4 pulls per side: pull bead back, one drop of thin CA run 90° of circumference, release, press 10 s. Kicker spray only on the last pass (kicker embrittles if soaked into the joint).
5. Band the wheels or use mounting rings for 20 min minimum before service.
6. Batch rule: tires are glued in fleet batches at the paint bench, ≥8 wheels per session — per-wheel gluing at wrenching bays is banned (fume + quality variance).
7. Vent hole check: each tire has its vent open (blocked vents balloon at speed).

### 5.11 SOP-WS-010 — Track-Pin Replacement (excavators & dozers)

> **SOP-WS-010** · Rev 1.0 · Owner: Artisan I+ · PPE: baseline · Tools: pin punch set, small hammer + anvil block, safety wire, lithium grease · Frequency: on thrown/kinked track or 100-cycle PM finding

1. Slacken track tensioner fully; note shim/adjuster position on ticket.
2. Drive out the master pin with the matched punch on the anvil block — support the link, strike the pin.
3. Remove damaged links; inspect neighbours for elongated pin bores (light through the bore shows ovality) — replace any link with visible ovality; they cascade.
4. Rebuild with new pins from the spares bin (track pins are a CONTINUOUS-class consumable, Chapter 8); grease pins sparingly — a wet film attracts pit sand; "damp, not dripping".
5. Master pin gets the safety-wire keeper (hack 26).
6. Re-tension: 5–8 mm sag mid-span top run; sprocket alignment sight-check.
7. **QC**: 5-minute figure-8 in the test yard including one 15° ramp climb; watch tracking straightness.

### 5.12 SOP-WS-011 — Lead-Screw Actuator Service (construction fleet)

> **SOP-WS-011** · Rev 1.0 · Owner: Artisan II+ · PPE: baseline · Tools: Tier-1 kit, PSU, lithium grease, micro-switch spares · Frequency: 100-cycle PM per §6; on symptom (stall, chatter, drift)

1. Cycle the function full-travel on the bench PSU with the watt meter inline; log stall/running current against the platform baseline (rising running current = dry or fouled screw).
2. Strip the actuator cover; clean old grease and pit dust from the screw with brush + IPA (never air-blast — drives grit into the nut).
3. Inspect: screw straightness, nut backlash (axial shake at the carriage >0.5 mm = replace nut), thrust bearing feel.
4. Re-grease with white lithium, thin film full length; cycle 5× to distribute.
5. Test both **limit micro-switches**: manual trigger stops the motor; measure switch continuity; replace at the first sign of intermittence (MEDIUM-turnover spare — boom-limit switches are a known Huina weak point).
6. Reassemble; re-run current log; must be within 10% of baseline. **QC** on the premium showcase machines only.

### 5.13 SOP-WS-012 — Waterproofing Treatment

> **SOP-WS-012** · Rev 1.0 · Owner: Artisan II+ · PPE: gloves, ventilation (booth) · Tools: conformal coating, dielectric grease, balloon/finger cots, silicone sealant · Frequency: at fleet hardening (new vehicles) and after any electronics replacement on wet-zone fleets (crawler, marine support, agriculture)

1. Receivers: open case, acrylic conformal coat the board both sides masking the antenna pad and connector pins (booth only); reassemble with a silicone bead at the case seam and case-exit grommets.
2. Servos: case seams and wire exit sealed with silicone; do not coat the pot/board of budget servos — buy waterproof-rated units for wet fleets instead (spec in Volume 8).
3. ESCs: fleet standard is waterproof-rated ESCs on wet fleets; add dielectric grease in connector housings.
4. Node: RCW Nodes arrive conformal-coated from bench assembly (Chapter 14); verify coating date on the Node label.
5. Motor note: brushed cans tolerate water but flush + re-oil after immersion; bearings replaced per §3.4 cleaning protocol.
6. Log treatment date; wet-fleet vehicles carry a blue dot on the asset tag.

### 5.14 SOP-WS-013 — RCW Node Installation & Test

> **SOP-WS-013** · Rev 1.0 · Owner: Artisan II+ · PPE: ESD strap · Tools: soldering station, JST-XH crimp set, zip anchors, laptop, RC WORLD OS test screen · Frequency: fleet induction; Node swap

1. Confirm Node type: Micro-Node (~25×25 mm, solder pads) for racing platforms; Heavy-Node (~40×30 mm, JST-XH latching) for construction/agriculture.
2. Wire the PWM intercept: receiver throttle channel → Node input; Node output → ESC signal lead (full pinout in §14.3). Battery sense leads to the main pack terminals **downstream of the vehicle's main switch** (no parasitic overnight drain — doctrine).
3. Micro-Node: solder pads per §3.8, then silicone strain-relief blob bridging harness to board edge. Heavy-Node: latch all JST connectors, tug-test each.
4. Mount: double-sided foam + zip anchor, antenna area clear of carbon/metal, GPS patch (ATGM336H) sky-facing where the shell allows.
5. Power on; confirm on the bench test screen: heartbeat, MAC bound to asset tag in `fleet_inventory`, voltage reads pack ±0.05 V/cell, GPS lock within 120 s outdoors.
6. **QC**: kill-test — issue KILL from the admin screen; throttle must drop to neutral/brake <1 s; release restores control. Under-voltage test with bench PSU ramp: soft-limit intervention at 3.4 V/cell (throttle to 20%, pit order push) per doctrine.

### 5.15 SOP-WS-014 — Transmitter Binding & Failsafe Setting

> **SOP-WS-014** · Rev 1.0 · Owner: Artisan I+ · PPE: none · Tools: platform TX, bind plug/procedure card · Frequency: at induction, after RX/TX replacement, at any unexplained control glitch

1. One vehicle powered at a time on the bind bench (a live twin on the same model memory is how "possessed vehicle" reports happen).
2. Bind per platform card; confirm model memory name = asset tag.
3. **Failsafe: throttle → neutral (brake where supported), steering → hold**; set on the RX per manufacturer procedure.
4. Test failsafe by TX power-off at 30% throttle on the rollers: wheels must stop.
5. Range check: TX low-power mode, 30 m walk-out, full control authority.
6. Log firmware/model-memory version. Note: failsafe is *independent of* the Node kill-switch — both must pass, they cover different failure modes (RF loss vs park-command).

### 5.16 SOP-WS-015 — End-of-Day Shutdown

> **SOP-WS-015** · Rev 1.0 · Owner: Duty Artisan (closing) · PPE: baseline · Tools: cell checker, kiosk · Frequency: daily, after last Shift

- [ ] All vehicles scanned back; RC WORLD OS grid shows zero assets on-field
- [ ] Every battery out of every vehicle — no pack sleeps in a vehicle, ever
- [ ] Packs sorted: ≥3.9 V/cell resting → discharge queue shelf; 3.80–3.85 → storage racks; <3.7 → charge-to-storage queue (Chapter 10 logic)
- [ ] Chargers: all cycles complete or attended-charging ended; bunker power master OFF except storage-mode smart chargers on the interlocked circuit
- [ ] Soldering stations, heat guns, PSUs off at the power rails; compressor drained (moisture)
- [ ] Benches clear, tools on outlines, totes shelved with tickets
- [ ] Repair queue board reconciled with RC WORLD OS for tomorrow's loading (Chapter 7)
- [ ] Battery Room and Charging Room locked; thermal camera/alarm armed
- [ ] Walk the floor for stray packs — the closing Artisan signs the shutdown log; this signature is the one the insurer will read

> **Safety Warning.** The two non-negotiable lines in SOP-WS-015 are "no pack sleeps in a vehicle" and the signed walk-through. Nearly every RC facility fire in hobby-community memory traces to an unattended pack left connected or charging overnight.

---

## 6. Preventive Maintenance System

### 6.1 Cycle-based, not calendar-based

Calendar PM wastes labor on garage queens and misses the weekend workhorses. RC WORLD OS gives every asset two odometers — **battery cycles** (packs issued against the asset) and **runtime hours** (Node telemetry, `total_hours_run`) — and PM triggers on whichever threshold arrives first. A battery cycle approximates one Shift; the conversion for planning is ~0.33 h runtime per cycle.

PM tiers:

| Tier | Trigger | Bench time | Who |
|---|---|---|---|
| Daily | park open | 90 s/vehicle | Duty Artisans (SOP-WS-002) |
| Minor ("25-cycle") | 25 cycles or 8 h | 10–15 min | Artisan I+ |
| Major ("100-cycle") | 100 cycles or 33 h | 45–90 min | Artisan II+ |
| Season | 6 months or 600 cycles | half day | Artisan II/III |

RC WORLD OS raises a PM flag at 90% of threshold and hard-blocks Shift assignment at 115% — a vehicle cannot be booked past its overdue PM (fleet-management module, Volume 13).

### 6.2 Minor service (25-cycle) — all families

- [ ] Full blow-down and brush; shell off; chassis visual
- [ ] Fastener pass with torque driver on the platform's "loosens in service" list (motor mount, servo mount, shock towers, wheel nuts, pillow balls)
- [ ] Bearings: spin-feel at each wheel; gritty = pull and clean or replace
- [ ] Gear mesh check; slipper clutch setting where fitted (push-test: slips on wheel-held throttle blip, doesn't slip on rolling launch)
- [ ] Connectors: XT60 pin browning, servo plugs seated, Node leads secure
- [ ] Tires: wear, glue joints, vent holes; tread depth vs class minimum
- [ ] Node: heartbeat, voltage-agreement check vs cell meter
- [ ] Log in `maintenance_logs`; 6-line form, target 12 min

### 6.3 Major service (100-cycle) — family-specific matrix

| Task | Touring/GT | Drift | Buggy/SC | Crawler | Excavator | Dump/Loader/Dozer | Tractor |
|---|---|---|---|---|---|---|---|
| Shock rebuild (SOP-WS-008) | ● | ● | ● | ● | — | — | — |
| Diff service (SOP-WS-007) | ● | ● | ● | ● (+lockers check) | — | ● (axles) | ● |
| Drivetrain teardown: CVDs, cups, spur/pinion wear | ● | ● | ● | ● | drive sprockets | ● | ● |
| Bearing full pass (clean/replace) | ● | ● | ● | ● | ● | ● | ● |
| Motor: brushless — sensor lead + bearing check; brushed — brush length, comm condition, skim if grooved | ● | ● | ● | ● | ● | ● | ● |
| Steering rack/servo-saver wear | ● | ● | ● | ● | — | ● | ● |
| Lead-screw service (SOP-WS-011) | — | — | — | — | ● boom+bucket+swing | ● bed lift / bucket | hitch lift |
| Track service: pins, links, tension, idler bearings | — | — | — | — | ● | dozers | — |
| Body/roll-cage fastener + mount inspection | ● | ● | ● | ● | cab | bed pivots | ● |
| ESC profile audit vs register | ● | ● | ● | ● | ● | ● | ● |
| Waterproofing integrity (wet-zone fleets) | — | — | — | ● | — | — | ● |
| Setup sheet re-baseline (parity program, Vol. 3) | ● | ● | ● | — | — | — | — |

Phase 2 families: **aircraft** follow a flight-hours regime (25 flights minor / 100 flights major: prop + spinner torque, control-linkage slop, elevator/aileron servo current draw, netting-strike airframe inspection) — detail lives in Volume 5's airworthiness annex; **boats** follow runtime (flex-shaft grease every 4 h — the dominant marine PM item, hull integrity, water-cooling loop flush, sacrificial-anode check on pond hardware) — detail in Volume 6. Both fleets' PM flags run through the same RC WORLD OS engine.

### 6.4 Season service (6-month)

Frame-off teardown to the bare chassis; every bearing out; every fastener re-threadlocked; wiring loom re-shrink where chafed; Node re-flash to current firmware + coating inspection; ESC thermal paste/heatsink renewal; full setup re-baseline and parity lap verification (racing); repaint/retire decision on shells; formal retire/rebuild economic call per asset (>60% of replacement cost in cumulative parts = retire to the donor shelf, Chapter 8).

### 6.5 Lubrication chart

| Point | Product (example) | Interval | Note |
|---|---|---|---|
| Gear diffs | Silicone diff fluid 1k–10k cSt (Team Associated/TLR/Traxxas lines) | 100-cycle | By weight, per platform register |
| Shocks | Silicone shock oil 250–600 cSt | 100-cycle | Pairs matched; log batch |
| CVD/dogbone cups | Black molybdenum CV grease (MIP/ProTek) | 100-cycle | Sparingly — attracts grit |
| Lead-screws | White lithium grease | 100-cycle | Thin film; never air-blast the nut |
| Track pins | Lithium grease, damp film | on service | "Damp, not dripping" |
| Wheel/transmission bearings | Light bearing oil (Team Associated FT or sewing-machine grade) | 25-cycle spot / 100-cycle full | After solvent clean only |
| Servo gears (metal) | Clear servo grease (Traxxas 1647 class) | on rebuild | Micro amount on load faces |
| Sliding plastics (battery slides, clips) | Pencil graphite | as needed | Hack 10 — no wet lube |
| Boat flex-shafts | Marine/flex-shaft grease | every 4 h runtime | Volume 6 owns detail |
| O-rings & seals | Green slime / silicone O-ring grease (Associated 6588 class) | at rebuild | Assembly lube, prevents seal nicks |
| Motor bushings (brushed) | Light machine oil, 1 drop | 100-cycle | Never on the commutator |

> **Trade Hack.** Buy diff fluids and shock oils in one brand family and never mix brands within a class: "3,000 cSt" is not perfectly standardized across manufacturers, and fleet parity (Volume 3's 2–3% rule) depends on repeatability more than on the absolute number.

### 6.6 PM capacity load

At steady state the PM engine generates, per 100 fleet-wide daily cycles: ~4 minor services (48 min) and ~1 major (75 min) — call it **2 bench-hours per 100 cycles**. A 230-cycle average day (Chapter 7's utilization case) therefore books ~4.5 bench-hours of PM on top of corrective work. This number sizes the Artisan roster in Chapter 7 and is the reason PM is scheduled into the morning trough, before the park's afternoon peak loads the corrective queue.

---

## 7. Repair Scheduling & Workflow

### 7.1 Triage classes and SLAs

Every intake ticket (SOP-WS-001) gets a class:

| Class | Definition | Examples | Turnaround SLA | Queue rule |
|---|---|---|---|---|
| **A — Pit-fixable** | ≤10 bench-minutes, no QC sign-off parts | Tire swap, body clip, wheel nut, re-bind, zip-tie body mount (hack 8) | Same Shift where possible; ≤2 h | Worked immediately at the triage bench |
| **B — Bench repair** | 10–90 min, standard spares on shelf | Servo, motor, diff, shocks, arms/knuckles, ESC swap | Back in fleet ≤24 h | FIFO within class, priority bump if class availability <buffer |
| **C — Major / waiting** | >90 min, parts on order, structural, or economic-retire assessment | Chassis tub, transmission case, water-damaged electronics set, premium hydraulic showcase faults | ≤7 days or formal retire decision | Workshop Lead schedules; donor-shelf harvest allowed |

The SLA is measured by RC WORLD OS from status-change timestamps and reported on the workshop KPI dashboard (§7.5). The class-availability buffer rule: each vehicle class must keep **≥85% of its fleet count available** during operating hours; when a class dips below buffer, its class-B tickets jump the queue.

### 7.2 Bench loading: the worked math

Assumptions (base case, Year 1 steady state; sources: Volume 10 revenue model, Volume 3/4 utilization):

- Fleet ≈ 150 powered assets; average utilization ≈ **230 Shifts/day** park-wide (85,000 Shifts/year ÷ 365, smoothed), peak weekend days ≈ 420.
- Corrective ticket rate (industry-informed planning figure, to be replaced by our own `maintenance_logs` data within one quarter): **1 ticket per 25 Shifts** overall = 4% per Shift, distributed A/B/C ≈ 55/38/7%.

Average day:

- Tickets: 230 ÷ 25 ≈ **9.2/day** → 5.1 class A, 3.5 class B, 0.6 class C.
- Bench minutes: A ≈ 5.1 × 8 min = 41; B ≈ 3.5 × 45 min = 158; C ≈ 0.6 × 150 min = 90. **Corrective total ≈ 4.8 h.**
- PM load (§6.6): 230 cycles → **≈4.5 h.**
- QC lane + intake/triage overhead ≈ 20% of the above ≈ 1.9 h.
- **Total ≈ 11.2 bench-hours/day** average; peak day scales to ≈ 20 bench-hours.

Roster consequence: an Artisan yields ~5.5 productive bench-hours per 8-hour shift (the rest is pit-lane support, customer-facing work, 5S). Average day needs **2.0 bench-Artisans**, peak day **3.6**. Phase 1 roster: **4 Artisans + Workshop Lead** covering a 7-day rota gives 2–3 on duty weekdays and 4 on weekends — consistent with the payroll model in Volume 10. The four wrenching bays therefore run at ~60% occupancy on peaks, which is the correct margin: a bay-saturated workshop converts every bad crash-day directly into lost Shifts.

> **Investor Note.** The 1-per-25-Shifts failure rate is the plan's most consequential engineering assumption after battery life. It is deliberately conservative (hobby-forum rental operators report anywhere from 1/15 unhardened to 1/40 well-hardened); the hardening pass (Volume 3 §12.2) and this volume's PM system exist to push the real number toward 1/40. Every point of improvement is ~1 bench-hour/day, i.e. most of an Artisan salary at scale.

### 7.3 Queue management in RC WORLD OS

The repair queue is a Kanban board in the artisan interface (Volume 13): columns **Intake → Triage → Queued (A/B/C swimlanes) → On Bench → Waiting Parts → QC → Fleet Staging**. Rules enforced by software, not memory:

- A ticket cannot enter *On Bench* without an Artisan and a bay assigned; a bay holds one active ticket.
- *Waiting Parts* auto-links to the inventory module; when the bin scan or PO receipt lands, the ticket bounces back to *Queued* at the head of its class.
- Vehicles in *QC* block their asset from booking until sign-off (the fleet state stays `maintenance`; Volume 13 §6.3).
- The board's aging alarm turns any B ticket amber at 18 h and red at 24 h (SLA), and pushes a notification to the Workshop Lead.

The physical mirror: queue shelving at intake is labelled by class and the shelf tag holds the tote + ticket. Physical position and board column are reconciled at end-of-day (SOP-WS-015).

### 7.4 Spares kanban

Repair speed is inventory speed. High-turnover spares run a **two-bin kanban**: two labelled bins per SKU on the wrenching-bay rack; when the front bin empties, the Artisan drops the bin card into the reorder slot and pulls the back bin forward. The storekeeper (a rotating Artisan duty, 30 min/day) scans dropped cards into RC WORLD OS, which raises the purchase requisition against the Volume 8 supplier register. Min/max levels in Chapter 8.

### 7.5 Workshop KPI dashboard

| KPI | Target | Source |
|---|---|---|
| Fleet availability (operating hours) | ≥92% overall, ≥85% per class | `fleet_inventory` status history |
| Class-B SLA hit rate | ≥95% ≤24 h | ticket timestamps |
| Repeat-failure rate (same subsystem, 10 cycles) | ≤5% | `maintenance_logs` join |
| PM compliance (flags cleared before hard-block) | ≥98% | PM engine |
| QC first-pass yield | ≥90% | QC module |
| Cost of parts per 100 Shifts | trend ↓, budget $85/100 Shifts Year 1 | parts_used × price |

---

## 8. Inventory & Parts Management

### 8.1 The canonical high-turnover spares — min/max register

Source doctrine: the high-turnover spares list from the original blueprint, extended by platform. Min = reorder trigger; Max = shelf cap. Quantities set for the Phase 1 fleet mix and ~2-week supplier lead time (fast lanes via Volume 8's distributor tier; slow boat for bulk).

| SKU class | Turnover | Min / Max | Note |
|---|---|---|---|
| Pinions (brass, per fleet pitch/counts) | HIGH | 10 / 30 per count | 48P (1/10), Mod 0.6/0.7 (1/14) |
| Spur gears (nylon + metal) | HIGH | 8 / 24 per platform | Impacts kill spurs; nylon is the fuse — that's intentional |
| CVD/dogbone driveshafts | HIGH | 8 / 20 per platform | Buggy fronts deplete 3× rears |
| Suspension A-arms | HIGH | 12 / 36 per platform-corner | Front-left ≠ front-right consumption; track direction bias is real — let the data set the split |
| Steering knuckles & hubs | HIGH | 8 / 24 per platform | |
| Shock shafts + full seal kits | HIGH | 10 / 30 | Seals: 20 / 60 kits |
| Servos 15 kg & 25 kg digital (metal gear) | HIGH | 6 / 15 each rating | Waterproof-rated for wet fleets |
| Wheel bearings (per size: 5×11, 10×15, 8×16 etc.) | HIGH | 40 / 120 per size | Rubber-sealed only |
| Wheel hexes + pins, wheel nuts | HIGH | 30 / 100 | Nylocks are one-way parts: 3 uses max |
| Tires: knobby (Track B), drift (A), slick/touring (A), crawler | CONTINUOUS | 24 / 80 sets per class | Pre-glued spare wheelsets: 8 per class minimum |
| Excavator track pins & links | CONTINUOUS | 100 / 400 pins; 30 / 100 links | Bag-of-pins economics; never stock out |
| Brushed motors 540/550 | MEDIUM | 6 / 15 | Plus refurbished pool from comm lathe |
| Brushless motors (fleet KV per class) | MEDIUM | 3 / 8 per class | |
| ESCs (fleet standard per class) | MEDIUM | 3 / 8 per class | Pre-programmed to profile before shelving |
| Receivers (fleet protocol) | MEDIUM | 6 / 15 | |
| Boom-limit micro-switches | MEDIUM | 10 / 30 | Known weak point |
| RCW Nodes (assembled, coated, flashed) | MEDIUM | 10 / 25 | Chapter 14 bench keeps the pool topped |
| Body posts, clips, shells | MEDIUM | posts 20/60; clips 200/600; shells 2/6 per class | Clips are the park's confetti |
| XT60 pairs, 12–16 AWG silicone wire, heat-shrink | CONTINUOUS | 40 / 120 pairs; 10 m / 30 m per gauge | |
| Loctite 243, CA (thin/med), activator, Shoe Goo | CONTINUOUS | 4 / 10 units each | |
| Silicone fluids (diff + shock, per weight) | CONTINUOUS | 2 / 6 bottles per weight | One brand family (§6.5) |
| Lithium & CV greases, bearing oil | CONTINUOUS | 2 / 6 each | |
| Fasteners: M2/M2.5/M3/M4 assortments, e-clips, nylocks | CONTINUOUS | 1 / 3 refill boxes per size | Sorted cabinet, never loose bags |

### 8.2 Bin system and labeling

- **Location code:** `RACK-SHELF-BIN` (e.g. `B2-3-07`), printed with the P-touch on both bin faces plus a QR that opens the SKU in RC WORLD OS.
- Two-bin kanban for HIGH/CONTINUOUS SKUs (§7.4); single bin + monthly count for MEDIUM.
- **Donor shelf:** retired vehicles are stripped to a labelled donor tote per platform; the donor shelf is checked *before* the new-parts bin for class-C repairs. Harvested parts log at zero cost, which keeps the parts-per-100-Shifts KPI honest about scavenging.
- Electronics SKUs live in shielding bags inside the bins; batteries never live in the parts store (Battery Room only).
- Quarterly full count; HIGH SKUs cycle-counted weekly (10 SKUs per day rotation — 5 minutes).

### 8.3 Consumables burn-rate table (Year 1 planning)

| Consumable | Burn rate @230 Shifts/day | Annual cost est. |
|---|---|---|
| Tires (all classes, incl. pre-glued sets) | ~1 set / 60 Shifts | $8,000–11,000 |
| CA glue + activator | 1 bottle / 4 days | $700–900 |
| Fasteners & clips | steady trickle | $600–900 |
| Silicone fluids & greases | monthly bottles | $500–700 |
| Threadlock | 1 × 10 ml / 3 weeks | $250–350 |
| Solder, flux, shrink, wire | Node bench dominates | $600–900 |
| Track pins/links | continuous | $400–600 |
| Shop consumables (IPA, gloves, towels, blades, silica) | — | $900–1,200 |
| **Total consumables** | | **$12,000–16,500** |

### 8.4 Reorder triggers and Volume 8 linkage

Kanban card scans raise requisitions automatically; the procurement rules — supplier register, wholesale-vs-distributor split, landed-cost math, order batching to hit freight breaks, and the strategic reserve of one-model-year buyouts when a fleet platform faces discontinuation — are Volume 8's territory. The workshop's obligations to that system are exactly three: scan cards same-day, log `parts_used` on every ticket, and flag rising-consumption anomalies (a SKU whose burn doubles is a fleet defect signal for Chapter 9, not just a bigger order).

---

## 9. Failure Analysis & FMEA

### 9.1 Structured failure reporting

Every class-B/C ticket closes with a structured failure record: **subsystem → component → failure mode → suspected cause → cycles-at-failure**, picked from controlled vocabularies (free text allowed only in the notes field — you cannot Pareto free text). The monthly failure review (Workshop Lead + division leads, 45 min) reads three standard cuts from RC WORLD OS: top 10 components by ticket count, by bench-hours, and by parts cost; repeat-failure assets (3+ tickets/30 days — candidates for teardown or retirement); and cycles-at-failure distributions vs the PM thresholds (if diffs fail at 80 cycles, the 100-cycle PM is mis-set — move it).

### 9.2 Root-cause discipline

The workshop standard is **5-Why with physical evidence** — a claimed root cause must point at an artifact (the part, a photo, a telemetry trace). Two worked examples from commissioning-period expectations:

- *Symptom:* buggy spur gears stripping at 3× fleet rate on Track B. Why? Mesh too tight on inspection → Why? Motor mounts shifting → Why? Mount screws loosening → Why? No threadlock found on sampled screws → Why? Batch of vehicles hardened before the threadlock step was added to the induction checklist. **Action:** recall pass on the batch; checklist gate added; spur burn returns to baseline in 3 weeks — verified in the KPI cut.
- *Symptom:* excavator boom stalls, cluster of tickets. Trace: running-current logs (SOP-WS-011) show 40% rise over 20 cycles before each stall. Root cause: pit sand ingress at a cover seam on one hull revision. **Action:** foam seal added at hardening; current-trend alert added to the Node telemetry rules so RC WORLD OS flags the *next* one at +20%, before the customer feels it.

### 9.3 FMEA method

Scoring 1–10 per standard practice: **Severity** (1 = cosmetic … 10 = safety/fire), **Occurrence** (1 = rare … 10 = near-certain per 100 cycles), **Detection** (1 = caught by existing checks … 10 = undetectable before failure). **RPN = S × O × D**; anything ≥100 requires a documented action; anything with S ≥ 8 requires action regardless of RPN. Reviewed quarterly; scores re-baselined against real ticket data.

### 9.4 FMEA — 1/10 touring car (rental-hardened)

| Item / function | Failure mode | Effect | S | Cause | O | Current controls | D | RPN | Action |
|---|---|---|---|---|---|---|---|---|---|
| Front A-arm | Crack/snap at hinge boss | Vehicle down mid-Shift | 4 | Wall impact | 7 | Daily flex check; spares depth | 3 | 84 | Accept; monitor per-corner consumption |
| Steering servo | Gear strip | No steering — runaway risk until kill | 7 | Impact through servo-saver, stall at EPA | 4 | Servo-saver verify at PM; EPA rule §3.6; Node kill | 3 | 84 | Keep; audit saver spring quarterly |
| Spur gear | Stripped teeth | No drive | 3 | Tight mesh / debris | 5 | Paper-strip method; mesh at PM | 3 | 45 | Accept — spur is the designed fuse |
| ESC | Thermal shutdown mid-Shift | Customer stops; refund risk | 4 | Overgearing, blocked airflow, hot day | 4 | Rollout register; thermal cutoff ON; IR gun at QC | 4 | 64 | Summer gearing table; log shutdowns via Node |
| Battery connector (XT60) | Browned/loose pins → resistance heating | Power loss; melt hazard | 7 | Cycle wear, poor solder | 3 | Daily connector check; §3.8 solder criteria | 4 | 84 | Connector replaced at 300 cycles preventively |
| Wheel bearing | Seizure | Drag, pull, DNF | 3 | Grit + water | 6 | 25-cycle spin-feel; sealed 2RS | 4 | 72 | Accept; ultrasonic clean batches |
| Chassis tub | Crack at bulkhead | Class-C repair | 5 | Repeated big hits | 3 | Post-crash SOP-WS-003 | 5 | 75 | Skid/brace kit on high-hit cars |
| RCW Node solder pads | Fatigue fracture | Telemetry loss → no kill authority | 8 | Vibration, missing strain relief | 3 | §3.8 + silicone blob QC at install; heartbeat watch | 2 | 48 | Heartbeat-loss auto-flags vehicle to intake |

### 9.5 FMEA — Huina 1580-class excavator (lead-screw)

| Item / function | Failure mode | Effect | S | Cause | O | Current controls | D | RPN | Action |
|---|---|---|---|---|---|---|---|---|---|
| Boom lead-screw | Stall / chatter | Function loss; motor overheat | 5 | Grit in nut, dry screw | 6 | SOP-WS-011 current logging; 100-cycle grease | 3 | 90 | Current-trend alert at +20% (done, §9.2) |
| Boom-limit micro-switch | Fails to open at limit | Motor stalls at end-stop → burnout | 7 | Switch wear, misadjustment | 5 | PM switch test; spares MEDIUM | 4 | 140 | **Action open:** add software current-limit kill in Node firmware as redundant stop (Volume 13 backlog) |
| Track master pin | Walks out | Thrown track, field recovery | 4 | Side-load vibration | 6 | Safety-wire keeper (hack 26); daily tension check | 3 | 72 | Keeper made standard at hardening |
| Slew gear | Tooth wear → slop | Sloppy rotation, play in digging | 3 | Sand ingress | 5 | Season teardown | 6 | 90 | Felt seal retrofit trial on 2 units |
| Bucket pivot pins | Ovalized bores | Slop, inaccurate digging | 2 | Wear | 7 | Season inspection | 5 | 70 | Accept; bushing upsize at rebuild |
| Drive motor (brushed 550) | Brush wear-out | Track dead | 4 | Runtime | 5 | 100-cycle brush check; comm lathe refurb pool | 3 | 60 | Accept |
| Cab glazing/body | Cracking | Cosmetic → brand damage | 2 | UV + impacts | 6 | Monthly fleet audit | 2 | 24 | Accept; repaint rotation |

### 9.6 FMEA — 2S/3S LiPo pack (fleet battery)

| Item / function | Failure mode | Effect | S | Cause | O | Current controls | D | RPN | Action |
|---|---|---|---|---|---|---|---|---|---|
| Cell | Over-discharge <3.4 V/cell | Capacity loss; internal damage; later swelling | 6 | ESC LVC mis-set; Node bypass; storage drain | 3 | Dual cutoff (Node soft 3.4 V + ESC hard); intake voltage check; no-pack-sleeps-in-vehicle rule | 2 | 36 | Keep dual-control doctrine |
| Cell | Internal short → thermal runaway | **Fire** | 10 | Puncture/crush in crash; charge after damage | 2 | Post-crash pack quarantine; charge only in bunker, in bags, attended; thermal watch | 3 | 60 | S=10 → action regardless: bunker doctrine (Ch. 11), quarterly fire drill |
| Pack | Swelling ("puffing") | Retirement; jammed battery bays | 4 | Age, heat, abuse cycles | 6 | IR tracking + physical inspection at every charge (Ch. 10) | 2 | 48 | Retirement thresholds §10.3 |
| Balance lead | Wire pull-out at housing | Charger error; miswired-charge risk | 6 | Yank removal | 4 | Grease hack 19; handling training; keyed JST-XH | 3 | 72 | Balance-lead repair is Artisan II bench job only |
| Main lead / XT60 | Solder-joint failure, wick-line fracture | Power loss; short risk during handling | 7 | Amateur repair, vibration | 3 | §3.8 criteria; one-lead-at-a-time rule | 3 | 63 | All battery-lead work at electronics bench only |
| Wrong charge profile | LiPo charged as NiMH / wrong cell count | Overcharge → **fire** | 10 | Operator error | 2 | Smart chargers with auto cell-count sanity + operator double-confirm; settings table posted (Ch. 11) | 3 | 60 | S=10: two-person rule for any non-standard charge |

### 9.7 Feeding fleet purchasing

FMEA outputs and ticket Paretos flow into Volume 8's purchasing decisions in two ways: **spares mix** (min/max levels re-set quarterly from real burn) and **platform selection** (a candidate fleet model inherits the FMEA of its class; if a new buggy platform can't beat the incumbent's top-3 RPNs on paper — metal drive cups, serviceable diffs, available A-arms — it doesn't get bought, whatever the unit price). This is the loop that makes the fleet cheaper to run every year it operates.

---

## 10. The Battery Room

### 10.1 Role and stock

The Battery Room — **24 m², geometry per Volume 11 Chapter 6** — is the *storekeeping* half of the LiPo estate: storage racks, logging bench, quarantine shelf. Charging happens next door in the bunker (Chapter 11); the two rooms share a pass-through hatch and nothing else. Stock under the 3:1 doctrine: ~150 vehicles × 3 = **≈450 packs** (2S and 3S, XT60), each with a laser-etched or heat-stamped pack ID linked to a battery record in RC WORLD OS (chemistry, capacity, C-rating, purchase date, cycle count, IR history).

### 10.2 State-of-charge storekeeping

The park's LiPo doctrine sets the operating window at 3.4–4.2 V/cell; the *storage* discipline sits inside it:

- **Storage state of charge: 3.80–3.85 V/cell** (≈50–60% SoC). Every pack not scheduled to run within ~24 h is brought to storage voltage — up via storage-charge, down via storage-discharge on the chargers' storage mode. Full packs held full for days lose capacity fast and swell early; empty packs risk drifting under 3.4 V.
- **Rack layout mirrors state:** READY racks (charged, 4.15–4.20 V/cell, ordered by class, oldest-charge-first issue), STORAGE racks (3.80–3.85), DISCHARGE-QUEUE shelf (came back high, waiting storage-discharge), QUARANTINE (locked metal cabinet, Chapter 10.4). Sacrificial red XT60 flags mark storage state (hack 27).
- READY packs not consumed within 48 h go back through storage mode. The overnight sort is SOP-WS-015's battery checklist.

### 10.3 Cycle logging, internal resistance, and retirement

Every charge event logs pack ID, cycles, per-cell voltages, and **internal resistance (IR)** as reported by the smart chargers (SkyRC/ISDT class report per-cell IR). IR is the pack's honest odometer:

| Metric (per cell, 25 °C reference) | Healthy 2S/3S 5,000 mAh class | Watch | Retire |
|---|---|---|---|
| IR per cell | 3–8 mΩ | 12–15 mΩ or +50% vs new-baseline | >20 mΩ or any cell 2× its siblings |
| Cell divergence at full charge | <0.02 V | 0.03–0.05 V | >0.05 V persistent after balance |
| Capacity vs label (annual discharge test) | >85% | 75–85% | <75% |
| Cycle count | — | 150 | 200–250 typical economic life |

Retirement is triggered by **any** retire condition, not consensus. Retired packs are logged, physically marked (corner cut off the shrink label), storage-discharged, then routed to disposal (§10.5). Replacement tempo follows Volume 10's throughput-derived model, which is canonical: **57,720 pack-cycles/year** across the ~450-pack pool ≈ **128 cycles per pack per year (~0.35 cycles/day)** — not every Shift consumes a full charge cycle (~30% buffer returned; multi-block Operator Shifts). Against the conservative 200-cycle retire trigger (economic band 200–250 cycles, or earlier on the IR thresholds above), a pack reaches retirement in roughly 19 months of cycling, bounded by a **~2-year calendar horizon**; plan **≈40–50% pool replacement per year** in the Volume 10 opex line.

### 10.4 Physical inspection and quarantine

At every charge hookup, a 5-second look and squeeze:

- [ ] No puffing — pack flat, shrink not drum-tight (light squeeze: a healthy pack has no "give-then-firm" balloon feel)
- [ ] No dents, punctures, split shrink, exposed foil
- [ ] Leads: insulation intact, no wick-stiffened zones, XT60 pins bright
- [ ] Balance lead: all wires seated in housing
- [ ] No sweet/solvent smell (electrolyte)

Any failure → **QUARANTINE**: the locked steel cabinet (or LiPo bunker box) *outdoors-vented*, logged, assessed by an Artisan II+ within 24 h. Post-crash packs from vehicles with battery-bay deformation are quarantined automatically for 24 h observation before any recharge — crush damage can take hours to become a short. Over-discharged packs (<3.0 V/cell) are quarantined and only recovered by the Workshop Lead at 0.5 C-limited low-current charge with continuous observation, once, then IR-tested; below 2.5 V/cell they are not recovered, they are retired.

> **Safety Warning.** A puffed pack is not "still fine because it works". Puffing is electrolyte decomposition gas — the cell chemistry is already failing and its abuse tolerance is gone. Puffed packs never return to the fleet and never get charged again except a supervised storage-discharge for disposal.

### 10.5 Disposal: the salt-water myth vs correct practice

The classic hobbyist advice — "soak the pack in salt water for a few days, then bin it" — is **obsolete and wrong**: salt water corrodes the terminals long before it discharges the cells, the current path stops, and you're left with a corroded pack that still holds charge, plus a bucket of contaminated electrolyte-tainted brine. RC WORLD's protocol:

1. Storage-discharge, then full discharge to ~3.0 V/cell on the charger; finish to near-0 V with a resistive discharger or 12 V bulb rig at the bench (attended), over hours.
2. Tape the connector (XT60 capped, balance lead taped), corner-cut label, log disposal in the battery record.
3. Deliver to a **certified battery recycler / municipal battery collection point** (Li-ion stream). Never general waste, never landfill skips.
4. Damaged packs that cannot be safely discharged go to the recycler in a sand-filled metal container, declared.

### 10.6 Fireproof storage

- Storage racks are open steel shelving (heat cannot build unnoticed) with packs in **LiPo-safe bags** or **steel ammunition boxes with the rubber door-seal removed** (pressure must vent, not build) — bags for singles, ammo boxes for class-batches of 4–6.
- No pack stored within 1 m of the door or blocking egress; no flammables (CA, IPA, paint) in the room — those live in the flammables cabinet in the main shop.
- Room fit-out: masonry walls, self-closing fire-rated door, smoke + heat detection wired to the park alarm, thermal camera or spot IR sensor watching the racks after hours (feed into RC WORLD OS alerting), dry-sand buckets and a Class ABC extinguisher *outside* the door (for surrounding materials — see §11.6 for the fire doctrine itself).

---

## 11. The Charging Room

### 11.1 Bunker design per doctrine

The charging room is the park's engineered fire cell, built per the original blueprint's doctrine and dimensioned by Volume 11, Chapter 6: **30 m² internal (6.0 × 5.0 m), inside the building**, in **filled-cell CMU (cinderblock) construction, sandbag-supplemented**, with blast venting to the exterior wall, an **FD90 fire-rated self-closing door**, and the pass-through hatch to the Battery Room:

- Filled-cell CMU walls on all sides, blockwork to ceiling; sandbags stacked to 1.2 m against the interior face of the working wall as spall/heat mass behind the charge racks.
- Ventilation: engineered blast/pressure vents through the exterior wall, high-level relief + low-level intake (thermal-runaway gas is hot and voluminous; the room must vent *outwards*), no recirculation into the workshop HVAC.
- Charge racks: steel shelving; every charging pack sits **inside a LiPo-safe bag or open sand tray / ammo box**; 100 mm sand-filled steel trays under each shelf level catch and smother a dropping burning pack.
- Floor: bare concrete; a 20 L dry-sand bucket per rack bay plus a long-handled scoop; nothing combustible in the room — no cardboard, no spare shrink, no curtains on the hatch.
- Electrical: dedicated circuits (below), emergency power-off (EPO) mushroom button at the door cutting all charger outlets, smoke/heat detection + thermal camera on the racks with RC WORLD OS alerting, door signage: occupancy rules and the fire card (§11.6).

### 11.2 Charger bank and electrical load

Daily demand at 230 Shifts/day: ≈230 pack-charges. Fleet packs are 2S–3S, 1,500–5,000 mAh; average ≈35 Wh per charge including losses. Bank specification:

| Position | Unit | Channels × power | Qty | Street price |
|---|---|---|---|---|
| Main bank | **ISDT K4** (dual, AC 400 W / DC 600 W×2, 1–8S) | 2 × 200 W (AC) | 6 | $220–295 ea |
| High-throughput | **SkyRC T1000** (dual, AC 450 W, 1–6S) | 2 × 225 W | 2 | $200–300 ea |
| Storage/utility | SkyRC or ToolkitRC compact duals (e.g. ToolkitRC M6D class) | 2 × 200–350 W (DC via PSU) | 4 | $70–120 ea |
| Bench/field spares | SkyRC iMAX B6 Evo class | 1 × 60 W | 2 | $40–55 ea |

= **24 charge channels**. At a fleet-average ~45 min per 1 C-class balance charge, the bank turns ~30 packs/hour flat out; the realistic duty pattern (morning top-up wave, midday rolling, evening storage wave) clears 230 charges in ~8 attended hours with ~60% channel occupancy — the correct margin for peak days. Electrical: worst-case simultaneous AC draw ≈ 6×400 + 2×450 + 4×250 + 2×60 ≈ **4.4 kW** plus ventilation; specify two dedicated 16 A circuits (or local equivalent) with the EPO upstream, and 30% spare breaker capacity for Phase 2 (Volume 11 electrical schedule).

### 11.3 Standard charger settings tables

Posted as laminates above each rack; operators select by pack label color:

| Pack class (label) | Chemistry/cells | Capacity | Charge mode | Current | Cutoff / balance | Storage mode |
|---|---|---|---|---|---|---|
| RED — 1/14 racing (144010-class, LDRC) | LiPo 2S | 1,500–2,200 mAh | Balance charge | 1.5–2.2 A (1 C) | 4.20 V/cell, balance to <0.01 V | 3.85 V/cell, ±1.0 A |
| BLUE — 1/10 touring/drift/buggy | LiPo 2S | 4,000–5,200 mAh | Balance | 4.0–5.0 A (1 C) | 4.20 V/cell | 3.85 V/cell |
| ORANGE — short-course / premium crawler | LiPo 3S | 5,000 mAh | Balance | 5.0 A (1 C) | 4.20 V/cell | 3.85 V/cell |
| GREEN — construction/agriculture | LiPo 2S–3S | 2,200–5,000 mAh | Balance | 1 C by label | 4.20 V/cell | 3.85 V/cell |
| GREY — small crawler (MN99S/C24 class) | LiPo/Li-ion per pack label | 350–1,500 mAh | Balance / Li-ion per label | 1 C (≤1.0 A small packs) | LiPo 4.20 / Li-ion 4.10 V/cell | 3.85 / 3.70 |

Rules: **1 C is the fleet ceiling** — faster charge rates are available on modern packs but trade cycle life we're not willing to sell; balance charge is the default mode (plain "fast charge" without balance ports connected is banned); cell-count on the charger display is read aloud and matched to the pack label before start (two-point check; the FMEA S=10 line).

### 11.4 Parallel charging: restricted practice

Parallel boards multiply throughput and multiply consequences. Permitted only for the RED 1/14 class on the T1000 positions, by Artisan II+, under these rules:

1. **Same chemistry, same cell count, same capacity class** on one board — no mixing.
2. **Voltage matching before connection: all packs within 0.05 V/cell** (checked with the cell meter; packs further apart equalize through the board at uncontrolled current).
3. Connect main leads first pack to last, then balance leads; charger current = 1 C × *sum* of capacities; per-pack share verified sane.
4. Maximum 4 packs per board; board fused per position (use fused parallel boards only, $25–45).
5. Attended for the full cycle — parallel charging is never "start and walk".

### 11.5 Charging SOP and occupancy rules

> **SOP-WS-016 — Charging Operations** · Rev 1.0 · Owner: Workshop Lead · PPE: baseline; no loose lanyards over racks · Tools: cell meter, IR thermometer · Frequency: continuous during operating hours

1. Inspect pack (§10.4 checklist) — failures to quarantine, not to charge.
2. Select settings from the laminate by label color; read cell count aloud against the label.
3. Pack into bag/tray on the rack; balance lead connected; start; verify first-minute current and detected cell count.
4. Log start in RC WORLD OS (scan pack QR; charger channel auto-associates where supported, else manual).
5. The room is **attended-adjacent**: a designated Artisan is within sight/alarm range whenever any channel runs; the thermal camera + smoke alarm cover gaps; overnight charging is prohibited except storage-mode cycles on the interlocked circuit, which self-terminates.
6. On completion: pack to READY rack (oldest-first issue), cycle + IR auto-logged.
7. Spot-check pack surface temperature by IR gun once per session: >45 °C at 1 C = stop, quarantine, investigate.

### 11.6 Fire response doctrine

Posted on the door as the **Fire Card**:

- **Never water on a burning LiPo pack.** Water conducts and spreads burning electrolyte; a lithium-*polymer* (Li-ion chemistry) fire is self-oxidizing during runaway — you cannot smother the reaction, only contain it and let it burn out.
- **Class D extinguishers are for lithium-*metal* fires** (machining swarf, primary lithium cells) — they are *not* the tool for LiPo packs and we do not stock one for the charging room; this is a common and expensive misunderstanding.
- **The correct response to a pack in runaway:** hit the EPO; if safely reachable with the scoop, lower the tray/bag to the concrete floor clear of the racks (never bare hands); **bury in dry sand** from the rack buckets; close the FD90 door behind you; let it complete; ventilate via the blast vents. The bunker's whole design assumes the pack finishes burning where it sits.
- The Class ABC extinguisher outside the door exists for **secondary fires** (packaging, wiring, adjacent materials) — never as the primary response to the pack itself.
- Any thermal event, including a pack that merely vented, triggers the incident report, quarantine of every pack that shared the rack shelf, and a review of the charge log within 24 h.
- Quarterly drill: full walkthrough with a dummy pack, timed; the marshal team's park-wide emergency procedures are in Volume 1's safety annex.

---

## 12. Quality Control

### 12.1 Pre-rental QC lane (fleet staging gate)

Every vehicle passes the QC lane between `maintenance` and `available` — after any repair, PM, or overnight if flagged. The lane checklist (2–4 min, printed + kiosk):

- [ ] Visual: shell, mounts, tires, no missing fasteners on the visible plane
- [ ] Rollers: throttle response clean at 25/50/100%, no drivetrain noise signature, brake/reverse per class profile
- [ ] Steering sweep at speed on rollers: full lock both ways, returns true, no chatter
- [ ] Failsafe: TX off under power → neutral <1 s
- [ ] Node: heartbeat, voltage agreement ±0.05 V/cell, kill command drop <1 s
- [ ] Current draw at free-run vs platform table (±20% band) — the cheapest hidden-fault detector in the building
- [ ] Construction: full function sweep, limit stops, current trace within band
- [ ] Battery bay: retention, connector condition
- [ ] Sign-off scan → state `available`, vehicle to staging shelf

### 12.2 Post-repair road test protocol

Class-B/C repairs additionally get the **strip test** on the 25 m fenced strip: two full-throttle passes, two figure-8s each direction, one panic stop; construction machines get the yard test (SOP-WS-010/011 patterns). The tester is *not* the repairing Artisan for QC-flagged steps — fresh eyes are the point. Failures bounce the ticket to the head of its class queue with the QC note attached; **QC first-pass yield ≥90%** is a bench-quality KPI, and repeat bounces route to the Workshop Lead as a coaching signal, not a blame signal.

### 12.3 Reference tables and instrument calibration

QC depends on reference numbers (free-run current per platform, temperature-rise bands, rollout per class) held in the **platform register** in RC WORLD OS and reviewed at season service. The instruments that generate them are calibrated on a schedule:

| Instrument | Check | Frequency | Method |
|---|---|---|---|
| Multimeters (Fluke 117 = shop reference) | vs reference | Spares monthly vs the 117; 117 externally every 2 yrs | 3-point V/I check |
| Cell checkers | vs Fluke 117 | Monthly | Known-pack ladder |
| Charger IR/voltage reporting | vs Fluke + reference pack | Quarterly | Same reference pack, logged drift |
| Torque screwdriver | vs test values | Quarterly | Calibration fixture or external cert annually |
| Scales (0.1 g, corner scales) | Check weights | Monthly | 3-point |
| Calipers | Gauge block / known pin | Quarterly | Zero + 25 mm point |
| IR thermometer | Ice bath / boiling ref | Quarterly | 2-point |
| Rollers/dyno | Reference vehicle | Monthly | Golden-car run, logged |

### 12.4 Monthly fleet audit

One half-day per month, the Workshop Lead + one Artisan audit a **20% rotating sample of the fleet** (whole fleet covered every 5 months) against: PM currency, setup-sheet conformity, hardening-spec conformity (threadlock witness marks, Node strain relief, connector condition), cosmetic grade (customer-facing paint/shell standard — brand matters), and telemetry-data sanity (odometer vs logs). Output: audit score per division on the KPI dashboard, a punch list of tickets, and — quarterly — the FMEA re-baselining data for Chapter 9. The audit is also the bench-quality audit: sampled vehicles' most recent repairs are inspected against Chapter 3's craft standards.

---

## 13. Building Custom RC Cars

This chapter is required by the founder's brief: a complete tutorial on building custom RC vehicles, from kit assembly through scratch design, closing with two worked park builds. It serves three business purposes: it is the Artisan III training text; it is the engineering basis for the park's own special vehicles (recovery crawlers, marshal utilities, showcase builds); and it seeds the future RC Academy curriculum (Phase 3, Volume 1).

### 13.1 Three routes to a custom car

1. **Kit build** — a hobby-grade kit (bag-by-bag assembly, ~6–12 bench hours) with your choice of electronics. Best learning-to-effort ratio; every Artisan III must have completed one.
2. **Platform conversion** — start from a cheap RTR (ready-to-run) and re-engineer it to a specification. This is the park's bread and butter (worked example §13.9).
3. **Scratch build** — design the chassis yourself around purchased drivetrain modules (axles, transmissions, motors). Reserved for vehicles no market product serves (worked example §13.10).

### 13.2 Chassis selection and design

The chassis answers four questions before any parts are chosen:

- **Mission:** speed surface, jump loads, crawl articulation, payload? Everything trades against everything: a stiff low tub that corners flat will drag its belly on Track C; a flexy crawler frame wanders at speed.
- **Layout:** where do the heavy masses (battery, motor) sit? Aim for the mission's weight split — touring ≈ 50/50 F/R with mass low and central; crawler ≈ 55–60% front (weight over the steering axle climbs); buggy slightly rear (traction on loose surfaces, jump attitude).
- **Structure:** tub (bathtub molded plastic — impact-tough, dirt-shedding, rental-friendly), plate (flat FRP/carbon deck — tunable flex, racing), or ladder frame (steel/aluminum rails + cross-members — crawlers, trucks, easiest to scratch-build and to 3D-print brackets for).
- **Serviceability:** the park test — can the diff come out without removing the shock tower? A custom build that fails the 15-minute-diff test fails the design review, whatever else it does well.

Scratch-design rules of thumb: wheelbase/track ratio ≈ 1.5–1.7 for stable trucks (shorter = agile, tippy); keep battery mass inside the wheelbase midpoint; design in mm around purchased hard points (bearing ODs, servo case standard sizes, 12 mm hex hubs) so failures are replaceable from the fleet bins.

### 13.3 Drivetrain layout: FWD / RWD / 4WD

| Layout | Behaviour | Park use |
|---|---|---|
| **RWD** | Throttle steers the rear; simplest, cheapest; demands throttle finesse | Drift fleet (deliberately loose), formula class, learning tool at the Academy |
| **FWD** | Pulls itself straight; understeers at the limit; forgiving under panic-lift | Rare in RC (some touring classes); good teaching contrast; not fleet-relevant |
| **4WD shaft** | Neutral, fast, launches hard; one propshaft ties both diffs; more parts to service | Standard for touring, buggy, crawler fleets |
| **4WD belt** | Smooth, quiet, tunable slip; belts hate grit | Indoor/asphalt only; avoid for dirt fleets |

Within 4WD, the differential stack sets character: open diffs (fluid-filled gear diffs, tune by cSt) for racing; **locked axles or one-way spools have no place in rental racing** (they punish smooth driving) but **lockers are mandatory in crawlers** (both axles turn everything, always). Ball diffs are banned fleet-wide as maintenance-intensive.

### 13.4 Motor and ESC matching: the mathematics

The chain: **motor KV × pack voltage → RPM; gearing → wheel RPM; wheel diameter → speed**. Define **rollout** = distance travelled per motor revolution = wheel circumference ÷ total drive ratio.

Worked example (1/10 touring, park spec):

- Motor: 13.5T sensored brushless ≈ **2,850 KV**. Pack: 2S LiPo, nominal 7.4 V.
- Free RPM = 2,850 × 7.4 ≈ **21,090 RPM**; under load assume ~85% ≈ 17,900 RPM.
- Gearing: pinion 27T, spur 78T, internal ratio 2.0 → total ratio = (78/27) × 2.0 = **5.78**.
- Wheel Ø 64 mm → circumference 0.201 m. Rollout = 201 ÷ 5.78 = **34.8 mm/rev**.
- Speed = 17,900 ÷ 5.78 × 0.201 ÷ 60 = **10.4 m/s ≈ 37 km/h** — right for Track A's 180 m line.

Matching rules: hotter motor (higher KV / lower turns) demands *shorter* gearing (smaller rollout) or it cooks — the thermal check is the IR gun after 5 minutes' running: **motor ≤ 75 °C, ESC ≤ 70 °C**, above that drop 2 pinion teeth and re-test. ESC current rating ≥ 1.5× the motor's expected burst draw; sensored systems for anything a customer throttles from zero (smooth low-speed control); the fleet's detune levers live in the ESC (punch, throttle cap, drag brake), not in motor swaps — one motor SKU per class, always.

### 13.5 Servo torque calculation

Steering torque scales with vehicle weight, tire grip and scrub geometry. Bench approximation: required stall torque (kg·cm) ≈ vehicle mass (kg) × grip factor (asphalt 2.5, dirt 2.0, crawl 4.0) × scrub radius factor (≈1.0 for typical 1/10 geometry). Examples:

- 1.7 kg touring car on asphalt: 1.7 × 2.5 ≈ **4.3 kg·cm minimum** → fit 9–12 kg·cm for margin and crash loads.
- 2.9 kg crawler, high-grip rock, big scrub: 2.9 × 4.0 ≈ **11.6 kg·cm** → fit 20–25 kg·cm waterproof (this is why the spares register standardizes 15 and 25 kg servos).

Speed matters too: racing wants ≤0.10 s/60°; crawlers tolerate 0.15+. Always feed high-torque servos from an adequate BEC — a 25 kg servo can pull 3–4 A stalled, above many built-in ESC BECs; the scratch-build spec (§13.10) uses an external 5 A switching BEC.

### 13.6 Battery selection: capacity and C-rating math

A pack's deliverable current = capacity (Ah) × C-rating. Work the requirement backwards from the powertrain:

- Touring example: 13.5T system bursts ~55 A, sustains ~25 A. A 5.0 Ah pack needs 55 ÷ 5.0 = **11 C minimum burst**. Any honest 30 C pack covers it 3×; buy 30–50 C from reputable lines (Gens Ace / CNHL per Volume 8) and ignore three-figure marketing C-ratings.
- Runtime sanity: 25 A sustained from 5.0 Ah ≈ 12 min flat-out; a rental Shift's real duty cycle (~40% throttle time-average) → 25–30 min — matching the 20-minute Shift with the doctrinal ~30% buffer returned.
- Weight is a design input: a 2S 5,000 mAh hard case ≈ 265 g — about 15% of a touring car's total mass; capacity beyond the Shift + buffer is dead ballast that slows the car and lengthens charge cycles. Fit the *smallest* pack that funds the Shift plus 30%.

### 13.7 Body prep and painting polycarbonate

RC bodies are clear polycarbonate (Lexan) painted **inside-out** — the paint lives protected behind the plastic and the outside stays glossy:

1. Trim the shell on the molded lines (curved lexan scissors), ream body-post holes 1 mm oversize (paint later takes the slack), drill the roof vent holes.
2. Wash the *inside* with warm water + dish soap — mold-release residue is the #1 cause of paint peel. Dry lint-free; from now on touch the inside with gloves only.
3. Mask the windows (window masks or masking film) and the outside overspray zones; leave the protective outer film ON until the build is done.
4. Paint **polycarbonate-specific paints only** (Tamiya PS line, Spaz Stix; airbrush or rattle-can) — normal enamels/acrylics crack off the flexing shell. Spray in the booth (§1.7).
5. Order: details and shadows first, then main color in 2–3 light coats, then **back the whole job with white or silver** — backing coat gives colors their depth and blocks light. Dark-to-light layering, always; each coat flash-dries 15–20 min.
6. Peel the window masks, apply decals to the *outside*, peel the outer film last, edge-seal decals with a heat gun waft. Fleet shells add a strip of lexan tape (drift/touring) or shoe-goo bead (off-road) inside the front lip — cheap crack insurance where every shell dies first.

### 13.8 Setup from first principles

A custom build is set up in this order, one variable at a time, on the platform setup sheet:

1. **Neutral mechanicals:** ride height per class (touring 5–6 mm, buggy 22–25 mm), droop symmetric, camber −1 to −2°, toe: front 0 to −1° (out), rear +2 to +3° (in) for stability.
2. **Diffs and shocks:** start at the class register's fluid weights; verify shock pairs matched (§5.9).
3. **Rollout:** gear to the track's longest straight (§13.4 math), thermal-check, lock the pinion count in the register.
4. **Drive:** three-lap feel test on the strip/track, changing exactly one thing per stop. Push (understeer) → softer front oil / more front droop / less front toe-out; loose (oversteer) → softer rear springs / more rear toe-in / smaller rear sway bar.
5. **Freeze and document.** The finished sheet enters the platform register; from here the parity program (Volume 3, Chapter 4) owns any racing-class deviations.

### 13.9 Worked build #1 — WLtoys 144010 → park-spec rental buggy

The 144010 is the canonical Phase 1 rally/buggy donor: ~$60–90 wholesale, metal-ish chassis, brushless power, absurd parts economy. Stock, it is a 60 km/h hand grenade in rental service. The conversion (target ≤2.5 bench-hours, parts ≈ $38–55):

**Teardown findings the conversion addresses:** plastic outdrive cups that split under abuse; self-tapping screws into soft bosses; marginal servo-saver; no telemetry; full-power ESC profile; body clips customers lose in minutes.

1. **Driveline hardening:** replace plastic drive cups and diff outdrives with the **metal drive cup/outdrive kit** (aftermarket steel, $12–18/set); metal center driveshaft if not already fitted; blue threadlock every grub screw; re-shim diffs and set mesh (§3.5).
2. **Fastener pass:** convert body-mount and gearbox self-tappers to M2.5 machine screws + nuts/inserts where bosses allow; nylock the wheel nuts (stock ones back out).
3. **Suspension:** stock shocks re-filled with 450 cSt (they arrive with inconsistent fluid), spring collars set; steering servo-saver spring shimmed one washer (stock is too soft to steer, too stiff to save).
4. **Electronics detune:** fleet ESC profile — **throttle cap 55%** (≈33 km/h from the §13.4 math run backwards on measured KV: bench KV on sampled units reads ≈3,900 with the SkyRC BMA-01; 3,900 × 7.4 × 0.55 duty ≈ 15,900 RPM loaded ≈ 9.2 m/s ≈ 33 km/h at the stock 5.7:1 and 62 mm wheels), punch level 3/9, drag brake 8%, reverse locked out on track classes, **LVC hard cutoff 3.4 V/cell**. Where the stock ESC lacks programmability, it is replaced by the fleet-standard programmable unit ($18–25) — the conversion budget assumes 50% need it.
5. **RCW Micro-Node install** per SOP-WS-013: PWM intercept, pads soldered, silicone strain relief, GPS clear of the metal top deck, bind to asset tag.
6. **Rental furniture:** tethered body clips (fuel-tubing lanyards — hack family), asset-tag decals, front-lip shoe-goo bead, velcro battery gate (hack 25), tires glued per SOP-WS-009 (factory glue is decorative).
7. **QC:** full lane + strip test; parity check against the class golden car (lap delta ≤3%); registration in `fleet_inventory`; setup sheet frozen.

> **Field Note.** The 144010 conversion is the best Artisan II training job in the building: it touches every craft standard in Chapter 3 in one afternoon, on a platform cheap enough that mistakes are tuition, not losses.

### 13.10 Worked build #2 — scratch-built heavy recovery crawler with winch

The Tow-Truck Retrieval Protocol (customers pilot a recovery vehicle to retrieve breakdowns) needs a machine no catalog sells: crawler-slow, stable under side-load from a winch line, near-indestructible, and telemetry-supervised. Phase 1 fields four; they are scratch-built on purchased modules. Specification and build:

- **Frame:** ladder frame from 3 mm aluminum flat bar rails + 3D-printed PETG cross-member/skid modules (printed at 60% gyroid infill, 4 walls; jig files in the library). Wheelbase 313 mm on 1.9" wheels — long for line-pull stability; track widened +10 mm per side with hex extensions.
- **Axles/transmission:** portal axles and a 2-speed transmission from the TRX-4-class aftermarket ecosystem (fleet commonality with the premium crawlers — same spares bins). Both diffs locked. Overall crawl ratio in low ≈ 100:1.
- **Power:** 540 brushed 20T motor (torque-dense, cheap, comm-lathe serviceable) on a crawler ESC with drag brake 100%; 3S 5,000 mAh pack low and central; external 5 A BEC feeding a 25 kg waterproof steering servo (§13.5 math: 2.9 kg × 4.0 ≈ 12 kg·cm minimum, doubled for winch-era side loads).
- **Winch:** hobby-class electric winch (Ø 1.5 mm synthetic line, ~4 kg pull — sized to drag any 1/10 fleet vehicle up a 15° haul-road grade: worst case 3.2 kg × (sin 15° + 0.35 rolling/drag) ≈ 1.9 kg line pull, 2× margin), driven through a servo-signal winch controller on channel 3, **line-out limit switch** and a printed fairlead. Free-spool clutch so marshals can pull line by hand.
- **Telemetry:** RCW **Heavy-Node** (JST-XH field connectors — this vehicle gets opened often), geofence set to the active recovery corridor only: the customer piloting it can physically drive only where the protocol allows; kill authority with the marshal.
- **Customer detune:** throttle cap 60% in high range, high range software-locked during retrievals, steering rate limited — piloting stays easy and theatrical, per the experience design in Volume 9.
- **Build sequence:** frame + axles dry-fit → drivetrain shakedown *before* electronics (roll it down the strip on a temp servo) → electronics + Node → winch + limit switch → waterproofing pass (SOP-WS-012) → ballast to 55/45 front bias at 4.1 kg all-up → QC yard test including a full retrieval rehearsal towing a dead 1580 excavator's dump-truck partner.

Documentation duty: both worked builds' full BOMs, print files and setup sheets live in the platform register; the recovery crawler's BOM is the template every future special build copies.

---

## 14. Telemetry Hardware Bench Work

The RCW Node's electrical design, firmware and cloud side belong to Volume 13; this chapter is the *workshop's* share: assembling, coating, testing, flashing and installing the boards. Canon recap: ESP32-C3-MINI-1 (or SuperMini module) + ATGM336H GPS, 10 kΩ/2.2 kΩ voltage-divider battery sense, TPS54202 (or LM2596-class) buck from 2S/3S to 3.3 V, PWM intercept between receiver and ESC; **Micro-Node** ~25×25 mm direct-solder for racing platforms, **Heavy-Node** ~40×30 mm JST-XH latching for the heavy fleet; unit cost target <$15; boards fabricated/assembled in JLCPCB-class batches per Volume 8.

### 14.1 Incoming PCBA QC (per batch)

- [ ] Visual at the magnifier lamp: solder bridges, tombstoned passives, module seating, cleanliness (no flux lakes)
- [ ] Sample 10% of batch: power-on current at 8.0 V bench supply — sleep and active currents within firmware datasheet band; buck output 3.30 ± 0.05 V
- [ ] Voltage-divider sanity: injected 8.40 V reads 8.40 ± 0.05 on the debug console (divider ratio 10 k/2.2 k → ADC ~1.52 V)
- [ ] GPS: cold-fix under open sky <60 s on sampled units
- [ ] Reject rate >3% → batch hold, supplier ticket via Volume 8

### 14.2 Conformal coating and verification

Boards are coated at the paint booth after flashing and *before* connectors/harness (mask connector pads, antenna areas, and the ATGM336H patch):

1. Acrylic conformal spray (MG Chemicals 419D/422B class), two light cross-coats, 30 min between; epoxy coating reserved for marine-fleet Nodes.
2. **Verification:** most acrylic coatings fluoresce — a $10 UV torch pass shows coverage as a uniform glow; voids re-coated. Cured coating passes a fingernail-drag without flaking. Coating date + operator initials on the Node label.
3. Coated spares stored in shielding bags in the parts store (10/25 min-max, Chapter 8).

### 14.3 PWM intercept wiring (textual diagram)

Described left-to-right along the signal path:

- **Receiver throttle channel (CH2 typical)** → 3-wire servo lead → **Node input header** (signal / +5 V / GND). The Node's MCU reads the incoming PWM (1,000–2,000 µs).
- **Node output header** → 3-wire lead → **ESC signal input**. In PASS mode the Node reproduces the input pulse; in LIMIT mode it clamps the pulse toward 1,500 µs (e.g. under-voltage soft limit = max 20% throttle authority); in KILL it holds neutral/brake.
- **Battery sense pair** (red/black, fused 100 mA inline) → main pack terminals **downstream of the vehicle master switch** — the doctrinal no-parasitic-drain point. Divider on-board.
- **Power:** Node logic feeds from its own buck off the battery sense pair, *not* from the receiver's BEC rail — a browning-out BEC must not take the telemetry down with it.
- Heavy-Node adds channel-3 intercept (boom/winch functions) and the JST-XH latching versions of all of the above; Micro-Node terminates all four looms on solder pads with the silicone strain-relief blob bridging loom to board edge.

Failsafe philosophy: the Node fails **transparent** — watchdog or brown-out puts the intercept into hardware PASS, so a dead Node never strands a customer; the RX failsafe (SOP-WS-014) still covers RF loss.

### 14.4 Bench-test jig

The flashing/test jig (3D-printed cradle + pogo pins onto the programming pads, USB-UART on the bench PC, PWM generator + oscilloscope-lite USB analyzer):

1. Node clicks into cradle; pogo pins land on TX/RX/EN/IO9/3V3/GND.
2. Jig PSU emulates a 2S pack (7.4–8.4 V sweep) on the sense pair; servo tester feeds a known PWM into the input header; the analyzer watches the output header.
3. Automated script (bench PC, part of the Volume 13 toolchain) walks: flash → boot → Wi-Fi join to the bench AP → heartbeat seen in RC WORLD OS test tenant → voltage read-back at 3 sweep points → PASS/LIMIT/KILL commands verified on the analyzer (KILL latency logged; must be <300 ms bench-side) → GPS fix (window bench antenna) → label print.
4. Jig throughput ~6 min/Node; the Chapter 8 spares pool (10–25 units) is topped up in monthly bench sessions.

### 14.5 Firmware flashing procedure

> **SOP-WS-017 — Node Firmware Flash** · Rev 1.0 · Owner: Artisan III / Node bench · PPE: ESD strap · Tools: test jig, bench PC · Frequency: at assembly; fleet-wide OTA campaigns are software-side (Volume 13); bench re-flash on OTA failure only

1. Pull the **released** firmware build from the RC WORLD OS artifact registry — never a developer's laptop build onto a fleet Node.
2. Jig-seat the Node; hold BOOT (IO9) via jig button; flash over UART at the toolchain's standard baud; verify checksum readback.
3. First-boot provisioning: Node generates/receives its identity, is bound to MAC in `fleet_inventory`, joins the bench AP.
4. Run the §14.4 automated test to PASS; label with firmware version + date.
5. Log flash event; a Node that fails flash twice is quarantined for the electronics bench, not retried indefinitely.

> **Safety Warning.** The kill-switch chain (park command → Supabase Realtime → Node → PWM clamp) is a safety function. Any firmware or wiring change that touches the intercept path requires the full §14.4 KILL/PASS verification *and* the SOP-WS-013 in-vehicle kill test before the vehicle re-enters service — no exceptions for "one-line changes".

---

## 15. Volume Summary & Cross-References

The Works is where RC WORLD's economics are physically defended. This volume specified the facility (450 m² GFA per Volume 11 Chapter 6, organized around a ~180 m² wrenching/electronics core with one-way flow, a 24 m² battery room and a 30 m² internal charging bunker, ESD-protected electronics benches, task-graded lighting, treated compressed air, extracted soldering and paint stations); the tooling in three tiers (~$420–600 per Artisan, $4.5–6.5 k shared bench, $6–9 k capital including lathe, comm lathe and two 3D printers — $28–38 k all-in with charging infrastructure); the craft standards every repair is audited against (screw mapping, torque tables, blue-not-red threadlock, paper-strip gear mesh, servo centering, strain-relieved wiring, solder-joint criteria); a 30-entry trade-hacks compendium; seventeen SOPs from intake to end-of-day shutdown; a cycle-based PM system driven by RC WORLD OS odometers with family matrices and a lubrication chart; repair workflow math showing ~11 bench-hours/day at 230 Shifts/day and a 4-Artisan + Lead roster; min/max inventory with two-bin kanban and a $12–16.5 k consumables budget; FMEA tables for the touring car, excavator and LiPo pack with one open action (redundant current-limit stop for boom lead-screws); battery storekeeping at 3.80–3.85 V/cell with IR-based retirement and correct (non-salt-water) disposal; the charging bunker with a 24-channel charger bank, settings tables, restricted parallel-charging rules and the dry-sand-never-water fire doctrine; the QC lane and calibration schedule; the full custom-build tutorial with the 144010 park-spec conversion and the scratch-built recovery crawler; and the RCW Node bench program from incoming QC to firmware flash.

**Cross-references.**

- **Volume 3** — racing platform specs, ESC parity profiles, setup sheets and the 2–3% parity audit this workshop executes.
- **Volume 4** — construction fleet duty cycles, lead-screw doctrine and the 1:3 excavator:dump-truck logistics the PM system protects.
- **Volumes 5 & 6** — aviation and marine PM annexes (flight-hours and flex-shaft regimes) that run on this volume's PM engine.
- **Volume 8** — supplier register, landed-cost purchasing, kanban requisition handling and the platform-selection gate fed by Chapter 9's FMEA data.
- **Volume 9** — Tow-Truck Retrieval Protocol experience design served by the §13.10 recovery crawler; Academy curriculum seeded by Chapter 13.
- **Volume 10** — the opex lines this volume quantifies: Artisan roster, parts per 100 Shifts, ≈40–50%/year battery pool replacement (from the canonical 57,720 pack-cycles/year model), tooling capex.
- **Volume 11 (Chapter 6)** — geometry authority for The Works (450 m² GFA, battery room 24 m², charging bunker 30 m² internal); architectural execution of Chapter 1's services checklist, bunker construction, and electrical schedules.
- **Volume 13** — RC WORLD OS modules this volume consumes: the seven-state fleet status machine (§6.3), `maintenance_logs`, PM engine, repair Kanban, battery records, Node firmware pipeline and kill-switch chain.





