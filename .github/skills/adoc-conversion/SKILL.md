---
name: adoc-conversion
description: "Use when converting a DOCX test plan into linked AsciiDoc pages with left-sidebar TOCs, per-section split files, appendix landing pages, test-plan index pages, and conflict/repetition consolidation."
---

# ADOC Conversion Skill

Convert a DOCX document into a multi-file AsciiDoc set with consistent navigation and cross-links.

## Use when

- User asks to convert `.docx` to `.adoc`
- User asks to split one large document into multiple ADOC files
- User asks for test-plan-per-file layout plus a test plan landing page
- User asks for appendix landing page + one page per appendix subsection
- User asks to consolidate repeated information and cross-link related sections

## Workflow

1. Locate DOCX source and extract structure (headings, paragraphs, tables, code blocks).
2. Identify top-level split boundaries and requested section ranges.
3. Generate ADOC files with standard attributes:
   - `:toc: left`
   - `:toclevels: 4`
   - `:sectnums:`
   - `:icons: font`
   - `:source-highlighter: highlight.js`
4. Create landing pages:
   - `index.adoc` as top-level navigation
   - `test-plans.adoc` linking individual tests
   - `appendix.adoc` linking one level below appendix headings
5. Keep each test as its own file when requested; keep feature tests one file per feature.
6. Consolidate duplicated sections and add explicit xrefs from moved/origin sections.
7. If conflicting source guidance is found, stop and ask user how to resolve before finalizing.
8. Validate all generated links and anchors.

## Splitting rules

- First file can cover intro sections (for example, *Providing feedback* through *Licensing requirements*).
- Next file can cover setup sections (for example, *Recommended setup* through *NFS server configuration*).
- Keep *Datasets and workloads* through *ONTAP limitations* together unless user requests a different split.
- Keep performance test configuration details together in the performance test plan file.
- Place scripts into a dedicated `scripts.adoc` page.
- Add NAS script references (for this repo, include:
  `https://github.com/whyistheinternetbroken/Benchmarking/tree/main/ONTAP`).

## Consolidation policy

- Repeated content: keep the most complete version, replace other occurrences with xrefs.
- Complementary duplicates: merge into one canonical section and note overlap when needed.
- Conflicts: ask user; do not silently choose.

## Output checklist

- [ ] `index.adoc` exists and links all major pages
- [ ] Every page has `:toc: left`
- [ ] `test-plans.adoc` links all test pages
- [ ] `appendix.adoc` links each appendix subsection page
- [ ] `scripts.adoc` exists with NAS scripts link
- [ ] Cross-links resolve
- [ ] Any consolidation/conflict decisions are documented in notes

## Table formatting conventions

- Use light gray header styling for all content tables, but only the header row should be shaded:
  - Apply the class to the table and scope CSS to `thead th` for gray headers.
  - Force `tbody td` / `tbody th` back to white when the theme shades the full table.
- Keep header cell labels on a single row using spaced pipes (for example: `| NFS | SMB | Object`).
- For multi-value content inside a single table cell, use AsciiDoc cell blocks with bullets:
  - Put `a|` immediately before the list content.
  - Do not insert a blank line between `a|` and the first bullet.
- Preserve special AsciiDoc table cell syntax (`a|`, `>|`, `+` line continuations) when normalizing formatting.
- Keep table row formatting consistent:
  - Use `|===` for table delimiters.
  - Prefer `| ` (pipe + space) for standard cell starts.
  - Remove trailing whitespace.
- Use caption syntax like `.NFS features`, not `.Table 1. NFS features`; let the renderer add the table number.
