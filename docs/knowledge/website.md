---
title: Website-Bestand und statisches Redesign
status: current
updated: 2026-11-17
---

# Website-Bestand und statisches Redesign

## Zweck und Grenzen

Lokaler Neuaufbau der Website von Asia & Sushi, Mahlsdorfer Str. 1, 15366 Hoppegarten. Auftrag: moderne, schlanke und responsive statische Website. Kein Deployment und keine Domain-/Anbieteränderung autorisiert. Second Brain: siehe Rückverknüpfung in der Projekt-AGENTS.md.

## Bestandsanalyse

Öffentlich am 17.11.2026 geprüft: [Startseite](https://asiaundsushi.de/), [Impressum](https://asiaundsushi.de/impressum.html), [Datenschutz](https://asiaundsushi.de/datenschutz.html) und robots.txt. Alle auf diesen HTML-Seiten verlinkten lokalen Seiten und Medien wurden verfolgt. Sitemap-Abruf ergab HTTP 403; nicht verlinkte Seiten lassen sich damit nicht ausschließen. Es gibt keine verlinkte PDF-Speisekarte. Vollständige Speisekarte befindet sich im externen Bestellservice.

Originale: [datierter HTML-/CSS-Bestand](../source/2026-11-17/index.html), [Assetmanifest](../source/assets.json). Acht Food-Bilder, zwei Logoauflösungen und eine lokale Bricolage-Schrift wurden unverändert heruntergeladen; Quell-URLs, Dateigrößen und SHA-256 sind dokumentiert. Externe Widget-Ressourcen sind kein Bestandteil dieser lokalen Mediensicherung.

### Verifizierte Inhalte

- Name: Asia & Sushi; rechtlicher Name laut Impressum Asia und Sushi.
- Inhaber und Inhaltsverantwortlicher: Trong Vinh Pham.
- Adresse: Mahlsdorfer Str. 1, 15366 Hoppegarten.
- Telefon: +49 30 547 85 101; E-Mail: asiaundsushi@gmail.com.
- Dienstag–Sonntag 12:00–15:00 und 17:00–21:30 Uhr; Montag Ruhetag.
- Lieferservice: Bestellungsannahme laut Website 11:30–21:00 Uhr. Dies ist keine durchgehend geöffnete Restaurantküche und keine zugesicherte Lieferzeit.
- Vier ursprüngliche Gerichte und Beschreibungen: Hako Sushi, Osiki Nigiri Sushi, Thai-Ente, Eierreis. Beschreibungen bleiben übernommen.
- Kartenlink: Google Maps ausschließlich als ausgehender Link.

### Abweichende Preise

Die externe Speisekarte wurde am 17.11.2026 über das echte Widget geöffnet und ohne Warenkorb-/Bestellaktion geprüft. Preise der Startseite sind teilweise überholt:

| Gericht | Ursprüngliche Startseite | Verifiziertes Widget |
| --- | --- | --- |
| Hako Sushi | 14,00 € | Nr. 149: 20,00 € |
| Thai-Ente | 9,00 € | Nr. 48: 13,00 € |
| Eierreis mit Hühnerfleisch | 5,00 € | Nr. 22: 8,00 € |
| Osiki Nigiri Sushi | 9,00 € | Unter diesem Namen nicht gefunden |

Neue Startseite verwendet die drei verifizierten Preise; beim nicht gefundenen Gericht steht „Preis bitte erfragen“. Betreiber muss Angebot und Aktualität vor Livegang bestätigen. Die vollständige Karte bleibt im führenden Bestellsystem; kein zweiter manuell zu pflegender Gesamtkatalog. Das Widget zeigte außerdem „10% Rabatt auf Abholung“; diese dynamische Aktion wurde bewusst nicht als dauerhafte Zusage auf die Startseite kopiert.

### Öffentliche technische Befunde

DNS-Abfrage am 17.11.2026: A `185.30.35.9`, NS `ns1.webgo.de` bis `ns4.webgo.de`; MX Prioritäten 10 und 20 jeweils `s260.goserver.host`. Bestehender Datenschutz nennt goserver.host. Dies bestätigt weder den Registrar noch die Vertragsinhaberschaft. Wix wurde nicht bestätigt. Kein Nachweis für Ursachen der vom Benutzer berichteten Hacks/Ausfälle. Vor DNS-Änderungen muss die gesamte Zone einschließlich SPF/DKIM/DMARC gesichert werden; Mail ist nicht als unbenutzt anzunehmen.

## Aktueller Stand und Entscheidungen

Direkt auslieferbare HTML-Seiten ohne Framework oder Buildpflicht. Farbwelt nach Benutzerentscheidung vom 17.11.2026 am Ladenschild orientiert: gedecktes Grün (`#285747`) für Überschriften und Flächen, warmes Rot (`#ae3d3d`) für Akzente und Bestellbuttons, Creme und helle Salbeiflächen als Hintergrund. Alle vier Header verwenden das Original-Logo mit lokaler 192-Pixel-Variante für scharfe Darstellung; die bereitgestellte `logo-96.png` ist per SHA-256 identisch zum bereits gesicherten Original. Originalmedien bleiben als austauschbare lokale Assets erhalten. CSS wird pro Grundlagen-, Komponenten-, Abschnitts- und Seitenverantwortung eingebunden. Informationsseiten benötigen kein JavaScript. Optionale Bündelung kopiert nur öffentliche Dateien nach `dist/`; Archive und Dokumentation bleiben draußen. Bestehende Rechtsseiten-URLs werden über `_redirects` für unterstützende Hosts erhalten.

Lesbarkeit und Schnellzugriff: Grundschrift 18 Pixel, mobil 19 Pixel, vergrößerte Begleittexte und Bedienelemente. Hero mit zwei gleichrangig erreichbaren Aktionen (Bestellen und Telefon), Google-Maps-Routenlink und Restaurantöffnungszeiten als dezenter 14-Pixel-Randnotiz direkt unter den Buttons. Der dekorative Streifen bleibt bis 1100 Pixel mit zwei kurzen Aussagen einzeilig; der gemeinsame Footer hat einen dunklen grünen Hintergrund. Responsive Prüfung der Startseite bei 320/390/768/1024/1440 Pixeln und aller drei Unterseiten bei 320 Pixeln ohne horizontalen Seitenüberlauf.

Originales Impressum inhaltlich übernommen. Datenschutz als lokaler Arbeitsstand: falsche Behauptung „keine Online-Bestellung/keine fremden Skripte“ korrigiert und automatisches Laden des Bestellservices auf der Bestellseite beschrieben. Vorhandene Hostingangabe bleibt bis zur tatsächlichen Anbieterwahl erhalten. Kein Anspruch auf rechtliche Vollständigkeit oder Freigabe.

## Bestellschnittstelle

- Originalbestand: `https://www.fbgcdn.com/embedder/js/ewm2.js`, Unternehmen `359414c1-ee2d-4b69-b527-4241905d372f`, Restaurant `9aa9f237-abd2-4df4-8862-536ed3f0376d`.
- Die Bestellseite enthält das echte Anbieter-iframe als statisches HTML: `https://www.foodbooking.com/ordering/?restaurant_uid=9aa9f237-abd2-4df4-8862-536ed3f0376d`. Speisekarte, Warenkorb, Zahlungs- und Bestellablauf bleiben beim Anbieter; kein eigener Checkout.
- Ausdrücklicher Benutzerwunsch: automatische Einbindung im Body der separaten Bestellseite mit eigenem Header/Footer. Kein Modal und keine zusätzliche Aktivierung. Informationsseiten laden weiterhin kein iframe. Auf der Bestellseite wird bereits beim Aufruf eine Verbindung zu Foodbooking aufgebaut.
- Breite auf Benutzerwunsch maximal 1024 Pixel, mobil volle Seitenbreite. Bei 1024 Pixeln zeigt Foodbooking die Gerichte zweispaltig ohne graue Außenränder; im Browser bei 1440 Pixeln Desktopbreite und 390 Pixeln Mobilbreite geprüft. iframe mit eigener Scrollfläche; normaler Seitenfluss führt anschließend zum Hilfelink und Footer.
- `allow="payment"` und das ursprüngliche `allowpaymentrequest` bleiben erhalten. Kein zusätzliches EWM-Parent-Script, keine Dialogverwaltung und keine fremden postMessage-Aktionen nötig. Ein externer Ausweichlink und telefonischer Kontakt stehen unterhalb der Einbettung.
- Unten erscheint ein schließbarer **Informationshinweis**, keine behauptete Cookie-Einwilligung. Foodbookings eigene Cookie-Auswahl bleibt beim Anbieter. Der Hinweis wird nach „Verstanden“ innerhalb der Sitzung über `sessionStorage` ausgeblendet; bei gesperrtem Speicher funktioniert Schließen trotzdem. Ein ResizeObserver reserviert Platz am Seitenende für den Banner. Der Klick verändert/lädt das iframe nicht neu.
- Prüfung zur automatischen Höhe am 17.11.2026: Foodbooking verwendet eine interne `.js-scrollable-content`-Scrollfläche (gemessen: 1110 Pixel sichtbar, 9886 Pixel Inhalt). Im aktuellen öffentlichen Embedder `https://www.fbgcdn.com/embedder/js/ewm2.js` und Frontend `https://www.fbgcdn.com/ordering/main.f9ac83028f89b526.js` wurde keine ausgehende Inhaltshöhenmeldung gefunden. Die empfangene `height`-Nachricht setzt nur die Anbieter-Bodyhöhe. Eine robuste Anpassung an Menü, Warenkorb und Checkout erfordert eine vom Anbieter unterstützte Inhaltshöhen-Schnittstelle; keine geschätzten festen Gesamthöhen und kein Abschalten des Scrollens verwenden. Aktuelle funktionierende Einbettung unverändert belassen.
- Farben, Inhalte und Cookieauswahl innerhalb des fremden iframes können nicht mit lokalem CSS umgestaltet werden. Keine Proxy-/Nachbau-Lösung; rechtliche Finalisierung der automatischen Drittanbietereinbindung bleibt vor Livegang offen.

## Verifikation

`python3 scripts/check_site.py` prüft alle vier Seiten, interne Links/Anker, Bilder sowie CSS-/JS-Referenzen. `node --check` prüft Einstieg und Hinweis-Modul. Startseite zuvor bei 320–1440 Pixeln geprüft. Aktuelle Bestellseite: automatische echte Speisekarte, eigener Header/Footer, keine Dialoge und kein Aktivierungsbutton; responsive Browserprüfung und leerer Warenkorb. Keine echte Bestellung ausgelöst. Noch offen: tatsächliche Auftragsannahme, Zahlungen und Betreiberprüfung der Inhalte sowie späterer Host-/DNS-Livebetrieb.
