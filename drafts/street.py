from content import *
import random
def street(n=12, w=1440, h=300, warmset=(2,5,9), coolset=(0,7,11), base=NAVY, line=CREAM, glow=True, seed=3):
    r=random.Random(seed); x=0; out=[]; hw=w/n
    for i in range(n):
        bh=r.choice([130,150,170,190]); roof=r.choice(["gable","flat","gable","step"]); bw=hw-8
        x0=i*hw+4; y0=h-bh
        out.append(f'<rect x="{x0:.0f}" y="{y0}" width="{bw:.0f}" height="{bh}" fill="{base}" stroke="{line}" stroke-width="2"/>')
        if roof=="gable": out.append(f'<polygon points="{x0-4:.0f},{y0} {x0+bw/2:.0f},{y0-46} {x0+bw+4:.0f},{y0}" fill="{base}" stroke="{line}" stroke-width="2"/>')
        elif roof=="step": out.append(f'<rect x="{x0+bw*.6:.0f}" y="{y0-34}" width="14" height="34" fill="{base}" stroke="{line}" stroke-width="2"/>')
        col = WARM if i in warmset else (COOL if i in coolset else "#F5ECDC")
        op = 1 if (i in warmset or i in coolset) else .35
        for yy in range(y0+18, h-50, 38):
            for k in (0,1):
                wx=x0+bw*(.18+k*.46)
                out.append(f'<rect x="{wx:.0f}" y="{yy}" width="{bw*.2:.0f}" height="22" rx="2" fill="{col}" opacity="{op}"/>')
        out.append(f'<rect x="{x0+bw*.4:.0f}" y="{h-42}" width="{bw*.2:.0f}" height="42" fill="{line}" opacity=".85"/>')
    return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMax meet" style="display:block;width:100%">{"".join(out)}<rect y="{h-2}" width="{w}" height="2" fill="{line}"/></svg>'
def house(label_no, col=CREAM, win=WARM):
    return f'''<svg viewBox="0 0 120 130" width="120" height="130"><polygon points="6,52 60,8 114,52" fill="{NAVY}"/><rect x="16" y="50" width="88" height="78" fill="{NAVY}"/>
<rect x="28" y="64" width="20" height="18" rx="2" fill="{win}"/><rect x="72" y="64" width="20" height="18" rx="2" fill="{win}"/><rect x="50" y="94" width="20" height="34" fill="{col}"/>
<text x="60" y="44" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="14" fill="{CREAM}">{label_no}</text></svg>'''
css=f'''
header{{position:sticky;top:0;z-index:10;background:{NAVY};color:{CREAM};display:flex;justify-content:space-between;align-items:center;padding:16px 56px;border-bottom:1px solid rgba(245,236,220,.15)}}
header nav{{display:flex;gap:26px;font-size:13px;font-weight:500}} header nav a{{text-decoration:none;opacity:.85}}
.btn{{display:inline-block;background:{CREAM};color:{NAVY};padding:14px 26px;border-radius:99px;font-weight:700;text-decoration:none;font-size:14px}}
.btn.ghost{{background:transparent;color:{CREAM};border:1.5px solid {CREAM}}}
.hero{{background:linear-gradient(180deg,#071634 0%,{NAVY} 70%);color:{WHITE};padding:90px 56px 0;text-align:center;position:relative;overflow:hidden}}
.hero .moon{{position:absolute;right:12%;top:70px;width:70px;height:70px;border-radius:50%;background:{CREAM};box-shadow:0 0 60px rgba(245,236,220,.5)}}
.hero h1{{font-size:64px;line-height:1.05;margin:0 auto 22px;max-width:960px;font-weight:800;letter-spacing:-.02em}}
.hero h1 em{{font-style:normal;color:{CREAM}}}
.hero p{{max-width:720px;margin:0 auto 34px;font-size:18px;line-height:1.6;opacity:.85}}
.legend{{display:flex;gap:28px;justify-content:center;font-size:13px;margin:28px 0 36px;color:{CREAM}}} .legend i{{display:inline-block;width:14px;height:14px;border-radius:3px;margin-right:8px;vertical-align:-2px}}
.road{{background:#1b2a4a;height:56px;position:relative}} .road:after{{content:"";position:absolute;left:0;right:0;top:26px;height:4px;background:{CREAM};opacity:.35;height:2px}}
section{{padding:96px 56px}} .wrap{{max-width:1200px;margin:0 auto}}
.kicker{{font-size:12px;letter-spacing:.22em;font-weight:700;text-transform:uppercase;color:#8a6b3c}}
h2{{font-size:42px;line-height:1.1;margin:12px 0 18px;color:{NAVY};font-weight:800;letter-spacing:-.01em}}
.lead{{font-size:18px;line-height:1.65;color:#2b3a5c;max-width:760px}}
.door{{display:grid;grid-template-columns:140px 1fr 1fr;gap:48px;align-items:start;padding:56px 0;border-top:2px solid {NAVY}}}
.door h3{{font-size:30px;color:{NAVY};margin:0 0 12px}} .door ul{{margin:0;padding-left:20px;line-height:1.7;color:#2b3a5c}} .door p{{line-height:1.65;color:#2b3a5c;margin:0 0 14px}}
.note{{font-size:13px;font-weight:600;color:#8a6b3c}}
.cream{{background:{CREAM}}} .white{{background:{WHITE}}}
.terrace{{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:44px}}
.terrace .h{{background:{NAVY};color:{CREAM};padding:28px 22px 30px;position:relative;margin-top:40px;border-right:2px solid {CREAM}}}
.terrace .h:before{{content:"";position:absolute;left:0;right:0;top:-40px;height:40px;background:{NAVY};clip-path:polygon(0 100%,50% 0,100% 100%)}}
.terrace .h b{{display:block;font-size:12px;letter-spacing:.2em;color:{WARM};margin-bottom:10px}} .terrace h4{{margin:0 0 10px;font-size:17px}} .terrace p{{margin:0;font-size:13.5px;line-height:1.6;opacity:.85}}
.walk{{display:grid;grid-template-columns:repeat(5,1fr);gap:24px;margin-top:40px;position:relative}}
.walk:before{{content:"";position:absolute;left:4%;right:4%;top:22px;border-top:3px solid {NAVY}}}
.walk div{{position:relative}} .walk span{{display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:{NAVY};color:{CREAM};font-weight:700;margin-bottom:16px}}
.walk h4{{margin:0 0 8px;color:{NAVY}}} .walk p{{margin:0;font-size:14px;line-height:1.6;color:#2b3a5c}}
.vals{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:56px}} .vals div{{background:{WHITE};border-radius:14px;padding:26px}} .vals h4{{margin:0 0 8px;color:{NAVY}}} .vals p{{margin:0;font-size:14px;line-height:1.6;color:#2b3a5c}}
.who{{display:grid;grid-template-columns:repeat(5,1fr);gap:18px;margin-top:40px}} .who div{{border:1.5px solid {NAVY};border-radius:14px;padding:22px}} .who h4{{margin:0 0 8px;color:{NAVY};font-size:16px}} .who p{{margin:0;font-size:13.5px;line-height:1.6;color:#2b3a5c}}
.about{{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center}} .badges{{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}} .badges span{{background:{CREAM};color:{NAVY};padding:9px 16px;border-radius:99px;font-size:13px;font-weight:600}}
footer{{background:{NAVY};color:{CREAM};padding:0 0 40px}} footer .cta{{text-align:center;padding:80px 56px 40px}} footer h2{{color:{WHITE};font-size:48px}} footer small{{display:block;text-align:center;opacity:.7;margin-top:36px;font-size:12px}}
@media(max-width:900px){{header nav,.moon{{display:none}} .hero h1{{font-size:40px}} .door,.about{{grid-template-columns:1fr}} .terrace,.walk,.vals,.who{{grid-template-columns:1fr 1fr}} section{{padding:64px 22px}}}}
'''
body=f'''<header>{lockup(CREAM,42)}<nav>{navlinks()}</nav><a class="btn" href="#contact" style="padding:10px 20px">Talk to us</a></header>
<div class="hero"><div class="moon"></div><div class="kicker" style="color:{CREAM};opacity:.8">UK Housing Software</div>
<h1>Every home on the street, <em>seen clearly and cared for.</em></h1><p>{HERO_SUB}</p>
<a class="btn" href="#resonest">Walk down the street</a> &nbsp; <a class="btn ghost" href="#contact">Talk to us</a>
<div class="legend"><span><i style="background:{WARM}"></i>Homes that need help first</span><span><i style="background:{COOL}"></i>Homes to keep an eye on</span><span><i style="background:{CREAM};opacity:.5"></i>Homes doing well</span></div>
{street()}</div><div class="road"></div>
<section class="white" id="resonest"><div class="wrap"><div class="kicker">Our street, house by house</div><h2>Software that helps housing teams care for homes and communities</h2>
<p class="lead">We design around how your organisation works. Resonest and SiteOps sit at the centre, with building-safety reporting, a field app, property data, integrations and bespoke software around them.</p>
<div class="door" style="margin-top:48px">{house("No. 1")}<div><div class="kicker">Built for Awaab's Law</div><h3>Resonest</h3><p>{RESO_LEAD}</p><p>Picture every home on your street lit up: warm where help is needed first, calm where all is well.</p></div>{ul(RESO)}</div>
<div class="door" id="siteops">{house("No. 2",CREAM,CREAM)}<div><div class="kicker">Housing compliance</div><h3>SiteOps</h3><p>{SITE_LEAD}</p><p class="note">{SITE_ROAD}</p></div>{ul(SITE)}</div></div></section>
<section class="cream" id="capabilities"><div class="wrap"><div class="kicker">Next door</div><h2>The rest of the terrace</h2><p class="lead">Five supporting capabilities that sit around Resonest and SiteOps, each one a home on the same street.</p>
<div class="terrace">{"".join(f'<div class="h"><b>NO. {i+3}</b><h4>{t}</h4><p>{d}</p></div>' for i,(t,d) in enumerate(CAPS))}</div></div></section>
<section class="white" id="how"><div class="wrap"><div class="kicker">How we work</div><h2>A walk we take together</h2><p class="lead">Every engagement follows a simple, transparent path, so you always know where things stand and what comes next.</p>
<div class="walk">{"".join(f'<div><span>{i+1}</span><h4>{t}</h4><p>{d}</p></div>' for i,(t,d) in enumerate(STEPS))}</div></div></section>
<section class="cream"><div class="wrap"><div class="kicker">What we value</div><h2>Good neighbours first</h2><div class="vals">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in VALUES)}</div></div></section>
<section class="white" id="who"><div class="wrap"><div class="kicker">Who we help</div><h2>Built for UK housing organisations</h2><p class="lead">We work with social landlords, council housing teams, residential landlords and building safety consultancies that want their homes, data and teams to work better together.</p>
<div class="who">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in SECTORS)}</div></div></section>
<section class="cream" id="about"><div class="wrap about"><div><div class="kicker">About</div><h2>Big aspirations for UK housing</h2><p class="lead">{ABOUT1}</p><p class="lead">{ABOUT2}</p><div class="badges" style="">{"".join(f"<span style='background:#fff'>{b}</span>" for b in BADGES)}</div></div>
<div style="background:{NAVY};border-radius:20px;padding:30px 20px 0;overflow:hidden">{street(6,700,260,(1,4),(2,),seed=8)}</div></div></section>
<footer id="contact"><div class="cta"><div class="kicker" style="color:{CREAM}">Contact</div><h2>What could work better for your homes?</h2><p class="lead" style="color:{CREAM};margin:0 auto 30px">Tell us about your homes, your teams and your plans. We would love to explore what we could build together.</p><a class="btn" href="mailto:{EMAIL}">Email {EMAIL}</a></div>
{street(14,1440,200,(3,10),(6,12),seed=5)}<small>{FOOT}</small></footer>'''
import pathlib; p=pathlib.Path("the-street"); p.mkdir(exist_ok=True); (p/"index.html").write_text(page("Watson Atlas · The Street (draft)",css,body))
