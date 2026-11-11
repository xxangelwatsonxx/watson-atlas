from content import *
css=f'''
body{{background:{CREAM};color:{NAVY}}}
header{{display:flex;justify-content:space-between;align-items:center;padding:28px 72px}}
header nav{{display:flex;gap:30px;font-size:14px;font-weight:500}} header nav a{{text-decoration:none}}
.btn{{display:inline-block;background:{NAVY};color:{CREAM};padding:18px 34px;border-radius:99px;font-weight:600;text-decoration:none;font-size:15px}} .btn.l{{background:transparent;color:{NAVY};box-shadow:inset 0 0 0 1.5px {NAVY}}}
.hero{{padding:120px 72px 140px;max-width:1300px;margin:0 auto}}
.hero h1{{font-size:96px;line-height:1.02;font-weight:300;letter-spacing:-.035em;margin:0 0 40px;max-width:1150px}} .hero h1 b{{font-weight:700}}
.hero p{{font-size:21px;line-height:1.6;max-width:720px;margin:0 0 44px;color:#2b3a5c}}
.small{{font-size:13px;font-weight:600;letter-spacing:.06em;color:#7a6440}}
section{{padding:120px 72px}} .wrap{{max-width:1200px;margin:0 auto}}
.big{{font-size:56px;line-height:1.12;font-weight:300;letter-spacing:-.025em;margin:16px 0 28px;max-width:1000px}} .big b{{font-weight:700}}
.lead{{font-size:19px;line-height:1.7;color:#2b3a5c;max-width:760px}}
.white{{background:{WHITE}}} .navy{{background:{NAVY};color:{CREAM}}} .navy .lead{{color:#dfe5f1}} .navy .small{{color:{CREAM};opacity:.8}}
.vals{{display:grid;grid-template-columns:1fr 1fr;gap:70px 90px;margin-top:70px}} .vals h3{{font-size:28px;font-weight:600;margin:0 0 12px}} .vals p{{font-size:17px;line-height:1.7;margin:0;color:#2b3a5c}}
.vals .n{{display:block;width:44px;height:44px;border-radius:50%;background:{CREAM};margin-bottom:22px;display:grid;place-items:center;font-weight:700}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:60px}} .card{{background:{WHITE};border-radius:28px;padding:48px}} .card h3{{font-size:40px;margin:8px 0 16px;letter-spacing:-.02em}} .card p{{font-size:17px;line-height:1.7;color:#2b3a5c}}
.card ul{{list-style:none;padding:0;margin:24px 0 0}} .card li{{padding:12px 0;border-top:1px solid #eee4d2;font-size:15px;line-height:1.55;color:#2b3a5c}}
.mini{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:28px}} .mini div{{background:rgba(255,255,255,.6);border-radius:22px;padding:28px}} .mini h4{{margin:0 0 10px;font-size:17px}} .mini p{{margin:0;font-size:14px;line-height:1.65;color:#2b3a5c}}
.steps{{display:flex;gap:0;margin-top:60px}} .steps div{{flex:1;padding:0 26px 0 0}} .steps h4{{font-size:22px;font-weight:600;margin:14px 0 8px;color:{WHITE}}} .steps p{{margin:0;font-size:15px;line-height:1.65;color:#dfe5f1}} .steps .o{{width:16px;height:16px;border-radius:50%;background:{CREAM}}}
.who{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:56px}} .who div{{border-radius:22px;padding:28px;background:{CREAM}}} .who h4{{margin:0 0 10px}} .who p{{margin:0;font-size:14px;line-height:1.65;color:#2b3a5c}}
.about{{display:grid;grid-template-columns:auto 1fr;gap:80px;align-items:center}} .badges span{{display:inline-block;background:{WHITE};border-radius:99px;padding:10px 18px;margin:0 8px 8px 0;font-size:14px;font-weight:500}}
.contact{{text-align:center;padding:150px 72px}} .contact .big{{margin:16px auto 28px;font-size:72px}} .contact .lead{{margin:0 auto 44px}}
footer{{display:flex;justify-content:space-between;align-items:center;padding:36px 72px;border-top:1px solid #e0d3bb;font-size:13px;flex-wrap:wrap;gap:20px}}
@media(max-width:900px){{header nav{{display:none}} header,.hero,section,footer{{padding-left:24px;padding-right:24px}} .hero h1{{font-size:52px}} .big,.contact .big{{font-size:38px}} .vals,.cards,.about{{grid-template-columns:1fr}} .mini,.who{{grid-template-columns:1fr 1fr}} .steps{{flex-direction:column;gap:30px}}}}
'''
body=f'''<header>{lockup(NAVY,46)}<nav>{navlinks()}</nav><a class="btn" style="padding:12px 24px" href="#contact">Say hello</a></header>
<div class="hero"><div class="small">UK Housing Software</div><br><h1>Homes that are <b>cared for</b>, not just counted.</h1><p>{HERO_SUB}</p><a class="btn" href="#contact">Start a conversation</a> &nbsp; <a class="btn l" href="#resonest">See what we build</a></div>
<section class="white" id="how"><div class="wrap"><div class="small">Relationship before business</div><p class="big">We start by <b>listening</b>. To your teams, your residents and your plans for the homes you look after.</p><p class="lead">Long-term partnerships come first. Software follows, built around how your organisation really works.</p>
<div class="vals">{"".join(f'<div><span class="n">{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(VALUES))}</div></div></section>
<section id="resonest"><div class="wrap"><div class="small">What we build</div><p class="big">Two simple tools, <b>one big aspiration</b>: every home safe, warm and well looked after.</p>
<div class="cards"><div class="card"><div class="small">Built for Awaab's Law</div><h3>Resonest</h3><p>{RESO_LEAD}</p>{ul(RESO)}</div>
<div class="card" id="siteops"><div class="small">Housing compliance</div><h3>SiteOps</h3><p>{SITE_LEAD}</p>{ul(SITE)}<p class="small" style="margin-top:18px">{SITE_ROAD}</p></div></div>
<div class="mini" id="capabilities">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in CAPS)}</div></div></section>
<section class="navy"><div class="wrap"><div class="small">How we work together</div><p class="big" style="color:{WHITE}">Clear steps, shared goals, <b>always looking forward</b>.</p><p class="lead">Every engagement follows a simple, transparent path, so you always know where things stand and what comes next.</p>
<div class="steps">{"".join(f'<div><span class="o" style="display:block"></span><h4>{t}</h4><p>{d}</p></div>' for t,d in STEPS)}</div></div></section>
<section class="white" id="who"><div class="wrap"><div class="small">Who we help</div><p class="big">Built for the people who look after <b>UK homes</b>.</p><p class="lead">We work with social landlords, council housing teams, residential landlords and building safety consultancies that want their homes, data and teams to work better together.</p>
<div class="who">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in SECTORS)}</div></div></section>
<section id="about"><div class="wrap about"><div style="background:{NAVY};border-radius:40px;padding:60px">{mono(CREAM,220)}</div><div><div class="small">About us</div><p class="big" style="font-size:46px">Big aspirations for <b>UK housing</b>.</p><p class="lead">{ABOUT1}</p><p class="lead">{ABOUT2}</p><div class="badges">{"".join(f"<span>{b}</span>" for b in BADGES)}</div></div></div></section>
<div class="contact white" id="contact"><div class="small">Contact</div><p class="big">What could work better <b>for your homes?</b></p><p class="lead">Tell us about your homes, your teams and your plans. We would love to explore what we could build together.</p><a class="btn" href="mailto:{EMAIL}">Email {EMAIL}</a></div>
<footer>{lockup(NAVY,36)}<span>{FOOT}</span></footer>'''
import pathlib; p=pathlib.Path("calm-and-human"); p.mkdir(exist_ok=True); (p/"index.html").write_text(page("Watson Atlas · Calm and Human (draft)",css,body))
