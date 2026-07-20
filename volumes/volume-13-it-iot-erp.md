# Volume 13 — IT, IoT & ERP Systems (RC WORLD OS)

**RC WORLD — Master Development Plan** · Volume 13 of 13
**Revision:** 1.0 · **Date:** July 2026 · **Status:** Living document — bump revision on material change

**Purpose of this volume.** This volume is the complete technical specification and development plan for **RC WORLD OS** — the single software platform that runs every sector of the business: finance and accounting, HR and payroll, online payments and the closed-loop wallet, bookings and queue management, fleet and maintenance management, live IoT telemetry from every powered asset, POS/retail/F&B, CRM and gamification, corporate events, access control, document management, and franchise multi-site operations. It specifies the architecture (Supabase/PostgreSQL + Kotlin services; Kotlin Multiplatform / Compose Multiplatform client apps on **both Android and iOS**; a web admin console), the founder-mandated **role-based access control** design under which every user class — executive, finance, HR, operations, division lead, Artisan, marshal, front-of-house, F&B, franchisee, customer — sees a different interface scoped to its permissions, the consolidated data model, the non-functional requirements, and the sprint-level implementation roadmap that delivers a working v1 before Phase 1 opening. A CTO or lead engineer hired into RC WORLD should be able to scope, staff, and ship the platform from this volume alone, honouring the telemetry and schema doctrine established in the original engineering blueprint.

**Intended readers.** The CTO / lead engineer and the RC WORLD OS development team; the founder and General Manager (as product owners); the finance manager (modules 5 and 8); investors performing technical due diligence; franchise operators evaluating the platform they will licence (with Volume 12); The Works engineering staff who maintain the RCW Node fleet.

**Chapters**

1. Platform Vision & Architecture Overview
2. Technology Stack & Development Approach
3. Identity, Roles & Access Control
4. Bookings & Scheduling Module
5. Payments & Wallet Module
6. Fleet Management & Maintenance Module
7. Live Telemetry & IoT Platform
8. Finance & Accounting Module
9. HR & Payroll Module
10. CRM, Marketing & Gamification Module
11. Additional Modules
12. Data Model
13. Non-Functional Requirements & Operations
14. Implementation Roadmap
15. Volume Summary & Cross-References

---

## 1. Platform Vision & Architecture Overview

### 1.1 One operating system for the whole business

RC WORLD is a miniaturized industrial complex, and it is run like one: by a single integrated operating system, not a patchwork of disconnected SaaS subscriptions. RC WORLD OS is that system. The same platform that streams a 1 Hz voltage feed from a $60 buggy on Track B also computes the marshal roster for Saturday, recognizes the revenue on a $99/month Foreman membership, decrements a brass pinion from The Works' spares shelf when an Artisan closes a work order, and shows the founder a live P&L. This is a deliberate strategic position, inherited from the original engineering blueprint: **high utilization of commercial-grade equipment is achieved through software** — telemetry that knows where every asset is and how healthy it is, bookings that keep every track slot sold, and gamification that brings the customer back.

The integration is the moat. A generic booking tool cannot offer a Top-Up button at T-5 minutes because it cannot see `queue_roster`. A generic maintenance CRM cannot open a work order because a motor's runtime crossed a greasing threshold, because it cannot see `live_telemetry`. A generic loyalty app cannot award a "Smooth Operator" badge for a low voltage-sag score, because it never sees a voltage curve. RC WORLD OS can do all three, on one customer record, one asset record, and one ledger.

### 1.2 Architecture at a glance

```text
 PARK EDGE                                CLOUD                              CLIENTS
┌─────────────────────────┐   ┌──────────────────────────────┐   ┌─────────────────────────────┐
│ ~150 powered assets     │   │  RC WORLD OS backend          │   │ Customer app (KMP/Compose)  │
│  each with RCW Node     │   │                               │   │   Android + iOS             │
│  (ESP32-C3, GPS,        │   │  ┌────────────────────────┐   │   │                             │
│   voltage divider,      │   │  │ Kotlin services (Ktor) │   │   │ Staff app (KMP/Compose)     │
│   PWM intercept)        │   │  │  ingestion · geofence  │   │   │   Android + iOS             │
│        │ 2.4 GHz        │   │  │  lap timing · rules    │   │   │   role-scoped modules       │
│        ▼                │   │  │  payroll calc · OTA    │   │   │                             │
│ Outdoor Wi-Fi mesh      │   │  └───────────┬────────────┘   │   │ Web admin console (SPA)     │
│ (Omada-class APs,       │──▶│              ▼                │◀─▶│   exec/finance/HR/ops       │
│  roaming handoff)       │   │  ┌────────────────────────┐   │   │                             │
│        │                │   │  │ Supabase               │   │   │ POS terminals (staff app    │
│        ▼                │   │  │  PostgreSQL (+RLS)     │   │   │  kiosk mode + card reader)  │
│ Edge cache server       │   │  │  Auth (JWT, MFA)       │   │   │                             │
│ (local queue, offline   │   │  │  Realtime (fan-out,    │   │   │ Walk-in kiosks              │
│  degraded mode, §13.2)  │   │  │   kill-switch channel) │   │   │ Track-side leaderboards     │
│                         │   │  │  Edge Functions        │   │   │ (Grid View wall display)    │
└─────────────────────────┘   │  │  Storage (photos, docs)│   │   └─────────────────────────────┘
                              │  └───────────┬────────────┘   │
                              │              ▼                │   ┌─────────────────────────────┐
                              │  Module layer: bookings ·     │──▶│ External: Stripe/Adyen-class│
                              │  payments/wallet · fleet ·    │   │ PSP · Xero/QuickBooks-class │
                              │  telemetry · finance · HR ·   │   │ ledger export · local       │
                              │  CRM · POS · events · docs    │   │ payroll processor · FCM/APNs│
                              └──────────────────────────────┘   └─────────────────────────────┘
```

Data flows left to right for telemetry (RCW Nodes → mesh → Kotlin ingestion → Postgres → Realtime fan-out → apps) and right to left for commands (admin app → Realtime kill-switch channel → node → PWM intercept → ESC to neutral). Every module reads and writes the same PostgreSQL schema under Row Level Security, so "different interfaces for different users" (Chapter 3) is enforced in the database, not merely hidden in the UI.

### 1.3 Build-vs-buy policy

The platform's scope is large; the engineering team is small. The policy that reconciles the two:

| Capability | Decision | Rationale |
|---|---|---|
| Telemetry ingestion, kill-switch, lap timing, geofencing | **Build** | Core differentiator; no product on the market intercepts PWM on a 1/14 excavator |
| Bookings, Shift inventory, queue_roster, Top-Up flow | **Build** | The 20-minute Shift and T-5 Top-Up are proprietary revenue mechanics |
| Gamification: XP, licenses, badges, leaderboards | **Build** | Driven by telemetry events only we have; the loyalty moat |
| Closed-loop wallet + Gears ledger | **Build** (double-entry core) | Wallet liability accounting must integrate with our finance module |
| Card processing, Apple Pay / Google Pay | **Buy** — Stripe-class / Adyen-class PSP | Never touch PANs; tokenization keeps us out of PCI-DSS SAQ D (§5.6) |
| Accounting ledger (statutory books) | **Buy** — Xero/QuickBooks-class, fed by our GL-lite export | Tax filing and audit belong in a mature accounting product |
| Payroll processing (tax tables, filings) | **Buy** — local payroll processor; we compute hours and export | Jurisdiction-specific tax logic is a liability, not a differentiator |
| Email/push delivery | **Buy** — FCM/APNs, SES/Postmark-class email | Commodity infrastructure |
| Auth, database, realtime transport | **Platform** — Supabase | Managed Postgres + Auth + Realtime is the fastest safe path |
| CCTV VMS, card readers, receipt printers | **Buy + integrate** | Hardware ecosystems; we integrate via APIs (§11.4) |

> **Field Note.** The test we apply before writing any line of code: *does this feature touch a Shift, an asset, or a customer's progression?* If yes, build — it will need our data and our doctrine. If no, it is commodity; buy it and spend the saved sprint on telemetry reliability, which is the one system that can close the park if it fails.

### 1.4 Platform principles

1. **One schema, one truth.** Every module writes to the same PostgreSQL database. No CSV shuttling between systems inside the park; exports exist only at the boundary (accounting, payroll).
2. **RLS is the security perimeter.** UI hiding is a courtesy; Row Level Security is the enforcement. Every table carries policies; no client ever holds a service-role key.
3. **The park must run when the internet does not.** Telemetry safety (kill on under-voltage/geofence) executes on the node itself; check-in, POS, and queue continue from the edge cache server (§13.2).
4. **Site-scoped from day one.** Every business table carries `site_id`. Site 1 is the flagship; the franchise network (Volume 12) is a configuration change, not a rewrite.
5. **Auditability over cleverness.** Money, roster, and safety actions are append-only, attributed, and timestamped. If a regulator, insurer, or franchisee asks "who did what, when" the answer is one query.

## 2. Technology Stack & Development Approach

### 2.1 Client apps: Kotlin Multiplatform + Compose Multiplatform, Android and iOS

The original blueprint specified a Kotlin + Jetpack Compose native Android app. This volume extends that decision — explicitly, per the living-document rule — to **Kotlin Multiplatform (KMP) with Compose Multiplatform (CMP)**, producing native apps for **both Android and iOS from one shared codebase**. The founder's requirement is unambiguous: client apps must be supported on both platforms, because roughly half of the target family and hobbyist demographic in a mid-size international city carries iPhones, and a customer who cannot install the app cannot complete the Toolbox Talk, hold a wallet, or join the queue.

Why KMP/CMP rather than two native teams or a JavaScript-based cross-platform stack:

- **Continuity.** The backend services are Kotlin; the original app plan was Kotlin; the team hires from one language pool. Domain logic — Shift timing rules, wallet arithmetic, XP evaluation, telemetry parsing — is written once in `commonMain` and unit-tested once.
- **Real native UI performance** for the live parts of the product: the Grid View map, the lap-timer HUD, and the live voltage gauge redraw at interactive frame rates; Compose Multiplatform renders via Skia on iOS with native performance characteristics.
- **Two apps, one codebase, shared modules.** We ship a **Customer app** and a **Staff app** as separate store listings (different review cycles, different permission requests), both built from the same repository with shared `core`, `design-system`, `telemetry`, `wallet`, and `api` modules. The staff app adds role-gated feature modules (Chapter 3).

What stays platform-specific (in `androidMain` / `iosMain` via `expect`/`actual`):

| Concern | Android | iOS |
|---|---|---|
| Push notifications | Firebase Cloud Messaging | APNs |
| Wallet-sheet payments | Google Pay API | Apple Pay (PassKit) |
| QR/NFC scanning | CameraX + ML Kit-class scanner; NFC via Android NFC API | AVFoundation; Core NFC |
| Geofenced clock-in location | FusedLocationProvider | Core Location |
| Background telemetry viewing | Foreground service (staff app) | Background modes (audited narrowly for App Store review) |
| Secure credential storage | EncryptedSharedPreferences / Keystore | Keychain |
| Store distribution | Play Console (internal → closed → production tracks) | App Store Connect + TestFlight |

> **Field Note.** Budget App Store review friction into the schedule. The staff app's kill-switch button and the customer app's closed-loop wallet both attract reviewer questions (remote device control; stored value). Prepare a reviewer-facing demo video and a written explanation of the closed-loop wallet (single-merchant stored value, not a money-transmitter product) before the first TestFlight external build — this paperwork has a two-sprint lead time if handled reactively.

### 2.2 Web admin console

Deep back-office work — permission matrices, finance close, payroll review, franchise dashboards — belongs on a large screen. The web admin console is a single-page application: **TypeScript + React-class SPA** (Next.js-class framework), using the Supabase JavaScript client for auth/RLS-scoped queries and the Kotlin service APIs for heavy operations. Kotlin/JS and Compose for Web were evaluated and declined for v1: the web hiring pool, component ecosystem (tables, charts, form-heavy CRUD), and admin-dashboard tooling are materially stronger in the TypeScript ecosystem, and the console shares *data contracts* (generated from the OpenAPI spec and the Postgres schema) rather than UI code with the apps. Revisit at v2 if Compose for Web matures.

### 2.3 Supabase: what we use and how

| Supabase component | Use in RC WORLD OS |
|---|---|
| **PostgreSQL** | The one schema (Chapter 12). Partitioned `live_telemetry`; JSONB for flexible payloads (`parts_used`, badge criteria); `pgcrypto` for column encryption of sensitive HR fields |
| **Auth** | Email/phone + OAuth sign-in for customers; staff accounts provisioned by HR; JWT carries `app_role` and `site_id` custom claims (§3.4); TOTP MFA enforced for privileged roles |
| **Realtime** | Fan-out of telemetry rows to Grid View and customer dashboards; the **kill-switch command channel** (doctrine: KILL over Supabase Realtime); queue position updates; leaderboard pushes |
| **Row Level Security** | The enforcement layer for the entire RBAC design (Chapter 3) |
| **Edge Functions** | PSP webhooks (payment confirmed, refund settled), booking-confirmation email triggers, scheduled jobs (downsampling, cert-expiry alerts) where a full Kotlin service is overkill |
| **Storage** | Damage photos, staff documents, SOP PDFs, firmware binaries for OTA (signed, versioned) |

### 2.4 Kotlin backend services

Everything that is compute-heavy, latency-sensitive, or long-running lives in **Kotlin services (Ktor-class framework)** deployed as containers alongside Supabase:

- **Ingestion service** — terminates node connections, validates/batches telemetry inserts (Chapter 7).
- **Rules engine** — geofence evaluation, under-voltage detection, lap-timing state machines, predictive-maintenance threshold evaluation, XP/badge triggers. One event-driven service consuming the telemetry stream.
- **Ledger service** — the only writer to wallet/Gears ledger tables; enforces double-entry invariants in one transactional code path (§5.3).
- **Payroll calculator** — hours/overtime computation runs (§9.4).
- **OTA manager** — firmware manifest signing and staged rollout (§7.8).
- **Export service** — accounting journal export, payroll export, BI extracts.

Services are stateless where possible, horizontally scalable, and communicate through Postgres (LISTEN/NOTIFY and outbox tables) rather than a separate message broker in v1 — one fewer system to operate at a single site.

### 2.5 Environments, CI/CD, testing

Three environments, each a separate Supabase project and container stack: **dev** (developers, seeded synthetic data), **staging** (park-identical config, a bench of 6 physical RCW Nodes in The Works wired to test vehicles), **prod**. Database schema migrates via versioned SQL migrations (sqldelight/Flyway-class tooling); RLS policies are migrations too, and are code-reviewed like application code.

CI/CD on a GitHub Actions-class pipeline:

1. Every PR: Kotlin compile for all targets, unit tests (`commonTest`), lint, RLS policy tests (pgTAP-class suite that asserts each role can/cannot read canary rows), SQL migration dry-run.
2. Merge to main: deploy dev; run integration suite (API contract tests, Maestro-class UI smoke flows on Android emulator + iOS simulator).
3. Tagged release: deploy staging; hardware-in-the-loop test against the bench nodes (telemetry round-trip, kill-switch latency assertion ≤ budget in §7.4); manual QA sign-off; then prod, with app binaries promoted through Play internal track / TestFlight.

Testing strategy pyramid: heavy unit coverage of domain logic in `commonMain` (wallet arithmetic, Shift-state transitions, XP rules — these are pure functions by design); pgTAP-class tests for every RLS policy; contract tests between apps and services from the shared OpenAPI spec; a small, ruthless set of end-to-end flows (book → pay → check in → drive → telemetry → Shift close → wallet debit) that run nightly against staging with bench hardware.

### 2.6 API design and offline-first client data

Two API surfaces, deliberately kept distinct. **Direct Supabase access** (PostgREST-style queries through the Supabase client, always under RLS) serves simple reads and own-record writes — browsing slots, reading a wallet balance, acknowledging a document. **Kotlin service APIs** (REST, OpenAPI-specified, JWT-authenticated with the same claims) serve anything transactional or multi-table: taking a payment, closing a work order, starting a Shift clock, issuing a kill command's sibling actions. The rule for choosing: *if the operation must be atomic across tables or enforce an invariant, it goes through a service; if RLS alone expresses the rule, the client may query directly.* The OpenAPI spec generates the Kotlin client in `commonMain` and the TypeScript client for the console, so contract drift is a compile error, not a production incident.

Clients are **offline-tolerant by design**, not by afterthought. The apps hold a local store (SQLDelight-class, shared in `commonMain`) with three data classes: *always-cached* (my bookings and QR codes, my wallet balance as-of, today's roster, SOPs I must acknowledge — render with a staleness banner when unsynced), *live-only* (telemetry HUD, Grid View, queue positions — these show a connectivity state honestly rather than stale positions), and *queued writes* (clock-in, work-order notes, incident photos — written locally with client-generated UUIDs and replayed with idempotency keys). A marshal in a mesh dead spot can still photograph damage and write an incident; a customer in the car park can still show their booking QR at the gate. What no client ever does is queue a *payment* or a *kill command* — those are online-only actions with explicit failure UI, because a replayed stale kill is worse than a refused one.

### 2.7 Team plan, build phases, budget

The build runs on a compact senior team; the roadmap detail is Chapter 14.

| Role | FTE (build) | FTE (run, Year 1+) |
|---|---|---|
| Tech lead / architect | 1.0 | 0.5 (becomes head of platform) |
| KMP/Compose engineers | 2.0 | 1.0 |
| Kotlin backend engineer | 1.0 | 1.0 |
| Web (TypeScript) engineer | 1.0 | 0.5 |
| Firmware engineer (RCW Node, shared with The Works) | 0.5 | 0.25 |
| QA engineer | 0.5 | 0.5 |
| Product designer | 0.5 | 0.25 |

Phasing: **MVP (v1)** ships before Phase 1 opening — bookings, wallet + payments, telemetry + kill-switch, fleet + maintenance, POS, RBAC core, Toolbox Talk (Chapter 14 defines the sprint plan). **v1.5** (Months 13–20) adds HR/payroll depth, finance close automation, CRM automations. **v2** (Months 21–36) adds franchise multi-tenancy activation, advanced analytics, and the Phase 2 division modules (aviation/marine mission scoring).

Budget, consistent with Volume 10's software line: **v1 development ≈ $185k** (team-months at blended $9–11k/month fully loaded in a favourable engineering market, plus $12k hardware/bench/licences), inside Phase 1's $1.85 M capex envelope; **run costs ≈ $45k/year** (Supabase Pro-class tier, container hosting, PSP fixed fees, push/email volume, observability tooling, store accounts) plus the run-team payroll above, which Volume 10 carries under operating headcount. Volume 10 is the source of truth for the consolidated numbers; any change there sweeps back into this section.

## 3. Identity, Roles & Access Control

This is the chapter the founder mandated in the brief: RC WORLD OS must give **different interfaces to different users based on access level**, across every user class in the business. The design principle is stated once and enforced everywhere: **the role decides three things — what data the database will serve you (RLS), what actions the API will accept from you (permission checks), and what the app renders for you (role-scoped navigation).** All three derive from the same role catalogue, so they can never disagree.

### 3.1 Role catalogue

Roles are assigned per user *per site* (a franchisee's ops manager has no rights at the flagship). One user may hold multiple roles (a division lead who also marshals); the app composes the union of permissions and offers a workspace switcher.

| # | Role code | Title | Primary surface | Notes |
|---|---|---|---|---|
| 1 | `executive` | Founder / GM / Executive | Web console + staff app | Cross-module read; strategic KPIs; limited write (approvals) |
| 2 | `finance_mgr` | Finance manager | Web console | Ledger, reconciliation, refund approval, exports; separation-of-duties rules §3.7 |
| 3 | `hr_mgr` | HR manager | Web console + staff app | Staff records, contracts, payroll runs, certifications |
| 4 | `ops_mgr` | Operations manager | Staff app + web console | Park-wide day control: rosters, capacity, incidents, weather closures |
| 5 | `division_lead` | Division lead (Motorsport, Construction, Aviation, Marine) | Staff app | `ops_mgr` powers scoped to one division |
| 6 | `artisan` | Artisan / technician | Staff app | Work orders, parts, battery lifecycle, asset status transitions |
| 7 | `marshal` | Track marshal | Staff app | Live Grid View, kill-switch, incident reports, retrieval protocol, Shift start/stop |
| 8 | `foh` | Front-of-house / POS | Staff app (kiosk mode) | Check-in, walk-in bookings, wallet top-ups, retail POS |
| 9 | `fnb` | F&B staff | Staff app (kiosk mode) | F&B POS, stock counts; no access to bookings or fleet |
| 10 | `franchisee` | Franchisee owner | Web console + staff app | Full operator rights **scoped to own site(s)**; sees franchisor-published doctrine read-only |
| 11 | `franchise_staff` | Franchise site staff | Staff app | Any of roles 4–9, site-scoped; provisioned by the franchisee |
| 12 | `customer` | Customer | Customer app | Own bookings, wallet, telemetry of own bound vehicle, progression |
| 13 | `guardian` | Guardian (of minor customer) | Customer app | Manages linked minor profiles: consent, spend limits, visibility (§10.6) |
| 14 | `service` | Machine identities | — | Ingestion service, kiosks, leaderboards; least-privilege API keys, never user JWTs |

### 3.2 Permission matrix per module

Legend: **F** full (read/write/configure) · **W** read/write within scope · **R** read only · **O** own records only · — no access. "Scope" is always site-scoped for roles 4–11 and division-scoped for role 5.

| Module | exec | finance | HR | ops mgr | div lead | artisan | marshal | FOH | F&B | franchisee | customer/guardian |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bookings & queue | R | R | — | F | W | R | W (start/stop) | W | — | F (own site) | O |
| Payments & wallet | R | F | — | R | R | — | — | W (take payment) | W (take payment) | F (own site) | O |
| Refunds | approve >$200 | approve ≤$200; execute | — | request | request | — | request (breakdown) | request ≤$25 auto | — | per own-site policy | request |
| Fleet & maintenance | R | R (costs) | — | W | W | F | R + status flags | — | — | F (own site) | O (bound vehicle) |
| Telemetry & kill-switch | R | — | — | W + kill | W + kill | R + kill (bench test) | **F + kill** | — | — | W + kill (own site) | O (own session view) |
| Finance & accounting | R | F | R (payroll GL) | R (own budget) | R (own budget) | — | — | — | — | F (own books) | — |
| HR & payroll | R (aggregates) | R (cost) | F | W (roster) | W (roster) | O + clock-in | O + clock-in | O + clock-in | O + clock-in | F (own staff) | — |
| CRM & gamification | R | — | — | W | W | — | R (customer license tier) | R (profile at desk) | — | F (own site) | O |
| Retail/F&B stock | R | R | — | W | — | — | — | W (retail) | W (F&B) | F (own site) | — |
| Corporate events | R | R (invoices) | — | F | W | — | — | R | R (catering brief) | F (own site) | O (their event) |
| Documents & SOPs | F | R | W (HR docs) | W | W | R + acknowledge | R + acknowledge | R + acknowledge | R + acknowledge | R (doctrine) + W (local) | R (waivers, own) |
| System config & roles | R | — | grant roles ≤ mgr | — | — | — | — | — | — | grant own-site roles | — |
| Audit log | R | R (financial) | R (HR) | R (ops) | — | — | — | — | — | R (own site) | — |

Role grants above manager level (`executive`, `finance_mgr`, franchise-network roles) require a second approver (§3.7). The matrix is stored in the `role_permissions` table (Chapter 12) and rendered in the admin console — the table above is the specification; the database is the implementation.

### 3.3 One platform, many interfaces: screen-by-screen

The founder's requirement is that each role *sees a different application*. In practice all staff roles run the same binary; at sign-in the app reads the JWT role claims and assembles a role-scoped navigation graph. What each role experiences:

**Executive (web console + app).** Home = the Volume 10 KPI wall: today's revenue vs. same-weekday average, park utilization by division (RevPASH-style, §8.5), live visitor count, fleet availability %, incident flag. Drill-down is read-only into every module. One write surface: the approvals inbox (refunds >$200, purchase orders above threshold, role grants). No POS, no work orders — an executive who needs to edit a booking asks ops, by design.

**Finance manager (web console).** Home = cash position and reconciliation status: PSP settlement vs. ledger (§5.7), wallet liability balance, unposted journals, AP inbox with invoices awaiting three-way match (§8.3). Tabs: Ledger, Reconciliation, Refunds (their approval queue ≤$200), Exports (Xero/QuickBooks-class journal, payroll GL), Budget vs. actuals. Cannot edit bookings, rosters, or fleet — but sees the revenue consequences of all three.

**HR manager (web console + app).** Home = compliance dashboard: expiring certifications (Volume 12 Academy feed), contracts awaiting signature, open positions, absence today. Tabs: Staff records, Contracts, Certifications & training, Payroll runs (compute → review → export, §9.4), Performance reviews, Safety-training records. Sees payroll cost; cannot see customer PII beyond aggregate counts.

**Operations manager (staff app, tablet).** Home = the *day board*: weather + minima flags, roster gaps, queue depth per division, fleet-readiness (assets green/amber/red), incident feed. Actions: open/close zones, adjust capacity rules, reassign marshals, trigger weather closure (auto-credits interrupted Shifts per Marine/Aviation doctrine), approve comp Shifts. The kill-switch is available but two-tap-guarded — marshals are the primary users.

**Division lead.** The ops manager's board filtered to one division, plus division KPIs (e.g. Motorsport parity spread from Volume 3, Chapter 14) and division roster editing.

**Artisan (staff app, phone — one-hand operable, glove-friendly).** Home = *my work queue*: open work orders sorted by priority, assets awaiting turnaround, PM tasks due today. Core loop: scan asset QR → work order card (history from `maintenance_logs`, predicted issues, parts suggestions) → log parts used (decrements stock) → photos → close with sign-off → asset status transition (§6.3). Battery screens: scan pack QR, log cycle, view internal-resistance trend. No visibility of prices beyond parts cost, no customer data beyond the booking name on a turnaround.

**Marshal (staff app, phone, sunlight-readable dark theme).** Home = *my track now*: Grid View of live vehicles on their assigned track with voltage/geofence state per vehicle, Shift clocks, queue next-up list. Actions: start/stop Shift clock, **kill-switch** (single vehicle, guarded swipe), throttle-limit command, launch Tow-Truck Retrieval Protocol (pauses the Shift clock automatically), incident report with photo. The kill-switch control renders *only* for marshals, division leads, and ops managers whose site+division scope matches the vehicle — enforced by RLS on the command table, not just UI.

**Front-of-house / POS (staff app, kiosk mode on counter tablet).** Home = check-in scanner. Flows: scan booking QR → verify Toolbox Talk complete → hand off to marshal queue; walk-in sale (§4.3); wallet top-up (card via PSP terminal); retail POS with barcode scan. Cash drawer reconciliation at close. Cannot browse customer records — a scanned QR or a searched booking reference opens exactly one customer card.

**F&B staff.** F&B POS catalogue, order queue, stock count screen. Nothing else — the role exists so a seasonal barista's credentials are worthless if phished.

**Franchisee owner.** The full operator console — but every query is fenced to `site_id ∈ own_sites`. Additionally sees the *doctrine layer* read-only: franchisor-published SOPs, PM matrices, pricing floors (Volume 12), and their own site's compliance score. The franchisor's executive role sees cross-site dashboards (§11.6); the franchisee never sees another site's data.

**Customer (customer app).** Home = next booking + wallet balance + license progress ring. Tabs: Book (Shift inventory per division), Wallet & Gears, Garage (live view *of their bound vehicle only* during a Shift: voltage bar, position dot, lap times), Progression (XP, badges, leaderboards), Profile (waivers, minors they guard). During an active Shift the home surface becomes the live HUD, with the T-5 Top-Up button appearing per doctrine when `queue_roster` shows no waiting customer for that class.

**Guardian.** The customer app plus a *family* tab: linked minor profiles, per-minor spend caps, consent toggles, session notifications ("Ava's Shift started on Track C"), and the minor's progression view. Minors under the digital-consent age have no independent login (§10.6).

### 3.4 Identity architecture and JWT claims

Supabase Auth issues JWTs. A `user_site_roles` table (user, site, role, granted_by, granted_at, revoked_at) is the single source of role truth; a Postgres function stamps custom claims into the JWT at token mint:

```json
{
  "sub": "d3f6…", "email": "j.moyo@rcworld.example",
  "app_roles": [{ "site": 1, "role": "marshal" }, { "site": 1, "role": "artisan" }],
  "mfa_verified": true, "amr": ["password", "totp"]
}
```

Claims are convenience; the tables are truth. Every RLS policy joins live to `user_site_roles` (revocation is immediate, not token-expiry-delayed) and uses the claim only as a fast-path hint. Customer accounts self-register (email/phone/OAuth); staff accounts are provisioned by HR through an onboarding flow that creates the auth user, assigns roles, and issues a first-login enrolment link — staff never self-register.

### 3.5 RLS policy patterns

Four patterns cover the whole schema. Helper functions keep policies readable and testable:

```sql
-- Helper: does the current user hold a role at a site?
create or replace function auth_has_role(p_site bigint, p_roles text[])
returns boolean language sql stable security definer as $$
  select exists (
    select 1 from user_site_roles r
    where r.user_id = auth.uid() and r.site_id = p_site
      and r.role = any(p_roles) and r.revoked_at is null);
$$;
```

**Pattern 1 — own-records (customer):**

```sql
alter table bookings enable row level security;

create policy customer_own_bookings on bookings
  for select using (customer_id = auth.uid()
    or exists (select 1 from guardian_links g
               where g.guardian_id = auth.uid() and g.minor_id = bookings.customer_id));
```

**Pattern 2 — site-scoped staff read, role-gated write:**

```sql
create policy staff_read_fleet on fleet_inventory
  for select using (auth_has_role(site_id,
    array['executive','ops_mgr','division_lead','artisan','marshal','finance_mgr','franchisee']));

create policy artisan_update_fleet on fleet_inventory
  for update using (auth_has_role(site_id, array['artisan','ops_mgr','franchisee']))
  with check (status in ('available','bound','on_track','pit','maintenance','charging','retired'));
```

**Pattern 3 — command tables (kill-switch): insert-only, tightly scoped, never updatable:**

```sql
create policy marshal_kill_command on vehicle_commands
  for insert with check (
    command in ('KILL','LIMIT_20','RETURN_TO_PIT')
    and auth_has_role(site_id, array['marshal','division_lead','ops_mgr','franchisee'])
    and exists (select 1 from fleet_inventory f
                where f.id = vehicle_commands.vehicle_id and f.site_id = vehicle_commands.site_id));
-- No update/delete policies exist: commands are append-only and audited.
```

**Pattern 4 — column-level privacy (HR):** payroll-sensitive columns live in a separate `staff_compensation` table with policies granting only `hr_mgr`, `finance_mgr` (read), and the record's owner (own row read). Joining tables never expose pay data to rostering screens.

Every policy ships with a pgTAP-class test asserting both the allow and the deny case; a policy without a deny test does not merge.

### 3.6 Audit logging

A single `audit_log` table (append-only; insert via trigger and service code, no update/delete grants to anyone including `service` roles) records: actor, role used, site, action, entity type/id, before/after JSONB diff for sensitive tables (roles, refunds, payroll, price config, firmware rollouts), device id, IP. Kill-switch commands, refunds, role grants, payroll approvals, and firmware promotions are always audited. Retention: 7 years for financial actions, 3 years otherwise (§13.6). The executive and franchisee consoles render scoped audit views; nobody edits history.

### 3.7 Separation of duties for financial actions

| Action | Initiator | Approver | Rule enforced in |
|---|---|---|---|
| Refund ≤ $25 (breakdown protocol auto-credit) | System / FOH / marshal | Automatic, logged | Ledger service |
| Refund ≤ $200 | Any operational role | `finance_mgr` | Ledger service state machine |
| Refund > $200 | `finance_mgr` | `executive` | Ledger service state machine |
| Supplier invoice payment | `finance_mgr` (three-way match, §8.3) | `executive` above PO threshold | AP workflow |
| Payroll run release | `hr_mgr` computes | `finance_mgr` releases export | Payroll module |
| Price/config change (Shift prices, membership) | `ops_mgr` proposes | `executive` publishes | Config versioning |
| Role grant ≥ manager level | `hr_mgr` / `franchisee` | `executive` (or franchisor for franchise sites) | Role-grant workflow |

The invariant: **no single account can create a payee and pay it, or grant itself a role, or approve its own refund.** The approval workflows check `initiator ≠ approver` at the database level.

### 3.8 Session and device security

- **MFA (TOTP)** mandatory for `executive`, `finance_mgr`, `hr_mgr`, `ops_mgr`, `franchisee`, and any role holding kill-switch rights; enforced at Supabase Auth level (`amr` checked in RLS for privileged writes).
- **Session lifetimes:** customer 30 days refresh; staff app 12 hours (a shift); web console 8 hours with 15-minute idle lock on finance/HR screens.
- **Kiosk mode:** FOH/F&B tablets run pinned single-app mode, device-enrolled (MDM-class), auto-logout on 90 seconds idle, no credential storage beyond the device-bound session.
- **Device registry:** staff app installs register the device; ops can remote-revoke a lost phone's sessions in one action.
- **Shared-terminal rule:** POS operators re-authenticate with a 6-digit PIN per transaction batch; the till knows *who* rang every sale.

> **Field Note.** Resist the temptation to give the founder a super-admin bypass "just for launch week". The first role the RBAC system must constrain is the most senior one — if the founder's account can silently edit a ledger row, the audit log is theatre and the franchise pitch (Volume 12) loses its best slide: *the platform itself enforces the doctrine.*

### 3.9 Worked example: one breakdown, six interfaces

To make "different interfaces for different users" concrete, trace a single physical event — a buggy dies mid-Shift on Track B — through every role that touches it:

1. **Customer.** Their live HUD shows the voltage bar collapse, then a friendly breakdown card: "Your buggy's down — time to drive the tow truck." The Shift clock visibly pauses (doctrine: retrieval is never billed). They see only their own vehicle and their own session — RLS pattern 1.
2. **Marshal.** Their Grid View flashes the vehicle amber (under-voltage kill fired node-locally); the vehicle card offers *Launch Retrieval Protocol*. One tap pauses the Shift clock, sounds nothing (the 85 dB buzzer already fired on the vehicle per doctrine), assigns a recovery crawler, and opens an incident stub. The marshal never sees the customer's wallet, spend, or contact details — only name, license tier, and session.
3. **Artisan.** The buggy lands in their work queue as it enters `pit → maintenance`: a work order pre-populated with the telemetry trace (voltage curve for the last 3 minutes), the model's likely-failure list, and suggested parts. They see cost of parts, not prices of Shifts.
4. **Operations manager.** The day board ticks one fleet-availability point down and shows the incident in the feed. If a fresh vehicle wasn't issued within 5 minutes, they also see the auto-credit event. They can reassign the venue unit's capacity if the class is now short.
5. **Finance manager.** Nothing, today — the ≤$25 auto-credit posted automatically and appears only in tomorrow's reconciliation pack as one line among many. That absence is the design: finance sees money movements, not track drama.
6. **Executive.** Nothing individually — unless this is the third breakdown of that model this week, in which case the maintenance-cost-per-vehicle-hour KPI trend line moves and the weekly review asks The Works why.

Same event, same rows in the same database — six different renderings, each scoped by RLS to exactly what that role needs to act on. No role saw more; every role saw enough. This walkthrough is also the acceptance test for the RBAC epic in Sprint 1 (Chapter 14): the demo script executes precisely this scenario on the staging bench with six logged-in devices.

## 4. Bookings & Scheduling Module

### 4.1 Session inventory model

Bookings sell **Shift slots**: the intersection of a *venue unit* (track, zone pod, airfield cage slot, marina berth-block), a *vehicle class*, and a *20-minute time block* — the Shift, the park's atomic billing unit per canon. The inventory tree:

```text
site → division → venue_unit (Track A / Mining pod 1–4 / cage slot / basin block)
     → vehicle_class (touring, drift, excavator, tractor, tug, …)
     → session_slot (date, block_start, capacity, price_band)
```

Capacity per slot = simultaneously operable vehicles of that class on that venue unit (e.g. Track A touring: 8; Mining pod: 1 excavator + 3 dump trucks per the 1:3 doctrine — the pod is sold as linked slots). Slots are generated 28 days ahead by the capacity rules engine (§4.5) and priced by the pricing engine (§4.6). An Operator Shift books two consecutive blocks and reserves an Artisan battery-swap task in the pit-lane roster automatically.

### 4.2 Booking flows

**App booking (primary).** Browse division → class → day grid of slots with live availability → select → pay from wallet or card → booking QR issued. First-time customers are gated: no booking completes until the **Toolbox Talk** induction module for that division is passed and the waiver signed in-app (doctrine; the waiver PDF lands in Storage against the customer record).

**Walk-in kiosk / FOH.** FOH sells from the same inventory — there is no "walk-in allocation" that can double-book against the app. Kiosk flow: pick class → next available slot → pay (card/cash/wallet) → print/SMS the QR. Toolbox Talk runs on the kiosk for first-timers.

**Corporate & party bookings.** A `group_booking` reserves multiple venue units across a window (e.g. 2 h, 20 pax corporate per the $1,400 anchor), takes a configurable deposit (default 30%) through the payments module, holds inventory in `held` state until final payment T-7 days, and generates a run-sheet for ops (marshal assignments, catering brief to F&B, per-guest Toolbox Talk links sent ahead). Party packages auto-attach retail/F&B bundles.

### 4.3 Queue management and the Top-Up flow

`queue_roster` (doctrine table) is the live truth of who is waiting for which class at which venue unit. Rows: customer, class, venue unit, joined_at, state (`waiting` → `called` → `checked_in` → `expired`). Walk-ups without bookings join the queue from the app or kiosk and see a live position + estimated wait computed from Shift clocks.

**The T-5 Top-Up (doctrine, implemented exactly):** at five minutes before Shift end, the rules engine queries `queue_roster` for the vehicle's class at that venue unit. If no customer is `waiting`, the customer's live HUD renders the **Top-Up Session** button; one tap debits the wallet for another block and extends the Shift clock without the vehicle leaving the track. If a queue exists, the button never renders and the turnaround proceeds. The check re-runs at confirmation time to close the race window (a walk-up joining at T-4:50 wins over the top-up).

### 4.4 Shift lifecycle

```text
booked ──check-in──▶ vehicle_bound ──first stick input──▶ running ──▶ completed
   │ (QR at FOH)      (QR on transmitter,                   │
   │                   fleet status → bound)                ├─ top_up (extends running)
   ├─ cancelled (per policy: free ≥24 h, 50% ≥2 h)          ├─ interrupted_breakdown → retrieval → resumed on fresh vehicle
   └─ no_show (15 min grace, slot released to queue)        └─ interrupted_weather → auto-credit (doctrine)
```

Shift clocks live server-side (Kotlin rules engine) with the marshal app as start/stop authority; the customer HUD mirrors them via Realtime. Breakdown interruptions pause the clock automatically when the marshal launches the Tow-Truck Retrieval Protocol — retrieval time is never billed, park-wide doctrine.

### 4.5 Capacity rules engine

Declarative rules evaluated at slot generation and at every booking attempt: max vehicles per venue unit per class; excavator:truck 1:3 pod linkage; license-tier gates (premium classes require the RC WORLD License tier from Volume 9 — the booking UI hides what the customer cannot yet book and shows the progression path instead); weather minima pre-closures (aviation wind bands, marine 30/30 lightning rule feed from division dashboards); maintenance blackouts (a venue unit under grooming per Volume 4's register generates no slots); staffing constraint (slots require a rostered marshal for that venue unit — the roster module (§9.3) feeds capacity, so an un-staffed track sells zero Shifts rather than creating a morning surprise).

### 4.6 Pricing engine

Price bands resolve in order: base class price (canon: Casual $15/$22 premium; Operator $26/$38) → peak/off-peak calendar (weekend/holiday multiplier, school-term matrix maintained by ops, published by executive per §3.7) → membership entitlements (Apprentice/Operator/Foreman monthly Shift allowances and % discounts per Volume 9 — entitlement consumption is a wallet-ledger event, §5.3) → promotions (code or segment-targeted, CRM module). Every booking stores the full resolved price breakdown JSONB for finance (revenue recognition needs the components, §8.2).

### 4.7 Booking communications

Every booking state change has a defined communication, dispatched through the CRM module's channels with consent respected (§10.5): confirmation (push + email with QR and Toolbox Talk link if outstanding), T-24 h reminder with weather note for outdoor divisions, T-2 h "you're up soon" push with live queue context, weather-closure auto-credit notice (doctrine: no refunds debated at the water's edge — the app credits first and explains immediately), and post-visit summary (lap times, tonnage, XP earned, next-tier progress — the retention hook Volume 9 specifies). Group bookings add organizer-facing run-sheet updates and per-guest induction chasers at T-7/T-2 days; an organizer can see which guests haven't completed the Toolbox Talk, because a corporate event where eight of twenty guests hit the induction wall at the gate is an operational failure the software should have prevented the week before.

> **Field Note.** The T-2 h push carries the single highest-leverage sentence in the product: the live wait estimate. Customers who arrive to a known 15-minute queue rate the experience higher than customers who arrive to an unknown 5-minute one. Never suppress the estimate because it looks bad — suppressing it converts a scheduling problem into a trust problem.

## 5. Payments & Wallet Module

### 5.1 Payment surfaces

- **In-app:** card via Stripe-class / Adyen-class PSP mobile SDK; **Apple Pay** (iOS) and **Google Pay** (Android) as first-class sheets — family customers at a kiosk queue convert measurably better with wallet-sheet payments than with card entry.
- **POS terminals:** PSP-provided card readers (Stripe Terminal-class) paired to FOH/F&B kiosk tablets; cash accepted at FOH with drawer reconciliation.
- **Invoice:** corporate events pay deposit + balance by card link or bank transfer; bank transfers reconcile in the finance module (§8.3).

### 5.2 The closed-loop wallet

Every customer has a **wallet** (stored value, USD) and a **Gears balance** (loyalty points, earn-only from behaviour, spend on defined rewards — Volume 9 owns the earn/burn rules). The wallet is closed-loop: loadable, spendable only inside RC WORLD, refundable to source per policy. This keeps the product outside money-transmitter licensing in most jurisdictions — legal review per site is a franchise-launch checklist item (Volume 12).

### 5.3 Double-entry ledger design

All value movements — wallet, Gears, and the park's own revenue/liability view — post to one **double-entry ledger**. Two tables: `ledger_transactions` (id, site, occurred_at, type, reference, initiator, metadata JSONB) and `ledger_entries` (transaction_id, account_id, direction debit/credit, amount, currency `USD` | `GEARS`). Invariant enforced by the ledger service and a database constraint trigger: entries per transaction per currency sum to zero.

Core accounts:

| Account | Type | Meaning |
|---|---|---|
| `customer_wallet:{id}` | Liability | Value the park owes this customer |
| `wallet_liability_control` | Liability (control) | Sum of all wallets — the finance module's wallet-liability line |
| `psp_clearing` | Asset | Card money captured, not yet settled to bank |
| `cash_drawer:{till}` | Asset | Physical cash by till |
| `revenue:{product_type}` | Revenue | Shifts, memberships, retail, F&B, events — split per §8.2 |
| `gears_liability` / `gears_expense` | Liability / Expense | Points issued vs. redeemed, valued at standard cost |
| `refunds_payable` | Liability | Approved, not yet settled to source |

Worked example — customer loads $50 by card, then books a $15 Casual Shift from wallet:

| Txn | Debit | Credit | Amount |
|---|---|---|---|
| Wallet load | `psp_clearing` | `customer_wallet:123` | $50.00 |
| (PSP fee accrual) | `expense:psp_fees` | `psp_clearing` | $1.55 |
| Shift purchase | `customer_wallet:123` | `deferred_revenue:shifts` | $15.00 |
| Shift delivered (clock completes) | `deferred_revenue:shifts` | `revenue:shifts` | $15.00 |
| Gears earned (e.g. 15 Gears) | `gears_expense` | `gears_liability` | 15 GEARS |

The **ledger service is the only writer**; every other module requests postings through its API. Balances are materialized views refreshed transactionally — no module ever computes a balance by summing on the fly at POS speed.

### 5.4 POS integration

Retail and F&B sales post to the same ledger (`revenue:retail`, `revenue:fnb`) with basket lines captured for stock decrement (§11.1). Mixed tenders (part wallet, part card, part cash) are one transaction with multiple asset-side entries. Offline POS behaviour: the edge cache server (§13.2) queues card-present authorizations per PSP offline rules and cash sales unconditionally, replaying to the ledger on reconnect with idempotency keys.

### 5.5 Refunds and the breakdown protocol

Refund paths honour the separation-of-duties table (§3.7). The **breakdown protocol** path is automatic by doctrine: when a Shift is interrupted by vehicle failure and the Tow-Truck Retrieval Protocol runs, the paused clock means the customer loses nothing — but if a fresh vehicle cannot be issued within 5 minutes, the system auto-credits the remaining block value to the wallet and flags the incident to the division lead. Card refunds always return to the original payment method via the PSP; wallet credits are the default and preferred instrument (faster, retains the value in-park).

### 5.6 PCI-DSS scope minimization

RC WORLD OS **never sees a PAN**. Card entry happens in PSP-hosted fields/SDK sheets (app), PSP terminals (POS), and PSP payment links (invoices); we store only tokens, last-4, and brand. This keeps the platform at SAQ A / SAQ A-EP-class scope rather than SAQ D. Rules that keep it that way: no card data in logs (log scrubber tested in CI), no "card on file" outside PSP vault tokens, webhook signatures verified in Edge Functions, PSP keys in the secrets manager (§13.5) — never in client binaries.

### 5.7 Reconciliation to finance

Nightly job produces the reconciliation pack: PSP settlement report vs. `psp_clearing` movements (match on PSP transaction ids); cash drawer counts vs. `cash_drawer:*` per till per operator; wallet liability control vs. sum of wallet balances (must equal to the cent — any drift is a sev-2 incident, because it means the ledger invariant broke); Gears liability movement. Exceptions land in the finance manager's morning queue. Month-end, the pack feeds the GL export (§8.1).

> **Field Note.** Build the reconciliation *before* the first real payment, not after the first discrepancy. A wallet product without daily liability reconciliation is an unaudited bank. The nightly zero-check on `wallet_liability_control` is ten lines of SQL and it is the single highest-value alarm in the finance module.

## 6. Fleet Management & Maintenance Module

### 6.1 Asset registry

The doctrine table `fleet_inventory` is the registry, extended: id, site_id, mac_address (RCW Node), asset_tag, model_id (FK to a `vehicle_models` catalogue carrying class, division, scale, wholesale cost, spares profile), status (state machine below), total_hours_run, total_shifts, purchase_date, warranty_until, retirement_reason. Sub-assets (motors, ESCs, servos, the RCW Node itself) register in `asset_components` so a binned motor's history (Volume 3, §4.3 readback discipline) follows it across chassis. Batteries are first-class assets in `battery_packs` (§6.7), never components — they move between vehicles hourly.

### 6.2 QR/NFC asset tags

Every powered asset, battery pack, and transmitter carries a QR (laser-etched tag; NFC sticker optional where gloves make scanning awkward — Heavy fleet mudguards). The QR encodes only the asset UUID; everything else resolves server-side, so tags never leak data and never go stale. Scans drive the three core loops: customer **vehicle binding** at Shift start (scan transmitter QR → session binds customer↔transmitter↔vehicle, doctrine), Artisan work orders, and battery cycle logging.

### 6.3 Status state machine

The original schema's ENUM (active/maintenance/charging) is **extended — explicitly superseding the digest's three-state list** — to the operational reality:

```text
            ┌────────────────────────────────────────────────────┐
            ▼                                                    │
 available ──▶ bound ──▶ on_track ──▶ pit ──▶ available          │
     │          (QR bind)   │           (turnaround pass)        │
     │                      ├──▶ pit ──▶ maintenance ──▶ available (work order closed + sign-off)
     │                      │            │
     ▼                      │            └──▶ retired (writes retirement_reason; terminal)
  charging ◀────────────────┘  (battery-swap assets: pack goes to charging, vehicle to pit)
     └──▶ available
```

Transition rules enforced in the database (trigger validates legal transitions) and in RLS (`artisan` may move anything; `marshal` may move `on_track → pit` and flag `maintenance`; nobody moves `maintenance → available` except the closing Artisan via a signed work order — the Volume 3 handshake: *no car returns to active without sign-off*). Every transition is timestamped; the intervals are the utilization analytics (§8.5).

### 6.4 Runtime hours and cycle counting

`total_hours_run` accrues from telemetry, not manual logging: the rules engine sums `on_track` time from Shift clocks and adds motion-detected bench time. Cycle counters per class (Shifts, battery swaps, crash-flag events from accelerometer-inferred telemetry anomalies) feed the PM engine. Doctrine honoured: predictive maintenance from logged runtime hours drives gear-greasing and motor-commutator inspection flags.

### 6.5 Predictive maintenance and work orders

The PM engine evaluates Volume 7's preventive-maintenance matrices as data, not code: `pm_rules` rows carry (model_id or class, metric ∈ {hours_run, shifts, battery_cycles, days}, threshold, task template, priority). Nightly evaluation + real-time triggers (crash flag, marshal defect flag, three same-symptom repairs in 30 days → engineering review per Volume 6's retirement doctrine) generate **work orders**: asset, type (PM/repair/rebuild/inspection), priority, tasks checklist, parts suggestions from the model's spares profile. The Artisan loop (§3.3) closes them with `parts_used` JSONB (doctrine field), labour minutes, photos, and sign-off. `maintenance_logs` remains the historical record exactly as the digest defines it.

### 6.6 Parts inventory and procurement link

`parts_stock` per site: SKU (Volume 8 catalogue), bin location in The Works, qty, min/max, unit landed cost, supplier lead time. Work-order `parts_used` decrements stock transactionally; crossing min fires a reorder proposal into the procurement workflow (Volume 8 owns supplier terms; the 4–8 week China-direct lead time is priced into the min levels per Volume 4, §parts doctrine). Three-way match on receipt (§8.3). Stock counts: cycle-count tasks generated weekly for high-turnover bins (pinions, A-arms, tires per the digest's turnover ratings).

### 6.7 Battery lifecycle tracking

`battery_packs`: id, QR, chemistry/config (2S/3S per canon), capacity_mah, connector (XT60 canon), purchase_date, cycle_count, last_internal_resistance_mohm (per cell, JSONB), status (in_service/charging/resting/quarantine/retired). Every swap logs a cycle against pack QR + vehicle asset tag (Volume 4 checklist doctrine). Smart-charger integrations (SkyRC/ISDT-class with logging) or manual IR entry feed the IR trend; retirement triggers: cycle count > model threshold, IR rise > 40% from baseline, physical damage flag (→ quarantine crock per Volume 5 doctrine, then documented disposal). The bunker dashboard shows the 3:1 pool health per class: packs available vs. vehicles active — the morning number that predicts whether the afternoon keeps its Shift schedule.

### 6.8 Damage and incident reports

Marshal or Artisan files from the app: asset, category (collision/water/electrical/wear/customer-misuse), photos (Storage), Shift/customer linkage if applicable, cost estimate on close. Incident reports link to CCTV bookmarks (§11.4) and feed three consumers: the FMEA failure-data loop (Volume 7), insurance claims (documents module), and the customer-misuse flag on the CRM record (repeated deliberate abuse → license review per Volume 9).

## 7. Live Telemetry & IoT Platform

The telemetry platform is the system the park cannot open without. It carries the safety doctrine (kill on under-voltage <3.4 V/cell or geofence breach), the revenue doctrine (F1-style power management, lap timing), and the maintenance doctrine (runtime accrual). Design targets: **~150 concurrent nodes, 1 Hz standard payload, kill-command delivery inside a hard latency budget, graceful degradation when the mesh drops.**

### 7.1 Node payload and transport

RCW Node payload (per doctrine hardware: ESP32-C3, ATGM336H GPS, voltage divider): `{mac, seq, ts, lat, lng, speed, v_batt_mv, v_cell_mv[], pwm_state, rssi, fw_version}` — ~90 bytes packed. At 1 Hz × 150 nodes this is trivial bandwidth; the engineering problem is *connection churn* across mesh AP handoffs, not throughput.

**MQTT vs HTTP trade-off, decided:** the nodes speak **MQTT over TLS** to a broker fronting the Kotlin ingestion service.

| Criterion | MQTT | HTTP POST |
|---|---|---|
| Persistent session across AP handoff | ✔ resumes with session state | ✘ new TLS handshake per burst |
| Downlink (kill command) | ✔ broker push on subscribed topic, milliseconds | ✘ requires polling — unacceptable for kill latency |
| Power/CPU on ESP32-C3 | ✔ lightweight keep-alive | heavier per-message overhead |
| QoS semantics | ✔ QoS 1 for commands (at-least-once + dedupe by seq) | manual retry logic |
| Ops complexity | broker to run (managed EMQX/HiveMQ-class or self-hosted Mosquitto-class) | none extra |

Verdict: MQTT's downlink is the deciding factor — the kill-switch path needs push, not poll. The doctrine phrase "KILL command over Supabase Realtime" maps as follows: the *command originates* over Supabase Realtime (marshal app → `vehicle_commands` insert → Realtime notifies the rules engine and Grid View) and is *delivered to the node* over MQTT; the node also holds autonomous local kill logic (§7.4) so cloud latency is never the last line of defence.

### 7.2 Ingestion pipeline

```text
node ─MQTT─▶ broker ─▶ Kotlin ingestion service ─▶ batch INSERT (1 s window, COPY) ─▶ live_telemetry
                                    │                                                    │
                                    ├─▶ rules engine (in-memory hot state per vehicle)   ├─▶ Supabase Realtime
                                    │     geofence · voltage · lap timing · sag score    │     fan-out to Grid View,
                                    └─▶ node health registry (last_seen, rssi, fw)       │     customer HUD (own vehicle)
```

The ingestion service buffers one second of payloads and bulk-inserts — 150 rows/s as single-row inserts would be fine for Postgres but wasteful; batching keeps headroom for Phase 2 growth (~200 assets) and burst replays after mesh drops (nodes buffer up to 60 s of payloads in RAM and replay with original timestamps, flagged `replayed=true` so lap timing ignores them).

### 7.3 Time-series storage, downsampling, retention

`live_telemetry` is **partitioned by day** (native Postgres partitioning; a Timescale-class extension is the v2 upgrade path if Phase 2 volumes demand it). Retention policy:

| Tier | Resolution | Retention | Use |
|---|---|---|---|
| Raw | 1 Hz | 14 days | incident replay, lap-timing audit, engineering diagnosis |
| Downsampled | 1/60 Hz (per-minute min/avg/max voltage, distance, max speed) | 13 months | maintenance analytics, sag-score history, season leaderboard audit |
| Session aggregates | per Shift (distance, energy proxy, sag score, laps, kills) | 7 years | customer progression, finance, legal |

Downsampling runs as a nightly Edge Function-scheduled job; raw partitions older than 14 days are dropped (cheap, instant). Session aggregates write at Shift close into `shift_telemetry_summary` — the table every other module actually joins against.

### 7.4 Geofencing and the kill-switch path, with latency budget

Geofences are polygons per venue unit (`geofences` table, PostGIS-class geometry) with per-class overlays (crawler course boundary differs from the buggy line on shared terrain). Evaluation is two-layer, per doctrine:

1. **Node-local (authoritative for safety):** each node holds its assigned fence (simplified polygon, ≤32 vertices) and the under-voltage threshold, pushed at binding time. Breach or <3.4 V/cell → PWM intercept forces ESC to neutral/brake locally, then reports. **Cloud outage cannot disable the safety net.**
2. **Cloud (authoritative for operations):** the rules engine re-evaluates every payload — catches nodes with stale fences, drives Grid View alarms, and executes marshal-initiated commands.

Marshal kill-command latency budget (tap → wheels stop):

| Hop | Budget |
|---|---|
| Marshal app → Supabase (insert `vehicle_commands`) | ≤ 150 ms |
| Realtime → rules engine pickup | ≤ 100 ms |
| Rules engine → MQTT publish (QoS 1) | ≤ 50 ms |
| Broker → node delivery (mesh RTT) | ≤ 200 ms |
| Node PWM intercept actuation | ≤ 50 ms |
| **Total (p95)** | **≤ 550 ms; alarm if p95 > 800 ms over 5 min** |

The staging bench (§2.5) asserts this budget on every release. Node-local triggers actuate in <100 ms with no network at all.

### 7.5 Lap timing from geofence checkpoints

Tracks define ordered **checkpoint lines** (start/finish + 2–3 sector gates). The rules engine runs a per-vehicle state machine: crossing detection by segment intersection between consecutive GPS fixes, with sequence validation (a lap counts only if sectors pass in order — GPS jitter cannot fake a lap) and a minimum-lap-time sanity floor per track. Accuracy: GPS at 1 Hz gives ±1–2 s lap resolution — adequate for rental leaderboards and license progression, honest about its limits. League racing (Volume 3, Chapter 13) uses the dedicated transponder timing loop (MYLAPS/EasyLap-class); its API feeds `lap_times` through the same table with `source='transponder'`, so leaderboards blend both with the source badge visible. This honours Volume 5's precedent of external timing feeding RC WORLD OS.

### 7.6 Voltage-sag scoring

The F1-style energy game (doctrine): the rules engine computes a rolling **sag score** per Shift — the integral of (loaded voltage drop below open-circuit baseline) weighted by throttle-correlated speed changes. Smooth drivers score low sag, keep more usable capacity, and earn the "Smooth Operator" badge family (Volume 9); aggressive drivers see their energy bar drain faster on the HUD and may hit the soft-limit ladder: at sustained sag beyond class threshold → HUD warning → 20% throttle limit command (doctrine) → pit order. Per-class calibration tables live with the parity data (Volume 3) so the game is fair across vehicles.

### 7.7 Grid View

The operational fleet map (doctrine: real-time grid map): Mapbox/Google Maps SDK-class base with the park's own tile overlay (Volume 11 site plan), vehicles as class-coloured dots with voltage rings, geofence outlines, breach/kill flashes, queue depth per venue unit, and node-health badges (stale >5 s = amber, >30 s = red). Rendered in the staff app (marshal: own track; ops: whole park) and on the wall display in ops. Customer app renders a single-vehicle version — their bound vehicle only, RLS-enforced.

### 7.8 OTA firmware management

Nodes check a signed manifest on boot and daily: `firmware_releases` (version, target hardware A/B Micro/Heavy, binary in Storage, SHA-256, signature, rollout ring). Rollout rings: bench (staging nodes) → canary (5 park nodes, ops-selected quiet class) → fleet. A/B partition scheme on the ESP32-C3 with automatic rollback on failed boot health-check. Promotion between rings is an audited executive/lead action. A node never updates while `bound` or `on_track`.

### 7.9 Offline and degraded modes

| Failure | Behaviour |
|---|---|
| Single AP down | Nodes roam to neighbours (mesh doctrine); brief telemetry gaps back-filled from node RAM buffer |
| Mesh partition / broker unreachable | Node-local safety active (fence + voltage kill autonomous); nodes buffer 60 s and replay; marshals fall back to line-of-sight control per division SOPs; Shift clocks continue server-side |
| Internet down, park LAN up | Edge cache server (§13.2) keeps check-in, queue, POS, and Grid View running from local state; telemetry stores locally and syncs on restore |
| Full power loss | Vehicles' nodes still kill on voltage locally (powered downstream of main switch, doctrine); park emergency procedures (division volumes) take over |

> **Field Note.** The kill-switch's most likely real-world failure is not the network — it is a node whose fence never updated after a vehicle moved classes. The binding flow therefore *pushes and verifies* the fence at every QR bind (node echoes fence checksum before status may enter `bound`). A vehicle that cannot confirm its fence does not go on track. This one check eliminates the entire class of "wrong geofence" incidents.

## 8. Finance & Accounting Module

### 8.1 General-ledger-lite and export

RC WORLD OS runs a **GL-lite**: the double-entry ledger (§5.3) plus a chart-of-accounts mapping table, producing trial-balance-grade journals — but statutory books, tax, and audit live in a **Xero/QuickBooks-class** accounting system fed by a nightly journal export (API where available, reviewed CSV otherwise). The boundary is explicit: RC WORLD OS is the *operational* source of truth (every dollar traceable to a Shift, basket, or work order); the accounting package is the *statutory* source of truth. The mapping table is finance-manager-maintained and version-controlled; unmapped account activity blocks the export and pages finance rather than silently mis-posting.

### 8.2 Revenue recognition per product type

| Product | Recognition rule | Ledger mechanics |
|---|---|---|
| Casual/Operator Shift | On delivery (Shift completed) | Sale posts to `deferred_revenue:shifts`; clock completion releases to `revenue:shifts` (§5.3 example) |
| Day Pass / bundles | On visit day, allocated across components | Deferred at sale; released at first check-in of the visit day |
| Memberships (Apprentice $29 / Operator $59 / Foreman $99) | Ratably over month (MRR) | Monthly charge → `deferred_revenue:memberships`, daily release job; churn analytics read the same rows |
| Packages / multi-Shift credits | Per Shift consumed; breakage on expiry | Credit sits in wallet sub-account; expiry sweeps to `revenue:breakage` per published T&Cs |
| Wallet loads | **Never revenue** | Pure liability until spent — the discipline the control account enforces |
| Corporate events / parties | On event delivery; deposits are liabilities | Deposit → `customer_deposits`; delivery releases full contract value |
| Retail / F&B | At sale | Direct to revenue with COGS posting from stock module |

### 8.3 Accounts payable and procurement link

Supplier invoices (Volume 8 suppliers) enter by upload or email-in; the AP workflow runs **three-way match**: purchase order (from the reorder flow, §6.6) ↔ goods receipt (Works receiving scan) ↔ invoice. Matched invoices queue for payment per §3.7 approvals; mismatches route to procurement with the delta highlighted. Landed-cost allocation (freight, duty on China-direct consolidations) spreads across receipt lines so `parts_stock` unit costs stay honest — Volume 8's landed-cost methodology, executed here.

### 8.4 Budgeting vs. actuals

Budgets load per site × department × month (finance console, versioned; Volume 10's model is the source). Actuals accrue from the ledger automatically. Division leads see their own budget line (§3.2); variance beyond threshold flags on the executive dashboard. No spreadsheet round-trips: the budget lives where the actuals live.

### 8.5 KPI dashboard as queries

Volume 10's KPI set is defined *as SQL against this schema* so every number on the executive wall is reproducible:

| KPI | Definition (schema terms) |
|---|---|
| RevPASH-style utilization | `revenue:shifts` per venue-unit-hour open: Shift revenue ÷ Σ(venue_unit open hours × capacity), from `session_slots` × ledger |
| Maintenance cost per vehicle-hour | (work-order parts at landed cost + labour minutes × loaded rate) ÷ Σ `total_hours_run` delta, per class per month |
| Membership churn | memberships lapsed in month ÷ active at month start, from membership ledger releases; cohort view by join month |
| Wallet liability & breakage | `wallet_liability_control` balance; breakage sweep trend |
| Fleet availability | time-in-status share of `available`+`bound`+`on_track` vs. `maintenance` per class (from status-transition intervals, §6.3) |
| 90-day second-visit rate (Volume 2 canary) | customers with ≥2 visit days within 90 days of first ÷ first-visit cohort |
| Battery pool health | packs in service ÷ (vehicles active × 3) per class — the 3:1 doctrine as a live number |

Each KPI ships as a versioned SQL view; the dashboard renders views, never ad-hoc queries — when a definition changes, the view changes in a reviewed migration and every consumer moves together.

## 9. HR & Payroll Module

### 9.1 Staff records, contracts, certifications

`staff_profiles` extends the auth user with employment data: position, department/division, start date, contract type, emergency contacts; compensation isolated per the column-privacy pattern (§3.5). Contracts and signed documents live in Storage against the record with e-signature capture. **Certifications** are the compliance backbone: every credential from the Volume 12 Academy — Artisan platform certifications (Volume 7 rebuild sign-offs), marshal safety tickets, LiPo-handling and bunker certification, first aid, FPV spotter rating (Volume 5), waders/water-work sign-off (Volume 6) — is a row with issue/expiry dates and evidence upload. The scheduler will not roster a staff member into a slot whose venue unit requires a certification they lack or that expires before the shift ends; expiring certs alert the staff member at T-30/T-14/T-7 days and the HR dashboard continuously.

### 9.2 Safety-training records

Toolbox-talk attendance (the staff kind, distinct from the customer induction), incident-response drills, and division safety briefings log against profiles with read-acknowledgement where the content is a document (§11.5). The insurer-facing export — "show me every marshal's current safety record" — is one filtered report, which Volume 5's regulator-evidence table anticipates.

### 9.3 Rostering against forecast demand

The roster builder plans marshals, Artisans, FOH, and F&B against **forecast demand**: booking curves (advance bookings by day/hour), historical walk-up patterns by weekday/season/weather, and the events calendar. Ops managers see a demand heat-map per venue unit and drag staff into shift slots; the engine validates certifications, rest rules (minimum 11 h between shifts, configurable per jurisdiction), and cost against the labour budget line live. Published rosters push to staff apps; swap requests route peer→lead approval. The capacity feedback loop (§4.5) means an unfilled marshal slot automatically caps that track's sellable Shifts — the roster is not advisory.

### 9.4 Time & attendance

Clock-in/out happens in the staff app with a **geofence check** (device inside the park polygon; Core Location / FusedLocation per platform) plus the venue-unit check for track roles. No biometric hardware in v1 — the phone, the geofence, and the roster cross-check (clock-in without a rostered shift flags to the lead) are sufficient controls at this scale. Missed punches resolve through a lead-approved correction flow, audited.

### 9.5 Payroll: compute locally, process externally

The payroll boundary mirrors the accounting boundary: **RC WORLD OS computes; a local payroll processor pays and files.** The payroll calculator (Kotlin service) assembles each period: rostered vs. actual hours from time & attendance, overtime per configured rules (daily/weekly thresholds, penalty rates for late-night race events), allowances (bunker duty, wet-work), leave accruals and deductions. HR reviews the computation sheet per employee with variance-to-last-period highlighting; finance releases (§3.7 separation); the export file goes to the payroll processor in its import format. Processor output (net pay, taxes, employer contributions) posts back as a GL journal. This "process locally, verify locally" framing keeps jurisdiction-specific tax logic — the part that changes with every local election — out of our codebase entirely, which matters double for franchising: each franchise site plugs in its own local processor without touching platform code.

### 9.6 Performance reviews

Lightweight and evidence-linked: review cycles per role family, self + lead assessment, and auto-attached operational evidence — an Artisan's closed work orders and rework rate, a marshal's incident-response log, FOH transaction accuracy. Reviews inform the Academy development plan (Volume 12) rather than a forced ranking; the schema stores them under HR-only RLS.

## 10. CRM, Marketing & Gamification Module

### 10.1 Customer 360

One customer record aggregates: identity and consent state, visit days (from check-ins), lifetime and 12-month spend by category (ledger), current wallet/Gears balances, membership status, **RC WORLD License tier**, badge case, bound-vehicle history, incident/misuse flags, marketing segment memberships, and guardian links. FOH sees the thin card (name, tier, today's bookings, flags); marketing sees segments; only the customer sees everything. The 360 is a view over module tables — never a copied "CRM database" that drifts from the truth.

### 10.2 The progression engine

Volume 9's design, implemented as data-driven rules evaluated by the rules engine on telemetry and transactional events:

- **XP rules** (`xp_rules` table): event type → XP, with per-day caps and class multipliers. Events: Shift completed, lap improvement vs. personal best, tonnage delivered to the hopper (Construction), mission completed (Marine harbour master), retrieval protocol piloted successfully, low sag score band, race podium.
- **Tier evaluation:** license tiers (Volume 9 catalogue) evaluate on XP thresholds *plus* gate requirements (e.g. a clean-driving criterion: no geofence kills in last N Shifts; a skills check-off by a marshal for premium classes). Evaluation runs at Shift close; promotions celebrate in-app and unlock booking classes (§4.5) and transmitter EPA profiles (Volume 3, §12.1).
- **Badge triggers:** declarative predicates over `shift_telemetry_summary` and event streams — "Night Owl" (5 night-race Shifts), "Smooth Operator" (sag score < threshold, 10 Shifts), "Excavator Foreman" (100 t lifetime tonnage), "Tow Master" (10 retrievals). Badges are additive and never revoked; the criteria JSONB is versioned so historical awards stay explicable.

**Leaderboards:** per track/class daily, weekly, season; per zone (tonnage, missions); global. Computed from `lap_times` and summaries into materialized boards refreshed on event, pushed via Realtime to app and track-side displays. Display names are customer-chosen handles with profanity screening; minors appear only per guardian visibility settings.

### 10.3 Campaigns and automations

Segmentation over the 360 (visit recency/frequency, spend band, tier, division affinity, distance from park) drives push (FCM/APNs) and email (SES/Postmark-class) campaigns. Automations shipped in v1.5: birthday offer (guardian-mediated for minors), win-back at 45/90 days dormant, post-first-visit sequence, membership renewal risk (usage-decline signal), event announcements by division affinity. Every send is consent-checked at dispatch time, not at segment build time.

### 10.4 Season passes and entitlements

Season passes and memberships materialize as **entitlement rows** (type, period, remaining allowance, constraints) that the pricing engine (§4.6) consumes. Entitlement usage is a ledger event, so finance sees membership utilization without a reconciliation project, and Volume 9's economics (allowance breakage, upgrade paths) read straight from the data.

### 10.5 Consent and privacy (GDPR-class)

- Consent ledger per purpose (transactional, marketing push, marketing email, photo/media, telemetry-derived gamification), timestamped, versioned against the privacy-policy revision; withdrawal is one tap and effective at next dispatch.
- Data subject rights: export (JSON bundle of the customer's rows) and erasure (anonymize identity, retain de-identified transactional/telemetry aggregates required by finance law) as built-in admin workflows, not engineering favours.
- Data minimization: telemetry is vehicle-keyed and joins to customers only through session binding; marketing never receives raw telemetry.

### 10.6 Minors' data policy

Minors under the local digital-consent age get **no independent account**: a guardian creates a linked minor profile (first name + birth year only), signs the waiver, holds all consents, sets spend caps, and controls leaderboard visibility (default: handle-only, no photos). Progression accrues to the minor profile and migrates to a full account at age of consent with guardian handover. Staff-facing screens show minors with a guardian badge; marketing automations never target minor profiles directly.

## 11. Additional Modules

### 11.1 Retail & F&B POS and stock

The POS surfaces (§5.4) sit on catalogue + stock: retail SKUs (Volume 8's retail range: parts, merch, starter RC kits) and F&B items with recipe-level stock decrement (a flat white decrements beans, milk, cup). Stock features: goods receipt against PO, cycle counts, wastage logging (F&B), min/max reorder into procurement, margin reporting by SKU to finance. Kitchen order screen for the Phase 2 restaurant; the Phase 1 kiosk runs order-and-collect with buzzer numbers.

### 11.2 Corporate events pipeline

A lightweight pipeline CRM for the events business (from $1,400/2 h anchor): enquiry → qualified → proposal (templated from package configurator) → deposit paid (→ bookings hold, §4.2) → confirmed → delivered → invoiced/closed. Stages carry tasks (run-sheet, catering brief, marshal roster block); conversion and pipeline value report to the executive dashboard. Loses record a reason code — the marketing feedback loop Volume 2 asks for.

### 11.3 Access control integration

Entry gates read the booking/day-pass QR or an NFC wristband (issued at FOH, mapped to the customer session — wristbands suit wet zones and children). Gate controllers (commodity QR/NFC turnstile-class hardware) call a local validation endpoint on the edge server (offline-tolerant, §13.2) which checks entitlement (valid booking today, day pass, member) and logs the movement. Zone-level gates (bunker, The Works, pit lane) run staff-credential NFC with role checks — the physical mirror of RLS.

### 11.4 CCTV / incident integration

CCTV stays on its own VMS (network video recorder-class, Volume 11 specifies coverage); RC WORLD OS integrates at the *bookmark* level: an incident report (§6.8), a kill event, or a marshal flag calls the VMS API to bookmark ±90 s across the venue unit's cameras, storing the bookmark reference on the incident. Footage never enters our Storage except as exported evidence clips attached to a closed incident (retention per §13.6). This keeps video privacy surface small and the integration vendor-swappable.

### 11.5 Document management for SOPs

Every SOP, checklist, and manual section from Volumes 3–8 lives as a versioned document: owner, revision, effective date, distribution list by role/site. **Read-acknowledgement tracking** is the operational point: publishing a revised SOP-MS-002 pushes a task to every affected role; the compliance board shows who has not acknowledged; rostering can require current acknowledgements for safety-critical SOPs the same way it requires certifications (§9.1). Franchise doctrine documents publish read-only to franchisee sites with local-annex support (Volume 12's mandatory-vs-adaptable split, executed).

### 11.6 Franchise multi-tenancy

The architecture is site-scoped from day one (§1.4); v2 activates the network features:

- **Partitioning:** every business table carries `site_id`; RLS fences all franchise roles to own sites. Telemetry partitions per site per day. Site-level data export supports a departing franchisee's wind-down obligations (Volume 12).
- **Franchisor cross-site dashboards:** the executive/franchisor role reads network rollups — same-site revenue growth, utilization, safety incident rates, compliance scores (SOP acknowledgements, cert currency, PM on-time %) — the operational royalty audit Volume 12 defines, computed continuously instead of annually.
- **Per-site configuration:** pricing bands (above franchisor floors), local tax and payroll processor bindings, opening calendars, local vehicle-class mix — all configuration rows, not code branches. Doctrine tables (PM matrices, safety rules, XP rules) publish from the franchisor with site-level read-only enforcement.
- **Tenancy hygiene:** shared platform, shared schema, fenced rows. A single-site franchisee's traffic cannot see or starve another site's; per-site rate limits and per-site Realtime channels enforce the isolation operationally as well as logically.

> **Field Note.** The most common multi-tenant mistake is retrofitting `site_id` after launch — a months-long migration through every query and policy. The second most common is *forking* per site "temporarily". This plan avoids both by decree: `site_id` is in every business table from migration 0001, and there is exactly one production codebase. Franchisees get configuration, never branches.

## 12. Data Model

### 12.1 How to read this chapter

This is the consolidated schema reference: the doctrine tables (`fleet_inventory`, `live_telemetry`, `maintenance_logs`, `queue_roster`) extended into the full entity-relationship design, ~30 core tables grouped by module. Conventions: every table has `id` (UUID or bigint identity), `site_id` (bigint, FK `sites`), `created_at`/`updated_at`; money is `numeric(12,2)` USD; enums are Postgres enums with migration-managed values; soft deletes only where legal retention demands (`revoked_at`/`deleted_at`), never on ledger or audit tables.

**ERD in prose.** `sites` roots everything. Identity: `user_site_roles` links auth users to roles per site; `staff_profiles` and `customer_profiles` extend users; `guardian_links` connects guardians to minor profiles. Commercial spine: `venue_units` → `session_slots` → `bookings` → `shifts`; `queue_roster` hangs off venue_unit + vehicle class. Money: `ledger_transactions` → `ledger_entries` → `ledger_accounts`; `payments` and `refunds` reference PSP objects and post through the ledger. Fleet: `vehicle_models` → `fleet_inventory` → (`asset_components`, `battery_packs` via swap logs, `work_orders` → `maintenance_logs`, `status_transitions`). Telemetry: `fleet_inventory` → `live_telemetry` (partitioned) and `shift_telemetry_summary`; `geofences` and `checkpoints` belong to venue_units; `vehicle_commands` and `node_registry` complete the IoT loop. A `shift` is the junction where everything meets: customer, booking, vehicle, telemetry summary, ledger postings, XP events.

### 12.2 Core table listing

**Identity & access**

| Table | Key columns | Relationships / notes |
|---|---|---|
| `sites` | name, timezone, status, franchisee_org_id | Root of tenancy |
| `user_site_roles` | user_id, site_id, role, granted_by, revoked_at | RBAC truth (§3.4) |
| `customer_profiles` | user_id, handle, birth_year, license_tier, consent JSONB | 1:1 auth user |
| `guardian_links` | guardian_id, minor_id, spend_cap, visibility | §10.6 |
| `staff_profiles` | user_id, position, division, contract refs | Compensation in separate table |
| `audit_log` | actor, role, action, entity, diff JSONB, device, ip | Append-only (§3.6) |

**Bookings & scheduling**

| Table | Key columns | Relationships / notes |
|---|---|---|
| `venue_units` | site_id, division, name, geometry ref | Track A, Mining pod 1… |
| `vehicle_classes` | division, name, premium flag, license_tier_required | |
| `session_slots` | venue_unit_id, class_id, block_start, capacity, price_band | Generated 28 d ahead (§4.1) |
| `bookings` | customer_id, slot_id (or group_booking_id), state, price_breakdown JSONB | Doctrine flows §4.2 |
| `group_bookings` | type (corporate/party), window, deposit ref, run_sheet | |
| `queue_roster` | customer_id, class_id, venue_unit_id, joined_at, state | **Doctrine table** — T-5 Top-Up reads it |
| `shifts` | booking_id, vehicle_id, clock events, state, top_up_count | The atomic delivered unit |

**Payments & ledger**

| Table | Key columns | Relationships / notes |
|---|---|---|
| `ledger_accounts` | code, type, site scope | Chart §5.3 |
| `ledger_transactions` | type, reference, initiator, occurred_at | |
| `ledger_entries` | transaction_id, account_id, direction, amount, currency | Zero-sum constraint |
| `payments` | psp_token, method, amount, state, psp_ids | Tokens only — no PANs (§5.6) |
| `refunds` | origin, amount, state machine, initiator, approver | §3.7 duties |
| `entitlements` | customer_id, type, period, remaining, constraints | Memberships/passes (§10.4) |

**Fleet, maintenance & telemetry**

| Table | Key columns | Relationships / notes |
|---|---|---|
| `vehicle_models` | class_id, make/model, scale, wholesale_cost, spares_profile | Volume 8 catalogue link |
| `fleet_inventory` | mac_address, asset_tag, model_id, status, total_hours_run, total_shifts | **Doctrine table**, status extended §6.3 |
| `status_transitions` | vehicle_id, from, to, actor, at | Utilization analytics |
| `battery_packs` | qr, config, cycle_count, ir_trend JSONB, status | 3:1 pool (§6.7) |
| `work_orders` | vehicle_id, type, priority, tasks, state, signoff | PM engine output |
| `maintenance_logs` | vehicle_id, mechanic_id, parts_used JSONB, description, date_resolved | **Doctrine table**, unchanged |
| `parts_stock` | sku, bin, qty, min/max, landed_cost, lead_time | Reorder → procurement |
| `pm_rules` | model/class, metric, threshold, task_template | Volume 7 matrices as data |
| `live_telemetry` | vehicle_id, ts, lat, lng, speed, voltage fields, pwm_state | **Doctrine table**, partitioned daily |
| `shift_telemetry_summary` | shift_id, distance, sag_score, laps, kills, energy proxy | 7-year retention |
| `geofences` / `checkpoints` | venue_unit_id, geometry, class overlays / ordered lines | §7.4–7.5 |
| `vehicle_commands` | vehicle_id, command, issuer, issued_at, acked_at | Append-only, RLS pattern 3 |
| `node_registry` | mac, hw form factor, fw_version, last_seen, rssi | OTA + health |
| `firmware_releases` | version, target, sha256, signature, ring | §7.8 |
| `incidents` | category, refs (shift/vehicle/customer), photos, cctv_bookmarks | §6.8, §11.4 |

**Finance, HR, CRM, ops**

| Table | Key columns | Relationships / notes |
|---|---|---|
| `suppliers` / `purchase_orders` / `goods_receipts` / `supplier_invoices` | three-way-match keys | §8.3, Volume 8 |
| `budgets` | site, department, month, amount, version | §8.4 |
| `staff_compensation` | staff_id, pay basis, rates | Column-privacy table (§3.5) |
| `certifications` | staff_id, type, issued, expires, evidence ref | Roster gate (§9.1) |
| `roster_shifts` / `time_entries` | slot, staff, venue_unit / clock events, geofence result | §9.3–9.4 |
| `payroll_runs` | period, computation snapshot, reviewed_by, released_by | Export boundary (§9.5) |
| `xp_rules` / `xp_events` / `badges` / `badge_awards` | rule predicates JSONB; event stream; award refs | §10.2 |
| `lap_times` | shift_id, lap, time_ms, source (gps/transponder) | Blended leaderboards (§7.5) |
| `segments` / `campaigns` / `consents` | definitions; sends; per-purpose ledger | §10.3, §10.5 |
| `products` / `stock_items` / `pos_baskets` | retail/F&B catalogue, recipe decrement, basket lines | §11.1 |
| `event_pipeline` | stage, value, tasks, reason codes | §11.2 |
| `documents` / `doc_acknowledgements` | revision, owner, distribution / user, doc, at | §11.5 |
| `entry_scans` | credential, gate, result, at | §11.3 |

### 12.3 Schema governance

The digest's original `fleet_inventory` status enum (active/maintenance/charging) is formally superseded by the seven-state machine in §6.3 — this volume states so explicitly per the living-document rule; `active` maps to `available|bound|on_track|pit`. All other doctrine columns are preserved verbatim. Schema changes ship only as reviewed migrations with RLS tests; any volume that binds to a table name (Volumes 3–6 reference `maintenance_logs` and `fleet_inventory` extensively) is protected by this governance: those names and their doctrine columns are frozen APIs.

## 13. Non-Functional Requirements & Operations

### 13.1 Availability targets

| Service | Target | Rationale |
|---|---|---|
| Node-local safety (kill on fence/voltage) | Always — no network dependency | Doctrine; life-safety adjacent |
| Telemetry pipeline + Grid View | 99.5% during park hours | Marshals fall back to line-of-sight SOPs below this |
| Bookings/check-in/POS | 99.5% park hours (with edge degraded mode below) | Revenue path |
| Web console / back office | 99% business hours | Tolerates maintenance windows |
| App availability | Store-distributed; offline-tolerant caches for tickets/QRs | A booking QR must render with no signal |

### 13.2 Edge resilience: the park cache server

One small on-prem server (redundant pair by Phase 2) runs at the ops room: local MQTT broker mirror, a read replica of hot operational tables (today's bookings, queue, fleet status, catalogue), and a write-ahead queue for check-ins, POS sales, and clock events. When the WAN drops, FOH keeps checking in, POS keeps selling (PSP offline rules for cards, unconditional for cash/wallet-cached), marshals keep Grid View from the local broker, and telemetry buffers locally. On restore, the queue replays with idempotency keys; conflicts (a slot double-sold across the partition) resolve by policy: honour both, flag to ops, comp the overflow — never argue with a customer at the gate over a sync conflict.

### 13.3 Backups and disaster recovery

Supabase point-in-time recovery on Postgres; nightly logical dumps to independent object storage in a second region; Storage (documents, photos, firmware) versioned + replicated. Targets: **RPO ≤ 5 minutes** (WAL-based) for transactional data, ≤ 24 h acceptable for raw telemetry (safety does not depend on history); **RTO ≤ 4 hours** to full back-office, ≤ 1 hour to park-operational (bookings/POS/telemetry) using the runbook-scripted restore. DR drill twice yearly against a scratch project, timed and reported to the executive dashboard like any other KPI.

### 13.4 Observability

Structured logs (correlation ids across app → service → DB), metrics (ingestion rate, command latency p95 vs. the §7.4 budget, queue depths, RLS-denial counts, wallet-invariant check), and alerting to the on-call rotation (platform run team, §2.7) via a PagerDuty-class escalation. Golden alarms: kill-command p95 breach, wallet control drift ≠ 0, node fleet stale >10%, PSP webhook failures, backup job failure. Each golden alarm has a written runbook in the documents module — the platform documents itself with its own SOP machinery.

### 13.5 Security hardening

Secrets in a managed secrets store (cloud KMS-class), never in repos or client binaries; quarterly key rotation. Dependency and container scanning in CI; signed firmware (§7.8); MDM-enrolled kiosk devices; least-privilege service keys per machine identity (§3.1 role 14). **Penetration test cadence:** external test before public launch, then annually and after any auth/payment architecture change; scope always includes the RLS layer (attempt cross-tenant and cross-role reads) and the MQTT/OTA path (attempt command injection and firmware substitution). Findings feed the same risk register as §14.4.

### 13.6 Data retention schedule

| Data | Retention | Basis |
|---|---|---|
| Financial ledger, invoices, payroll exports | 7 years | Statutory |
| Audit log (financial actions) / (other) | 7 / 3 years | §3.6 |
| Raw telemetry / downsampled / Shift summaries | 14 days / 13 months / 7 years | §7.3 |
| CCTV bookmarks & evidence clips | 90 days; incident-attached until case closes + 2 years | Insurance |
| Customer PII after erasure request | Anonymized immediately; ledger rows retained de-identified | GDPR-class |
| Marketing consent records | Life of consent + 3 years | Proof of consent |
| Staff records post-employment | Per jurisdiction (default 6 years) | Local labour law, per-site config |

### 13.7 Change management and release operations

The park runs seven days a week; the platform changes under it. Release rules: schema migrations deploy in the park's closed hours (with the two-phase expand/contract pattern for anything touching a hot table — add column, backfill, switch readers, drop later); app releases ride store review cycles, so every server change stays backward-compatible with the previous two app versions (enforced by contract tests against pinned older specs); feature flags gate anything customer-visible so a launch is a flag flip at 9 a.m. with the team watching dashboards, not a deploy at midnight with the team asleep. Firmware follows its own ring discipline (§7.8). A one-page change calendar in the ops day board tells the duty manager what changed this week — half of "the system is acting weird" reports resolve by looking at that page.

### 13.8 Scalability path

One site at 150 assets and ~1,500 daily visitors runs comfortably on a mid-tier Supabase instance and two service containers. Scaling levers, in order of need: read replicas for dashboards; Timescale-class extension for telemetry (Phase 2, ~200 assets); per-site MQTT brokers at franchise sites feeding the shared cloud; regional deployment split only if a franchise cluster lands on another continent (Volume 12's international scenario). Nothing in the design requires re-architecture before ~10 sites.

## 14. Implementation Roadmap

### 14.1 Release strategy

Three releases mapped to park phasing: **v1 (MVP)** must be live for Phase 1 opening (Month 12 at the latest; target Month 10 for two months of staff rehearsal); **v1.5** lands Months 13–20; **v2** lands Months 21–36 alongside the Phase 3 franchise pilot. MVP scope per the founder's cut: bookings, wallet + payments, telemetry + kill-switch, fleet + maintenance, POS, RBAC core — plus the Toolbox Talk, without which no booking can legally complete.

### 14.2 Sprint-level breakdown (v1: 11 two-week sprints ≈ 5.5 months, then hardening)

| Sprint | Theme | Key deliverables |
|---|---|---|
| 0 | Foundations | Repos, CI/CD, environments, schema migration 0001 (sites, identity, RBAC tables), design system, KMP app shells on both stores' internal tracks |
| 1 | RBAC core | Auth flows, role provisioning, RLS pattern library + pgTAP harness, role-scoped navigation skeleton |
| 2 | Telemetry ingest | MQTT broker, ingestion service, `live_telemetry` partitioning, node bench integration, Grid View alpha |
| 3 | Kill-switch & geofence | Command path end-to-end, node fence push/verify at bind, latency-budget test in CI, marshal screen |
| 4 | Fleet & maintenance | Registry, status machine, QR binding, work orders, `maintenance_logs`, parts stock |
| 5 | Bookings I | Inventory generation, capacity rules, app booking flow, Toolbox Talk module, waivers |
| 6 | Payments & wallet | Ledger service + invariants, PSP integration, Apple Pay/Google Pay, wallet load/spend, reconciliation job |
| 7 | Bookings II + queue | `queue_roster`, walk-in kiosk, T-5 Top-Up flow, Shift clocks, breakdown pause + auto-credit |
| 8 | POS & check-in | FOH kiosk mode, retail/F&B POS, card terminals, cash drawer, entry QR validation on edge server |
| 9 | Lap timing & customer HUD | Checkpoint engine, sag score v1, live HUD, leaderboards v1, basic XP/badges |
| 10 | Back office v1 | Finance console (ledger views, refund queue, GL export v1), ops day board, roster v1, staff clock-in |
| 11–13 | Hardening | Load test at 150 nodes, offline drills, pen test + fixes, DR drill, staff-app rehearsal content, store review buffer |

v1.5 (six sprints): payroll computation + processor export, certification compliance + Academy integration, AP three-way match, budgets vs. actuals, CRM automations, season pass entitlements, document read-acknowledgement. v2 (eight sprints): franchise tenancy activation + franchisor dashboards, per-site config packs, advanced analytics/BI extracts, Timescale-class telemetry migration, Phase 2 division features (aviation weather-minima automation, marine mission scoring), corporate events pipeline v2.

### 14.3 Team composition through the roadmap

The §2.7 build team (6.5 FTE) covers v1. v1.5 runs at 4 FTE (payroll/finance depth is backend + web heavy). v2 returns to ~5 FTE with a data engineer added for analytics. The firmware engineer's 0.5 FTE is shared with The Works throughout — node hardware and firmware are one budget line and one owner, avoiding the classic split-brain between "the PCB team" and "the app team".

### 14.4 Software program risk register

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| R1 | Kill-command latency misses budget on real mesh | M | H | Node-local safety is primary (design); staging bench asserts budget every release; AP density survey in Volume 11 build |
| R2 | App Store rejection/delay (kill-switch, stored value) | M | H | Reviewer dossier prepared early (§2.1 Field Note); TestFlight external review two sprints before launch need |
| R3 | Wallet ledger defect → liability drift | L | H | Single-writer ledger service, zero-sum constraint, nightly invariant alarm, property-based tests on posting logic |
| R4 | RLS policy gap leaks cross-role/tenant data | M | H | pgTAP deny-tests mandatory per policy; pen-test scope includes RLS; no service-role key in clients |
| R5 | GPS lap-timing accuracy disappoints racers | H | M | Positioned honestly as rental-grade; transponder loop for leagues (§7.5); expectation set in Volume 9 UX |
| R6 | Scope creep from division wish-lists pre-opening | H | M | MVP cut is founder-signed (this chapter); post-MVP requests enter the v1.5 backlog, not the launch plan |
| R7 | Single-vendor dependence (Supabase) | L | M | Plain Postgres + SQL migrations = portable core; Realtime/Auth abstractions isolated behind interfaces |
| R8 | Key-person loss (tech lead) | M | M | This volume + ADR log + runbooks as institutional memory; code review discipline; no unshared credentials |
| R9 | Payroll/tax misconfiguration at a franchise site | M | M | Process-locally boundary (§9.5): local processor owns tax; launch checklist requires processor sign-off |
| R10 | Mesh coverage gaps discovered post-build | M | H | RF survey milestone in Volume 11 construction schedule *before* surfacing; node buffer + replay masks brief gaps |

> **Investor Note.** The software line is ≈10% of Phase 1 capex and it is the multiplier on the other 90%: utilization (bookings + queue), asset life (predictive maintenance), spend per visit (wallet + gamification), and franchisability (a platform, not a park, is what franchises). The MVP cut above is the minimum that opens the gates; every v1.5/v2 item has a named revenue or margin mechanism behind it in Volumes 9, 10 and 12.

## 15. Volume Summary & Cross-References

RC WORLD OS is the single operating system of the business: one PostgreSQL schema under Row Level Security, Kotlin services for telemetry/rules/ledger/payroll compute, Kotlin Multiplatform + Compose Multiplatform apps on **both Android and iOS**, and a web admin console — with a build-vs-buy line that keeps custom engineering on the differentiators (telemetry, bookings, gamification, wallet) and buys the commodities (card processing, statutory accounting, payroll filing). The founder's central requirement is delivered as architecture: a fourteen-role catalogue with per-module permission matrices, role-scoped interfaces specified screen by screen, RLS policy patterns with tested SQL, separation of duties on every financial action, and an append-only audit trail. The doctrine systems are implemented exactly — the 20-minute Shift as atomic inventory, the T-5 Top-Up against `queue_roster`, PWM-intercept kill on under-voltage/geofence with a ≤550 ms p95 command budget and node-local autonomy, the breakdown protocol's paused clocks and auto-credits, predictive maintenance from runtime hours — and the schema chapter extends the doctrine tables into a governed model of ~30 core tables (plus supporting tables) whose doctrine names are frozen APIs. Non-functional commitments (edge degraded mode, RPO ≤5 min/RTO ≤4 h, retention schedule, pen-test cadence) and an 11-sprint MVP roadmap with team, budget (≈$185k v1 inside Volume 10's software line) and risk register complete the program.

**Decisions this volume establishes for other volumes** (living-document notices): client apps are KMP/CMP on Android **and** iOS, extending the digest's Android-only statement; `fleet_inventory.status` is the seven-state machine of §6.3, superseding the three-state enum; telemetry transport is MQTT with Supabase Realtime as the command origination and fan-out layer; the wallet is a double-entry ledger and wallet loads are never revenue.

**Cross-references.**

- **Volume 3** — Motorsport: parity data behind sag-score calibration; transponder league timing feeding `lap_times`; transmitter EPA profiles gated by license tier.
- **Volume 4** — Construction: Heavy-Node fleet, tonnage crediting, pod-linked 1:3 slot model, grooming blackouts feeding capacity.
- **Volumes 5–6** — Aviation/Marine: weather-minima feeds into the capacity engine; external timing precedent; incident and retrieval doctrine implemented in Shift lifecycle.
- **Volume 7** — Engineering & Workshop Manual: PM matrices loaded as `pm_rules`; work-order sign-off handshake; RCW Node build and conformal-coating doctrine.
- **Volume 8** — Procurement: supplier catalogue, landed-cost methodology, reorder linkage from `parts_stock`.
- **Volume 9** — Customer Experience & Loyalty: License tiers, XP/badge/Gears rules the progression engine executes; membership economics behind entitlements.
- **Volume 10** — Finance: source of truth for the software budget line, KPI definitions (§8.5 implements them as SQL), revenue model the recognition rules serve.
- **Volume 11** — Architecture & Park Design: mesh AP placement and RF survey, conduit and timing-loop provisions, ops room and edge-server housing, CCTV coverage.
- **Volume 12** — Franchise Manual: multi-tenancy features (§11.6), doctrine publication, per-site payroll/tax boundary, platform licensing terms.




