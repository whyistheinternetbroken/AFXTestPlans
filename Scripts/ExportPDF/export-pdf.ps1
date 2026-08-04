<#
.SYNOPSIS
  Export the AFX test plan AsciiDoc book to a single PDF.

.DESCRIPTION
  Builds Scripts/ExportPDF/book.adoc with asciidoctor-pdf (local gem or Docker).
  Run from anywhere; the script resolves the repository root.

.PARAMETER OutDir
  Output directory relative to the repo root (default: exports).

.PARAMETER OutFile
  PDF file name (default: AFX-Test-Plan-ONTAP-9.19.1.pdf).

.PARAMETER UseDocker
  Force Docker even if asciidoctor-pdf is on PATH.
#>
[CmdletBinding()]
param(
    [string]$OutDir = "exports",
    [string]$OutFile = "AFX-Test-Plan-ONTAP-9.19.1.pdf",
    [switch]$UseDocker
)

$ErrorActionPreference = "Stop"

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "../..")
Set-Location $RepoRoot

$BookRel = "Scripts/ExportPDF/book.adoc"
$Book = Join-Path $RepoRoot $BookRel
if (-not (Test-Path $Book)) {
    throw "Missing book master: $Book"
}

$OutPath = Join-Path $RepoRoot $OutDir
New-Item -ItemType Directory -Force -Path $OutPath | Out-Null
$PdfPath = Join-Path $OutPath $OutFile

$AsciidoctorPdf = Get-Command "asciidoctor-pdf" -ErrorAction SilentlyContinue
$Docker = Get-Command "docker" -ErrorAction SilentlyContinue

if (-not $UseDocker -and $AsciidoctorPdf) {
    Write-Host "Using local asciidoctor-pdf..."
    & asciidoctor-pdf `
        -a icons=font `
        -a experimental `
        -a allow-uri-read `
        -D $OutPath `
        -o $OutFile `
        $Book
}
elseif ($Docker) {
    Write-Host "Using Docker image asciidoctor/docker-asciidoctor..."
    $RelOutDir = $OutDir -replace '\\', '/'
    $BookDocker = $BookRel -replace '\\', '/'
    docker run --rm `
        -v "${RepoRoot}:/documents" `
        -w /documents `
        asciidoctor/docker-asciidoctor `
        asciidoctor-pdf `
        -a icons=font `
        -a experimental `
        -a allow-uri-read `
        -D $RelOutDir `
        -o $OutFile `
        $BookDocker
}
else {
    throw @"
Neither asciidoctor-pdf nor docker was found.

Install one of:
  gem install asciidoctor-pdf rouge
  Docker Desktop (image: asciidoctor/docker-asciidoctor)

See Scripts/ExportPDF/PDF-EXPORT.adoc for details.
"@
}

if (-not (Test-Path $PdfPath)) {
    throw "PDF was not created: $PdfPath"
}

Write-Host "Wrote $PdfPath"
Write-Host "Share via Box/OneDrive/SharePoint (view-only + expiration). Do not publish the PDF or repo publicly."
