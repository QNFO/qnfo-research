# Phase 3 Citation Audit Report — The Informational Universe

**Date:** 2026-07-21  
**Phase:** 3 (Citation Management)  
**Protocol:** research v2.10 §Phase 3

---

## Citation Audit Summary

| Metric | Count |
|:-------|------:|
| Core arXiv (Phase 2 auto-fetched) | 20 |
| Core arXiv (manual — rate-limited) | 6 |
| Core entries with DOI | 19 (13 auto + 6 manual) |
| Core entries without DOI | 7 |
| Foundational must-cite entries | 21 |
| Foundational entries with DOI | 18 |
| **Total BibTeX entries** | **47** |
| Overlapping keys (dedup) | 0 |
| **Unique BibTeX keys** | **47** |

## BibTeX Classification

| Tier | Count | Description |
|:-----|------:|:------------|
| **Foundational** | 21 | Canonical papers any informational-universe paper must cite (Susskind, Maldacena, Bekenstein, Ryu-Takayanagi, Wheeler, Jacobson, Verlinde, etc.) |
| **Core (arXiv)** | 26 | Directly relevant papers from Phase 2 arXiv search (20 auto-fetched + 6 manual from rate-limited retries) |
| **Supporting** | 0 | (arXiv Supporting papers — 33 from Phase 2 — not yet added to BibTeX; can be added as needed during Phase 5 drafting) |
| **Total** | **47** | |

## DQ Audit (Core Papers)

| DOI Status | Count | Papers |
|:-----------|------:|:-------|
| DOI present | 13 | Nishioka-Ryu-Takayanagi 2009, Bao-Carroll-Singh 2017, Chiribella-Spekkens 2018, Bianchi-Livine 2023, Rovelli 2018, Planat 2013, Verlinde 2015, Esfeld 2014, Ghosh-Mishra 2016, Hu 2009, Huang 2024, Ydri 2021, Page 2018, Taghiloo 2025, Parvizi et al 2025, Barbon-Fuertes 2008 |
| DOI missing (built from metadata) | 7 | Zhang 2016, Miao 2013, Park 2015, Klauder 2021, Gambini-Pullin 2023, Hao-Taylor 2023, Jones et al 2025, Dawid-Franzmann 2025, Speranza 2018 |

## Missing Papers (arXiv fetch failed)

6 papers (arXiv rate-limited: 0903.0878v1 Hu, 1804.10623v1 Page, 2110.05634v1 Ydri, 2412.05446v1 Huang, hep-th/0404176v2 Papadimitriou-Skenderis, gr-qc/9903002v2 Bekenstein-Mayo) — manually added to BibTeX

## Foundational Citation Coverage

The 21 foundational entries cover:
- **Holographic principle:** Susskind 1995, 't Hooft 1993, Bousso 2002
- **AdS/CFT:** Maldacena 1999
- **Entanglement entropy + area:** Ryu-Takayanagi 2006, Hubeny-Rangamani-Takayanagi 2007, Swingle 2012, Srednicki 1993, Van Raamsdonk 2010
- **Black hole thermodynamics:** Bekenstein 1973, Hawking 1975, Bekenstein-Mayo 1999 (also in Core)
- **Information-theoretic derivations:** Chiribella-D'Ariano-Perinotti 2011, Zeilinger 1999, Wheeler 1989
- **Emergent spacetime/gravity:** Jacobson 1995, Verlinde 2011, Padmanabhan 2010
- **Quantum foundations:** Lloyd 2006, Almheiri-Dong-Harlow 2015, Pastawski-Yoshida-Harlow-Preskill 2015
- **Relational QM:** Rovelli 1996 (complements LQG-information Core papers)

