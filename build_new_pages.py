import os

BASE_CSS = open('_base.css').read()
NAV_ROOT = open('_nav.html').read()
FOOTER_ROOT = open('_footer.html').read()
NAV_SUB = open('_nav_sub.html').read()
FOOTER_SUB = open('_footer_sub.html').read()
SCRIPTS_JS = open('_scripts.js').read()

def page(title, desc, canonical, body, extra_css='', subpage=False):
    nav = NAV_SUB if subpage else NAV_ROOT
    footer = FOOTER_SUB if subpage else FOOTER_ROOT
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
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="https://leadwiseconnect.com{canonical}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<style>
{BASE_CSS}
{extra_css}
</style>
</head>
<body>
{nav}
{body}
{footer}
<script>{SCRIPTS_JS}</script>
</body>
</html>"""

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w') as f: f.write(content)
    print(f"  wrote {path}")

CHECK = '<svg width="14" height="14" fill="currentColor" viewBox="0 0 16 16" style="flex-shrink:0;margin-top:.15rem"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"/></svg>'
X_ICON = '<svg width="14" height="14" fill="currentColor" viewBox="0 0 16 16" style="flex-shrink:0;margin-top:.15rem;color:#F87171"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg>'

# ─── TRADE PAGE TEMPLATE ─────────────────────────────────────────────
def trade_page(slug, trade, trade_plural, keyword, pain_point, pain_detail, 
               stat1_num, stat1_label, stat2_num, stat2_label, stat3_num, stat3_label,
               specific_features, why_items, cta_line):
    features_html = ''.join(f'<div style="display:flex;align-items:flex-start;gap:.75rem;padding:1.25rem;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);border-radius:1rem"><div style="flex-shrink:0;margin-top:.1rem">{CHECK}</div><div><p style="font-weight:600;color:var(--text);font-size:.95rem;margin-bottom:.25rem">{f[0]}</p><p style="color:var(--text2);font-size:.85rem;line-height:1.6">{f[1]}</p></div></div>' for f in specific_features)
    why_html = ''.join(f'<div style="display:flex;gap:1rem"><div style="width:2px;background:rgba(232,160,32,.3);border-radius:9999px;flex-shrink:0"></div><div><p style="font-weight:600;color:var(--text);margin-bottom:.25rem;font-size:.95rem">{w[0]}</p><p style="color:var(--text2);font-size:.875rem;line-height:1.6">{w[1]}</p></div></div>' for w in why_items)

    return page(
        f"{trade} Marketing Agency | Websites & SEO for {trade_plural} | LeadWise Connect",
        f"We build SEO-optimized websites and lead generation systems exclusively for {trade_plural}. Stop paying for shared leads — own your Google rankings instead.",
        f"/{slug}.html",
        f"""
<section class="page-hero" style="background:radial-gradient(ellipse 60% 50% at 50% -10%,rgba(232,160,32,.12) 0%,transparent 70%);position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.015) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.015) 1px,transparent 1px);background-size:80px 80px;pointer-events:none"></div>
  <div class="container" style="position:relative;z-index:1">
    <div style="display:inline-flex;align-items:center;gap:.5rem;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.2);border-radius:9999px;padding:.35rem .85rem .35rem .5rem;margin-bottom:1.5rem" class="fadein">
      <span style="width:6px;height:6px;border-radius:50%;background:#E8A020;animation:pulse-gold 2s ease-in-out infinite"></span>
      <span style="font-size:.7rem;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:#E8A020">{trade} Marketing Specialists</span>
    </div>
    <h1 class="serif fadein d1" style="font-size:clamp(2.75rem,6vw,5.5rem);color:var(--text);line-height:1;max-width:900px;margin-bottom:1.75rem">
      Stop renting leads.<br><span style="background:linear-gradient(135deg,#F5C060 0%,#E8A020 50%,#B87818 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">Own your rankings</span><br>instead.
    </h1>
    <p class="fadein d2" style="font-size:clamp(1rem,2vw,1.2rem);color:var(--text2);max-width:580px;line-height:1.75;margin-bottom:2.5rem">{pain_point} We build SEO-optimized websites and lead systems that put your {trade_plural.lower()} company at the top of Google — so customers call you directly, not a lead broker.</p>
    <div class="fadein d3" style="display:flex;flex-wrap:wrap;gap:1rem;margin-bottom:4rem">
      <a href="contact.html" class="btn-gold" style="font-size:1rem;padding:1rem 2rem">Get Your Free {trade} Audit <span class="icon-wrap">↗</span></a>
      <a href="results.html" class="btn-ghost" style="font-size:1rem;padding:1rem 2rem">See Our Work</a>
    </div>
    <div class="fadein d4" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;max-width:600px" id="hero-stats">
      <div style="background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.15);border-radius:1rem;padding:1.25rem;text-align:center">
        <p style="font-size:2rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">{stat1_num}</p>
        <p style="font-size:.75rem;color:var(--text2);margin-top:.35rem;line-height:1.4">{stat1_label}</p>
      </div>
      <div style="background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.15);border-radius:1rem;padding:1.25rem;text-align:center">
        <p style="font-size:2rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">{stat2_num}</p>
        <p style="font-size:.75rem;color:var(--text2);margin-top:.35rem;line-height:1.4">{stat2_label}</p>
      </div>
      <div style="background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.15);border-radius:1rem;padding:1.25rem;text-align:center">
        <p style="font-size:2rem;font-weight:800;color:var(--gold);letter-spacing:-.04em;line-height:1">{stat3_num}</p>
        <p style="font-size:.75rem;color:var(--text2);margin-top:.35rem;line-height:1.4">{stat3_label}</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" style="background:rgba(232,160,32,.03);border-top:1px solid rgba(232,160,32,.08);border-bottom:1px solid rgba(232,160,32,.08)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center" id="pain-grid">
      <div class="reveal">
        <span class="eyebrow">The Problem</span>
        <h2 class="serif" style="font-size:clamp(1.75rem,3vw,2.75rem);color:var(--text);margin-bottom:1.5rem">Angi and HomeAdvisor are not your friends.</h2>
        <p style="color:var(--text2);line-height:1.8;margin-bottom:1.5rem">{pain_detail}</p>
        <p style="color:var(--text2);line-height:1.8">Every dollar you spend on shared leads is a dollar that could be building your own Google rankings — an asset you own forever, not a tap that turns off the moment you stop paying.</p>
      </div>
      <div class="reveal">
        <div style="display:flex;flex-direction:column;gap:.75rem">
          <p style="font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--text3);margin-bottom:.5rem">Lead platforms vs. owning your rankings</p>
          <div style="background:var(--surface);border:1px solid rgba(255,87,87,.2);border-radius:1rem;padding:1.5rem">
            <p style="font-weight:700;color:#F87171;font-size:.9rem;margin-bottom:1rem">❌ Angi / HomeAdvisor / Thumbtack</p>
            <div style="display:flex;flex-direction:column;gap:.6rem">
              {f''.join(f'<div style="display:flex;align-items:flex-start;gap:.6rem">{X_ICON}<span style="font-size:.875rem;color:var(--text2)">{x}</span></div>' for x in ["$50–$200 per shared lead — split with 3–5 competitors","Leads go cold fast — you're one of many calling","Zero brand building — customers remember the platform, not you","Pricing goes up every year — you have no leverage","Turn it off and the phone goes silent immediately"])}
            </div>
          </div>
          <div style="background:var(--surface);border:1px solid rgba(232,160,32,.2);border-radius:1rem;padding:1.5rem">
            <p style="font-weight:700;color:var(--gold);font-size:.9rem;margin-bottom:1rem">✓ LeadWise: Own Your Google Rankings</p>
            <div style="display:flex;flex-direction:column;gap:.6rem">
              {f''.join(f'<div style="display:flex;align-items:flex-start;gap:.6rem">{CHECK}<span style="font-size:.875rem;color:var(--text2)">{x}</span></div>' for x in ["Customers find YOU directly — no middleman","Exclusive leads — they called your number, nobody else","Every month your rankings compound and get stronger","Your site is an asset that works while you sleep","Stop paying and the rankings stay — you built something real"])}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">What We Build for {trade_plural}</span>
      <h2 class="serif" style="font-size:clamp(1.75rem,3vw,2.75rem);color:var(--text);max-width:600px;margin-bottom:1rem">Everything a {trade.lower()} company needs to dominate local search</h2>
      <p style="color:var(--text2);margin-bottom:3rem;max-width:560px;line-height:1.7">We have built our entire system around how {trade_plural.lower()} get found online. Every page we create, every keyword we target, every automation we configure is specific to your trade.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem">
      {features_html}
    </div>
  </div>
</section>

<section class="sec" style="background:#0D0D0D;border-top:1px solid rgba(255,255,255,.04)">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start" id="why-grid">
      <div class="reveal">
        <span class="eyebrow">Why LeadWise</span>
        <h2 class="serif" style="font-size:clamp(1.75rem,3vw,2.75rem);color:var(--text);margin-bottom:3rem">Why {trade_plural} choose us over a generalist agency</h2>
        <div style="display:flex;flex-direction:column;gap:1.5rem">
          {why_html}
        </div>
      </div>
      <div class="reveal">
        <div style="background:rgba(232,160,32,.05);border:1px solid rgba(232,160,32,.15);border-radius:1.5rem;padding:2.5rem">
          <span class="eyebrow">Free audit included</span>
          <h3 class="serif" style="font-size:1.75rem;color:var(--text);margin-bottom:1rem">{cta_line}</h3>
          <p style="color:var(--text2);line-height:1.7;margin-bottom:2rem;font-size:.95rem">We will audit your current website, Google rankings, and competitor landscape — then show you exactly what it would take to rank above them. No pitch. No pressure. Just data.</p>
          <a href="contact.html" class="btn-gold" style="width:100%;justify-content:center;font-size:1rem">Get My Free {trade} Audit <span class="icon-wrap">↗</span></a>
          <p style="font-size:.75rem;color:var(--text3);text-align:center;margin-top:1rem">Responds within 24 hours · No obligation</p>
        </div>
      </div>
    </div>
  </div>
</section>
""",
        extra_css="""
@keyframes pulse-gold{0%,100%{opacity:1}50%{opacity:.4}}
@media(max-width:768px){
  #hero-stats{grid-template-columns:1fr 1fr 1fr!important}
  #pain-grid,#why-grid{grid-template-columns:1fr!important;gap:2.5rem!important}
}
@media(max-width:480px){#hero-stats{grid-template-columns:1fr!important}}
"""
    )


# ─── TRADE DATA ──────────────────────────────────────────────────────
trades = [
    {
        "slug": "hvac-marketing",
        "trade": "HVAC",
        "trade_plural": "HVAC Companies",
        "keyword": "hvac marketing agency",
        "pain_point": "HVAC is one of the most competitive local markets online. If you are not on page one of Google, you are invisible during peak season when every homeowner is searching.",
        "pain_detail": "The average HVAC company spends $2,000–$5,000 per month on Angi and HomeAdvisor leads — and splits every one of those leads with four other contractors. You win maybe 20% of them. The math does not work. Meanwhile, the HVAC companies at the top of Google are getting exclusive inbound calls every single day without paying a per-lead tax.",
        "stat1_num": "87%", "stat1_label": "of HVAC customers start with Google search",
        "stat2_num": "34", "stat2_label": "Google reviews generated for our HVAC client",
        "stat3_num": "20+", "stat3_label": "city pages ranking in Tampa Bay",
        "specific_features": [
            ("HVAC service pages that rank", "Dedicated pages for AC repair, AC installation, heating repair, duct cleaning, and every other service you offer — each targeting the exact keywords homeowners search."),
            ("Seasonal SEO strategy", "We optimize your content and Google Business Profile around Florida's HVAC seasons — peak cooling season, pre-winter maintenance pushes, and emergency service keywords."),
            ("AI call answering — 24/7", "When a homeowner's AC goes out at 10pm, they call the first number they find. Our AI voice agent answers, qualifies the lead, and books the appointment before your competitor even wakes up."),
            ("Review generation system", "We took one HVAC client from 10 to 34 Google reviews in 6 months using automated post-job follow-up. More reviews means higher map pack rankings."),
            ("Emergency service SEO", "We target high-intent emergency searches like 'AC not working' and 'emergency HVAC repair' — the leads with the highest willingness to pay."),
            ("City coverage pages", "Dedicated location pages for every suburb and community in your service area, so you rank in Brandon, Riverview, Wesley Chapel — not just your primary city."),
        ],
        "why_items": [
            ("We only work with contractors", "We have never built a site for a dentist, a restaurant, or a SaaS company. Every SEO strategy we know is built around how homeowners search for HVAC service."),
            ("We built the North East HVAC playbook", "Our Tampa Bay HVAC client went from a generic GHL page to a 30+ page SEO site with 20+ city pages, a 5.0 star rating, and 34 Google reviews. That system is now our standard."),
            ("Speed to lead is built in", "HVAC emergencies do not wait. Our AI voice agents answer every call instantly, 24/7, so you never lose a job because nobody picked up."),
            ("No shared leads, ever", "Every customer that contacts you through your website is yours exclusively. No bidding wars. No competing with the other contractors on Angi's list."),
        ],
        "cta_line": "See exactly what it would take to rank #1 in your market."
    },
    {
        "slug": "plumber-marketing",
        "trade": "Plumbing",
        "trade_plural": "Plumbers",
        "keyword": "plumber marketing agency",
        "pain_point": "When a pipe bursts at midnight or a water heater fails before guests arrive, homeowners do not scroll through a lead platform — they Google and call the first result they trust.",
        "pain_detail": "Plumbing leads on Angi and HomeAdvisor routinely cost $80–$150 each — and get sent to multiple plumbers simultaneously. The homeowner gets bombarded with calls. You are competing on price and speed from the first second. Meanwhile, plumbers who own their Google rankings get exclusive calls from customers who already chose them before they even dialed.",
        "stat1_num": "3x", "stat1_label": "more calls from page-one Google vs. lead platforms",
        "stat2_num": "24/7", "stat2_label": "AI answers every call — even burst pipe emergencies at 2am",
        "stat3_num": "90%", "stat3_label": "of plumbing searches happen on mobile, in the moment",
        "specific_features": [
            ("Plumbing service pages that rank", "Individual pages for drain cleaning, water heater repair, leak detection, sewer line service, and every other service — each targeting exact search terms homeowners use."),
            ("Emergency plumbing SEO", "We target the highest-converting searches: 'emergency plumber near me,' 'burst pipe repair,' 'water heater not working' — keywords with immediate purchase intent."),
            ("AI call answering 24/7", "Plumbing emergencies happen at 2am on Sundays. Our AI answers every call, collects job details, and books the appointment — so you wake up with work already scheduled."),
            ("Google Business Profile domination", "We fully optimize your GBP so you appear in the map pack for every major plumbing search in your area. This alone can double your inbound call volume."),
            ("Review automation", "Automated post-job review requests sent at the perfect moment. More 5-star reviews means you rank higher and convert more visitors into calls."),
            ("City-by-city coverage", "Dedicated location pages for every suburb you serve, so you rank in every community — not just your primary city."),
        ],
        "why_items": [
            ("We speak plumber", "We know the difference between a water heater install and a tankless conversion, between a hydro-jet and a snake. Our content sounds like it was written by someone who understands your trade."),
            ("Emergency SEO is our specialty", "The most valuable plumbing leads are emergencies. We build content and site structure specifically to capture those high-intent, ready-to-pay searches."),
            ("Every lead is yours exclusively", "No platform taking a cut. No competing with three other plumbers on the same job. The customer found your site and called your number."),
            ("We track what matters", "Not impressions. Not clicks. Phone calls and booked jobs — the only metrics that grow your business."),
        ],
        "cta_line": "Find out why your competitors are ranking above you — and how to fix it."
    },
    {
        "slug": "roofing-marketing",
        "trade": "Roofing",
        "trade_plural": "Roofing Companies",
        "keyword": "roofing company marketing agency",
        "pain_point": "Roofing is a high-ticket, high-competition market. The companies winning the most jobs are not the ones spending the most on lead platforms — they are the ones who own page one of Google.",
        "pain_detail": "Storm season brings door-knockers and lead sellers flooding the market simultaneously. Angi roofing leads can cost $100–$300 each, get sold to multiple contractors, and convert at a fraction of organic leads. Homeowners who find you directly through Google already trust you enough to call — they did not get your number from a platform that sent them five other options first.",
        "stat1_num": "$12k+", "stat1_label": "average roofing job value — one organic lead pays for months of SEO",
        "stat2_num": "68%", "stat2_label": "of homeowners pick the first contractor they find on Google",
        "stat3_num": "5x", "stat3_label": "higher close rate on organic leads vs. shared platform leads",
        "specific_features": [
            ("Roofing service pages that rank", "Dedicated pages for roof replacement, roof repair, storm damage, flat roofing, gutters, and every service you offer — each built around the keywords homeowners and insurance adjusters search."),
            ("Storm damage SEO surge strategy", "When a major storm hits your market, we have a playbook ready to push your storm damage pages to the top of search results within 48 hours."),
            ("Insurance claim content", "We create content that educates homeowners on the insurance claim process and positions your company as the expert guide — the highest-converting roofing leads in the market."),
            ("AI call answering", "Every call answered instantly. Every lead qualified. Every appointment booked — even during the post-storm rush when your phone is ringing off the hook."),
            ("Reputation building system", "Roofing is a referral-heavy trade. Our automated review system turns every satisfied customer into a 5-star Google review that drives the next job."),
            ("City and neighborhood pages", "We build location pages targeting every community you serve, so you rank for 'roofing contractor [city]' searches across your entire market."),
        ],
        "why_items": [
            ("We understand the roofing sales cycle", "From the initial inspection through the insurance claim to the final walkthrough — we know how roofing jobs are won and we build your digital presence around that process."),
            ("Storm season ready", "We build your SEO foundation before storm season so when hail hits your market, you are already ranking — not scrambling to catch up."),
            ("High-ticket means high ROI", "One organic roofing lead that closes is worth $8,000–$25,000. The math on owning your rankings vs. renting leads is overwhelming."),
            ("No door-knockers, no lead brokers", "Your customers found your website, read about your company, and chose to call you. That is a completely different quality of lead."),
        ],
        "cta_line": "See how much revenue you are leaving on the table with your current online presence."
    },
    {
        "slug": "electrician-marketing",
        "trade": "Electrical",
        "trade_plural": "Electricians",
        "keyword": "electrician marketing agency",
        "pain_point": "Electrical work requires trust and licensing. When homeowners search for an electrician, they want someone credible — and Google is where that credibility is built.",
        "pain_detail": "Electricians who rely on Angi and Thumbtack compete on price against unlicensed handymen and out-of-area contractors. When you own your Google rankings, customers find your licensed, insured business first — and they are ready to pay a fair rate because they already trust what they have read about you.",
        "stat1_num": "76%", "stat1_label": "of electrical customers check Google reviews before calling",
        "stat2_num": "24/7", "stat2_label": "AI answers every call — panel upgrades booked while you sleep",
        "stat3_num": "10x", "stat3_label": "ROI on organic search vs. paid lead platforms for electricians",
        "specific_features": [
            ("Electrical service pages that rank", "Individual pages for panel upgrades, EV charger installation, whole-home rewiring, generator hookup, outlet repair — each targeting the exact searches homeowners and businesses use."),
            ("EV charger SEO opportunity", "EV charger installation is one of the fastest-growing electrical searches in the US. We get you ranking for these high-value, low-competition keywords before your competitors wake up to them."),
            ("Commercial electrical pages", "We build separate service pages targeting commercial clients — restaurants, offices, retail spaces — a completely different buyer with higher job values."),
            ("License and trust signals", "We build your site and Google Business Profile to showcase your licensing, insurance, and certifications prominently — the trust signals that convert browsers into callers."),
            ("AI call qualification", "Every call answered and qualified 24/7. The AI knows to ask about job type, urgency, and property type so you arrive to every call with context."),
            ("Neighborhood and city coverage", "Location pages for every community you serve, targeting searches like 'electrician in [suburb]' — lower competition, higher conversion."),
        ],
        "why_items": [
            ("We position your credentials, not just your services", "Licensing and insurance matter to homeowners. We build your site and content to make your credentials front and center — which directly increases call conversion rates."),
            ("EV charger installs are our specialty keyword", "This is a booming, underserved search category. We get electricians ranking for EV charger installation before the market gets saturated."),
            ("Commercial + residential covered", "We build separate SEO strategies for homeowner searches and commercial client searches — two different buyers, two different keyword sets, one agency."),
            ("No shared leads, ever", "The customer found your site, verified your credentials, and called your number. They are yours from the first contact."),
        ],
        "cta_line": "Find out which electrical keywords your competitors are ranking for — and you are not."
    },
    {
        "slug": "pest-control-marketing",
        "trade": "Pest Control",
        "trade_plural": "Pest Control Companies",
        "keyword": "pest control marketing agency",
        "pain_point": "Pest control has one of the highest repeat-customer rates of any home service — which means owning your Google rankings does not just get you one job, it gets you a customer for life.",
        "pain_detail": "Pest control leads from platforms like Angi are almost always one-time jobs shared with competitors. The real value in pest control is the recurring service contract — and those come from customers who found your company, trust your brand, and call you directly. You can not build that kind of relationship through a lead broker.",
        "stat1_num": "65%", "stat1_label": "of pest control customers convert to recurring service contracts",
        "stat2_num": "24/7", "stat2_label": "AI books termite inspections and service calls around the clock",
        "stat3_num": "$180+", "stat3_label": "average annual value of a single recurring pest control customer",
        "specific_features": [
            ("Pest-specific service pages", "Individual pages for termite treatment, rodent control, ant extermination, mosquito control, bed bug treatment — each targeting the exact pest searches in your market."),
            ("Seasonal pest SEO", "We time your content and Google Business Profile posts around local pest seasons — mosquito season, termite swarm season, rodent weather migrations — so you rank when demand spikes."),
            ("Recurring contract positioning", "We build your website to sell the value of a quarterly service plan, not just a one-time treatment — dramatically increasing your lifetime customer value."),
            ("Termite inspection SEO", "Termite inspections are one of the highest-value pest control entry points. We get you ranking for pre-purchase inspection searches in your market."),
            ("AI appointment booking", "Pest control customers want immediate relief. Our AI answers every call, explains your services, and books the inspection or treatment on the spot."),
            ("Local service area pages", "Coverage pages for every community you serve — because pest problems are hyper-local and your rankings should be too."),
        ],
        "why_items": [
            ("We understand recurring revenue", "We build your site to convert one-time callers into quarterly contract customers — the highest LTV play in pest control."),
            ("Seasonal timing built in", "Our content calendar is built around your local pest seasons, not a generic template. When termite swarms start, you are already ranking."),
            ("Trust signals matter in pest control", "Homeowners are letting you into their homes and around their families. We build your online presence to establish that trust before the first call."),
            ("No shared leads, no platform dependency", "Every customer who calls found your company directly and chose you before they dialed. That is a completely different quality relationship than a platform lead."),
        ],
        "cta_line": "See how many pest control customers in your area are going to your competitors."
    },
    {
        "slug": "landscaping-marketing",
        "trade": "Landscaping",
        "trade_plural": "Landscaping Companies",
        "keyword": "landscaping company marketing agency",
        "pain_point": "Landscaping is one of the most search-driven home services — homeowners are actively looking for someone they can trust with their property every single week. Are they finding you?",
        "pain_detail": "Lawn care and landscaping leads from platforms are cheap because the margins are thin and the competition is fierce. The landscaping companies that build sustainable, profitable businesses are the ones with steady inbound calls from homeowners who found them on Google, read their reviews, and called directly. That is a relationship built on trust — not a race to the bottom on price.",
        "stat1_num": "Weekly", "stat1_label": "recurring lawn care = predictable revenue all season",
        "stat2_num": "4x", "stat2_label": "higher LTV from direct customers vs. platform leads",
        "stat3_num": "24/7", "stat3_label": "AI books lawn care and landscaping estimates around the clock",
        "specific_features": [
            ("Landscaping service pages that rank", "Individual pages for lawn maintenance, landscape design, sod installation, irrigation, tree trimming, hardscaping — each targeting the searches homeowners in your market use."),
            ("Recurring service SEO strategy", "We build your site to attract and convert homeowners looking for a regular lawn care partner — not just a one-time cleanup. Recurring contracts are the foundation of a profitable landscaping business."),
            ("Before/after photo integration", "Landscaping is visual. We build your site to showcase project photos in a way that converts — and that Google rewards with higher rankings."),
            ("Seasonal service pushes", "Spring cleanups, fall leaf removal, holiday lighting — we time your content and GBP posts to capture seasonal demand spikes before your competitors do."),
            ("HOA and commercial landscaping pages", "We build separate pages targeting commercial properties and HOA contracts — the highest-value landscaping clients in your market."),
            ("Local area coverage pages", "Neighborhood-level location pages so you rank for 'lawn service in [neighborhood]' — some of the most valuable, lowest-competition keywords in landscaping."),
        ],
        "why_items": [
            ("We understand the landscaping sales cycle", "From the initial estimate to the recurring weekly contract — we know how landscaping customers are won and we build your digital presence around it."),
            ("Recurring revenue is the goal", "We do not just help you get calls — we help you get the right calls. Homeowners looking for a long-term lawn care partner, not a one-time deal."),
            ("Visual trade, visual strategy", "Landscaping sells itself when the photos are right. We build your site to showcase your work in a way that converts visitors into callers."),
            ("No shared leads, ever", "Every customer who contacts you found your business directly. No competing bids sent simultaneously. They chose you before they called."),
        ],
        "cta_line": "Find out which landscaping keywords your competitors are ranking for in your market."
    },
    {
        "slug": "painting-contractor-marketing",
        "trade": "Painting",
        "trade_plural": "Painting Contractors",
        "keyword": "painting contractor marketing agency",
        "pain_point": "Painting is a trust-based trade — homeowners are letting you into their home and around their belongings. The companies that win the most jobs are the ones who build that trust online before the first call.",
        "pain_detail": "Painting leads from platforms put you in a bidding war with low-cost competitors who cut corners. Homeowners who find you through Google — who read your reviews, see your project photos, and learn about your process — are pre-sold before they call. They are not asking 'how cheap can you do it.' They are asking 'when can you start.'",
        "stat1_num": "89%", "stat1_label": "of painting customers get multiple quotes — yours needs to stand out",
        "stat2_num": "5-star", "stat2_label": "review profiles convert 3x better than competitors with fewer reviews",
        "stat3_num": "24/7", "stat3_label": "AI books painting estimates while you are on a job",
        "specific_features": [
            ("Painting service pages that rank", "Individual pages for interior painting, exterior painting, cabinet refinishing, deck staining, commercial painting — each targeting exact search terms homeowners use."),
            ("Project photo gallery optimization", "We build your gallery pages to rank for searches like 'interior painting [city]' — because homeowners researching painters want to see the work first."),
            ("Review generation system", "Painting customers are highly likely to leave reviews when asked the right way at the right time. Our automated system captures those reviews consistently."),
            ("Commercial painting pages", "Office buildings, retail spaces, and property managers are a completely different buyer with larger job values. We build separate pages targeting commercial painting work."),
            ("Cabinet refinishing SEO", "One of the fastest-growing painting searches. We get you ranking for this high-value, lower-competition service before the market saturates."),
            ("Neighborhood coverage pages", "Location pages for every community you serve — because painting searches are intensely local and hyper-specific to neighborhood demographics."),
        ],
        "why_items": [
            ("We sell trust, not just services", "Painting is chosen on trust and aesthetics — not price. We build your online presence to convey professionalism, quality, and reliability before the first conversation."),
            ("Photo-first strategy", "We know painting sells visually. Your site is built to showcase your best work in a way that converts browsers into booked estimates."),
            ("Cabinet refinishing is our specialty keyword", "This underserved search category converts at a premium rate. We position your painting company to capture it."),
            ("No platform dependency", "When you own your Google rankings, you are never at the mercy of a platform's pricing changes or algorithm updates. Your leads are yours."),
        ],
        "cta_line": "See what it would take for your painting company to rank #1 in your area."
    },
    {
        "slug": "general-contractor-marketing",
        "trade": "General Contractor",
        "trade_plural": "General Contractors",
        "keyword": "general contractor marketing agency",
        "pain_point": "General contracting projects are some of the highest-value home service jobs on the market. The GCs winning the most bids are not on Angi — they are on page one of Google.",
        "pain_detail": "General contractor leads from platforms are notoriously low-quality — homeowners looking for the cheapest bid on a project that may or may not happen. The GCs with the strongest pipelines get their leads from homeowners who found them on Google, researched their work, and reached out ready to move forward. That is a completely different quality of opportunity.",
        "stat1_num": "$25k+", "stat1_label": "average general contracting project value — one organic lead is priceless",
        "stat2_num": "72%", "stat2_label": "of homeowners research contractors online before making contact",
        "stat3_num": "24/7", "stat3_label": "AI qualifies project leads and books consultations around the clock",
        "specific_features": [
            ("Project-type service pages", "Individual pages for kitchen remodels, bathroom renovations, home additions, ADUs, whole-home renovation — each targeting the searches homeowners use when they are ready to hire."),
            ("Portfolio and project showcase", "We build your project gallery to rank for searches like 'kitchen remodel [city]' — because homeowners researching GCs want to see your best work first."),
            ("High-value keyword targeting", "We focus on searches with high project intent: 'home addition contractor,' 'ADU builder,' 'whole home renovation' — the keywords that attract serious buyers, not tire-kickers."),
            ("Commercial and residential split", "If you do both commercial and residential work, we build separate SEO strategies for each — completely different buyers, different keywords, different content."),
            ("AI consultation booking", "GC projects start with a consultation. Our AI answers every inquiry, collects project details, and books the site visit directly into your calendar."),
            ("Submarket targeting", "We build your site to rank in the specific neighborhoods and communities where your highest-value projects come from — not just a generic city-level presence."),
        ],
        "why_items": [
            ("We understand long sales cycles", "GC projects take weeks or months from first contact to signed contract. We build your content to nurture trust throughout that process."),
            ("Portfolio is everything", "We know GC work is sold on past projects. Your site is built to showcase your portfolio in a way that builds confidence and converts."),
            ("High-value clients require high-trust websites", "A homeowner considering a $50,000 renovation is not hiring from a platform. They are vetting your online presence carefully. We make sure it holds up."),
            ("No shared leads, no price wars", "Customers who find you through your website reach out because they want to work with you specifically — not because a platform sent them five options."),
        ],
        "cta_line": "Find out what your GC website is costing you in lost project opportunities."
    },
]

for t in trades:
    write(f"{t['slug']}.html", trade_page(**t))

print(f"\n{len(trades)} trade pages built!")

# ─── COMPARISON PAGE ─────────────────────────────────────────────────
comparison = page(
    "Why Contractors Are Ditching Angi & HomeAdvisor | LeadWise Connect",
    "Angi and HomeAdvisor sell your leads to 5 competitors at $100–$200 each. There is a better way. See why local contractors are switching to owning their Google rankings.",
    "/vs-angi-homeadvisor.html",
    f"""
<section class="page-hero" style="background:radial-gradient(ellipse 60% 50% at 50% -10%,rgba(232,160,32,.12) 0%,transparent 70%);position:relative;overflow:hidden">
  <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.015) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.015) 1px,transparent 1px);background-size:80px 80px;pointer-events:none"></div>
  <div class="container" style="position:relative;z-index:1">
    <div style="display:inline-flex;align-items:center;gap:.5rem;background:rgba(248,113,113,.1);border:1px solid rgba(248,113,113,.2);border-radius:9999px;padding:.35rem .85rem;margin-bottom:1.5rem" class="fadein">
      <span style="font-size:.7rem;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:#F87171">The Truth About Lead Platforms</span>
    </div>
    <h1 class="serif fadein d1" style="font-size:clamp(2.75rem,6vw,5rem);color:var(--text);line-height:1;max-width:900px;margin-bottom:1.75rem">
      Angi and HomeAdvisor<br>are <span style="background:linear-gradient(135deg,#F5C060 0%,#E8A020 50%,#B87818 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">not on your side.</span>
    </h1>
    <p class="fadein d2" style="font-size:clamp(1rem,2vw,1.2rem);color:var(--text2);max-width:600px;line-height:1.75;margin-bottom:2.5rem">They charge you $50–$200 per lead. They sell that same lead to 4 other contractors. You compete on price. You win maybe 20%. And the moment you stop paying, the phone goes silent. There is a better model — and it is called owning your Google rankings.</p>
    <div class="fadein d3" style="display:flex;flex-wrap:wrap;gap:1rem">
      <a href="contact.html" class="btn-gold" style="font-size:1rem;padding:1rem 2rem">Get Off the Lead Treadmill <span class="icon-wrap">↗</span></a>
      <a href="results.html" class="btn-ghost" style="font-size:1rem;padding:1rem 2rem">See What We Build</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="container">
    <div class="reveal" style="max-width:760px;margin:0 auto;text-align:center;margin-bottom:5rem">
      <span class="eyebrow" style="display:block;text-align:center">The Real Math</span>
      <h2 class="serif" style="font-size:clamp(2rem,3.5vw,3rem);color:var(--text);margin-bottom:1.5rem">What you are actually paying for</h2>
      <p style="color:var(--text2);line-height:1.8;font-size:1.05rem">A contractor spending $2,000/month on Angi leads gets roughly 15–20 leads. At a 20% close rate, that is 3–4 jobs. At $400 average job value, you barely break even — and you built nothing. No rankings. No reviews from the platform. Nothing that compounds.</p>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:5rem" id="compare-grid">
      <div style="background:var(--surface);border:1px solid rgba(248,113,113,.2);border-radius:1.5rem;padding:2.5rem">
        <p style="font-size:1.1rem;font-weight:700;color:#F87171;margin-bottom:2rem;padding-bottom:1rem;border-bottom:1px solid rgba(248,113,113,.15)">❌ Angi / HomeAdvisor / Thumbtack</p>
        <div style="display:flex;flex-direction:column;gap:1.25rem">
          {f''.join(f'<div style="display:flex;align-items:flex-start;gap:.75rem"><div style="width:20px;height:20px;border-radius:50%;background:rgba(248,113,113,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.7rem;color:#F87171;margin-top:.1rem">✕</div><div><p style="font-weight:600;color:var(--text);font-size:.9rem;margin-bottom:.2rem">{x[0]}</p><p style="color:var(--text2);font-size:.82rem;line-height:1.5">{x[1]}</p></div></div>' for x in [
            ("Shared leads sent to 4–5 competitors", "The homeowner gets bombarded with calls the moment they submit. You are competing from second one."),
            ("$50–$200 per lead, every single time", "No matter if the job is $300 or $30,000 — you pay the same lead fee. The math rarely works in your favor."),
            ("Zero brand equity built", "Customers remember Angi. They do not remember you. You are just another contractor on a list."),
            ("Platform controls your pricing power", "When Angi raises rates — and they always do — you either pay more or lose access. You have zero leverage."),
            ("Leads stop the moment you pause", "Cancel your account and the phone goes silent. You built nothing. No rankings. No reviews that stick. Just expenses."),
            ("Lead quality is notoriously inconsistent", "Tire-kickers, wrong service area, price shoppers, people who submitted to 10 contractors — all mixed in with real buyers."),
          ])}
        </div>
      </div>
      <div style="background:rgba(232,160,32,.04);border:1px solid rgba(232,160,32,.2);border-radius:1.5rem;padding:2.5rem">
        <p style="font-size:1.1rem;font-weight:700;color:var(--gold);margin-bottom:2rem;padding-bottom:1rem;border-bottom:1px solid rgba(232,160,32,.15)">✓ LeadWise: Own Your Google Rankings</p>
        <div style="display:flex;flex-direction:column;gap:1.25rem">
          {f''.join(f'<div style="display:flex;align-items:flex-start;gap:.75rem"><div style="width:20px;height:20px;border-radius:50%;background:rgba(232,160,32,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:.7rem;color:var(--gold);margin-top:.1rem">✓</div><div><p style="font-weight:600;color:var(--text);font-size:.9rem;margin-bottom:.2rem">{x[0]}</p><p style="color:var(--text2);font-size:.82rem;line-height:1.5">{x[1]}</p></div></div>' for x in [
            ("Exclusive leads — they called you directly", "The customer found your website, read your reviews, and chose to call your number. No competition."),
            ("No per-lead fees — ever", "You own the rankings. Every call that comes in costs you nothing beyond your monthly investment."),
            ("Every month builds your brand", "Reviews compound. Rankings improve. Your name becomes the one homeowners recognize and trust in your market."),
            ("You own the asset forever", "Your Google rankings and reviews cannot be taken away. Stop paying a platform and your rankings stay."),
            ("Rankings compound over time", "The longer your site ranks, the more authority it builds. Month 12 performs better than month 1 — the opposite of a lead platform."),
            ("Pre-qualified, high-intent leads", "Someone who finds your website through Google, reads your reviews, and then calls you is already 80% sold before the conversation starts."),
          ])}
        </div>
      </div>
    </div>

    <div class="reveal" style="background:var(--surface);border:1px solid rgba(255,255,255,.08);border-radius:1.5rem;padding:3rem;margin-bottom:5rem">
      <h2 class="serif" style="font-size:clamp(1.5rem,2.5vw,2.25rem);color:var(--text);margin-bottom:2rem;text-align:center">The 12-month comparison</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;background:rgba(255,255,255,.06);border-radius:1rem;overflow:hidden" id="table-grid">
        {"".join(f'<div style="background:var(--surface);padding:1.25rem;text-align:center"><p style="font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--text3)">{h}</p></div>' for h in ["","Angi / HomeAdvisor","LeadWise (own your rankings)"])}
        {"".join(f'<div style="background:#0D0D0D;padding:1.25rem;text-align:center"><p style="font-weight:600;color:var(--text);font-size:.875rem">{r[0]}</p></div><div style="background:#0D0D0D;padding:1.25rem;text-align:center"><p style="color:#F87171;font-size:.875rem">{r[1]}</p></div><div style="background:#0D0D0D;padding:1.25rem;text-align:center"><p style="color:var(--gold);font-size:.875rem">{r[2]}</p></div>' for r in [
            ("Monthly cost", "$2,000–$5,000", "$1,000–$2,500"),
            ("Lead exclusivity", "Shared with 4–5 competitors", "100% exclusive"),
            ("Brand building", "None", "Compounds monthly"),
            ("Close rate", "15–25%", "40–60%"),
            ("Asset value at month 12", "$0 — you built nothing", "Established rankings + reviews"),
            ("What happens if you pause", "Phone goes silent immediately", "Rankings remain — you own them"),
        ])}
      </div>
    </div>

    <div class="reveal" style="max-width:760px;margin:0 auto;text-align:center">
      <span class="eyebrow" style="display:block;text-align:center">Ready to get off the treadmill?</span>
      <h2 class="serif" style="font-size:clamp(2rem,3.5vw,3rem);color:var(--text);margin-bottom:1.5rem">Let&apos;s build something you actually own.</h2>
      <p style="color:var(--text2);line-height:1.8;margin-bottom:2.5rem;font-size:1.05rem">We will audit your current online presence and show you exactly what it would cost to own your Google rankings instead of renting leads forever. No obligation. No pitch. Just the honest picture.</p>
      <a href="contact.html" class="btn-gold" style="font-size:1.1rem;padding:1.1rem 2.5rem">Get My Free Audit <span class="icon-wrap">↗</span></a>
      <p style="color:var(--text3);font-size:.8rem;margin-top:1.25rem">Responds within 24 hours · No contracts required</p>
    </div>
  </div>
</section>
""",
    extra_css="@media(max-width:768px){#compare-grid,#table-grid{grid-template-columns:1fr!important}}"
)
write("vs-angi-homeadvisor.html", comparison)
print("Comparison page done!")
