# Speelgoed Sorteerder

iPhone-webapp om speelgoed te sorteren: QR-labels voor bakken, dozen en locaties, foto's per artikel, zoeken op omschrijving en "Wat is dit?"-fotoherkenning.

**App:** https://bartvanrouveroy.github.io/speelgoed-sorteerder/ — open in Safari → Deel → *Zet op beginscherm*.

- `index.html` — de volledige app (één bestand, offline bruikbaar)
- `sw.js`, `manifest.webmanifest`, iconen — installatie als app op het beginscherm
- `src/` — bronbestand + bouwscript (`build.py` voegt de QR-bibliotheken in)

Gegevens blijven enkel op het toestel (IndexedDB). Maak geregeld een back-up via *Meer → Back-up maken*.
