# RC WORLD — Master Development Plan: Volume Map

Twelve volumes plus front matter build into the complete master plan. Each volume is a
standalone markdown file, written to `style-guide.md` and consistent with
`source-material/original-notes-digest.md`.

| # | File | Title | Word target | Page est. |
|---|---|---|---|---|
| 0 | `volume-00-front-matter.md` | Front matter, how to use this plan, master TOC | 2,500 | 8 |
| 1 | `volume-01-executive-master-plan.md` | Executive Master Plan | 14,000 | ~42 |
| 2 | `volume-02-market-research.md` | Market Research & Competitive Landscape | 15,000 | ~45 |
| 3 | `volume-03-motorsport-division.md` | RC Motorsport Division | 16,000 | ~48 |
| 4 | `volume-04-construction-division.md` | RC Construction Division | 14,000 | ~42 |
| 5 | `volume-05-aviation-division.md` | Aviation Division | 12,000 | ~36 |
| 6 | `volume-06-marine-division.md` | Marine Division | 12,000 | ~36 |
| 7 | `volume-07-engineering-workshop-manual.md` | Engineering & Workshop Manual | 20,000 | ~60 |
| 8 | `volume-08-procurement-handbook.md` | Procurement Handbook | 18,000 | ~54 |
| 9 | `volume-09-customer-experience.md` | Customer Experience & Loyalty | 12,000 | ~36 |
| 10 | `volume-10-finance.md` | Finance | 15,000 | ~45 |
| 11 | `volume-11-architecture-park-design.md` | Architecture & Park Design | 18,000 | ~54 |
| 12 | `volume-12-franchise-manual.md` | Franchise Manual | 13,000 | ~39 |
| 13 | `volume-13-it-iot-erp.md` | IT, IoT & ERP Systems (RC WORLD OS) | 16,000 | ~48 |

Combined target ≈ 196,000 words ≈ **440–490 finished pages** (at ~400 words/page, tables and
checklists set denser).

## Build

`python3 build/assemble.py` concatenates all volumes into
`build/RC-WORLD-Master-Development-Plan.md`, prints per-volume word counts and estimated page
counts, and (if `pandoc` is installed) renders `build/RC-WORLD-Master-Development-Plan.docx`
and `.pdf`.

## Living-document workflow

- One volume = one file = one review unit. Update volumes independently as suppliers, products
  or plans change; bump the revision line in each volume's header block.
- Keep `style-guide.md` as the single source of canonical numbers. If a canonical number changes
  (pricing, fleet counts, capex), change it there first, then sweep volumes.
