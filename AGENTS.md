# Projektanweisungen

<!-- project-knowledge:start -->
## Projektwissen und Pläne

- Gemeinsames, dauerhaftes Projektwissen liegt unter `docs/knowledge/`; aktive,
  ausreichend ausgearbeitete Vorhaben liegen unter `docs/plans/`.
- Lies bei benötigtem Projektverständnis den Knowledge-Index und nur passende
  Einträge; den Plan-Index bei geplanter oder laufender nichttrivialer Umsetzung.
  Nutze bereits gelesenen, unveränderten Kontext weiter.
- Nutze die Skill `project-knowledge`, sofern sie verfügbar ist. Fehlt sie,
  befolge den hier beschriebenen Lebenszyklus direkt.
- Halte als Knowledge nur verifiziertes, dauerhaftes und nicht offensichtlich
  aus dem Code ableitbares Wissen fest. Keine Chatprotokolle, Zugangsdaten,
  temporären Debug-Notizen oder spekulativen Aussagen.
- Lege einen Plan nur für ein nicht triviales, ausreichend abgestimmtes oder
  ausgearbeitetes Vorhaben an. Kleine Änderungen und lose Ideen brauchen keine
  eigene Plan-Datei.
- Prüfe vor Abschluss relevanter Implementierungs- und Review-Aufgaben, ob
  Knowledge erstellt oder aktualisiert werden muss. Nach vollständiger
  Umsetzung eines Plans überführe den weiterhin gültigen Inhalt in Knowledge
  und entferne Plan sowie Indexeintrag in derselben Änderung.
- In einem read-only Review formulierst du nötige Dokumentationsänderungen als
  Befund und schreibst sie nur, wenn der Auftrag auch Änderungen erlaubt.
<!-- project-knowledge:end -->

## Projekt und Second Brain

- Rein statisches HTML/CSS, ES-Module nur nach Bedarf. Kein Framework oder Backend einführen.
- Bilder und Schrift lokal halten; Originale und Herkunft unter `docs/source/` bewahren.
- Second Brain: `../second-brain`, Vorhaben [Asia und Sushi](../second-brain/02%20Vorhaben/Asia%20und%20Sushi%20%E2%80%93%20Website%20erneuern%20und%20Domain%20%C3%BCbernehmen.md), Thema [Unternehmertum](../second-brain/01%20Themen/Unternehmertum.md).
- Nur `dist/` aus dem optionalen Bundle veröffentlichen. Commit, Push, Deployment und Domainänderungen benötigen einen ausdrücklichen Auftrag.
