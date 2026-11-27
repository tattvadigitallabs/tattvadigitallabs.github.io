import os, sys
root = sys.argv[1]
EMAIL = 'support.tattvadigitallabs@gmail.com'
MARK = '<img class="mark-img" src="/assets/brand/tattva-mark.svg" alt="" width="34" height="34">'
APP_ICON = '/assets/brand/image-compressor-icon.svg'
FINANCE_ICON = '/assets/brand/finance-calculator-icon.svg'
PDF_ICON = '/assets/brand/pdf-tools-icon.svg'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>'
PLAY = '<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path fill="#0f6e6a" d="M4.2 2.6c-.13.15-.2.37-.2.65v17.5c0 .28.07.5.2.65l.04.04L14 11.7v-.2L4.24 2.56z"/><path fill="#14b8a6" d="M17.3 15l-3.3-3.3v-.2l3.3-3.3.07.04 3.9 2.22c1.12.63 1.12 1.67 0 2.3l-3.9 2.22z"/><path fill="#0b5a57" d="M17.37 14.96L14 11.6 4.2 21.4c.36.38.96.43 1.64.04l11.53-6.48"/><path fill="#2dd4bf" d="M17.37 8.24L5.84 1.76C5.16 1.37 4.56 1.42 4.2 1.8L14 11.6z"/></svg>'
ICONS = {
 'lock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 'offline': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 2l20 20"/><path d="M8.5 16.5a5 5 0 0 1 7 0M5 13a10 10 0 0 1 5.2-2.8M19 13a10 10 0 0 0-2-1.5M12 20h.01"/></svg>',
 'spark': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.2 5.6L20 11l-5.8 2.4L12 19l-2.2-5.6L4 11l5.8-2.4z"/></svg>',
 'noads': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/></svg>',
}

def head(title, desc, extra_css='', current='', og='/assets/img/og.png'):
    def nav(href, label, key, cls=''):
        cur = ' aria-current="page"' if key == current else ''
        c = f' class="{cls}"' if cls else ''
        return f'<a href="{href}"{cur}{c}>{label}</a>'
    return f'''<!doctype html>
<html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<meta name="theme-color" content="#061010">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="https://tattvadigitallabs.github.io{og}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">{extra_css}
</head><body>
<header class="nav"><div class="wrap">
<a class="brand" href="/">{MARK}<span class="name">Tattva Digital Labs</span></a>
<nav>{nav("/#apps","Apps","apps","hide-sm")}{nav("/privacy/","Privacy","privacy")}{nav("/support/","Support","support")}</nav>
</div></header>
'''

FOOT = f'''<footer class="foot"><div class="wrap">
<a class="brand" href="/">{MARK}<span>Tattva Digital Labs</span></a>
<span><a href="/#apps">Apps</a> &nbsp;·&nbsp; <a href="/privacy/">Privacy</a> &nbsp;·&nbsp; <a href="/support/">Support</a> &nbsp;·&nbsp; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
<span>© 2026 Tattva Digital Labs</span>
</div></footer>
<script src="/assets/site.js" defer></script>
</body></html>
'''

def device(src, alt, cls=''):
    c = f'device {cls}'.strip()
    return f'<div class="{c}"><img src="/assets/img/{src}.jpg" alt="{alt}" loading="lazy" width="450" height="1000"></div>'

HOME_CSS = '<link rel="stylesheet" href="/assets/home.css">'

# ---------------- Company home ----------------
home = head("Tattva Digital Labs: simple apps that respect your privacy",
            "Tattva Digital Labs builds simple, beautifully crafted apps that work offline and never collect your data.",
            HOME_CSS) + f'''
<section class="band hero co-hero"><div class="wrap">
  <img class="big-mark reveal" src="/assets/brand/tattva-mark.svg" alt="Tattva Digital Labs" width="84" height="84">
  <div class="reveal">
    <h1>Simple tools. <em>Serious about privacy.</em></h1>
    <p class="lead">Tattva Digital Labs builds focused, beautifully crafted apps that do one job brilliantly, work offline, and never collect your data.</p>
    <div class="cta"><a class="btn btn-store" href="#apps"><span><small>Explore</small><b>Our apps</b></span></a><a class="btn btn-ghost" href="/privacy/">Our privacy promise</a></div>
  </div>
</div></section>

<div class="wrap">
  <div class="proof values reveal"><div class="grid">
    <div class="cell"><span class="ico">{ICONS["lock"]}</span><b>Private by design</b><span>Your data stays on your device.</span></div>
    <div class="cell"><span class="ico">{ICONS["offline"]}</span><b>Offline-first</b><span>Works anywhere, no signal needed.</span></div>
    <div class="cell"><span class="ico">{ICONS["noads"]}</span><b>No ads, no tracking</b><span>No analytics, no third-party SDKs.</span></div>
    <div class="cell"><span class="ico">{ICONS["spark"]}</span><b>Crafted with care</b><span>Fast, focused and delightful to use.</span></div>
  </div></div>

  <section class="products" id="apps">
    <div class="head"><span class="kicker reveal">Our apps</span><h2 class="reveal">Made to do one thing really well</h2></div>
    <article class="prod-card reveal">
      <div>
        <img class="icon" src="{APP_ICON}" alt="Tattva Image Compressor icon" width="72" height="72">
        <h3>Tattva Image Compressor</h3>
        <p>Compress photos to the exact size you need, like 200&nbsp;KB for forms, exam and job portals, with the best quality that fits. Entirely offline.</p>
        <div class="tags"><span>Exact-size compression</span><span>Batch of 50</span><span>Before/after compare</span><span>Android</span></div>
        <div class="actions"><a class="btn btn-dark" href="/image-compressor/">Learn more →</a><span class="status">Coming soon on Google Play</span></div>
      </div>
      <div class="shots">{device("target","Compress to a target size")}{device("target-results","Results under the limit")}</div>
    </article>
    <article class="prod-card reveal">
      <div>
        <img class="icon" src="{FINANCE_ICON}" alt="Tattva Finance Calculator icon" width="72" height="72">
        <h3>Tattva Finance Calculator</h3>
        <p>EMI, SIP, income tax, FD, PPF, GST and more, with every result explained: the method, the assumptions, and what the number means for you. Entirely offline.</p>
        <div class="tags"><span>Calculation Passport</span><span>What-if scenarios</span><span>13 calculators</span><span>Android</span></div>
        <div class="actions"><a class="btn btn-dark" href="/finance-calculator/">Learn more →</a><span class="status">Coming soon on Google Play</span></div>
      </div>
      <div class="shots">{device("finance-emi","EMI result")}{device("finance-passport","Calculation Passport")}</div>
    </article>
    <div class="next-card reveal"><b>More on the way</b>We're working on new tools built the same way: simple, private, offline.</div>
  </section>
</div>

<section class="band trust reveal"><div class="wrap">
  <div>
    <span class="kicker">Our promise</span>
    <h2>We don't want your data.</h2>
    <p>Our apps are designed to work without collecting anything about you. No accounts, no ads, no trackers. Each app's privacy details are on our <a href="/privacy/">privacy page</a>.</p>
  </div>
  <div class="tiles">
    <div class="tile"><b>On-device</b><span>Processing happens on your phone</span></div>
    <div class="tile"><b>No accounts</b><span>Nothing to sign up for</span></div>
    <div class="tile"><b>No ads or trackers</b><span>Zero data sold or shared</span></div>
    <div class="tile"><b>Transparent</b><span>Plain-language privacy policies</span></div>
  </div>
</div></section>

<section class="band final reveal"><div class="wrap">
  <h2>Say hello</h2>
  <p>Questions, feedback or ideas for what we should build next? We read every message.</p>
  <div class="cta"><a class="btn btn-store" href="mailto:{EMAIL}"><span><small>Write to us</small><b>{EMAIL}</b></span></a></div>
</div></section>
''' + FOOT

# ---------------- Product: Image Compressor ----------------
product = head("Tattva Image Compressor: compress photos to an exact size",
               "Compress photos to an exact size like 200 KB for forms, exam and job portals. Fully offline, no ads, no tracking. Your photos never leave your phone.",
               HOME_CSS, 'apps') + f'''
<section class="band hero"><div class="wrap">
  <div class="reveal">
    <span class="app-eyebrow"><img src="{APP_ICON}" alt="" width="28" height="28">Tattva Image Compressor · Android</span>
    <h1>Exactly the size you need. <em>None of the blur.</em></h1>
    <p class="lead">Need a photo under 200&nbsp;KB for a form, exam or job portal? Type the limit and get the sharpest image that fits, in seconds, entirely on your phone.</p>
    <ul class="assure">
      <li>{CHECK} Works 100% offline</li><li>{CHECK} No ads, no tracking</li><li>{CHECK} Originals never touched</li>
    </ul>
    <div class="cta">
      <span class="btn btn-store">{PLAY}<span><small>Coming soon on</small><b>Google Play</b></span></span>
      <a class="btn btn-ghost" href="#features">See how it works</a>
    </div>
  </div>
  <div class="stage reveal" aria-hidden="true">
    {device("home","","d1")}
    {device("target-results","","d2")}
    <div class="float f1">20.7 MB → 96 KB<span>99% smaller</span></div>
    <div class="float f2"><b>✓</b> Under 100 KB<span>Guaranteed, every time</span></div>
  </div>
</div></section>

<div class="wrap">
  <div class="proof reveal"><div class="grid">
    <div class="cell"><b>Up to 99%</b><span>smaller files</span></div>
    <div class="cell"><b>Always</b><span>under your limit</span></div>
    <div class="cell"><b>50 photos</b><span>in one batch</span></div>
    <div class="cell"><b>0 bytes</b><span>ever uploaded</span></div>
  </div></div>

  <section class="feature" id="features">
    <div class="copy reveal">
      <span class="kicker">Compress to exact size</span>
      <h2>Type a limit. Get a photo that fits, and still looks great.</h2>
      <p>Portals reject photos that are too big. Tattva searches for the highest quality that stays under your limit, and when space is tight it reduces pixels instead of turning your photo to mush.</p>
      <div class="sizes"><span>20 KB</span><span>50 KB</span><span>100 KB</span><span class="on">200 KB</span><span>500 KB</span><span>1 MB</span><span>Any size</span></div>
      <ul class="ticks"><li>Every image guaranteed under your limit</li><li>One photo or a whole batch</li><li>Location data removed automatically</li></ul>
    </div>
    <div class="pair reveal">{device("target","Choosing a target size")}{device("target-results","All images under 100 KB")}</div>
  </section>

  <section class="feature rev">
    <div class="copy reveal">
      <span class="kicker">Pixel-perfect comparison</span>
      <h2>See exactly what changed, before you save.</h2>
      <p>Slide between original and compressed, flip side by side, and zoom in at full resolution. Quality you can verify, not just trust.</p>
      <ul class="ticks"><li>Drag or tap anywhere to compare</li><li>Double-tap or pinch for full-resolution detail</li><li>Exact size and savings for every photo</li></ul>
    </div>
    <div class="pair reveal">{device("compare","Before and after slider")}{device("compare-zoom","Zoomed comparison at full resolution")}</div>
  </section>

  <section class="feature">
    <div class="copy reveal">
      <span class="kicker">Batch in the background</span>
      <h2>Free up gigabytes in one go.</h2>
      <p>Pick up to 50 photos and compress them together. Switch apps if you like; it keeps working and shows progress.</p>
      <ul class="ticks"><li>Light, Balanced, Strong or your own quality</li><li>JPEG, WebP or PNG, with optional resize</li><li>Save to your gallery or share to WhatsApp in one tap</li></ul>
    </div>
    <div class="pair reveal">{device("home","Home screen")}{device("batch","Batch results showing space saved")}</div>
  </section>

  <section class="how">
    <span class="kicker reveal">Effortless</span>
    <h2 class="reveal">Three taps. Done.</h2>
    <p class="muted reveal">No sign-up. No settings to learn.</p>
    <div class="steps">
      <div class="step reveal"><span class="n">STEP 01</span><h3>Pick your photos</h3><p>Choose from your gallery, or share from any app and tap “Compress with Tattva”.</p></div>
      <div class="step reveal"><span class="n">STEP 02</span><h3>Set size or quality</h3><p>Enter a limit like 200&nbsp;KB, or choose Light, Balanced or Strong.</p></div>
      <div class="step reveal"><span class="n">STEP 03</span><h3>Save or share</h3><p>Check before and after, then save to your gallery or share anywhere.</p></div>
    </div>
  </section>
</div>

<section class="band trust reveal"><div class="wrap">
  <div>
    <span class="kicker">Private by design</span>
    <h2>Your photos never leave your phone.</h2>
    <p>Tattva Image Compressor has no internet permission. It physically cannot upload anything. <a href="/privacy/#image-compressor">Read its privacy details</a>.</p>
  </div>
  <div class="tiles">
    <div class="tile"><b>No internet</b><span>Every step runs offline</span></div>
    <div class="tile"><b>No accounts</b><span>Nothing to sign up for</span></div>
    <div class="tile"><b>No ads or trackers</b><span>Zero data collected</span></div>
    <div class="tile"><b>Originals safe</b><span>Never changed or deleted</span></div>
  </div>
</div></section>

<div class="wrap">
  <section class="gallery-sec">
    <span class="kicker reveal">Crafted with care</span>
    <h2 class="reveal">A closer look</h2>
    <div class="gallery">
      <figure>{device("onboarding","Welcome screen")}<figcaption>A calm, simple start</figcaption></figure>
      <figure>{device("target","Compress to size")}<figcaption>Exact-size control</figcaption></figure>
      <figure>{device("compare-zoom","Zoomed comparison")}<figcaption>Full-resolution compare</figcaption></figure>
      <figure>{device("history","History")}<figcaption>Your savings, tracked</figcaption></figure>
      <figure>{device("dark","Dark mode")}<figcaption>Beautiful in the dark</figcaption></figure>
    </div>
  </section>
</div>

<section class="band final reveal"><div class="wrap">
  <h2>Coming soon to Google Play</h2>
  <p>Want early access or have a question? We'd love to hear from you.</p>
  <div class="cta"><a class="btn btn-store" href="mailto:{EMAIL}?subject=Early%20access%20-%20Tattva%20Image%20Compressor"><span><small>Get early access</small><b>Email us</b></span></a></div>
</div></section>
''' + FOOT

# ---------------- Product: Finance Calculator ----------------
finance = head("Tattva Finance Calculator: every money calculation, clearly explained",
               "EMI, SIP, income tax, FD, PPF, GST and more. Every result comes with its method, assumptions and meaning. Fully offline, no ads, no sign-up.",
               HOME_CSS, 'apps', og='/assets/img/finance-og.png') + f'''
<section class="band hero"><div class="wrap">
  <div class="reveal">
    <span class="app-eyebrow"><img src="{FINANCE_ICON}" alt="" width="28" height="28">Tattva Finance Calculator · Android</span>
    <h1>Not just the number. <em>What it means.</em></h1>
    <p class="lead">Most calculators give you an EMI and stop. Tattva shows how it was worked out, what was assumed, where your money goes, and what changes if you prepay, switch regime or pick another offer.</p>
    <ul class="assure">
      <li>{CHECK} Works 100% offline</li><li>{CHECK} No ads, no sign-up</li><li>{CHECK} Every result explained</li>
    </ul>
    <div class="cta">
      <span class="btn btn-store">{PLAY}<span><small>Coming soon on</small><b>Google Play</b></span></span>
      <a class="btn btn-ghost" href="#features">See how it works</a>
    </div>
  </div>
  <div class="stage reveal" aria-hidden="true">
    {device("finance-emi","","d1")}
    {device("finance-whatif","","d2")}
    <div class="float f1">₹18.55 lakh less<span>interest, by prepaying ₹1 lakh a year</span></div>
    <div class="float f2"><b>✓</b> 6 years sooner<span>loan paid off in 14 years</span></div>
  </div>
</div></section>

<div class="wrap">
  <div class="proof reveal"><div class="grid">
    <div class="cell"><b>13</b><span>everyday calculators</span></div>
    <div class="cell"><b>Every</b><span>result explained</span></div>
    <div class="cell"><b>₹50L</b><span>or just type 50L</span></div>
    <div class="cell"><b>0 bytes</b><span>ever uploaded</span></div>
  </div></div>

  <section class="feature" id="features">
    <div class="copy reveal">
      <span class="kicker">Calculation Passport</span>
      <h2>Know where every number comes from.</h2>
      <p>Tap “Understand this” on any result to see your inputs, the method and formula with your numbers in it, how the total divides, every assumption, and why your bank's figure might differ.</p>
      <ul class="ticks"><li>Breakdowns that always add up exactly</li><li>Year-by-year schedule and growth</li><li>Plain words, not jargon</li></ul>
    </div>
    <div class="pair reveal">{device("finance-passport","Calculation Passport: inputs and method")}{device("finance-meaning","Assumptions and what it means")}</div>
  </section>

  <section class="feature rev">
    <div class="copy reveal">
      <span class="kicker">What if?</span>
      <h2>See the effect of a decision before you make it.</h2>
      <p>Prepay a lakh a year, pay a little more each month, step up your SIP, or use your full 80C. One tap shows the difference in rupees and years, and your original stays untouched.</p>
      <ul class="ticks"><li>Ready-made scenarios for every calculator</li><li>Changes spelled out: “₹18.55 lakh less interest”</li><li>Save the scenario you like</li></ul>
    </div>
    <div class="pair reveal">{device("finance-whatif","What-if comparison")}{device("finance-compare","Comparing two loan offers")}</div>
  </section>

  <section class="feature">
    <div class="copy reveal">
      <span class="kicker">Made for India</span>
      <h2>Type money the way you say it.</h2>
      <p>Enter 50L, 1.25&nbsp;Cr or 45k, or tap ×Lakh on the number pad. Amounts appear as ₹50,00,000 with lakh and crore in words, everywhere.</p>
      <ul class="ticks"><li>Income tax for FY 2026-27, new vs old regime</li><li>PPF and Sukanya Samriddhi at current government rates</li><li>GST with CGST/SGST or IGST split</li></ul>
    </div>
    <div class="pair reveal">{device("finance-input","Typing 75 lakh with the Lakh button")}{device("finance-tax","New vs old tax regime")}</div>
  </section>

  <section class="how">
    <span class="kicker reveal">Every calculator you need</span>
    <h2 class="reveal">One calm app, thirteen tools.</h2>
    <p class="muted reveal">Loans: EMI, loan eligibility, compare offers · Investments: SIP, lumpsum, goal planner · Deposits: FD, RD · Schemes: PPF, Sukanya Samriddhi · Tax: income tax, GST · Everyday: simple &amp; compound interest</p>
    <div class="steps">
      <div class="step reveal"><span class="n">STEP 01</span><h3>Pick a calculator</h3><p>Popular ones are on the home screen. Search understands “home loan”, “sukanya” or “80c”.</p></div>
      <div class="step reveal"><span class="n">STEP 02</span><h3>Enter your numbers</h3><p>Results update as you type. Mistakes get a helpful hint, like “did you mean 8.5%?”.</p></div>
      <div class="step reveal"><span class="n">STEP 03</span><h3>Understand, explore, share</h3><p>Open the Passport, try a What-if, save it, or share a clean summary card.</p></div>
    </div>
  </section>
</div>

<section class="band trust reveal"><div class="wrap">
  <div>
    <span class="kicker">Private by design</span>
    <h2>Your numbers never leave your phone.</h2>
    <p>Tattva Finance Calculator has no internet permission. It cannot upload your salary, loans or savings, and it has no ads or trackers. <a href="/privacy/#finance-calculator">Read its privacy details</a>.</p>
  </div>
  <div class="tiles">
    <div class="tile"><b>No internet</b><span>Every calculation runs offline</span></div>
    <div class="tile"><b>No accounts</b><span>Nothing to sign up for</span></div>
    <div class="tile"><b>No ads or trackers</b><span>Zero data collected</span></div>
    <div class="tile"><b>Not advice</b><span>Clear estimates, honest assumptions</span></div>
  </div>
</div></section>

<div class="wrap">
  <section class="gallery-sec">
    <span class="kicker reveal">Crafted with care</span>
    <h2 class="reveal">A closer look</h2>
    <div class="gallery">
      <figure>{device("finance-home","Home screen")}<figcaption>Everything in one place</figcaption></figure>
      <figure>{device("finance-tax","Income tax")}<figcaption>New vs old regime</figcaption></figure>
      <figure>{device("finance-compare","Compare offers")}<figcaption>Fees included, honestly</figcaption></figure>
      <figure>{device("finance-goal","Goal planner")}<figcaption>Goals with inflation</figcaption></figure>
      <figure>{device("finance-meaning","What it means")}<figcaption>Assumptions in plain words</figcaption></figure>
    </div>
  </section>
</div>

<section class="band final reveal"><div class="wrap">
  <h2>Coming soon to Google Play</h2>
  <p>Want early access or have a question? We'd love to hear from you.</p>
  <div class="cta"><a class="btn btn-store" href="mailto:{EMAIL}?subject=Early%20access%20-%20Tattva%20Finance%20Calculator"><span><small>Get early access</small><b>Email us</b></span></a></div>
</div></section>
''' + FOOT

def page(title, desc, current, kicker, h1, lede, body):
    return head(title, desc, current=current) + f'''
<section class="band page-head"><div class="wrap">
<span class="kicker">{kicker}</span><h1>{h1}</h1><p>{lede}</p>
</div></section>
<main class="wrap content">{body}</main>
''' + FOOT

def product_head(anchor, name, sub, icon=APP_ICON):
    return f'<div class="product-head" id="{anchor}"><img src="{icon}" alt="" width="48" height="48"><div><h2>{name}</h2><span>{sub}</span></div></div>'

privacy_body = f'''<div class="grid">
<aside class="toc"><b>On this page</b>
<a href="#principles">Our principles</a><a href="#website">This website</a><a href="#image-compressor">Tattva Image Compressor</a><a href="#finance-calculator">Tattva Finance Calculator</a><a href="#pdf-tools">Tattva PDF Tools</a><a href="#children">Children</a><a href="#changes">Changes</a><a href="#contact">Contact</a></aside>
<article class="prose">
<div class="summary"><h2>The short version</h2>
<p>Tattva Digital Labs builds apps that work without collecting your personal data. Each app below explains exactly what it accesses and what stays on your device.</p>
<div class="pills"><span class="pill">{CHECK}No personal data collected</span><span class="pill">{CHECK}No ads or trackers</span><span class="pill">{CHECK}No data sold or shared</span></div></div>

<h2 id="principles">Our principles</h2>
<ul><li><strong>On-device first.</strong> Our apps process your content on your device wherever possible.</li>
<li><strong>Collect nothing we don't need.</strong> If an app ever needs data to work, its section below will say what, why, and for how long.</li>
<li><strong>No advertising or tracking.</strong> We don't include ad networks, analytics or tracking SDKs in our apps.</li>
<li><strong>No selling or sharing.</strong> We never sell or share personal data.</li></ul>

<h2 id="website">This website</h2>
<p>This site has no cookies, analytics or ads, and our fonts are hosted here rather than by a third party. It is hosted on GitHub Pages; like any web host, GitHub may process technical data such as your IP address to serve and secure the site (see GitHub's privacy statement). If you email us, we use your message only to reply.</p>

{product_head("image-compressor", "Tattva Image Compressor", "Android app · Updated 27 November 2026")}
<p><strong>Summary:</strong> this app does not collect, store, send or share any personal data. Every photo is processed on your phone, and the app has no internet permission at all.</p>
<h3>What the app accesses</h3>
<ul><li><strong>Photos you choose.</strong> You pick images with Android's photo picker, or share them to the app. It can only read the images you select, and never modifies or deletes your originals.</li>
<li><strong>Compressed images you save.</strong> When you tap Save, a compressed copy is written to your gallery in <code>Pictures/Tattva Compressor</code>.</li></ul>
<h3>What stays on your device</h3>
<ul><li><strong>Settings</strong> such as theme and default compression options.</li>
<li><strong>History</strong> of images you saved: file name, sizes, dimensions, date and a link to the saved copy. Clear it any time in the app; your gallery is not affected.</li>
<li><strong>Temporary files</strong> created while compressing, kept in private app storage and removed automatically within 24 hours.</li></ul>
<p>None of this leaves your device. App data is excluded from cloud backup and device-to-device transfer.</p>
<h3>Network access</h3>
<p>The app does not request internet permission, so it cannot send data anywhere. This is checked automatically every time the app is built. Links you tap in the app (this page, or emailing support) open in your browser or email app.</p>
<h3>Photo metadata</h3>
<p>By default, compressed images have their metadata removed, including location (GPS), camera model and date. You can choose to keep it in Settings.</p>
<h3>Permissions</h3>
<ul><li><strong>Notifications</strong> (Android 13+, optional): show progress while compressing several images.</li>
<li><strong>Storage</strong> (Android 8–9 only): save compressed images to your gallery. Newer Android versions don't need it.</li></ul>

{product_head("finance-calculator", "Tattva Finance Calculator", "Android app · Updated 27 November 2026", FINANCE_ICON)}
<p><strong>Summary:</strong> this app does not collect, store, send or share any personal data. Every calculation happens on your phone, and the app has no internet permission at all. We never see the numbers you enter.</p>
<h3>What the app accesses</h3>
<p>Only what you type into a calculator, such as a loan amount, salary or interest rate. The app requests no permissions: no contacts, photos, location, SMS or files.</p>
<h3>What stays on your device</h3>
<ul><li><strong>Settings</strong> such as theme.</li>
<li><strong>Last values in each calculator</strong>, so leaving a screen doesn't lose your work.</li>
<li><strong>Saved calculations</strong>: the name you give them and their inputs. Delete them any time in the app (Saved → Delete), or remove everything by clearing the app's data or uninstalling it.</li></ul>
<p>None of this leaves your device. App data is excluded from cloud backup and device-to-device transfer.</p>
<h3>Sharing a summary</h3>
<p>When you tap Share, the app creates a summary image or text in its private storage and hands it only to the app you choose (for example WhatsApp or email). What happens after that is governed by the app you chose.</p>
<h3>Network access</h3>
<p>The app does not request internet permission, so it cannot send data anywhere. This is checked automatically every time the app is built. It contains no ads, analytics, crash reporting or other third-party SDKs that collect data.</p>
<h3>Calculations are not advice</h3>
<p>Results are estimates for understanding only and are not financial or tax advice. Each result's Calculation Passport explains the method and assumptions used.</p>
<h3>If this changes</h3>
<p>If we ever add anonymous usage statistics, we will update this section and the app's Google Play data safety information before that version is released. The numbers you enter would never be included.</p>

{product_head("pdf-tools", "Tattva PDF Tools", "Android app · Updated 28 November 2026", PDF_ICON)}
<p><strong>Summary:</strong> your files never leave your phone. The app makes, merges, splits, unlocks and compresses PDFs entirely on your device. It does not collect, store, send or share any personal data, and it has no internet permission.</p>
<h3>What the app accesses</h3>
<p>Only the PDFs, photos and scans you choose, through Android's file and photo pickers or when you share a file to the app. While you work on a file, the app keeps a private working copy, which is deleted when you finish or the app restarts. Your original files are never changed.</p>
<h3>Passwords</h3>
<p>A password you type to unlock a PDF is kept in memory only for that task. It is never saved, logged or sent anywhere. The app removes passwords you already know; it never guesses or cracks them.</p>
<h3>What stays on your device</h3>
<ul><li><strong>Settings</strong> such as theme, default page size and default compress size.</li>
<li><strong>History</strong>: the name, size, date and saved location of files you saved. Clear it any time in Settings → Clear history. The files themselves are not affected.</li></ul>
<p>None of this leaves your device. App data is excluded from cloud backup and device-to-device transfer.</p>
<h3>Scanning</h3>
<p>The document scanner is Google's on-device scanner, provided by Google Play services. Its screens run inside Google Play services; the scanned pages are returned to the app and processed on your phone. Google's handling of that component is covered by Google's privacy policy.</p>
<h3>Saving and sharing</h3>
<p>Files you save go to Download/Tattva PDF or Pictures/Tattva PDF, or a place you choose. When you tap Share, the file is handed only to the app you pick. What happens after that is governed by that app.</p>
<h3>Network access</h3>
<p>The app does not request internet permission, so it cannot send data anywhere. This is checked automatically every time the app is built. It contains no ads or analytics.</p>
<h3>Permissions</h3>
<ul><li><strong>Notifications</strong> (Android 13+, optional): show progress while a large file is processed.</li>
<li><strong>Storage</strong> (Android 8–9 only): save files to Download and Pictures. Newer Android versions don't need it.</li></ul>
<p>Tattva PDF Tools is not affiliated with UIDAI or any government body.</p>

<h2 id="children">Children</h2>
<p>Our apps do not knowingly collect personal data from anyone, including children.</p>

<h2 id="changes">Changes to this policy</h2>
<p>If this policy changes, the updated version will be published on this page with a new date. When we release a new app, we add its own section here.</p>

<h2 id="contact">Contact</h2>
<p>Tattva Digital Labs: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</article></div>'''

general_faq = [
 ("Do your apps collect my data?", "No personal data is collected by our apps. See the <a href=\"/privacy/\">privacy page</a> for each app's details."),
 ("How do I contact you?", f"Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. We usually reply within a few days."),
]
ic_faq = [
 ("Are my photos uploaded anywhere?", "No. The app has no internet permission, so it can't upload anything. Every step happens on your phone."),
 ("Are my original photos changed?", "Never. The app only reads your photos and saves a separate compressed copy when you tap Save."),
 ("Where are compressed images saved?", "In your gallery, in the <strong>Tattva Compressor</strong> album (<code>Pictures/Tattva Compressor</code>)."),
 ("Why does an image say “Can't read”?", "Some formats can't be read on every phone, for example HEIC photos on Android 8. Animated GIFs aren't supported."),
 ("Is location removed from my photos?", "Yes, by default. You can choose to keep photo details (date, camera, location) in Settings."),
 ("Can I compress many photos at once?", "Yes, up to 50 at a time. Compression keeps running in the background with a progress notification, and you can cancel any time."),
]
fc_faq = [
 ("Are my numbers sent anywhere?", "No. The app has no internet permission, so your salary, loans and savings never leave your phone."),
 ("Why is my bank's EMI slightly different?", "Banks may use daily interest, add broken-period interest to the first EMI, or include fees and insurance. Tap <strong>Understand this</strong> on any result: the Calculation Passport shows the method and lists why another figure may differ."),
 ("Can I type amounts like 50L?", "Yes. Type 50L, 1.25 Cr or 45k, or tap ×Thousand / ×Lakh / ×Crore under the amount field. The app shows the full amount, like ₹50,00,000, before using it."),
 ("Which tax rules does the income tax calculator use?", "FY 2026-27 (AY 2027-28) under the Income-tax Act, 2025, for resident individuals: new and old regime slabs, rebate, surcharge and cess. It's an estimate for understanding, not tax advice."),
 ("Are PPF and Sukanya rates up to date?", "Defaults are the government rates for October–December 2026 (PPF 7.1%, SSY 8.2%). Rates change every quarter, so you can always edit them."),
 ("Where are saved calculations kept?", "Only on your phone. Rename, duplicate, compare or delete them in the <strong>Saved</strong> tab; deleting has an undo."),
]
def faq_block(items): return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

support_body = '<div class="prose" style="max-width:860px;margin:0 auto">' + \
 f'''<div class="chooser">
<a href="#image-compressor"><img src="{APP_ICON}" alt="" width="44" height="44"><span>Tattva Image Compressor<small>Android</small></span></a>
<a href="#finance-calculator"><img src="{FINANCE_ICON}" alt="" width="44" height="44"><span>Tattva Finance Calculator<small>Android</small></span></a>
<a class="soon" aria-disabled="true"><span class="ph"></span><span>More apps<small>Coming soon</small></span></a>
</div>''' + \
 product_head("image-compressor", "Tattva Image Compressor", "Tip: in the app, Settings → Contact support fills in your device details") + faq_block(ic_faq) + \
 product_head("finance-calculator", "Tattva Finance Calculator", "Tip: found a number that looks wrong? Settings → Contact support, and include a screenshot", FINANCE_ICON) + faq_block(fc_faq) + \
 '<div class="product-head" id="general"><div><h2>General</h2><span>About Tattva Digital Labs</span></div></div>' + faq_block(general_faq) + \
 f'''<div class="contact"><div><h3>Still need help?</h3><p>Email us and tell us which app you're using, your phone model and Android version.</p></div>
<a class="btn" href="mailto:{EMAIL}?subject=Support%20request">Email support</a></div></div>'''

files = {
 'index.html': home,
 'image-compressor/index.html': product,
 'finance-calculator/index.html': finance,
 'privacy/index.html': page("Privacy · Tattva Digital Labs", "How Tattva Digital Labs and its apps handle your information. No personal data collected.", "privacy",
                             "Privacy policy · Updated 27 November 2026", "Your data is yours. Full stop.",
                             "How Tattva Digital Labs and each of our apps handle your information, in plain language.", privacy_body),
 'support/index.html': page("Support · Tattva Digital Labs", "Help and answers for Tattva Digital Labs apps.", "support",
                             "Support", "How can we help?", "Choose an app for quick answers, or write to us directly.", support_body),
}
for path, html in files.items():
    os.makedirs(os.path.dirname(os.path.join(root, path)) or root, exist_ok=True)
    with open(os.path.join(root, path), 'w') as f:
        f.write(html)
print("built", list(files))
