NAVY="#0B1F45"; NAVY2="#13295A"; CREAM="#F5ECDC"; CREAM2="#EADDC6"; WHITE="#FFFFFF"; WARM="#D9894A"; COOL="#7FA7C9"
PTS=[(-74,-30),(-44,44),(-20,-6),(4,44),(30,-52),(62,50)]
_n=[0]
def mono(fg, size=44, ring=None):
    _n[0]+=1; mid=f"ko{_n[0]}"
    p=" ".join(f"{x},{y}" for x,y in PTS)
    ko="".join(f'<polyline points="{a[0]},{a[1]} {b[0]},{b[1]}" stroke="#000" stroke-width="19"/>' for a,b in [(PTS[0],PTS[1]),(PTS[4],PTS[5])])
    return (f'<svg width="{size}" height="{size}" viewBox="-90 -90 180 180" role="img" aria-label="Watson Atlas"><mask id="{mid}" maskUnits="userSpaceOnUse" x="-90" y="-90" width="180" height="180"><rect x="-90" y="-90" width="180" height="180" fill="#fff"/>{ko}</mask>'
            f'<circle r="80" fill="none" stroke="{ring or fg}" stroke-width="6" mask="url(#{mid})"/><polyline points="{p}" fill="none" stroke="{fg}" stroke-width="9" stroke-linejoin="miter" stroke-miterlimit="10"/></svg>')
def lockup(fg, size=44, sub=True):
    return (f'<a class="brand" href="#top" style="display:flex;align-items:center;gap:12px;color:{fg};text-decoration:none">{mono(fg,size)}'
            f'<span style="display:flex;flex-direction:column;line-height:1"><b style="font-weight:700;letter-spacing:.14em;font-size:{size*.38:.0f}px">WATSON</b>'
            f'<span style="font-weight:400;letter-spacing:.5em;font-size:{size*.3:.0f}px;margin-top:4px">ATLAS</span></span></a>')
FONT='@font-face{font-family:"Montserrat";src:url(../../assets/montserrat.woff2) format("woff2");font-weight:100 900}'
BASE=FONT+'*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Montserrat,system-ui,sans-serif;-webkit-font-smoothing:antialiased}img,svg{max-width:100%}a{color:inherit}'
NAV=[("Resonest","#resonest"),("SiteOps","#siteops"),("Capabilities","#capabilities"),("How we work","#how"),("Who we help","#who"),("About","#about"),("Contact","#contact")]
HERO_SUB="Watson Atlas builds software for UK housing providers. Our two main products are Resonest, a privacy-first digital twin for social landlords, and SiteOps, a housing compliance platform for inspections and reports."
RESO_LEAD="Built for Awaab's Law, Resonest is a privacy-first digital twin that helps social landlords get ahead of damp, mould and cold homes."
RESO=["Uses existing property and weather data, with no in-home sensors or tenant monitoring","Shows which homes will struggle first in winter, and why","Highlights which low-cost improvements will make homes safer and cheaper to keep warm","Helps teams meet Awaab's Law with confidence, with clear action lists and deadlines for every home","Keeps an audit trail of what was done and what changed"]
SITE_LEAD="A housing compliance platform for capturing inspections on site and turning them into consistent, branded PDF reports, tied to the right property. It works alongside a landlord's existing housing system, rather than replacing it."
SITE=["On-site inspection capture and branded PDF reports for fire risk assessments, electrical work, and building and tower-block surveys","A property register keyed on UPRN, with EPC and condition information","A no-code form and report designer","Job planning to schedule, assign and track inspection programmes","A mobile app for on-site capture against the same forms"]
SITE_ROAD="A repairs and maintenance module is on the SiteOps roadmap."
CAPS=[("Building safety &amp; cladding reporting","A specialist reporting system for building-safety work, including FRAEW, desktop assessments, EWS1 and site-visit reports, with configurable forms, specialist PDFs, job management and a connected surveyor app."),
("Field &amp; surveyor app","A mobile app, in live use, for surveyors and assessors to capture photographs, geotagged data and evidence on site, even offline, against the same forms used in the web platform."),
("Property data","UPRN address verification, EPC certificate lookup and weather data. These already underpin Resonest and the SiteOps property register."),
("Integrations","Already have a housing or asset system? We connect rather than replace it, exchanging records, results, reports and actions using UPRN as the common reference."),
("Bespoke housing software","When off-the-shelf software does not quite fit, we design around the requirement, with controlled integration into the systems you already use.")]
STEPS=[("Define","We start with people: residents, users, workflows, integrations and what success looks like."),("Prototype","Narrow, early versions on representative data, so everyone can see and shape the direction."),("Build","Delivery in stages, with source control, automated testing and staging environments."),("Verify","Careful checks against agreed acceptance criteria before anything goes live."),("Deploy","A smooth handover into everyday use, with ongoing support as needs grow.")]
VALUES=[("Relationship before business","We invest in understanding your organisation, your residents and your goals. Long-term partnerships come first."),("Always looking forward","We focus on what could work better tomorrow, and on practical steps to get there."),("Big aspirations","We believe every home deserves great care, and that great software can help make that happen at scale."),("Evidence before claims","We prove ideas on real requirements before scaling them, so every step forward is a confident one.")]
SECTORS=[("Housing associations","Software that helps teams care for homes and communities, from compliance and property data to seeing which homes will struggle first in winter."),("Local authorities","Tools for council housing teams, including compliance, property data and a clear view of thermal risk across a portfolio."),("Residential landlords","The same warmth, fabric and compliance tools, for large residential landlords as well as social landlords."),("Building safety consultancies","Specialist systems for building-safety work, including FRAEW, EWS1, desktop assessments and site-visit reports."),("Partners and programmes","We can work alongside your existing teams and systems, taking on specialist software, integration and reporting.")]
ABOUT1="Watson Atlas is the housing software brand from the team behind Rowe AI, a Scottish software company building bespoke systems and digital twins for complex operational challenges."
ABOUT2="We bring that engineering experience to housing, with one simple ambition: to help every home and every resident benefit from software that is clear, reliable and built around real needs."
BADGES=["UK based","Cyber Essentials certified","Bespoke &amp; integrated","People in the loop"]
EMAIL="info@rowe.ai"
FOOT="&copy; 2026 Watson Atlas. A Rowe AI Ltd brand. Registered in Scotland, company no. SC770018."
DRAFT_TAG='<div style="position:fixed;right:14px;bottom:14px;z-index:99;background:#fff;color:#0B1F45;border:1px solid #0B1F45;border-radius:99px;padding:6px 14px;font:600 11px Montserrat;letter-spacing:.12em">DRAFT CONCEPT</div>'
def page(title, css, body):
    return f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{title}</title><style>{BASE}{css}</style></head><body id="top">{body}{DRAFT_TAG}</body></html>'
def navlinks(): return "".join(f'<a href="{h}">{t}</a>' for t,h in NAV)
def ul(items): return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"
