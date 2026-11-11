"""Extra pages for the Watson Atlas site: Awaab's Law explainer and How can we help?"""

from __future__ import annotations

import base64

import cairosvg


def _css(t, extra=""):
    from build import FONT64, root_css

    return f"""
@font-face{{font-family:"Montserrat";src:url(data:font/woff2;base64,{FONT64}) format("woff2");font-weight:100 900;font-display:swap}}
:root{{{root_css(t)};--r:18px}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;font-family:Montserrat,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--body-bg);line-height:1.6;font-size:17px;-webkit-font-smoothing:antialiased}}
a{{color:inherit}}img,svg{{display:block}}
.wrap{{width:min(1160px,92vw);margin:0 auto}}
.skip{{position:absolute;left:-999px}}.skip:focus{{left:12px;top:12px;z-index:99;background:#fff;padding:8px 12px;border-radius:8px}}
header.top{{position:fixed;inset:0 0 auto 0;z-index:50;color:var(--header-fg);transition:background .3s,box-shadow .3s,color .3s}}
header.top.scrolled,header.top.open{{background:var(--header-scrolled-bg);color:var(--header-scrolled-fg);box-shadow:var(--header-shadow)}}header.top.scrolled{{backdrop-filter:blur(8px)}}
.bar{{display:flex;align-items:center;justify-content:space-between;height:76px;gap:16px}}
.brand{{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;flex-shrink:0}}
.brand b{{display:block;font-size:15px;letter-spacing:.14em;font-weight:700;line-height:1}}
.brand span{{display:block;font-size:12px;letter-spacing:.46em;font-weight:500;margin-top:3px;opacity:.9}}
.brand .mono{{width:42px;height:42px}}
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
.hero{{position:relative;overflow:hidden;background:linear-gradient(180deg,#071634 0%,var(--navy) 70%);color:var(--hero-fg);padding:132px 0 0;text-align:center}}
.hero-small{{padding:118px 0 0}}
.hero .moon{{position:absolute;right:12%;top:88px;width:52px;height:52px;border-radius:50%;background:var(--cream);box-shadow:0 0 44px rgba(245,236,220,.45)}}
.hero-small .moon{{width:44px;height:44px;top:86px}}
.hero .wrap{{position:relative;display:block}}
.hero .eyebrow{{color:var(--cream);opacity:.8}}
.eyebrow{{display:inline-block;font-size:13px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--hero-accent)}}
h1{{font-size:clamp(34px,4.6vw,56px);line-height:1.08;margin:16px auto 18px;font-weight:800;letter-spacing:-.01em;max-width:900px}}
h1 em{{font-style:normal;color:var(--cream)}}
.hero .lead{{max-width:720px;margin:0 auto 28px;font-size:clamp(16px,1.5vw,19px);opacity:.9}}
.ctas{{display:flex;gap:14px;flex-wrap:wrap;justify-content:center}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;padding:13px 24px;font-weight:600;font-size:15px;text-decoration:none;transition:transform .2s,background .2s,color .2s}}
.btn:hover{{transform:translateY(-2px)}}
.btn.gold{{background:var(--btn);color:var(--btn-fg)}}
.btn.gold:hover{{background:var(--btn-hover)}}
.btn.ghost{{border:1.5px solid var(--ghost-border);color:var(--ghost-fg)}}
.btn.ghost:hover{{border-color:var(--ghost-hover);color:var(--ghost-hover)}}
.hero .street{{display:block;width:100%;height:auto;margin-top:8px;max-height:200px}}
.road{{background:#1b2a4a;height:40px;position:relative}}
.road:after{{content:"";position:absolute;left:0;right:0;top:18px;height:2px;background:var(--cream);opacity:.35}}
section{{padding:88px 0}}
section.alt{{background:var(--alt-bg)}}
.head{{max-width:760px;margin-bottom:36px}}
.head .eyebrow{{color:var(--eyebrow)}}
h2{{font-size:clamp(28px,3.2vw,42px);line-height:1.14;margin:12px 0 16px;color:var(--heading);letter-spacing:-.01em}}
h3{{font-size:19px;line-height:1.3;margin:0 0 10px;color:var(--heading)}}
.prose p{{margin:0 0 16px;color:var(--ink);max-width:760px}}
.prose p.lede{{font-size:18px}}
.prose ul,.prose ol{{margin:0 0 18px;padding:0 0 0 22px;max-width:760px;color:var(--ink)}}
.prose li{{margin:0 0 8px}}
.prose a{{color:var(--navy);font-weight:600;text-decoration:underline;text-underline-offset:3px}}
.prose a:hover{{color:var(--navy2)}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.grid-2{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}}
.card{{background:var(--card-bg);border:1px solid var(--line);border-radius:var(--r);padding:26px 24px;box-shadow:var(--card-shadow)}}
.card .when{{display:block;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--eyebrow);margin-bottom:8px}}
.card p{{margin:0;color:var(--muted);font-size:15.5px}}
.card ul{{margin:10px 0 0;padding:0 0 0 18px;color:var(--ink);font-size:15px}}
.times .card .num{{display:block;font-size:28px;font-weight:800;color:var(--navy);letter-spacing:-.03em;margin:0 0 6px;line-height:1.1}}
.note-box{{background:var(--cream);border-radius:var(--r);padding:22px 24px;margin-top:28px;max-width:860px}}
.note-box p{{margin:0;color:var(--ink);font-size:15.5px}}
.sources{{margin-top:22px;font-size:14.5px}}
.sources h3{{font-size:16px;margin-bottom:12px}}
.sources ol{{padding-left:22px;margin:0}}
.sources li{{margin:0 0 8px}}
.disclaimer{{font-size:14.5px;color:var(--muted);background:var(--white);border-top:1px solid var(--line);padding:28px 0 8px}}
.disclaimer p{{margin:0 0 10px;max-width:860px}}
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
.helps{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}}
.helps article{{background:var(--white);border-radius:var(--r);padding:24px;border:1px solid var(--line)}}
.helps h3{{margin-bottom:8px}}
.helps p{{margin:0;color:var(--muted);font-size:15.5px}}
.caveat{{margin-top:28px;max-width:800px;font-size:15.5px;color:var(--ink)}}
/* chat */
.chat-wrap{{max-width:760px;margin:0 auto}}
.chat{{background:var(--white);border:1px solid var(--line);border-radius:22px;box-shadow:var(--card-shadow);overflow:hidden;display:flex;flex-direction:column;min-height:520px}}
.chat-log{{flex:1;padding:22px 22px 8px;display:flex;flex-direction:column;gap:12px;max-height:520px;overflow-y:auto}}
.bubble{{max-width:85%;padding:12px 16px;border-radius:16px;font-size:15.5px;line-height:1.55}}
.bubble p{{margin:0 0 8px}}.bubble p:last-child{{margin:0}}
.bubble.joe{{background:var(--navy);color:var(--cream);align-self:flex-start;border-bottom-left-radius:6px}}
.bubble.you{{background:var(--cream);color:var(--navy);align-self:flex-end;border-bottom-right-radius:6px}}
.bubble.sys{{align-self:center;background:transparent;color:var(--muted);font-size:13.5px;text-align:center;max-width:100%}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;padding:4px 22px 16px}}
.chips button{{background:var(--cream);color:var(--navy);border:0;border-radius:999px;padding:8px 14px;font:inherit;font-size:13.5px;font-weight:600;cursor:pointer}}
.chips button:hover{{background:#eadfcb}}
.composer{{display:flex;gap:10px;padding:16px 18px;border-top:1px solid var(--line);background:var(--body-bg)}}
.composer textarea{{flex:1;border:1px solid var(--line);border-radius:14px;padding:12px 14px;font:inherit;font-size:15px;resize:none;min-height:52px;max-height:120px;color:var(--ink);background:var(--white)}}
.composer textarea:focus{{outline:2px solid var(--navy);outline-offset:1px}}
.composer button.send{{background:var(--navy);color:var(--cream);border:0;border-radius:999px;padding:0 20px;font:inherit;font-weight:700;font-size:14px;cursor:pointer;white-space:nowrap}}
.composer button.send:disabled{{opacity:.5;cursor:not-allowed}}
.ai-note{{text-align:center;font-size:13px;color:var(--muted);margin:14px 0 0}}
.reveal{{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}}
.reveal.in{{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}.reveal{{opacity:1;transform:none;transition:none}}.btn,.card,.drawer,.nav-overlay{{transition:none}}}}
@media (max-width:900px){{.grid,.grid-2,.helps{{grid-template-columns:1fr}}}}
@media (max-width:820px){{
 .hero,.hero-small{{padding:110px 0 0}}.hero .moon{{display:none}}
 section{{padding:72px 0}}
 footer .wrap{{justify-content:center;text-align:center}}
}}
@media (max-width:560px){{body{{font-size:16px}}h1{{font-size:32px}}.chat{{min-height:460px}}.composer{{flex-direction:column}}.composer button.send{{padding:12px 20px}}}}
{extra}
"""


def _head(t, title, description, page="awaab"):
    from build import icon_svg, entry_script

    ico = icon_svg(*t["favicon"])
    fav64 = base64.b64encode(ico.encode()).decode()
    png64 = base64.b64encode(cairosvg.svg2png(bytestring=ico.encode(), output_width=180)).decode()
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{entry_script(page)}
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="{t['theme_color']}">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,{fav64}">
<link rel="apple-touch-icon" href="data:image/png;base64,{png64}">
<style>{_css(t)}</style>
</head>
"""


def render_awaab(t):
    from build import MAIL, mailto, header_html, footer_html, site_script, street_svg

    html = _head(
        t,
        "Awaab's Law, explained | Watson Atlas",
        "A plain-English explainer of Awaab's Law for social landlords in England, and how Resonest can help teams get ahead of damp, mould and cold homes.",
        page="awaab",
    )
    html += f"""<body>
<a class="skip" href="#main">Skip to content</a>
{header_html(t, "awaab")}
<main id="main">
<section class="hero hero-small" aria-labelledby="hero-title">
 <div class="moon" aria-hidden="true"></div>
 <div class="wrap">
   <span class="eyebrow">Awaab's Law</span>
   <h1 id="hero-title">A clearer view of the law, <em>and of the homes it is there to protect.</em></h1>
   <p class="lead">Awaab's Law sets fixed timeframes for social landlords in England to investigate and fix dangerous hazards. This page explains what the law is, who it applies to, and the timescales that apply, in plain English.</p>
   <div class="ctas"><a class="btn gold" href="#timescales">The key timescales</a><a class="btn ghost" href="#resonest-helps">How Resonest helps</a></div>
 </div>
 {street_svg(n=12, w=1440, h=200, seed=3)}
 <div class="road" aria-hidden="true"></div>
</section>

<section id="what-it-is" aria-labelledby="what-it-is-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">What it is and why</span><h2 id="what-it-is-title">A legal duty to act on dangerous hazards in time</h2></div>
  <div class="prose">
   <p class="lede">Awaab's Law is named after Awaab Ishak, a two-year-old who died in 2020 from a severe respiratory condition caused by prolonged exposure to mould in his social home. His parents had complained repeatedly to their social landlord in the three years before his death, but no action was taken to treat the mould.</p>
   <p>The law is there so that social landlords investigate and repair emergency and significant hazards within set timeframes, and so that tenants can hold them to account if they do not. It was first introduced through the Social Housing (Regulation) Act 2023, which implies a term into social housing tenancy agreements. The detailed rules are in the Hazards in Social Housing (Prescribed Requirements) (England) Regulations 2025, as amended for later phases.</p>
   <p>If a landlord does not meet the requirements, tenants can take legal action through the courts for a breach of contract. They can also use the landlord's complaints procedure and the Housing Ombudsman Service.</p>
  </div>
 </div>
</section>

<section class="alt" id="who-it-applies-to" aria-labelledby="who-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">Who it applies to</span><h2 id="who-title">Social landlords in England</h2></div>
  <div class="prose">
   <p>Awaab's Law applies in England. It covers almost all social housing that is occupied under a tenancy and let by a registered provider of social housing. Registered providers may be local authorities or private registered providers, such as housing associations.</p>
   <p>It also applies to temporary and supported accommodation provided as social housing by a registered provider, where the home is occupied under a tenancy agreement.</p>
   <p>It does not apply to housing occupied under a licence, to long leaseholds, to owner-occupied homes, or to low-cost home ownership including shared ownership.</p>
   <p>The hazard must arise from a deficiency (for example a defect, disrepair or lack of maintenance) in a building or land for which the social landlord is responsible. Everyday activities such as cooking, bathing and drying laundry are not a reason for a landlord to refuse to act.</p>
  </div>
 </div>
</section>

<section id="phases" aria-labelledby="phases-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">When it came in</span><h2 id="phases-title">A phased rollout, so the rules can be tested and learned from</h2>
  <p>The requirements have been introduced in stages. The timeframes themselves stay the same. What changes in each phase is which significant hazards those timeframes cover. Emergency hazards have been in scope since Phase 1 began.</p></div>
  <div class="grid">
   <article class="card reveal"><span class="when">Phase 1</span><h3>From 27 October 2025</h3><p>Social landlords must address all emergency hazards, and damp and mould hazards that present a significant risk of harm, within the set timeframes. Phase 1 guidance remains in effect until 11:59pm on 29 November 2026.</p></article>
   <article class="card reveal"><span class="when">Phase 2</span><h3>From 30 November 2026</h3><p>The same timeframes for significant hazards also cover:</p>
    <ul>
     <li>excess cold</li>
     <li>excess heat</li>
     <li>falls (including on the level, on stairs and between levels)</li>
     <li>structural collapse</li>
     <li>fire and explosions</li>
     <li>electrical hazards</li>
     <li>domestic hygiene, including personal hygiene and food safety</li>
    </ul>
   </article>
   <article class="card reveal"><span class="when">Phase 3</span><h3>To be introduced in 2027</h3><p>Phase 3 will extend the requirements to the remaining Housing Health and Safety Rating System (HHSRS) hazards, except overcrowding. The government has said this third phase will be introduced in 2027. A specific commencement date has not yet been published in the same way as the 30 November 2026 date for Phase 2.</p></article>
  </div>
  <div class="note-box"><p>The phased approach does not give landlords leeway on other safety duties in the meantime. They should continue to keep homes safe, fit for habitation, and free of dangerous category 1 hazards, and to meet the Regulator of Social Housing's Safety and Quality standard.</p></div>
 </div>
</section>

<section class="alt times" id="timescales" aria-labelledby="times-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">Key timescales</span><h2 id="times-title">The clocks that landlords must work to</h2>
  <p>These are the current maximum timeframes in the official guidance. Landlords can and should act more quickly where the situation requires it, or where another law sets a shorter deadline.</p></div>
  <div class="grid-2">
   <article class="card reveal"><span class="num">24 hours</span><h3>Emergency hazards</h3><p>If a landlord has reasonable grounds to believe there is an emergency hazard, they must investigate it and, if the investigation confirms one, complete the relevant safety work as soon as reasonably practicable. Both the investigation and the safety work must be finished within 24 hours of the landlord becoming aware of the hazard. This clock starts immediately, not the next day.</p></article>
   <article class="card reveal"><span class="num">10 working days</span><h3>Investigating a significant hazard</h3><p>A potential significant hazard must be investigated within 10 working days of the landlord becoming aware of it. Day 1 is the day after the landlord becomes aware. Investigations can sometimes be done remotely, but if a tenant asks for an in-person inspection the landlord must arrange one.</p></article>
   <article class="card reveal"><span class="num">3 working days</span><h3>A written summary for the tenant</h3><p>After an investigation, the landlord must usually give the tenant a written summary of the findings within 3 working days of the investigation ending. The summary should say whether a significant or emergency hazard was found, what action will be taken and by when, or why no action is required, and how to contact the landlord. A written summary is not required if all the required work is finished within those 3 working days, though the tenant should still be told that the work is done.</p></article>
   <article class="card reveal"><span class="num">5 working days</span><h3>Making a significant hazard safe</h3><p>If the investigation finds a significant hazard, relevant safety work must be completed within 5 working days of the investigation ending. Temporary measures can be used to make the home safe as a first step, for example cleaning mould and providing a dehumidifier while wider work is arranged.</p></article>
   <article class="card reveal"><span class="num">5 working days, and 12 weeks</span><h3>Stopping the hazard coming back</h3><p>The landlord must begin, or take steps to begin, supplementary preventative work within 5 working days of the investigation ending. If the work itself cannot begin within 5 working days, it must begin as soon as reasonably practicable, and within 12 weeks. That further work must then be completed within a reasonable time.</p></article>
   <article class="card reveal"><span class="num">If the home cannot be made safe in time</span><h3>Alternative accommodation</h3><p>If relevant safety work cannot be completed within the initial period (24 hours for an emergency, or 5 working days for a significant hazard), the landlord must secure suitable alternative accommodation for the household, at the landlord's expense, until the safety work is done. If someone stays in the home, the landlord must give them information on how to keep safe.</p></article>
  </div>
  <div class="note-box"><p>Except for the 24 hour emergency clock, timeframes usually begin the day after the triggering event. A significant hazard is one that a reasonable landlord, with the knowledge they have or ought to have about the occupier, would make safe within 15 working days. An emergency hazard is one that a reasonable landlord would make safe within 24 hours. The assessment is about the actual people living in the home, not a notional occupier, and a full HHSRS assessment is not required.</p></div>
 </div>
</section>

<section id="records" aria-labelledby="records-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">Records and communication</span><h2 id="records-title">Keep tenants informed, and keep a clear record</h2></div>
  <div class="prose">
   <p>Social landlords are responsible for making sure tenants know their rights under Awaab's Law. Official campaign materials are available to help with this. Communication should be clear, accessible and timely, and should take account of tenants' needs, including language and accessibility.</p>
   <p>Landlords must take reasonable steps to keep the tenant updated about the timing and progress of required work until it is finished. If the work is no longer required, that should be explained clearly.</p>
   <p>The government guidance is clear that landlords should keep accurate, up-to-date information about their residents and their homes, and clear records of all engagement, investigations and communications, including reports from third parties and attempts to gain access. Those records support good decisions, and they may be needed if a case later goes to the Housing Ombudsman or to court. Landlords are also encouraged to record when a written summary was given.</p>
   <p>If the landlord cannot complete safety work in time and a tenant remains in or returns to the home, the landlord must provide clear written safety advice, and should keep a record of that advice.</p>
  </div>
 </div>
</section>

<section class="alt" id="resonest-helps" aria-labelledby="helps-title">
 <div class="wrap">
  <div class="head"><span class="eyebrow">How Resonest helps</span><h2 id="helps-title">Seeing risk earlier, with a clear trail of what was done</h2>
  <p>Resonest was built for Awaab's Law. It is a privacy-first digital twin that helps social landlords get ahead of damp, mould and cold homes, using information they already hold.</p></div>
  <div class="helps">
   <article class="reveal"><h3>Existing data, no sensors in homes</h3><p>Resonest uses existing property and weather data. There are no in-home sensors and no tenant monitoring.</p></article>
   <article class="reveal"><h3>Spotting homes at risk early</h3><p>It shows which homes will struggle first in winter, and why, so teams can focus on the homes that need help first.</p></article>
   <article class="reveal"><h3>Action lists and deadlines</h3><p>It gives officers a short action list, with deadlines for every home, so planned work is easier to see and to follow through.</p></article>
   <article class="reveal"><h3>An audit trail</h3><p>It keeps a record of what was done and what changed, which can support the kind of clear record keeping the guidance expects.</p></article>
  </div>
  <p class="caveat">Resonest can help teams see risk earlier and keep a clearer record of their work. It does not take the place of a landlord's legal duties, and using it does not, on its own, mean a landlord has complied with Awaab's Law. Investigations, safety work and communication with tenants still need to be carried out in line with the regulations.</p>
 </div>
</section>

<section class="contact" id="contact" aria-labelledby="contact-title">
 <div class="wrap">
  <span class="eyebrow">Contact</span>
  <h2 id="contact-title">Want to talk about Resonest and Awaab's Law?</h2>
  <p>Tell us about your homes and your teams. We would be glad to show you how Resonest can help you see risk earlier.</p>
  <a class="btn gold" href="{mailto}">Email us <span aria-hidden="true">→</span></a>
  <a class="mail" href="mailto:{MAIL}">{MAIL}</a>
 </div>
</section>
<div class="disclaimer">
 <div class="wrap">
  <p>This page is general information about Awaab's Law, written in plain English for housing teams. It is not legal advice, and it is not a substitute for the official regulations or guidance. Landlords should read the government's guidance and take their own legal advice if they are unsure about their duties.</p>
  <p>The official collection of government documents is <a href="https://www.gov.uk/government/collections/awaabs-law-in-the-social-rented-sector">Awaab's Law in the social rented sector</a> on GOV.UK. The current process guidance for social landlords from 30 November 2026 is the <a href="https://www.gov.uk/government/publications/awaabs-law-phase-2-guidance-for-social-housing-landlords/awaabs-law-phase-2-guidance-for-social-landlords">Phase 2 guidance for social landlords</a>. Phase 1 guidance remains relevant until 11:59pm on 29 November 2026. There is also <a href="https://www.gov.uk/government/publications/awaabs-law-guidance-for-tenants-in-social-housing/awaabs-law-guidance-for-tenants-in-social-housing">guidance for tenants in social housing</a>.</p>
  <div class="sources">
   <h3>Sources used for this page</h3>
   <ol>
    <li><a href="https://www.gov.uk/government/collections/awaabs-law-in-the-social-rented-sector">Awaab's Law in the social rented sector</a>, Ministry of Housing, Communities and Local Government (MHCLG), collection published 13 July 2026.</li>
    <li><a href="https://www.gov.uk/government/publications/awaabs-law-phase-2-guidance-for-social-housing-landlords/awaabs-law-phase-2-guidance-for-social-landlords">Awaab's Law Phase 2: Guidance for social landlords</a>, MHCLG, updated 31 July 2026.</li>
    <li><a href="https://www.gov.uk/government/publications/awaabs-law-guidance-for-social-landlords">Awaab's Law Phase 1: Guidance for social landlords</a>, MHCLG, last updated 16 July 2026. In effect until 11:59pm on 29 November 2026.</li>
    <li><a href="https://www.gov.uk/government/publications/awaabs-law-guidance-for-tenants-in-social-housing/awaabs-law-guidance-for-tenants-in-social-housing">Awaab's Law: Guidance for tenants in social housing</a>, MHCLG.</li>
    <li><a href="https://www.gov.uk/government/news/safer-homes-for-4m-tenants-with-quicker-action-on-dangerous-homes">Safer homes for 4m tenants with quicker action on dangerous homes</a>, MHCLG news story, which confirms the 30 November 2026 Phase 2 date and that Phase 3 is to be introduced in 2027.</li>
   </ol>
  </div>
 </div>
</div>
</main>
{footer_html(t, "awaab")}
{site_script()}
</body>
</html>"""
    return html


CHAT_JS = r"""
(function(){
  var API="/api/chat";
  var MAX_MSG=1200;
  var MAX_TURNS=12;
  var SYSTEM="You are Joe, a friendly helper on the Watson Atlas website. Watson Atlas is UK housing software from the team behind Rowe AI, a Scottish software company. You help visitors work out what they need and what help they want.\n\nBe warm, concise and professional, in British English. Do not use en dashes or em dashes. Use commas, colons or short sentences instead.\n\nWhat Watson Atlas offers:\n- Resonest is a privacy-first digital twin, built for Awaab's Law. It uses existing property and weather data, with no in-home sensors or tenant monitoring. It helps social landlords get ahead of damp, mould and cold homes by showing which homes will struggle first in winter and why, with clear action lists and deadlines, and an audit trail of what was done.\n- SiteOps is a housing compliance platform for capturing inspections on site and turning them into consistent, branded PDF reports. It includes a property register keyed on UPRN, a no-code form and report designer, job planning, and a mobile app for on-site capture. A repairs and maintenance module is on the roadmap.\n- Around those products, Watson Atlas also offers building safety and cladding reporting, a field and surveyor app, property data, integrations with a landlord's existing housing system, and bespoke housing software.\n- Rowe AI holds Cyber Essentials certification.\n\nRules you must follow:\n- Never name clients or customer organisations.\n- Never give legal advice. If asked about legal duties under Awaab's Law, give a short plain-English outline and point people to the official UK government guidance at https://www.gov.uk/government/collections/awaabs-law-in-the-social-rented-sector and to the explainer on this site at /awaabs-law/.\n- Never invent prices, contracts, timescales for our work, or promises of legal compliance. Using Resonest does not, on its own, mean a landlord has complied with Awaab's Law.\n- If you are unsure, say so.\n- When it is natural, nudge the visitor to leave their details or start a conversation via the contact section on this page, or by emailing info@rowe.ai.\n\nKeep answers short: a few short paragraphs or a short list, unless the visitor asks for more detail.";
  var log=document.getElementById("chat-log");
  var form=document.getElementById("chat-form");
  var input=document.getElementById("chat-input");
  var send=document.getElementById("chat-send");
  var chips=document.getElementById("chat-chips");
  var history=[];
  var busy=false;
  var unavailable=false;

  function el(cls, html){
    var d=document.createElement("div");
    d.className="bubble "+cls;
    d.innerHTML=html;
    return d;
  }
  function esc(s){
    return String(s).replace(/[&<>"]/g,function(c){return ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"})[c];});
  }
  function toHtml(s){
    return esc(s).replace(/\n\n/g,"</p><p>").replace(/\n/g,"<br>");
  }
  function add(cls, text){
    var b=el(cls, "<p>"+toHtml(text)+"</p>");
    log.appendChild(b);
    log.scrollTop=log.scrollHeight;
    return b;
  }
  function setBusy(v){
    busy=v;
    send.disabled=v || unavailable;
    input.disabled=unavailable;
  }
  function fallback(msg){
    unavailable=true;
    add("sys", msg || "The chat is not available just now. You are welcome to email us at info@rowe.ai, or use the contact section below, and we will get back to you.");
    if(chips) chips.style.display="none";
    setBusy(false);
  }
  async function ask(text){
    text=(text||"").trim();
    if(!text || busy || unavailable) return;
    if(text.length>MAX_MSG){
      add("sys","That message is a little long. Could you shorten it to "+MAX_MSG+" characters or fewer?");
      return;
    }
    if(history.filter(function(m){return m.role==="user";}).length>=MAX_TURNS){
      add("sys","We have reached the end of this chat for now. Please email info@rowe.ai and we will happily continue the conversation.");
      return;
    }
    add("you", text);
    history.push({role:"user", content:text});
    if(chips) chips.style.display="none";
    setBusy(true);
    var thinking=add("sys","Joe is writing a reply...");
    var body={
      model:"grok-4.3",
      messages:[{role:"system", content:SYSTEM}].concat(history),
      max_tokens:400,
      temperature:0.6
    };
    try{
      var res=await fetch(API,{
        method:"POST",
        headers:{"Content-Type":"application/json","Accept":"application/json"},
        body:JSON.stringify(body)
      });
      if(res.status===404 || res.status===501 || res.status===401){
        thinking.remove();
        fallback("The chat is not quite ready yet. Please use the contact section below and we will get back to you.");
        return;
      }
      if(res.status===429){
        thinking.remove();
        add("sys","The chat is a little busy just now. Please try again in a little while, or email info@rowe.ai.");
        history.pop();
        setBusy(false);
        return;
      }
      if(!res.ok){
        thinking.remove();
        fallback("Sorry, the chat could not be started just now. Please email info@rowe.ai and we will help you from there.");
        return;
      }
      var data=await res.json();
      var reply=data && data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content;
      thinking.remove();
      if(!reply){
        add("sys","Sorry, I could not read that reply. Please try again, or email info@rowe.ai.");
        history.pop();
        setBusy(false);
        return;
      }
      history.push({role:"assistant", content:reply});
      add("joe", reply);
    }catch(err){
      thinking.remove();
      fallback("Sorry, we could not reach the chat just now. Please email info@rowe.ai, or leave a message in the contact section below.");
      return;
    }
    setBusy(false);
    input.focus();
  }
  form.addEventListener("submit", function(e){
    e.preventDefault();
    var v=input.value;
    input.value="";
    ask(v);
  });
  input.addEventListener("keydown", function(e){
    if(e.key==="Enter" && !e.shiftKey){
      e.preventDefault();
      form.requestSubmit();
    }
  });
  if(chips){
    chips.querySelectorAll("button").forEach(function(b){
      b.addEventListener("click", function(){ ask(b.getAttribute("data-q")||b.textContent); });
    });
  }
})();
"""


def render_help(t):
    from build import MAIL, mailto, header_html, footer_html, site_script, street_svg

    html = _head(
        t,
        "How can we help? | Watson Atlas",
        "Chat with Joe, a Watson Atlas helper, to work out whether Resonest, SiteOps or another part of our housing software is the right fit.",
        page="help",
    )
    html += f"""<body>
<a class="skip" href="#main">Skip to content</a>
{header_html(t, "help")}
<main id="main">
<section class="hero hero-small" aria-labelledby="hero-title">
 <div class="moon" aria-hidden="true"></div>
 <div class="wrap">
   <span class="eyebrow">How can we help?</span>
   <h1 id="hero-title">Tell us what you need, <em>and we will help you find the right starting point.</em></h1>
   <p class="lead">Joe is a chat assistant on this site. He can help you work out whether Resonest, SiteOps or another part of our housing software is the right place to begin. When you are ready, you can also email us directly.</p>
 </div>
 {street_svg(n=12, w=1440, h=180, seed=3)}
 <div class="road" aria-hidden="true"></div>
</section>

<section id="chat" aria-labelledby="chat-title">
 <div class="wrap">
  <div class="head" style="margin-left:auto;margin-right:auto;text-align:center">
   <span class="eyebrow">Chat with Joe</span>
   <h2 id="chat-title">A quick way to see what might help</h2>
  </div>
  <div class="chat-wrap">
   <div class="chat" id="chat-panel">
    <div class="chat-log" id="chat-log" role="log" aria-live="polite">
     <div class="bubble joe"><p>Hello, I am Joe. I can help you work out what you need from Watson Atlas, whether that is Resonest, SiteOps, or something more bespoke. What would you like to look at?</p></div>
    </div>
    <div class="chips" id="chat-chips">
     <button type="button" data-q="Tell me about Resonest">Tell me about Resonest</button>
     <button type="button" data-q="What is Awaab's Law?">What is Awaab's Law?</button>
     <button type="button" data-q="I need inspection software">I need inspection software</button>
    </div>
    <form class="composer" id="chat-form">
     <label class="skip" for="chat-input">Your message</label>
     <textarea id="chat-input" name="message" rows="2" maxlength="1200" placeholder="Ask Joe a question..." required></textarea>
     <button class="send" id="chat-send" type="submit">Send</button>
    </form>
   </div>
   <p class="ai-note">Joe is an AI assistant and may make mistakes. For legal questions about Awaab's Law, please read the official guidance. Nothing here is legal advice or a formal quote.</p>
  </div>
 </div>
</section>

<section class="contact" id="contact" aria-labelledby="contact-title">
 <div class="wrap">
  <span class="eyebrow">Contact</span>
  <h2 id="contact-title">Would you rather talk to us directly?</h2>
  <p>Tell us about your homes, your teams and your plans. We would love to explore what we could build together.</p>
  <a class="btn gold" href="{mailto}">Email us <span aria-hidden="true">→</span></a>
  <a class="mail" href="mailto:{MAIL}">{MAIL}</a>
 </div>
</section>
</main>
{footer_html(t, "help")}
{site_script()}
<script>{CHAT_JS}</script>
</body>
</html>"""
    return html
