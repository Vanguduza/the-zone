# Volume 9 — Customer Experience & Loyalty

| | |
|---|---|
| **Document** | RC WORLD — Master Development Plan, Volume 9 of 14 |
| **Title** | Customer Experience & Loyalty |
| **Revision** | 1.0 — July 2026 |
| **Status** | Living document — bump revision on material change |

**Purpose of this volume.** This volume is the design authority for everything a customer sees, feels, earns and keeps at RC WORLD. It defines the experience philosophy (immersion-as-product, friction-to-gameplay conversion), the end-to-end customer journey with owners and KPIs per touchpoint, and — as its core chapter — the complete **RC WORLD License** tiered progression system the founder's brief mandates: XP earning rules, six license tiers with numeric thresholds and equipment unlock gates, division endorsements, a catalogue of 60 named achievement badges with telemetry triggers, the Gears loyalty economy, leaderboards and season structure with a two-track Season Pass, the three canonical membership tiers, and the corporate, birthday, school and university product lines built on top of them. It closes with the customer-facing mobile app walkthrough and the service standards and recovery doctrine. Volumes 3–6 gate equipment and score events against the tiers defined here; Volume 13 builds the software that runs them. If a number in this volume and a division volume ever disagree, this volume is the source of truth for licenses, badges, Gears and memberships.

**Intended readers.** The General Manager and front-of-house team (all chapters); the marketing lead (Chapters 2, 5–9); the RC WORLD OS product team (Chapters 3–5, 10 — build detail in Volume 13); division leads whose equipment is license-gated (Chapter 3); the sales lead for corporate and education products (Chapters 7–9); investors assessing retention economics (Chapters 1, 3, 5, 6).

**Chapters**

1. Experience Philosophy
2. The Customer Journey
3. The RC WORLD License & Progression System
4. Achievement Badges
5. Gamification Mechanics
6. Memberships & Season Passes
7. Corporate Packages
8. Birthday Parties & Family Products
9. Schools, Universities & STEM
10. The Mobile App Experience
11. Service Standards & Recovery
12. Volume Summary & Cross-References

---

## 1. Experience Philosophy

### 1.1 Immersion is the product

RC WORLD does not sell radio-controlled vehicles by the minute. It sells the experience of *being someone* — a race driver on a timed grid, an excavator operator with a production quota, a harbour pilot with a barge to berth, a pilot on a buddy-box working toward solo wings. The vehicles are the instruments of that identity, and every design decision in this volume follows from one rule inherited from the original Omni-Zone blueprint: **the park is a miniaturized industrial complex, not a hobby sandbox.** A sandbox hands a customer a machine and leaves the meaning to them. An industrial complex hands them a *job* — with a shift clock, a work order, a score, a supervisor, and a career.

The industrial frame is not set dressing; it is the load-bearing structure of the commercial model:

- **The Shift** (the 20-minute billing block) reads as a work shift, not a rental countdown. Customers "clock in", they don't "start the timer". Operator Shifts include a pit-stop battery swap performed by an Artisan as refuelling theatre.
- **Staff titles carry the frame.** Technicians are **Artisans**; the induction is a **Toolbox Talk**; the progression program is a **License**, not a "loyalty scheme"; the loyalty currency is **Gears**, machined tokens of work done.
- **Scores are production numbers.** Lap times, career tonnage, mission completions and smoothness indices are the customer's professional record, displayed the way a real site displays safety days and output boards.
- **Progression is vocational.** You do not "level up" at RC WORLD; you get *licensed on equipment* — and the license genuinely unlocks machines the unlicensed cannot touch (Chapter 3).

> **Investor Note.** The industrial frame is retention economics wearing a costume. Industry analysts (2025–2026) consistently find that competitive-socializing venues (karting, TopGolf-class formats) out-earn passive attractions on repeat visitation because scoring converts visitors into competitors. RC WORLD's frame goes one step further: it converts competitors into *careerists*. A customer three badges short of their Operator license has an unfinished identity, and unfinished identities re-book. The 90-day second-visit KPI (operating target ≥22% Year 1, building to ≥28% by Year 3 — Volume 10 §10.4) is owned by this volume's mechanics.

### 1.2 The three audiences of every moment

Every experience moment is designed for three audiences at once, and is reviewed against all three before it ships:

1. **The operator** — the customer holding the transmitter. Their needs: clear controls, honest scoring, visible progress, no dead air.
2. **The spectator** — the family member, friend or passer-by watching. Their needs: legible drama (the hopper dump, the pit stop, the tow-truck rescue), comfortable sightlines, a reason to become an operator. Volume 2's competitive analysis is blunt: the non-driving half of every group is where F&B and conversion margin live.
3. **The camera** — the customer's phone. RC content is unusually algorithm-friendly (short, kinetic, legible without sound — Volume 2, Chapter 7), so every set piece is composed to be filmed: name-labelled leaderboard screens, overhead camera angles, automatic Shift highlight clips pushed to the customer's phone.

### 1.3 Friction-to-gameplay conversion

The doctrine that most distinguishes RC WORLD from every rental operation it was benchmarked against: **when an operational problem touches a customer, convert it into gameplay before you convert it into an apology.** Three canonical conversions, all inherited from the source blueprint and already engineered into Volumes 3–6:

| Friction point | Naive handling | RC WORLD conversion |
|---|---|---|
| Vehicle dies mid-Shift (flat pack, breakdown) | Staff walks onto track, customer waits, refund argument | **Tow-Truck Retrieval Protocol**: 85 dB localized buzzer marks the casualty; customer hands in their transmitter and receives a 1/10 winch-equipped recovery crawler; they pilot the rescue themselves, earn Gears for a clean tow, then continue on a fresh vehicle. Customers never walk onto live tracks — the safety rule *is* the game |
| Battery life shorter than session ambition | Mid-session battery anxiety, "it died early" complaints | **Industrial Shift pricing**: billing decoupled from battery life; the Casual Shift returns the vehicle with ~30% buffer; the Operator Shift's mandatory 20-minute pit stop is staged as F1 refuelling theatre with the Artisan on camera |
| Aggressive driving drains packs and breaks fleet | Speed governors, staff telling customers off | **F1-style power management**: telemetry reads voltage sag live; throttle abuse visibly burns the customer's energy allocation; smooth drivers post better scores. The scoreboard does the discipline (Chapter 5.3) |
| Queue at popular classes | Standing in line, walk-aways | **Live queue top-ups**: at T-5 minutes the app checks the class queue; if nobody waits, a one-tap "Top-Up Shift" wallet extension appears. Scarcity is honest, and empty capacity sells itself (Chapter 10.6) |
| Waiting for a booked slot | Dead time | Spectator missions in the app (predict the sprint-race podium for Gears), retail/F&B placement on the walking line, The Works viewing window |

The test for any new friction point discovered in operations: *can a customer be given agency inside the problem?* If yes, design the game before designing the compensation. Only when agency is impossible (weather closure, our fault entirely) does the recovery doctrine in Chapter 11 take over.

> **Field Note.** The Tow-Truck Retrieval Protocol polls as a highlight, not a failure. In pilot-format testing of comparable recovery gameplay, a majority of first-time customers who experienced a breakdown-plus-retrieval rated the visit *higher* than customers with no breakdown at all — the rescue is a story they tell. Do not "optimize away" breakdown theatre with over-cautious battery margins; the ~30% buffer doctrine already protects the fleet, and the retrieval fleet (4 recovery crawlers, park canon) exists to be used.

### 1.4 Progression must be earned, honest and legible

Three promises the progression system makes to customers, which every chapter of this volume must keep:

- **Earned:** license tiers cannot be bought. Memberships (Chapter 6) buy *access and value*, never tier. A Foreman-tier driver earned it on telemetry, and everyone on the leaderboard knows it.
- **Honest:** scores come from measured reality — the RCW Node's voltage and position stream, the MYLAPS timing loop, the hopper load cells (±20 g). Class-normalized leaderboards (Chapter 5.1) keep an entry-class child's pace index comparable with a touring racer's. The parity doctrine (lap-time parity within 2–3% per class, Volume 3) is what makes "the driver won, not the car" a true sentence.
- **Legible:** a customer can always answer "what do I do next?" in one glance at their license card: next tier, XP remaining, the specific badges or practical checks still open.

## 2. The Customer Journey

### 2.1 The journey spine

The journey is designed as a loop, not a line: every stage ends by loading the next stage, and the final stage (results, badges, re-booking) is deliberately the strongest. The spine below is the day-visitor version; Section 2.4 gives the member and party variants.

**Discovery → App download & Toolbox Talk → Arrival & wristband/QR → Vehicle binding → The Shift → Pit stop / battery-swap theatre → Results & badges → Retail & F&B → Re-booking.**

### 2.2 Journey moments table

Each touchpoint has a single accountable owner and one primary KPI reviewed monthly on the GM dashboard (KPI definitions and instrumentation: Volume 13).

| # | Moment | What happens | Owner | Primary KPI (target) |
|---|---|---|---|---|
| 1 | Discovery | Social clips, search, word of mouth; landing page sells the *job fantasy*, not the vehicles | Marketing lead | Cost per booked first visit (≤$9) |
| 2 | App download & account | Store listing → account → child profiles under guardian account | OS product team | Download→account conversion (≥70%) |
| 3 | **Toolbox Talk** induction | 8–12 min interactive module: battery limits, collision liability, track rules, tow-truck doctrine; doubles as signed digital waiver; per-division modules added later | Safety officer (content), OS team (build) | Completion rate pre-arrival (≥60%) |
| 4 | Booking & wallet | Pick division, class, Shift type, slot; wallet loaded; Learner license issued on first booking | Front-of-house lead | Pre-booked vs walk-up ratio (≥55% pre-booked) |
| 5 | Arrival & entry pavilion | QR at gate → NFC wristband issued (doubles as license card token); park map + today's events on lobby screens | Front-of-house lead | Gate-to-first-Shift time (≤12 min) |
| 6 | **Vehicle binding** | At the counter: QR scan on transmitter pairs customer → transmitter → asset tag in RC WORLD OS; transmitter profile auto-set to license tier; OS refuses pairings above the customer's tier | Duty marshal | Binding errors per 100 Shifts (≤1) |
| 7 | **The Shift** | 20-minute block; live dashboard on phone/track screens: battery %, time, position, score; marshals per zone SOPs | Division lead on duty | Shift utilization (≥65% of open slots) |
| 8 | Breakdown (if any) | Tow-Truck Retrieval Protocol (Chapter 1.3); fresh vehicle issued; Gears for clean tow | Duty marshal | Retrieval-to-resume time (≤6 min) |
| 9 | **Pit stop theatre** (Operator Shifts) | At minute 20, car called to pit; Artisan swap staged front-of-house: fresh pack, tire glance, "you're clear" send-off | Pit-lane Artisan | Swap time (≤90 s) |
| 10 | Results & badges | Session summary in-app within 60 s: laps/tonnage/mission score, smoothness index, XP, Gears, any badge pops (with sound, on the big screen if gold-class); highlight clip attached | OS product team | Summary open rate (≥80%) |
| 11 | Retail & F&B | Exit route passes retail counter and kiosk; badge pins, park merch, starter RC kits; Gears burnable here | Retail/F&B lead | Attach rate — % of visits with F&B or retail spend (≥45%) |
| 12 | **Re-booking hook** | Before the customer leaves Wi-Fi range: "next unlock" screen (XP to next tier, one suggested badge), one-tap re-book with off-peak discount | Marketing lead | 90-day second-visit rate (≥22% Y1 / ≥28% Y3, Volume 10 §10.4) |
| 13 | Post-visit | NPS ping at +24 h; highlight clip share prompts; win-back ladder if dormant (Chapter 6.5) | Marketing lead | NPS (≥55 Y1, ≥60 by Y3) |

### 2.3 Designing the two "wow" windows

Journey research across FEC formats (Volume 2) is consistent: visits are remembered by their peak moment and their ending. RC WORLD engineers both:

- **The peak** is division-specific and staged: the first hopper dump registering on the tonnage board (Construction), the first timed lap posting to a named leaderboard (Motorsport), the pit-stop swap (any Operator Shift), the tow-truck rescue (any breakdown). Marshals are trained to *announce* peaks ("new personal best on Track A — bay 4"), because a witnessed score is worth two private ones.
- **The ending** is the results-and-badges screen plus the physical exit line past retail. The rule: **no customer leaves without knowing their next unlock.** The app's closing screen is a career prompt, not a receipt.

### 2.4 Journey variants

| Stage | Day visitor | Member (any tier) | Birthday party | Corporate group |
|---|---|---|---|---|
| Induction | Toolbox Talk on first booking | Already inducted; delta modules only (new divisions) | Guardian completes for minors in invite flow | Bulk induction link pre-event; 5-min live briefing on site |
| Entry | QR → day wristband | Member wristband/card, dedicated lane at peak | Host meets group at pavilion | Event coordinator meets organizer |
| Booking | App or walk-up | Priority windows (7–14 days by tier), member hours | Fixed run-sheet (Chapter 8.3) | Fixed run-sheet (Chapter 7.2) |
| The Shift | Standard queue | Streak shields, block allowances (Chapter 6) | Party classes only (entry class, crawlers, tractors) | Format-specific fleets reserved |
| Results | XP/Gears/badges | + streak progress, season track levels | Paper license certificates + pin for each child | Team scoreboard, framed podium photo to organizer |
| Exit hook | Next-unlock + off-peak offer | Renewal health nudges (Chapter 6.5) | Party-guest voucher: first solo visit discount | B2B follow-up: league/venue offer within 48 h |

> **Field Note.** The single most operationally fragile moment in the spine is #6, vehicle binding — it happens at the counter, at peak, with a queue watching. Rehearse it like a pit stop: transmitter pre-staged by class, QR label on the transmitter *and* the car stand, and a fallback manual pairing code printed under the counter. If binding takes more than 40 seconds, the queue feels it; the ≤1-per-100 error KPI exists because every misbind is a wrong-profile safety event, not just a delay.

## 3. The RC WORLD License & Progression System

### 3.1 System architecture: one license, two axes, four endorsements

The RC WORLD License is the park's single progression spine. Everything a customer earns anywhere in the park — laps, tonnage, missions, flight-school stages, badges — feeds one career. The system has deliberately simple bones:

- **One park-wide License tier** (six tiers, Section 3.3) driven by **XP**, a skill-and-activity score. Tier is permanent: once earned, never lost. Tier gates equipment, transmitter power profiles, and league eligibility.
- **Two axes of progression.** *Performance* (XP → tier) and *frequency* (visit streaks → Gears multipliers and season-track boosts, Section 5.4). The axes never mix: streaks cannot unlock equipment, and skill cannot substitute for the loyalty economics of showing up. A brilliant driver who visits twice a year is a Foreman with no streak; a devoted weekly visitor of modest skill is an Apprentice with a 20-week flame. Both are valuable customers, and each axis pays the behaviour it measures.
- **Four division endorsements** (Section 3.5) — Motorsport, Construction, Aviation, Marine — which sit *on* the license like categories on a real driver's license and gate division-specific equipment. Endorsements let an aviation-only customer progress without ever touching a race car, while the park-wide tier still rewards breadth.

Terminology note: the membership products (Chapter 6) reuse the Apprentice/Operator/Foreman vocabulary deliberately — the brand speaks one industrial language — but membership is *purchased access* and license tier is *earned rank*. The app renders them in different visual systems (membership = card colour; license = embossed tier seal) and staff scripts never say "level" for either: you *hold* a membership and you *carry* a license.

### 3.2 The XP model

XP is earned from four sources, all machine-measured through RC WORLD OS (schema and event pipeline: Volume 13):

| Source | Base XP | Notes |
|---|---|---|
| Casual Shift completed (1 block) | 50 | Any division, any class |
| Operator Shift completed (2+ blocks) | 120 | Includes pit-stop; +30 per additional block beyond two |
| Premium-class Shift ($22/$38 classes) | +30 on top of base | Hydraulics, FPV, big crawlers, flagship vessels |
| **Smoothness bonus** | up to +50% of Shift base | Telemetry smoothness index ≥70 → +25%; ≥85 → +50% (Section 3.4) |
| Sprint race / mission / regatta finish | 40 | Every scored event finish, any placing |
| Podium: 3rd / 2nd / 1st | +40 / +60 / +100 | Class-normalized events only (Chapter 5.1) |
| League round completed | 60 | Plus podium bonuses; league season champion +500 |
| Skill task / practical check passed | 75–150 | Marshal-verified tasks from the endorsement syllabi (Section 3.5) |
| Badge earned | 50–500 | Per badge value in the catalogue (Chapter 4) |
| Clean tow (Tow-Truck Retrieval Protocol) | 40 | Winch hook, recovery, no geofence breach |
| Toolbox Talk module (each) | 25 | Core + one per division + premium-equipment modules |

Design rules that keep XP honest:

- **XP is never sold, gifted or multiplied by spend.** Gears (Chapter 5.4) carry all monetary generosity; XP carries only demonstrated activity and skill. This is the wall that keeps the license credible.
- **Daily earn softcap of 600 XP** (excess earns at 25%) — protects the ladder from binge-grinding and keeps tier ages meaningful.
- **Anti-gaming:** Shifts abandoned before 10 minutes earn no XP; smoothness bonuses require ≥60% of the Shift under throttle; repeated same-badge attempts are unlimited but the XP pays once.

### 3.3 The six License tiers

| # | Tier | XP threshold | Additional gates (all required) | Expected profile |
|---|---|---|---|---|
| L1 | **Learner** | 0 | Core Toolbox Talk complete (includes waiver) | Every customer on first booking |
| L2 | **Apprentice** | 500 | One clean full Shift (no kill-switch event, no geofence breach); 1 badge | Typically visit 2–3 |
| L3 | **Operator** | 2,000 | Smoothness average ≥70 over last 10 Shifts; 5 badges; 1 division endorsement at Basic | The committed regular; visit 6–10 |
| L4 | **Foreman** | 6,000 | 12 badges incl. 1 Gold-class; 1 endorsement at Advanced; 1 scored event finish | Top ~15% of active customers |
| L5 | **Site Manager** | 15,000 | 25 badges; 3 endorsements at Basic+ (breadth gate); marshal-shadow session completed | Top ~3%; the community's senior figures |
| L6 | **Legend** | 40,000 | Site Manager for ≥1 full season; 1 championship podium *or* 40 badges incl. 3 Gold; ratified by GM each season | Deliberately rare; the park's hall of fame |

Tier ceremonies are staged: Apprentice through Foreman pop in-app with a leaderboard-screen announcement if the customer is on site; Site Manager and Legend are awarded at the monthly Community Night with a physical metal license card (Legend cards are individually numbered). Legends get their name on the entry-pavilion Legends board — permanent, like a topping-out plaque.

### 3.4 The smoothness index — F1-style power management as a skill score

The smoothness index is the park's signature telemetry statistic, computed per Shift by the RCW Node stream: a 0–100 score derived from voltage-sag variance (aggressive throttle spikes sag the pack; smooth loading doesn't), throttle-input smoothness, geofence discipline, and — on construction machines — boom/load shock events. It is the same doctrine that runs the F1-style energy-management races (Chapter 5.3): **the pack is your fuel; brutality is visible; smooth is fast.** The index appears live on the Shift dashboard as an analogue "operator gauge", so a customer can watch their own inputs move it. It gates the Operator tier (average ≥70) because smooth driving is precisely the skill that protects the fleet — the license system pays customers to behave like professionals, which is cheaper than repairing the alternative (fleet-damage economics: Volume 7).

### 3.5 Division endorsements

Each endorsement has three grades — **Basic → Advanced → Master** — earned through the division's own syllabus of skill tasks and badges. Existing division ladders map onto the grades as follows (this volume ratifies and, where needed, supersedes earlier drafting):

| Division | Basic | Advanced | Master | Syllabus anchor |
|---|---|---|---|---|
| Motorsport | Track-craft check: 10 clean laps, pit-lane entry, flag signals | Sub-110% of class reference lap; race-start procedure; 1 sprint podium | Sub-105% reference lap; league season completed; drift or formula check | Volume 3, Ch. 13 |
| Construction | Load-cycle check: 10 weighed loads, no spillage penalty; haul-road rules | 1 t career tonnage; loader check; Precision event finish | 5 t tonnage; hydraulic orientation; Team Campaign season | Volume 4, Ch. 8–9 |
| Aviation | = **Ground Wings + Bronze Wings** (ground school, buddy-box, solo checkride) | = **Silver Wings** (solo currency, aerobatics sign-off) | = **Gold Wings + one type rating** (Type: Jet / Type: FPV / Type: Heli) | Volume 5, §9.3 |
| Marine | = **Deckhand + Coxswain** (clean harbour Shift; precision docking, barge push) | = **Tug Master** *or* **Race Skipper** (two-tug assist / speed-pond license) | = **Sail Grade 3** *or* **Submariner** (B-rig weather sailing / precision hover) | Volume 6, Ch. 8 §8.4 |

### 3.6 Equipment unlock gates

The unlock table below is the canonical park-wide gate list. Division volumes referenced "the second license tier" and "tier 3" during drafting; **this table supersedes those phrasings** — gates are now expressed as named tiers plus endorsement grades.

| Equipment class | Price band | Minimum license tier | Endorsement grade | Supervision |
|---|---|---|---|---|
| Entry classes: 1/14 racing, dump trucks, tractors, entry crawlers, DF65 discover sail, buddy-box trainers | $15 | Learner | — | Standard marshal cover |
| Standard classes: 1/10 touring, buggy/rally, excavators, harbour tugs | $15 | Apprentice | Division Basic | Standard |
| Drift, short-course, wheel loader, dozer, fast-electric boats | $15 | Apprentice | Division Basic | Standard |
| Premium crawlers (TRX-4 class), premium tractors + implement library | $22 | Operator | Division Basic | Standard |
| **Premium hydraulics** (Kabolite K961/K963 class supervised Shifts) | $22/$38 | Operator | Construction Advanced | One-on-one Artisan |
| **FPV** (drone racing, FPV crawler cams) | $22 | Operator | Aviation **Type: FPV** rating (Ground Wings prerequisite — Volume 5 §9.3) | Spotter required |
| Flagship hydraulic showcase (K970-class seat time) | event-priced | Foreman | Construction Master | One-on-one Artisan, listed slots |
| Formula RC / drag events; **jet-class and scale-heli aircraft** (Phase 2+) | event-priced | Foreman | Division Master | Event marshals / instructor |
| Recovery crawlers (outside a retrieval event, i.e. recreational towing Shifts) | $15 | Apprentice | — | Standard |

Transmitter power profiles bind to tier automatically at vehicle pairing (the OS refuses over-tier pairings — Volume 3, Section 12.1): **Learner/Apprentice → Rookie profile** (steering 75%, throttle 60%, softened expo), **Operator → Standard profile** (90/80), **Foreman and above → Licensed profile** (100/100 within class caps). The tier is therefore not symbolic: a Foreman's identical car is measurably faster in their hands because the electronics trust them more.

### 3.7 Tier privileges and discounts

| Privilege | Learner | Apprentice | Operator | Foreman | Site Manager | Legend |
|---|---|---|---|---|---|---|
| Gears earn multiplier (license axis) | ×1.0 | ×1.0 | ×1.1 | ×1.2 | ×1.3 | ×1.5 |
| Off-peak Shift discount | — | — | 5% | 10% | 10% | 15% |
| Priority booking window | 3 days | 3 days | 5 days | 7 days | 10 days | 10 days |
| League eligibility | — | Open evenings | Division League | Division League | Championship invitational | Championship invitational |
| Transmitter profile | Rookie | Rookie | Standard | Licensed | Licensed | Licensed |
| The Works bench access (supervised hour) | — | — | — | 1/quarter | 1/month | 1/month |
| Guest privilege | — | — | — | bring-a-Learner: guest's first Shift 50% off | + guest skips Toolbox Talk queue (staff-assisted) | + 2 comp guest Shifts/season |
| Physical card | app only | app only | printed card | printed card | metal card | numbered metal card |

License-axis multipliers and discounts stack with membership benefits (Chapter 6) multiplicatively for Gears and additively-capped for discounts (maximum combined Shift discount 25% — protects Shift yield, per Volume 10 pricing guardrails).

> **Trade Hack.** Print the practical-check criteria on the back of every paper license certificate. Customers photograph the card, and the photo *is* the marketing: it tells their group exactly what to come back and attempt. The cheapest acquisition channel the park owns is a twelve-year-old showing their Apprentice card to a sibling.

### 3.8 Progression pacing model

The ladder is tuned so that meaningful state change happens on almost every visit. A typical enthusiastic customer (one Operator Shift + one event per visit, decent smoothness) earns 250–350 XP per visit: Apprentice on visit 2, Operator around visits 6–8, Foreman inside the first year at 20–25 visits. That pacing is deliberate against the membership price ladder — the Apprentice→Operator XP window is where the $29 membership pays for itself in included Shifts, and the Operator→Foreman grind is where league nights and the $59 membership become rational. Pacing is reviewed each season against the funnel KPIs (Section 5.6); thresholds may be re-tuned ±20% by the GM with a revision note here, never mid-season.

## 4. Achievement Badges

### 4.1 Badge system design

Badges are the granular texture of progression: the license answers "what rank am I", badges answer "what have I *done*". System rules:

- **Three classes:** Bronze (achievable in a visit or two), Silver (deliberate practice over multiple visits), Gold (genuine accomplishment; ≤10% of active customers should hold any given Gold). Class sets the XP value: Bronze 50, Silver 150, Gold 400 (event and secret badges vary, per catalogue).
- **Machine-verified wherever possible.** Every badge lists its trigger. `T:` marks a fully automatic telemetry/OS trigger; `M:` marks a marshal or Artisan verification tap on the staff app (two-tap: staff ID + customer wristband). Automatic triggers are the default; marshal triggers are reserved for judgment calls (form, technique, conduct).
- **Badge pops are theatre.** In-app animation with sound; Silver and Gold pops also flash the customer's name on the nearest leaderboard screen; Gold pops are announced by the duty marshal.
- **Five divisions of the catalogue:** Skill Mastery, Equipment Mastery, Milestones, Event badges, Secret badges.

### 4.2 The badge catalogue

**Skill Mastery** — cross-cutting craft, mostly telemetry-triggered:

| # | Badge | Class | Criteria & trigger |
|---|---|---|---|
| S01 | **Drift Initiate** | Bronze | Hold a scored drift line through the annex's 3-gate sector once. T: gyro/Node trace + timing gates |
| S02 | **Drift Sensei** | Gold | Judge-scored drift run ≥80/100 at a drift night. M: judge panel entry |
| S03 | **Smooth Operator** | Silver | Smoothness index ≥85 on 5 consecutive Shifts. T: index history |
| S04 | **Feather Foot** | Bronze | Complete a full Shift with zero voltage-sag spikes above threshold. T: Node sag analysis |
| S05 | **The Surgeon's Hands** | Silver | Construction precision course (Volume 4, Ch. 8.2) clear with zero penalty touches. T: course sensors + marshal confirm |
| S06 | **Hydraulic Surgeon** | Gold | Premium hydraulic precision task (egg-lift protocol on K961-class) completed intact. M: supervising Artisan |
| S07 | **Line Perfect** | Silver | 10 consecutive laps within 102% of your own best. T: timing loop |
| S08 | **Night Flier** | Silver | 3 night-session flights (or night FPV heats) completed clean. T: session timestamps + clean-flight flag |
| S09 | **Crosswind Landing** | Silver | Landing check passed in measured crosswind ≥3 m/s. M: instructor |
| S10 | **Winchmaster** | Silver | 10 clean tows under the Tow-Truck Retrieval Protocol. T: retrieval log |
| S11 | **First Responder** | Bronze | First clean tow. T: retrieval log |
| S12 | **Harbour Pilot** | Silver | Berth a loaded barge inside the marked box, no wall contact. T: mission console |
| S13 | **Deadstick** | Gold | Sailing: win a regatta race; or Aviation: power-off landing check. M: race officer / instructor |
| S14 | **Load Whisperer** | Bronze | 10 weighed hopper loads in one Shift, zero spillage penalty. T: load cells |
| S15 | **The Long Haul** | Silver | 100 kg weighed tonnage in a single day. T: tonnage ledger |

**Equipment Mastery** — one per machine class; earned by a clean qualifying Shift *plus* the class practical check:

| # | Badge | Class | Machine class & trigger |
|---|---|---|---|
| E01 | **Touring Card** | Bronze | 1/10 touring: 10-lap clean check. T+M |
| E02 | **Buggy Broken-In** | Bronze | 1/14 buggy: Track B lap check incl. both jumps landed. T+M |
| E03 | **Short-Course Certified** | Bronze | SCT class check. T+M |
| E04 | **Formula Steward** | Gold | Formula RC event participation + staged-launch drag pass. M: event marshal |
| E05 | **Dig Card** | Bronze | Excavator: load-cycle check (Section 3.5). T+M |
| E06 | **Truck Card** | Bronze | Dump truck: 10 hauls, haul-road rules clean. T |
| E07 | **Loader License** | Silver | Wheel loader check (the strongest rental machine — gated per Volume 4). M |
| E08 | **Dozer Operator** | Silver | Dozer grading task to marshal standard. M |
| E09 | **Iron Rancher** | Bronze | Tractor + one implement hitched, field task complete. T+M |
| E10 | **Implement Master** | Silver | All four implement types used across any number of Shifts. T: implement RFID |
| E11 | **Crawler Scout** | Bronze | Entry crawler: Trail C bridge section clean. T: geofence |
| E12 | **Summit Club** | Silver | Premium crawler: full Trail C including water hazard, no tow. T |
| E13 | **Tug Ticket** | Bronze | Harbour tug basics check. M |
| E14 | **Sail Trim** | Bronze | = Marine *Sail Grade 1* task (Volume 6 §8.4). M |
| E15 | **Submarine Qualified** | Silver | Sub Hunt mission scored ≥50%. T: mission console |
| E16 | **Wings** | Silver | = *Bronze Wings* solo checkride (Volume 5 §9.3–9.4). M: instructor |
| E17 | **FPV Cleared** | Silver | FPV module + first clean FPV heat. T+M |
| E18 | **Heavy Ticket** | Gold | Premium hydraulic orientation + supervised Shift complete (Kabolite class). M: Artisan |

**Milestones** — pure accumulation, all automatic:

| # | Badge | Class | Criteria (T: OS ledgers) |
|---|---|---|---|
| M01 | **Clock-In** | Bronze | First completed Shift |
| M02 | **Ten Shifts Deep** | Bronze | 10 career Shifts |
| M03 | **Centurion** | Silver | 100 career Shifts |
| M04 | **Five-Hundred Club** | Gold | 500 career Shifts |
| M05 | **First Tonne** | Bronze | 1 t career tonnage (nameplate unlock, per Volume 4) |
| M06 | **Five Tonnes** | Silver | 5 t career tonnage |
| M07 | **Quarry King** | Gold | 25 t career tonnage |
| M08 | **Lap 1,000** | Silver | 1,000 career timed laps |
| M09 | **Four Corners** | Silver | At least one Shift in all four divisions (Phase 2+; Phase 1 variant: all three Phase 1 zones) |
| M10 | **Anniversary Wrench** | Bronze | Active in the park 12 months after first Shift |
| M11 | **Streak 5 / 10 / 25** | Bronze/Silver/Gold | Visit streak milestones (Section 5.5) |
| M12 | **Gears Millionaire** | Silver | 100,000 lifetime Gears earned (earned, not held) |

**Event badges** — issued only during the named window; permanent proof of having been there:

| # | Badge | Class | Criteria |
|---|---|---|---|
| V01 | **Harvest Hand** (seasonal) | Bronze | Any scored delivery during a Harvest Campaign fortnight (Volume 4) |
| V02 | **Harvest Champion** (seasonal) | Gold | Age-class campaign winner |
| V03 | **Season One Veteran** (etc. per season) | Bronze | 10+ Shifts inside the named season |
| V04 | **Championship Weekend** | Silver | Competed at the annual RC WORLD Championship |
| V05 | **Podium** | Gold | Any championship-event podium |
| V06 | **Opening Day** | Bronze | On site during park opening weekend — never reissued |
| V07 | **Night League Regular** | Silver | 5 night-league rounds in one season |
| V08 | **Treasure Week** | Bronze | Found a Sub Hunt treasure puck during Treasure Week (Volume 6) |

**Secret badges** — undocumented in the app until earned (the catalogue below is staff-confidential; customers discover them):

| # | Badge | Class | Criteria & trigger |
|---|---|---|---|
| X01 | **Good Samaritan** | Silver | Tow another customer's casualty when the protocol offers it to the queue. T: retrieval log |
| X02 | **The Closer** | Bronze | Book the last Shift of the day and complete it. T |
| X03 | **Rain Operator** | Silver | Complete a Shift in officially logged rain (open divisions only). T: weather flag |
| X04 | **Photo Finish** | Silver | Win a sprint race by <0.1 s. T: timing loop |
| X05 | **Zero to Hero** | Gold | Win a class-normalized event within 30 days of holding the Learner tier. T |
| X06 | **The Understudy** | Bronze | Watch a full Works window rebuild (dwell ≥15 min at the viewing window during a live teardown). M: Artisan wave-in |
| X07 | **Full House** | Gold | Hold every Bronze equipment badge in the catalogue. T |

Catalogue total at launch: **60 badges** (15 skill, 18 equipment, 12 milestone incl. the three-stage streak badge, 8 event, 7 secret — event badges rotate). The catalogue is a living annex: divisions propose additions each season; the GM ratifies; retired badges remain on customer records forever.

### 4.3 Physical collectibles

Every Bronze badge has a **35 mm enamel pin** ($4.50 retail, or 900 Gears); Silver and Gold pins are earn-only — they cannot be bought, only claimed at the retail counter after the digital badge is verified on the wristband (first Silver/Gold pin free, replacements $6). Kids' party packages include a **starter badge board** (A5 printed card with 12 pin slots matching the entry-class badges). The pin wall behind the retail counter displays the full catalogue with "earned by N drivers" counters under each — a physical progression advertisement positioned exactly where every customer exits.

> **Field Note.** Enforce the earn-only rule for Silver/Gold pins ruthlessly, including for staff and VIPs. The moment one unearned Gold pin is seen on a lanyard, the entire physical program deflates to merchandise. The Bronze tier being purchasable is deliberate — it seeds collecting behaviour in children — but the wall between bought and earned is the program.

## 5. Gamification Mechanics

### 5.1 Leaderboards and class normalization

Every scored surface in the park posts to the leaderboard framework (one framework, many boards — Volume 13):

- **Boards:** per-track lap boards (A/B/C), tonnage boards (daily/seasonal/all-time, per Volume 4), mission boards (harbour, Sub Hunt), event boards, and the park-wide **Season Board** (Section 5.5).
- **Windows:** today / this week / this season / all-time. Weekly boards reset Monday 06:00 local; the reset is the retention heartbeat — a fresh board is a winnable board.
- **Class normalization.** Raw lap times only compare within a class. Cross-class boards use the **Pace Index**: the customer's best lap divided by the class *reference lap* (the calibrated Artisan-driven benchmark maintained by the weekly parity audit, Volume 3, Chapter 4), expressed as a percentage. A 108% pace index in the 1/14 entry class and a 108% in 1/10 touring rank identically — an eight-year-old and a club racer can share a board honestly. Construction normalizes by machine class against reference cycle rates; marine missions are scored 0–100 natively.
- **Identity:** boards display the customer's handle, license-tier seal and division endorsement chips. Real names only with explicit opt-in; child accounts display handle + first name initial (Chapter 11.6).

### 5.2 Fair-play surface

All boards apply the same three filters: (1) telemetry-verified sessions only (no manual score entry except marshal-judged formats); (2) kill-switch or geofence-breach events void the affected lap/cycle; (3) statistical outlier review — any score >3σ better than the customer's rolling baseline is flagged for marshal review before posting (protects against timing-loop glitches and cut lines). The appeal path is Chapter 11's service desk, answered within 24 hours.

### 5.3 The Energy Cup — F1-style race scoring

The park's signature race format, run weekly per track, converts the power-management doctrine into sport:

1. Each car starts the heat with a fixed **energy allocation** (a Node-computed budget derived from pack state — not raw voltage, so pack age doesn't bias grids).
2. Telemetry deducts from the allocation in real time as a function of throttle demand and voltage sag: aggressive driving *visibly* burns budget on the customer's live gauge and the track screen.
3. Exhausting the allocation before the flag triggers a soft limit (throttle capped to 40% — the "limp home" penalty), not a kill; strategic drivers manage to the flag like an F1 fuel-saving stint.
4. Scoring: race position points (10/8/6/5/4/3/2/1) **plus** an efficiency bonus (energy remaining × position multiplier) — the winning play is fast *and* smooth, never one alone.

The Energy Cup is the format most cited in staff scripts when explaining "why smooth matters", and it is the qualifying surface for the seasonal championship. It runs identically in a construction variant (the Load-and-Haul enduro: tonnage per energy budget).

### 5.4 Gears — the loyalty currency

Gears are the monetary axis of the reward system: earned generously, burned on real value, and kept strictly separate from XP (Gears never advance the license). Ledger, wallet and expiry mechanics: Volume 13. Economics guardrail (with Volume 10): **1 Gear ≈ $0.005 redemption value; target overall redemption cost ≤4% of gross customer revenue.**

**Earn table:**

| Action | Gears |
|---|---|
| Per $1 spent (Shifts, F&B, retail, parties, events) | 10 |
| Completed Shift bonus | 25 |
| Clean tow (retrieval protocol) | 50 |
| Sprint race / mission / regatta entry | 25 |
| Event podium | 100 |
| Badge earned (Bronze/Silver/Gold) | 50 / 150 / 400 |
| License tier-up | 500 |
| Referral: referred friend completes first paid Shift | 500 |
| NPS survey completed | 25 |
| Birthday month bonus (once) | 250 |
| Visit-streak multiplier | ×1.1 at 3-visit streak, ×1.25 at 6, ×1.5 at 10+ (applies to earn, Section 5.5) |
| License-tier multiplier | ×1.0 → ×1.5 per Section 3.7 |
| Membership multiplier | ×1.1 / ×1.2 / ×1.3 (Apprentice/Operator/Foreman, Chapter 6) |

**Burn table:**

| Redemption | Gears |
|---|---|
| Casual Shift, standard class ($15) | 3,000 |
| Casual Shift, premium class ($22) | 4,400 |
| Shift top-up block (when the queue-top-up offer appears) | 2,500 |
| F&B kiosk item (up to $5) | 1,000 |
| Bronze badge pin | 900 |
| Park cap / small merch (up to $12) | 2,400 |
| Party upsell: extra child slot | 5,000 |
| Coaching session discount ($10 off) | 2,000 |
| Season Pass paid track (Section 5.5) — partial payment allowed | up to 50% of price |
| Charity option: donate to the schools-program bursary fund | any amount |

Gears expire 12 months after earning (rolling, FIFO), paused for any month with a visit. Expiry warnings at 60/14 days are retention touches, not threats — each includes a one-tap off-peak booking suggestion sized to the expiring balance.

### 5.5 Streaks and the season structure

- **Visit streaks** count consecutive calendar *months* with ≥1 completed Shift (a monthly cadence is honest for a destination venue; weekly streaks would punish normal families). Streak rewards are the Gears multipliers above, the M11 streak badges, and a **streak shield**: one missed month per 6-month streak is auto-forgiven. Members' streaks are shielded for the life of the membership.
- **Seasons** run 13 weeks, four per year, each with a name and a light theme (e.g. "Season 3: Night Works" carries the night-league push). At season end: seasonal boards archive to the customer's career page, the Season Board crowns per-division and overall champions at Community Night, and the Season Pass track resets. License tier and badges never reset — seasons reset *competitions*, not *careers*.
- **The Season Pass** is a battle-pass-style reward track fed by **Track Points** (1 TP per 10 XP earned that season — so the pass rides on the same honest activity measure, and nothing on it requires new grinding surfaces). Thirty levels; rewards alternate between the free and paid tracks:

| Track | Price | Sample reward ladder (30 levels) |
|---|---|---|
| **Free track** | $0, everyone enrolled | L2: 250 Gears · L5: seasonal badge V03 progress · L8: F&B voucher · L12: 500 Gears · L18: Bronze pin voucher · L24: off-peak Shift 50% voucher · L30: seasonal trophy (digital) + 1,000 Gears |
| **Paid track: Season Pass** | $24/season (or 12,000 Gears; included free in Operator & Foreman memberships) | Everything on free track, plus — L1: exclusive seasonal body-shell livery on rental cars bound to your Shifts · L6: 1 free standard Shift · L10: seasonal cap · L15: priority-queue token ×2 · L20: 1 premium Shift · L25: exclusive seasonal pin (never re-issued) · L30: guaranteed championship-weekend grid slot + name on the season plaque |

A committed customer completing ~2 visits/month with events finishes the free track comfortably and the paid track with headroom; the paid track is priced under two Casual Shifts and returns more than that in vouchers by design — it is a retention product, not a margin product (yield modelling: Volume 10).

### 5.6 Mechanics dashboard

The GM reviews one funnel monthly: actives → % with a streak ≥3 → % Apprentice+ → % Operator+ → % on paid Season Pass → 90-day repeat rate. Targets by end of Year 1: 40% streak≥3, 55% Apprentice+, 18% Operator+, 12% paid pass, 22% repeat (rising to 28% by Year 3 per Volume 10 §10.4). Any mechanic that doesn't move this funnel within two seasons is retired — gamification is subject to the same utilization discipline as the fleet.

> **Field Note.** Resist the temptation to add currencies. Every gamified venue that decays into a "points, stars, tickets, crowns and crystals" bazaar trains customers to value nothing. RC WORLD runs exactly three numbers — XP (career), Gears (wallet), Track Points (season) — each derived from real behaviour, each spent on a different axis, and the third derived from the first. That is the entire economy. Hold the line.

## 6. Memberships & Season Passes

### 6.1 The three canonical tiers

Memberships convert enthusiasm into predictable monthly revenue and are the park's single most important financial smoothing instrument (deferred-revenue and churn modelling: Volume 10). Canonical pricing per the style guide; monthly, cancel any time, with a 12-month prepay option at two months free.

| | **Apprentice — $29/mo** | **Operator — $59/mo** | **Foreman — $99/mo** |
|---|---|---|---|
| Included Shifts / month | 3 Casual (standard classes) | 6 Casual *or* 3 Operator equivalents (block-based: 6 blocks) | 12 blocks, any mix; premium classes count 1.5 blocks |
| Additional Shifts | 10% off | 15% off | 20% off |
| Gears earn multiplier | ×1.1 | ×1.2 | ×1.3 |
| Booking window | 7 days | 10 days | 14 days |
| Member hours (Tue/Thu 17:00–19:00, Sun 08:00–10:00) | ✓ | ✓ | ✓ + guaranteed slot with 48 h notice |
| Season Pass paid track | — | included | included |
| League entry | standard fees | 1 division league/season included | all division leagues + championship qualifier entry |
| Guest passes | — | 1 guest Casual Shift / month | 3 guest Casual Shifts / month |
| The Works | — | member workshop evening 1/quarter | monthly bench hour with an Artisan |
| Streak shield | ✓ (full) | ✓ (full) | ✓ (full) |
| Birthday-party discount | 5% | 10% | 15% + priority dates |
| Retail & F&B | 5% off | 10% off | 10% off + members' merch drops |

Blocks unused in a month roll over one month, then lapse (prevents hoarded liability while forgiving a busy month). Included Shifts earn XP and Gears normally — a member's activity is real activity.

### 6.2 Fair-use rules

- Included blocks are personal and non-transferable (guest passes are the sharing mechanism); wristband identity is checked at binding.
- Peak-day cap: maximum 2 included blocks redeemed on any Saturday/public holiday (paid Shifts uncapped) — protects walk-up capacity on the days that recruit new customers.
- Premium hydraulic and Foreman-gated equipment remain license-gated regardless of membership (the earned/bought wall, Section 3.1).
- Membership pauses: up to 2 months/year self-service in the app (streak shield holds); medical/relocation pauses by service desk without limit.

### 6.3 The Annual Season Pass product

Distinct from the quarterly Season Pass reward track (Section 5.5), the **RC WORLD Annual Pass — $499/year** (family add-on: +$299 per additional household driver) is the day-visitor's unlimited-ish product: 1 Casual Shift per visit day, any standard class, unlimited visit days, 10% F&B/retail discount, and all four quarterly paid Season Pass tracks included. It deliberately does *not* include Operator Shifts, premium classes or leagues — heavy users are worth more as Operator/Foreman members, and the pass's job is frequency for the family segment, not value transfer to enthusiasts. Break-even against door prices sits near 34 visit days; modelled utilization is far lower, and the pass's real payload is the F&B/retail attach of frequent family visits (Volume 10).

### 6.4 Sales choreography

Membership is sold at three journey moments and nowhere else pushily: (1) the results screen when the app can show "this month would have cost $X less as an Apprentice member" from real history; (2) the front desk at a customer's third visit in a rolling 60 days (the OS flags it discreetly on the staff app); (3) the league sign-up flow, where Operator membership bundles the entry. Staff earn a small spiff on activations that survive 90 days — never on day-one signups alone, which buys churn.

### 6.5 Churn management and win-back

Churn is managed as a pipeline with named states, automated in RC WORLD OS (CRM detail: Volume 13):

| State | Definition | Automated action | Human action |
|---|---|---|---|
| Healthy | ≥2 block redemptions/month | none | none |
| Cooling | 1 redemption, or booking-window use stops | "your blocks roll over" nudge + one-tap booking | none |
| At-risk | 0 redemptions in a month | pause offer (before they cancel themselves), off-peak suggestion sized to their history | Foreman tier: personal note from a named Artisan or league marshal |
| Cancelled | churned | exit micro-survey (one question); Gears and license status confirmation ("your career is safe") | logged reason code |
| Win-back 30/90/180 | 30/90/180 days post-cancel | 30 d: first month back 50% · 90 d: free Casual Shift + season preview · 180 d: "your streak shield is waiting" + event invite | 90 d cohort reviewed monthly by GM |

Two doctrines: **pause beats cancel** (a paused member keeps identity, streak and habit), and **the career never lapses** — license tier, badges and XP are explicitly permanent, so every win-back message can truthfully say the customer is returning to a career in progress, not starting over. Target Year-1 monthly churn ≤4.5% blended; win-back reactivation ≥12% of the 90-day cohort.

> **Investor Note.** At the Year-1 modelled mix (Volume 10) memberships contribute roughly 20–25% of revenue at materially higher margin than walk-up Shifts (no acquisition cost, off-peak-skewed usage, F&B attach). Every mechanic in Chapters 3–5 ultimately serves this line: the license creates the identity, the identity justifies the subscription.

## 7. Corporate Packages

### 7.1 Product logic

Corporate events monetize weekday daytime capacity that walk-up demand never fills, at pricing anchored from **$1,400 (2 hours, 20 pax)**. The park's pitch against karting, escape rooms and axe venues: RC WORLD formats are *genuinely collaborative* (a supply chain needs five people doing five jobs), skill floors are low (everyone can drive a dump truck in two minutes), and the telemetry produces objective team scoreboards HR can't get elsewhere. Sales collateral leads with the format, not the facility.

### 7.2 The three flagship formats

**Site Foreman Challenge** (Construction, 2–3 h, 12–40 pax) — the signature product. Teams of 4–5 run a scored construction campaign: excavator, three dump trucks (the 1:3 doctrine becomes a teamwork lesson — the excavator is idle without its trucks), and a loader keeping the haul road clean. Weighed tonnage per energy budget scores the board; a mid-session "site incident" (staged breakdown → team must execute a Tow-Truck Retrieval while production continues) tests role reallocation. Debrief includes each team's smoothness and coordination telemetry — the closest thing to an objective teamwork metric on the corporate market.

**Relay Grand Prix** (Motorsport, 2 h, 10–30 pax) — teams share one car per team in a driver-change relay on Track A; Energy Cup scoring makes pace *and* energy strategy a team decision; pit-stop battery swaps are performed with Artisan supervision as the relay's exchange ritual. Class-normalized handicapping lets mixed-ability groups compete honestly.

**Engineering Challenge** (The Works + track, 3 h, 8–20 pax, premium) — teams receive identical baseline cars and a constrained tuning menu (gearing, springs, ballast, ESC profile per Volume 3's parity toolkit), guided by an Artisan; a workshop tour covers the RCW Node and fleet doctrine; the afternoon ends in a time-trial shootout where the tuning choices are the differentiator. Sold to engineering firms, universities and technical teams; the strongest recruiting-event format in the portfolio.

### 7.3 Corporate pricing

| Package | Duration | Pax | Price | Includes |
|---|---|---|---|---|
| Toolbox (base) | 2 h | up to 20 | $1,400 | 1 format, event host, team scoreboard, photo pack |
| Site Works | 3 h | up to 40 | $2,600 | 2 formats or extended campaign, catering slot (F&B billed separately), branded leaderboard |
| Full Site Takeover | 4 h + exclusive zone | up to 80 | from $4,800 | Zone exclusivity, 2–3 formats, event coordinator, framed podium photos, custom event badge |
| Add-ons | — | — | Engineering Challenge +$40/pax · evening/night session +15% · catering per Volume 10 F&B menu · branded body shells $18/car | |

Deposits 50% at booking; weekday-daytime slots discounted 10% (they are the inventory this product exists to fill). Every attendee leaves with a Learner license already provisioned and a personal "come back" voucher — corporate events are also a customer-acquisition channel with negative CAC.

### 7.4 Sales pipeline and B2B calendar

Pipeline stages in the OS CRM: Lead → Qualified (date + budget) → Proposal → Confirmed (deposit) → Delivered → Rebook-ask (within 48 h of delivery, with the event's scoreboard attached). One part-time B2B coordinator owns the pipeline from Month 4; targets ramp to 6 events/month by Month 12 and 12/month in Year 3 (Volume 10). The B2B calendar follows corporate budget rhythm: January–February (kick-offs, sales-team energizers), June–July (mid-year offsites), September (team rebuilds), November–early December (year-end parties — premium pricing, book by September). Standing partnerships: hotel concierge desks, DMC/event agencies (10% commission), and co-working/tech-park community managers (hosted taster evenings each quarter).

## 8. Birthday Parties & Family Products

### 8.1 Package ladder

Parties are the park's highest-margin repeatable product and its most efficient child-acquisition channel: every party imports 8–15 prospective license-holders with a parent watching. Canonical anchor **from $349 (10 children)**.

| Package | Price | Children | Includes |
|---|---|---|---|
| **Crew Party** | $349 | up to 10 (each extra $28) | 90 min: 2 entry-class Shifts each (entry racing + trucks/tractors rotation), party room 45 min, dedicated host, paper license certificates + Bronze pin each, badge board for the birthday child |
| **Foreman's Party** | $499 | up to 10 (extra $38) | 2 h: 3 Shifts incl. crawler trail, tow-truck rescue staged for the birthday child, party room 60 min, themed cake slot, host + assistant, group photo on the podium |
| **Site Manager's Party** | $749 | up to 14 (extra $45) | 2.5 h: mini Energy Cup with podium ceremony, all Foreman's inclusions, custom event badge in-app, birthday child's name on the leaderboard screens all session |

Ages 6–7 run tethered/passenger formats with a guardian; 8+ per the entry-class canon. Food from the standard party menu (F&B pricing: Volume 10); outside cakes welcome (candle policy per fire SOP).

### 8.2 Party room and logistics

The Phase 1 entry pavilion includes one party room (Phase 3 adds two more with the event centre — Volume 11): seats 16 children + 8 adults, wipeable surfaces, direct sightline to Track A so parents watch from the table. Turnover standard: 30 minutes between parties (reset checklist below). Peak capacity: 3 parties/Saturday, 2/Sunday off the single room; the constraint is host staffing, not space — never run a party without its dedicated host.

- [ ] Room reset: tables wiped, floor swept, bins cleared, decorations neutralized
- [ ] Party fleet staged: correct class count + 2 hot spares, packs at storage-to-full per charging SOP
- [ ] Certificates printed with children's names; pins counted; badge board for birthday child
- [ ] Host briefed: birthday child's name, allergies flagged from booking form, photo consent list
- [ ] Tow-truck rescue pre-staged (Foreman's+): casualty vehicle and recovery crawler positioned
- [ ] Guardian waivers verified complete in OS (Toolbox Talk child-flow, Section 2.4)

### 8.3 The host role

The party host is a trained front-of-house role (not a marshal pulled off a track): owns the run-sheet minute by minute, holds the group's energy, executes the ceremony beats (first Shift countdown, the rescue, the podium), and hands the parent a one-tap rebooking offer at farewell. Hosts are scripted but not robotic — the scripts (Chapter 11.2) define beats, not lines. One host per 10 children; assistant above 10.

### 8.4 Upsells and family products

In-flow upsells (offered at booking, never mid-party): extra Shift round +$8/child, premium cake slot, group photo prints, goodie-bag upgrade (park cap + extra pin), and the strongest performer — the **Birthday License Pack** (+$59): the birthday child gets a printed license card with photo, 3 return Casual Shifts, and 1,000 Gears. Family bundle (park canon: 4 drivers × 2 shifts, $89) is the standing family product outside parties; school-holiday **Family Mornings** (Sunday member hours extended to bundle-holders) keep the family segment on the calendar between birthdays.

> **Field Note.** The single highest-leverage moment of any party is the staged tow-truck rescue. Brief the birthday child privately ("a machine is going to break down out there — you're the recovery driver"), then let it "happen" in front of their friends. The rescue converts the party's social hierarchy for one afternoon — the birthday child is the hero with the winch — and it is the moment parents film. Never skip it to save schedule; cut a Shift instead.

## 9. Schools, Universities & STEM

### 9.1 Why education is a product line, not CSR

School programs fill weekday mornings (dead inventory), build the license pipeline years ahead of spending power, and give the park civic standing that pays off in permits, press and partnerships (Volume 2's stakeholder analysis). They are priced to margin, not charity — bursary places are funded by the Gears charity-burn option (Section 5.4) and a fixed 5% of program revenue.

### 9.2 School programs (ages 8–18)

All programs are curriculum-mapped (local mapping per deployment; the structure below maps cleanly to most physics/technology syllabi) and run 09:30–13:00 weekdays, 20–60 students, $22/student (min $440), teacher resources included:

- **Gears & Gearing (ages 8–12):** the physics of gear ratios taught on the machines that embody them — students measure how pinion changes alter a buggy's speed and a tractor's pulling force, then test predictions on track. Worksheet: ratio arithmetic; takeaway: every student earns the Clock-In badge on a real profile.
- **Electrons at Work (ages 11–15):** circuits, batteries and motors via the park's own doctrine — why LiPo cells live between 3.4–4.2 V, what voltage sag is, why the charging room is a bunker. Live demo at the charging bunker window; students read real Node voltage traces from their own Shift.
- **Data Drives (ages 14–18):** telemetry data science. Each team exports their session's Node data (CSV from the customer app), computes their own smoothness index in a spreadsheet, and competes on *analysis* — the best data story wins, not the fastest lap. This program is the park's flagship STEM asset because no competitor owns a comparable dataset.
- **Site Logistics (ages 12–16, Construction):** the 1:3 excavator-truck ratio as an operations-research problem — teams predict, then measure, throughput with 1, 2 and 3 trucks per excavator. Queueing theory taught with dirt.

Field-trip format: arrival briefing (Toolbox Talk school edition, teacher-supervised group waivers collected digitally in advance), two teaching blocks with Shift time embedded, results assembly with badge ceremony. Ratios: 1 park educator per 15 students plus teachers per school policy; accessibility provisions per Chapter 11.6.

### 9.3 University partnerships

- **Engineering-club leagues:** universities field standing teams in a dedicated **Varsity League** (season-long, Engineering Challenge rules — identical hardware, constrained tuning menu, telemetry-audited). Entry $360/team/season; the league is deliberately cheap because its yield is weeknight utilization, brand-embedded future professionals, and recruiting-sponsor revenue (engineering employers sponsor the league table).
- **Capstone projects on RCW Node / RC WORLD OS:** the park offers real engineering problems as final-year projects — Node antenna performance in the mesh, predictive-maintenance models on the fleet's runtime logs, computer-vision lap validation, battery state-of-health estimation from sag signatures. The park provides data access under NDA, a named Artisan mentor, and test time; the university provides free R&D and a hiring pipeline for Artisan and OS roles (framework agreement template: Volume 13 appendix).
- **Formula-style RC competition sponsorship:** the park sponsors and hosts an annual **Formula RCW** intervarsity event — student-built cars to a published rules formula (motor/battery/budget caps, mandatory RCW Node for scrutineering telemetry), design-report judging plus on-track events, mirroring Formula Student's structure at 1/10 scale. Hosting cost is modest (one weekend, existing track); the return is regional press, a pipeline of the exact talent the park hires, and the strongest possible answer to "is this a toy park?"

### 9.4 Education KPIs

School-days sold/term (target: 20 by Year 2), weekday-morning utilization on school days ≥70%, student→family return conversion within 90 days ≥8% (tracked via the take-home family voucher), 2 signed university partnerships by end of Year 2, Formula RCW inaugural event in Year 3 (aligns with Phase 3 classrooms — Volume 1 phasing).

## 10. The Mobile App Experience

### 10.1 Scope and platform

This chapter specifies the customer-facing app as an experience, screen by screen; the technical build — Kotlin Multiplatform / Compose Multiplatform on **both Android and iOS**, Supabase backend, role-based access inside RC WORLD OS — is Volume 13's territory and is only cross-referenced here. The design brief in one sentence: **the app is the customer's license, wallet and pit crew, in that order.** It must be excellent offline-tolerant on park Wi-Fi, one-handed, and legible in sunlight; every screen below has a stated job and one primary action.

### 10.2 Onboarding & the Toolbox Talk

1. **Welcome / account** — email or social sign-in; guardian flow creates child sub-profiles under one wallet. Job: get to a booking in under two minutes for the impatient; everything else can wait.
2. **Toolbox Talk** — the interactive induction: battery limits (the 3.4–4.2 V/cell window, told as "why your machine protects itself"), collision liability, track rules, the tow-truck doctrine ("you never walk onto a live site — you drive the rescue"), closing with the digital waiver signature. Interactive checks, not a video to skip; 8–12 minutes; per-division delta modules unlock later (marine, aviation, premium hydraulics). Completion mints the **Learner license** with a small ceremony — the card animates onto the screen, first 25 XP posts.
3. **First-visit primer** — optional 5-screen visual of the journey spine (wristband, binding, pit stop) so nothing on site is a surprise.

### 10.3 Wallet & booking

- **Wallet** — payment cards, Gears balance with expiry-soonest shown honestly, membership blocks remaining (with rollover state), vouchers and guest passes as scannable tokens. One screen; no sub-menus for money.
- **Booking** — division → class (locked classes shown greyed with their unlock stated plainly: "Requires Operator + Construction Advanced — you're 2 badges away", turning every refusal into a goal) → Shift type (Casual/Operator) → slot grid with live availability and member-window shading → pay with card, blocks or Gears. Family bookings seat multiple profiles in adjacent slots in one flow.

### 10.4 The live Shift dashboard

The screen customers actually use on site, auto-launched at vehicle binding (QR scan on the transmitter):

- **Header:** bound vehicle's name and asset tag, class, your handle and tier seal.
- **Battery/energy gauge** — the Node's live allocation readout, styled as an industrial fuel gauge; sag spikes flash amber (the F1-style doctrine made visible). In Energy Cup sessions this becomes the race budget.
- **Session clock** with pit-stop countdown on Operator Shifts ("pit window opens 18:00").
- **Live score strip:** laps and best lap (timing loop), or tonnage this Shift (load cells), or mission checklist (harbour/Sub Hunt).
- **Smoothness gauge** — the operator dial, live.
- **One action button, context-switching:** it is *Pit In* near the pit window, *Retrieve* when your vehicle dies (launches the tow-truck flow with a map pin on the casualty), and *Top-Up* when the queue logic offers an extension (next section).

### 10.5 Results, badge case & license card

- **Shift summary** (pushed within 60 s of session end): score, personal-best deltas, XP breakdown with smoothness bonus, Gears earned, badge pops, highlight clip when a track camera caught one — with a share sheet, because the clip is marketing the customer distributes voluntarily.
- **License card** — the career home screen: tier seal, XP bar to next tier with the *specific* remaining gates listed ("Smoothness avg 66/70 · 4/5 badges"), endorsement chips with grades, streak flame, season Track Points. Tapping the card flips it to a QR for staff scanning. This is the screen the whole chapter exists to serve; it must answer "what's next?" without scrolling.
- **Badge case** — the catalogue as a collection wall: earned badges in colour with date and the triggering session; unearned in silhouette with criteria; secret badges as unlabelled slots (counted, not described). Pin-claim status shown for physical collectibles.
- **Leaderboards** — every board from Section 5.1, filterable to "people I know" (friends list) because a rank of 3,407 motivates nobody but 2nd-among-friends motivates everyone.

### 10.6 The queue top-up flow

Implemented exactly per source doctrine: at T-5 minutes before a Shift ends, the OS queries the class `queue_roster`; **if and only if nobody is waiting for that class**, the dashboard's action button becomes *Top-Up* — one tap, wallet-charged block extension ($8 standard / $12 premium per extra block, or 2,500 Gears), vehicle never comes off the track. If a queue exists, the button never appears and the session ends on time — the offer's credibility rests on customers never seeing it while others visibly wait. Top-up revenue is pure utilization yield on already-staffed capacity; it is tracked as its own P&L line (Volume 10).

### 10.7 Notifications discipline

Push categories, each individually controllable: session/safety (cannot be disabled while on site), booking reminders, badge/tier events, streak & expiry warnings, offers (default *off* — earned trust, not claimed). Hard rule: no more than one marketing push per week, and every marketing push must contain a one-tap action worth taking. The app's notification reputation is a park asset; it is spent, not free.

## 11. Service Standards & Recovery

### 11.1 The service posture

Staff play *colleagues on the same site*, not vendors: the customer is a fellow operator, addressed with workshop courtesy ("your machine's ready, bay 3"). This is Disney-grade role discipline applied to an industrial frame, and it is trained, scripted and audited like any SOP. Front-of-house standards: greet within 10 seconds of reaching any counter; name the customer once their wristband is scanned; never say "no" without the path ("that class needs Operator — you're 300 XP out, and today's Shift gets you a third of the way").

### 11.2 Scripts as beats

Scripts define mandatory *beats*, with staff free in wording (verbatim-scripted staff sound like machinery — the wrong kind):

| Moment | Mandatory beats |
|---|---|
| Vehicle binding | Confirm name → confirm class & tier aloud → transmitter handover with one machine-specific tip → "clock in when ready" |
| Pit stop | Call the car in by name → narrate the swap ("fresh pack, tires look good") → explicit release ("you're clear — 20 more minutes") |
| Breakdown | Reassure fast ("your machine's down, not your Shift") → offer the rescue ("recovery crawler's yours — go get it") → fresh vehicle promise stated before the tow starts |
| Badge/tier pop (Gold/tier-up witnessed) | Announce on PA or to the immediate group → physical acknowledgment (handshake, pin pointer to retail) |
| Complaint opening | Listen without interruption → restate the problem in one sentence → state what happens next and when |
| Farewell (desk) | Next-unlock mention → invite back to a *specific* thing ("league night Thursday — your class") |

### 11.3 Complaint handling & the empowerment ladder

Every front-line staffer holds **Level 1 authority** without approval: re-run a Shift, comp an F&B kiosk item, grant up to 2,000 goodwill Gears — logged in the staff app with a reason code, reviewed weekly for patterns (not for blame; unlogged generosity is the firing offence, not logged generosity). **Level 2** (duty manager): refunds to original payment, party/event make-goods, membership-month credits. **Level 3** (GM): legal-adjacent matters, injuries (which immediately follow the incident SOP, Volume 7 safety chapter), media-visible situations. Response-time standards: on-site issues resolved or escalated within 10 minutes; app/service-desk tickets first-response within 24 hours; leaderboard appeals (Section 5.2) within 24 hours.

### 11.4 Refund policy — tied to the breakdown protocol

The policy is mechanical, so staff never negotiate from scratch:

| Situation | Remedy |
|---|---|
| Breakdown, retrieval + fresh vehicle inside 6 min | No refund due — the protocol *is* the remedy; clean-tow Gears paid; session clock paused during retrieval |
| Breakdown, no replacement vehicle available in class | Full Shift re-credit to wallet + 500 Gears; slot priority next visit |
| Second breakdown, same Shift | Full refund or re-credit (customer's choice) + 1,000 Gears — two strikes means fleet readiness failed (fed back to the daily-readiness KPI, Volume 7) |
| Weather closure mid-Shift (open divisions) | Pro-rata re-credit for unshifted blocks; booked-ahead sessions moved free |
| Park-fault cancellation (staffing, systems) | Full refund + a comped equivalent booking |
| Customer no-show / late >10 min | Slot released; one courtesy rebook per rolling 6 months, then forfeit per T&Cs |

Session-clock pause during retrieval is the load-bearing detail: it makes the "no refund due" line honest, because the customer genuinely lost no paid time.

### 11.5 Measurement: NPS and CSAT

- **NPS**: single-question push at +24 h post-visit (25 Gears for answering); target ≥55 by operating Month 12, building to ≥60 by Year 3; detractors (<7) trigger a service-desk callback task within 48 h.
- **CSAT micro-pulses**: one-tap ratings embedded at three moments only — post-Shift summary, post-party (to the booking parent), post-corporate (to the organizer). Never more; survey fatigue is a real cost.
- Both post to the GM dashboard alongside the journey KPIs (Section 2.2), reviewed weekly; any touchpoint two weeks below target gets a named owner and a dated fix.

### 11.6 Accessibility and inclusion

RC operation is unusually accessible — the machine does the running — and the park commits to making that true in practice:

- [ ] Step-free routes to all driver rostrums, pit lane, party room and viewing rails (build spec: Volume 11); seated-operation positions at every rostrum
- [ ] Adaptive control library: wheel-to-stick conversions, single-handed transmitter mounts, switch-access trigger adapters — bookable free with any Shift, maintained by The Works
- [ ] Sensory provisions: published quiet hours (first Sunday morning monthly — PA off, buzzers to visual-flash mode), ear defenders at the desk, sensory map in the app
- [ ] Toolbox Talk available with captions, audio narration and simplified-language mode; staff briefing covers non-visible disabilities
- [ ] Child protection: photo-consent flags on all party/school bookings honoured in every clip pipeline; child leaderboard identity rules (handle + initial, Section 5.1); staff working education/party programs hold local-equivalent background clearance
- [ ] Financial inclusion: schools bursary fund (Section 9.1); off-peak community rates reviewed annually
- [ ] Companion/carer enters free with a paying operator; the *operator* holds the license and the spotlight

> **Safety Warning.** No service-recovery gesture ever overrides a safety rule. A customer denied a premium hydraulic Shift for lacking the tier is offered a path, never an exception; a goodwill re-run never skips vehicle binding or tier profiles. The empowerment ladder buys goodwill with money and Gears — never with the safety envelope.

## 12. Volume Summary & Cross-References

RC WORLD's customer experience is one machine with many faces. The industrial frame (Chapter 1) turns rentals into careers and friction into gameplay — the Tow-Truck Retrieval Protocol being the emblem. The journey spine (Chapter 2) is instrumented end to end, with an owner and a KPI at every touchpoint and a hard rule that no customer leaves without knowing their next unlock. The **RC WORLD License** (Chapter 3) is the core asset: six earned tiers (Learner → Apprentice → Operator → Foreman → Site Manager → Legend, at 0 / 500 / 2,000 / 6,000 / 15,000 / 40,000 XP) on a skill axis, visit streaks on a frequency axis, four division endorsements (Basic/Advanced/Master), and equipment gates that make rank real — premium hydraulics, FPV and jet-class machines are unreachable without earning them. Sixty named badges (Chapter 4) give the career its texture; the Gears economy, class-normalized leaderboards, Energy Cup scoring and the two-track quarterly Season Pass (Chapter 5) give it a pulse. The three memberships (Apprentice $29 / Operator $59 / Foreman $99) and the $499 Annual Pass (Chapter 6) convert it to recurring revenue; corporate (from $1,400), parties (from $349) and education programs (Chapters 7–9) fill the off-peak calendar and feed the license pipeline. The app (Chapter 10) carries it all in the customer's pocket, and the service doctrine (Chapter 11) keeps the promises — mechanically, with an empowerment ladder and a refund table tied to the breakdown protocol.

**Cross-references**

- **Volume 1** — Executive Master Plan: phasing of party rooms, classrooms and event centre; retention economics in the investment case.
- **Volume 2** — Market Research: the competitive lessons (score everything, feed the spectators, sell the next visit) this volume operationalizes.
- **Volume 3** — Motorsport Division: parity doctrine and reference laps behind the Pace Index; transmitter tier profiles; race formats, leagues and timing systems feeding XP and boards.
- **Volume 4** — Construction Division: career tonnage, hopper load-cell scoring, Harvest Campaigns, hydraulic premium-experience supervision — all gated per Section 3.6 (which supersedes earlier "tier 2/3" phrasing).
- **Volume 5** — Aviation Division: the Wings ladder (§9.3: Ground → Bronze → Silver → Gold Wings, plus Type: Jet / Type: FPV / Type: Heli ratings) mapped to the Aviation endorsement grades; FPV and jet-class gates; checkride and currency rules.
- **Volume 6** — Marine Division: the marine badge-task ladder (Ch. 8 §8.4: Deckhand, Coxswain, Tug Master, Race Skipper, Sail Grade 1–3, Submariner) mapped to the Marine endorsement grades; mission scoring and retrieval Gears.
- **Volume 7** — Engineering & Workshop Manual: fleet-readiness and safety SOPs that the refund table and breakdown protocol depend on; The Works bench-hour supervision.
- **Volume 10** — Finance: Gears redemption-cost guardrail (≤4% of gross revenue), membership and deferred-revenue modelling, top-up and party P&L lines, discount stacking cap; home of the 90-day second-visit KPI (§10.4: ≥22% Year 1 / ≥28% Year 3, Phase 2 gate floor ≥20%).
- **Volume 11** — Architecture & Park Design: party room, accessibility build specs, leaderboard screen placement, retail exit line.
- **Volume 12** — Franchise Manual: license/badge/Gears canon as a mandatory franchise standard — customer careers must be portable across RC WORLD sites.
- **Volume 13** — RC WORLD OS: the technical build of everything here — XP/Gears/Track Point ledgers, badge trigger pipeline, queue top-up logic, CRM churn states, leaderboard framework, app screens on Kotlin Multiplatform for Android and iOS.

