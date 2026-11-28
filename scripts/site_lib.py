"""Shared layout: head, footer, helpers and reusable blocks. Content lives in apps.py and content/."""
import os
EMAIL = 'support.tattvadigitallabs@gmail.com'
# Bump when CSS/JS change so browsers don't keep stale copies.
ASSET_VERSION = '2026-11-28'
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
<link rel="stylesheet" href="/assets/style.css?v={ASSET_VERSION}">{extra_css}
</head><body>
<header class="nav"><div class="wrap">
<a class="brand" href="/">{MARK}<span class="name">Tattva Digital Labs</span></a>
<nav>{nav("/apps/","Apps","apps")}{nav("/privacy/","Privacy","privacy")}{nav("/support/","Support","support")}</nav>
</div></header>
'''

FOOT = f'''<footer class="foot"><div class="wrap">
<a class="brand" href="/">{MARK}<span>Tattva Digital Labs</span></a>
<span><a href="/apps/">Apps</a> &nbsp;·&nbsp; <a href="/privacy/">Privacy</a> &nbsp;·&nbsp; <a href="/support/">Support</a> &nbsp;·&nbsp; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
<span>© 2026 Tattva Digital Labs</span>
</div></footer>
<script src="/assets/site.js?v={ASSET_VERSION}" defer></script>
</body></html>
'''

def device(src, alt, cls=''):
    c = f'device {cls}'.strip()
    return f'<div class="{c}"><img src="/assets/img/{src}.jpg" alt="{alt}" loading="lazy" width="450" height="1000"></div>'



HOME_CSS = f'<link rel="stylesheet" href="/assets/home.css?v={ASSET_VERSION}">'
APPS_CSS = f'<link rel="stylesheet" href="/assets/apps.css?v={ASSET_VERSION}">'


def page(title, desc, current, kicker, h1, lede, body, extra_css=''):
    return head(title, desc, extra_css, current=current) + f'''
<section class="band page-head"><div class="wrap">
<span class="kicker">{kicker}</span><h1>{h1}</h1><p>{lede}</p>
</div></section>
<main class="wrap content">{body}</main>
''' + FOOT


def product_head(anchor, name, sub, icon=APP_ICON):
    return f'<div class="product-head" id="{anchor}"><img src="{icon}" alt="" width="48" height="48"><div><h2>{name}</h2><span>{sub}</span></div></div>'


def faq_block(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'


def read(path):
    with open(path) as f:
        return f.read()
