"""Generate the animated, self-contained GitHub profile hero SVG.

Run from the repository root:
    python scripts/generate_profile_assets.py

No third-party packages are needed. The generated graphic does not depend on
external image or statistics services, so it works in local previews and after
publishing to GitHub.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "data-analyst-hero.svg"
IMPACT_OUTPUT = ROOT / "assets" / "idea-to-impact.svg"
ACTIVITY_OUTPUT = ROOT / "assets" / "github-activity-pulse.svg"
LINKS_DIR = ROOT / "assets" / "links"
COLLAB_OUTPUT = ROOT / "assets" / "collaboration-network.svg"

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 330" role="img" aria-labelledby="title desc">
  <title id="title">Chiranjeeb Kumar Sahoo — aspiring data analyst</title>
  <desc id="desc">An animated analytics command centre showing Chiranjeeb's journey through SQL, Python, and Power BI.</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#07111d"/><stop offset=".55" stop-color="#101c30"/><stop offset="1" stop-color="#0b0d19"/></linearGradient>
    <linearGradient id="accent" x1="0" x2="1"><stop stop-color="#2bd9ff"/><stop offset=".52" stop-color="#9373ff"/><stop offset="1" stop-color="#52f0ae"/></linearGradient>
    <linearGradient id="chart" x1="0" x2="0" y1="1" y2="0"><stop stop-color="#2bd9ff" stop-opacity=".12"/><stop offset="1" stop-color="#2bd9ff" stop-opacity=".72"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#89b4d0" stroke-opacity=".08"/></pattern>
  </defs>
  <rect width="1100" height="330" rx="22" fill="url(#bg)"/><rect width="1100" height="330" rx="22" fill="url(#grid)"/>
  <rect x="1" y="1" width="1098" height="328" rx="21" fill="none" stroke="#2c4967"/>
  <rect x="0" y="0" width="1100" height="5" rx="2" fill="url(#accent)"/>
  <g font-family="Arial, Helvetica, sans-serif">
    <g transform="translate(46 42)"><rect width="230" height="30" rx="15" fill="#0c2b38" stroke="#2bd9ff" stroke-opacity=".75"/><circle cx="18" cy="15" r="5" fill="#4ff1af"><animate attributeName="opacity" values="1;.3;1" dur="1.4s" repeatCount="indefinite"/></circle><text x="35" y="20" fill="#8ff5d0" font-size="12" font-weight="700" letter-spacing="1">ANALYTICS JOURNEY: LIVE</text></g>
    <text x="46" y="122" fill="#f7fbff" font-size="38" font-weight="700">Chiranjeeb Kumar Sahoo</text>
    <text x="46" y="151" fill="#56dcff" font-size="14" font-weight="700" letter-spacing="2">ASPIRING DATA ANALYST  /  BUILDING IN PUBLIC</text>
    <text x="46" y="187" fill="#a7b8ca" font-size="15">Learning with real datasets, clear questions, and practical projects.</text>
    <g transform="translate(46 220)" font-size="11" font-weight="700" text-anchor="middle"><g><rect width="104" height="30" rx="8" fill="#102538" stroke="#2bd9ff"/><text x="52" y="20" fill="#67e5ff">SQL</text></g><g transform="translate(116)"><rect width="104" height="30" rx="8" fill="#19243d" stroke="#9a7bff"/><text x="52" y="20" fill="#c2b3ff">PYTHON</text></g><g transform="translate(232)"><rect width="104" height="30" rx="8" fill="#2c2814" stroke="#f6ca43"/><text x="52" y="20" fill="#ffe28d">POWER BI</text></g></g>
    <text x="46" y="291" fill="#7289a0" font-size="11" letter-spacing="1.4">QUESTION  →  DATA  →  INSIGHT  →  NEXT STEP</text>
  </g>
  <g transform="translate(676 34)">
    <rect width="378" height="252" rx="17" fill="#091421" stroke="#304c6a"/>
    <text x="24" y="34" fill="#c5d4e2" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" letter-spacing="1.4">PROJECT SIGNAL</text>
    <path d="M24 202H350M24 158H350M24 114H350M24 70H350" stroke="#4d6c85" stroke-opacity=".25"/>
    <path d="M33 204 L82 168 L130 183 L180 124 L229 139 L281 75 L337 52 L337 204 Z" fill="url(#chart)" opacity=".8"/>
    <path d="M33 204 L82 168 L130 183 L180 124 L229 139 L281 75 L337 52" fill="none" stroke="#2bd9ff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)" stroke-dasharray="420" stroke-dashoffset="420"><animate attributeName="stroke-dashoffset" values="420;0;0;420" dur="6s" repeatCount="indefinite"/></path>
    <g fill="#f8fbff" filter="url(#glow)"><circle cx="82" cy="168" r="5"><animate attributeName="opacity" values=".25;1;.25" dur="2s" repeatCount="indefinite"/></circle><circle cx="180" cy="124" r="5"><animate attributeName="opacity" values=".25;1;.25" begin=".4s" dur="2s" repeatCount="indefinite"/></circle><circle cx="281" cy="75" r="5"><animate attributeName="opacity" values=".25;1;.25" begin=".8s" dur="2s" repeatCount="indefinite"/></circle><circle cx="337" cy="52" r="6" fill="#52f0ae"><animate attributeName="r" values="4;8;4" dur="1.5s" repeatCount="indefinite"/></circle></g>
    <g transform="translate(24 217)"><rect width="142" height="19" rx="9" fill="#123128"/><text x="71" y="14" text-anchor="middle" fill="#75f2b6" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="700">BUILD • LEARN • SHARE</text></g>
  </g>
</svg>'''

IMPACT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 310" role="img" aria-labelledby="title desc">
  <title id="title">From idea to product impact</title>
  <desc id="desc">An animated flow from a normal idea to data evidence, business insight, and product improvement.</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#101426"/><stop offset=".52" stop-color="#0b1c2b"/><stop offset="1" stop-color="#111821"/></linearGradient>
    <linearGradient id="flow" x1="0" x2="1"><stop stop-color="#ffbd59"/><stop offset=".34" stop-color="#2bd9ff"/><stop offset=".68" stop-color="#a78bfa"/><stop offset="1" stop-color="#52f0ae"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <pattern id="grid" width="26" height="26" patternUnits="userSpaceOnUse"><path d="M26 0H0V26" fill="none" stroke="#9eb9d0" stroke-opacity=".06"/></pattern>
  </defs>
  <rect width="1100" height="310" rx="20" fill="url(#bg)"/><rect width="1100" height="310" rx="20" fill="url(#grid)"/><rect x="1" y="1" width="1098" height="308" rx="19" fill="none" stroke="#344762"/>
  <g font-family="Arial, Helvetica, sans-serif"><text x="42" y="52" fill="#f8fbff" font-size="24" font-weight="700">FROM IDEA TO IMPACT</text><text x="42" y="76" fill="#9cb1c5" font-size="13" letter-spacing="1.3">HOW DATA CAN TURN A SIMPLE THOUGHT INTO A BETTER PRODUCT</text></g>
  <path d="M174 181 C237 181 256 181 314 181 S 470 181 526 181 S 682 181 738 181 S 894 181 946 181" fill="none" stroke="url(#flow)" stroke-width="5" stroke-linecap="round" opacity=".78"/>
  <path d="M174 181 C237 181 256 181 314 181 S 470 181 526 181 S 682 181 738 181 S 894 181 946 181" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="7 18" opacity=".8"><animate attributeName="stroke-dashoffset" from="0" to="-50" dur="1.6s" repeatCount="indefinite"/></path>
  <circle r="7" fill="#fff4b8" filter="url(#glow)"><animateMotion dur="4.8s" repeatCount="indefinite" path="M174 181 C237 181 256 181 314 181 S 470 181 526 181 S 682 181 738 181 S 894 181 946 181"/></circle>
  <g font-family="Arial, Helvetica, sans-serif" text-anchor="middle">
    <g transform="translate(38 113)"><rect width="156" height="137" rx="16" fill="#302719" stroke="#ffbd59"/><circle cx="78" cy="40" r="21" fill="#ffbd59" fill-opacity=".16"/><path d="M78 23c-10 0-18 8-18 18 0 7 4 12 9 15v10h18V56c5-3 9-8 9-15 0-10-8-18-18-18z" fill="none" stroke="#ffcf7b" stroke-width="2"/><text x="78" y="92" fill="#fff" font-size="16" font-weight="700">NORMAL IDEA</text><text x="78" y="114" fill="#d4ba91" font-size="11">“Can this be better?”</text></g>
    <g transform="translate(304 113)"><rect width="156" height="137" rx="16" fill="#102b3a" stroke="#2bd9ff"/><circle cx="78" cy="40" r="21" fill="#2bd9ff" fill-opacity=".16"/><path d="M64 48V34m9 14V26m9 22V31m9 17V21" stroke="#67e7ff" stroke-width="4" stroke-linecap="round"/><text x="78" y="92" fill="#fff" font-size="16" font-weight="700">EVIDENCE</text><text x="78" y="114" fill="#9fc7d6" font-size="11">Collect the signals</text></g>
    <g transform="translate(570 113)"><rect width="156" height="137" rx="16" fill="#261e3d" stroke="#a78bfa"/><circle cx="78" cy="40" r="21" fill="#a78bfa" fill-opacity=".16"/><path d="M62 47l10-10 8 6 15-17" fill="none" stroke="#c5b5ff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><circle cx="62" cy="47" r="3" fill="#c5b5ff"/><circle cx="72" cy="37" r="3" fill="#c5b5ff"/><circle cx="80" cy="43" r="3" fill="#c5b5ff"/><circle cx="95" cy="26" r="3" fill="#c5b5ff"/><text x="78" y="92" fill="#fff" font-size="16" font-weight="700">INSIGHT</text><text x="78" y="114" fill="#b6a9d7" font-size="11">Explain what matters</text></g>
    <g transform="translate(836 113)"><rect width="226" height="137" rx="16" fill="#102f25" stroke="#52f0ae"/><circle cx="113" cy="40" r="21" fill="#52f0ae" fill-opacity=".16"><animate attributeName="r" values="19;25;19" dur="1.8s" repeatCount="indefinite"/></circle><path d="M101 40l8 8 17-19" fill="none" stroke="#87f8c3" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><text x="113" y="92" fill="#fff" font-size="16" font-weight="700">PRODUCT IMPROVEMENT</text><text x="113" y="114" fill="#9ccdb3" font-size="11">Make a confident next move</text></g>
  </g>
  <g font-family="Arial, Helvetica, sans-serif"><rect x="42" y="268" width="242" height="22" rx="11" fill="#172638"/><text x="163" y="283" text-anchor="middle" fill="#7fdfff" font-size="10" font-weight="700" letter-spacing="1">DATA IS THE BRIDGE</text><text x="1058" y="283" text-anchor="end" fill="#8ea6b8" font-size="11">QUESTION → MEASURE → LEARN → SHIP</text></g>
</svg>'''

ACTIVITY_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 265" role="img" aria-labelledby="title desc">
  <title id="title">Animated GitHub activity stream</title><desc id="desc">A live-style signal line representing continued building and sharing on GitHub.</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1"><stop stop-color="#0a121f"/><stop offset="1" stop-color="#101222"/></linearGradient>
    <linearGradient id="fill" x1="0" x2="0" y1="0" y2="1"><stop stop-color="#2bd9ff" stop-opacity=".34"/><stop offset="1" stop-color="#2bd9ff" stop-opacity="0"/></linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="1100" height="265" rx="20" fill="url(#bg)"/><rect x="1" y="1" width="1098" height="263" rx="19" fill="none" stroke="#2d445f"/>
  <g font-family="Arial, Helvetica, sans-serif"><text x="42" y="48" fill="#f8fbff" font-size="23" font-weight="700">BUILD ACTIVITY STREAM</text><text x="42" y="72" fill="#93a8bd" font-size="13" letter-spacing="1.1">A VISUAL SIGNAL THAT MOVES WHEN YOU KEEP BUILDING</text><g transform="translate(871 31)"><rect width="185" height="28" rx="14" fill="#0f3027" stroke="#52f0ae" stroke-opacity=".7"/><circle cx="18" cy="14" r="5" fill="#52f0ae"><animate attributeName="opacity" values="1;.25;1" dur="1.3s" repeatCount="indefinite"/></circle><text x="34" y="19" fill="#89f7c3" font-size="11" font-weight="700" letter-spacing="1">KEEP SHIPPING</text></g></g>
  <g stroke="#62809b" stroke-opacity=".2"><path d="M48 112H1052M48 150H1052M48 188H1052M48 226H1052"/><path d="M88 95V229M218 95V229M348 95V229M478 95V229M608 95V229M738 95V229M868 95V229M998 95V229"/></g>
  <path d="M50 226 L112 226 L150 209 L193 219 L240 189 L286 204 L330 161 L375 190 L425 174 L469 198 L520 145 L568 172 L618 136 L666 157 L711 114 L758 155 L809 131 L859 169 L909 103 L958 126 L1002 86 L1050 116 L1050 226 Z" fill="url(#fill)"/>
  <path d="M50 226 L112 226 L150 209 L193 219 L240 189 L286 204 L330 161 L375 190 L425 174 L469 198 L520 145 L568 172 L618 136 L666 157 L711 114 L758 155 L809 131 L859 169 L909 103 L958 126 L1002 86 L1050 116" fill="none" stroke="#2bd9ff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"><animate attributeName="stroke-dashoffset" values="100;0;0;100" dur="7s" repeatCount="indefinite"/></path>
  <g fill="#a78bfa" filter="url(#glow)"><circle cx="330" cy="161" r="4"><animate attributeName="r" values="3;7;3" dur="2s" repeatCount="indefinite"/></circle><circle cx="711" cy="114" r="4"><animate attributeName="r" values="3;7;3" begin=".7s" dur="2s" repeatCount="indefinite"/></circle><circle cx="1002" cy="86" r="5"><animate attributeName="r" values="4;9;4" begin="1.2s" dur="2s" repeatCount="indefinite"/></circle></g>
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#87a1b7"><text x="50" y="249">START</text><text x="968" y="249">NEXT PUSH</text></g>
</svg>'''

COLLAB_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 275" role="img" aria-labelledby="title desc">
  <title id="title">Collaboration network</title><desc id="desc">An animated network that connects code, data, and ideas.</desc>
  <defs><linearGradient id="bg" x1="0" x2="1"><stop stop-color="#0c1420"/><stop offset="1" stop-color="#101b2a"/></linearGradient><linearGradient id="line" x1="0" x2="1"><stop stop-color="#2bd9ff"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#52f0ae"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <rect width="1100" height="275" rx="20" fill="url(#bg)"/><rect x="1" y="1" width="1098" height="273" rx="19" fill="none" stroke="#334b66"/>
  <g font-family="Arial, Helvetica, sans-serif"><text x="42" y="49" fill="#f8fbff" font-size="23" font-weight="700">COLLABORATION NETWORK</text><text x="42" y="73" fill="#9cb1c5" font-size="13" letter-spacing="1.2">GOOD WORK GROWS FASTER WHEN IDEAS MOVE BETWEEN PEOPLE</text></g>
  <path d="M220 172 C350 96 437 92 550 151 S757 218 880 131" fill="none" stroke="url(#line)" stroke-width="4" stroke-linecap="round" opacity=".8"/>
  <path d="M220 172 C350 96 437 92 550 151 S757 218 880 131" fill="none" stroke="#effdff" stroke-width="2" stroke-dasharray="8 18" opacity=".75"><animate attributeName="stroke-dashoffset" from="0" to="-52" dur="1.7s" repeatCount="indefinite"/></path>
  <circle r="6" fill="#fff" filter="url(#glow)"><animateMotion dur="4s" repeatCount="indefinite" path="M220 172 C350 96 437 92 550 151 S757 218 880 131"/></circle>
  <g font-family="Arial, Helvetica, sans-serif" text-anchor="middle"><g transform="translate(160 172)"><circle r="58" fill="#112a38" stroke="#2bd9ff" stroke-width="2"/><text y="-5" fill="#f8fbff" font-size="18" font-weight="700">CODE</text><text y="17" fill="#9fc7d6" font-size="11">build together</text></g><g transform="translate(550 151)"><circle r="66" fill="#241d39" stroke="#a78bfa" stroke-width="2"/><circle r="49" fill="none" stroke="#a78bfa" stroke-opacity=".35" stroke-dasharray="3 7"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="8s" repeatCount="indefinite"/></circle><text y="-5" fill="#f8fbff" font-size="18" font-weight="700">IDEAS</text><text y="17" fill="#bbadd9" font-size="11">share freely</text></g><g transform="translate(940 131)"><circle r="58" fill="#123127" stroke="#52f0ae" stroke-width="2"/><text y="-5" fill="#f8fbff" font-size="18" font-weight="700">DATA</text><text y="17" fill="#9bcbb1" font-size="11">learn together</text></g></g>
  <g font-family="Arial, Helvetica, sans-serif"><rect x="42" y="231" width="304" height="22" rx="11" fill="#172638"/><text x="194" y="246" text-anchor="middle" fill="#74ddff" font-size="10" font-weight="700" letter-spacing="1">OPEN TO FEEDBACK &amp; PROJECT TALKS</text><text x="1057" y="246" text-anchor="end" fill="#89a1b6" font-size="11">LET’S BUILD SOMETHING USEFUL</text></g>
</svg>'''


def link_card(label: str, value: str, color: str, code: str) -> str:
    """Return a compact, animated navigation card with no external assets."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 510 98" role="img" aria-label="{label}: {value}">
  <defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#0b1422"/><stop offset="1" stop-color="#151c2a"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
  <rect width="510" height="98" rx="15" fill="url(#g)"/><rect x="1" y="1" width="508" height="96" rx="14" fill="none" stroke="{color}" stroke-opacity=".55"/>
  <rect x="0" y="0" width="7" height="98" rx="3" fill="{color}" filter="url(#glow)"/><circle cx="45" cy="49" r="22" fill="{color}" fill-opacity=".13" stroke="{color}"/>
  <text x="45" y="54" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="{color}">{code}</text>
  <text x="84" y="39" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" letter-spacing="1.6" fill="#9ab0c5">{label.upper()}</text>
  <text x="84" y="66" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#f8fbff">{value}</text>
  <circle cx="475" cy="49" r="5" fill="{color}"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle>
</svg>'''


def main() -> None:
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(SVG, encoding="utf-8")
    IMPACT_OUTPUT.write_text(IMPACT_SVG, encoding="utf-8")
    ACTIVITY_OUTPUT.write_text(ACTIVITY_SVG, encoding="utf-8")
    COLLAB_OUTPUT.write_text(COLLAB_SVG, encoding="utf-8")
    LINKS_DIR.mkdir(exist_ok=True)
    cards = {
        "github.svg": ("GitHub", "Chiranjeeb1101", "#2bd9ff", "GH"),
        "journey.svg": ("Roadmap", "Data Analyst Journey", "#a78bfa", "01"),
        "linkedin.svg": ("LinkedIn", "Chiranjeeb Kumar Sahoo", "#58a6ff", "in"),
        "email.svg": ("Email", "Let’s connect", "#52f0ae", "@"),
    }
    for filename, (label, value, color, code) in cards.items():
        (LINKS_DIR / filename).write_text(link_card(label, value, color, code), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)}")
    print(f"Generated {IMPACT_OUTPUT.relative_to(ROOT)}")
    print(f"Generated {ACTIVITY_OUTPUT.relative_to(ROOT)}")
    print(f"Generated {COLLAB_OUTPUT.relative_to(ROOT)}")
    print(f"Generated navigation cards in {LINKS_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
