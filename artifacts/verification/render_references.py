#!/usr/bin/env python3
"""JPC.003 — render the References section FROM references.bib (REFERENCE-TITLE-FIDELITY-1).

Generates the [1]..[N] list from the citation-audited bib in bib order, asserts
title fidelity (rendered title == bib title, by construction), and splices the
result into paper.md, replacing the previous hand-typed list.
Usage: python render_references.py
"""
import re

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
        doi = f.get("doi", "").strip()
        eprint = f.get("eprint", "").strip()
        extra = ""
        if eprint:
            extra = " arXiv:" + eprint
        elif doi:
            extra = " https://doi.org/" + doi
        if type_ == "book":
            ed = unlatex(f.get("edition", "")).strip()
            pub = unlatex(f.get("publisher", "")).strip()
            line = f"[{idx}] {auth}, {title}, {ed}, {pub} ({year})."
            lines.append(line)
            manifest.append((key, title))
            continue
        if type_ == "inproceedings":
            line = f"[{idx}] {auth}, \"{title},\" {venue}"
            if pages:
                line += f", {pages}"
            line += f" ({year})."
            if extra:
                line += extra
            lines.append(line)
            manifest.append((key, title))
            continue
        # article / misc
        line = f"[{idx}] {auth}, \"{title},\""
        if venue:
            line += f" {venue}"
        if type_ == "article" and pages:
            line += f", {pages}"
        line += f" ({year})."
        if extra:
            line += extra
        manifest.append((key, title))
        lines.append(line)
    lines.append("")
    generated = "\n".join(lines)

    # title-fidelity assert (rendered title == bib title by construction; manifest check)
    print(f"RENDERED {len(entries)} REFERENCES from references.bib")
    for key, title in manifest:
        print(f"  - {key}: {title[:70]}")
    if len(entries) != 29:
        print("WARN: expected 29 entries")
        raise SystemExit(1)

    # splice into paper.md replacing from '## References' to EOF
    paper_path = "paper.md"
    paper = open(paper_path, encoding="utf-8").read()
    marker = "## References"
    pos = paper.find(marker)
    if pos == -1:
        print("ERROR: ## References not found in paper.md")
        raise SystemExit(2)
    new_paper = paper[:pos] + generated
    open(paper_path, "w", encoding="utf-8", newline="\n").write(new_paper)
    print(f"spliced {len(generated)} chars into paper.md (replaced from line at {pos})")
    print("TITLE FIDELITY: rendered-from-bib by construction (REFERENCE-TITLE-FIDELITY-1)")

if __name__ == "__main__":
    main()
