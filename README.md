# Asia & Sushi · Hoppegarten

Lokales Redesign von [asiaundsushi.de](https://asiaundsushi.de/). Reines HTML/CSS und kleine JavaScript-Module für den Datenschutzhinweis. Kein Framework, Backend, Paketmanager oder Build zum Betrieb erforderlich.

## Vorschau

```sh
python3 -m http.server 4174 --bind 127.0.0.1
```

Anschließend [lokale Vorschau](http://127.0.0.1:4174) öffnen. Ein HTTP-Server wird wegen der ES-Module empfohlen.

## Struktur

- `index.html`: Startseite, direkt auslieferbar.
- `pages/`: Bestellung, Impressum, Datenschutz.
- `css/base/`: Farben, lokale Schrift, grundlegende Darstellung.
- `css/components/`: Navigation, Footer, Buttons.
- `css/sections/`: je eine Datei für Hero, Küche, Menü, Galerie, Besuch.
- `css/pages/`: ausschließlich auf den jeweiligen Unterseiten geladene Styles.
- `js/components/`: schließbarer Datenschutzhinweis; Einstieg `js/order.js` nur auf der Bestellseite.
- `assets/`: lokal gesicherte Originalbilder, Logos und Schrift.
- `docs/source/`: datierter Originalbestand und Assetmanifest mit Quell-URLs und Prüfsummen.
- `docs/knowledge/`: Analyse, verifizierte Inhalte und technische Grenzen.

Gemeinsames HTML ist bewusst direkt in den statischen Seiten enthalten. Kein JavaScript zum Nachladen von Navigation oder Inhalten. Farbwerte zentral in `css/base/tokens.css` ändern.

## Prüfen und optional bündeln

```sh
python3 scripts/check_site.py
node --check js/order.js
node --check js/components/privacy-notice.js
python3 scripts/build_site.py
```

Das optionale Bündeln erzeugt `dist/` ausschließlich aus öffentlichen Dateien. `docs/`, Skripte und archivierte Ursprungsseiten werden nicht veröffentlicht. `dist/` eignet sich später als statisches Uploadverzeichnis. Das Skript führt kein Deployment aus. `_redirects` erhält die bisherigen Impressums- und Datenschutz-URLs auf Hosts, die diese Datei unterstützen (z. B. Cloudflare Pages).

## Offene Freigaben vor dem Livegang

Preise, Öffnungszeiten, Lieferbedingungen und Rechtsangaben durch den Betreiber bestätigen. Datenschutzerklärung nach Auswahl des tatsächlichen Hosters und Prüfung des Bestellservices finalisieren. Domain, Mail-DNS und Hosting getrennt behandeln. Derzeit kein Deployment, Commit oder Push.

[Analyse und Bestellintegration](docs/knowledge/website.md) · [Second-Brain-Vorhaben](../second-brain/02%20Vorhaben/Asia%20und%20Sushi%20%E2%80%93%20Website%20erneuern%20und%20Domain%20%C3%BCbernehmen.md)
