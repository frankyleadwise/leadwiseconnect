import os

BASE_CSS = open('_base.css').read()
NAV_HTML = open('_nav.html').read()
FOOTER_HTML = open('_footer.html').read()
SCRIPTS_JS = open('_scripts.js').read()

def page(title, desc, canonical, body, extra_css='', robots='index, follow'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="https://leadwiseconnect.com{canonical}"/>
<meta name="robots" content="{robots}"/>
<link rel="canonical" href="https://leadwiseconnect.com{canonical}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<style>
{BASE_CSS}
{extra_css}
</style>
</head>
<body>
{NAV_HTML}
{body}
{FOOTER_HTML}
<script>{SCRIPTS_JS}</script>
</body>
</html>"""

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w') as f:
        f.write(content)
    print(f"  wrote {path}")

# ─── CHECK ICON ───
CHECK = '<svg width="14" height="14" fill="currentColor" viewBox="0 0 16 16" style="flex-shrink:0;margin-top:.15rem"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"/></svg>'

MARQUEE = """<div class="marquee-wrap">
  <div class="marquee-track">
    <span class="marquee-item">HVAC Companies<span class="mdot"></span></span><span class="marquee-item">Plumbers<span class="mdot"></span></span><span class="marquee-item">Roofers<span class="mdot"></span></span><span class="marquee-item">Electricians<span class="mdot"></span></span><span class="marquee-item">Landscapers<span class="mdot"></span></span><span class="marquee-item">General Contractors<span class="mdot"></span></span><span class="marquee-item">Pest Control<span class="mdot"></span></span><span class="marquee-item">Pool Services<span class="mdot"></span></span><span class="marquee-item">Painters<span class="mdot"></span></span><span class="marquee-item">Garage Door<span class="mdot"></span></span><span class="marquee-item">Concrete &amp; Paving<span class="mdot"></span></span><span class="marquee-item">Cleaning Services<span class="mdot"></span></span><span class="marquee-item">HVAC Companies<span class="mdot"></span></span><span class="marquee-item">Plumbers<span class="mdot"></span></span><span class="marquee-item">Roofers<span class="mdot"></span></span><span class="marquee-item">Electricians<span class="mdot"></span></span><span class="marquee-item">Landscapers<span class="mdot"></span></span><span class="marquee-item">General Contractors<span class="mdot"></span></span><span class="marquee-item">Pest Control<span class="mdot"></span></span><span class="marquee-item">Pool Services<span class="mdot"></span></span><span class="marquee-item">Painters<span class="mdot"></span></span><span class="marquee-item">Garage Door<span class="mdot"></span></span><span class="marquee-item">Concrete &amp; Paving<span class="mdot"></span></span><span class="marquee-item">Cleaning Services<span class="mdot"></span></span>
  </div>
</div>"""

# ─── HOMEPAGE ───
homepage = page(
    "LeadWise Connect | Marketing Agency for Local Service Contractors",
    "We build SEO-optimized websites, AI voice agents, and lead generation systems for HVAC, plumbing, roofing, and electrical contractors. Tampa, FL — serving the US.",
    "/",
    f"""
<section style="min-height:100dvh;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden;padding:8rem 2rem 6rem">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 50% at 50% -10%,rgba(232,160,32,.14) 0%,transparent 70%);pointer-events:none"></div>
  <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.02) 1px,transparent 1px);background-size:80px 80px;pointer-events:none"></div>
  <div class="container" style="position:relative;z-index:1">
    <div class="fadein" style="display:inline-flex;align-items:center;gap:.5rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.2);border-radius:9999px;padding:.35rem .85rem .35rem .5rem;margin-bottom:2rem">
      <span style="width:6px;height:6px;border-radius:50%;background:#E8A020;animation:pulse-gold 2s ease-in-out infinite"></span>
      <span style="font-size:.7rem;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:#E8A020">Tampa, FL — Serving Contractors Nationwide</span>
    </div>
    <h1 class="serif fadein d1" style="font-size:clamp(3rem,7vw,6.5rem);line-height:1;letter-spacing:-.02em;color:var(--text);max-width:900px;margin-bottom:2rem">
      Your competitors are<br>
      <span style="background:linear-gradient(135deg,#F5C060 0%,#E8A020 50%,#B87818 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">losing leads</span> you<br>
      could be closing.
    </h1>
    <p class="fadein d2" style="font-size:clamp(1rem,2vw,1.2rem);color:var(--text2);max-width:540px;line-height:1.7;margin-bottom:2.5rem">We build SEO-optimized websites, AI automation, and lead systems for local service contractors — engineered to rank, convert, and scale.</p>
    <div class="fadein d3" style="display:flex;flex-wrap:wrap;gap:1rem;margin-bottom:4rem">
      <a href="/contact.html" class="btn-gold" style="font-size:1rem;padding:1rem 2rem">Get Your Free Audit <span class="icon-wrap">↗</span></a>
      <a href="/results.html" class="btn-ghost" style="font-size:1rem;padding:1rem 2rem">See Our Work</a>
    </div>
    <div class="fadein d4" style="display:flex;flex-wrap:wrap;gap:1.5rem">
      <span style="display:flex;align-items:center;gap:.5rem;color:var(--text2);font-size:.85rem">{CHECK} No contracts — results or you walk</span>
      <span style="display:flex;align-items:center;gap:.5rem;color:var(--text2);font-size:.85rem">{CHECK} Free website audit included</span>
      <span style="display:flex;align-items:center;gap:.5rem;color:var(--text2);font-size:.85rem">{CHECK} Built on proven SEO architecture</span>
    </div>
  </div>
</section>

{MARQUEE}

<section class="sec">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">What We Build</span>
      <h2 class="serif" style="font-size:clamp(2rem,4vw,3.5rem);color:var(--text);max-width:600px;margin-bottom:4rem">The full-stack growth system for contractors</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.25rem">
      <a href="/services/smart-websites.html" style="display:block;text-decoration:none">
        <div class="reveal svc-card-home" style="background:rgba(17,17,17,.8);border:1px solid rgba(255,255,255,.06);border-radius:1.5rem;padding:2rem;display:flex;flex-direction:column;gap:1rem;height:100%;transition:all .4s cubic-bezier(.22,1,.36,1)">
          <div style="display:flex;align-items:flex-start;justify-content:space-between">
            <div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div>
            <span style="font-size:.65rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.2);border-radius:9999px;padding:.25rem .65rem">Most Popular</span>
          </div>
          <h3 style="font-size:1.2rem;font-weight:600;color:var(--text);letter-spacing:-.01em">Smart Contractor Websites</h3>
          <p style="font-size:.9rem;color:var(--text2);line-height:1.7;flex:1">SEO-first, conversion-optimized websites built to rank on Google and turn visitors into booked jobs. AI chat and voice widgets included.</p>
          <span style="color:var(--gold);font-size:.85rem;font-weight:500">Learn more →</span>
        </div>
      </a>
      <a href="/services/ai-voice-agents.html" style="display:block;text-decoration:none">
        <div class="reveal svc-card-home" style="background:rgba(17,17,17,.8);border:1px solid rgba(255,255,255,.06);border-radius:1.5rem;padding:2rem;display:flex;flex-direction:column;gap:1rem;height:100%;transition:all .4s cubic-bezier(.22,1,.36,1)">
          <div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h.01M15 9h.01M9 15a3 3 0 0 0 6 0"/></svg></div>
          <h3 style="font-size:1.2rem;font-weight:600;color:var(--text);letter-spacing:-.01em">AI Voice Agents</h3>
          <p style="font-size:.9rem;color:var(--text2);line-height:1.7;flex:1">Never miss a lead again. Our AI voice agents answer calls 24/7, qualify leads, and book appointments automatically.</p>
          <span style="color:var(--gold);font-size:.85rem;font-weight:500">Learn more →</span>
        </div>
      </a>
      <a href="/services/lead-generation.html" style="display:block;text-decoration:none">
        <div class="reveal svc-card-home" style="background:rgba(17,17,17,.8);border:1px solid rgba(255,255,255,.06);border-radius:1.5rem;padding:2rem;display:flex;flex-direction:column;gap:1rem;height:100%;transition:all .4s cubic-bezier(.22,1,.36,1)">
          <div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg></div>
          <h3 style="font-size:1.2rem;font-weight:600;color:var(--text);letter-spacing:-.01em">Lead Generation</h3>
          <p style="font-size:.9rem;color:var(--text2);line-height:1.7;flex:1">Google Ads, Local Services Ads, and social campaigns engineered for contractors. We run what converts — not what looks good in a report.</p>
          <span style="color:var(--gold);font-size:.85rem;font-weight:500">Learn more →</span>
        </div>
      </a>
      <a href="/services/crm-automation.html" style="display:block;text-decoration:none">
        <div class="reveal svc-card-home" style="background:rgba(17,17,17,.8);border:1px solid rgba(255,255,255,.06);border-radius:1.5rem;padding:2rem;display:flex;flex-direction:column;gap:1rem;height:100%;transition:all .4s cubic-bezier(.22,1,.36,1)">
          <div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg></div>
          <h3 style="font-size:1.2rem;font-weight:600;color:var(--text);letter-spacing:-.01em">CRM &amp; Automation</h3>
          <p style="font-size:.9rem;color:var(--text2);line-height:1.7;flex:1">GHL-powered pipeline management, automated follow-up sequences, and review generation — all integrated into your workflow.</p>
          <span style="color:var(--gold);font-size:.85rem;font-weight:500">Learn more →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="sec" style="background:rgba(232,160,32,.03);border-top:1px solid rgba(232,160,32,.08);border-bottom:1px solid rgba(232,160,32,.08)">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">Proof of Work</span>
      <h2 class="serif" style="font-size:clamp(2rem,4vw,3.5rem);color:var(--text);margin-bottom:1rem">Real results. Real contractors.</h2>
      <p style="color:var(--text2);font-size:1rem;margin-bottom:4rem;max-width:500px">Our first client, North East Heating &amp; Cooling, is a blueprint for what we do for every contractor we partner with.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.5rem;margin-bottom:3rem">
      <div class="reveal card"><div style="font-size:clamp(2.5rem,5vw,3.5rem);font-weight:800;color:var(--gold);line-height:1;margin-bottom:.5rem;letter-spacing:-.03em">34</div><div style="font-weight:600;color:var(--text);font-size:1rem;margin-bottom:.35rem">Google Reviews</div><div style="font-size:.8rem;color:var(--text2);margin-bottom:1rem">Up from 10 in 6 months</div><div style="font-size:.7rem;color:var(--text3);font-weight:500;letter-spacing:.05em;text-transform:uppercase">North East Heating &amp; Cooling</div></div>
      <div class="reveal card"><div style="font-size:clamp(2.5rem,5vw,3.5rem);font-weight:800;color:var(--gold);line-height:1;margin-bottom:.5rem;letter-spacing:-.03em">5.0</div><div style="font-weight:600;color:var(--text);font-size:1rem;margin-bottom:.35rem">Star Rating</div><div style="font-size:.8rem;color:var(--text2);margin-bottom:1rem">Maintained throughout growth</div><div style="font-size:.7rem;color:var(--text3);font-weight:500;letter-spacing:.05em;text-transform:uppercase">North East Heating &amp; Cooling</div></div>
      <div class="reveal card"><div style="font-size:clamp(2.5rem,5vw,3.5rem);font-weight:800;color:var(--gold);line-height:1;margin-bottom:.5rem;letter-spacing:-.03em">20+</div><div style="font-weight:600;color:var(--text);font-size:1rem;margin-bottom:.35rem">Location Pages</div><div style="font-size:.8rem;color:var(--text2);margin-bottom:1rem">Ranking across Tampa Bay</div><div style="font-size:.7rem;color:var(--text3);font-weight:500;letter-spacing:.05em;text-transform:uppercase">North East Heating &amp; Cooling</div></div>
    </div>
    <div class="reveal card" style="border-color:rgba(232,160,32,.15);display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:2rem;padding:2.5rem">
      <div><p style="font-size:.8rem;color:var(--text2);margin-bottom:.5rem">Live client example</p><h3 style="font-size:1.3rem;font-weight:700;color:var(--text);margin-bottom:.35rem">North East Heating &amp; Cooling</h3><p style="color:var(--text3);font-size:.875rem">Tampa Bay HVAC — Full website + SEO + Review automation</p></div>
      <a href="https://northeastheatingcooling.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-ghost" style="font-size:.9rem">View live site ↗</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">The Process</span>
      <h2 class="serif" style="font-size:clamp(2rem,4vw,3.5rem);color:var(--text);max-width:600px;margin-bottom:5rem">From invisible to in-demand — in 30 days</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;background:rgba(255,255,255,.05);border-radius:1.5rem;overflow:hidden">
      <div class="reveal" style="background:#0D0D0D;padding:2.5rem 2rem"><div style="font-size:2.5rem;font-weight:800;color:rgba(232,160,32,.2);letter-spacing:-.05em;margin-bottom:1.5rem;line-height:1">01</div><h3 style="font-size:1.2rem;font-weight:600;color:var(--text);margin-bottom:.75rem">Free Audit</h3><p style="font-size:.9rem;color:var(--text2);line-height:1.7">We analyze your digital presence, competitors, and keyword opportunities. No pitch — just data.</p></div>
      <div class="reveal" style="background:#0D0D0D;padding:2.5rem 2rem"><div style="font-size:2.5rem;font-weight:800;color:rgba(232,160,32,.2);letter-spacing:-.05em;margin-bottom:1.5rem;line-height:1">02</div><h3 style="font-size:1.2rem;font-weight:600;color:var(--text);margin-bottom:.75rem">Strategy Call</h3><p style="font-size:.9rem;color:var(--text2);line-height:1.7">We present a custom growth roadmap: what pages to build, what keywords to target, what to automate.</p></div>
      <div class="reveal" style="background:#0D0D0D;padding:2.5rem 2rem"><div style="font-size:2.5rem;font-weight:800;color:rgba(232,160,32,.2);letter-spacing:-.05em;margin-bottom:1.5rem;line-height:1">03</div><h3 style="font-size:1.2rem;font-weight:600;color:var(--text);margin-bottom:.75rem">We Build</h3><p style="font-size:.9rem;color:var(--text2);line-height:1.7">Our team builds your SEO-optimized site, sets up AI voice agents, and configures your lead pipeline.</p></div>
      <div class="reveal" style="background:#0D0D0D;padding:2.5rem 2rem"><div style="font-size:2.5rem;font-weight:800;color:rgba(232,160,32,.2);letter-spacing:-.05em;margin-bottom:1.5rem;line-height:1">04</div><h3 style="font-size:1.2rem;font-weight:600;color:var(--text);margin-bottom:.75rem">Leads Flow</h3><p style="font-size:.9rem;color:var(--text2);line-height:1.7">Your site starts ranking. Your phone starts ringing. Your AI answers 24/7. You focus on the work.</p></div>
    </div>
  </div>
</section>

<section class="sec" style="text-align:center;background:#0D0D0D;border-top:1px solid rgba(255,255,255,.04)">
  <div style="max-width:680px;margin:0 auto" class="reveal">
    <span class="eyebrow" style="display:block;text-align:center">Stop losing to your competitors</span>
    <h2 class="serif" style="font-size:clamp(2.5rem,5vw,4.5rem);color:var(--text);margin-bottom:1.5rem;line-height:1.05;letter-spacing:-.02em">Get a free audit of your digital presence</h2>
    <p style="color:var(--text2);font-size:1.1rem;margin-bottom:2.5rem;line-height:1.7">We'll show you exactly what's costing you leads — and what it would take to fix it. No obligation. No pitch.</p>
    <a href="/contact.html" class="btn-gold" style="font-size:1.1rem;padding:1.1rem 2.5rem">Claim Your Free Audit <span class="icon-wrap">↗</span></a>
    <p style="color:var(--text3);font-size:.8rem;margin-top:1.25rem">Takes 2 minutes to request. We respond within 24 hours.</p>
  </div>
</section>
""",
    extra_css=".svc-card-home:hover{border-color:rgba(232,160,32,.25)!important;background:rgba(232,160,32,.05)!important;transform:translateY(-3px)}"
)
write("index.html", homepage)

# ─── CONTACT PAGE ───
contact_page = page(
    "Get Your Free Audit | Contact LeadWise Connect",
    "Request a free digital marketing audit for your contracting business. We analyze your website, local SEO, and lead flow — no obligation.",
    "/contact.html",
    f"""
<section class="page-hero" style="background:radial-gradient(ellipse 50% 40% at 30% 50%,rgba(232,160,32,.07) 0%,transparent 70%)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:start" class="contact-outer">
      <div class="reveal">
        <span class="eyebrow">Free. No Obligation.</span>
        <h1 class="serif">Let's see what's costing you leads.</h1>
        <p style="color:var(--text2);line-height:1.8;font-size:1rem;margin:1.5rem 0 3rem">We'll do a complete audit of your website, Google Business Profile, local SEO rankings, and competitors — then walk you through exactly what's holding you back. No pitch. No pressure.</p>
        <div style="display:flex;flex-direction:column;gap:1.5rem">
          <div style="display:flex;gap:1rem"><div style="width:2px;background:rgba(232,160,32,.3);border-radius:9999px;flex-shrink:0"></div><div><p style="font-weight:600;color:var(--text);margin-bottom:.25rem;font-size:.95rem">Website &amp; SEO Audit</p><p style="color:var(--text2);font-size:.875rem;line-height:1.6">We grade your current site on speed, structure, and keyword targeting.</p></div></div>
          <div style="display:flex;gap:1rem"><div style="width:2px;background:rgba(232,160,32,.3);border-radius:9999px;flex-shrink:0"></div><div><p style="font-weight:600;color:var(--text);margin-bottom:.25rem;font-size:.95rem">Competitor Analysis</p><p style="color:var(--text2);font-size:.875rem;line-height:1.6">See exactly how your top 3 local competitors are outranking you — and why.</p></div></div>
          <div style="display:flex;gap:1rem"><div style="width:2px;background:rgba(232,160,32,.3);border-radius:9999px;flex-shrink:0"></div><div><p style="font-weight:600;color:var(--text);margin-bottom:.25rem;font-size:.95rem">Lead Flow Review</p><p style="color:var(--text2);font-size:.875rem;line-height:1.6">We map where leads are dropping and what automation would fix it.</p></div></div>
        </div>
      </div>
      <div class="reveal">
        <div id="form-card" class="card">
          <h2 style="font-size:1.3rem;font-weight:700;color:var(--text);margin-bottom:.5rem">Request Your Free Audit</h2>
          <p style="color:var(--text2);font-size:.875rem;margin-bottom:2rem">We respond within 24 hours, usually much faster.</p>
          <form id="audit-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem">
              <div class="fg"><label>First Name</label><input type="text" name="first_name" placeholder="Chris" required/></div>
              <div class="fg"><label>Last Name</label><input type="text" name="last_name" placeholder="Grullon" required/></div>
            </div>
            <div class="fg"><label>Business Name</label><input type="text" name="business" placeholder="North East Heating &amp; Cooling" required/></div>
            <div class="fg"><label>Phone Number</label><input type="tel" name="phone" placeholder="(813) 555-0100" required/></div>
            <div class="fg"><label>Email</label><input type="email" name="email" placeholder="you@yourcompany.com" required/></div>
            <div class="fg"><label>Trade / Service Type</label><select name="trade" required><option value="" disabled selected>Select your trade...</option><option>HVAC</option><option>Plumbing</option><option>Roofing</option><option>Electrical</option><option>Landscaping</option><option>Pest Control</option><option>General Contractor</option><option>Other</option></select></div>
            <div class="fg"><label>Current Website (if any)</label><input type="url" name="website" placeholder="https://yoursite.com"/></div>
            <div class="fg"><label>Biggest challenge right now</label><textarea name="challenge" rows="3" placeholder="Not enough calls, hard to rank on Google, missing leads after hours..."></textarea></div>
            <button type="submit" class="btn-gold" style="width:100%;justify-content:center;font-size:1rem;padding:1rem;margin-bottom:.75rem">Get My Free Audit <span class="icon-wrap">↗</span></button>
            <p style="font-size:.75rem;color:var(--text3);text-align:center;line-height:1.6">No spam. No obligations. Your info is never shared.</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
""",
    extra_css="@media(max-width:900px){.contact-outer{grid-template-columns:1fr!important;gap:3rem!important}} @media(max-width:600px){form [style*='grid-template-columns:1fr 1fr']{grid-template-columns:1fr!important}}"
)
write("contact.html", contact_page)

# ─── RESULTS PAGE ───
results_page = page(
    "Results & Case Studies | LeadWise Connect",
    "Real contractor marketing results — websites, SEO rankings, review growth, and lead generation. See the LeadWise system in action.",
    "/results.html",
    f"""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow fadein">Proof of Work</span>
    <h1 class="serif fadein d1">Real contractors. Real growth.</h1>
    <p class="fadein d2">We are a focused agency with a clear, proven system. Here is exactly what we built, what changed, and what you can expect.</p>
  </div>
</section>
<section class="sec" style="padding-top:2rem">
  <div class="container">
    <div class="reveal" style="background:var(--surface);border:1px solid rgba(232,160,32,.15);border-radius:1.5rem;overflow:hidden">
      <div style="padding:3rem;border-bottom:1px solid rgba(255,255,255,.06);display:flex;flex-wrap:wrap;align-items:flex-start;justify-content:space-between;gap:2rem">
        <div>
          <span style="font-size:.65rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.2);border-radius:9999px;padding:.3rem .75rem;display:inline-block;margin-bottom:1rem">Case Study 001</span>
          <h2 style="font-size:2rem;font-weight:700;color:var(--text);letter-spacing:-.02em;margin-bottom:.5rem">North East Heating &amp; Cooling</h2>
          <p style="color:var(--text2);font-size:.95rem">HVAC Contractor — Tampa Bay, FL — Full digital build</p>
        </div>
        <a href="https://northeastheatingcooling.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-ghost">View live site ↗</a>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1px;background:rgba(255,255,255,.04)">
        <div style="background:var(--surface);padding:2rem"><p style="font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3);margin-bottom:1rem">Google Reviews</p><div style="display:flex;align-items:center;gap:.75rem"><span style="font-size:1.1rem;color:var(--text3);text-decoration:line-through">10</span><span style="color:var(--text3);font-size:.8rem">to</span><span style="font-size:1.75rem;font-weight:800;color:var(--gold)">34</span></div></div>
        <div style="background:var(--surface);padding:2rem"><p style="font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3);margin-bottom:1rem">SEO Pages Built</p><div style="display:flex;align-items:center;gap:.75rem"><span style="font-size:1.1rem;color:var(--text3);text-decoration:line-through">1</span><span style="color:var(--text3);font-size:.8rem">to</span><span style="font-size:1.75rem;font-weight:800;color:var(--gold)">30+</span></div></div>
        <div style="background:var(--surface);padding:2rem"><p style="font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3);margin-bottom:1rem">City Pages</p><div style="display:flex;align-items:center;gap:.75rem"><span style="font-size:1.1rem;color:var(--text3);text-decoration:line-through">0</span><span style="color:var(--text3);font-size:.8rem">to</span><span style="font-size:1.75rem;font-weight:800;color:var(--gold)">20+</span></div></div>
        <div style="background:var(--surface);padding:2rem"><p style="font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3);margin-bottom:1rem">Star Rating</p><div style="display:flex;align-items:center;gap:.75rem"><span style="font-size:1.1rem;color:var(--text3);text-decoration:line-through">4.2</span><span style="color:var(--text3);font-size:.8rem">to</span><span style="font-size:1.75rem;font-weight:800;color:var(--gold)">5.0</span></div></div>
      </div>
      <div style="padding:3rem;border-top:1px solid rgba(255,255,255,.06)">
        <h3 style="font-size:1.1rem;font-weight:700;color:var(--text);margin-bottom:1.75rem">What we delivered</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem">
          <div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:1rem;padding:1.5rem"><h4 style="font-weight:600;color:var(--text);margin-bottom:.5rem;font-size:.95rem">Full Next.js website</h4><p style="color:var(--text2);font-size:.85rem;line-height:1.7">Residential and commercial service pages with schema markup, Core Web Vitals tuned for speed.</p></div>
          <div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:1rem;padding:1.5rem"><h4 style="font-weight:600;color:var(--text);margin-bottom:.5rem;font-size:.95rem">20+ location pages</h4><p style="color:var(--text2);font-size:.85rem;line-height:1.7">City-specific pages covering every Tampa Bay suburb, each targeting local search intent.</p></div>
          <div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:1rem;padding:1.5rem"><h4 style="font-weight:600;color:var(--text);margin-bottom:.5rem;font-size:.95rem">Review automation</h4><p style="color:var(--text2);font-size:.85rem;line-height:1.7">Post-service review request sequence — 10 reviews to 34, a 240% increase in 6 months.</p></div>
          <div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.05);border-radius:1rem;padding:1.5rem"><h4 style="font-weight:600;color:var(--text);margin-bottom:.5rem;font-size:.95rem">Google Business Profile</h4><p style="color:var(--text2);font-size:.85rem;line-height:1.7">Fully optimized GBP with service areas, photos, and consistent post schedule.</p></div>
        </div>
      </div>
      <div style="padding:3rem;border-top:1px solid rgba(255,255,255,.06);background:rgba(232,160,32,.02)">
        <h3 style="font-size:1.1rem;font-weight:700;color:var(--text);margin-bottom:1.75rem">What customers are saying</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.25rem">
          <div class="card"><div style="color:var(--gold);font-size:.85rem;letter-spacing:2px;margin-bottom:1rem">★★★★★</div><p style="color:var(--text2);font-size:.875rem;line-height:1.7">"Called them for an emergency and their technician Christian showed up fast. Thorough, skilled, and truly professional."</p></div>
          <div class="card"><div style="color:var(--gold);font-size:.85rem;letter-spacing:2px;margin-bottom:1rem">★★★★★</div><p style="color:var(--text2);font-size:.875rem;line-height:1.7">"This is an amazing family company that truly cares about your home. Honest, reliable, and genuinely invested in doing right by their customers."</p></div>
          <div class="card"><div style="color:var(--gold);font-size:.85rem;letter-spacing:2px;margin-bottom:1rem">★★★★★</div><p style="color:var(--text2);font-size:.875rem;line-height:1.7">"Their work was outstanding — polished and professional. They left everything cleaner than they found it. Highly recommend."</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:4rem;text-align:center">
  <div style="max-width:580px;margin:0 auto" class="reveal">
    <h2 class="serif" style="font-size:2.5rem;color:var(--text);margin-bottom:1rem">Your business could be next</h2>
    <p style="color:var(--text2);margin-bottom:2rem;line-height:1.7">We are selectively onboarding contractor clients. If you are serious about growing your local business, start with a free audit.</p>
    <a href="/contact.html" class="btn-gold">Apply to Work With Us ↗</a>
  </div>
</section>
"""
)
write("results.html", results_page)

# ─── ABOUT PAGE ───
about_page = page(
    "About LeadWise Connect | Contractor Marketing Agency Tampa",
    "LeadWise Connect is a Tampa-based digital marketing agency built specifically for local service contractors. Our mission: help tradespeople compete online like the big guys.",
    "/about.html",
    f"""
<section class="page-hero" style="background:radial-gradient(ellipse 50% 40% at 70% 50%,rgba(232,160,32,.07) 0%,transparent 70%)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:center" class="about-outer">
      <div class="reveal">
        <span class="eyebrow">Our Story</span>
        <h1 class="serif">Built for the trades. Obsessed with local search.</h1>
        <p style="color:var(--text2);line-height:1.8;font-size:1rem;margin:1.75rem 0 1.5rem">LeadWise Connect was founded in Tampa, Florida with one belief: local service contractors deserve the same quality of digital marketing that big brands get — without the big agency runaround.</p>
        <p style="color:var(--text2);line-height:1.8;font-size:1rem;margin-bottom:2.5rem">Plumbers, HVAC techs, roofers, electricians — these are the people who keep homes running. They are skilled at their craft but often invisible online. We fix that.</p>
        <a href="/contact.html" class="btn-gold">Work with us <span class="icon-wrap">↗</span></a>
      </div>
      <div class="reveal">
        <div class="card" style="border-color:rgba(232,160,32,.12)">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem">
            <div><p style="font-size:2.25rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">1</p><p style="font-weight:600;color:var(--text);font-size:.9rem;margin-top:.35rem">Flagship client</p><p style="color:var(--text3);font-size:.75rem;margin-top:.2rem">North East HVAC, Tampa</p></div>
            <div><p style="font-size:2.25rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">34</p><p style="font-weight:600;color:var(--text);font-size:.9rem;margin-top:.35rem">Reviews generated</p><p style="color:var(--text3);font-size:.75rem;margin-top:.2rem">Up from 10</p></div>
            <div><p style="font-size:2.25rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">30+</p><p style="font-weight:600;color:var(--text);font-size:.9rem;margin-top:.35rem">SEO pages built</p><p style="color:var(--text3);font-size:.75rem;margin-top:.2rem">All ranking</p></div>
            <div><p style="font-size:2.25rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">100%</p><p style="font-weight:600;color:var(--text);font-size:.9rem;margin-top:.35rem">Satisfaction</p><p style="color:var(--text3);font-size:.75rem;margin-top:.2rem">Or we make it right</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="sec" style="background:#0D0D0D;border-top:1px solid rgba(255,255,255,.04)">
  <div class="container">
    <div class="reveal"><h2 class="serif" style="font-size:clamp(2rem,3vw,3rem);color:var(--text);margin-bottom:4rem;max-width:500px">How we think about this work</h2></div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem">
      <div class="reveal card"><div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.12);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div><h3 style="font-weight:600;color:var(--text);font-size:1.05rem;margin-bottom:.75rem">Local-first, always</h3><p style="color:var(--text2);font-size:.875rem;line-height:1.7">We do not chase national campaigns or SaaS clients. Every strategy is built around local search intent and what ranks in your specific market.</p></div>
      <div class="reveal card"><div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.12);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg></div><h3 style="font-weight:600;color:var(--text);font-size:1.05rem;margin-bottom:.75rem">Leads over vanity</h3><p style="color:var(--text2);font-size:.875rem;line-height:1.7">We do not celebrate page views or impressions. We track phone calls, form fills, and booked jobs. That is what pays your bills.</p></div>
      <div class="reveal card"><div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.12);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3 style="font-weight:600;color:var(--text);font-size:1.05rem;margin-bottom:.75rem">Lead by example</h3><p style="color:var(--text2);font-size:.875rem;line-height:1.7">Our own site is built to the same SEO standards we build for clients. If we would not do it here, we will not recommend it to you.</p></div>
      <div class="reveal card"><div style="width:2.75rem;height:2.75rem;border-radius:.75rem;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.12);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem;color:var(--gold)"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div><h3 style="font-weight:600;color:var(--text);font-size:1.05rem;margin-bottom:.75rem">Long-term partners</h3><p style="color:var(--text2);font-size:.875rem;line-height:1.7">We treat clients as partners. Your success is our portfolio. We have skin in the game every time your phone should be ringing.</p></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="container">
    <div class="reveal card-gold" style="padding:3rem;display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center" class="geo-outer">
      <div>
        <span class="eyebrow">Based in Tampa, FL</span>
        <h2 class="serif" style="font-size:2rem;color:var(--text);margin-bottom:1rem">Tampa roots. Nationwide reach.</h2>
        <p style="color:var(--text2);line-height:1.8;margin-bottom:1.5rem">We started in Tampa Bay and know the local contractor market inside and out. But our system works in any market across the US — same architecture, same SEO principles, same results.</p>
        <p style="color:var(--text2);line-height:1.8">Whether you are in Houston, Atlanta, Phoenix, or Charlotte — if you serve local customers, we can build you a machine that brings them in.</p>
      </div>
      <div class="pills"><span class="pill">Tampa, FL</span><span class="pill">Orlando, FL</span><span class="pill">Houston, TX</span><span class="pill">Dallas, TX</span><span class="pill">Atlanta, GA</span><span class="pill">Phoenix, AZ</span><span class="pill">Charlotte, NC</span><span class="pill">Denver, CO</span><span class="pill">Nashville, TN</span><span class="pill">Las Vegas, NV</span><span class="pill">And more...</span></div>
    </div>
  </div>
</section>
""",
    extra_css="@media(max-width:900px){.about-outer,.geo-outer{grid-template-columns:1fr!important;gap:3rem!important}}"
)
write("about.html", about_page)

print("Core pages done!")

# ─── SERVICES OVERVIEW ───
services_page = page(
    "Services | Contractor Marketing Agency | LeadWise Connect",
    "Premium websites, AI voice agents, lead generation, and CRM automation for local service contractors. See everything LeadWise Connect offers.",
    "/services.html",
    f"""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow fadein">What We Offer</span>
    <h1 class="serif fadein d1">Everything a contractor needs to dominate local search</h1>
    <p class="fadein d2">We don't do SEO for dentists or social media for restaurants. We do one thing: grow local service contractors — and we're obsessed at it.</p>
  </div>
</section>
<section class="sec" style="padding-top:2rem">
  <div class="container">
    <div style="display:flex;flex-direction:column;gap:3rem">
      <div class="reveal card" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start" class="svc-row">
        <div>
          <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem">
            <div style="width:3rem;height:3rem;border-radius:.875rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold)"><svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div>
            <span style="font-size:.65rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.2);border-radius:9999px;padding:.25rem .65rem">Most Popular</span>
          </div>
          <h2 style="font-size:1.6rem;font-weight:700;color:var(--text);margin-bottom:.5rem;letter-spacing:-.02em">Smart Websites for Contractors</h2>
          <p style="color:var(--gold);font-size:.9rem;font-weight:500;margin-bottom:1.25rem">Your #1 lead source — or we rebuild it.</p>
          <p style="color:var(--text2);line-height:1.8;margin-bottom:1.75rem;font-size:.95rem">Every site we build is architected from the ground up for Google rankings and phone call conversions. We create dedicated pages for every service and every city you serve, integrated with AI chat and voice widgets that qualify leads around the clock.</p>
          <a href="/services/smart-websites.html" class="btn-gold">Learn more <span class="icon-wrap">↗</span></a>
        </div>
        <div>
          <p style="font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--text3);margin-bottom:1.25rem">What's included</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
            {''.join(f'<div style="display:flex;align-items:flex-start;gap:.5rem">{CHECK}<span style="font-size:.85rem;color:var(--text2);line-height:1.4">{f}</span></div>' for f in ["SEO-optimized service pages","Location/city landing pages","AI chat widget (24/7)","AI voice widget (answers calls)","Google Business Profile optimization","Core Web Vitals optimized","Schema markup included","Monthly rank tracking"])}
          </div>
        </div>
      </div>
      <div class="reveal card" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start" class="svc-row">
        <div>
          <div style="width:3rem;height:3rem;border-radius:.875rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold);margin-bottom:1.5rem"><svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h.01M15 9h.01M9 15a3 3 0 0 0 6 0"/></svg></div>
          <h2 style="font-size:1.6rem;font-weight:700;color:var(--text);margin-bottom:.5rem;letter-spacing:-.02em">AI Voice Agents</h2>
          <p style="color:var(--gold);font-size:.9rem;font-weight:500;margin-bottom:1.25rem">Your best employee. Works 24/7. Never calls in sick.</p>
          <p style="color:var(--text2);line-height:1.8;margin-bottom:1.75rem;font-size:.95rem">Our AI voice agents answer inbound calls, qualify the lead, collect job details, and book appointments directly into your calendar — all without you lifting a finger. When a real human is needed, the call transfers seamlessly.</p>
          <a href="/services/ai-voice-agents.html" class="btn-gold">Learn more <span class="icon-wrap">↗</span></a>
        </div>
        <div>
          <p style="font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--text3);margin-bottom:1.25rem">What's included</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
            {''.join(f'<div style="display:flex;align-items:flex-start;gap:.5rem">{CHECK}<span style="font-size:.85rem;color:var(--text2);line-height:1.4">{f}</span></div>' for f in ["24/7 call answering","Lead qualification scripts","Appointment booking","CRM data capture","Call transcripts","Seamless human transfer","Custom voice setup","Multi-location support"])}
          </div>
        </div>
      </div>
      <div class="reveal card" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start" class="svc-row">
        <div>
          <div style="width:3rem;height:3rem;border-radius:.875rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold);margin-bottom:1.5rem"><svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg></div>
          <h2 style="font-size:1.6rem;font-weight:700;color:var(--text);margin-bottom:.5rem;letter-spacing:-.02em">Lead Generation</h2>
          <p style="color:var(--gold);font-size:.9rem;font-weight:500;margin-bottom:1.25rem">Google Ads that pay for themselves.</p>
          <p style="color:var(--text2);line-height:1.8;margin-bottom:1.75rem;font-size:.95rem">We manage Google Search Ads, Local Services Ads, and Meta campaigns exclusively for contractors. Every dollar tracked. Every call attributed. No bloated agency overhead — just results.</p>
          <a href="/services/lead-generation.html" class="btn-gold">Learn more <span class="icon-wrap">↗</span></a>
        </div>
        <div>
          <p style="font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--text3);margin-bottom:1.25rem">What's included</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
            {''.join(f'<div style="display:flex;align-items:flex-start;gap:.5rem">{CHECK}<span style="font-size:.85rem;color:var(--text2);line-height:1.4">{f}</span></div>' for f in ["Google Search Ads","Local Services Ads","Facebook & Instagram","Call tracking setup","Monthly reporting","Landing page optimization","Competitor analysis","Budget optimization"])}
          </div>
        </div>
      </div>
      <div class="reveal card" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start" class="svc-row">
        <div>
          <div style="width:3rem;height:3rem;border-radius:.875rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;color:var(--gold);margin-bottom:1.5rem"><svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg></div>
          <h2 style="font-size:1.6rem;font-weight:700;color:var(--text);margin-bottom:.5rem;letter-spacing:-.02em">CRM &amp; Automation</h2>
          <p style="color:var(--gold);font-size:.9rem;font-weight:500;margin-bottom:1.25rem">Stop letting leads fall through the cracks.</p>
          <p style="color:var(--text2);line-height:1.8;margin-bottom:1.75rem;font-size:.95rem">Built on GoHighLevel, our white-labeled CRM keeps every lead, job, and customer in one place. Automated texts, emails, and review requests go out the moment a job is complete.</p>
          <a href="/services/crm-automation.html" class="btn-gold">Learn more <span class="icon-wrap">↗</span></a>
        </div>
        <div>
          <p style="font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--text3);margin-bottom:1.25rem">What's included</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:.75rem">
            {''.join(f'<div style="display:flex;align-items:flex-start;gap:.5rem">{CHECK}<span style="font-size:.85rem;color:var(--text2);line-height:1.4">{f}</span></div>' for f in ["GHL CRM setup","Automated follow-up","Review automation","Missed call text-back","Pipeline management","Email & SMS sequences","Reputation monitoring","Multi-location support"])}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
""",
    extra_css="@media(max-width:900px){.svc-row{grid-template-columns:1fr!important;gap:2rem!important}}"
)
write("services.html", services_page)

# ─── SERVICE SUBPAGES ───
def svc_subpage(title, desc, canonical, badge_color, badge_text, h1, tagline, body_text, steps, included):
    steps_html = ''.join(f'<div style="background:var(--surface);padding:2rem 2.5rem;display:grid;grid-template-columns:3rem 1fr;gap:1.5rem;align-items:flex-start"><span style="font-size:2rem;font-weight:800;color:rgba(232,160,32,.25);line-height:1">{s["n"]}</span><div><h3 style="font-weight:600;color:var(--text);font-size:1.05rem;margin-bottom:.5rem">{s["t"]}</h3><p style="color:var(--text2);font-size:.875rem;line-height:1.7">{s["d"]}</p></div></div>' for s in steps)
    included_html = ''.join(f'<div style="display:flex;align-items:center;gap:.6rem">{CHECK}<span style="font-size:.875rem;color:var(--text2)">{i}</span></div>' for i in included)
    return page(title, desc, canonical, f"""
<section class="page-hero" style="background:radial-gradient(ellipse 50% 40% at 30% 50%,{badge_color}11 0%,transparent 70%)">
  <div class="container">
    <div style="display:inline-flex;align-items:center;gap:.5rem;background:{badge_color}14;border:1px solid {badge_color}30;border-radius:9999px;padding:.35rem .85rem;margin-bottom:1.5rem" class="fadein">
      <span style="font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:{badge_color}">{badge_text}</span>
    </div>
    <h1 class="serif fadein d1">{h1}</h1>
    <p class="fadein d2">{tagline}</p>
    <div class="fadein d3" style="margin-top:2.5rem;display:flex;flex-wrap:wrap;gap:1rem">
      <a href="/contact.html" class="btn-gold" style="font-size:1rem;padding:1rem 2rem">Get a Free Audit <span class="icon-wrap">↗</span></a>
      <a href="/results.html" class="btn-ghost" style="font-size:1rem;padding:1rem 2rem">See Our Work</a>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:4rem">
  <div class="container">
    <div class="reveal">
      <h2 class="serif" style="font-size:clamp(1.75rem,3vw,2.5rem);color:var(--text);margin-bottom:3rem;max-width:500px">{body_text["h"]}</h2>
    </div>
    <div style="display:flex;flex-direction:column;gap:1px;background:rgba(255,255,255,.04);border-radius:1.5rem;overflow:hidden;margin-bottom:5rem">{steps_html}</div>
    <div class="reveal card" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem" class="included-outer">
      <div>
        <h2 class="serif" style="font-size:2rem;color:var(--text);margin-bottom:1rem">What is included</h2>
        <p style="color:var(--text2);line-height:1.7;margin-bottom:2rem">{body_text["p"]}</p>
        <a href="/contact.html" class="btn-gold">Get Started <span class="icon-wrap">↗</span></a>
      </div>
      <div style="display:flex;flex-direction:column;gap:.65rem">{included_html}</div>
    </div>
  </div>
</section>
""", extra_css="@media(max-width:900px){.included-outer{grid-template-columns:1fr!important;gap:2rem!important}} @media(max-width:600px){[style*='grid-template-columns:3rem 1fr']{grid-template-columns:1fr!important}}")

write("services/smart-websites.html", svc_subpage(
    "SEO-Optimized Websites for Contractors | LeadWise Connect",
    "We build contractor websites engineered from the ground up to rank on Google and convert visitors into booked jobs. AI chat, voice widgets, and full local SEO architecture included.",
    "/services/smart-websites.html",
    "#E8A020", "Smart Websites",
    "A contractor website that works as hard as you do",
    "We build SEO-first contractor websites that rank in Google search, answer leads at 2am, and convert visitors into booked jobs — all while you are on the jobsite.",
    {"h": "Why our sites outperform the competition", "p": "No surprise add-ons. No separate charges for SEO or mobile. One engagement — everything your site needs to rank and convert."},
    [
        {"n":"1","t":"SEO-first architecture","d":"Every page is built around the keywords your customers search. Service pages, city pages, and blog all strategically structured for maximum organic visibility."},
        {"n":"2","t":"AI chat & voice widget","d":"An AI chatbot and voice agent embedded on every page. They answer questions, qualify leads, and book appointments 24/7 — even when you're on a job."},
        {"n":"3","t":"Location page strategy","d":"We create dedicated pages for every city and suburb you serve — the system that earns thousands of monthly visitors from organic search."},
        {"n":"4","t":"Built to convert","d":"Clear CTAs, click-to-call buttons, trust signals, and lead forms positioned exactly where visitors are ready to act."},
    ],
    ["Custom website build","Homepage, About, Contact","Service-specific pages","City/location pages (20+)","Blog setup (5 seed articles)","Schema markup (LocalBusiness)","Google Business Profile optimization","AI chat widget","AI voice widget","Core Web Vitals optimized","XML sitemap","Google Analytics 4","Google Search Console","Monthly rank tracking","CRM form integration","SSL + hosting setup"]
))

write("services/ai-voice-agents.html", svc_subpage(
    "AI Voice Agents for Contractors | 24/7 Call Answering | LeadWise Connect",
    "Never miss a lead again. Our AI voice agents answer contractor calls 24/7, qualify leads, and book appointments automatically. Built for HVAC, plumbing, roofing, and electrical.",
    "/services/ai-voice-agents.html",
    "#C084FC", "AI Voice Agents",
    "Your best employee. Works 24/7. Never calls in sick.",
    "Every missed call after hours is a job your competitor just booked. Our AI voice agents answer every call, qualify every lead, and book appointments directly into your calendar — automatically.",
    {"h": "What happens when your phone rings at midnight", "p": "Every AI Voice Agent deployment is customized to your trade, your service area, and your booking process."},
    [
        {"n":"1","t":"Call comes in — any hour, any day","d":"Your AI voice agent answers instantly with a professional greeting branded to your company. The caller has no idea they are not talking to your office."},
        {"n":"2","t":"Lead is qualified on the spot","d":"The agent asks the right questions: type of service, urgency level, location, contact info. All captured and logged to your CRM in real time."},
        {"n":"3","t":"Appointment booked automatically","d":"If the lead is ready to book, the AI checks your calendar and schedules directly. A confirmation text goes to the customer immediately."},
        {"n":"4","t":"You get the full summary","d":"You receive a call transcript, lead score, and appointment notification — so you show up prepared and ready to close."},
    ],
    ["Custom voice & personality","Branded greeting script","Lead qualification flow","Calendar integration","CRM data capture (GHL)","Call transcripts & recordings","Seamless human transfer","SMS confirmation to callers","After-hours emergency routing","Multi-location support"]
))

write("services/lead-generation.html", svc_subpage(
    "Lead Generation for Contractors | Google Ads & Local Services | LeadWise Connect",
    "Google Ads, Local Services Ads, and Meta campaigns built exclusively for HVAC, plumbing, roofing, and electrical contractors. Pay for results — not reports.",
    "/services/lead-generation.html",
    "#4ADE80", "Lead Generation",
    "Paid ads that pay for themselves — or we fix it",
    "We manage Google Search Ads, Local Services Ads, and Meta campaigns exclusively for contractors. Every dollar tracked. Every call attributed. No bloated reports full of impressions nobody cares about.",
    {"h": "Where we run your ads", "p": "We track every call, form fill, and booked job back to the exact ad that generated it. You always know your cost per lead."},
    [
        {"n":"1","t":"Google Local Services Ads","d":"Pay-per-lead ads at the very top of Google with your reviews and license. The best cost-per-lead in the industry for most trades."},
        {"n":"2","t":"Google Search Ads","d":"Capture customers actively searching for your services right now. We write the ads, manage bids, and optimize weekly."},
        {"n":"3","t":"Facebook & Instagram Ads","d":"Ideal for seasonal promotions, retargeting website visitors, and reaching homeowners before they have a problem."},
        {"n":"4","t":"Reporting & optimization","d":"Monthly reporting with every metric that matters — calls, leads, cost per acquisition — and ongoing optimization to keep improving."},
    ],
    ["Google Search Ads","Google Local Services Ads","Facebook & Instagram Ads","Call tracking setup","Monthly reporting dashboard","Landing page optimization","Competitor keyword analysis","Negative keyword management","Bid strategy optimization","Campaign restructuring"]
))

write("services/crm-automation.html", svc_subpage(
    "CRM & Automation for Contractors | GHL Setup | LeadWise Connect",
    "Stop letting leads fall through the cracks. Our GHL-powered CRM automates follow-ups, review requests, and pipeline management for local service contractors.",
    "/services/crm-automation.html",
    "#60A5FA", "CRM & Automation",
    "Stop letting leads fall through the cracks",
    "Most contractors lose jobs not because they do bad work — but because they never followed up. Our GHL-powered automation handles follow-ups, review requests, and pipeline tracking so nothing slips.",
    {"h": "What runs on autopilot", "p": "Built on GoHighLevel — the same platform used by thousands of agency-level operations. You get a professional, fully-configured CRM without touching a single setting."},
    [
        {"n":"1","t":"Missed call text-back","d":"The instant a call goes unanswered, an automated text goes out: 'Sorry we missed you — how can we help?' Recovers 30–40% of missed leads."},
        {"n":"2","t":"Lead nurture sequences","d":"Automated SMS and email sequences keep prospects warm over 7, 14, and 30 days. Most jobs are booked on the 3rd or 4th touchpoint."},
        {"n":"3","t":"Review request automation","d":"After every completed job, a review request goes out automatically. This is how we took our HVAC client from 10 to 34 Google reviews in 6 months."},
        {"n":"4","t":"Pipeline management","d":"Every lead lives in a visual pipeline — New, Contacted, Quoted, Booked, Complete. You always know exactly where every job stands."},
    ],
    ["Full GHL account setup","Custom pipeline stages","Automated SMS sequences","Automated email sequences","Missed call text-back","Review request automation","Appointment reminders","Two-way SMS inbox","Lead source tracking","Monthly reporting"]
))

print("Service pages done!")

# ─── BLOG POSTS ───
posts = [
    {
        "slug": "why-contractor-websites-fail-at-seo",
        "category": "SEO",
        "title": "Why 90% of Contractor Websites Fail at SEO (And What to Do Instead)",
        "date": "March 2025", "read": "6 min read",
        "desc": "Most contractor sites are single-page brochures with no content strategy. Here is the exact page architecture that actually ranks in local search.",
        "content": [
            ("p", "Most contractor websites were built to look good in a portfolio — not to rank on Google or generate leads. The result is a site that costs thousands and generates essentially zero organic traffic."),
            ("p", "The core problem is simple: Google needs content to understand what your business does and where you do it. A single homepage with a paragraph about your services gives Google almost nothing to work with."),
            ("h", "The five reasons contractor sites fail at SEO"),
            ("p", "First, they have one page covering every service. A single page listing HVAC repair, AC installation, duct cleaning, and water heaters is invisible to Google. Each service needs its own dedicated page because people search for specific services — not generic menus."),
            ("p", "Second, they have no location targeting. If you serve Tampa, Brandon, Riverview, and Plant City, you need a dedicated page for each. Google ranks pages for local searches, not just businesses."),
            ("p", "Third, they have no blog or educational content. Google rewards websites that publish helpful, relevant content consistently. A blog signals expertise and attracts long-tail search traffic over time."),
            ("p", "Fourth, they are not technically optimized. Slow load times, missing schema markup, and poor Core Web Vitals scores hurt rankings even if content is solid."),
            ("p", "Fifth, they have no internal linking strategy. Every page should link to related pages — service pages to location pages, blog posts to service pages."),
            ("h", "The architecture that works"),
            ("p", "Homepage positioned for your primary city and top services. Service pages — one per service. Location pages — one per city you serve. Blog targeting informational keywords. Supporting pages with local signals."),
            ("p", "This structure gives Google hundreds of specific, relevant pages to index — instead of one generic homepage. The contractors who invest in this architecture consistently dominate local search."),
        ]
    },
    {
        "slug": "google-business-profile-for-contractors",
        "category": "Local SEO",
        "title": "The Complete Google Business Profile Guide for Contractors in 2025",
        "date": "February 2025", "read": "8 min read",
        "desc": "Your GBP is your most powerful free ranking tool — and most contractors are wasting it. Here is how to optimize every section for maximum local visibility.",
        "content": [
            ("p", "Your Google Business Profile is the single most powerful free tool available to local service contractors. It determines whether you appear in the map pack — those three businesses at the top of local searches — and drives more calls than most contractors realize."),
            ("h", "Complete every section fully"),
            ("p", "Google uses completion signals to determine which businesses to show. Incomplete profiles rank lower. Make sure every section is filled out: business name, category, address, phone, website, hours, service area, services, photos, and description."),
            ("h", "Choose the right primary category"),
            ("p", "Your primary category is the most important ranking factor on your GBP. For an HVAC company, it should be 'HVAC Contractor.' Use secondary categories for additional services."),
            ("h", "Post consistently"),
            ("p", "Google Posts appear directly on your profile. Post once or twice per week — seasonal promotions, tips, recent jobs. Consistent posting signals that you are an active, engaged business."),
            ("h", "Reviews are your most important ranking signal"),
            ("p", "The number, recency, and rating of your reviews is one of the top three local ranking factors. Automate your review requests: send a text with your direct review link within 24 hours of every completed job."),
            ("p", "We took our HVAC client from 10 to 34 reviews in six months using exactly this system."),
        ]
    },
    {
        "slug": "ai-voice-agents-for-hvac-plumbers",
        "category": "AI & Automation",
        "title": "How AI Voice Agents Are Helping HVAC and Plumbing Companies Book 30% More Jobs",
        "date": "February 2025", "read": "5 min read",
        "desc": "Speed to lead wins jobs. We break down exactly how AI voice agents work, what they cost, and the ROI calculation for service contractors.",
        "content": [
            ("p", "In the trades, speed to lead is everything. Studies show that 78% of customers hire the first contractor who responds to them. The problem is most calls come when you are on a job, driving, or asleep."),
            ("h", "What an AI voice agent actually does"),
            ("p", "When a customer calls your number and you do not answer — whether it is 2pm or 2am — the AI picks up immediately. It greets the caller with your company name, gathers their information, qualifies the lead, and either books them directly into your calendar or routes urgent calls to you personally."),
            ("p", "The caller never knows they are talking to AI. The conversation feels natural, professional, and fast."),
            ("h", "The ROI calculation for contractors"),
            ("p", "A typical HVAC company doing 8–12 jobs per week misses 20–30% of calls during business hours and nearly all after-hours calls. At an average job value of $400–$800, that is $3,000–$6,000 per week in potential revenue that evaporates because nobody answered."),
            ("p", "An AI voice agent capturing even 30–40% of those missed calls pays for itself many times over within the first month."),
            ("h", "What to look for in a voice agent"),
            ("p", "You want one that integrates with your CRM so lead data flows automatically, handles natural conversation rather than rigid menu systems, can transfer to a live human when needed, and provides call transcripts and recordings for every interaction."),
        ]
    },
    {
        "slug": "contractor-location-pages-seo",
        "category": "SEO",
        "title": "How to Build Location Pages That Actually Rank for Contractors",
        "date": "January 2025", "read": "7 min read",
        "desc": "City landing pages are the single highest-ROI SEO move for contractors who serve multiple areas. Here is how to build them the right way.",
        "content": [
            ("p", "If you serve more than one city or suburb, location pages are the single highest-ROI SEO investment you can make. A dedicated page for each city lets you rank for searches like 'HVAC repair Brandon FL' or 'plumber Riverview' — searches with extremely high purchase intent."),
            ("h", "What a real location page needs"),
            ("p", "First, unique content for each location. Do not copy and paste the same text and swap the city name. Google detects this immediately. Write genuinely unique content for each location — mention specific neighborhoods, local landmarks, the type of housing common in that area."),
            ("p", "Second, a clear H1 that includes the service and city. Something like 'HVAC Repair in Riverview, FL' — not 'Welcome to Our Riverview Page.'"),
            ("p", "Third, local schema markup. Use LocalBusiness schema with the specific address, service area, and geo coordinates for each location."),
            ("p", "Fourth, real local signals. Mention the zip codes you serve, reference local weather patterns if relevant, include a specific phone number or local tracking number if possible."),
            ("h", "How many location pages do you need?"),
            ("p", "For a contractor serving a metro area, we typically build 15–25 location pages — one per major suburb or city. For the HVAC client we serve in Tampa, we built 20 location pages covering every major community in Hillsborough and Pinellas counties."),
        ]
    },
    {
        "slug": "google-reviews-for-contractors",
        "category": "Reputation",
        "title": "From 10 to 34 Reviews in 6 Months: The Review Automation System We Use",
        "date": "January 2025", "read": "5 min read",
        "desc": "Reviews are the fastest way to rank higher and convert more visitors. Here is the automated post-job follow-up sequence we built for our HVAC client.",
        "content": [
            ("p", "When we started working with North East Heating and Cooling, they had 10 Google reviews. Six months later, they have 34 — all 5 stars, all genuine, all from real customers. Here is exactly how we did it."),
            ("h", "The three-step sequence"),
            ("p", "Step one: within 2 hours of job completion, the technician sends a personalized text. Not a generic template — a personal message referencing the job and the customer by name. Include a direct review link that opens the form immediately."),
            ("p", "Step two: if no review after 48 hours, an automated follow-up SMS goes out. Simple, friendly, no pressure."),
            ("p", "Step three: if still no review, a final email goes out 72 hours later. After three touches, we stop."),
            ("h", "The result"),
            ("p", "With this system, roughly 40–50% of customers who receive the sequence leave a review. For a contractor doing 5–8 jobs per week, that is 2–4 new reviews per week, compounding fast."),
            ("p", "The difference between 10 and 34 reviews is not just a number. More reviews means higher map pack rankings, stronger trust signals on your website, and higher conversion when customers compare you to competitors."),
        ]
    },
    {
        "slug": "how-much-does-contractor-website-cost",
        "category": "Websites",
        "title": "How Much Should a Contractor Website Cost in 2025? (Honest Breakdown)",
        "date": "December 2024", "read": "6 min read",
        "desc": "From $500 templates to $30k agency builds — what do you actually need? We break down what drives cost and what is worth paying for.",
        "content": [
            ("p", "The range of prices for contractor websites is enormous — from a few hundred dollars on Wix to $30,000+ at a large agency. Most contractors end up in the middle somewhere, often overpaying for something that does not generate leads."),
            ("h", "The $500–$2,000 template option"),
            ("p", "Platforms like Wix, Squarespace, and basic WordPress installs can get you a decent-looking site for minimal cost. The problem is not how they look — it is what they are missing underneath. Most template sites have no SEO architecture, no location pages, no schema markup."),
            ("h", "The $5,000–$15,000 custom option"),
            ("p", "This is where most professional agencies live. A custom build with a real content strategy, proper technical SEO, and conversion optimization. If done right, this is a strong investment."),
            ("p", "The key questions: does the agency specialize in contractors, or do they build sites for everyone? Do they understand local SEO, or just design? Will they build location pages with real content?"),
            ("h", "What actually moves the needle"),
            ("p", "After building contractor sites ourselves, here is what generates real leads: multiple service-specific pages, city and location pages targeting every area you serve, proper schema markup, fast load times, clear calls-to-action, and an integrated lead capture system."),
            ("p", "A site with all of this will outperform a beautiful but thin site every single time. The budget matters less than the strategy behind it."),
        ]
    },
]

def blog_content_html(content):
    out = []
    for t, txt in content:
        if t == "h":
            out.append(f'<h2 style="font-size:1.3rem;font-weight:700;color:var(--text);margin:2.5rem 0 .75rem">{txt}</h2>')
        else:
            out.append(f'<p style="color:var(--text2);line-height:1.85;margin-bottom:1.5rem;font-size:1rem">{txt}</p>')
    return '\n'.join(out)

cat_colors = {"SEO":"#E8A020","Local SEO":"#60A5FA","AI & Automation":"#C084FC","Reputation":"#4ADE80","Websites":"#F87171"}

# Blog listing
post_cards = []
for i, p in enumerate(posts):
    cc = cat_colors.get(p['category'], '#E8A020')
    if i == 0:
        post_cards.append(f'''
<div class="reveal" style="margin-bottom:3rem">
  <a href="/blog/{p["slug"]}.html" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;background:var(--surface);border:1px solid rgba(232,160,32,.15);border-radius:1.5rem;padding:3rem;text-decoration:none;transition:all .4s cubic-bezier(.22,1,.36,1)" class="blog-featured">
    <div>
      <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1.5rem">
        <span style="font-size:.65rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:{cc};background:{cc}22;border-radius:9999px;padding:.3rem .75rem">{p["category"]}</span>
        <span style="font-size:.75rem;color:var(--text3)">Featured</span>
      </div>
      <h2 style="font-size:1.75rem;font-weight:700;color:var(--text);line-height:1.2;letter-spacing:-.02em;margin-bottom:1rem">{p["title"]}</h2>
      <p style="color:var(--text2);line-height:1.7;margin-bottom:1.5rem;font-size:.95rem">{p["desc"]}</p>
      <div style="display:flex;align-items:center;gap:.75rem"><span style="font-size:.8rem;color:var(--text3)">{p["date"]}</span><span style="color:var(--text3)">·</span><span style="font-size:.8rem;color:var(--text3)">{p["read"]}</span></div>
    </div>
    <div style="display:flex;justify-content:flex-end;align-items:center"><div style="width:4rem;height:4rem;border-radius:50%;border:1px solid rgba(232,160,32,.3);display:flex;align-items:center;justify-content:center;font-size:1.25rem;color:var(--gold)">↗</div></div>
  </a>
</div>''')
    else:
        post_cards.append(f'''
<a href="/blog/{p["slug"]}.html" style="display:block;text-decoration:none" class="blog-card-link">
  <div class="reveal" style="background:var(--surface);border:1px solid rgba(255,255,255,.06);border-radius:1.5rem;padding:2rem;display:flex;flex-direction:column;gap:1rem;height:100%;transition:all .4s cubic-bezier(.22,1,.36,1)" class="blog-card">
    <span style="font-size:.65rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:{cc};background:{cc}22;border-radius:9999px;padding:.3rem .75rem;align-self:flex-start">{p["category"]}</span>
    <h3 style="font-size:1.1rem;font-weight:600;color:var(--text);line-height:1.35;flex:1">{p["title"]}</h3>
    <p style="font-size:.875rem;color:var(--text2);line-height:1.6">{p["desc"]}</p>
    <div style="display:flex;align-items:center;justify-content:space-between"><div style="display:flex;gap:.75rem"><span style="font-size:.75rem;color:var(--text3)">{p["date"]}</span><span style="color:var(--text3)">·</span><span style="font-size:.75rem;color:var(--text3)">{p["read"]}</span></div><span style="color:var(--gold);font-size:.85rem">→</span></div>
  </div>
</a>''')

grid_cards = post_cards[1:]
blog_listing = page(
    "Blog | Contractor Marketing Tips & SEO Guides | LeadWise Connect",
    "Free guides on local SEO, contractor websites, Google rankings, and lead generation for HVAC, plumbing, roofing, and electrical businesses.",
    "/blog.html",
    f"""
<section class="page-hero">
  <div class="container">
    <span class="eyebrow fadein">The LeadWise Blog</span>
    <h1 class="serif fadein d1">Free guides for contractors who want to grow online</h1>
    <p class="fadein d2">No fluff. No generic advice. Everything here is built for HVAC, plumbing, roofing, electrical, and other local service trades.</p>
  </div>
</section>
<section class="sec" style="padding-top:2rem">
  <div class="container">
    {''.join(post_cards[:1])}
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.25rem">
      {''.join(grid_cards)}
    </div>
  </div>
</section>
<section class="sec" style="background:#0D0D0D;border-top:1px solid rgba(255,255,255,.04);text-align:center">
  <div style="max-width:600px;margin:0 auto" class="reveal">
    <h2 class="serif" style="font-size:2.5rem;color:var(--text);margin-bottom:1rem;line-height:1.1">Want us to apply this to your business?</h2>
    <p style="color:var(--text2);margin-bottom:2rem;line-height:1.7">Stop reading and start ranking. Get a free audit of your contractor website and local SEO — no obligation.</p>
    <a href="/contact.html" class="btn-gold">Get My Free Audit ↗</a>
  </div>
</section>
""",
    extra_css=".blog-featured:hover{border-color:rgba(232,160,32,.35)!important;transform:translateY(-2px)} .blog-card:hover{border-color:rgba(232,160,32,.2)!important;transform:translateY(-3px)}"
)
write("blog.html", blog_listing)

# Individual blog posts
for p in posts:
    cc = cat_colors.get(p['category'], '#E8A020')
    post_html = page(
        f"{p['title']} | LeadWise Connect Blog",
        p["desc"],
        f"/blog/{p['slug']}.html",
        f"""
<section style="padding:8rem 2rem 3rem">
  <div style="max-width:780px;margin:0 auto">
    <a href="/blog.html" style="display:inline-flex;align-items:center;gap:.4rem;color:var(--text2);font-size:.85rem;margin-bottom:2rem;transition:color .2s" class="back-link">← Back to Blog</a>
    <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1.5rem">
      <span style="font-size:.65rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:{cc};background:{cc}22;border-radius:9999px;padding:.3rem .75rem">{p["category"]}</span>
      <span style="font-size:.8rem;color:var(--text3)">{p["date"]}</span>
      <span style="color:var(--text3)">·</span>
      <span style="font-size:.8rem;color:var(--text3)">{p["read"]}</span>
    </div>
    <h1 class="serif" style="font-size:clamp(2rem,4vw,3rem);color:var(--text);line-height:1.1;margin-bottom:1rem">{p["title"]}</h1>
    <p style="color:var(--text2);font-size:1.1rem;line-height:1.7">{p["desc"]}</p>
  </div>
</section>
<article style="padding:0 2rem 4rem">
  <div style="max-width:780px;margin:0 auto;border-top:1px solid rgba(255,255,255,.06);padding-top:3rem">
    {blog_content_html(p["content"])}
  </div>
</article>
<section style="padding:4rem 2rem 8rem">
  <div style="max-width:780px;margin:0 auto">
    <div style="background:rgba(232,160,32,.05);border:1px solid rgba(232,160,32,.15);border-radius:1.5rem;padding:3rem;text-align:center">
      <h3 class="serif" style="font-size:2rem;color:var(--text);margin-bottom:.75rem">Want us to do this for your business?</h3>
      <p style="color:var(--text2);margin-bottom:2rem;line-height:1.7">Get a free audit and we will show you exactly what it would take to apply this to your contracting business.</p>
      <a href="/contact.html" class="btn-gold">Get My Free Audit ↗</a>
    </div>
  </div>
</section>
""",
        extra_css=".back-link:hover{color:var(--gold)!important}"
    )
    write(f"blog/{p['slug']}.html", post_html)

# ─── SITEMAP ───
sitemap_urls = [
    ("https://leadwiseconnect.com/", "1.0", "weekly"),
    ("https://leadwiseconnect.com/services.html", "0.9", "monthly"),
    ("https://leadwiseconnect.com/services/smart-websites.html", "0.9", "monthly"),
    ("https://leadwiseconnect.com/services/ai-voice-agents.html", "0.9", "monthly"),
    ("https://leadwiseconnect.com/services/lead-generation.html", "0.8", "monthly"),
    ("https://leadwiseconnect.com/services/crm-automation.html", "0.8", "monthly"),
    ("https://leadwiseconnect.com/results.html", "0.8", "monthly"),
    ("https://leadwiseconnect.com/about.html", "0.7", "monthly"),
    ("https://leadwiseconnect.com/blog.html", "0.8", "weekly"),
    ("https://leadwiseconnect.com/contact.html", "0.9", "monthly"),
] + [(f"https://leadwiseconnect.com/blog/{p['slug']}.html", "0.7", "monthly") for p in posts]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url, pri, freq in sitemap_urls:
    sitemap += f'  <url><loc>{url}</loc><priority>{pri}</priority><changefreq>{freq}</changefreq></url>\n'
sitemap += '</urlset>'
write("sitemap.xml", sitemap)

with open("robots.txt", "w") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://leadwiseconnect.com/sitemap.xml\n")
print("robots.txt written")

print("\nAll pages built!")
import os
for root,dirs,files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            print(f"  {os.path.join(root,file)}")
