"""Hand-crafted product pages for the first two apps (kept as they were). New apps use the generic template."""
from site_lib import *


def image_compressor_page():
    return head("Tattva Image Compressor: compress photos to an exact size",
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


def finance_page():
    return head("Tattva Finance Calculator: every money calculation, clearly explained",
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
