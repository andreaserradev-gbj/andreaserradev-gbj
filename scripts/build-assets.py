#!/usr/bin/env python3
"""Generate the profile README artwork.

Palette and geometry mirror the `concrete` design system in the portfolio
repository (src/config/design-systems.json): 2px rules, zero radius, no
shadows, one kintsugi-gold accent.

Run: python3 scripts/build-assets.py
Outputs: assets/loop-v3-{light,dark}.svg
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
        (OUT / f"loop-v3-{name}.svg").write_text(loop(theme), encoding="utf-8")
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))


if __name__ == "__main__":
    main()
