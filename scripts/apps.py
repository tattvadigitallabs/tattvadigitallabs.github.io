"""
The app registry: every app is declared once here, and the home directory, /apps/ catalogue, product page,
privacy page and support page are generated from it.

Adding an app:
  1. Add its icon to assets/brand/<slug>-icon.svg and screenshots (450×1000 JPG) to assets/img/.
  2. Add an entry to APPS below (pick an existing category or add one to CATEGORIES).
  3. Add its privacy text to content/privacy/<slug>.html.
  4. Run: python3 scripts/build_site.py .
"""
from _faqs import ic_faq, fc_faq, general_faq

CATEGORIES = [
    {"id": "documents", "name": "Documents", "desc": "PDFs, scans and forms"},
    {"id": "photos", "name": "Photos & media", "desc": "Size, quality and sharing"},
    {"id": "money", "name": "Money", "desc": "Calculations you can trust"},
]

pdf_faq = [
    ("Are my files uploaded anywhere?", "No. Every tool runs on your phone and the app has no internet permission. Your PDFs, scans and passwords never leave the device."),
    ("Will compressing go over my size limit?", "Never. If the limit can't be reached while keeping the text readable, the app tells you the smallest readable size and offers the best next step, such as the nearest limit that works, black &amp; white, or splitting the file."),
    ("Does merging or making a PDF reduce quality?", "No. Merge, Split and Organize copy pages exactly, and photos are added at original quality. Only Compress makes a file smaller, and only when you ask."),
    ("Can it open password-protected PDFs?", "Yes, if you know the password. Bank statements and e-Aadhaar PDFs open after you enter it, and Unlock can save a copy without the password. The app never guesses or cracks passwords."),
    ("Where are files saved?", "PDFs go to <code>Download/Tattva PDF</code> and images to <code>Pictures/Tattva PDF</code>, or anywhere you choose with “Save to…”."),
    ("Can I use it to open PDFs from WhatsApp or email?", "Yes. Choose “Open with Tattva PDF Tools” to view the PDF, then use any tool on it."),
]

APPS = [
    {
        "slug": "pdf-tools",
        "name": "Tattva PDF Tools",
        "icon": "/assets/brand/pdf-tools-icon.svg",
        "category": "documents",
        "status": "soon",
        "released": "2026-11-28",
        "tagline": "Compress PDFs to any size limit, scan, merge, split and unlock. Fully offline.",
        "summary": "Get documents ready for any form or exam portal: compress to an exact size (never over the limit), scan to PDF, put an ID card on one page, merge, split, organize, lock and unlock.",
        "tags": ["Exact-size compression", "Scanner", "Merge & split", "PDF viewer"],
        "keywords": "pdf compress 100kb 200kb merge split scan unlock password aadhaar id card viewer",
        "shots": ["pdf-home", "pdf-result"],
        "faq": pdf_faq,
        "support_tip": "Tip: if a file won't compress, the app explains why. Settings → Contact support fills in your device details",
        "privacy_updated": "28 November 2026",
        "page": {
            "title": "Tattva PDF Tools: compress PDFs to any size limit",
            "desc": "Compress PDFs to 100 KB, 200 KB or any size for forms and exam portals, never over the limit. Scan, merge, split, organize, lock and unlock. Fully offline.",
            "og": "/assets/img/pdf-og.png",
            "h1": "Any upload limit.", "h1_em": "Every time.",
            "lead": "Portal wants a PDF under 200&nbsp;KB? Pick the limit and Tattva lands just under it, readable and never over. Then scan, merge, split or unlock, all on your phone.",
            "assure": ["Your files stay on your phone", "No ads, no watermark", "Originals never touched"],
            "stage": ["pdf-home", "pdf-result"],
            "floats": [("1.6 MB → 97 KB", "94% smaller"), ("✓ Under 100 KB", "Never over your limit")],
            "proof": [("Never", "over your limit"), ("Original", "quality, until you compress"), ("9 tools", "in one app"), ("0 bytes", "ever uploaded")],
            "features": [
                {"kicker": "Compress to a size limit", "title": "Lands just under the limit. Stays readable.",
                 "body": "Text stays sharp: Tattva shrinks images first and only turns pages into images when there's no other way. If a limit is too small to stay readable, it says so and offers the best option instead of a blurry file.",
                 "ticks": ["Common portal limits, or any size", "Black &amp; white for even smaller files", "Already small enough? It keeps your original"],
                 "shots": ["pdf-compress", "pdf-advice"]},
                {"kicker": "Open and read any PDF", "title": "Open from WhatsApp or email. Read it. Fix it.",
                 "body": "“Open with Tattva PDF Tools” shows the document in a clean viewer, password-protected ones included, with every tool one tap away.",
                 "ticks": ["Pinch to zoom, page counter", "Unlocks bank statements and e-Aadhaar with your password", "Share in one tap"],
                 "shots": ["pdf-viewer", "pdf-organize"]},
                {"kicker": "Made for forms", "title": "Your ID card, front and back, on one page.",
                 "body": "Scan both sides and Tattva places them on one A4 page at real card size, ready to print or upload. Photos are kept at original quality.",
                 "ticks": ["Built-in scanner with edge detection", "Make PDFs from photos or scans", "Merge, split, reorder, rotate, lock"],
                 "shots": ["pdf-idcard", "pdf-home"]},
            ],
            "steps": [("Pick a PDF or scan", "Choose a file, scan a document, or open a PDF from any app."),
                      ("Choose what to do", "Pick a size limit, or merge, split, organize, lock or unlock."),
                      ("Save or share", "Save to Downloads or share straight to the portal, email or WhatsApp.")],
            "trust_title": "Your documents never leave your phone.",
            "trust_body": "Aadhaar cards, bank statements, marksheets: everything is processed on the device. The app has no internet permission, no ads and no account.",
            "tiles": [("On-device", "Every tool runs offline"), ("No accounts", "Nothing to sign up for"), ("No watermark", "Your files stay yours"), ("Originals safe", "Never changed or deleted")],
            "gallery": [("pdf-home", "Every tool, one tap away"), ("pdf-compress", "Pick the portal's limit"), ("pdf-result", "Just under the limit"), ("pdf-viewer", "A clean PDF viewer"), ("pdf-dark", "Comfortable in the dark")],
        },
    },
    {
        "slug": "image-compressor",
        "name": "Tattva Image Compressor",
        "icon": "/assets/brand/image-compressor-icon.svg",
        "category": "photos",
        "status": "soon",
        "released": "2026-11-27",
        "tagline": "Compress photos to the exact size you need, with the best quality that fits. Entirely offline.",
        "summary": "Compress photos to the exact size you need, like 200&nbsp;KB for forms, exam and job portals, with the best quality that fits. Entirely offline.",
        "tags": ["Exact-size compression", "Batch of 50", "Before/after compare"],
        "keywords": "image photo compress resize jpeg kb form exam job portal batch",
        "shots": ["target", "target-results"],
        "faq": ic_faq,
        "support_tip": "Tip: in the app, Settings → Contact support fills in your device details",
        "privacy_updated": "27 November 2026",
        "page": "legacy:image_compressor",
    },
    {
        "slug": "finance-calculator",
        "name": "Tattva Finance Calculator",
        "icon": "/assets/brand/finance-calculator-icon.svg",
        "category": "money",
        "status": "soon",
        "released": "2026-11-27",
        "tagline": "EMI, SIP, income tax, FD, PPF and GST, with every result explained. Entirely offline.",
        "summary": "EMI, SIP, income tax, FD, PPF, GST and more, with every result explained: the method, the assumptions, and what the number means for you. Entirely offline.",
        "tags": ["Calculation Passport", "What-if scenarios", "13 calculators"],
        "keywords": "finance emi sip income tax fd ppf gst loan calculator india lakh crore",
        "shots": ["finance-emi", "finance-passport"],
        "faq": fc_faq,
        "support_tip": "Tip: found a number that looks wrong? Settings → Contact support, and include a screenshot",
        "privacy_updated": "27 November 2026",
        "page": "legacy:finance",
    },
]

GENERAL_FAQ = general_faq


def by_category():
    """[(category, [apps])] in CATEGORIES order, skipping empty categories."""
    return [(c, [a for a in APPS if a["category"] == c["id"]]) for c in CATEGORIES if any(a["category"] == c["id"] for a in APPS)]


def newest():
    return sorted(APPS, key=lambda a: a["released"], reverse=True)[0]


def category(cid):
    return next(c for c in CATEGORIES if c["id"] == cid)
