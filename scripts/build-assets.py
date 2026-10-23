#!/usr/bin/env python3
"""Generate the profile README artwork.

Palette and geometry mirror the `concrete` design system in the portfolio
repository (src/config/design-systems.json): 2px rules, zero radius, no
shadows, one kintsugi-gold accent.

Run: python3 scripts/build-assets.py
Outputs: assets/hero-v2-{light,dark}.svg
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

FONT_DISPLAY = "'Hanken Grotesk','Helvetica Neue',Helvetica,Arial,sans-serif"
FONT_MONO = "'JetBrains Mono',ui-monospace,'DejaVu Sans Mono',monospace"

THEMES = {
    "light": {
        "bg": "#d8d6d2",
        "elev": "#cecbc4",
        "fg": "#2c2a28",
        "muted": "#6e6a64",
        "rule": "#2c2a28",
        "gold": "#b08648",
    },
    "dark": {
        "bg": "#1a1816",
        "elev": "#221f1c",
        "fg": "#d8d4cc",
        "muted": "#8a857c",
        "rule": "#d8d4cc",
        "gold": "#c69a5d",
    },
}

def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hero(theme: dict) -> str:
    w, h = 1000, 300
    mid = w / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Andrea Serra, full-stack developer at Balsamiq. Thirty years from racing ECUs to web and cloud to fintech risk. Bologna, Italy, remote.">
  <rect width="{w}" height="{h}" fill="{theme['bg']}"/>
  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" fill="none" stroke="{theme['rule']}" stroke-width="2"/>

  <rect x="{mid - 190}" y="44" width="24" height="2" fill="{theme['gold']}"/>
  <text x="{mid - 150}" y="49" font-family="{FONT_MONO}" font-size="11.5" letter-spacing="2.6" fill="{theme['muted']}">FULL-STACK DEVELOPER</text>

  <text x="{mid}" y="128" text-anchor="middle" font-family="{FONT_DISPLAY}" font-size="62" font-weight="900" letter-spacing="-1.8" fill="{theme['fg']}">Andrea Serra</text>

  <text x="{mid}" y="166" text-anchor="middle" font-family="{FONT_MONO}" font-size="12.5" letter-spacing="0.7" fill="{theme['muted']}">racing ECUs &#8594; web &amp; cloud &#8594; fintech risk</text>

  <line x1="{mid - 170}" y1="200" x2="{mid + 170}" y2="200" stroke="{theme['gold']}" stroke-width="2"/>

  <text x="{mid}" y="226" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="2.2" fill="{theme['muted']}">BOLOGNA, IT &#183; REMOTE</text>

  <text x="{mid}" y="268" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="1.6" fill="{theme['muted']}">ARTAX 1996 &#183; BALSAMIQ 2013 &#183; SCALAPAY 2026</text>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (OUT / f"hero-v2-{name}.svg").write_text(hero(theme), encoding="utf-8")
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))


if __name__ == "__main__":
    main()
