import base64, cairosvg, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAVY = "#0B1F45"
NAVY2 = "#13295A"
CREAM = "#F5ECDC"
WHITE = "#FFFFFF"
GOLD = "#D9A441"
BRICK = "#B5432F"
TEAL = "#1F6F78"
WARM = "#D9894A"
COOL = "#7FA7C9"
PTS = [(-74, -30), (-44, 44), (-20, -6), (4, 44), (30, -52), (62, 50)]
_n = [0]


def street_svg(n=12, w=1440, h=300, warmset=(2, 5, 9), coolset=(0, 7, 11), base=NAVY, line=CREAM, seed=3):
    import random
    r = random.Random(seed)
    out = [
        '<defs><filter id="win-glow" x="-60%" y="-60%" width="220%" height="220%">'
        '<feGaussianBlur stdDeviation="3.2" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
        "</filter></defs>"
    ]
    hw = w / n
    for i in range(n):
        bh = r.choice([130, 150, 170, 190])
        roof = r.choice(["gable", "flat", "gable", "step"])
        bw = hw - 8
        x0 = i * hw + 4
        y0 = h - bh
        out.append(
            f'<rect x="{x0:.0f}" y="{y0}" width="{bw:.0f}" height="{bh}" fill="{base}" stroke="{line}" stroke-width="2"/>'
        )
        if roof == "gable":
            out.append(
                f'<polygon points="{x0-4:.0f},{y0} {x0+bw/2:.0f},{y0-46} {x0+bw+4:.0f},{y0}" fill="{base}" stroke="{line}" stroke-width="2"/>'
            )
        elif roof == "step":
            out.append(
                f'<rect x="{x0+bw*.6:.0f}" y="{y0-34}" width="14" height="34" fill="{base}" stroke="{line}" stroke-width="2"/>'
            )
        lit = i in warmset or i in coolset
        col = WARM if i in warmset else (COOL if i in coolset else CREAM)
        op = 1 if lit else 0.35
        filt = ' filter="url(#win-glow)"' if lit else ""
        for yy in range(y0 + 18, h - 50, 38):
            for k in (0, 1):
                wx = x0 + bw * (0.18 + k * 0.46)
                out.append(
                    f'<rect x="{wx:.0f}" y="{yy}" width="{bw*.2:.0f}" height="22" rx="2" fill="{col}" opacity="{op}"{filt}/>'
                )
        out.append(
            f'<rect x="{x0+bw*.4:.0f}" y="{h-42}" width="{bw*.2:.0f}" height="42" fill="{line}" opacity=".85"/>'
        )
    return (
        f'<svg class="street" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMax meet" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
        + "".join(out)
        + f'<rect y="{h-2}" width="{w}" height="2" fill="{line}"/></svg>'
    )




def mono(fg, bg, acc=None, ring=None, label="Watson Atlas"):
    _n[0] += 1
    mid = f"wa-ko{_n[0]}"
    p = " ".join(f"{x},{y}" for x, y in PTS)
    ko = "".join(
        f'<polyline points="{a[0]},{a[1]} {b[0]},{b[1]}" stroke="#000" stroke-width="19" stroke-linecap="butt"/>'
        for a, b in [(PTS[0], PTS[1]), (PTS[4], PTS[5])]
    )
    pa = " ".join(f"{x},{y}" for x, y in PTS[3:])
    aa = (
        f'<polyline points="{pa}" fill="none" stroke="{acc}" stroke-width="9" stroke-linejoin="miter" stroke-miterlimit="10"/>'
        if acc
        else ""
    )
    return (
        f'<svg class="mono" viewBox="-90 -90 180 180" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">'
        f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-90" y="-90" width="180" height="180"><rect x="-90" y="-90" width="180" height="180" fill="#fff"/>{ko}</mask>'
        f'<circle r="80" fill="none" stroke="{ring or fg}" stroke-width="6" mask="url(#{mid})"/>'
        f'<polyline points="{p}" fill="none" stroke="{fg}" stroke-width="9" stroke-linejoin="miter" stroke-miterlimit="10"/>{aa}</svg>'
    )


def icon_svg(fg="#FFFFFF", bg=NAVY):
    p = " ".join(f"{512 + x * 4.4:.1f},{512 + y * 4.4:.1f}" for x, y in PTS)
    ko = "".join(
        f'<polyline points="{512 + a[0] * 4.4:.1f},{512 + a[1] * 4.4:.1f} {512 + b[0] * 4.4:.1f},{512 + b[1] * 4.4:.1f}" stroke="{bg}" stroke-width="83.6"/>'
        for a, b in [(PTS[0], PTS[1]), (PTS[4], PTS[5])]
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" rx="220" fill="{bg}"/>'
        f'<circle cx="512" cy="512" r="352" fill="none" stroke="{fg}" stroke-width="26.4"/>{ko}'
        f'<polyline points="{p}" fill="none" stroke="{fg}" stroke-width="39.6" stroke-linejoin="miter" stroke-miterlimit="10"/></svg>'
    )


def ic(path):
    return f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'


ICONS = {
    "resonest": '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M12 12l9-5M12 12v10M12 12L3 7"/>',
    "siteops": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "safety": '<path d="M3 21h18"/><path d="M5 21V8l7-5 7 5v13"/><path d="M9 21v-8h6v8"/>',
    "field": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "data": '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v4c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 10v4c0 1.7 3.6 3 8 3s8-1.3 8-3v-4M4 14v4c0 1.7 3.6 3 8 3s8-1.3 8-3v-4"/>',
    "integrate": '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M8 7.5l2.5 7M16 7.5l-2.5 7M8.5 6h7"/>',
    "bespoke": '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6M14 4l-4 16"/>',
}
products = [
    (
        "resonest",
        "resonest",
        "Resonest",
        "Built for Awaab's Law, Resonest is a privacy-first digital twin that helps social landlords get ahead of damp, mould and cold homes.",
        [
            "Uses existing property and weather data, with no in-home sensors or tenant monitoring",
            "Shows which homes will struggle first in winter, and why",
            "Highlights which low-cost improvements will make homes safer and cheaper to keep warm",
            "Helps teams meet Awaab's Law with confidence, with clear action lists and deadlines for every home",
            "Keeps an audit trail of what was done and what changed",
        ],
        "",
    ),
    (
        "siteops",
        "siteops",
        "SiteOps",
        "A housing compliance platform for capturing inspections on site and turning them into consistent, branded PDF reports, tied to the right property. It works alongside a landlord's existing housing system, rather than replacing it.",
        [
            "On-site inspection capture and branded PDF reports for fire risk assessments, electrical work, and building and tower-block surveys",
            "A property register keyed on UPRN, with EPC and condition information",
            "A no-code form and report designer",
            "Job planning to schedule, assign and track inspection programmes",
            "A mobile app for on-site capture against the same forms",
        ],
        "A repairs and maintenance module is on the SiteOps roadmap.",
    ),
]
services = [
    ("safety", "Building safety &amp; cladding reporting", "A specialist operational and reporting system for building-safety work, including Fire Risk Appraisal of External Walls (FRAEW), desktop assessments, EWS1 and site-visit reports, with configurable forms, specialist PDFs, job management and a connected surveyor app."),
    ("field", "Field &amp; surveyor app", "A mobile app, in live use, for surveyors and assessors to capture inspection evidence on site, including photographs, geotagged data and offline capture, against the same structured forms used in the web platform."),
    ("data", "Property data", "UPRN address verification, EPC certificate lookup and import from the register, and weather data. These already underpin Resonest and the SiteOps property register, including fabric and condition information on each home."),
    ("integrate", "Integrations", "When a landlord already has a housing or asset system, we connect rather than replace it. Property records, inspection results, generated reports and remedial actions can be exchanged, using UPRN as the common property reference."),
    ("bespoke", "Bespoke housing software", "When off-the-shelf software does not quite fit, we design around the requirement, including specialist operational systems and controlled integration with the systems you already use."),
]
steps = [
    ("01", "Define", "We start with people: residents, users, workflows, integrations and what success looks like."),
    ("02", "Prototype", "Narrow, early versions on representative data, so everyone can see and shape the direction."),
    ("03", "Build", "Delivery in stages, with source control, automated testing and staging environments."),
    ("04", "Verify", "Careful checks against agreed acceptance criteria before anything goes live."),
    ("05", "Deploy", "A smooth handover into everyday use, with ongoing support as needs grow."),
]
values = [
    ("Relationship before business", "We invest in understanding your organisation, your residents and your goals. Long-term partnerships come first."),
    ("Always looking forward", "We focus on what could work better tomorrow, and on practical steps to get there."),
    ("Big aspirations", "We believe every home deserves great care, and that great software can help make that happen at scale."),
    ("Evidence before claims", "We prove ideas on real requirements before scaling them, so every step forward is a confident one."),
]
sectors = [
    ("Housing associations", "Software that helps teams care for homes and communities, from compliance and property data to seeing which homes will struggle first in winter."),
    ("Local authorities", "Tools for council housing teams, including compliance, property data and a clear view of thermal risk across a portfolio."),
    ("Residential landlords", "The same warmth, fabric and compliance tools, for large residential landlords as well as social landlords."),
    ("Building safety consultancies", "Specialist systems for building-safety work, including FRAEW, EWS1, desktop assessments and site-visit reports, with a connected surveyor app."),
    ("Partners and programmes", "We can work alongside your existing teams and systems, taking on specialist software, integration and reporting."),
]

contours = "".join(
    f'<path d="M-50 {y} C 250 {y-60+i*7}, 450 {y+70-i*5}, 700 {y-10} S 1150 {y+50}, 1500 {y-30}" />'
    for i, y in enumerate(range(40, 900, 48))
)
grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="900"/>' for x in range(0, 1500, 120)) + "".join(
    f'<line x1="0" y1="{y}" x2="1500" y2="{y}"/>' for y in range(0, 900, 120)
)
hero_bg = (
    f'<svg class="map" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
    f'<g class="grid">{grid}</g><g class="contours">{contours}</g>'
    f'<g class="pins"><circle cx="1080" cy="300" r="5"/><circle cx="1180" cy="520" r="5"/>'
    f'<circle cx="930" cy="610" r="5"/><circle cx="1290" cy="380" r="5"/>'
    f'<path d="M1080 300 L1180 520 L930 610 M1180 520 L1290 380" /></g></svg>'
)

MAIL = "info@rowe.ai"
mailto = f"mailto:{MAIL}?subject=Hello%20Watson%20Atlas"

FONT64 = base64.b64encode((ROOT / "assets/montserrat.woff2").read_bytes()).decode()


def root_css(t):
    keys = [
        "navy", "navy2", "cream", "white", "ink", "muted", "line", "heading",
        "header-fg", "header-scrolled-bg", "header-scrolled-fg", "header-shadow",
        "nav-hover", "btn", "btn-fg", "btn-hover", "ghost-border", "ghost-fg", "ghost-hover",
        "hero-bg", "hero-fg", "hero-accent", "map-grid", "map-contour", "map-pin", "map-path",
        "strip-bg", "strip-fg", "strip-dot", "strip-line", "eyebrow", "body-bg",
        "alt-bg", "about-bg", "card-bg", "card-hover", "card-shadow", "icon-bg", "icon-fg",
        "step-num", "value-bg", "value-fg", "value-h", "value-ring", "partner-bg", "partner-fg",
        "sector-bg", "sector-accent", "about-card-bg", "about-card-fg", "facts-bg", "facts-fg",
        "contact-bg", "contact-fg", "footer-bg", "footer-fg", "footer-link", "footer-hover",
    ]
    return ";".join(f"--{k}:{t[k]}" for k in keys)


# Legacy published palette (gold / brick accents), kept for reference.
# Default build is Classic Navy: `python3 build.py` writes it to index.html.
DEFAULT = {
    "id": "default",
    "label": "Current",
    "theme_color": NAVY,
    "navy": NAVY, "navy2": NAVY2, "cream": CREAM, "white": WHITE,
    "ink": "#16223B", "muted": "#56607A", "line": "rgba(11,31,69,.12)", "heading": NAVY,
    "header-fg": WHITE, "header-scrolled-bg": "rgba(11,31,69,.96)", "header-scrolled-fg": WHITE,
    "header-shadow": "0 6px 24px rgba(0,0,0,.18)", "nav-hover": GOLD,
    "btn": GOLD, "btn-fg": NAVY, "btn-hover": "#E6B65A",
    "ghost-border": "rgba(255,255,255,.55)", "ghost-fg": WHITE, "ghost-hover": GOLD,
    "hero-bg": f"radial-gradient(1200px 600px at 80% 20%,#1A3470 0%,{NAVY} 60%)",
    "hero-fg": WHITE, "hero-accent": GOLD,
    "map-grid": "rgba(255,255,255,.05)", "map-contour": "rgba(217,164,65,.18)",
    "map-pin": GOLD, "map-path": "rgba(217,164,65,.55)",
    "strip-bg": NAVY2, "strip-fg": WHITE, "strip-dot": GOLD, "strip-line": "transparent",
    "eyebrow": BRICK, "body-bg": "#FBF8F2", "alt-bg": CREAM, "about-bg": WHITE,
    "card-bg": WHITE, "card-hover": "rgba(217,164,65,.6)", "card-shadow": "0 18px 40px rgba(11,31,69,.10)",
    "icon-bg": CREAM, "icon-fg": BRICK, "step-num": BRICK,
    "value-bg": NAVY, "value-fg": WHITE, "value-h": GOLD, "value-ring": "rgba(217,164,65,.35)",
    "partner-bg": TEAL, "partner-fg": WHITE,
    "sector-bg": WHITE, "sector-accent": TEAL,
    "about-card-bg": NAVY, "about-card-fg": WHITE, "facts-bg": CREAM, "facts-fg": NAVY,
    "contact-bg": f"linear-gradient(135deg,{NAVY},#183466)", "contact-fg": WHITE,
    "footer-bg": "#071530", "footer-fg": "rgba(255,255,255,.75)",
    "footer-link": "rgba(255,255,255,.85)", "footer-hover": GOLD,
    "logo_header": (WHITE, NAVY, GOLD),
    "logo_hero": (WHITE, "#15306A", GOLD),
    "logo_about": (WHITE, NAVY, GOLD),
    "logo_footer": (WHITE, "#071530", GOLD),
    "header_logo_current": False,
    "footer_logo_current": False,
    "sector_rainbow": True,
    "favicon": (WHITE, NAVY),
}

CLASSIC_NAVY = {
    "id": "classic-navy",
    "label": "Classic Navy",
    "theme_color": NAVY,
    "navy": NAVY, "navy2": NAVY2, "cream": CREAM, "white": WHITE,
    "ink": NAVY, "muted": "rgba(11,31,69,.62)", "line": "rgba(11,31,69,.12)", "heading": NAVY,
    "header-fg": WHITE, "header-scrolled-bg": "rgba(11,31,69,.96)", "header-scrolled-fg": WHITE,
    "header-shadow": "0 6px 24px rgba(0,0,0,.18)", "nav-hover": CREAM,
    "btn": CREAM, "btn-fg": NAVY, "btn-hover": WHITE,
    "ghost-border": "rgba(255,255,255,.55)", "ghost-fg": WHITE, "ghost-hover": CREAM,
    "hero-bg": f"radial-gradient(1200px 600px at 80% 20%,{NAVY2} 0%,{NAVY} 60%)",
    "hero-fg": WHITE, "hero-accent": CREAM,
    "map-grid": "rgba(255,255,255,.05)", "map-contour": "rgba(245,236,220,.22)",
    "map-pin": CREAM, "map-path": "rgba(245,236,220,.55)",
    "strip-bg": NAVY2, "strip-fg": WHITE, "strip-dot": CREAM, "strip-line": "transparent",
    "eyebrow": NAVY, "body-bg": WHITE, "alt-bg": CREAM, "about-bg": WHITE,
    "card-bg": WHITE, "card-hover": "rgba(11,31,69,.35)", "card-shadow": "0 18px 40px rgba(11,31,69,.10)",
    "icon-bg": CREAM, "icon-fg": NAVY, "step-num": NAVY,
    "value-bg": NAVY, "value-fg": WHITE, "value-h": CREAM, "value-ring": "rgba(245,236,220,.35)",
    "partner-bg": NAVY2, "partner-fg": WHITE,
    "sector-bg": WHITE, "sector-accent": NAVY,
    "about-card-bg": NAVY, "about-card-fg": WHITE, "facts-bg": CREAM, "facts-fg": NAVY,
    "contact-bg": f"linear-gradient(135deg,{NAVY},{NAVY2})", "contact-fg": WHITE,
    "footer-bg": NAVY, "footer-fg": "rgba(255,255,255,.75)",
    "footer-link": "rgba(255,255,255,.85)", "footer-hover": CREAM,
    "logo_header": ("currentColor", NAVY, None),
    "logo_hero": (WHITE, NAVY2, None),
    "logo_about": (WHITE, NAVY, None),
    "logo_footer": ("currentColor", NAVY, None),
    "header_logo_current": True,
    "footer_logo_current": True,
    "sector_rainbow": False,
    "favicon": (WHITE, NAVY),
    "palette": [("Navy", NAVY), ("Cream", CREAM), ("White", WHITE), ("Mid navy", NAVY2)],
}

CREAM_HERITAGE = {
    "id": "cream-heritage",
    "label": "Cream Heritage",
    "theme_color": NAVY,
    "navy": NAVY, "navy2": NAVY2, "cream": CREAM, "white": WHITE,
    "ink": NAVY, "muted": "rgba(11,31,69,.62)", "line": "rgba(11,31,69,.12)", "heading": NAVY,
    "header-fg": WHITE, "header-scrolled-bg": "rgba(245,236,220,.96)", "header-scrolled-fg": NAVY,
    "header-shadow": "0 6px 24px rgba(11,31,69,.08)", "nav-hover": NAVY2,
    "btn": NAVY, "btn-fg": CREAM, "btn-hover": NAVY2,
    "ghost-border": "rgba(255,255,255,.55)", "ghost-fg": WHITE, "ghost-hover": CREAM,
    "hero-bg": f"radial-gradient(1200px 600px at 80% 20%,{NAVY2} 0%,{NAVY} 60%)",
    "hero-fg": WHITE, "hero-accent": CREAM,
    "map-grid": "rgba(255,255,255,.05)", "map-contour": "rgba(245,236,220,.22)",
    "map-pin": CREAM, "map-path": "rgba(245,236,220,.55)",
    "strip-bg": NAVY2, "strip-fg": WHITE, "strip-dot": CREAM, "strip-line": "transparent",
    "eyebrow": NAVY, "body-bg": CREAM, "alt-bg": CREAM, "about-bg": CREAM,
    "card-bg": WHITE, "card-hover": "rgba(11,31,69,.28)", "card-shadow": "0 18px 40px rgba(11,31,69,.08)",
    "icon-bg": CREAM, "icon-fg": NAVY, "step-num": NAVY,
    "value-bg": WHITE, "value-fg": NAVY, "value-h": NAVY, "value-ring": "rgba(11,31,69,.16)",
    "partner-bg": WHITE, "partner-fg": NAVY,
    "sector-bg": WHITE, "sector-accent": NAVY,
    "about-card-bg": WHITE, "about-card-fg": NAVY, "facts-bg": WHITE, "facts-fg": NAVY,
    "contact-bg": CREAM, "contact-fg": NAVY,
    "footer-bg": CREAM, "footer-fg": "rgba(11,31,69,.7)",
    "footer-link": NAVY, "footer-hover": NAVY2,
    "logo_header": ("currentColor", NAVY, None),
    "logo_hero": (WHITE, NAVY2, None),
    "logo_about": (NAVY, WHITE, None),
    "logo_footer": ("currentColor", CREAM, None),
    "header_logo_current": True,
    "footer_logo_current": True,
    "sector_rainbow": False,
    "favicon": (NAVY, CREAM),
    "palette": [("Cream", CREAM), ("Navy", NAVY), ("White", WHITE), ("Mid navy", NAVY2)],
}

CRISP_WHITE = {
    "id": "crisp-white",
    "label": "Crisp White",
    "theme_color": NAVY,
    "navy": NAVY, "navy2": NAVY2, "cream": CREAM, "white": WHITE,
    "ink": NAVY, "muted": "rgba(11,31,69,.62)", "line": "rgba(11,31,69,.10)", "heading": NAVY,
    "header-fg": NAVY, "header-scrolled-bg": "rgba(255,255,255,.96)", "header-scrolled-fg": NAVY,
    "header-shadow": "0 6px 24px rgba(11,31,69,.08)", "nav-hover": NAVY2,
    "btn": NAVY, "btn-fg": WHITE, "btn-hover": NAVY2,
    "ghost-border": "rgba(11,31,69,.4)", "ghost-fg": NAVY, "ghost-hover": NAVY2,
    "hero-bg": f"radial-gradient(1200px 600px at 80% 20%,{WHITE} 0%,{CREAM} 55%)",
    "hero-fg": NAVY, "hero-accent": NAVY,
    "map-grid": "rgba(11,31,69,.06)", "map-contour": "rgba(11,31,69,.16)",
    "map-pin": NAVY, "map-path": "rgba(11,31,69,.4)",
    "strip-bg": WHITE, "strip-fg": NAVY, "strip-dot": NAVY, "strip-line": "rgba(11,31,69,.12)",
    "eyebrow": NAVY, "body-bg": WHITE, "alt-bg": WHITE, "about-bg": WHITE,
    "card-bg": CREAM, "card-hover": "rgba(11,31,69,.28)", "card-shadow": "0 18px 40px rgba(11,31,69,.08)",
    "icon-bg": WHITE, "icon-fg": NAVY, "step-num": NAVY,
    "value-bg": CREAM, "value-fg": NAVY, "value-h": NAVY, "value-ring": "rgba(11,31,69,.16)",
    "partner-bg": CREAM, "partner-fg": NAVY,
    "sector-bg": CREAM, "sector-accent": NAVY,
    "about-card-bg": CREAM, "about-card-fg": NAVY, "facts-bg": CREAM, "facts-fg": NAVY,
    "contact-bg": WHITE, "contact-fg": NAVY,
    "footer-bg": WHITE, "footer-fg": "rgba(11,31,69,.7)",
    "footer-link": NAVY, "footer-hover": NAVY2,
    "logo_header": ("currentColor", WHITE, None),
    "logo_hero": (NAVY, CREAM, None),
    "logo_about": (NAVY, CREAM, None),
    "logo_footer": ("currentColor", WHITE, None),
    "header_logo_current": True,
    "footer_logo_current": True,
    "sector_rainbow": False,
    "favicon": (NAVY, WHITE),
    "palette": [("White", WHITE), ("Navy", NAVY), ("Cream", CREAM), ("Mid navy", NAVY2)],
}

DEEP_NAVY = {
    "id": "deep-navy",
    "label": "Deep Navy",
    "theme_color": NAVY,
    "navy": NAVY, "navy2": NAVY2, "cream": CREAM, "white": WHITE,
    "ink": WHITE, "muted": "rgba(255,255,255,.72)", "line": "rgba(245,236,220,.16)", "heading": CREAM,
    "header-fg": CREAM, "header-scrolled-bg": "rgba(11,31,69,.96)", "header-scrolled-fg": CREAM,
    "header-shadow": "0 6px 24px rgba(0,0,0,.28)", "nav-hover": WHITE,
    "btn": CREAM, "btn-fg": NAVY, "btn-hover": WHITE,
    "ghost-border": "rgba(245,236,220,.55)", "ghost-fg": CREAM, "ghost-hover": WHITE,
    "hero-bg": f"radial-gradient(1200px 600px at 80% 20%,{NAVY2} 0%,{NAVY} 60%)",
    "hero-fg": WHITE, "hero-accent": CREAM,
    "map-grid": "rgba(255,255,255,.05)", "map-contour": "rgba(245,236,220,.22)",
    "map-pin": CREAM, "map-path": "rgba(245,236,220,.55)",
    "strip-bg": NAVY2, "strip-fg": WHITE, "strip-dot": CREAM, "strip-line": "transparent",
    "eyebrow": CREAM, "body-bg": NAVY, "alt-bg": NAVY2, "about-bg": NAVY,
    "card-bg": NAVY2, "card-hover": "rgba(245,236,220,.45)", "card-shadow": "0 18px 40px rgba(0,0,0,.28)",
    "icon-bg": NAVY, "icon-fg": CREAM, "step-num": CREAM,
    "value-bg": NAVY, "value-fg": WHITE, "value-h": CREAM, "value-ring": "rgba(245,236,220,.35)",
    "partner-bg": NAVY2, "partner-fg": WHITE,
    "sector-bg": NAVY2, "sector-accent": CREAM,
    "about-card-bg": NAVY2, "about-card-fg": CREAM, "facts-bg": NAVY2, "facts-fg": CREAM,
    "contact-bg": f"linear-gradient(135deg,{NAVY},{NAVY2})", "contact-fg": WHITE,
    "footer-bg": NAVY2, "footer-fg": "rgba(255,255,255,.75)",
    "footer-link": "rgba(255,255,255,.85)", "footer-hover": CREAM,
    "logo_header": ("currentColor", NAVY, None),
    "logo_hero": (CREAM, NAVY2, None),
    "logo_about": (CREAM, NAVY2, None),
    "logo_footer": ("currentColor", NAVY2, None),
    "header_logo_current": True,
    "footer_logo_current": True,
    "sector_rainbow": False,
    "favicon": (CREAM, NAVY),
    "palette": [("Navy", NAVY), ("Cream", CREAM), ("White", WHITE), ("Mid navy", NAVY2)],
}

VARIANTS = [CLASSIC_NAVY, CREAM_HERITAGE, CRISP_WHITE, DEEP_NAVY]



def nav_hrefs(page="home"):
    if page == "home":
        return {
            "home": "#main",
            "what": "#what",
            "how": "#how",
            "who": "#who",
            "about": "#about",
            "awaab": "awaabs-law/",
            "help": "help/",
            "contact": "#contact",
            "home_cur": ' aria-current="page"',
            "awaab_cur": "",
            "help_cur": "",
        }
    if page == "awaab":
        return {
            "home": "../",
            "what": "../#what",
            "how": "../#how",
            "who": "../#who",
            "about": "../#about",
            "awaab": "./",
            "help": "../help/",
            "contact": "#contact",
            "home_cur": "",
            "awaab_cur": ' aria-current="page"',
            "help_cur": "",
        }
    return {
        "home": "../",
        "what": "../#what",
        "how": "../#how",
        "who": "../#who",
        "about": "../#about",
        "awaab": "../awaabs-law/",
        "help": "./",
        "contact": "#contact",
        "home_cur": "",
        "awaab_cur": "",
        "help_cur": ' aria-current="page"',
    }


def nav_html(page="home"):
    l = nav_hrefs(page)
    return (
        '<div class="nav-overlay" id="nav-overlay" hidden></div>'
        '<nav class="drawer" id="nav" aria-label="Main menu" aria-hidden="true">'
        '<div class="drawer-head">'
        '<p class="drawer-title" id="menu-title">Menu</p>'
        '<button type="button" class="drawer-close" aria-label="Close menu">'
        '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<path d="M6 6l12 12M18 6L6 18"/></svg></button></div>'
        '<div class="drawer-links">'
        f'<a href="{l["home"]}"{l["home_cur"]}>Home</a>'
        f'<a href="{l["what"]}">What we do</a>'
        f'<a href="{l["awaab"]}"{l["awaab_cur"]}>Awaab\'s Law</a>'
        f'<a href="{l["how"]}">How we work</a>'
        f'<a href="{l["who"]}">Who we work with</a>'
        f'<a href="{l["help"]}"{l["help_cur"]}>How can we help?</a>'
        f'<a href="{l["about"]}">About</a>'
        f'</div>'
        f'<a class="btn gold drawer-cta" href="{l["contact"]}">Get in touch</a>'
        "</nav>"
    )


CE_BADGE = (
    '<div class="ce-badge"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/>'
    '<path d="M8.5 12l2.5 2.5 4.5-5"/></svg>'
    "<span>Cyber Essentials Certified</span></div>"
)


def header_html(t, page="home"):
    lh, lb, la = t["logo_header"]
    l = nav_hrefs(page)
    brand = l["home"]
    return (
        '<header class="top" id="top">\n'
        ' <div class="wrap bar">\n'
        f'  <a class="brand" href="{brand}" aria-label="Watson Atlas home">{mono(lh, lb, la)}<div><b>WATSON</b><span>ATLAS</span></div></a>\n'
        '  <div class="tools">'
        f'<a class="home-link" href="{l["home"]}"{l["home_cur"]}>Home</a>'
        '<button type="button" class="menu" aria-label="Open menu" aria-expanded="false" aria-controls="nav">'
        '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'
        "</div>\n"
        " </div>\n"
        "</header>\n"
        f"{nav_html(page)}"
    )


def footer_html(t, page="home"):
    fh, fb, fa = t["logo_footer"]
    brand = "#main" if page == "home" else "../"
    return (
        "<footer>\n"
        ' <div class="wrap">\n'
        f'  <a class="brand" href="{brand}" aria-label="Back to top">{mono(fh, fb, fa)}<div><b>WATSON</b><span>ATLAS</span></div></a>\n'
        "  <p>© 2026 Watson Atlas. A Rowe AI Ltd brand. Registered in Scotland, company no. SC770018.</p>\n"
        f"  {CE_BADGE}\n"
        f'  <a href="mailto:{MAIL}">{MAIL}</a>\n'
        " </div>\n"
        "</footer>"
    )


def entry_script(page="home"):
    """Mark this tab as in-site once Home (or a later page) has loaded.

    Subpages only send the visitor to / when this tab has no flag at all
    (a fresh entry). If the flag is present, or sessionStorage is blocked,
    they never redirect, so menu navigation always works. The flag is also
    set on the next click of any same-origin link.
    """
    if page == "home":
        return """<script>
(function(){
  try{history.scrollRestoration='manual'}catch(e){}
  var seen=false,storageOk=true;
  try{seen=sessionStorage.getItem('wa-atlas-entry')==='1'}catch(e){storageOk=false}
  if(!seen){
    if(location.hash){
      try{history.replaceState(null,'',location.pathname+location.search)}catch(e){}
    }
    window.scrollTo(0,0);
    function top(){window.scrollTo(0,0)}
    document.addEventListener('DOMContentLoaded',top);
    window.addEventListener('load',top);
    window.addEventListener('pageshow',function(e){if(e.persisted)top()});
  }
  if(storageOk){try{sessionStorage.setItem('wa-atlas-entry','1')}catch(e){}}
})();
</script>"""
    return """<script>
(function(){
  var seen=false,storageOk=true;
  try{seen=sessionStorage.getItem('wa-atlas-entry')==='1'}catch(e){storageOk=false}
  if(!storageOk) return;
  if(!seen){location.replace('/');return}
})();
</script>"""


def site_script():
    return """<script>
(function(){
 document.addEventListener('click',function(e){
  var a=e.target&&e.target.closest?e.target.closest('a[href]'):null;
  if(!a) return;
  var href=a.getAttribute('href')||'';
  if(!href||/^(mailto:|tel:|javascript:)/i.test(href)) return;
  try{
   var u=new URL(a.href,location.href);
   if(u.origin===location.origin) sessionStorage.setItem('wa-atlas-entry','1');
  }catch(err){}
 },true);
 var h=document.getElementById('top');
 var b=document.querySelector('.menu');
 var n=document.getElementById('nav');
 var ov=document.getElementById('nav-overlay');
 var x=document.querySelector('.drawer-close');
 var last=null;
 function scrolled(){h.classList.toggle('scrolled',window.scrollY>20)}
 scrolled();window.addEventListener('scroll',scrolled,{passive:true});
 function focusables(){return n.querySelectorAll('a,button,[tabindex]:not([tabindex="-1"])')}
 function isOpen(){return n.classList.contains('open')}
 function openMenu(){
  last=document.activeElement;
  n.classList.add('open');ov.classList.add('open');h.classList.add('open');
  document.body.classList.add('menu-open');
  b.setAttribute('aria-expanded','true');
  n.setAttribute('aria-hidden','false');
  ov.removeAttribute('hidden');
  (x||focusables()[0]).focus();
 }
 function closeMenu(){
  n.classList.remove('open');ov.classList.remove('open');h.classList.remove('open');
  document.body.classList.remove('menu-open');
  b.setAttribute('aria-expanded','false');
  n.setAttribute('aria-hidden','true');
  ov.setAttribute('hidden','');
  if(last&&last.focus) last.focus();
 }
 b.addEventListener('click',function(){isOpen()?closeMenu():openMenu()});
 if(x) x.addEventListener('click',closeMenu);
 ov.addEventListener('click',closeMenu);
 document.addEventListener('keydown',function(e){
  if(!isOpen()) return;
  if(e.key==='Escape'){e.preventDefault();closeMenu();return}
  if(e.key!=='Tab') return;
  var f=[].slice.call(focusables());
  if(!f.length) return;
  var first=f[0],lastEl=f[f.length-1];
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();lastEl.focus()}
  else if(!e.shiftKey&&document.activeElement===lastEl){e.preventDefault();first.focus()}
 });
 n.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeMenu)});
 var els=document.querySelectorAll('.reveal');
 if(!('IntersectionObserver' in window)||document.documentElement.dataset.static||/static=1/.test(location.search)){els.forEach(function(e){e.classList.add('in')});return}
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
 els.forEach(function(e){io.observe(e)});
})();
</script>"""


def render(t):
    _n[0] = 0
    lh, lb, la = t["logo_header"]
    mh, mb, ma = t["logo_hero"]
    ah, ab, aa = t["logo_about"]
    fh, fb, fa = t["logo_footer"]
    def product_block(pid, k, title, intro, bullets, note):
        more = ""
        if pid == "resonest":
            more = '<p class="more"><a href="awaabs-law/">Read our Awaab\'s Law explainer</a></p>'
        return (
            f'<article class="product reveal" id="{pid}">{ic(ICONS[k])}<h3>{title}</h3>'
            f'<p class="intro">{intro}</p><ul>'
            + "".join(f"<li>{b}</li>" for b in bullets)
            + f"</ul>{f'<p class=\"note\">{note}</p>' if note else ''}{more}</article>"
        )
    prod_html = "".join(product_block(*row) for row in products)
    svc_html = "".join(f'<article class="card reveal">{ic(ICONS[k])}<h3>{title}</h3><p>{d}</p></article>' for k, title, d in services)
    step_html = "".join(f'<li class="step reveal"><span class="num">{n}</span><h3>{title}</h3><p>{d}</p></li>' for n, title, d in steps)
    val_html = "".join(f'<div class="value reveal"><h3>{title}</h3><p>{d}</p></div>' for title, d in values)
    sec_html = "".join(f'<li class="sector reveal"><h3>{title}</h3><p>{d}</p></li>' for title, d in sectors)
    ico = icon_svg(*t["favicon"])
    fav64 = base64.b64encode(ico.encode()).decode()
    png64 = base64.b64encode(cairosvg.svg2png(bytestring=ico.encode(), output_width=180)).decode()
    sector_rainbow = ""
    if t.get("sector_rainbow"):
        sector_rainbow = (
            ".sector:nth-child(2){border-top-color:var(--icon-fg)}"
            ".sector:nth-child(3){border-top-color:var(--hero-accent)}"
            ".sector:nth-child(4){border-top-color:var(--navy)}"
        )
        # Keep original default rainbow (teal/brick/gold/navy) only for DEFAULT
        if t["id"] == "default":
            sector_rainbow = (
                ".sector:nth-child(2){border-top-color:var(--brick, #B5432F)}"
                ".sector:nth-child(3){border-top-color:var(--gold, #D9A441)}"
                ".sector:nth-child(4){border-top-color:var(--navy)}"
            )

    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{entry_script("home")}
<title>Watson Atlas | UK Housing Software</title>
<meta name="description" content="Watson Atlas builds software for UK housing providers, including Resonest, a privacy-first digital twin for social landlords, and SiteOps, a housing compliance platform.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="{t['theme_color']}">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,{fav64}">
<link rel="apple-touch-icon" href="data:image/png;base64,{png64}">
<style>
@font-face{{font-family:"Montserrat";src:url(data:font/woff2;base64,{FONT64}) format("woff2");font-weight:100 900;font-display:swap}}
:root{{{root_css(t)};--r:18px}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;font-family:Montserrat,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--body-bg);line-height:1.6;font-size:17px;-webkit-font-smoothing:antialiased}}
a{{color:inherit}}img,svg{{display:block}}
.wrap{{width:min(1160px,92vw);margin:0 auto}}
.skip{{position:absolute;left:-999px}}.skip:focus{{left:12px;top:12px;z-index:99;background:#fff;padding:8px 12px;border-radius:8px}}
/* header */
header.top{{position:fixed;inset:0 0 auto 0;z-index:50;color:var(--header-fg);transition:background .3s,box-shadow .3s,color .3s}}
header.top.scrolled,header.top.open{{background:var(--header-scrolled-bg);color:var(--header-scrolled-fg);box-shadow:var(--header-shadow)}}header.top.scrolled{{backdrop-filter:blur(8px)}}
.bar{{display:flex;align-items:center;justify-content:space-between;height:76px;gap:16px}}
.brand{{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;flex-shrink:0}}
.brand .mono{{width:44px;height:44px}}
.brand b{{display:block;font-weight:700;letter-spacing:.14em;font-size:15px;line-height:1.1}}
.brand span{{display:block;font-weight:400;letter-spacing:.42em;font-size:12px;opacity:.85}}
.tools{{display:flex;align-items:center;gap:18px;flex-shrink:0}}
.home-link{{color:inherit;text-decoration:none;font-size:15px;font-weight:600;letter-spacing:.02em;opacity:.92}}
.home-link:hover,.home-link[aria-current="page"]{{opacity:1}}
.menu{{display:inline-flex;align-items:center;justify-content:center;background:none;border:0;color:inherit;padding:8px;margin:0;cursor:pointer;border-radius:8px}}
.menu:hover,.drawer-close:hover{{opacity:.8}}
.menu:focus-visible,.home-link:focus-visible,.drawer-close:focus-visible,.drawer a:focus-visible{{outline:2px solid var(--cream);outline-offset:3px}}
body.menu-open{{overflow:hidden}}
.nav-overlay{{position:fixed;inset:0;background:rgba(7,21,48,.58);opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s;z-index:80}}
.nav-overlay.open{{opacity:1;visibility:visible}}
.drawer{{position:fixed;top:0;right:0;bottom:0;width:min(400px,88vw);background:var(--navy);color:var(--cream);z-index:90;transform:translateX(100%);transition:transform .35s ease;display:flex;flex-direction:column;padding:22px 28px 36px;overflow-y:auto;box-shadow:-16px 0 40px rgba(0,0,0,.25)}}
.drawer.open{{transform:none}}
.drawer-head{{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 0 18px;min-height:44px}}
.drawer-title{{margin:0;font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--cream);opacity:.75}}
.drawer-close{{display:inline-flex;align-items:center;justify-content:center;background:none;border:0;color:var(--cream);padding:8px;margin:0;cursor:pointer;border-radius:8px}}
.drawer-links{{display:flex;flex-direction:column;gap:2px;flex:1}}
.drawer-links a{{color:var(--cream);text-decoration:none;font-size:20px;font-weight:600;letter-spacing:-.01em;padding:12px 0;border-bottom:1px solid rgba(245,236,220,.14)}}
.drawer-links a:hover{{opacity:.85}}
.drawer-links a[aria-current="page"]{{color:var(--cream);box-shadow:inset 0 -2px 0 var(--cream)}}
.drawer-cta{{margin-top:auto;padding:13px 24px;justify-content:center;align-self:stretch;text-align:center;width:100%}}
/* hero: The Street night scene (live nav kept above) */
.hero{{position:relative;overflow:hidden;background:linear-gradient(180deg,#071634 0%,var(--navy) 70%);color:var(--hero-fg);padding:132px 0 0;text-align:center}}
.hero .moon{{position:absolute;right:12%;top:96px;width:70px;height:70px;border-radius:50%;background:var(--cream);box-shadow:0 0 60px rgba(245,236,220,.5)}}
.hero .wrap{{position:relative;display:block}}
.hero .eyebrow{{color:var(--cream);opacity:.8}}
h1{{font-size:clamp(38px,5.4vw,68px);line-height:1.06;margin:18px 0 22px;font-weight:700;letter-spacing:-.01em}}
.hero h1{{margin:18px auto 22px;max-width:960px;font-weight:800}}
h1 em{{font-style:normal;color:var(--hero-accent)}}
.hero h1 em{{color:var(--cream)}}
.lead{{font-size:clamp(17px,1.6vw,20px);max-width:600px;opacity:.9;margin:0 0 34px}}
.hero .lead{{max-width:720px;margin:0 auto 34px}}
.ctas{{display:flex;gap:14px;flex-wrap:wrap}}
.hero .ctas{{justify-content:center}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;padding:13px 24px;font-weight:600;font-size:15px;text-decoration:none;transition:transform .2s,background .2s,color .2s}}
.btn:hover{{transform:translateY(-2px)}}
.btn.gold{{background:var(--btn);color:var(--btn-fg)}}
.btn.gold:hover{{background:var(--btn-hover)}}
.btn.ghost{{border:1.5px solid var(--ghost-border);color:var(--ghost-fg)}}
.btn.ghost:hover{{border-color:var(--ghost-hover);color:var(--ghost-hover)}}
.legend{{display:flex;gap:16px 28px;justify-content:center;flex-wrap:wrap;font-size:13px;margin:28px 0 8px;color:var(--cream)}}
.legend span{{display:inline-flex;align-items:center;gap:8px}}
.legend i{{display:inline-block;width:14px;height:14px;border-radius:3px;flex-shrink:0}}
.legend .need{{background:#D9894A}}
.legend .watch{{background:#7FA7C9}}
.legend .well{{background:var(--cream);opacity:.5}}
.hero .street{{display:block;width:100%;height:auto;margin-top:8px}}
.road{{background:#1b2a4a;height:48px;position:relative}}
.road:after{{content:"";position:absolute;left:0;right:0;top:22px;height:2px;background:var(--cream);opacity:.35}}
.eyebrow{{display:inline-block;font-size:13px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--hero-accent)}}
.strip{{background:var(--strip-bg);color:var(--strip-fg);border-top:1px solid var(--strip-line);border-bottom:1px solid var(--strip-line)}}
.strip ul{{list-style:none;margin:0;padding:22px 0;display:flex;flex-wrap:wrap;gap:12px 36px;justify-content:center;font-size:14px;font-weight:500;letter-spacing:.04em;opacity:.92}}
.strip li{{display:flex;align-items:center;gap:10px}}.strip li::before{{content:"";width:7px;height:7px;border-radius:50%;background:var(--strip-dot)}}
/* sections */
section{{padding:110px 0}}
.head{{max-width:720px;margin-bottom:56px}}
.head .eyebrow,.about .eyebrow{{color:var(--eyebrow)}}
h2{{font-size:clamp(30px,3.6vw,46px);line-height:1.12;margin:14px 0 18px;color:var(--heading);letter-spacing:-.01em}}
.head p{{color:var(--muted);font-size:18px;margin:0}}
h3{{font-size:19px;line-height:1.3;margin:0 0 10px;color:var(--heading)}}
p{{margin:0}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.card{{background:var(--card-bg);border:1px solid var(--line);border-radius:var(--r);padding:30px 28px;transition:transform .25s,box-shadow .25s,border-color .25s}}
.card:hover{{transform:translateY(-4px);box-shadow:var(--card-shadow);border-color:var(--card-hover)}}
.card p{{color:var(--muted);font-size:15.5px}}
.ic{{width:46px;height:46px;padding:10px;border-radius:12px;background:var(--icon-bg);color:var(--icon-fg);margin-bottom:20px}}
.products{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-bottom:48px}}
.product{{background:var(--alt-bg);border:1px solid var(--line);border-radius:var(--r);padding:36px 34px 32px;transition:transform .25s,box-shadow .25s,border-color .25s}}
.product:hover{{transform:translateY(-4px);box-shadow:var(--card-shadow);border-color:var(--card-hover)}}
.product h3{{font-size:28px;margin:0 0 12px}}
.product .intro{{color:var(--muted);font-size:16px;margin:0 0 22px}}
.product ul{{list-style:none;margin:0;padding:0}}
.product li{{position:relative;padding:10px 0 10px 22px;font-size:15.5px;color:var(--ink);border-top:1px solid var(--line)}}
.product li:first-child{{border-top:0;padding-top:0}}
.product li::before{{content:"";position:absolute;left:0;top:1.15em;width:7px;height:7px;border-radius:50%;background:var(--heading)}}
.product li:first-child::before{{top:.55em}}
.product .note{{margin-top:16px;font-size:14px;color:var(--muted)}}
.product .more{{margin:18px 0 0}}
.product .more a{{color:var(--heading);font-weight:600;font-size:15px;text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--heading) 40%,transparent)}}
.product .more a:hover{{color:var(--navy2);border-color:var(--navy2)}}
.cap-head{{font-size:14px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--heading);margin:0 0 22px}}
.cards.support{{display:flex;flex-wrap:wrap;gap:22px}}
.cards.support .card{{flex:1 1 calc(33.333% - 15px);min-width:min(100%,260px)}}
/* how we work */
.how{{background:var(--alt-bg)}}
.steps{{list-style:none;padding:0;margin:0 0 70px;display:grid;grid-template-columns:repeat(5,1fr);gap:18px;counter-reset:s}}
.step{{position:relative;padding-top:26px;border-top:2px solid var(--heading)}}
.step .num{{font-size:13px;font-weight:700;color:var(--step-num);letter-spacing:.15em}}
.step h3{{margin-top:8px}}.step p{{font-size:15px;color:var(--muted)}}
.values{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}}
.value{{background:var(--value-bg);color:var(--value-fg);border-radius:var(--r);padding:30px 26px;position:relative;overflow:hidden}}
.value::after{{content:"";position:absolute;right:-30px;top:-30px;width:110px;height:110px;border-radius:50%;border:2px solid var(--value-ring)}}
.value h3{{color:var(--value-h)}}.value p{{font-size:15px;opacity:.88}}
.sub{{font-size:14px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--heading);margin:0 0 22px}}
/* sectors */
.sectors{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(5,1fr);gap:18px}}
.sector{{border-radius:var(--r);padding:26px 22px;background:var(--sector-bg);border:1px solid var(--line);border-top:4px solid var(--sector-accent)}}
{sector_rainbow}
.sector p{{font-size:15px;color:var(--muted)}}
.partner{{margin-top:34px;display:flex;gap:24px;align-items:center;justify-content:space-between;flex-wrap:wrap;background:var(--partner-bg);color:var(--partner-fg);border-radius:var(--r);padding:30px 34px}}
.partner p{{max-width:720px;opacity:.95}}.partner strong{{color:inherit}}
/* about */
.about{{background:var(--about-bg)}}
.about .wrap{{display:grid;grid-template-columns:.9fr 1.1fr;gap:70px;align-items:center}}
.about-card{{background:var(--about-card-bg);border-radius:28px;padding:56px;display:grid;place-items:center;aspect-ratio:1/1;position:relative;overflow:hidden}}
.about-card .mono{{width:70%;height:auto}}
.about-card small{{position:absolute;bottom:28px;color:var(--about-card-fg);letter-spacing:.3em;font-size:12px;text-transform:uppercase;opacity:.8}}
.about p+p{{margin-top:16px}}.about .body p{{color:var(--muted)}}
.facts{{list-style:none;padding:0;margin:28px 0 0;display:flex;flex-wrap:wrap;gap:10px}}
.facts li{{background:var(--facts-bg);color:var(--facts-fg);border-radius:999px;padding:8px 16px;font-size:14px;font-weight:600}}
/* contact */
.contact{{background:var(--contact-bg);color:var(--contact-fg);text-align:center}}
.contact h2{{color:var(--contact-fg)}}.contact p{{opacity:.9;max-width:640px;margin:0 auto 34px;font-size:18px}}
.contact .mail{{display:block;margin-top:22px;font-size:15px;opacity:.85}}
footer{{background:var(--footer-bg);color:var(--footer-fg);font-size:14px;padding:44px 0}}
footer .wrap{{display:flex;justify-content:space-between;align-items:center;gap:20px 28px;flex-wrap:wrap}}
footer .brand{{color:var(--footer-link)}}
footer .brand .mono{{width:36px;height:36px}}
footer a{{color:var(--footer-link);text-decoration:none}}footer a:hover{{color:var(--footer-hover)}}
footer .ce-badge{{display:inline-flex;align-items:center;gap:8px;margin:0;padding:7px 14px 7px 10px;border:1px solid color-mix(in srgb,var(--cream) 55%,transparent);border-radius:999px;color:var(--cream);font-size:12px;font-weight:600;letter-spacing:.01em;line-height:1.2;white-space:nowrap;flex:0 0 auto}}
footer .ce-badge svg{{width:18px;height:18px;flex-shrink:0}}
.reveal{{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}}
.reveal.in{{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}.reveal{{opacity:1;transform:none;transition:none}}.btn,.card,.drawer,.nav-overlay{{transition:none}}}}
@media (max-width:1050px){{.cards{{grid-template-columns:repeat(2,1fr)}}.products{{grid-template-columns:1fr}}.steps{{grid-template-columns:repeat(3,1fr)}}.values{{grid-template-columns:repeat(2,1fr)}}.sectors{{grid-template-columns:repeat(2,1fr)}}}}
@media (max-width:820px){{
 .hero{{padding:110px 0 0}}.hero .moon{{width:42px;height:42px;top:82px;right:7%;box-shadow:0 0 28px rgba(245,236,220,.4)}}
 .legend{{gap:10px 18px;font-size:12px;margin:20px 12px 4px}}
 .about .wrap{{grid-template-columns:1fr;gap:40px}}.about-card{{max-width:420px}}
 section{{padding:80px 0}}
 footer .wrap{{justify-content:center;text-align:center}}
}}
@media (max-width:560px){{.cards,.products,.steps,.values,.sectors{{grid-template-columns:1fr}}.partner{{padding:26px}}body{{font-size:16px}}
 .hero .moon{{display:none}}.hero h1{{font-size:36px}}.hero .ctas{{justify-content:center}}.legend{{flex-direction:column;align-items:center;gap:8px}}}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header_html(t, 'home')}
<main id="main">
<section class="hero" aria-labelledby="hero-title">
 <div class="moon" aria-hidden="true"></div>
 <div class="wrap">
   <span class="eyebrow">UK Housing Software</span>
   <h1 id="hero-title">Every home on the street, <em>seen clearly and cared for.</em></h1>
   <p class="lead">Watson Atlas builds software for UK housing providers. Our two main products are Resonest, a privacy-first digital twin for social landlords, and SiteOps, a housing compliance platform for inspections and reports.</p>
   <div class="ctas"><a class="btn gold" href="#what">Walk down the street</a><a class="btn ghost" href="#contact">Talk to us</a></div>
   <div class="legend"><span><i class="need"></i>Homes that need help first</span><span><i class="watch"></i>Homes to keep an eye on</span><span><i class="well"></i>Homes doing well</span></div>
 </div>
 {street_svg()}
 <div class="road" aria-hidden="true"></div>
</section>
<div class="strip"><ul class="wrap"><li>Housing associations</li><li>Local authorities</li><li>Social landlords</li><li>Building safety consultancies</li><li>Residential landlords</li></ul></div>

<section id="what" aria-labelledby="what-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">What we do</span><h2 id="what-title">Software that helps housing teams care for homes and communities</h2><p>We design around how your organisation works. Resonest and SiteOps sit at the centre, with building-safety reporting, a field app, property data, integrations and bespoke software around them.</p></div>
  <div class="products">{prod_html}</div>
  <p class="cap-head">Around Resonest and SiteOps</p>
  <div class="cards support">{svc_html}</div>
 </div>
</section>

<section class="how" id="how" aria-labelledby="how-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">How we work</span><h2 id="how-title">Clear steps, shared goals, lasting partnerships</h2><p>Every engagement follows a simple, transparent path, so you always know where things stand and what comes next.</p></div>
  <ol class="steps">{step_html}</ol>
  <p class="sub">What we value</p>
  <div class="values">{val_html}</div>
 </div>
</section>

<section id="who" aria-labelledby="who-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">Who we work with</span><h2 id="who-title">Built for UK housing organisations</h2><p>We work with social landlords, council housing teams, residential landlords and building safety consultancies that want their homes, data and teams to work better together.</p></div>
  <ul class="sectors">{sec_html}</ul>
  <div class="partner reveal"><p><strong>Already have a housing or asset system?</strong> We connect to the systems you already rely on, rather than replacing them, and can take on specialist software, integration and reporting as part of a wider programme.</p><a class="btn gold" href="{mailto}">Talk to us</a></div>
 </div>
</section>

<section class="about" id="about" aria-labelledby="about-title">
 <div class="wrap">
  <div class="about-card reveal">{mono(ah, ab, aa, label="Watson Atlas monogram")}<small>Watson Atlas</small></div>
  <div class="body">
   <span class="eyebrow">About</span>
   <h2 id="about-title">Big aspirations for UK housing</h2>
   <p>Watson Atlas is the housing software brand from the team behind Rowe AI, a Scottish software company building bespoke systems and digital twins for complex operational challenges.</p>
   <p>We bring that engineering experience to housing, with one simple ambition: to help every home and every resident benefit from software that is clear, reliable and built around real needs.</p>
   <ul class="facts"><li>UK based</li><li>Cyber Essentials certified</li><li>Bespoke &amp; integrated</li><li>People in the loop</li></ul>
  </div>
 </div>
</section>

<section class="contact" id="contact" aria-labelledby="contact-title">
 <div class="wrap">
  <span class="eyebrow">Contact</span>
  <h2 id="contact-title">What could work better for your homes?</h2>
  <p>Tell us about your homes, your teams and your plans. We would love to explore what we could build together.</p>
  <a class="btn gold" href="{mailto}">Email us <span aria-hidden="true">→</span></a>
  <a class="mail" href="mailto:{MAIL}">{MAIL}</a>
 </div>
</section>
</main>
{footer_html(t, 'home')}
{site_script()}
</body>
</html>'''
    return html


def write_favicon(t, dest: Path):
    ico = icon_svg(*t["favicon"])
    (dest / "favicon.svg").write_text(ico)
    cairosvg.svg2png(bytestring=ico.encode(), write_to=str(dest / "favicon.png"), output_width=180)
    cairosvg.svg2png(bytestring=ico.encode(), write_to=str(dest / "favicon-32.png"), output_width=32)


def _write_tree(theme, dest: Path, write_fav=False):
    dest.mkdir(parents=True, exist_ok=True)
    html = render(theme)
    (dest / "index.html").write_text(html)
    from subpages import render_awaab, render_help
    for name, fn in (("awaabs-law", render_awaab), ("help", render_help)):
        d = dest / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(fn(theme))
    proxy_src = ROOT / ".herenow" / "proxy.json"
    if proxy_src.exists():
        hn = dest / ".herenow"
        hn.mkdir(parents=True, exist_ok=True)
        (hn / "proxy.json").write_text(proxy_src.read_text())
    if write_fav:
        write_favicon(theme, dest)
    return dest / "index.html", len(html)


def build(theme, dest_dir, write_fav=False):
    return _write_tree(theme, Path(dest_dir), write_fav=write_fav)


def build_variants():
    out = ROOT / "variants"
    paths = []
    for t in VARIANTS:
        p, n = build(t, out / t["id"], write_fav=False)
        paths.append((t["id"], p, n))
        print(t["id"], n, p)
    return paths


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "variants":
        build_variants()
    else:
        import shutil
        p, n = build(CLASSIC_NAVY, ROOT, write_fav=True)
        dist = ROOT / "dist"
        dist.mkdir(exist_ok=True)
        for name in ("index.html", "favicon.svg", "favicon.png", "favicon-32.png"):
            shutil.copy2(ROOT / name, dist / name)
        for sub in ("awaabs-law", "help"):
            (dist / sub).mkdir(exist_ok=True)
            shutil.copy2(ROOT / sub / "index.html", dist / sub / "index.html")
        (dist / ".herenow").mkdir(exist_ok=True)
        shutil.copy2(ROOT / ".herenow" / "proxy.json", dist / ".herenow" / "proxy.json")
        print("classic-navy", n, p)
        print("awaabs-law", (ROOT / "awaabs-law" / "index.html").stat().st_size)
        print("help", (ROOT / "help" / "index.html").stat().st_size)
