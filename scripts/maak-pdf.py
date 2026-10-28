#!/usr/bin/env python3
"""Genereer Pong-Huisstijl-en-Handleiding.pdf vanuit docs/huisstijl-en-handleiding.html.

Gebruik:  python scripts/maak-pdf.py
Vereist:  Google Chrome (headless print-to-pdf). Geen internet nodig.
De PDF gebruikt de PONG huisstijl v1.0 (logo, kleuren en typografie uit huisstijl.md).
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRON = ROOT / "docs" / "huisstijl-en-handleiding.html"
DOEL = ROOT / "Pong-Huisstijl-en-Handleiding.pdf"

CHROME_KANDIDATEN = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    shutil.which("chrome") or "",
    shutil.which("msedge") or "",
    shutil.which("chromium") or "",
]


def zoek_browser() -> str | None:
    for pad in CHROME_KANDIDATEN:
        if pad and Path(pad).exists():
            return pad
    return None


def main() -> int:
    if not BRON.exists():
        print(f"Fout: bronbestand ontbreekt: {BRON}", file=sys.stderr)
        return 1
    browser = zoek_browser()
    if not browser:
        print("Fout: geen Chrome/Edge gevonden om de PDF mee te maken.", file=sys.stderr)
        return 1
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf=" + str(DOEL),
        BRON.as_uri(),
    ]
    print("Browser:", browser)
    print("Bron:   ", BRON)
    subprocess.run(cmd, check=True)
    if not DOEL.exists() or DOEL.stat().st_size == 0:
        print("Fout: PDF is niet aangemaakt.", file=sys.stderr)
        return 1
    print(f"PDF aangemaakt: {DOEL} ({DOEL.stat().st_size / 1024:.0f} kB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
