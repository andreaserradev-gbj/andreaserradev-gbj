#!/usr/bin/env python3
"""Generate the profile README artwork.

Palette and geometry mirror the `concrete` design system in the portfolio
repository (src/config/design-systems.json): 2px rules, zero radius, no
shadows, one kintsugi-gold accent.

Run: python3 scripts/build-assets.py
Outputs: assets/{hero,work}-{light,dark}.svg
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
        "gold_fg": "#1a1816",
    },
    "dark": {
        "bg": "#1a1816",
        "elev": "#221f1c",
        "fg": "#d8d4cc",
        "muted": "#8a857c",
        "rule": "#d8d4cc",
        "faint": "#3a3631",
        "gold": "#c69a5d",
        "gold_fg": "#1a1816",
    },
}


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hero(theme: dict) -> str:
    w, h = 1000, 280
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Andrea Serra, senior backend engineer in Bologna. Racing ECUs to web and cloud to fintech risk. ARTAX 1996, Balsamiq 2013, Scalapay 2026.">
  <rect width="{w}" height="{h}" fill="{theme['bg']}"/>
  <rect x="2" y="2" width="{w - 4}" height="{h - 4}" fill="none" stroke="{theme['rule']}" stroke-width="2"/>

  <rect x="451" y="44" width="20" height="2" fill="{theme['gold']}"/>
  <text x="483" y="49" font-family="{FONT_MONO}" font-size="11.5" letter-spacing="2.4" fill="{theme['muted']}">SENIOR BACKEND ENGINEER</text>

  <text x="{w / 2}" y="126" text-anchor="middle" font-family="{FONT_DISPLAY}" font-size="60" font-weight="900" letter-spacing="-1.6" fill="{theme['fg']}">Andrea Serra</text>

  <text x="{w / 2}" y="162" text-anchor="middle" font-family="{FONT_MONO}" font-size="12.5" letter-spacing="0.6" fill="{theme['muted']}">racing ECUs &#8594; web &amp; cloud &#8594; fintech risk</text>

  <line x1="120" y1="205" x2="880" y2="205" stroke="{theme['rule']}" stroke-width="2"/>
  <line x1="120" y1="199" x2="120" y2="211" stroke="{theme['rule']}" stroke-width="2"/>
  <line x1="880" y1="199" x2="880" y2="211" stroke="{theme['rule']}" stroke-width="2"/>
  <line x1="500" y1="195" x2="500" y2="215" stroke="{theme['gold']}" stroke-width="3"/>

  <text x="120" y="234" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="1.4" fill="{theme['muted']}">1996 · ARTAX</text>
  <text x="500" y="234" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="1.4" fill="{theme['muted']}">2013 · BALSAMIQ</text>
  <text x="880" y="234" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="1.4" fill="{theme['muted']}">2026 · SCALAPAY</text>

  <text x="{w / 2}" y="258" text-anchor="middle" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="2.2" fill="{theme['muted']}">BOLOGNA, IT · REMOTE</text>
</svg>
"""


CARDS = [
    {
        "id": "01",
        "name": "dev-workflow",
        "lang": "JavaScript",
        "desc": ["Multi-session feature work with coding agents:", "PRD phases, checkpoints, resume across tools."],
        "live": None,
    },
    {
        "id": "02",
        "name": "portfolio-template",
        "lang": "TypeScript",
        "desc": ["JSON-driven portfolio with six switchable", "design systems, validated at build time."],
        "live": "portfolio-template-ten-eta.vercel.app",
    },
    {
        "id": "03",
        "name": "jev-access-day",
        "lang": "TypeScript",
        "desc": ["Typed decision model against an LLM stand-in", "on 24 operational decisions, every run committed."],
        "live": "jev-access-day.vercel.app",
    },
    {
        "id": "04",
        "name": "dotfiles-nix",
        "lang": "Nix",
        "desc": ["Three machines from one NixOS flake. One", "command rebuilds system and $HOME."],
        "live": None,
    },
]


def card(theme: dict, c: dict, x: int, y: int, w: int = 448, h: int = 198) -> str:
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{theme["elev"]}"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{theme["rule"]}" stroke-width="2"/>',
        f'<text x="{x + 24}" y="{y + 34}" font-family="{FONT_MONO}" font-size="10.5" letter-spacing="1.6" fill="{theme["gold"]}">{c["id"]}</text>',
        f'<text x="{x + 24}" y="{y + 66}" font-family="{FONT_MONO}" font-size="18" font-weight="700" fill="{theme["fg"]}">{esc(c["name"])}</text>',
    ]
    for i, line in enumerate(c["desc"]):
        parts.append(
            f'<text x="{x + 24}" y="{y + 98 + i * 20}" font-family="{FONT_DISPLAY}" font-size="13.5" fill="{theme["muted"]}">{esc(line)}</text>'
        )
    fy = y + h - 24
    parts.append(
        f'<text x="{x + 24}" y="{fy}" font-family="{FONT_MONO}" font-size="11" letter-spacing="0.8" fill="{theme["muted"]}">{c["lang"]}</text>'
    )
    if c["live"]:
        parts.append(
            f'<text x="{x + w - 24}" y="{fy}" text-anchor="end" font-family="{FONT_MONO}" font-size="11" fill="{theme["gold"]}">live &#8599;</text>'
        )
    return "\n  ".join(parts)


def work(theme: dict) -> str:
    w, h = 1000, 500
    positions = [(36, 44), (516, 44), (36, 272), (516, 272)]
    cards = "\n  ".join(card(theme, c, x, y) for c, (x, y) in zip(CARDS, positions))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Selected work: dev-workflow, portfolio-template, jev-access-day, dotfiles-nix.">
  <rect width="{w}" height="{h}" fill="{theme['bg']}"/>
  {cards}
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(hero(theme), encoding="utf-8")
        (OUT / f"work-{name}.svg").write_text(work(theme), encoding="utf-8")
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))


if __name__ == "__main__":
    main()
