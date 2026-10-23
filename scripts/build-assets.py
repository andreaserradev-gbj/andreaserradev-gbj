#!/usr/bin/env python3
"""Generate the profile README artwork.

Palette and geometry mirror the `concrete` design system in the portfolio
repository (src/config/design-systems.json): 2px rules, zero radius, no
shadows, one kintsugi-gold accent.

Run: python3 scripts/build-assets.py
Outputs: assets/hero-v3-{light,dark}.svg, assets/loop-v2-{light,dark}.svg
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
        "faint": "#b8b4ac",
        "gold": "#b08648",
    },
    "dark": {
        "bg": "#1a1816",
        "elev": "#221f1c",
        "fg": "#d8d4cc",
        "muted": "#8a857c",
        "rule": "#d8d4cc",
        "faint": "#3a3631",
        "gold": "#c69a5d",
    },
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hero(theme: dict) -> str:
    w, h = 1000, 300
    mid = w / 2
    label = "SENIOR BACKEND ENGINEER"
    # JetBrains Mono advance is 0.6em; label carries 2.6px tracking.
    label_w = len(label) * (11.5 * 0.6 + 2.6)
    group_w = 24 + 12 + label_w
    group_x = mid - group_w / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Andrea Serra, senior backend engineer in Bologna. Thirty years from racing ECUs to web and cloud to fintech risk.">
  <rect width="{w}" height="{h}" fill="{theme['bg']}"/>
  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" fill="none" stroke="{theme['rule']}" stroke-width="2"/>

  <rect x="{group_x:.1f}" y="44" width="24" height="2" fill="{theme['gold']}"/>
  <text x="{group_x + 36:.1f}" y="49" font-family="{FONT_MONO}" font-size="11.5" letter-spacing="2.6" fill="{theme['muted']}">{label}</text>

  <text x="{mid}" y="128" text-anchor="middle" font-family="{FONT_DISPLAY}" font-size="62" font-weight="900" letter-spacing="-1.8" fill="{theme['fg']}">Andrea Serra</text>

  <text x="{mid}" y="166" text-anchor="middle" font-family="{FONT_MONO}" font-size="12.5" letter-spacing="0.7" fill="{theme['muted']}">racing ECUs &#8594; web &amp; cloud &#8594; fintech risk</text>

  <line x1="{mid - 170}" y1="200" x2="{mid + 170}" y2="200" stroke="{theme['gold']}" stroke-width="2"/>

  <text x="{mid}" y="226" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="2.2" fill="{theme['muted']}">BOLOGNA, IT &#183; REMOTE</text>

  <text x="{mid}" y="268" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="1.6" fill="{theme['muted']}">ARTAX 1996 &#183; BALSAMIQ 2013 &#183; SCALAPAY 2026</text>
</svg>
"""


STEPS = ["I ARCHITECT", "AGENT BUILDS", "I REVIEW"]


def loop(theme: dict) -> str:
    """Three-word working loop. Only large type, so it stays legible when
    GitHub scales the image down to a phone width."""
    w, h = 1000, 124
    box_w, box_h = 284, 78
    gap = 48
    total = len(STEPS) * box_w + (len(STEPS) - 1) * gap
    x0 = (w - total) / 2
    y0 = (h - box_h) / 2

    parts = [f'<rect width="{w}" height="{h}" fill="{theme["bg"]}"/>']

    for i, label in enumerate(STEPS):
        x = x0 + i * (box_w + gap)
        parts += [
            f'<rect x="{x:.1f}" y="{y0}" width="{box_w}" height="{box_h}" fill="{theme["elev"]}"/>',
            f'<rect x="{x:.1f}" y="{y0}" width="{box_w}" height="{box_h}" fill="none" stroke="{theme["rule"]}" stroke-width="2"/>',
            f'<rect x="{x:.1f}" y="{y0}" width="5" height="{box_h}" fill="{theme["gold"]}"/>',
            f'<text x="{x + box_w / 2 + 3:.1f}" y="{y0 + 47}" text-anchor="middle" font-family="{FONT_MONO}" font-size="26" font-weight="700" letter-spacing="1" fill="{theme["fg"]}">{label}</text>',
        ]
        if i < len(STEPS) - 1:
            ax = x + box_w + 12
            cy = y0 + box_h / 2
            parts += [
                f'<line x1="{ax:.1f}" y1="{cy}" x2="{ax + 18:.1f}" y2="{cy}" stroke="{theme["muted"]}" stroke-width="3"/>',
                f'<path d="M {ax + 12:.1f} {cy - 7} L {ax + 22:.1f} {cy} L {ax + 12:.1f} {cy + 7} Z" fill="{theme["muted"]}"/>',
            ]

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Working loop: I architect, the agent builds, I review.">
  {"\n  ".join(parts)}
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (OUT / f"hero-v3-{name}.svg").write_text(hero(theme), encoding="utf-8")
        (OUT / f"loop-v2-{name}.svg").write_text(loop(theme), encoding="utf-8")
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))


if __name__ == "__main__":
    main()
