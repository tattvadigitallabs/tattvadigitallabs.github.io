"""
Builds the Tattva Digital Labs website from the app registry (apps.py) and content/.

    python3 scripts/build_site.py .

Every page that lists apps (home, /apps/, privacy, support) is generated from APPS, so adding an app to the
registry is enough for it to appear everywhere.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from apps import APPS, GENERAL_FAQ, by_category, category, newest  # noqa: E402
from legacy_pages import finance_page, image_compressor_page  # noqa: E402
from site_lib import (  # noqa: E402
    APPS_CSS, CHECK, EMAIL, FOOT, HOME_CSS, ICONS, PLAY, device, faq_block, head, page, product_head, read,
)

root = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
content_dir = os.path.join(here, "..", "content")
LEGACY = {"legacy:image_compressor": image_compressor_page, "legacy:finance": finance_page}


# ---------------- Building blocks ----------------

def status_badge(app):
    if app["status"] == "live" and app.get("play_url"):
        return '<span class="badge live">On Google Play</span>'
    return '<span class="badge soon">Coming soon</span>'


def store_button(app):
    if app["status"] == "live" and app.get("play_url"):
        return f'<a class="btn btn-store" href="{app["play_url"]}">{PLAY}<span><small>Get it on</small><b>Google Play</b></span></a>'
    return f'<span class="btn btn-store">{PLAY}<span><small>Coming soon on</small><b>Google Play</b></span></span>'


def app_card(app):
    cat = category(app["category"])
    search = " ".join([app["name"], app["tagline"], cat["name"], app.get("keywords", ""), *app["tags"]]).lower()
    tags = "".join(f"<span>{t}</span>" for t in app["tags"][:3])
    return f'''<a class="app-card" href="/{app["slug"]}/" data-cat="{cat["id"]}" data-search="{search}">
  <div class="top"><img class="icon" src="{app["icon"]}" alt="" width="56" height="56" loading="lazy">{status_badge(app)}</div>
  <span class="cat">{cat["name"]}</span>
  <h3>{app["name"]}</h3>
  <p>{app["tagline"]}</p>
  <div class="tags">{tags}</div>
  <span class="more">Learn more <span aria-hidden="true">→</span></span>
</a>'''


def next_card():
    return f'''<div class="app-card next"><b>More on the way</b><span>New tools built the same way: simple, private, offline.
<a href="mailto:{EMAIL}?subject=App%20idea">Suggest one</a></span></div>'''


def filters():
    chips = [f'<button class="chip" type="button" data-filter="all" aria-pressed="true">All <i>{len(APPS)}</i></button>']
    for cat, apps in by_category():
        chips.append(f'<button class="chip" type="button" data-filter="{cat["id"]}" aria-pressed="false">{cat["name"]} <i>{len(apps)}</i></button>')
    search = '''<label class="search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
<input type="search" placeholder="Search apps, e.g. PDF, EMI, photo" aria-label="Search apps" data-search-input></label>'''
    return f'<div class="filters" role="toolbar" aria-label="Filter apps by category">{"".join(chips)}{search}</div>'


# ---------------- Home ----------------

def home_page():
    featured = newest()
    fcat = category(featured["category"])
    cards = "\n".join(app_card(a) for a in APPS)
    shots = "".join(device(s, "") for s in featured["shots"][:2])
    return head("Tattva Digital Labs: simple apps that respect your privacy",
                "Tattva Digital Labs builds simple, beautifully crafted apps for documents, photos and money that work offline and never collect your data.",
                HOME_CSS + APPS_CSS) + f'''
<section class="band hero co-hero"><div class="wrap">
  <img class="big-mark reveal" src="/assets/brand/tattva-mark.svg" alt="Tattva Digital Labs" width="84" height="84">
  <div class="reveal">
    <h1>Simple tools. <em>Serious about privacy.</em></h1>
    <p class="lead">Focused, beautifully crafted apps for documents, photos and money. They do one job brilliantly, work offline, and never collect your data.</p>
    <div class="cta"><a class="btn btn-store" href="#apps"><span><small>Explore</small><b>Our apps</b></span></a><a class="btn btn-ghost" href="/privacy/">Our privacy promise</a></div>
    <p class="hero-stats"><b>{len(APPS)}</b> apps <span>·</span> <b>{len(by_category())}</b> categories <span>·</span> <b>0</b> bytes of your data collected</p>
  </div>
</div></section>

<div class="wrap">
  <div class="proof values reveal"><div class="grid">
    <div class="cell"><span class="ico">{ICONS["lock"]}</span><b>Private by design</b><span>Your data stays on your device.</span></div>
    <div class="cell"><span class="ico">{ICONS["offline"]}</span><b>Offline-first</b><span>Works anywhere, no signal needed.</span></div>
    <div class="cell"><span class="ico">{ICONS["noads"]}</span><b>No ads, no tracking</b><span>No analytics, no third-party SDKs.</span></div>
    <div class="cell"><span class="ico">{ICONS["spark"]}</span><b>Crafted with care</b><span>Fast, focused and delightful to use.</span></div>
  </div></div>

  <section class="featured reveal" aria-label="Newest app">
    <article class="prod-card">
      <div>
        <span class="new-label">New · {fcat["name"]}</span>
        <img class="icon" src="{featured["icon"]}" alt="" width="72" height="72">
        <h3>{featured["name"]}</h3>
        <p>{featured["summary"]}</p>
        <div class="tags">{"".join(f"<span>{t}</span>" for t in featured["tags"])}</div>
        <div class="actions"><a class="btn btn-dark" href="/{featured["slug"]}/">Learn more →</a>{status_badge(featured)}</div>
      </div>
      <div class="shots">{shots}</div>
    </article>
  </section>

  <section class="directory" id="apps">
    <div class="dir-head">
      <div><span class="kicker reveal">Our apps</span><h2 class="reveal">Made to do one thing really well</h2></div>
      <a class="all-link" href="/apps/">Browse by category →</a>
    </div>
    {filters()}
    <div class="app-grid" data-grid>
{cards}
      {next_card()}
    </div>
    <p class="no-results" hidden>No apps match that search. <button type="button" class="linkish" data-clear>Show all apps</button></p>
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


# ---------------- /apps/ catalogue ----------------

def apps_page():
    jump = "".join(f'<a class="chip" href="#{c["id"]}">{c["name"]} <i>{len(a)}</i></a>' for c, a in by_category())
    sections = ""
    for cat, apps in by_category():
        cards = "\n".join(app_card(a) for a in apps)
        sections += f'''<section class="cat-section" id="{cat["id"]}">
  <div class="cat-head"><h2>{cat["name"]}</h2><span>{cat["desc"]} · {len(apps)} app{"s" if len(apps) != 1 else ""}</span></div>
  <div class="app-grid">{cards}</div>
</section>'''
    body = f'''<div class="filters jump" aria-label="Jump to a category">{jump}</div>
{sections}
<div class="app-grid" style="margin-top:32px">{next_card()}</div>'''
    return page("Apps · Tattva Digital Labs", "Every Tattva Digital Labs app, by category: documents, photos and money. Private, offline, no ads.",
                "apps", f"{len(APPS)} apps · {len(by_category())} categories", "All apps",
                "Simple, private tools for everyday jobs. Every app works offline and collects nothing about you.", body, APPS_CSS)


# ---------------- Generic product page ----------------

def product_page(app):
    p = app["page"]
    cat = category(app["category"])
    assure = "".join(f"<li>{CHECK} {a}</li>" for a in p["assure"])
    stage = "".join(device(s, "", f"d{i + 1}") for i, s in enumerate(p["stage"]))
    floats = "".join(f'<div class="float f{i + 1}">{big}<span>{small}</span></div>' for i, (big, small) in enumerate(p["floats"]))
    proof = "".join(f'<div class="cell"><b>{b}</b><span>{s}</span></div>' for b, s in p["proof"])
    feats = ""
    for i, f in enumerate(p["features"]):
        ticks = "".join(f"<li>{t}</li>" for t in f["ticks"])
        pair = "".join(device(s, "") for s in f["shots"])
        anchor = ' id="features"' if i == 0 else ''
        feats += f'''<section class="feature{" rev" if i % 2 else ""}"{anchor}>
    <div class="copy reveal"><span class="kicker">{f["kicker"]}</span><h2>{f["title"]}</h2><p>{f["body"]}</p><ul class="ticks">{ticks}</ul></div>
    <div class="pair reveal">{pair}</div>
  </section>'''
    steps = "".join(f'<div class="step reveal"><span class="n">STEP 0{i + 1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(p["steps"]))
    tiles = "".join(f'<div class="tile"><b>{b}</b><span>{s}</span></div>' for b, s in p["tiles"])
    gallery = "".join(f'<figure>{device(s, c)}<figcaption>{c}</figcaption></figure>' for s, c in p["gallery"])
    others = "".join(app_card(a) for a in APPS if a["slug"] != app["slug"])
    subject = app["name"].replace(" ", "%20")
    return head(p["title"], p["desc"], HOME_CSS + APPS_CSS, "apps", og=p.get("og", "/assets/img/og.png")) + f'''
<section class="band hero"><div class="wrap">
  <div class="reveal">
    <span class="app-eyebrow"><img src="{app["icon"]}" alt="" width="28" height="28">{app["name"]} · {cat["name"]} · Android</span>
    <h1>{p["h1"]} <em>{p["h1_em"]}</em></h1>
    <p class="lead">{p["lead"]}</p>
    <ul class="assure">{assure}</ul>
    <div class="cta">{store_button(app)}<a class="btn btn-ghost" href="#features">See how it works</a></div>
  </div>
  <div class="stage reveal" aria-hidden="true">{stage}{floats}</div>
</div></section>

<div class="wrap">
  <div class="proof reveal"><div class="grid">{proof}</div></div>
  {feats}
  <section class="how">
    <span class="kicker reveal">Effortless</span>
    <h2 class="reveal">Three taps. Done.</h2>
    <p class="muted reveal">No sign-up. No settings to learn.</p>
    <div class="steps">{steps}</div>
  </section>
</div>

<section class="band trust reveal"><div class="wrap">
  <div>
    <span class="kicker">Private by design</span>
    <h2>{p["trust_title"]}</h2>
    <p>{p["trust_body"]} <a href="/privacy/#{app["slug"]}">Read its privacy details</a>.</p>
  </div>
  <div class="tiles">{tiles}</div>
</div></section>

<div class="wrap">
  <section class="gallery-sec">
    <span class="kicker reveal">Crafted with care</span>
    <h2 class="reveal">A closer look</h2>
    <div class="gallery">{gallery}</div>
  </section>
  <section class="more-apps">
    <div class="dir-head"><div><span class="kicker">From Tattva</span><h2>More apps</h2></div><a class="all-link" href="/apps/">All apps →</a></div>
    <div class="app-grid">{others}</div>
  </section>
</div>

<section class="band final reveal"><div class="wrap">
  <h2>Coming soon to Google Play</h2>
  <p>Want early access or have a question? We'd love to hear from you. Answers to common questions are on the <a href="/support/#{app["slug"]}">support page</a>.</p>
  <div class="cta"><a class="btn btn-store" href="mailto:{EMAIL}?subject=Early%20access%20-%20{subject}"><span><small>Get early access</small><b>Email us</b></span></a></div>
</div></section>
''' + FOOT


# ---------------- Privacy ----------------

def privacy_page():
    toc = '<a href="#principles">Our principles</a><a href="#website">This website</a>'
    toc += "".join(f'<a href="#{a["slug"]}">{a["name"]}</a>' for _, apps in by_category() for a in apps)
    toc += '<a href="#children">Children</a><a href="#changes">Changes</a><a href="#contact">Contact</a>'
    sections = ""
    for _, apps in by_category():
        for a in apps:
            sections += product_head(a["slug"], a["name"], f'Android app · Updated {a["privacy_updated"]}', a["icon"]) + "\n"
            sections += read(os.path.join(content_dir, "privacy", f'{a["slug"]}.html')) + "\n"
    body = f'''<div class="grid">
<aside class="toc"><b>On this page</b>
{toc}</aside>
<article class="prose">
{read(os.path.join(content_dir, "privacy", "_intro.html"))}
{sections}
{read(os.path.join(content_dir, "privacy", "_outro.html"))}
</article></div>'''
    latest = max((a["released"], a["privacy_updated"]) for a in APPS)[1]
    return page("Privacy · Tattva Digital Labs", "How Tattva Digital Labs and its apps handle your information. No personal data collected.", "privacy",
                f"Privacy policy · Updated {latest}", "Your data is yours. Full stop.",
                "How Tattva Digital Labs and each of our apps handle your information, in plain language.", body)


# ---------------- Support ----------------

def support_page():
    chooser = "".join(
        f'<a href="#{a["slug"]}"><img src="{a["icon"]}" alt="" width="44" height="44"><span>{a["name"]}<small>{cat["name"]}</small></span></a>'
        for cat, apps in by_category() for a in apps
    )
    blocks = "".join(
        product_head(a["slug"], a["name"], a["support_tip"], a["icon"]) + faq_block(a["faq"])
        for _, apps in by_category() for a in apps
    )
    body = '<div class="prose" style="max-width:860px;margin:0 auto">' + \
        f'<div class="chooser">{chooser}</div>' + blocks + \
        '<div class="product-head" id="general"><div><h2>General</h2><span>About Tattva Digital Labs</span></div></div>' + faq_block(GENERAL_FAQ) + \
        f'''<div class="contact"><div><h3>Still need help?</h3><p>Email us and tell us which app you're using, your phone model and Android version.</p></div>
<a class="btn" href="mailto:{EMAIL}?subject=Support%20request">Email support</a></div></div>'''
    return page("Support · Tattva Digital Labs", "Help and answers for Tattva Digital Labs apps.", "support",
                "Support", "How can we help?", "Choose an app for quick answers, or write to us directly.", body)


# ---------------- Build ----------------

files = {
    "index.html": home_page(),
    "apps/index.html": apps_page(),
    "privacy/index.html": privacy_page(),
    "support/index.html": support_page(),
}
for a in APPS:
    files[f'{a["slug"]}/index.html'] = LEGACY[a["page"]]() if isinstance(a["page"], str) else product_page(a)

for path, html in files.items():
    full = os.path.join(root, path)
    os.makedirs(os.path.dirname(full) or root, exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
print("built", list(files))
