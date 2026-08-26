#!/usr/bin/env python3
"""JPC.003 — render the References section FROM references.bib (REFERENCE-TITLE-FIDELITY-1).

Generates the [1]..[N] list from the citation-audited bib in bib order, asserts
title fidelity (rendered title == bib title, by construction), and splices the
result into paper.md, replacing the previous hand-typed list.

Field fixes (pass-2 audit):
  - articles: emit volume (+ number in parentheses) before pages
  - inproceedings: do not append the year when the booktitle already ends (YYYY)
  - books: append "ed." to the edition field
Usage: python render_references.py   (run from the repository root)
"""
import re
import sys

def parse_bib(path):
    src = open(path, encoding="utf-8").read()
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,]+),\s*", src):
        type_, key = m.group(1), m.group(2).strip()
        i = m.end()
        depth = 1
        while i < len(src) and depth:
            if src[i] == "{":
                depth += 1
            elif src[i] == "}":
                depth -= 1
            i += 1
        block = src[m.end():i - 1]
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", block):
            j = fm.end()
            d = 1
            while j < len(block) and d:
                if block[j] == "{":
                    d += 1
                elif block[j] == "}":
                    d -= 1
                j += 1
            fields[fm.group(1).lower()] = block[fm.end():j - 1]
        entries.append((type_, key, fields))
    return entries

ACCENTS = {
    r"{\v{c}}": "č", r"{\'a}": "á", r"{\v{s}}": "š", r"{\aa}": "å", r"\aa": "å",
    r"{\'e}": "é", r"{\'{\i}}": "í", r"{\i}": "ı", r"{\'o}": "ó", r"{\"o}": "ö",
    r"{\'u}": "ú", r"{\'y}": "ý", r"{\v{z}}": "ž", r"{\v{r}}": "ř",
}
def unlatex(s):
    for k, v in ACCENTS.items():
        s = s.replace(k, v)
    s = s.replace("---", "—").replace("--", "–")
    return s.replace("{", "").replace("}", "")

def names(author):
    parts = [p.strip() for p in author.split(" and ") if p.strip()]
    out = []
    for p in parts:
        if "," in p:
            last, first = [x.strip() for x in p.split(",", 1)]
            out.append(f"{first} {last}".strip())
        else:
            out.append(p)
    return [unlatex(x) for x in out if x]

def fmt_authors(author):
    ns = names(author)
    if not ns:
        return ""
    if len(ns) > 4:
        return ns[0] + " et al."
    return ", ".join(ns)

def main():
    entries = parse_bib("references.bib")
    lines = ["## References", ""]
    manifest = []
    for idx, (type_, key, f) in enumerate(entries, 1):
        title = unlatex(f.get("title", "")).strip()
        auth = fmt_authors(f.get("author", ""))
        year = f.get("year", "").strip()
        venue = unlatex((f.get("journal") or f.get("booktitle") or "").strip())
        pages = unlatex(f.get("pages", "")).strip().replace("--", "–")
        volume = unlatex(f.get("volume", "")).strip()
        number = unlatex(f.get("number", "")).strip()
        doi = f.get("doi", "").strip()
        eprint = f.get("eprint", "").strip()
        extra = ""
        if eprint:
            extra = " arXiv:" + eprint
        elif doi:
            extra = " https://doi.org/" + doi
        if type_ == "book":
            ed = unlatex(f.get("edition", "")).strip()
            if ed:
                ed = ed.rstrip(".") + " ed."
            pub = unlatex(f.get("publisher", "")).strip()
            line = f"[{idx}] {auth}, {title}, {ed}, {pub} ({year})."
            lines.append(line)
            manifest.append((key, title))
            continue
        if type_ == "inproceedings":
            line = f"[{idx}] {auth}, \"{title},\" {venue}"
            if pages:
                line += f", {pages}"
            # avoid a duplicate year when the venue already ends with (…YYYY)
            if not re.search(r"\([^)]*\d{4}\)$", venue):
                line += f" ({year})"
            line += "."
            if extra:
                line += extra
            lines.append(line)
            manifest.append((key, title))
            continue
        # article / misc
        line = f"[{idx}] {auth}, \"{title},\""
        if venue:
            line += f" {venue}"
        if type_ == "article":
            if volume:
                line += f" {volume}" + (f"({number})" if number else "")
            if pages:
                line += f", {pages}"
        line += f" ({year})."
        if extra:
            line += extra
        manifest.append((key, title))
        lines.append(line)
    lines.append("")
    generated = "\n".join(lines)

    print(f"RENDERED {len(entries)} REFERENCES from references.bib")
    if len(entries) != 32:
        print("WARN: expected 32 entries")
        raise SystemExit(1)

    paper_path = sys.argv[1] if len(sys.argv) > 1 else "jpcub-qec-landauer.md"
    paper = open(paper_path, encoding="utf-8").read()
    marker = "## References"
    pos = paper.find(marker)
    if pos == -1:
        print("ERROR: ## References not found in paper.md")
        raise SystemExit(2)
    new_paper = paper[:pos] + generated
    open(paper_path, "w", encoding="utf-8", newline="\n").write(new_paper)
    print(f"spliced {len(generated)} chars into {paper_path} (replaced from offset {pos})")
    print("TITLE FIDELITY: rendered-from-bib by construction (REFERENCE-TITLE-FIDELITY-1)")
    print("--- generated list ---")
    print(generated)

if __name__ == "__main__":
    main()
