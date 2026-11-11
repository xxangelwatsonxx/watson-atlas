from content import *
def reso_mock():
    rows=[("Home 014","High",WARM,"Ventilation check before December"),("Home 027","High",WARM,"Loft insulation top-up"),("Home 033","Medium",COOL,"Monitor, review after cold spell"),("Home 041","Medium",COOL,"Draught proofing"),("Home 052","Low","#9bb59a","No action needed")]
    tr="".join(f'<tr><td>{a}</td><td><span class="pill" style="background:{c}">{b}</span></td><td>{d}</td></tr>' for a,b,c,d in rows)
    grid="".join(f'<i style="background:{[WARM,COOL,"#9bb59a","#9bb59a",COOL,"#9bb59a"][(k*7)%6]}"></i>' for k in range(48))
    return f'''<div class="mock"><div class="bar"><b>Resonest</b><span>Winter outlook · Illustrative example</span></div><div class="mbody">
<div class="side"><div class="mk">Portfolio heat view</div><div class="grid">{grid}</div><div class="mk" style="margin-top:14px">Awaab's Law actions</div><div class="due"><b>Clear list</b><span>Every home with a next step and a deadline</span></div></div>
<table><tr><th>Home</th><th>Winter risk</th><th>Suggested next step</th></tr>{tr}</table></div></div>'''
def site_mock():
    f=["Property (UPRN)","Inspection type","Findings","Photos","Sign off"]
    return f'''<div class="mock"><div class="bar"><b>SiteOps</b><span>Inspection form · Illustrative example</span></div><div class="mbody">
<div class="form">{"".join(f'<label>{x}<span></span></label>' for x in f)}<a class="mbtn">Generate branded PDF</a></div>
<div class="phone"><div class="scr"><div class="ph-h">On site</div><div class="ph-l"></div><div class="ph-l s"></div><div class="ph-img"></div><div class="ph-l"></div><div class="ph-b">Save &amp; sync</div></div></div></div></div>'''
css=f'''
header{{display:flex;justify-content:space-between;align-items:center;padding:18px 48px;background:{WHITE};color:{NAVY};border-bottom:1px solid #e6e0d4;position:sticky;top:0;z-index:10}}
header nav{{display:flex;gap:24px;font-size:13px;font-weight:600}} header nav a{{text-decoration:none}}
.btn{{white-space:nowrap;display:inline-block;padding:13px 24px;border-radius:10px;font-weight:700;text-decoration:none;font-size:14px;background:{NAVY};color:{WHITE}}} .btn.c{{background:{CREAM};color:{NAVY}}}
.intro{{text-align:center;padding:56px 48px 34px;background:{WHITE}}} .intro h1{{font-size:46px;color:{NAVY};margin:10px 0 12px;font-weight:800;letter-spacing:-.02em}} .intro p{{max-width:760px;margin:0 auto;color:#2b3a5c;line-height:1.6;font-size:17px}}
.k{{font-size:12px;letter-spacing:.22em;font-weight:700;text-transform:uppercase;color:#8a6b3c}}
.doors{{display:grid;grid-template-columns:1fr 1fr;min-height:560px}}
.doors a{{text-decoration:none;padding:64px 64px 56px;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}}
.doors .d1{{background:{NAVY};color:{WHITE}}} .doors .d2{{background:{CREAM};color:{NAVY}}}
.doors h2{{font-size:72px;margin:14px 0 8px;font-weight:800;letter-spacing:-.03em}} .doors h3{{font-size:26px;margin:0 0 18px;font-weight:600}} .doors p{{font-size:16px;line-height:1.65;max-width:470px;opacity:.9}}
.doors .go{{font-weight:700;font-size:15px;margin-top:26px}} .doors .arch{{position:absolute;right:-60px;bottom:-60px;width:320px;height:420px;border-radius:160px 160px 0 0;border:2px solid currentColor;opacity:.18}}
section{{padding:96px 48px}} .wrap{{max-width:1240px;margin:0 auto}}
h2.s{{font-size:44px;margin:10px 0 18px;color:{NAVY};font-weight:800;letter-spacing:-.02em}} .lead{{font-size:17px;line-height:1.65;color:#2b3a5c;max-width:720px}}
.deep{{display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:center}}
.deep ul{{padding:0;list-style:none;margin:22px 0}} .deep li{{padding:12px 0 12px 34px;border-bottom:1px solid #e2d8c6;position:relative;line-height:1.55;color:#2b3a5c;font-size:15px}}
.deep li:before{{content:"";position:absolute;left:0;top:15px;width:18px;height:18px;border-radius:50%;background:{NAVY};box-shadow:inset 0 0 0 5px {CREAM}}}
.dark{{background:{NAVY};color:{WHITE}}} .dark h2.s{{color:{WHITE}}} .dark .lead,.dark li{{color:#dbe2f0}} .dark li{{border-color:rgba(255,255,255,.14)}} .dark .k{{color:{CREAM}}}
.mock{{background:{WHITE};border-radius:16px;box-shadow:0 30px 70px rgba(0,0,0,.28);overflow:hidden;color:{NAVY};font-size:13px}}
.mock .bar{{background:{NAVY2};color:{WHITE};padding:12px 18px;display:flex;justify-content:space-between}} .mock .bar span{{opacity:.7;font-size:12px}}
.mbody{{display:grid;grid-template-columns:200px 1fr;gap:18px;padding:18px}}
.mk{{font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:8px}} .grid{{display:grid;grid-template-columns:repeat(8,1fr);gap:4px}} .grid i{{aspect-ratio:1;border-radius:3px}}
.due{{background:{CREAM};border-radius:10px;padding:12px}} .due b{{display:block}} .due span{{font-size:12px}}
table{{border-collapse:collapse;width:100%}} th{{text-align:left;font-size:11px;letter-spacing:.08em;text-transform:uppercase;padding:8px;border-bottom:2px solid {NAVY}}} td{{padding:10px 8px;border-bottom:1px solid #eee}}
.pill{{padding:3px 10px;border-radius:99px;color:#fff;font-weight:700;font-size:11px}}
.form{{grid-column:1/2;display:flex;flex-direction:column;gap:10px}} .mock .mbody:has(.phone){{grid-template-columns:1fr 200px}}
.form label{{font-weight:600;font-size:12px}} .form label span{{display:block;height:30px;border:1.5px solid #d9d2c4;border-radius:8px;margin-top:4px;background:#faf7f1}}
.mbtn{{background:{NAVY};color:#fff;text-align:center;padding:10px;border-radius:8px;font-weight:700}}
.phone{{background:{NAVY};border-radius:26px;padding:10px}} .scr{{background:{CREAM};border-radius:18px;height:340px;padding:14px;display:flex;flex-direction:column;gap:10px}}
.ph-h{{font-weight:800}} .ph-l{{height:12px;background:#d8ccb4;border-radius:6px}} .ph-l.s{{width:60%}} .ph-img{{flex:1;background:repeating-linear-gradient(45deg,#e7dcc6 0 10px,#efe5d3 10px 20px);border-radius:10px}} .ph-b{{background:{NAVY};color:#fff;text-align:center;border-radius:8px;padding:8px;font-weight:700;font-size:12px}}
.caps{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:40px}} .caps div{{background:{WHITE};border-radius:14px;padding:24px;border-top:4px solid {NAVY}}} .caps h4{{margin:0 0 10px;color:{NAVY}}} .caps p{{margin:0;font-size:13.5px;line-height:1.6;color:#2b3a5c}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:56px}} .steps div{{display:grid;grid-template-columns:44px 1fr;gap:14px;padding:14px 0;border-bottom:1px solid #e2d8c6}} .steps b{{font-size:22px;color:{NAVY}}} .steps h4{{margin:0 0 4px;color:{NAVY}}} .steps p{{margin:0;font-size:14px;color:#2b3a5c;line-height:1.55}}
.vals{{display:grid;grid-template-columns:1fr 1fr;gap:14px}} .vals div{{background:{CREAM};border-radius:14px;padding:22px}} .vals h4{{margin:0 0 6px;color:{NAVY}}} .vals p{{margin:0;font-size:14px;color:#2b3a5c;line-height:1.55}}
.who{{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}} .who span{{border:1.5px solid {CREAM};border-radius:99px;padding:12px 22px;font-weight:600}}
footer{{background:{CREAM};padding:80px 48px 36px;color:{NAVY}}} footer .row{{display:flex;justify-content:space-between;align-items:center;gap:40px;flex-wrap:wrap}} footer h2{{font-size:46px;margin:0 0 12px}} footer small{{display:block;margin-top:56px;opacity:.7}}
@media(max-width:900px){{header nav{{display:none}} .doors,.deep,.split{{grid-template-columns:1fr}} .doors h2{{font-size:48px}} .caps{{grid-template-columns:1fr 1fr}} section{{padding:64px 22px}}}}
'''
body=f'''<header>{lockup(NAVY,40)}<nav>{navlinks()}</nav><a class="btn" href="#contact">Book a demo chat</a></header>
<div class="intro"><div class="k">UK Housing Software</div><h1>Two ways to care for every home.</h1><p>{HERO_SUB}</p></div>
<div class="doors"><a class="d1" href="#resonest"><div><div class="k" style="color:{CREAM}">Built for Awaab's Law</div><h2>Resonest</h2><h3>Warmer, healthier homes, seen early.</h3><p>{RESO_LEAD}</p></div><span class="go">Explore Resonest &rarr;</span><div class="arch"></div></a>
<a class="d2" href="#siteops"><div><div class="k">Housing compliance</div><h2>SiteOps</h2><h3>Inspections done right, first time.</h3><p>{SITE_LEAD}</p></div><span class="go">Explore SiteOps &rarr;</span><div class="arch"></div></a></div>
<section class="dark" id="resonest"><div class="wrap deep"><div><div class="k">Resonest</div><h2 class="s">Get ahead of damp, mould and cold homes</h2><p class="lead">Resonest helps teams meet Awaab's Law with confidence, using data you already hold.</p>{ul(RESO)}</div>{reso_mock()}</div></section>
<section style="background:{WHITE}" id="siteops"><div class="wrap deep"><div>{site_mock()}</div><div><div class="k">SiteOps</div><h2 class="s">From site visit to branded report, tied to the right home</h2><p class="lead">Works alongside your existing housing system, rather than replacing it.</p>{ul(SITE)}<p class="k" style="letter-spacing:.08em;text-transform:none">{SITE_ROAD}</p></div></div></section>
<section style="background:{CREAM}" id="capabilities"><div class="wrap"><div class="k">Around Resonest and SiteOps</div><h2 class="s">Everything that makes the two products sing</h2>
<div class="caps">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in CAPS)}</div></div></section>
<section style="background:{WHITE}" id="how"><div class="wrap split"><div class="steps"><div class="k">How we work</div><h2 class="s">Clear steps, shared goals</h2>{"".join(f'<div><b>{i+1}</b><span><h4>{t}</h4><p>{d}</p></span></div>' for i,(t,d) in enumerate(STEPS))}</div>
<div><div class="k">What we value</div><h2 class="s">Lasting partnerships</h2><div class="vals">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in VALUES)}</div></div></div></section>
<section class="dark" id="who"><div class="wrap split"><div><div class="k">Who we help</div><h2 class="s">Built for UK housing organisations</h2><p class="lead">We work with social landlords, council housing teams, residential landlords and building safety consultancies that want their homes, data and teams to work better together.</p><div class="who">{"".join(f"<span>{t}</span>" for t,_ in SECTORS)}</div></div>
<div id="about"><div class="k">About</div><h2 class="s">Big aspirations for UK housing</h2><p class="lead">{ABOUT1}</p><p class="lead">{ABOUT2}</p><div class="who">{"".join(f"<span style='border-style:solid'>{b}</span>" for b in BADGES)}</div></div></div></section>
<footer id="contact"><div class="wrap"><div class="row"><div><div class="k">Contact</div><h2>Which door would you like to open first?</h2><p class="lead">Tell us about your homes, your teams and your plans. We would love to explore what we could build together.</p></div><div style="display:flex;gap:12px"><a class="btn" href="mailto:{EMAIL}?subject=Resonest">Ask about Resonest</a><a class="btn" style="background:#fff;color:{NAVY}" href="mailto:{EMAIL}?subject=SiteOps">Ask about SiteOps</a></div></div>
<div class="row" style="margin-top:56px;border-top:1px solid #d8ccb4;padding-top:28px">{lockup(NAVY,36)}<span>{EMAIL}</span></div><small>{FOOT} Product screens shown are illustrative.</small></div></footer>'''
import pathlib; p=pathlib.Path("two-doors"); p.mkdir(exist_ok=True); (p/"index.html").write_text(page("Watson Atlas · Two Doors (draft)",css,body))
