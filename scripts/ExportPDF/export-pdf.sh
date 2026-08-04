#!/usr/bin/env bash
# Export the AFX test plan AsciiDoc book to a single PDF.
# Usage: ./scripts/ExportPDF/export-pdf.sh [outdir] [outfile]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

OUT_DIR="${1:-exports}"
OUT_FILE="${2:-AFX-Test-Plan-ONTAP-9.19.1.pdf}"
BOOK="book.adoc"

if [[ ! -f "$BOOK" ]]; then
  echo "Missing $BOOK at repo root" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

if command -v asciidoctor-pdf >/dev/null 2>&1; then
  echo "Using local asciidoctor-pdf..."
  asciidoctor-pdf \
    -a icons=font \
    -a experimental \
    -a allow-uri-read \
    -D "$OUT_DIR" \
    -o "$OUT_FILE" \
    "$BOOK"
elif command -v docker >/dev/null 2>&1; then
  echo "Using Docker image asciidoctor/docker-asciidoctor..."
  docker run --rm \
    -v "$ROOT:/documents" \
    -w /documents \
    asciidoctor/docker-asciidoctor \
    asciidoctor-pdf \
    -a icons=font \
    -a experimental \
    -a allow-uri-read \
    -D "$OUT_DIR" \
    -o "$OUT_FILE" \
    "$BOOK"
else
  cat >&2 <<'EOF'
Neither asciidoctor-pdf nor docker was found.

Install one of:
  gem install asciidoctor-pdf rouge
  Docker (image: asciidoctor/docker-asciidoctor)

See PDF-EXPORT.adoc for details.
EOF
  exit 1
fi

echo "Wrote $OUT_DIR/$OUT_FILE"
echo "Share via Box/OneDrive/SharePoint (view-only + expiration). Do not publish the PDF or repo publicly."
