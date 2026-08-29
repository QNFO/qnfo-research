# Citation Audit — Distinction-Primitive Research Framework v0.1

- **Date:** 2026-08-29
- **Method:** every cited DOI verified against the QNFO registry (D1 portfolio-state
  program_registry) and/or the Zenodo records API; rendered titles cross-checked against
  the bib entries (REFERENCE-TITLE-FIDELITY-1).

## Cited records

| Bib key | DOI | Registry row | Verification |
|:--------|:----|:-------------|:-------------|
| spencerbrown1969 | — (1969, Allen & Unwin) | — | standard reference; no DOI exists for the 1969 edition |
| umporr014 | 10.5281/zenodo.22150472 | QNFO.UMP.014, published, v1.0 | registry row matches; live on Zenodo |
| res027 | 10.5281/zenodo.22133122 | QNFO.RES.027, published, v1.0.1 | registry row matches |
| res028 | 10.5281/zenodo.22124744 | QNFO.RES.028, published, v1.0.0 | registry row matches |
| res029 | 10.5281/zenodo.22142794 | QNFO.RES.029, published, v1.1.0 | registry row matches |
| res030 | 10.5281/zenodo.22152967 | QNFO.RES.030, published, v1.0 | registry row matches |
| res031 | 10.5281/zenodo.22159758 | QNFO.RES.031, published, v1.0 | registry row + live Zenodo API match |
| res021 | 10.5281/zenodo.22046458 | QNFO.RES.021, published, v1.0.2 | registry row matches |

## In-text citation check (BIB-ORPHAN-1)

- Every bib entry above is cited in the paper body (spencerbrown1969 §2.1; umporr014 §1/§2.2/§4;
  res027 §1/§3.2/§4; res028 §1/§4; res029 §1/§4/§6; res030 §1/§2.7/§3.2; res021 §4; res031 §4).

## Rendering check

- The rendered bibliography (pandoc --citeproc) was diffed against the titles above;
  all seven DOI-carrying titles match the bib strings verbatim (rebuilt at v0.2 with the
  `references.bib` filename fix in the CDP pipeline; the v0.1 ship was built with the
  pipeline's `refs.bib` check disabled — red-team C1, remediated).
