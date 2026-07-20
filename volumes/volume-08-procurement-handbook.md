# Volume 8 — Procurement Handbook

**RC WORLD — Master Development Plan** · Volume 8 of 12
**Revision 1.0 • July 2026** · Status: Living document — bump revision on material change

**Purpose of this volume.** This volume is the buying manual for the entire park. RC WORLD's business model rests on a single procurement thesis: the park buys commercial-grade, modifiable RC equipment **direct from Chinese factories at wholesale**, cutting out two to three distribution margins, and converts that cost advantage into fleet depth, spares abundance, and pricing headroom that no competitor buying at hobby-shop retail can match. This volume turns that thesis into an operating system. It sets the procurement doctrine (Chapter 1), maps the Chinese manufacturing geography the park will buy from (Chapter 2), and delivers the core asset of the volume — a directory of more than seventy real Chinese (plus Taiwanese and Hong Kong) manufacturers and brands, profiled by location, specialty, price tier, OEM capability, MOQ class, lead time, and RC WORLD relevance (Chapter 3). It then builds the machinery around the directory: a factory rating scorecard (Chapter 4), OEM and custom-program strategy including park-spec variants and RCW Node pre-installation (Chapter 5), MOQ and lead-time planning with worked buffer-stock math (Chapter 6), a China-specific negotiation playbook (Chapter 7), import and logistics strategy including the LiPo dangerous-goods constraints that shape the whole battery supply chain (Chapter 8), inspection and quality assurance with AQL tables and container checklists (Chapter 9), supplier scorecards and relationship management (Chapter 10), and the SOPs and templates that make the whole system executable by a two-person procurement function (Chapter 11). Where a specific commercial figure (exact MOQ, exact factory-gate price, exact tooling cost) could not be verified from public sources at the time of writing, this volume gives a realistic range and marks it **[verify at factory audit]** — the plan never fabricates precision it does not have.

**Intended readers.** The founder and General Manager (who own supplier strategy in Year 0–1); the Procurement & Logistics Lead (the volume's day-to-day user); The Works' Head Artisan (who co-signs technical evaluations and spare-parts plans, Volume 7); the Finance Lead (landed-cost and payment-terms discipline, Volume 10); investors performing supply-chain diligence on the funding ask.

**Chapters**

1. Procurement Strategy Overview
2. The Chinese RC Manufacturing Landscape
3. Manufacturer Directory
4. Factory Rating System
5. OEM & Custom Programs
6. MOQ & Lead-Time Planning
7. Negotiation Strategy
8. Import & Logistics Strategy
9. Inspection & Quality Assurance
10. Supplier Scorecards & Relationship Management
11. Procurement SOPs & Templates
12. Volume Summary & Cross-References

---

## 1. Procurement Strategy Overview

### 1.1 The direct-wholesale doctrine

Every RC vehicle that reaches a Western hobby shop has typically passed through two or three margin layers: factory → exporter/trading company → national distributor → retailer. Each layer adds 25–60%. A WLtoys 144010-class buggy that retails at $120–140 in the West leaves the factory in Chenghai at roughly $60–90; a Huina 1580 excavator retailing at $600–800 wholesales at $350–420 (source digest, fleet matrix). RC WORLD's doctrine is to buy at or near the factory gate:

1. **Buy factory-direct or one step removed.** For fleet vehicles, spares, electronics and batteries, purchase from the manufacturer's own export department, its official Alibaba/Made-in-China storefront, or (for small brands) its designated export agent. Accept a trading company only where it demonstrably adds value: consolidation of many small brands, English-language engineering support, or credit terms.
2. **Buy at wholesale quantity from day one.** The Phase 1 fleet (~150 powered assets, 3:1 battery ratio, and a spares depth specified in Volume 7) is a genuine wholesale order book — roughly $55,000–75,000 of vehicles and $20,000–30,000 of batteries, chargers, and spares in the first buying wave alone [verify at contract]. That volume commands wholesale pricing, factory attention, and OEM conversation rights that a hobbyist or small shop never gets.
3. **Convert margin into depth, not savings.** The money saved against retail is not banked; it is spent on fleet redundancy (spare complete vehicles), a 3:1 battery ratio, and a spares inventory sized so that no common failure ever idles a revenue asset for more than one working day (Volume 7, Chapter 6).

> **Investor Note.** Direct sourcing is not merely a cost tactic; it is a moat. A competitor buying the same fleet at Western retail needs roughly 1.8–2.4× RC WORLD's fleet capex and pays 2–3× for every replacement part, forever. The procurement function described in this volume is therefore a permanent structural advantage, and the supplier relationships it builds compound over time (Chapter 10).

### 1.2 Total cost of ownership, not unit price

The cheapest quote is frequently the most expensive purchase. Every sourcing decision in this volume is made on **total cost of ownership (TCO) per operating Shift**, not on unit price. The TCO of a fleet vehicle is:

> **TCO = landed unit cost + (spares consumption × parts landed cost) + (artisan labour hours × loaded rate) + (downtime × contribution margin per Shift) − residual/salvage value**, all over the vehicle's service life in Shifts.

Worked contrast (numbers are planning-grade; Volume 10 carries the canonical financial model):

| Metric | Buggy A ("cheapest") | Buggy B (WLtoys 144010-class) |
|---|---|---|
| Landed unit cost | $52 | $78 |
| Spare-parts ecosystem | Sparse, slow (single seller) | Deep, cheap, multi-seller |
| Parts cost / 100 Shifts | $28 | $14 |
| Artisan hours / 100 Shifts | 3.5 h | 1.6 h |
| Expected service life | ~700 Shifts | ~1,400 Shifts |
| **TCO per Shift (labour at $12/h)** | **≈ $0.20** | **≈ $0.09** |

The doctrine that follows: **a vehicle is only purchasable if its spare-parts ecosystem is purchasable.** Before any platform is fleet-approved, procurement must demonstrate three independent sources for its top ten failure parts (Volume 7's failure-parts list: control arms, knuckles, driveshafts, gears, shock shafts, servos, tires, bearings, ESCs, motors).

### 1.3 Dual-sourcing rules

Single-source dependencies are treated as risks with owners and review dates (risk register, Section 9.4 of Volume 1). The rules:

- **Rule DS-1 — every fleet *category* has two qualified platforms.** Example: entry crawler = MN Model MN99S *and* WPL C24; if MN Model's line stops, the category does not.
- **Rule DS-2 — every consumable and high-turnover spare has two qualified *sellers*,** even if both sell the same OEM part (e.g., factory store + a large Chenghai parts consolidator).
- **Rule DS-3 — electronics standards are multi-vendor by design.** XT60 connectors, 2S/3S packs, 540/550 motors, and standard-pinout ESCs are commodity interfaces; any compliant vendor can supply them. Proprietary connectors and sealed packs are banned by battery doctrine (style-guide canon).
- **Rule DS-4 — premium showcase assets are exempt.** The Kabolite-class hydraulic showcase machine is a single-source purchase by nature; it is a display/premium asset, not a rental workhorse, so its downtime does not break the park.
- **Rule DS-5 — failover is pre-negotiated.** The second source is not a name on a list; it has been sampled, audited at least remotely, and holds a dormant price agreement refreshed annually (Chapter 10 failover triggers).

### 1.4 Fleet standardization as procurement leverage

Volume 3's racing doctrine (one or two standardized chassis platforms, personalities via tuning) and Volume 4's construction doctrine (electromechanical Huina-class fleet) are also procurement weapons:

- **Order concentration.** Buying 24 identical touring cars, 18 identical dump trucks, or 60 identical LiPo packs moves the park up every factory's customer-priority list and across MOQ thresholds for OEM asks (Chapter 5).
- **Spares compression.** One chassis platform = one spares bin architecture = fewer SKUs at higher reorder quantities = better pricing and simpler AQL inspection (Chapter 9).
- **Negotiating theatre.** A buyer who says "we will standardize our park on your platform for three years" is offering a factory something rare: predictable, repeating B2B volume in a business dominated by one-shot consumer orders. This is the park's single strongest card and it must be played deliberately (Chapter 7).

### 1.5 The annual procurement calendar

Chinese manufacturing has a heartbeat, and orders must be timed to it. The two dominant events are **Chinese New Year (CNY)** — factories close entirely for 2–4 weeks in the late-January-to-February window, with degraded capacity for 2–3 weeks on either side as migrant workforces travel and re-form — and the **Canton Fair** (China Import and Export Fair, Guangzhou, April and October, with toys/hobby product concentrated in the second phase of each session).

| Month | Procurement action | Rationale |
|---|---|---|
| Jan | Final pre-CNY deliveries land; freeze new POs; annual supplier reviews (Ch. 10). Hong Kong Toys & Games Fair (early Jan) for scouting | Factories quote long or not at all pre-CNY |
| Feb | CNY shutdown. Consume buffer stock; audit inventory; refresh RFQs | No production; plan, don't buy |
| Mar | Place post-CNY "restock wave" POs the week factories re-open; expect first-batch QC risk (new line workers) | Beat the post-CNY backlog; inspect harder |
| Apr | **Canton Fair Phase 2 (toys, ~mid–late Apr)** — annual supplier tour #1: meet incumbents, scout alternates, collect samples | Every major Chenghai/Shenzhen supplier exhibits or hosts visits |
| May–Jun | Negotiate annual agreements off fair meetings; place main fleet-expansion POs | Factories quietest, most flexible |
| Jul | Mid-year scorecard round; sample-test next-year platforms | Low-season attention |
| Aug | Place all Q4 and pre-CNY buffer POs **now** | Western Christmas production peaks Aug–Oct; space and airfreight tighten |
| Sep | Pre-shipment inspections of Q4 orders; book sea freight early (pre-Golden-Week squeeze) | Rates and space degrade into October |
| Oct | China National Day "Golden Week" (Oct 1–7, factories slow); **Canton Fair Phase 2 (late Oct)** — supplier tour #2; China Toy Expo (Shanghai) scouting | Second annual face-to-face round |
| Nov | Final POs that must ship before CNY; confirm production slots in writing | Slots sell out 8–10 weeks before CNY |
| Dec | Receive/inspect pre-CNY wave; build 8–10 week buffer stock on all HIGH-turnover spares | Cover the Feb–Mar supply hole |

> **Trade Hack.** The pre-CNY buffer is not optional. A park that runs out of touring-car control arms in February will not see replacements until late March at the earliest — production restart + backlog + transit. Rule of thumb: on 1 December, on-hand quantity of every HIGH-turnover spare must be ≥ 10 weeks of forecast consumption plus safety stock (worked math in Chapter 6).

### 1.6 Procurement organization and authority

Phase 1 runs procurement with **one Procurement & Logistics Lead** (full-time from Month −6) supported by the Head Artisan (technical evaluation) and the Finance Lead (payments, landed-cost accounting). Authority matrix:

| Decision | Authority | Countersign |
|---|---|---|
| New supplier onboarding | Procurement Lead | GM |
| PO ≤ $2,000 (catalogue spares) | Procurement Lead | — |
| PO $2,000–15,000 | Procurement Lead | GM |
| PO > $15,000 or any OEM/tooling commitment | GM | Founder/Board |
| Supplier suspension / failover trigger | Procurement Lead | GM |
| Payment release against inspection | Finance Lead | Procurement Lead |

All POs, quotes, supplier records, landed-cost calculations and scorecards live in RC WORLD OS procurement module (Volume 13, Chapter 6) — no spreadsheet shadow systems after Month 3.

### 1.7 What the doctrine is not

Four boundaries keep the direct-wholesale doctrine honest:

- **It is not "cheapest wins".** Section 1.2's TCO rule outranks any unit price; a supplier that fails the spares-ecosystem test is unpurchasable at any discount.
- **It is not grey-market importing.** The park declares honestly, pays duties, ships batteries as dangerous goods, and keeps compliance files an insurer can audit (Chapter 8). The margin comes from removing distribution layers, not from removing legality.
- **It is not brand-hostile.** Where a Western-branded platform is genuinely superior for a premium class (TRX-4-class crawlers in the fleet matrix), the park buys it through the cheapest legitimate channel and accepts the margin stack — a handful of premium assets do not justify a parallel-import adventure.
- **It is not a one-person memory.** Every relationship, price, defect, and promise lives in the OS supplier record from day one, because the doctrine must survive staff turnover and franchise replication (Volume 12 licenses this volume to franchisees as an operating asset).

---

## 2. The Chinese RC Manufacturing Landscape

### 2.1 Why China — and why these four clusters

China manufactures the overwhelming majority of the world's RC products — including most vehicles sold under Western brand names — and, decisively for RC WORLD, it is where the **value hobby-grade** band (serviceable, tunable, spare-parted vehicles at near-toy prices) was invented between roughly 2015 and 2024 (Volume 2, Chapter 2 carries the full market analysis). Four geographic clusters matter to this plan, and knowing which cluster a supplier sits in predicts a great deal about its capabilities, pricing, and behaviour.

### 2.2 Shantou / Chenghai — the toy capital

**Chenghai District, Shantou, Guangdong** is the densest toy-manufacturing cluster on earth — thousands of factories and workshops within roughly 20 km, producing a large share of the world's toys and the majority of the RC vehicles in RC WORLD's fleet plan. Huina, MN Model, WPL, WLtoys, MJX, Remo Hobby, HBX, Double E, Heng Long and many others are Chenghai companies (directory, Chapter 3). Cluster characteristics:

- **Strengths:** unbeatable cost engineering; complete local supply chain (mold shops, motor winders, plastic compounders, PCB assemblers within minutes); fast product cycles; deep RC-specific tooling experience; used to export compliance (EN71, ASTM F963, CE).
- **Weaknesses:** quality ceilings — most Chenghai factories engineer to a price, not to a duty cycle; English-language engineering communication is thin outside the biggest firms; brand/factory boundaries blur (one factory may produce for three "brands", and one "brand" may buy from three factories).
- **Behaviour:** Chenghai firms are volume merchants. They respond to concrete quantities and quick decisions, not to long technical correspondence. Site visits are cheap to arrange — dozens of relevant factories can be audited in a three-day trip from the Shantou high-speed-rail station.

### 2.3 Shenzhen (and Huizhou) — the electronics engine

**Shenzhen** supplies the fleet's nervous system: ESCs and motors (Hobbywing, Surpass), radio systems (Flysky, Radiolink), chargers (SkyRC, ToolkitRC, ISDT), batteries (Grepow/Gens Ace), FPV systems (BetaFPV, GEPRC, HGLRC, SpeedyBee), and the PCBA ecosystem (JLCPCB class) that fabricates the RCW Node (source digest; Volume 13). Neighbouring **Huizhou** hosts overflow manufacturing (iFlight; Hobbywing's motor plant). Characteristics:

- **Strengths:** genuine engineering departments; firmware competence; OEM/ODM as a native business model; international-grade communication; certifications (FCC/CE/UN38.3) handled routinely.
- **Weaknesses:** higher labour and land costs than Chenghai (reflected in pricing); consumer-drone regulatory turbulence periodically distracts the FPV firms; fast product churn means spare-part longevity must be contracted, not assumed.
- **Behaviour:** Shenzhen firms think in projects and platforms. They will engage seriously with the RCW Node pre-install proposition (Chapter 5) and with custom firmware asks (detuned ESC profiles) — provided the volumes are honest and the specification is written like an engineering document.

### 2.4 Dongguan, Foshan, and the Pearl River Delta machining belt

Between Shenzhen and Guangzhou, **Dongguan** (ZD Racing, Joysway, Flysky's and Radiolink's production plants, RGT's southern factory) and **Foshan** (LESU) represent the Delta's precision-manufacturing tier: CNC machining, aluminium and zinc die-casting, hydraulics, higher-grade injection molding. This is where the park's metal-intensive premium assets (LESU/Kabolite-class hydraulics, CNC upgrade parts) and its most exacting plastic tooling come from. **Guangzhou** anchors the region with the Canton Fair, HSP's trading networks, and the deepest freight-forwarding market in south China. Characteristics: mid-to-premium pricing, strong OEM culture inherited from decades of contract manufacturing for global brands, and the best factories for "toy platform, industrial expectations" upgrades — exactly RC WORLD's niche.

### 2.5 Yiwu and the trading layer

**Yiwu (Zhejiang)** hosts the world's largest small-commodity wholesale market. Almost nothing is manufactured there; nearly everything can be bought there. For RC WORLD, Yiwu and its online equivalents (Alibaba trading companies, AliExpress consolidators, Taobao agents) are the channel for **long-tail purchases**: diorama and scenery materials (with Volume 2 Chapter 4's supplier study), track furniture, pit-lane consumables, retail-counter merchandise, staff uniforms and giveaway stock. Doctrine: the trading layer is permitted for items where (a) no single item exceeds $500/order, (b) failure is an inconvenience rather than a fleet stoppage, and (c) consolidation into one shipment saves more than the trading margin costs.

### 2.6 Factory or trading company? How to tell

Chinese B2B marketplaces blur the line deliberately; many storefronts marked "Manufacturer" are traders with a related factory, and many honest traders provide real value. The park's verification protocol:

- [ ] **Business licence check.** Request the licence (营业执照) and read the registered *business scope* (经营范围): a factory's scope includes 生产/制造 ("production/manufacturing"); a pure trader's scope reads 贸易/批发 ("trade/wholesale"). Cross-check the registered capital and address on the National Enterprise Credit Information system or via a $30–60 third-party company report.
- [ ] **Product coherence test.** A factory's catalogue is narrow and deep (forty excavator SKUs, one category); a trader's is wide and shallow (excavators, hoverboards, kitchenware). Incoherent catalogues = trader, regardless of the badge.
- [ ] **Ask for the tooling.** Request photos/video of *your product's* injection molds and assembly line with a dated note in frame. Factories comply in days; traders stall or send stock footage.
- [ ] **VAT invoice test.** Ask whether they can issue a 13% VAT special invoice for the goods from the manufacturing entity itself, and whether the exporting entity matches the manufacturing entity. Mismatches are normal (export agents are common) but must be explained coherently.
- [ ] **Video factory audit.** A 45-minute live video walk-through (line, warehouse, QC benches, mold shop) is now a standard, free pre-qualification step — script in Section 4.4.
- [ ] **Third-party verification.** For any supplier expected to take >$10,000/year, commission a supplier-verification report (QIMA/V-Trust class, $100–350) or a full on-site audit (Chapter 9) before the first large PO.

> **Field Note.** Do not treat "trading company" as a slur. Several of the directory's most useful counterparties — Chenghai parts consolidators, LESU's export resellers, Hong Kong upgrade-parts houses — are traders that hold stock, speak fluent English, ship DDP, and answer at 11 p.m. The sin is not trading; it is *hidden* trading, where the buyer prices a factory relationship and gets a middleman's lead times.

### 2.7 OEM/ODM capability levels

The directory (Chapter 3) grades each supplier's customization capability. The scale used throughout this volume:

| Level | Label | What the supplier can actually do | Typical evidence |
|---|---|---|---|
| L0 | Stock only | Sells catalogue product as-is; no changes | Refuses colour/packaging asks |
| L1 | Cosmetic OEM | Custom colours, decals, logo printing, custom packaging at modest MOQs | Existing white-label customers |
| L2 | Configuration OEM | Component swaps within existing tooling: different ESC/servo/motor, connector standard (XT60), firmware settings, pre-installed third-party modules (RCW Node) | Engineering contact who discusses BOMs |
| L3 | Structural ODM | New or modified tooling: reinforced arms, metal replacement parts, custom bodies; co-developed variants | In-house mold shop or captive mold partner |
| L4 | Full ODM/JDM | Designs to a customer specification from a blank sheet | Design department, patent portfolio, brand-name OEM references |

RC WORLD's Phase 1 asks live at **L1–L2** (park colours, XT60 standardization, detuned ESC profiles, RCW Node pre-install); Phase 2–3 asks reach **L3** (reinforced control arms, park-branded bodies). L4 is out of scope this planning horizon — the park is a fleet buyer, not a product company.

### 2.8 The Taiwan and Hong Kong lanes

Two directory sub-populations sit outside mainland logistics. **Taiwan** (MST, Team Magic) means separate freight lanes and customs origin, typically courier or air for the modest volumes involved, and a business culture closer to Japanese suppliers: slower to discount, faster to document, extremely reliable on spec. Do not bundle Taiwanese POs into mainland consolidations; the paperwork friction eats the freight saving. **Hong Kong** (3Racing, Yeah Racing, GPM, JDModel's trading entity) is a commercial layer over PRC manufacturing: English-fluent, small-MOQ-friendly, credit-card/PayPal-tolerant, courier-native — the ideal counterparties for The Works' fast-turn upgrade orders, at a structural 10–20% premium over factory-gate. Both lanes are also the park's hedge against any future mainland export friction on specific categories [monitor annually with the forwarder].

---

## 3. Manufacturer Directory

### 3.1 How to read this directory

This chapter profiles **76 manufacturers and brands** across ten categories. It is the park's sourcing map: every fleet platform in Volumes 3–6 traces to at least one entry here, and every entry carries enough structure to start an RFQ (Chapter 11) the same day. Reading conventions:

- **HQ / factory:** principal verified location; where brand and factory differ, both are noted.
- **Founded:** from company statements or public registries where available; otherwise marked *unverified*.
- **Price tier:** Entry (toy-adjacent) / Value (the park's core band) / Mid / Premium / Flagship.
- **OEM:** capability level L0–L4 per Section 2.7. Levels asserted from public OEM/ODM offers are marked "(claimed)" until audited.
- **MOQ class:** A = off-shelf wholesale, <50 units; B = 50–200; C = 200–1,000; D = 1,000+ or tooling-gated. Classes are planning estimates from published wholesale behaviour — **all MOQs [verify at factory audit]**.
- **Lead time:** indicative production lead time for a wholesale order, ex-works, outside CNY season; add freight per Chapter 8.
- **RCW rating:** 5 = strategic core supplier (fleet doctrine names it); 4 = planned supplier; 3 = qualified alternate / dual-source; 2 = watchlist, sample before relying; 1 = reference/context only.

> **Field Note.** A directory is a snapshot of a fast-moving industry. Chinese RC brands appear, merge, and vanish within two product cycles; the brand on the box is not always the factory behind it. Treat every entry as *true as of July 2026, to be re-verified at order time*, and re-audit the whole directory annually at the Canton Fair rounds (Section 1.5).

### 3.2 Cars, buggies & trucks

The Motorsport Division's volume fleet (Volume 3) comes from this table. The category is dominated by Chenghai, with Dongguan and Shenzhen supplying the performance tier and Hong Kong the upgrade-parts layer.

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 1 | WLtoys (Weili) | Chenghai, Shantou | co. reg. 2011 | High-speed value buggies/tourers (144010, 124017) | Value | L1–L2 (claimed) | B | 3–6 wk | 5 |
| 2 | MJX (Meijiaxin) | Chenghai, Shantou | 1983 (renamed 2001) | Hyper Go brushless 1/16–1/14 line | Value–Mid | L2 (claimed) | B | 4–6 wk | 5 |
| 3 | ZD Racing | Fenggang, Dongguan | ~2011 [verify] | 1/10–1/8 buggies, truggies, DBX-10 | Mid | L2 (claimed) | B–C | 4–8 wk | 4 |
| 4 | HBX / Haiboxing | Chenghai, Shantou | 1990s [verify] | 1/18–1/12 entry buggies (16889 class) | Entry–Value | L1–L2 | B–C | 3–6 wk | 4 |
| 5 | Remo Hobby | Chenghai, Shantou | ~2011 [verify] | 1/16–1/8 trucks, Smax/Mmax lines | Value | L1–L2 | B | 4–6 wk | 3 |
| 6 | JLB Racing | Longhua, Shenzhen | ~2015 [verify] | Cheetah 1/10 brushless tourer/truggy | Value–Mid | L1 | B | 4–8 wk | 3 |
| 7 | SG / Pinecone Forest | Chenghai, Shantou [verify] | 2010s [verify] | 1/16 SG-1603/1604 budget drift & tourers | Entry–Value | L1 | B–C | 3–6 wk | 3 |
| 8 | Hosim / Xinlehong (XLH) | Chenghai, Shantou | 2010s [verify] | Amazon-optimized 1/16–1/10 trucks (9125 class) | Entry–Value | L1 | B–C | 3–5 wk | 2 |
| 9 | LC Racing | Guangdong (Dongguan area) [verify] | ~2011 [verify] | 1/14 competition-grade buggies/truggies (EMB) | Mid | L2 [verify] | A–B | 4–8 wk | 4 |
| 10 | HSP Racing | Guangzhou | ~1990s [verify] | Legacy 1/10 nitro/electric platform ecosystem | Entry–Value | L1–L2 | C | 4–8 wk | 2 |
| 11 | Team Magic | Taiwan HQ; PRC production [verify] | 2003 [verify] | Competition touring (E4 series) | Mid–Premium | L1 | A–B | 4–8 wk | 2 |
| 12 | 3Racing | Hong Kong; PRC factories | 2001 [verify] | Budget competition kits (Sakura line), option parts | Value–Mid | L2 (claimed) | A–B | 3–6 wk | 3 |
| 13 | Yeah Racing | Hong Kong | 2004 [verify] | Aluminium/steel upgrade & option parts | Value–Mid | L2 | A | 2–4 wk | 4 |
| 14 | GPM Racing | Hong Kong | 1980s [verify] | CNC aluminium upgrade parts, brand-specific | Mid | L2 | A | 2–4 wk | 3 |

**WLtoys (Shantou Chenghai Weili Toys Industrial Co., Ltd.)** is canon: the 144010-class buggy is the named Track B platform (fleet matrix). Weili is a genuine Chenghai manufacturer with 500–1,000 staff and a 10,000–30,000 m² plant per marketplace registry data, selling through a dense reseller network at $60–90 wholesale for the 144-series. Strengths: extraordinary price-to-speed; the deepest cheap-spares ecosystem in RC (arms ~$2–4, complete driveshafts ~$5–8 from multiple sellers); every Artisan already knows the platform. Weaknesses: QC variance between batches (motor/ESC lottery), soft stock servos, marketing-grade speed claims; factory-direct communication is transactional, so most buyers work through large Chenghai consolidators. Buy strategy: order vehicles + a 25% spares basket per PO; inspect to the Chapter 9 car checklist; standardize on the brushless 144010 spec for rental duty. **RCW 5.**

**MJX / Meijiaxin Toys** — Chenghai veteran (roots 1983 as Jiaxin Toys, renamed Meijiaxin 2001, per company history) whose **Hyper Go** brushless line (14209/14210 1/14, 16207-class 1/16) redefined entry performance pricing and is a named touring/GT platform in the fleet doctrine. Strengths: modern brushless + gyro spec at $80–130 wholesale, improving parts support, licensed-brand experience (Ferrari, Lamborghini historically), real factory scale. Weaknesses: hobby-grade parts network younger than WLtoys'; some Hyper Go plastics engineered close to their limits — fleet duty needs the metal-upgrade kit basket. **RCW 5.**

**ZD Racing (Dongguan ZD Hobby Co., Ltd.)** — Dongguan factory (Fenggang Town) with 10+ years in RC, brand storefronts in Chenghai. The DBX-10 1/10 desert buggy and 9106 truggy sit one durability class above the WLtoys band at $110–180 wholesale [verify]. Use case: Track B upper class and staff/marshal vehicles. Strengths: metal-geared diffs, real 45–70 km/h performance, factory OEM posture on Made-in-China. Weaknesses: parts pricing ~2× WLtoys; brand support thinner in the West. **RCW 4.**

**HBX / Haiboxing** — long-standing Chenghai maker of entry buggies; the 16889/16890 1/16 class ($45–70 wholesale) is a candidate for the junior/training fleet where crash energy is low. Strengths: cost, simplicity, tolerant electronics. Weaknesses: plastic drivetrain at the margin of rental duty; verify current corporate form at audit. **RCW 4** (junior fleet).

**Remo Hobby** — Chenghai factory (Yongxin Industrial Area, Lianshang) building 1/16–1/8 trucks and buggies with unusually good metal content for the price. Qualified alternate to ZD Racing for Track B upper class. **RCW 3.**

**JLB Racing (Shenzhen Golden Cheetah)** — Shenzhen-based maker of the Cheetah 1/10 brushless platform ($130–190 wholesale [verify]); known for speed, less for refinement. Qualified alternate; sample before fleet commitment. **RCW 3.**

**SG / Pinecone Forest** — budget 1/16 drift and touring line (SG-1603/1604) popular as gyro-equipped entry drifters at $40–60 wholesale; a candidate for the Casual drift taster class where MST would be wasted. Brand/factory structure opaque — **[verify at factory audit]**. **RCW 3.**

**Hosim / Xinlehong Toys** — Chenghai manufacturer behind the Amazon-dominant Hosim brand (9125/9135 class). Useful as a price benchmark and emergency alternate; the park's inspection burden for XLH batches is higher. **RCW 2.**

**LC Racing** — Guangdong maker of genuinely competition-grade 1/14 buggies/truggies (EMB/PTG series, $150–220 wholesale [verify]); the platform used by several national-level small-scale race series. Candidate for the park's racing-league upper class and staff race fleet. Verify factory location and OEM depth at audit. **RCW 4.**

**HSP Racing (Guangzhou)** — the classic first-generation Chinese 1/10 export platform (94122 tourers etc.). Aging designs but a gigantic, cheap, standardized parts ecosystem, and corporate kinship with RGT (crawlers, Section 3.4). Relevance now is mostly parts-layer and context. **RCW 2.**

**Team Magic / 3Racing / Yeah Racing / GPM Racing** — the Taiwan/Hong Kong performance-and-parts layer. Team Magic (competition touring) matters if the racing league professionalizes. **3Racing** (Hong Kong, PRC tooling) supplies the Sakura kit line — the cheapest credible competition chassis — plus vast option-part catalogues; **Yeah Racing** and **GPM** are the park's named channels for aluminium upgrade parts (knuckles, C-hubs, links) for WLtoys/MJX/Traxxas-pattern fleets at MOQ class A with 2–4 week availability. All communicate in fluent English and ship small orders fast — ideal for The Works' running upgrades. Ratings **2–4** as tabled.

> **Trade Hack.** For Chenghai volume brands (WLtoys, MJX, HBX), the fastest wholesale route is often not the factory itself but two or three of the big Chenghai/Shenzhen RC consolidators that hold official distribution. Play them against each other for the same SKU basket: same goods, real competition, and they will bundle mixed-brand spares into one shipment — which the factories will never do.

### 3.3 Drift & touring specialists

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 15 | MST (Max Speed Technology) | Taiwan | 2000s [verify] | RWD drift chassis (RMX 2.5/4.0, FXX) | Premium | L1 | A–B | 4–8 wk | 5 |
| 16 | LDRC | Guangdong [verify] | 2020s [verify] | 1/18 gyro drift RTRs, 1/14 scale tourers | Value | L1–L2 [verify] | B | 3–6 wk | 5 |
| 17 | Sinohobby | Shenzhen [verify] | 2010s [verify] | 1/28 mini touring/drift (Q-series) | Value–Mid | L1 | B | 3–6 wk | 2 |
| 18 | Firelap | Shenzhen [verify] | 2000s [verify] | 1/28 Mini-Z-class racers, timing ecosystems | Value | L2 [verify] | B | 4–6 wk | 2 |

**MST** is the named premium drift platform (source digest): Taiwanese engineering, purpose-built RWD geometry (RMX 2.5 RTR ~$180–260 wholesale [verify]; kits less), superb parts machining. The 12-car drift fleet standardizes on one MST platform with Killerbody/Pandora shells (Section 3.10). Strengths: the best steering geometry and tuning depth in the class; strong global reputation that markets the park's drift program by itself. Weaknesses: Taiwanese pricing; RTR supply allocation can lag demand; parts must be stocked deep because substitutes don't fit. Note for logistics: Taiwan origin changes the freight/customs lane vs PRC goods (Chapter 8). **RCW 5.**

**LDRC** is the named entry-scale platform: 1/18 gyro-equipped drift RTRs (1803 NSX, 1804 MX-5 class, $45–70 wholesale [verify]) with alloy upgrades and LED shells that photograph beautifully — the Casual-tier drift/touring taster. The brand's corporate structure (and its distinctness from the similarly named FPV maker LDARC of Dongguan) must be pinned down at audit — **[verify at factory audit]**. Strengths: instant fun, low crash cost, strong social-media presence. Weaknesses: young parts chain; verify continuity of supply before fleet-scale commitment; dual-source with SG (Section 3.2). **RCW 5.**

**Sinohobby** and **Firelap** cover the 1/28 micro class — relevant only if Phase 3 adds an indoor arena micro league (Volume 3 options list). Watchlist. **RCW 2.**

### 3.4 Crawlers & scale trail

Track C and the Crawler Park (Volume 3) plus the recovery fleet draw from here. This is the fastest-innovating value category in RC.

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 19 | MN Model (Chile Toys) | Chenghai, Shantou | 2010s | 1/12 scale crawlers (MN99S, MN86) | Entry–Value | L1–L2 | B–C | 3–6 wk | 5 |
| 20 | WPL | Chenghai, Shantou | ~2016 [verify] | 1/16–1/10 mini trucks/crawlers (C24, D12) | Entry–Value | L1–L2 | B–C | 3–6 wk | 5 |
| 21 | RGT / Ruitai Model | Kunshan, Jiangsu + Dongguan plant | 2013 | 1/24–1/10 crawlers (EX86 line); OEM/ODM | Value–Mid | L2–L3 (stated) | B–C | 4–8 wk | 5 |
| 22 | FMS Model | Shenzhen | 2007 | Licensed scale crawlers (FCX24/FCX10), planes | Mid | L2–L3 | B | 4–8 wk | 4 |
| 23 | RocHobby | Shenzhen (FMS brand) | 2010s | Scale crawlers/vehicles under FMS group | Mid | L2 | B | 4–8 wk | 3 |
| 24 | Eazy RC | Shenzhen [verify] | ~2021 [verify] | 1/18 RTR scale crawlers (Triton, Arizona) | Value | L1 | B | 4–6 wk | 3 |
| 25 | Cross RC | Shenzhen [verify] | ~2013 [verify] | Premium scale truck/crawler kits (8×8, trial) | Premium | L2 [verify] | A–B | 4–8 wk | 3 |
| 26 | Traction Hobby | China (Guangdong) [verify] | ~2017 [verify] | 1/8 large-scale crawlers (Founder/KM) | Mid–Premium | L2 [verify] | A–B | 4–8 wk | 2 |
| 27 | Yikong Model | China [verify] | ~2020 [verify] | 1/10–1/8 RTR scale crawlers (4102/4103) | Value–Mid | L1–L2 [verify] | B | 4–6 wk | 3 |
| 28 | Capo Racing | China [verify] | 2000s [verify] | Ultra-detailed crawler kits (JK Max) | Flagship | L1 | A | 6–12 wk | 1 |
| 29 | Orlandoo Hunter | Guangdong [verify] | ~2015 [verify] | 1/32–1/24 micro scale kits | Value–Mid | L1 | A–B | 4–6 wk | 2 |

**MN Model** (brand of Chile Toys, Xinxiang Road Industrial Zone, Chenghai) is canon: the MN99S 1/12 crawler anchors the entry crawler fleet at $45–60 wholesale (fleet matrix). Strengths: absurd value, huge aftermarket of metal upgrades, simple electronics that Artisans can service in minutes, iconic Defender-style looks customers recognize. Weaknesses: toy-grade stock electronics (upgrade servo + ESC on fleet units), plastic transmission gears (fit the brass upgrade at induction — Volume 7 build sheet), batch QC variance. **RCW 5.**

**WPL** (Fengxia Street, Chenghai) is the C24/C34/D12 mini-truck factory — the second leg of the entry-crawler dual source and the park's scale-utility comedy fleet (D12 drift vans are a social-media weapon). Wholesale $30–60. Same strengths/weaknesses profile as MN with an even bigger modding culture. **RCW 5.**

**RGT (Ruitai Model Technology)** — established 2013, HQ Kunshan (Jiangsu), with a modern Dongguan factory (2020) running CNC, injection molding, and ABB body-cutting; explicitly offers OEM/ODM (company statements). The EX86 1/10 crawler line ($120–200 wholesale [verify]) is the named premium-tier crawler candidate alongside TRX-4-class imports, and RGT's OEM posture makes it the leading candidate for a park-spec crawler (park colours, XT60, RCW Node pre-fit — Chapter 5). Strengths: real factory, stated OEM/ODM openness, trademark registrations in EU/US, scale range 1/24–1/10. Weaknesses: brand less known to Western customers than Traxxas — mitigated by park context where customers ride the experience, not the badge. **RCW 5.**

**FMS Model (Shenzhen, est. 2007)** — 300+ staff, licensed-scale specialist (Land Rover, Toyota licences) whose FCX24/FCX18/FCX10 crawlers bring showroom-grade detail at Value-Mid pricing; also a first-rank foam-plane maker (Section 3.6). The FCX24 ($60–90 wholesale [verify]) is the premium *mini* crawler option; licensing means bodies the public instantly recognizes. **RCW 4**, with **RocHobby** (its scale sub-brand) at **3**.

**Eazy RC / Cross RC** — related Shenzhen scale-crawler operations [corporate linkage **verify at factory audit**]: Eazy RC sells accessible 1/18 RTRs; Cross RC sells premium multi-axle truck and trial kits ($250–900) beloved by advanced hobbyists. Eazy RC is a Casual-fleet candidate; Cross RC is a Works showcase/build-class platform (Volume 7 custom-build curriculum). **RCW 3 / 3.**

**Traction Hobby, Yikong, Capo, Orlandoo Hunter** — respectively: 1/8 large-scale crawlers with presence (premium supervised class candidate, **2**); fast-rising value RTR crawlers to dual-source the premium tier (**3**); the Rolls-Royce of crawler kits, one display/build unit at most (**1**); micro-kits for retail/Academy build classes rather than fleet (**2**).

### 3.5 Construction, mining & agriculture

The Construction Division (Volume 4) is the park's differentiator, and this supplier set is its backbone. Doctrine reminder: the *rental* fleet is electromechanical (lead-screw) — Huina class; hydraulics (Kabolite/LESU/JDModel class) are premium supervised experiences and display only.

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 30 | Huina (Guangdong Huina Model) | Chenghai, Shantou | 2012 | 1/14 electromechanical construction fleet (1580/1582/1583) | Value | L1–L2 | B | 4–8 wk | 5 |
| 31 | Kabolite | Chenghai, Shantou (Huina premium line) | ~2018 [verify] | Full-hydraulic 1/14–1/16 machines (K970, K961/963, K336) | Premium–Flagship | L1 | A | 6–12 wk | 5 |
| 32 | LESU Model | Danzao, Foshan | 2000s [verify] | 1/14 hydraulic excavators, trucks, metal option parts | Premium | L2–L3 | A–B | 6–12 wk | 4 |
| 33 | JDModel (Eagle Machinery) | HK entity; Guangdong production [verify] | 2010s [verify] | CNC hydraulic excavators/loaders/dozers | Flagship | L2 [verify] | A | 8–16 wk | 3 |
| 34 | Tongde | China [verify] | [unverified] | 1/14 hydraulic loaders/dozers, aggressive pricing | Mid–Premium | [unknown] | A–B | 6–12 wk | 2 |
| 35 | XDRC | China [verify] | [unverified] | 1/14 construction models & metal parts | Mid | [unknown] | B | 6–10 wk | 2 |
| 36 | Diecast Masters (RC line) | US brand; PRC manufacture | 2010s | Officially licensed Cat® RC/diecast machines | Mid–Premium | L0–L1 | A | via distribution | 2 |
| 37 | Double E (Doubleeagle Industry) | Chenghai, Shantou | 1988 | Licensed RC toys & E351 tractors; CaDA bricks; 300+ molding machines | Entry–Value | L2–L3 (stated) | C | 4–8 wk | 5 |
| 38 | Heng Long | Chenghai, Shantou | 1986 (workshop roots) | 1/16 RC tanks, metal chassis sets; some marine | Value–Mid | L1–L2 (claimed) | B | 4–8 wk | 2 |
| 39 | Huina parts ecosystem (consolidators) | Chenghai/Shenzhen | — | Tracks, pins, motors, lead-screws for 15xx fleet | Value | — | A | 1–3 wk | 4 |

**Huina (Guangdong Huina Model Co., Ltd., Chenghai, founded 2012)** is the single most important supplier in this plan. The 1580 V4 excavator ($350–420 wholesale), 1582/1573 dump trucks ($150–200), and 1583 wheel loader ($180–220) *are* the Mining Zone fleet (fleet matrix; 1:3 excavator:truck ratio). Huina pivoted from electronics gifts to RC construction around 2015 and now leads the global hobby segment, with in-house mold making and export compliance experience. Strengths: metal structures with lead-screw (fluid-free) actuation exactly matching the park's electromechanical doctrine; spares availability; V-generation improvements each cycle; a factory used to container-quantity buyers. Weaknesses: control feel is steppier than hydraulics (accepted trade-off); electronics are the weak point under rental duty (stock 15% spare mainboards/ESCs); documentation is thin, so The Works writes its own service manuals (Volume 7). OEM asks in play: park colours, XT60, Heavy-Node pre-wiring [negotiate at audit]. **RCW 5.**

**Kabolite** — Huina's premium hydraulic line from the same Chenghai group: K961/K963 excavators ($1,750–1,900 retail class), K336GC, K970 flagship (~$10,500–12,500 retail, 31 kg, brushless, 18-channel radio) and K5701 dump (~$670) (research anchors, July 2026). Role: the **premium supervised experience and showcase machine** — one to two units in Phase 1, expanding with the Premium Shift program ($22/38 pricing tier). Strengths: near-industrial hydraulic realism that anchors marketing and justifies premium pricing; shared parentage with Huina simplifies commercial relations. Weaknesses: hydraulic maintenance burden (seals, fluid — exactly why doctrine bans it from open rental); five-figure flagship capex; allocation queues on new releases. **RCW 5** (premium tier).

**LESU Model Technology (Danzao Town, Nanhai District, Foshan)** — the metal-machining champion of 1/14: hydraulic excavators (Aoue-SK500, PC360 class), mining trucks, and the deepest catalogue of CNC option parts and truck components in the industry; one of the earliest 1/14 truck-parts makers in China (company statements). Role: premium display/experience alternates to Kabolite; source of metal upgrade assemblies for the truck fleet; long-term partner for Phase 3 showcase builds. Kits demand skilled assembly — a feature for The Works' build program, a cost everywhere else. **RCW 4.**

**JDModel / Eagle Machinery** — flagship-grade CNC hydraulic machines (excavators, wheel loaders, the D575 dozer) retailing $1,900–7,400 via Western resellers; HK-registered trading/manufacturing entity with PRC production [structure **verify at factory audit**]. Watch for Phase 3 destination showcase pieces; not a Phase 1 purchase. **RCW 3.** **Tongde** and **XDRC** are lower-priced hydraulic challengers seen through reseller channels; data is thin and quality reports mixed — sample and audit before any commitment. **RCW 2 / 2.**

**Diecast Masters (RC)** — the officially Cat-licensed line (US brand, Chinese manufacture). Relevance: licensed realism for retail shelf and possibly a licensed premium experience; but park fleet purchases route to Huina/Kabolite economics. **RCW 2.**

**Double E (Doubleeagle Industry (China) Ltd., Chenghai, founded 1988)** is canon for Agriculture: the E351 tractor (1/16, $80–120 wholesale) with hitch-standardized implement library (Volume 4, Agriculture Zone). One of Shantou's largest toy groups: 300+ injection-molding machines, in-house mold production, BSCI/CE/ASTM certification, and licensing relationships (Mercedes-Benz, Volvo, JCB, Land Rover among others per company statements) — meaning L2–L3 OEM capability is credible if the park later wants park-branded tractors. Weaknesses: toy-grade electronics on entry SKUs (fleet units get servo/ESC upgrades per Volume 7); MOQ class C for custom work. **RCW 5.**

**Heng Long (Chenghai, roots 1986)** — the world's dominant RC tank maker (1/16 battle tanks, metal chassis options, IR combat systems), with marine SKUs. Not in current fleet doctrine, but tanks are a recurring customer request and a plausible Phase 3 "armour arena" event class; keep warm. **RCW 2.**

> **Field Note.** Entry 39 is not one company but a function: two or three Chenghai/Shenzhen consolidators that keep Huina 15xx tracks, idlers, pins, lead-screw assemblies, and mainboards on the shelf. The Works' continuous consumables (track pins, grease, motors — source digest spares list) flow through them weekly; the factory itself only sees quarterly volume POs. Qualify two, scorecard them like factories (Chapter 10).

### 3.6 Aviation & FPV

Phase 2 fleet (~20 aircraft, netted airfield — Volume 5). Procurement begins Month 10–12; directory maintained from Day 1 because electronics cross-pollinate (radio links, chargers, batteries).

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 40 | Volantex / Exhobby | Shantou | 2000 (brand 2005) | Foam trainers, warbirds, gliders; RTF ecosystems | Value | L2–L3 (stated ODM) | B–C | 4–8 wk | 5 |
| 41 | XK / WLtoys air | Chenghai, Shantou | 2010s | Entry fixed-wing (A250/A430), helis | Entry–Value | L1 | B–C | 3–6 wk | 4 |
| 42 | Eachine | Guangzhou/Shenzhen (Banggood house brand) | ~2014 [verify] | Entry FPV quads, RTF bundles | Entry–Value | L0–L1 | A–B | stock | 3 |
| 43 | BetaFPV | Longgang, Shenzhen | 2017 | Tiny Whoop/cine whoops, RTF FPV kits | Value–Mid | L2 | B | 4–6 wk | 5 |
| 44 | iFlight | Huizhou | 2014 | FPV quads (Nazgul/Cidora), motors, frames | Mid | L2–L3 | B | 4–8 wk | 4 |
| 45 | GEPRC | Shenzhen | brand 2012 | FPV quads (Cinelog), OEM/ODM offered | Mid | L2–L3 (stated) | B | 4–8 wk | 4 |
| 46 | Flywoo | Shenzhen [verify] | ~2019 [verify] | Micro long-range quads (Explorer) | Mid | L2 [verify] | B | 4–6 wk | 3 |
| 47 | HGLRC | Shenzhen | 2016 | FPV components, budget quads | Value–Mid | L2 | B | 4–6 wk | 3 |
| 48 | SpeedyBee | Shenzhen | 2010s [verify] | Flight controllers, app-configurable stacks | Value–Mid | L2 | B | 4–6 wk | 3 |
| 49 | Happymodel | Shenzhen/Dongguan [verify] | ~2016 [verify] | Ultralight whoops (Mobula series) | Value | L1–L2 | B | 4–6 wk | 4 |
| 50 | EMAX | Shenzhen [verify] | ~2004 [verify] | Motors, Tinyhawk RTF line | Value–Mid | L2 | B | 4–6 wk | 3 |
| 51 | T-Motor | Nanchang, Jiangxi | ~2009 [verify] | Premium UAV/FPV motors | Premium | L2–L3 | B | 4–8 wk | 2 |
| 52 | RadioMaster | Shenzhen [verify] | ~2019 [verify] | EdgeTX radios (TX16S/Pocket), ELRS | Value–Mid | L1–L2 | B | 4–6 wk | 4 |
| 53 | LDARC | Dongguan | 2010s | FPV drones/parts; drone-soccer ecosystems | Value | L2 (claimed) | B | 4–6 wk | 2 |

**Volantex (Shantou VolantexRC / Exhobby, est. 2000; VolantexRC brand 2005)** is the anchor fixed-wing supplier: crash-tolerant foam trainers (Trainstar, Sport Cub, ASW28 gliders) at $40–120 wholesale, plus the Racent marine line (Section 3.7). Company states ODM services and ~$3.35 M annual export on its Alibaba profile. Strengths: RTF completeness, gyro-stabilized trainers ideal for tethered/instructed Shifts, one commercial relationship covering air and water. Weaknesses: foam airframes are consumables under rental duty (order 30–40% airframe-only spares); electronics adequate but not premium. **RCW 5.**

**BetaFPV (Shenzhen Longgang, est. February 2017)** anchors the indoor/netted FPV program: Tiny Whoop-class quads (Meteor65/75) and Cetus RTF kits ($25–60 wholesale per quad [verify]) that bounce off nets and people harmlessly — the only FPV class permitted for uninstructed customers under Volume 5 safety doctrine. Strengths: the most complete beginner-to-intermediate ecosystem in micro FPV (quad + goggles + radio + simulator in one carton), deep spares (frames, canopies, motors sold in fleet-friendly multipacks), and a brand customers already know from YouTube. Weaknesses: product churn — a given Meteor revision lives 12–24 months, so fleet buys must include end-of-life spares. **RCW 5.**

**Happymodel (Shenzhen/Dongguan [verify])** builds the Mobula6/Mobula7 ultralight whoops that dominate the sub-25 g class — the qualified dual source to BetaFPV under Rule DS-1, with near-identical economics and the lightest airframes (least sting on contact, a safety selling point). Parts interchange partially with BetaFPV stock (motors, cameras), which compresses the spares bin. **RCW 4.**

**iFlight (Huizhou, 2014)** is the largest of the freestyle/racing makers (Nazgul Evoque and Chimera lines, plus motors and frames sold as components) with a genuine factory campus in the Greater Bay Area and consistent global distribution. Role: the 3–5-inch instructor, display, and cinematic tier — flown by staff pilots and licensed advanced customers only (Volume 5 licensing gates). **GEPRC (Shenzhen, brand 2012)** — legal entity Shenzhen Beizao Innovation Technology, ~100–200 staff, 3,000–5,000 m² plant, explicit OEM/ODM offer per marketplace data — is the credible counterparty if the park later wants a park-liveried cinewhoop fleet (Cinelog class) for the spectator-feed drone that films races (Volume 9 media plan). **Flywoo** (Explorer long-range micros) and **HGLRC** (Shenzhen, 2016; budget components) are qualified alternates and the component layer for The Works' FPV repair bench. **SpeedyBee** matters for a different reason: its app-configurable flight controllers let Artisans tune and diagnose without a laptop — a workflow win worth standardizing on for staff quads. **RCW 4 / 4 / 3 / 3 / 3** respectively.

**EMAX (Shenzhen [verify], one of the oldest motor houses in FPV)** supplies the Tinyhawk RTF line — the strongest single-box alternative to BetaFPV's Cetus for the training fleet — and motors with long revision lives, which fleet maintenance loves. **T-Motor (Nanchang, Jiangxi)** is the premium motor tier: relevant only if Phase 3 fields a sponsored demo/race team where failure is reputational. **RadioMaster (Shenzhen [verify])** standardizes the airfield's radio fleet: EdgeTX open-source firmware, multi-protocol RF, and per-student model profiles — one TX16S/Pocket pool serving every trainer protocol on the field, with lockable profiles that enforce beginner rates (the airborne cousin of the ESC detune doctrine). **XK/WLtoys air** (A250/A430 class, $30–60) equips the "first flight" bulk tier where write-offs are budgeted, riding the existing WLtoys commercial relationship. **Eachine**, Banggood's house brand, is a stock-availability convenience for odd items rather than a factory relationship — useful, never load-bearing. **RCW 3 / 2 / 4 / 4 / 3.**

### 3.7 Marine

Phase 2 pond complex (~24 vessels — Volume 6). Small category, but the venue-starved boat niche gives it outsized community value.

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 54 | Joysway Hobby | Dongguan | ~2009 | RC sailboats (DragonFlite 95), speedboats | Value–Mid | L2–L3 (stated) | B–C | 4–8 wk | 5 |
| 55 | Volantex marine (Racent) | Shantou | 2012 (line) | Value speedboats (Vector series) | Value | L2 | B–C | 4–8 wk | 4 |
| 56 | TFL Hobby | Shenzhen [verify] | 2000s [verify] | CNC-aluminium/fiberglass race hulls | Premium | L2 [verify] | A–B | 6–10 wk | 3 |
| 57 | Feilun | Shantou/Shenzhen [verify] | 2000s [verify] | Entry boats (FT011/FT012) | Entry–Value | L1 | B–C | 3–6 wk | 3 |
| 58 | Henglong marine | Chenghai, Shantou | (see #38) | Entry/mid boats from the tank house | Entry–Value | L1 | B | 4–8 wk | 2 |

**Joysway (Dongguan, est. ~2009)** is the strategic marine partner, and the reason is one product: the **DragonFlite 95**, a one-design racing sailboat with an organized global class association. One-design means every hull is identical by rule — which is the park's racing doctrine (skill decides, hardware doesn't) already institutionalized by someone else. A DF95 park fleet plugs the Marine Division straight into an existing worldwide ranking culture and gives the sailing league instant legitimacy. Around it, Joysway's electric hulls (Bullet, Magic series, $40–110 wholesale [verify]) cover the powerboat Shifts, and the company's stated OEM/ODM posture makes park-liveried hulls a realistic L1–L2 ask. Weaknesses: sailboats demand wind and coaching (staffing implication, Volume 6); electric hull electronics need the same waterproofing audit as every marine brand. **RCW 5.**

**Volantex Racent** (Vector SR48/SR65/SR80, $30–90 wholesale) is the volume speedboat tier — self-righting hulls, tolerant electronics, and it rides the existing Volantex air relationship, so one supplier meeting covers two divisions. **TFL Hobby (Shenzhen [verify])** machines CNC-aluminium and fiberglass race hulls one class above anything else in the table — the premium demo/race tier and a source of hardware (struts, rudders, couplers) for The Works' marine bench. **Feilun** (FT011/FT012 class, $25–60) is the budget dual source and a retail-shelf line; treat its included electronics as replaceable. **Heng Long marine** exists mainly as an alternate quote. Marine-specific procurement notes: order 2× propeller sets and flex-shafts per hull per season (the category's tires); UV and water ingress make ESC potting/conformal coating a receiving-inspection checkpoint (Chapter 9); pond-weed tolerance testing is a sample-evaluation criterion (Chapter 11 form); and every marine PO includes hull-only spares at 15–20% of fleet count, because hulls fatigue at dock impacts long before electronics die. **RCW 4 / 3 / 3 / 2.**

### 3.8 Electronics: power systems, radios, chargers

The standardization layer — these choices bind the whole fleet (XT60, 2S/3S, common radio protocols, bunker charging doctrine).

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 59 | Hobbywing | Longgang, Shenzhen (+ Huizhou motor plant) | 2005 | ESCs & brushless systems (QuicRun/EzRun/XeRun) | Mid–Premium | L2–L3 | B | 4–8 wk | 5 |
| 60 | Flysky | Shenzhen (Dongguan production) | 2006 | Radio systems (NB4/NB4+, GT5, i6); custom RF solutions | Value–Mid | L2–L3 (stated) | B–C | 4–8 wk | 5 |
| 61 | Radiolink | Futian, Shenzhen (Dongguan plant) | 2003 | Radios (RC4GS/RC6GS/AT10), receivers, GPS modules | Value–Mid | L2–L3 | B | 4–6 wk | 4 |
| 62 | Surpass Hobby / Rocket | Longgang, Shenzhen | 2013 | Budget–mid brushless motors/ESC combos | Value | L2 | B–C | 3–6 wk | 5 |
| 63 | SkyRC | Shenzhen | 2008 | Chargers (T1000 quad-channel class), analyzers | Mid | L2 | B | 4–6 wk | 5 |
| 64 | ToolkitRC | Bao'an, Shenzhen | 2018 | Compact smart chargers (M6D/Q6AC), tools; custom charging OEM (stated) | Value–Mid | L2–L3 (stated) | B | 4–6 wk | 4 |
| 65 | ISDT | Shenzhen | ~2015 [verify] | Smart chargers (K4 dual-channel class) | Mid | L2 [verify] | B | 4–6 wk | 4 |
| 66 | HOTA | Shenzhen [verify] | [unverified] | Value multi-channel chargers (D6 Pro class) | Value–Mid | [unknown] | B | 4–6 wk | 3 |
| 67 | Power HD | Shenzhen [verify] | 2000s [verify] | Digital servos 15–45 kg class | Value–Mid | L2 | B–C | 3–6 wk | 4 |

**Hobbywing (Shenzhen, 2005)** is the named ESC standard (source digest): QuicRun 10BL120/16BL30-class ESCs for the racing fleet, with programmable profiles that implement the park's tuning-personality and detune doctrine (Volume 3). A national "Little Giant" enterprise with real firmware depth — the counterparty for the Chapter 5 ask of **park-spec ESC profiles** (thermal + current limits tuned for rental abuse, locked customer profiles). **Flysky (Shenzhen, 2006)** is the named radio standard: NB4/GT5-class surface radios, i6-class air; the company advertises customized wireless solutions, which is exactly the Phase 2–3 conversation about park-locked transmitter firmware and QR-bound handsets (Volume 13 binding flow). **Surpass Hobby (Shenzhen Surpass Tech, 2013)** supplies fleet motors (540/550 brushed for construction; 2838/3650-class brushless for cars) at $6–25 wholesale — the named motor source. **SkyRC (2008)** and **ISDT** are canon for the charging bunker (T1000 / K4-class multi-channel balance chargers per battery doctrine), with **ToolkitRC** (2018; states custom charging OEM work) the value alternate and field-tool source, **HOTA** the budget dual source [audit before reliance]. **Radiolink** doubles as an RCW Node component source (its GPS modules are drop-in candidates for the ATGM336H position in the Node BOM — Volume 13 engineering note). **Power HD** standardizes the 15 kg/25 kg servo spec from the source digest's spares list. All entries here communicate in professional English and are accustomed to B2B/OEM terms; MOQs for custom firmware asks are the binding constraint (Chapter 5).

### 3.9 Batteries

The most safety- and logistics-critical category (UN3480/3481 rules, Chapter 8; bunker doctrine, Volume 7). Fleet standard: 2S/3S LiPo, XT60, 3:1 ratio.

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 68 | Grepow (Gens Ace / Tattu) | Longhua, Shenzhen (4 plants) | 1998 | Full-stack LiPo maker; RC + UAV packs; custom cells | Mid–Premium | L3–L4 | C | 6–10 wk | 5 |
| 69 | CNHL (China Hobby Line) | Shenzhen [verify] | ~2005 [verify] | Direct-sale value LiPo (Black/MiniStar) | Value | L1–L2 [verify] | B | 3–6 wk (stock) | 5 |
| 70 | Ovonic (Ampow) | Guangdong [verify] | ~2017 [verify] | Value LiPo, strong 2S/3S car range | Value | L1 [verify] | B | 3–6 wk | 4 |
| 71 | Zeee Power | Guangdong [verify] | ~2010s [verify] | Value LiPo, marketplace-optimized | Value | L1 [verify] | B | 3–6 wk | 3 |
| 72 | Auline | Shenzhen [verify] | ~2018 [verify] | FPV-focused Li-ion/LiPo packs | Value–Mid | L1 [verify] | B | 4–6 wk | 2 |

**Grepow (Shenzhen Grepow Battery Co., Longhua, founded 1998)** — parent of **Gens Ace** (RC, brand from 2010) and **Tattu** (UAV): ~3,500 staff, four factories totalling ~250,000 m², 300+ R&D engineers, and genuine custom pack and BMS programs (company statements) — one of very few directory entries that is a *cell maker*, not a pack assembler buying cells elsewhere. This is the park's quality anchor: Gens Ace packs for the racing and premium fleets, where sag consistency directly affects the lap-parity doctrine, and the long-term counterparty for a custom park pack — park-branded, XT60, capacity tuned so a full Casual Shift lands at the doctrinal ~30% buffer (realistic custom MOQ 500–2,000 packs [verify]; the park crosses that line in Year 1 at 3:1 ratios). Weaknesses: premium pricing (30–60% over value brands) and Class C MOQs for anything custom. **RCW 5.**

**CNHL (China Hobby Line)** is the named value source (source digest): a factory-direct e-commerce operation whose Black Series and MiniStar lines price roughly 30–50% under Western-branded equivalents with well-regarded consistency and — critically — a decade of routine experience shipping DG worldwide, including sea-freight bulk. The volume workhorse for construction, crawler, and marine fleets where a few percent of sag consistency is invisible. Verify the manufacturing entity behind the storefront at audit (pack assembly vs cell origin). **RCW 5.**

**Ovonic (Ampow)** and **Zeee Power** are the qualified value alternates under Rule DS-2 — both Guangdong pack assemblers optimized for marketplace retail, both credible on 2S/3S car packs, both to be batch-tested harder (Chapter 9 capacity sub-sampling) because marketplace-tier QC is statistically noisier. **Auline** matters when Phase 2 FPV wants Li-ion endurance packs for staff camera quads. Battery procurement rules, non-negotiable: every PO requires current **UN38.3 test summaries and MSDS**; every batch gets the Chapter 9 LiPo inspection including per-cell voltage and IR sampling; suppliers must ship via DG-certified forwarders (Chapter 8); and no pack enters service without an RC WORLD OS asset record binding it to cycle-count tracking and the bunker charging log (Volume 13). **RCW 4 / 3 / 2.**

### 3.10 Bodies, upgrade parts & accessories

| # | Supplier | HQ / factory | Founded | Specialty | Tier | OEM | MOQ | Lead time | RCW |
|---|---|---|---|---|---|---|---|---|---|
| 73 | Killerbody | Shenzhen [verify] | ~2011 [verify] | Licensed hard/poly bodies, scale accessories | Mid–Premium | L2–L3 | B | 4–8 wk | 5 |
| 74 | Pandora RC | Japan (design); PRC-facing supply chain [verify] | 2000s [verify] | 1/10 drift body kits (JDM styles) | Premium | L1 | A–B | 4–8 wk | 4 |
| 75 | Team C | Brand (EU-linked); PRC manufacture [verify] | 2000s [verify] | Polycarbonate bodies, wide catalogue | Value–Mid | L2 [verify] | B | 4–6 wk | 3 |
| 76 | Injora | Shenzhen [verify] | ~2016 [verify] | Crawler upgrade parts, wheels/tires, scale accessories | Value | L1–L2 | A–B | 2–4 wk | 4 |

**Killerbody (named in source digest)** supplies the drift/touring fleet's licensed body shells and scale detail parts — the visual identity of Track A. Buy pre-painted park-livery batches (L2 ask: custom paint/decal MOQ realistically 50–200 shells [verify]). **Pandora RC** is the premium Japanese-designed drift-shell line for league and showcase cars (its "China ops" are effectively distribution/production interfaces — treat commercially as an import via HK/JP channels [verify]). **Team C** provides value polycarbonate volume. **Injora** is the crawler-fleet accessory engine — cheap, fast, vast catalogue — ideal for retail-shelf stock (Volume 9 retail plan) as well as fleet upgrades.

### 3.11 Diorama & scale-scenery suppliers

Volume 2, Chapter 4 carries the commissioned deep study of Chinese diorama and miniature-environment makers; this section holds only the procurement interface. Three buying channels: (1) **architectural-model-supply manufacturers** (scale trees, figures, textured sheet — the Guangzhou/Shenzhen model-shop supply belt; Evemodel-class online brands [verify entities at order time]); (2) **Chenghai/Yiwu généraliste suppliers** for signage, fencing, cones, barrels, container props at toy pricing; (3) **brick-construction makers** (Double E's CaDA line, MouldKing class) for modular buildings the Academy can rebuild seasonally. Procurement treats scenery as MOQ-class A–B consumables ordered twice yearly with the fleet waves; landed-cost discipline still applies (it is bulky, low-value freight — sea LCL only, never air).

> **Trade Hack.** The park's most photogenic scenery — graded aggregate, boulders, timber — is *local* (quarry and landscaping supply), not imported. Import only what must be to-scale and manufactured (figures, signage, structures). This halves scenery freight and makes the Mining Zone's material replenishable in a pickup truck (Volume 4 site operations).

---

## 4. Factory Rating System

### 4.1 Purpose and scope

Every supplier expected to receive more than $5,000/year, or to supply any fleet-critical item at any spend, must carry a **Factory Rating** before the first volume PO. The rating is produced once at onboarding (desk research + video audit, upgraded to on-site audit at the next China trip) and refreshed annually. It feeds the quarterly scorecard (Chapter 10), which tracks *performance*; the Factory Rating tracks *capability*.

### 4.2 The six dimensions and weights

| Dimension | Weight | What is measured | Evidence sources |
|---|---|---|---|
| Quality system | 25% | Incoming/in-process/final QC existence and records; defect rates on samples; AQL literacy; calibration of test gear | Audit walk-through, sample inspection results, ISO 9001 (bonus, not required) |
| Communication | 15% | Response time, English/technical clarity, one named account contact, honesty about problems | 90-day correspondence log |
| Engineering depth | 20% | Real R&D staff, mold shop access, BOM transparency, ability to discuss changes at L2–L3 | Engineering call, tooling photos, change-request test |
| Capacity & flexibility | 15% | Lines, shifts, realistic monthly output vs. promises; small-batch tolerance; peak-season behaviour | Audit, order history, peak-season test order |
| Compliance & ethics | 15% | Business licence coherence; export record; safety/cert files (EN71/ASTM/CE/FCC/UN38.3 as applicable); labour conditions observed | Registry checks, certificate verification, audit observation |
| Financial stability | 10% | Registered capital, years trading, litigation flags, credit report; does it survive a bad season? | Third-party company report ($30–60), payment-term behaviour |

**Scoring:** each dimension 1–5 (anchored rubrics in the audit workbook, Chapter 11); weighted sum × 20 gives a 0–100 score.

| Score | Class | Procurement consequence |
|---|---|---|
| ≥ 80 | A — Strategic | Eligible for OEM programs, annual agreements, 30/70 terms, sole-PO status within dual-source rules |
| 65–79 | B — Qualified | Volume POs allowed; 100% pre-shipment inspection until two clean quarters |
| 50–64 | C — Conditional | Sample/small POs only; corrective-action plan required to grow |
| < 50 | D — Not approved | No POs; re-audit possible after 12 months |

### 4.3 Audit question bank (excerpt)

The full 90-question bank lives in the procurement workbook; the twenty highest-yield questions:

1. Show me the production line building *this* SKU today. (If it isn't running: when did it last run?)
2. Who owns the injection molds for this product — you, or a customer? May I photograph them?
3. What is your incoming QC procedure for motors/ESCs you buy in? Show the last rejection record.
4. What percentage of last month's output failed final QC, and what were the top three defects?
5. Show me your repair/rework station. (No rework station = defects ship.)
6. Which export markets do you ship to, and under which certifications? Show current test reports for this SKU.
7. What is your realistic monthly capacity for this SKU in October? In March?
8. How many workers return after CNY, on average? (Honest answers: 70–90%.)
9. If we standardize on this platform for three years, what changes for us? (Tests imagination and B2B literacy.)
10. Can you fit customer-supplied electronics (a 25×25 mm PCB) inline between receiver and ESC on your line? What would you charge per unit?
11. What is the smallest custom-colour batch you have actually produced? For whom (category, not name)?
12. Walk me through what happens when a customer rejects a batch at pre-shipment inspection.
13. Which components in this product have single-source suppliers upstream of *you*?
14. Show me how finished goods are packed for a sea container. Drop-test standard?
15. What are your payment terms for a first order, and when did you last give 30/70 to a new customer?
16. Who is my engineering contact by name, and what are their working hours?
17. What spare parts do you commit to producing after this SKU is discontinued, and for how long?
18. Has your company changed its registered name or legal entity in the last five years? Why?
19. What happens to our tooling and our spec if we stop ordering for a year?
20. What do you *not* make well? (The only honest factories answer this one.)

> **Field Note.** Question 20 is the audit inside the audit. A factory that names a real weakness ("our painting line is inconsistent, we outsource metallic colours") is managing quality; a factory that answers "no weakness" is managing *you*.

### 4.4 The 45-minute video audit script

The free pre-qualification step referenced in Section 2.6, run over WeChat/WhatsApp video with the sales contact walking and the buyer directing. Insist the call is live (ask them to pan to a window, a clock, today's newspaper equivalent — a dated production board works). Sequence:

1. **Gate and signage (2 min).** Company name on the building vs. the licence name. Photograph.
2. **The line running your SKU or its family (15 min).** Count stations and workers; watch one unit assembled end-to-end; ask the line worker (via the guide) what the most common assembly fault is. Look for torque drivers with set clutches vs. raw electric screwdrivers — a small tell with high signal.
3. **Incoming-material and QC benches (10 min).** Ask to see today's incoming inspection record and the reject shelf. An empty reject shelf is a bad sign, not a good one.
4. **Warehouse and packing (8 min).** Carton stacks, humidity, drop-test rig if claimed, how packed goods are staged by customer.
5. **Mold shop or mold storage (5 min).** For factories claiming L2–L3: see the tools, ask which are customer-owned.
6. **Close (5 min).** Ask the three hardest bank questions (Q4, Q8, Q20 from Section 4.3) face-to-face; note whether answers match the earlier email answers.

Score the six rating dimensions provisionally the same day, while impressions are fresh; the on-site audit later confirms or corrects. Cost: zero. Suppliers who refuse a video walk with two weeks' notice are auto-classed D.

---

## 5. OEM & Custom Programs

### 5.1 What "park-spec" means

RC WORLD's fleet is standard product, modified. The park's OEM program converts the highest-value modifications from Works labour (paid at artisan hours) into factory options (paid pennies at assembly). The Phase 1–2 ask list, in priority order:

| Ask | Level | Target suppliers | Realistic MOQ [verify] | Cost effect | Value |
|---|---|---|---|---|---|
| XT60 connector standard, no proprietary plugs | L2 | All vehicle makers | often 50–100/SKU | ±$0 | Kills connector chaos; battery doctrine |
| Park colours + decals, custom carton | L1 | Huina, WLtoys, MJX, MN, WPL, Double E | 100–500/SKU | +$0.5–2/unit | Brand coherence; theft deterrence |
| Detuned ESC profile (current/thermal caps, soft throttle curve) | L2 | Hobbywing, Surpass; vehicle makers using own ESCs | 100–500 units or firmware fee $500–2,000 | +$0–1/unit | Fleet lifetime + lap-parity doctrine |
| RCW Node pre-install (harness tap, Node mounting, JST XH pigtail for Heavy-Node) | L2 | Huina, RGT, MJX, WLtoys [negotiate] | 200–500/SKU | +$1–3/unit labour | Deletes ~20 min/vehicle of Works labour |
| Reinforced high-failure parts (metal knuckles/arms as line-fit) | L2–L3 | MJX, RGT, ZD, Huina | 500–1,000 or tooling | +$2–6/unit | Halves top failure mode |
| Upgraded servo line-fit (15/25 kg Power HD-class) | L2 | Construction & crawler makers | 100–300/SKU | +$3–8/unit | Deletes the #1 Works retrofit |
| Park-branded battery pack (label + capacity spec) | L1–L2 | Grepow, CNHL | 500–2,000 packs | ±$0 at volume | Asset control, doctrine-tuned capacity |
| Custom body shells (park livery, sponsor panels) | L2–L3 | Killerbody, Team C | 50–200 shells | +$2–5/shell | Sponsorship inventory (Volume 9) |

### 5.2 Tooling economics

Structural asks (L3) mean tooling money. Planning figures for Chinese injection tooling [all verify at quotation]: simple single-cavity tool for a small arm/knuckle **$1,500–5,000**; multi-cavity production tool **$5,000–20,000**; a full vehicle body tool **$8,000–30,000**. Amortization rule: an L3 ask is approved only when (tooling cost ÷ expected 3-year unit volume) + unit-price delta < 60% of the Works retrofit labour it replaces. In practice this means Phase 1 buys **zero custom tools**; the first plausible L3 case is a reinforced touring-car arm at Phase 2 fleet scale, and even that competes against simply stocking more $2 arms (Chapter 6 math).

### 5.3 Who owns what

Every OEM engagement states in writing: (1) tooling paid by RC WORLD is RC WORLD property, tagged and photographed, removable on 30 days' notice; (2) park livery, logos, and the RCW Node design are RC WORLD IP, usable only on park POs; (3) factory improvements to their own base product remain theirs. Do not pay for tooling on another customer's mold, and do not accept "free tooling" amortized invisibly into unit prices without a stated buyout schedule.

### 5.4 IP protection basics: NNN before NDA

A Western NDA is close to unenforceable against a Chinese factory. The standard instrument is the **NNN agreement — Non-Disclosure, Non-Use, Non-Circumvention** — drafted (a) in Chinese as the governing text, (b) under PRC law, (c) with jurisdiction in the supplier's local court or CIETAC arbitration, and (d) with liquidated damages in RMB per breach event. Cost from a China-focused firm: $800–2,500 per template class [verify]. Doctrine:

- NNN **before** any RCW Node schematic, park-spec ESC parameter set, or customer-data-adjacent integration is shared. Fleet colour schemes and decals do not need NNN theatre.
- The Node's real IP protection is architectural: factories receive a mounting/harness spec and a black-box unit, never gerbers or firmware (Volume 13 security posture).
- Register the RC WORLD trademark in China (classes 28 toys, 41 entertainment, 9 software) **before** the first branded OEM order — China is first-to-file; cost $300–600/class via agent [verify].
- Assume anything customer-visible will be imitated if the park succeeds. The moat is the operation (telemetry, ERP, venue, brand), not the plastic.

> **Trade Hack.** The cheapest OEM concession in China is paint, and the most expensive is firmware. Sequence asks accordingly: win colours/connectors/cartons in the first negotiation (they cost the factory nothing and build the habit of saying yes), and bring the ESC-profile and Node-pre-install asks only once you are a proven repeat buyer with a face — typically at the second Canton Fair meeting, not the first email.

### 5.5 Case study: the detuned ESC, end to end

The single highest-value L2 ask, walked through as a template for all others. **Problem:** stock 144010-class buggies pull ~55–60 km/h — thrilling, and lethal to consistency: crash rates and drivetrain wear scale super-linearly with top speed, and lap-parity doctrine (2–3% across the fleet) is impossible when ESC batches vary. **Specification:** a locked customer profile at ~70% throttle ceiling, softened initial punch, thermal cutback at 85 °C, low-voltage cutoff aligned to the 3.4 V/cell doctrine — and a PIN-protected staff profile at full power for marshal vehicles and events. **Routes:** (a) vehicle factory flashes its stock ESC supplier's firmware variant — cheapest, but opaque and batch-risky; (b) the park standardizes on Hobbywing QuicRun-class ESCs fleet-wide and orders them pre-programmed from Hobbywing at 100–500-unit MOQ, then has the vehicle factory line-fit them (the recommended route: one ESC vendor, auditable parameters, and the swap doubles as the QC uplift the value platforms need anyway); (c) Works flashes everything by hand — the Phase 0 fallback, ~6 min/vehicle. **Economics (route b):** ESC delta +$9–14/vehicle over stock [verify], offset by measured reductions in crash damage and ESC failures; break-even at roughly one avoided control-arm-plus-labour incident per vehicle per season — comfortably cleared by Volume 3's damage assumptions. **Verification:** every batch sampled at PSI with a programming-card readback against the parameter sheet (Chapter 9 checklist line). The general lesson: every OEM ask needs this same chain — problem, spec, route options, economics, verification — before it goes in front of a factory.

---

## 6. MOQ & Lead-Time Planning

### 6.1 MOQ bands by category

Planning bands compiled from published wholesale behaviour of the Chapter 3 directory — **confirm per supplier at RFQ**:

| Category | Stock wholesale (class A/B) | Custom colour (L1) | Config OEM (L2) | Structural (L3) |
|---|---|---|---|---|
| Value cars/buggies (WLtoys/MJX class) | 20–100 units | 100–500 | 200–500 | 1,000+ |
| Crawlers (MN/WPL/RGT) | 20–100 | 100–300 | 200–500 | 1,000+ |
| Construction (Huina 15xx) | 10–50 | 100–200 | 200–300 | 500+ |
| Premium hydraulics (Kabolite/LESU) | 1–5 | 10–50 | 20–50 | negotiated |
| Foam aircraft (Volantex/XK) | 20–100 | 100–500 | 300–500 | 1,000+ |
| FPV quads (BetaFPV class) | 10–50 | 50–200 | 100–300 | 500+ |
| Boats | 20–100 | 100–300 | 200–500 | 1,000+ |
| ESCs/motors/radios | 50–200 | 100–500 | 200–1,000 (fw fee alt.) | 1,000+ |
| LiPo packs | 50–200 | 500–1,000 | 500–2,000 | 2,000+ |
| Spares/upgrade parts | 10–100 lots | n/a | n/a | tooling-gated |

The Phase 1 fleet order (64 cars, 30 construction, 12 tractors, 16+4 crawlers, batteries at 3:1) clears stock-wholesale MOQ everywhere and reaches L1 thresholds on the four biggest SKUs (touring cars, buggies, dump trucks, entry crawlers) when initial + first replenishment orders are combined on one annual agreement — which is exactly how procurement should present it (Chapter 7).

### 6.2 The lead-time stack

Total replenishment lead time = **production + QC + freight + customs + inland**, and each stage has a season:

| Stage | Courier route | Sea LCL route | Notes |
|---|---|---|---|
| Production (stock SKU) | 1–3 wk | 3–6 wk | 0 if consolidator holds stock |
| Production (L1/L2 batch) | — | 4–8 wk | Post-CNY add 2–4 wk |
| Pre-shipment inspection | 2–4 d | 3–5 d | Book at 80% completion |
| Freight | 3–7 d | 30–45 d port-to-door | Air freight middle option 7–12 d |
| Customs & inland | 1–3 d | 3–10 d | DG (batteries) adds 3–7 d |
| **Planning total** | **2–5 wk** | **9–17 wk** | Use 12 wk sea planning figure |

### 6.3 Buffer-stock math — worked example: touring-car control arms

Doctrine: no common failure idles a revenue asset >1 working day. Control arms are the #1 impact casualty (source digest failure list). Inputs (Volume 3/7 planning figures):

- Fleet: 24 touring/GT cars; average 30 Shifts/car/week in season.
- Failure rate: 1 arm per 90 Shifts (planning figure from rental-duty assumptions; recalibrate from RC WORLD OS failure logs after Month 3).
- **Demand d** = 24 × 30 ÷ 90 = **8 arms/week**; observed weekly σ assumed 4.
- Replenishment: consolidator stock via courier, **L = 3 weeks**; deep restock via sea PO, 12 weeks.
- Service target 98% (z = 2.05).

Safety stock = z × σ × √L = 2.05 × 4 × √3 ≈ **14 arms**.
Reorder point = d × L + SS = 8 × 3 + 14 = **38 arms**.
Order quantity: arms cost ~$2.5 landed in 10-packs; carrying cost is trivial against a $15 lost Shift, so order in 100-unit lots (≈ 12 weeks of demand) and let the pre-CNY rule (Section 1.5) override: on 1 Dec, on-hand ≥ 10 wk × 8 + 14 = **94 arms minimum**.

The same arithmetic runs for every HIGH-turnover spare in Volume 7's inventory list; RC WORLD OS computes d and σ live from maintenance logs and flags reorder points automatically (Volume 13, inventory module). Two structural lessons: (1) cheap parts get deep stock — the math almost never justifies scarcity on sub-$5 items; (2) the *battery* buffer is set by the 3:1 doctrine and DG lead times (sea, 12–17 wk), so battery POs are placed two seasons ahead, not from reorder points.

### 6.4 The expedite ladder

When buffer math fails anyway — a demand spike, a lost carton, a failed lot — procurement climbs a pre-priced ladder rather than improvising:

| Rung | Action | Typical cost premium | Buys back |
|---|---|---|---|
| 1 | Pull from dual-source consolidator stock (courier) | +15–30% on parts | 2–4 wk |
| 2 | Air-freight the in-production balance (non-DG only) | +$3.5–6/kg | 3–5 wk vs sea |
| 3 | Cannibalize the spare-vehicle pool (Volume 7 authorizes) | internal | immediate |
| 4 | Cross-class substitution (run adjacent fleet class at higher rotation) | revenue mix effect | immediate |
| 5 | Local retail purchase at destination pricing | +100–180% | days |

Each rung is legitimate; the failure mode is skipping to rung 5 by panic. The OS shortage alert names the rung the playbook recommends, and every rung-2+ event triggers a Chapter 10 review of why the buffer failed.

---

## 7. Negotiation Strategy

### 7.1 The relationship premise

Chinese factory negotiation is repeat-game, not one-shot. Price is remembered for a quarter; behaviour is remembered for a decade. The park's posture: a **small but permanent customer** — modest orders by export standards ($75k–120k/year across the directory) but repeating, predictable, technically literate, and publicity-generating. That posture, played consistently, buys more than aggressive price-grinding: priority slots before CNY, honest defect disclosure, engineering favours, first allocation on new releases.

### 7.2 Price anchoring around published wholesale

Never open a negotiation blind. For every SKU the RFQ pack (Chapter 11) records: (a) the factory's own Alibaba/Made-in-China listed band; (b) two consolidator quotes; (c) the Western street price ÷ 2.2 as a sanity anchor. Open at the bottom of the evidenced band, not below it — quoting under the credible band signals ignorance and invites the classic counter: a "yes" delivered with silent component downgrades. Target outcomes: 8–15% under listed wholesale on volume SKUs, plus non-price wins (spares bundles, carton customization, inspection access) that are worth more than the last 3%.

> **Trade Hack.** Ask every vehicle factory for a **"spares ratio" line** in the PO: 5–10% of order value in a factory-picked assortment of that SKU's fastest-moving parts, at parts-wholesale prices, packed in the same cartons. Factories price this generously (it's their own inventory), it ships freight-free inside the vehicle shipment, and it seeds The Works' bins with exactly what the factory *knows* breaks.

### 7.3 Payment terms

- **Norm: 30/70 T/T** — 30% deposit at PO, 70% against copy of bill of lading or, better, **against passed pre-shipment inspection** (fight for this sequencing; A-class suppliers grant it).
- First orders with unproven suppliers: **Alibaba Trade Assurance** even at 1–2% platform cost — the dispute mechanism is real leverage while trust is zero.
- Never 100% up front, at any discount. Never Western Union/private accounts; company-to-company bank transfer only, matching the licence name (mismatch = the Section 2.6 protocol failed).
- Letters of credit are overkill below ~$50k/PO; revisit for Phase 2 container-scale orders.
- Currency: quote and pay USD Year 1; consider RMB pricing later if the bank spread + factory USD-hedging premium exceeds ~2% [review with Finance, Volume 10].

### 7.4 The Canton Fair playbook

Twice-yearly rhythm (Section 1.5). Tactics that pay:

1. **Book incumbents before the fair** — booth meetings are for renewal signatures and new-model previews; discovery happens in the aisles.
2. **Walk Phase 2 (toys/hobby) with the fleet matrix printed.** A buyer holding a real order book is visibly different from a browser; booth staff escalate to owners fast.
3. **Collect quotes on a standard one-page RFQ card** (SKU, quantity band, target spec, inspection expectation) so post-fair comparison is mechanical.
4. **Visit factories the same week** — Chenghai is 4 hours from Guangzhou by high-speed rail; a fair trip that skips factory floors wastes half its airfare.
5. **Bring the telemetry demo.** A two-minute live RCW Node + dashboard demo does more for OEM credibility than any deck; factories decide whether you're technically real within minutes.
6. Off-years alternates: Hong Kong Toys & Games Fair (Jan) for scouting; China Toy Expo Shanghai (Oct) for Chenghai brands' domestic lines.

### 7.5 Consolidated-freight leverage and sample protocol

Because the park ships consolidated (Chapter 8), it can dangle **carton-level add-ons** to smaller suppliers: "join our monthly LCL from Shenzhen and your effective MOQ to us drops." This wins better pricing from accessory makers (Injora/Yeah Racing class) who otherwise gate on courier costs. Sample protocol, fixed: pay full sample price + courier without negotiation (it marks you as serious); order samples from two suppliers minimum per category; run samples through the Volume 7 teardown rubric and the Chapter 11 sample-evaluation form; photograph everything into the supplier record; then negotiate volume with sample defects as the agenda. Refuse "free samples against future order promises" — they create soft obligations that cost more than the sample.

### 7.6 When it goes wrong

Escalation ladder for disputes (defect batch, silent spec change, delay): (1) evidence pack within 48 h — photos, video, inspection report, PO clause; (2) proposed remedy sized to the harm (rework, discount, freight credit, replacement in next shipment) — factories settle fast when the ask is proportionate; (3) withhold the 70% only if inspection-gated terms allow; (4) Trade Assurance / CIETAC per contract; (5) failover to the dual source (Chapter 10 triggers) — and say so plainly. Do not threaten what you will not execute; in a repeat-game market, empty threats price you as noise.

---

## 8. Import & Logistics Strategy

### 8.1 Incoterms for this business

Incoterms (2020) define where the supplier's risk and cost end. The four that matter here:

| Term | Supplier delivers… | RC WORLD pays/handles… | When to use |
|---|---|---|---|
| **EXW** (Ex Works) | at their factory door | everything: China pickup, export clearance, freight, import, delivery | Only with a strong forwarder; maximum control, maximum admin |
| **FOB** (Free On Board, named port) | loaded on vessel at (e.g.) Shenzhen/Yantian | ocean freight, insurance, import, inland | **Park default for sea shipments** — clean split, forwarder-friendly, prices comparable across suppliers |
| **CIF** (Cost, Insurance, Freight to named port) | to destination port, minimally insured | import clearance, duties, inland | Acceptable for one-off buys; hides freight margin, weakens control — avoid as default |
| **DDP** (Delivered Duty Paid) | to the park gate, duties paid | nothing but receiving | Small courier orders and sample flows; verify duties were genuinely paid, not smuggled under-declared |

Doctrine: **FOB Shenzhen/Yantian (or Shantou) for consolidated sea; DDP courier for samples and urgent spares; EXW only when consolidating multiple small Chenghai suppliers via our own forwarder's warehouse.**

### 8.2 Freight modes and when

| Mode | Cost (planning) | Door-to-door | Use for |
|---|---|---|---|
| Courier (DHL/FedEx/SF class) | $5–9/kg | 3–7 d | Samples, urgent spares <30 kg, documents |
| Air freight (forwarder, airport-to-airport + handling) | $3.5–6/kg | 7–12 d | Season-saving replenishment 30–300 kg; never batteries without DG lane |
| Sea LCL (less than container) | $30–80/m³ + $150–350 fixed fees per shipment | 5–8 wk | **Park default**: monthly/bi-monthly consolidation |
| Sea FCL 20 ft (~28 m³ usable) | $1,500–4,000 lane-dependent (volatile post-2024; verify at booking) | 5–8 wk | Fleet waves ≥ ~15 m³ — initial fleet, annual expansion |
| Rail/truck (China–Europe lanes, if applicable) | between air and sea | 3–5 wk | Verify by destination country |

Rule of thumb: below ~2 m³ LCL fixed fees dominate — batch orders until a consolidation clears 3 m³. The Phase 1 initial fleet (~150 vehicles + spares + scenery) is realistically **one 20 ft FCL plus one DG battery shipment plus 2–3 LCL follow-ups** [verify volumes at packing-list stage].

### 8.3 Freight forwarders

Appoint **one primary freight forwarder with proven dangerous-goods capability and a South-China consolidation warehouse** (Shenzhen/Guangzhou), plus one backup. Selection checklist:

- [ ] Licensed for DG sea (IMDG) and DG air (IATA CAT-certified staff) — ask for battery shipment references, not assurances
- [ ] Consolidation warehouse accepting multi-supplier cartons with photo-on-receipt service
- [ ] Destination-country customs brokerage in-house or partnered
- [ ] All-in quotes to door showing every fee line (watch: fuel, CIC, peak, chassis, DO fees)
- [ ] Cargo insurance at ~0.2–0.4% of CIF value arranged per shipment
- [ ] Weekly status reporting the Procurement Lead can pipe into RC WORLD OS

### 8.4 Customs classification and duties

- **RC models and vehicles:** heading **9503** (toys, including reduced-scale models, whether or not working) covers most RC cars, construction models, and parts under the WCO nomenclature; some destination regimes push hobby-grade or camera-equipped items elsewhere (e.g., drones toward aircraft/UAS headings post-2022 WCO updates). **Classification and duty rates are destination-specific — verify locally with the customs broker before the first shipment**; many jurisdictions apply 0% to modest duty on 9503 plus local VAT/GST on CIF + duty.
- **Batteries:** lithium cells/packs classify under **8507.60** (lithium-ion) with their own duty profile, and their transport is governed by DG rules regardless of duty (next section).
- Declare honestly. Under-declaration to save a few percent of VAT puts the entire container — and the operating licence narrative in front of investors — at risk. The landed-cost model (8.6) treats duty as a planning line of 0–5% pending local verification.

### 8.5 LiPo dangerous-goods reality — a major planning factor

Lithium batteries are Class 9 dangerous goods, and this constraint shapes the park's battery logistics more than price does:

- **UN3480** — lithium-ion batteries shipped alone. Air: IATA PI965, **cargo aircraft only**, state of charge ≤ 30%, Class 9 fully regulated (no passenger-flight uplift). Sea: IMDG Class 9, DG declaration, UN-spec packaging.
- **UN3481** — batteries **packed with** or **contained in** equipment (PI966/PI967). Slightly gentler handling; this is how RTR vehicles with included packs typically move.
- Every shipment needs the supplier's **UN38.3 test summary** and MSDS on file; carriers and forwarders will ask, and so will the park's insurer (Volume 10 risk schedule).
- Practical doctrine: **batteries travel by sea, in consolidated DG shipments, two seasons ahead of need** (lead time 12–17 wk). Air-freighting LiPo is possible via DG lanes at $6–12/kg equivalent but is the emergency channel, not the plan. Vehicles ship with batteries *removed to a separate DG consignment* where feasible — it simplifies both inspection and any non-DG air contingency for the vehicles themselves.
- Small-parcel "battery included" e-commerce shipments that dodge DG paperwork are common in the hobby and **prohibited for the park**: uninsurable, seizable, and indefensible in a safety-first business that operates a public charging bunker.

> **Safety Warning.** DG compliance is not only a shipping formality. Receiving inspection (Chapter 9) must verify packs arrive at storage charge (~3.80–3.85 V/cell), undamaged and unswollen, before they enter the bunker inventory. A pack that shipped abused enters service pre-damaged — and fails in a customer's hands.

### 8.6 Worked landed-cost example

Consolidated LCL replenishment from Shenzhen, FOB, destination a mid-size international city (planning rates; rebuild with real quotes per shipment — template in Chapter 11):

| Line | Basis | Amount |
|---|---|---|
| 40 × MJX Hyper Go 1/14 @ $95 FOB | invoice | $3,800 |
| 20 × MN99S @ $52 FOB | invoice | $1,040 |
| Spares basket (arms, gears, servos, tires) | invoice | $1,150 |
| **FOB subtotal** | | **$5,990** |
| Sea LCL 4.2 m³ @ $55/m³ + $260 fixed | freight | $491 |
| Cargo insurance 0.3% × (FOB+freight) | insurance | $19 |
| **CIF value** | | **$6,500** |
| Import duty (planning 3% on CIF; **verify locally**) | duty | $195 |
| VAT/GST (planning 15% on CIF+duty; **verify locally**; often recoverable) | tax | $1,004 |
| Broker + DO + inland delivery | fees | $310 |
| Pre-shipment inspection (1 man-day) | QA | $290 |
| **Landed total (ex-recoverable VAT)** | | **$7,285** |

Landed-cost factor = 7,285 ÷ 5,990 ≈ **1.22 on FOB** (ex-VAT). Planning factors adopted: **1.20–1.30 sea LCL; 1.12–1.18 FCL; 1.35–1.60 courier/DDP small orders; batteries add 3–6 points for DG handling.** Every unit cost quoted anywhere in this master plan as "landed" uses these factors until real lanes are priced.

---

## 9. Inspection & Quality Assurance

### 9.1 Third-party inspection layer

For every PO ≥ $3,000, and every battery PO of any size, commission a **pre-shipment inspection (PSI)** at the factory when goods are ≥ 80% complete and packed. Providers in the QIMA / V-Trust / HQTS / SGS / Bureau Veritas / TÜV class operate across Guangdong on 48-hour booking at **$230–350 per man-day** [verify current rate cards]; one man-day covers one location and roughly one AQL sample of the sizes below. Annual budget: 14–18 man-days ≈ **$3,500–5,500** — noise against the fleet capex it protects. Factory audits (Chapter 4) from the same firms run $300–700/day. Never let the *supplier* book or pay the inspector.

The service menu, and when the park uses each:

| Service | When performed | Park usage |
|---|---|---|
| Pre-shipment inspection (PSI) | ≥ 80% produced & packed | **Default** on every qualifying PO |
| During-production inspection (DUPRO) | 20–50% produced | First OEM batch of any L2+ ask; first post-CNY batch from B/C-class suppliers |
| Initial production check (IPC) | Materials/first articles | New tooling (L3) only |
| Container loading supervision (CLS) | At loading | FCL fleet waves and every DG battery consignment (verifies packaging, marks, quantities into the sealed box) |
| Supplier verification / audit | Onboarding, annual | Per Chapter 4 |

One tactical note: rotate inspection firms occasionally, and never announce which units the inspector will sample. Factories learn individual inspectors' habits; variety keeps the sampling honest.

### 9.2 AQL sampling, explained and tabled

PSIs use ISO 2859-1 / ANSI-ASQ Z1.4 sampling. The park's standard: **General Inspection Level II, AQL 0 critical / 2.5 major / 4.0 minor.** Critical = safety (battery damage, exposed mains, sharp edges); Major = function or durability loss (won't run, cracked chassis, wrong ESC); Minor = cosmetic. Working table:

| Lot size | Sample size | Critical (0): Ac/Re | Major (2.5): Ac/Re | Minor (4.0): Ac/Re |
|---|---|---|---|---|
| 51–90 | 13 | 0 / 1 | 1 / 2 | 1 / 2 |
| 91–150 | 20 | 0 / 1 | 1 / 2 | 2 / 3 |
| 151–280 | 32 | 0 / 1 | 2 / 3 | 3 / 4 |
| 281–500 | 50 | 0 / 1 | 3 / 4 | 5 / 6 |
| 501–1,200 | 80 | 0 / 1 | 5 / 6 | 7 / 8 |
| 1,201–3,200 | 125 | 0 / 1 | 7 / 8 | 10 / 11 |
| 3,201–10,000 | 200 | 0 / 1 | 10 / 11 | 14 / 15 |

Ac = accept at or below; Re = reject at or above. A rejected lot triggers the Chapter 10 corrective-action process: 100% factory rework and re-inspection at supplier cost is the standard remedy written into every PO (Chapter 11 checklist).

### 9.3 Park-specific PSI checklists

**Container/lot of RC cars (touring/buggy class):**

- [ ] Quantity, SKU, colour/livery vs PO; carton markings and drop-test spec
- [ ] Per sample: visual (chassis cracks, flash, paint), fastener torque spot-check, wheel/hex tightness
- [ ] Function: bind to radio, full throttle/brake/steer sweep on stand, 2-minute floor run, steering trim within spec, gyro (drift class) engages
- [ ] Electrical: connector is XT60 per park spec; ESC model matches BOM (photograph!); servo spec matches; no hot ESC/motor after run
- [ ] Spares basket present and matching packing list; manuals/decals in carton
- [ ] Serial capture: photograph model plate + MAC/ID where present for RC WORLD OS asset pre-registration

**Lot of LiPo packs:**

- [ ] UN38.3 summary + MSDS accompany shipment; cartons carry correct UN3480/3481 marks
- [ ] Per sample: voltage per cell 3.80–3.85 V (storage), cell IR within datasheet band, no swelling/dents/leaks, XT60 + JST-XH balance lead orientation correct
- [ ] Capacity test on sub-sample (2–5 packs): discharge at 1C to 3.5 V/cell ≥ 95% of rated
- [ ] Label: capacity, C-rating, batch code present; batch recorded for OS cycle tracking
- [ ] Reject lot on ANY critical (swollen/damaged cell) regardless of AQL arithmetic

**Lot of excavators (Huina 15xx class):**

- [ ] Metal structure: boom/stick/bucket pins seated, no casting cracks, track tension in spec, no missing track pins
- [ ] Function: full boom/stick/bucket travel under load (sample digs prepared sand tray), slew smooth, lead-screw current draw within spec (no stall clicking), limit behaviour at end stops
- [ ] Electronics: mainboard version noted, connectors seated, radio range spot-check 30 m
- [ ] 15% spare mainboard/ESC line present per PO; grease points pre-lubricated
- [ ] Livery/decals per park spec; Heavy-Node pre-wiring present if the L2 ask applies (JST XH pigtail, correct polarity — meter every sample)

### 9.4 Incoming-goods inspection at the park

> **SOP PRC-01 — Incoming Goods Inspection.** Rev 1.0 · Owner: Procurement & Logistics Lead · PPE: gloves, safety knife · Tools: multimeter, cell checker, scale, camera, OS terminal · Frequency: every shipment, within 24 h of arrival.
>
> 1. Photograph consignment sealed; verify carton count vs packing list; note damage on carrier POD before signing.
> 2. Quarantine batteries to the bunker ante-room immediately; no LiPo waits on the receiving dock.
> 3. Sample-check per Section 9.2 sizes against the relevant checklist (cars / packs / machines); PSI report open alongside — you are auditing the audit.
> 4. Register accepted assets in RC WORLD OS (`fleet_inventory` for vehicles, battery batch records for packs); print asset tags; route vehicles to The Works induction queue (Volume 7 build sheets: metal-gear fits, Node install, detune verification).
> 5. Log defects with photos into the supplier record; if the lot fails, freeze payment steps per PO terms and open corrective action (Chapter 10) within 48 h.
> 6. File customs docs, UN38.3, MSDS, inspection certificates into the compliance folder (insurer + authority audits, Volume 10).

---

## 10. Supplier Scorecards & Relationship Management

### 10.1 Quarterly scorecard

Every active supplier ≥ $2,500/year is scored quarterly in RC WORLD OS on delivered performance (distinct from the Chapter 4 capability rating):

| Metric | Weight | Data source | 5 looks like | 1 looks like |
|---|---|---|---|---|
| On-time delivery | 25% | PO vs receipt dates | ≥ 95% lines on time | < 70% |
| Quality (lot acceptance + field failures) | 30% | PSI results + Works failure logs | ≥ 98% lots accepted, field failures at plan | Rejected lots, systemic field failures |
| Price stability vs agreement | 15% | Invoice audit | Honoured bands, honest surcharges flagged early | Silent increases, spec downgrades |
| Responsiveness | 15% | Correspondence SLA log | < 24 h substantive answers | Ghosting, holiday blackouts unannounced |
| Documentation & compliance | 15% | Shipment file completeness | Every doc right first time | Chasing UN38.3s at the port |

**Sample filled-in scorecard — Q3 (illustrative), supplier: Huina (vehicles + spares):**

| Metric | Score | Note |
|---|---|---|
| On-time delivery | 4 | 1583 loader batch slipped 9 days post-Golden-Week; flagged in advance |
| Quality | 4 | 2 lots accepted clean; field mainboard failures 1.8%/quarter vs 2.5% plan |
| Price stability | 5 | Annual band honoured; freight surcharge documented |
| Responsiveness | 4 | Engineering answers in 36 h avg; sales in 12 h |
| Documentation | 5 | Complete, first time |
| **Weighted total** | **4.3 / 5** | Class A trajectory — renew annual agreement; raise Node pre-install ask at October meeting |

### 10.2 Corrective action and failover triggers

**Corrective-action process (CAP):** any rejected lot, field-failure spike (>150% of plan for two consecutive months), or documentation breach opens a CAP: written problem statement with evidence → supplier root-cause + containment within 10 working days → agreed remedy and verification method → verified closure recorded on the scorecard. Two open CAPs = new POs require GM sign-off.

**Failover triggers (Rule DS-5 executes):** score < 2.5 for two consecutive quarters; a critical safety defect reaching customers; insolvency signals (asked for >30% deposit changes, licence changes, factory visits refused); discontinuation of a fleet platform without the contracted spares tail. On trigger: dormant dual-source agreement activates, open POs complete under escrowed terms, and the supplier moves to Class C pending re-audit.

### 10.3 The annual review

Each January (pre-CNY freeze, Section 1.5): consolidate four quarters of scorecards, re-run the Chapter 4 capability rating for A/B suppliers, re-verify licences and certificates, refresh dormant dual-source pricing, and issue next year's annual agreements ahead of the April Canton Fair signing round. Output: a one-page **Supplier Portfolio Map** (category × class × spend) for the GM and board pack — the procurement function's annual report card.

---

## 11. Procurement SOPs & Templates

### 11.1 RFQ template (one page per SKU)

1. **Header:** RFQ ID, date, buyer contact, validity requested (60 d).
2. **Item:** SKU/model, photos, target spec table (scale, motor/ESC, servo, connector = XT60, battery = 2S/3S none-included option, colour/livery code).
3. **Quantities:** three bands (e.g. 50 / 150 / 400) — always ask three; the curve reveals cost structure.
4. **Terms requested:** FOB port, 30/70 T/T with 70% against passed PSI, spares-ratio line 7% of order value, lead time ex-works, carton spec + drop test.
5. **Compliance:** certifications required for destination; battery documentation if applicable.
6. **Evaluation notice:** "Order subject to sample approval and pre-shipment inspection at AQL 0/2.5/4.0."

### 11.2 Purchase-order checklist

- [ ] Supplier legal name matches licence and bank account
- [ ] SKU, spec table, and *photographed sample reference* attached to PO ("as approved sample #S-042")
- [ ] Price, currency, Incoterm, port named
- [ ] Payment terms with inspection gate sequenced explicitly
- [ ] Lead time with penalty/remedy clause (e.g. 1%/week credit after grace week; capped)
- [ ] Spares-ratio line included (vehicles)
- [ ] Rejected-lot remedy: 100% rework + re-inspection at supplier cost
- [ ] Spares-tail clause: parts availability commitment (target 24 months post-discontinuation)
- [ ] Battery lines: UN38.3 + MSDS + DG shipping responsibility assigned
- [ ] Tooling/IP clauses if OEM content (Chapter 5.3)
- [ ] PO entered in RC WORLD OS with milestone dates before deposit released

### 11.3 Sample-evaluation form (summary)

Header (SKU, supplier, date, evaluator) then scored sections, 1–5 each: build quality on teardown (fastener quality, plastics, bearing feel); electronics inspection (ESC/servo/motor identity vs BOM, solder quality, connector spec); performance test (speed/function per class rubric, temperature after 10-minute duty cycle); durability proxy (drop/crash test per Volume 7 rubric, water/dust splash for outdoor classes); spares check (top-10 failure parts priced and sourced from 3 sellers); serviceability (time for an Artisan to reach motor, servo, arms). Verdict: Approve / Approve with conditions / Reject — two evaluator signatures (Procurement Lead + Head Artisan). Filed to the supplier record; referenced by every subsequent PO.

### 11.4 Landed-cost calculator layout

Columns per shipment line: FOB unit price × qty → FOB subtotal → +allocated freight (by volume share) → +insurance → CIF → +duty (rate by HS line) → +local tax (flag recoverable) → +fees allocated → +inspection allocated → **landed unit cost** → landed factor vs FOB. Maintained as an OS worksheet; every fleet asset's landed cost writes to `fleet_inventory` for Volume 10's cost-per-Shift model. Planning factors from Section 8.6 pre-fill until real quotes replace them.

### 11.5 Supplier onboarding checklist

- [ ] Directory entry created/updated (Chapter 3 format)
- [ ] Business licence + registry cross-check (Section 2.6) filed
- [ ] Video factory audit completed and scored (Chapter 4)
- [ ] Third-party verification or on-site audit for spend > $10k/yr
- [ ] Samples evaluated and approved (11.3)
- [ ] NNN signed if any OEM/IP exposure (5.4)
- [ ] Bank details verified by test payment + callback
- [ ] Dual-source identified for the category (DS rules, 1.3)
- [ ] Scorecard shell opened in RC WORLD OS; account contact named both sides
- [ ] First PO ≤ 30% of intended steady-state volume

---

## 12. Volume Summary & Cross-References

This volume converted the park's founding procurement thesis — direct-from-China wholesale as a structural moat — into an operating system: a doctrine (TCO per Shift, dual-sourcing rules DS-1–5, fleet standardization as leverage, a CNY-and-Canton-Fair-shaped calendar); a map of the four manufacturing clusters and a factory-vs-trader verification protocol; a directory of **76 profiled manufacturers and brands** across ten categories, each with location, tier, OEM level, MOQ class, lead time, and an RCW relevance rating, with unverifiable specifics honestly flagged for factory audit; and the machinery around it — a six-dimension weighted factory rating with an audit question bank, an OEM program that sequences cheap asks (colours, XT60) before expensive ones (ESC firmware, RCW Node pre-install) under NNN protection, MOQ/lead-time planning with worked buffer-stock math, a China-specific negotiation playbook, an import strategy dominated by the LiPo dangerous-goods constraint and a 1.20–1.30 sea landed-cost factor, AQL-based inspection with park-specific checklists, quarterly scorecards with failover triggers, and the five templates that make a two-person procurement function executable.

**Cross-references:**

- **Volume 2, Chapters 2 & 4** — the market context for the Chinese manufacturing ecosystem and the commissioned diorama-supplier study this volume's Section 3.11 interfaces with.
- **Volume 3 / 4 / 5 / 6** — the division fleet doctrines (platforms, classes, tuning parity, electromechanical-vs-hydraulic rule) that this volume's directory and OEM program serve.
- **Volume 7** — The Works: spares lists, failure data, induction build sheets, and the teardown rubrics used in sample evaluation; failure logs feed Chapter 6 buffer math and Chapter 10 scorecards.
- **Volume 9** — retail and sponsorship inventory (bodies, accessories, branded merchandise) sourced through Sections 3.10–3.11.
- **Volume 10** — landed costs, payment terms, duty verification, and insurance schedules; the financial source of truth this volume's planning factors roll into.
- **Volume 12** — franchise procurement: franchisees buy through the park's supplier agreements; this volume's directory and scorecards become licensed franchise assets.
- **Volume 13** — RC WORLD OS procurement, inventory, and fleet modules that operationalize the POs, scorecards, buffer-stock triggers, and asset registration described here; RCW Node BOM sourcing.




