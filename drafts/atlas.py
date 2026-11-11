from content import *
import math, random
def contours(w,h,col,n=14,seed=2,op=.35,cx=.7,cy=.45):
    r=random.Random(seed); out=[]
    for k in range(1,n+1):
        R=k*w/(n*1.6); pts=[]
        ph=[r.uniform(0,6.28) for _ in range(3)]
        for t in range(0,73):
            a=t/72*2*math.pi
            rr=R*(1+.12*math.sin(3*a+ph[0])+.07*math.sin(5*a+ph[1])+.05*math.sin(2*a+ph[2]))
            pts.append(f"{w*cx+rr*math.cos(a):.0f},{h*cy+rr*.62*math.sin(a):.0f}")
        out.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="{1.6 if k%4==0 else .8}" opacity="{op}"/>')
    grid="".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{col}" stroke-width=".6" opacity=".18"/>' for x in range(0,w,120))+"".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{col}" stroke-width=".6" opacity=".18"/>' for y in range(0,h,120))
    return f'<svg class="topo" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">{grid}{"".join(out)}</svg>'
SYM={"reso":'<circle cx="16" cy="16" r="12" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="16" cy="16" r="5" fill="currentColor"/>',
"site":'<rect x="5" y="5" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 16l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2"/>',
"tri":'<polygon points="16,4 28,27 4,27" fill="none" stroke="currentColor" stroke-width="2"/>'}
def sym(k): return f'<svg width="32" height="32" viewBox="0 0 32 32">{SYM[k]}</svg>'
css=f'''
body{{background:{CREAM};color:{NAVY}}}
.topo{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}
header{{display:flex;justify-content:space-between;align-items:center;padding:20px 56px;position:relative;z-index:2;color:{CREAM};background:{NAVY}}}
header nav{{display:flex;gap:26px;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase}} header nav a{{text-decoration:none}}
.coord{{font-size:11px;letter-spacing:.24em;font-weight:600;text-transform:uppercase;opacity:.75}}
.hero{{position:relative;background:{NAVY};color:{CREAM};padding:110px 56px 120px;overflow:hidden;min-height:760px}}
.hero h1{{position:relative;font-size:118px;line-height:.92;margin:26px 0 30px;font-weight:800;letter-spacing:-.04em;max-width:1000px;color:{WHITE}}}
.hero h1 span{{color:{CREAM};font-weight:300}}
.hero p{{position:relative;max-width:600px;font-size:18px;line-height:1.65}}
.compass{{position:absolute;right:90px;bottom:90px;text-align:center;font-weight:700;font-size:13px;letter-spacing:.2em}}
.scale{{position:relative;display:flex;align-items:center;gap:14px;margin-top:40px;font-size:11px;letter-spacing:.2em}} .scale i{{display:block;width:240px;height:8px;border:1.5px solid {CREAM};background:linear-gradient(90deg,{CREAM} 0 25%,transparent 25% 50%,{CREAM} 50% 75%,transparent 75%)}}
.btn{{display:inline-block;padding:15px 28px;border:1.5px solid currentColor;font-weight:700;text-decoration:none;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-top:30px;position:relative}} .btn.f{{background:{CREAM};color:{NAVY};border-color:{CREAM}}}
section{{position:relative;padding:100px 56px;overflow:hidden}} .wrap{{max-width:1240px;margin:0 auto;position:relative}}
.sheet{{display:flex;justify-content:space-between;border-bottom:1.5px solid {NAVY};padding-bottom:12px;margin-bottom:40px}}
h2{{font-size:56px;line-height:1;margin:0 0 20px;font-weight:800;letter-spacing:-.03em;max-width:900px}}
.lead{{font-size:17px;line-height:1.65;max-width:720px;color:#24365f}}
.panels{{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1.5px solid {NAVY};background:{WHITE}}}
.panel{{padding:40px}} .panel+.panel{{border-left:1.5px solid {NAVY}}}
.panel .hd{{display:flex;gap:14px;align-items:center}} .panel h3{{font-size:36px;margin:0;letter-spacing:-.02em}}
.panel ul{{padding-left:18px;line-height:1.7;color:#24365f;font-size:15px}} .panel p{{line-height:1.65;color:#24365f}}
.key{{font-size:11px;letter-spacing:.2em;font-weight:700;text-transform:uppercase;margin:18px 0 6px}}
.legend{{display:grid;grid-template-columns:repeat(5,1fr);border:1.5px solid {NAVY};border-top:0;background:{CREAM}}}
.legend div{{padding:26px 22px}} .legend div+div{{border-left:1.5px solid {NAVY}}} .legend h4{{margin:10px 0 8px;font-size:16px}} .legend p{{margin:0;font-size:13.5px;line-height:1.6;color:#24365f}}
.route{{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:30px}} .route div{{padding:0 22px 0 0}} .route .pin{{display:flex;align-items:center;gap:0;margin-bottom:16px}} .route .pin b{{width:34px;height:34px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:{NAVY};display:grid;place-items:center}} .route .pin b span{{transform:rotate(45deg);color:{CREAM};font-size:13px}} .route .pin i{{flex:1;height:2px;background:{NAVY};margin-left:8px}}
.route h4{{margin:0 0 6px;font-size:17px}} .route p{{margin:0;font-size:14px;line-height:1.6;color:#24365f}}
.dark{{background:{NAVY};color:{CREAM}}} .dark .lead,.dark p{{color:#dfe5f1}} .dark .sheet{{border-color:{CREAM}}}
.vals{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1.5px solid {CREAM}}} .vals div{{padding:30px}} .vals div+div{{border-left:1.5px solid {CREAM}}} .vals h4{{margin:12px 0 8px;font-size:20px;color:{WHITE}}} .vals p{{font-size:14px;line-height:1.6;margin:0}}
.regions{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}} .regions div{{background:{WHITE};padding:24px;border-left:4px solid {NAVY}}} .regions h4{{margin:0 0 8px}} .regions p{{margin:0;font-size:13.5px;line-height:1.6;color:#24365f}}
.about{{display:grid;grid-template-columns:1fr 1fr;gap:60px}} .badges span{{display:inline-block;border:1.5px solid {NAVY};padding:8px 14px;margin:0 8px 8px 0;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}}
footer{{position:relative;background:{NAVY};color:{CREAM};padding:110px 56px 40px;overflow:hidden}} footer h2{{color:{WHITE};font-size:76px}} footer small{{display:block;margin-top:80px;opacity:.7;position:relative}}
@media(max-width:900px){{header nav,header .coord{{display:none}} .hero h1{{font-size:56px}} .panels,.about{{grid-template-columns:1fr}} .panel+.panel{{border-left:0;border-top:1.5px solid {NAVY}}} .legend,.route,.vals,.regions{{grid-template-columns:1fr 1fr}} section{{padding:64px 22px}} .compass{{display:none}}}}
'''
def sheet(a,b): return f'<div class="sheet"><span class="coord">{a}</span><span class="coord">{b}</span></div>'
compass=f'<div class="compass">N<br><svg width="90" height="90" viewBox="-45 -45 90 90"><circle r="40" fill="none" stroke="{CREAM}" stroke-width="1.5"/><polygon points="0,-38 8,0 0,8 -8,0" fill="{CREAM}"/><polygon points="0,38 8,0 0,-8 -8,0" fill="none" stroke="{CREAM}"/></svg></div>'
body=f'''<header>{lockup(CREAM,42)}<nav>{navlinks()}</nav><span class="coord">Every home, one clear view</span></header>
<div class="hero">{contours(1440,800,CREAM)}<div class="coord" style="position:relative">Sheet 01 &nbsp;·&nbsp; UK Housing Software</div>
<h1>Mapping a better <span>tomorrow</span> for every home.</h1><p>{HERO_SUB}</p>
<a class="btn f" href="#resonest">Open the map</a> &nbsp; <a class="btn" href="#contact">Plan a route with us</a>
<div class="scale"><i></i><span>Scale: one home at a time</span></div>{compass}</div>
<section id="resonest">{contours(1440,1100,NAVY,10,5,.12,.15,.3)}<div class="wrap">{sheet("Sheet 02 · What we do","Key landmarks")}
<h2>Software that helps housing teams care for homes and communities</h2><p class="lead">We design around how your organisation works. Resonest and SiteOps sit at the centre, with building-safety reporting, a field app, property data, integrations and bespoke software around them.</p><br><br>
<div class="panels"><div class="panel"><div class="hd">{sym("reso")}<h3>Resonest</h3></div><div class="key">Built for Awaab's Law</div><p>{RESO_LEAD}</p>{ul(RESO)}</div>
<div class="panel" id="siteops"><div class="hd">{sym("site")}<h3>SiteOps</h3></div><div class="key">Housing compliance</div><p>{SITE_LEAD}</p>{ul(SITE)}<p class="key" style="letter-spacing:.06em;text-transform:none">{SITE_ROAD}</p></div></div>
<div class="legend" id="capabilities">{"".join(f'<div>{sym("tri")}<h4>{t}</h4><p>{d}</p></div>' for t,d in CAPS)}</div></div></section>
<section style="background:{WHITE}" id="how"><div class="wrap">{sheet("Sheet 03 · How we work","Our route together")}<h2>A clear route, shared goals, lasting partnerships</h2><p class="lead">Every engagement follows a simple, transparent path, so you always know where things stand and what comes next.</p>
<div class="route">{"".join(f'<div><div class="pin"><b><span>{i+1}</span></b><i></i></div><h4>{t}</h4><p>{d}</p></div>' for i,(t,d) in enumerate(STEPS))}</div></div></section>
<section class="dark">{contours(1440,700,CREAM,9,9,.2,.85,.6)}<div class="wrap">{sheet("Sheet 04 · What we value","True north")}<h2 style="color:{WHITE}">Our compass points</h2><div class="vals">{"".join(f'<div><span class="coord">{d}</span><h4>{t}</h4><p>{x}</p></div>' for d,(t,x) in zip(["North","East","South","West"],VALUES))}</div></div></section>
<section id="who"><div class="wrap">{sheet("Sheet 05 · Who we help","Across the UK")}<h2>Built for UK housing organisations</h2><p class="lead">We work with social landlords, council housing teams, residential landlords and building safety consultancies that want their homes, data and teams to work better together.</p><br><br>
<div class="regions">{"".join(f'<div><h4>{t}</h4><p>{d}</p></div>' for t,d in SECTORS)}</div></div></section>
<section style="background:{WHITE}" id="about"><div class="wrap">{sheet("Sheet 06 · About","Origin")}<div class="about"><div><h2>Big aspirations for UK housing</h2></div><div><p class="lead">{ABOUT1}</p><p class="lead">{ABOUT2}</p><div class="badges">{"".join(f"<span>{b}</span>" for b in BADGES)}</div></div></div></div></section>
<footer id="contact">{contours(1440,700,CREAM,12,4,.25,.5,.9)}<div class="wrap">{sheet("Sheet 07 · Contact","Your next destination")}<h2>What could work better for your homes?</h2><p class="lead" style="position:relative">Tell us about your homes, your teams and your plans. We would love to explore what we could build together.</p><a class="btn f" href="mailto:{EMAIL}">Email {EMAIL}</a>
<small>{FOOT}</small></div></footer>'''
import pathlib; p=pathlib.Path("the-atlas"); p.mkdir(exist_ok=True); (p/"index.html").write_text(page("Watson Atlas · The Atlas (draft)",css,body))
