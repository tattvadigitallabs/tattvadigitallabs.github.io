from site_lib import EMAIL

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
