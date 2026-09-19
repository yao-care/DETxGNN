---
layout: default
title: Lusutrombopag
parent: Nur Modellvorhersage (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Lusutrombopag: Von der Thrombopoietin-Rezeptor-Agonisten-Therapie zur erblichen Thrombozytopenie mit normalen Thrombozyten

## Zusammenfassung in einem Satz

> Die ursprüngliche zugelassene Indikation von Lusutrombopag ist im aktuellen Evidenzpaket nicht dokumentiert, obwohl sein bekannter Wirkmechanismus Thrombopoietin-Rezeptor-Agonismus (TPO-RA) ist, eine Wirkstoffklasse, die typischerweise zur Behandlung von Thrombozytopenie verwendet wird.
> Die Top-Vorhersage des TxGNN-Modells ist **Erbliche Thrombozytopenie mit normalen Thrombozyten**,
> aber diese Richtung wird derzeit durch **0 klinische Studien** und **0 Publikationen** unterstützt, und die Krankheitsbezeichnung selbst wird in der eigenen Begründung des Modells als intern widersprüchlich vermerkt.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert (kein genehmigter Indikationstext verfügbar; Arzneimittel nicht in Deutschland im Handel) |
| Vorhergesagte neue Indikation | Erbliche Thrombozytopenie mit normalen Thrombozyten |
| TxGNN-Vorhersage-Score | 99.995% |
| Evidenzlevel | L5 |
| Marktstand in Deutschland | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfehlenswerte Entscheidung | Zurückstellen |

## Warum ist diese Vorhersage vernünftig?

Formale Wirkmechanismus-Daten für Lusutrombopag sind derzeit eine Datenlücke (DG002). Die Begründung des Evidenzpakets selbst identifiziert Lusutrombopag jedoch als **TPO-Rezeptor-Agonist**, eine Wirkstoffklasse, die die Megakaryozyten-Produktion im Knochenmark stimuliert, um die Thrombozytenzahl zu erhöhen – dies steht im Einklang mit seiner etablierten pharmakologischen Klasse (TPO-RAs wie Eltrombopag, Avatrombopag).

Die höchstrangige Vorhersage „erbliche Thrombozytopenie mit normalen Thrombozyten" hat eine Bezeichnung, die semantisch widersprüchlich ist (eine Thrombozytopenie-Diagnose verbunden mit „normalen Thrombozyten"), was die eigene Begründung des Modells als wahrscheinliches Artefakt der Krankheits-Ontologie-Benennung oder -Klassifizierung anstelle eines kohärenten klinischen Phänotyps kennzeichnet. Dies macht die biologische Interpretierbarkeit der #1-Vorhersage schwach, trotz ihres hohen Ähnlichkeitswerts.

Von den verbleibenden neun Vorhersagen haben nur die Ränge 2–5 (Makrothrombozytopenie mit Mitralinsuffizienz, transiente neonatale Thrombozytopenie, Störung der dichten Granula, Thrombozytenspeicherpool-Defekt) einen plausiblen mechanistischen Zusammenhang zur Thrombozytologie, und selbst diese werden in der Begründung als indirekt oder mechanistisch nicht übereinstimmend beschrieben (z. B. erhöhen TPO-RAs die Thrombozyten*quantität*, nicht die *Funktion*, daher ist es unwahrscheinlich, dass sie Speicherpool- oder Granulitmängel korrigieren). Die Ränge 6–10 (ALS, Syndrom des unteren Motoneurons, Polymikrogyrie, spondylometaphysäre Dysplasie) weisen keine bekannte biologische Verbindung zwischen TPO-Rezeptor-Signalisierung und ihrer Pathologie auf, und die Begründung schreibt diese explizit Nähe-Artefakten im Wissensgraph statt echtem mechanistischem Signal zu.

## Klinische Studienbelege

Derzeit keine registrierten klinischen Studien vorhanden.

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

## Informationen zum deutschen Markt

Derzeit sind keine Zulassungen verzeichnet (total_licenses = 0; Marktstand: nicht im Handel). Es stehen keine Daten zu Produkten, Darreichungsformen oder zugelassenen Indikationen zur Verfügung.

## Sicherheitsaspekte

Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen.

Hinweis: TFDA/BfArM-Kennzeichnungsdaten (Warnungen, Kontraindikationen) sind derzeit eine **blockierende** Datenlücke (DG001), was bedeutet, dass dieser Kandidat nicht zur formalen Sicherheitsbewertungsstufe (S1) voranschreiten kann, bis die Kennzeichnungsdaten beschafft und überprüft werden.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Alle zehn vorhergesagten Indikationen befinden sich auf Evidenzlevel L5 (nur Modellscore, ohne unterstützende Studien oder Literatur), die Krankheitsbezeichnung der Top-Vorhersage ist gemäß der eigenen Begründung des Modells intern widersprüchlich, und grundlegende Arzneimittel-Daten (ursprüngliche Indikation, Wirkmechanismus, Marktstand in Deutschland, Sicherheitskennzeichnung) sind weitgehend nicht verfügbar. Eine Weiterentwicklung über den Stand einer Forschungshypothese hinaus ist derzeit nicht gerechtfertigt.

**Für die Weiterentwicklung erforderlich:**
- TFDA/BfArM-Kennzeichnungsdaten (Warnungen, Kontraindikationen) – derzeit blockierend (DG001)
- Bestätigter Wirkmechanismus aus DrugBank – derzeit Hochprioritäts-Datenlücke (DG002)
- Klarstellung der Krankheits-Ontologie für „erbliche Thrombozytopenie mit normalen Thrombozyten" vor weiterer Bewertung
- Vorklinische oder Fall-basierte Daten für eine der Top-5-Thrombozyten-bezogenen Vorhersagen, bevor der Übergang zur Studiephase erwogen wird
- Erneute Überprüfung der Ränge 6–10 auf mögliches Rauschen im Wissensgraph vor Aufnahme in zukünftige Priorisierungen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

