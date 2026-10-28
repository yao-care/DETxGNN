---
layout: default
title: Moroctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 306
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Moroctocog Alfa: vorhergesagte neue Indikation Primäre Freisetzungsstörung der Thrombozyten (Evidenzstufe L5). Ursprüngliche Indikation: Hämophilie A"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
---

# Moroctocog Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **8** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Moroctocog alfa: Von Hämophilie A zu Primäre Thrombozyten-Freisetzungsstörung
{: .text-alpha }

## Zusammenfassung in einem Satz

Moroctocog alfa ist ein rekombinanter Faktor VIII mit deletierter B-Domäne und wurde ursprünglich zur Behandlung der **Hämophilie A** eingesetzt.
Das TxGNN-Modell sagt voraus, dass es bei der **primären Freisetzungsstörung der Thrombozyten** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien und keine Publikationen** vor, die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie A |
| Vorhergesagte neue Indikation | Primäre Freisetzungsstörung der Thrombozyten |
| TxGNN-Vorhersagewert | 0,9997 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Detaillierte Daten zum Wirkmechanismus liegen derzeit nicht vor. Bekannt ist, dass Moroctocog alfa ein rekombinanter Faktor VIII (FVIII) ohne B-Domäne ist. Seine Wirksamkeit bei Hämophilie A beruht auf dem Ersatz des fehlenden Gerinnungsfaktors.

Bei der vorhergesagten Indikation liegt die Ursache dagegen in einem intrinsischen Defekt der Thrombozyten (Speicherpool bzw. Sekretion), nicht in einem FVIII-Mangel. Ein zusätzlicher FVIII-Ersatz dürfte diesen Defekt daher nicht beheben. Der hohe Vorhersagewert ist eine graphbasierte Modellaussage ohne klinische oder literaturbasierte Stütze. Die mechanistische Verbindung ist schwach.

### Weitere vorhergesagte Indikationen

Alle weiteren Vorhersagen liegen ebenfalls nur auf Evidenzstufe L5 (Empfehlung: Hold):

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Mechanistische Einschätzung |
|----|------|------|------|
| 2 | Pseudo-von-Willebrand-Erkrankung | 0,9997 | Gain-of-function-Defekt des thrombozytären GPIbα; FVIII korrigiert diesen nicht, Verbindung spekulativ |
| 3 | Glanzmann-Thrombasthenie | 0,9996 | Defekt von Integrin αIIbβ3; Standard sind Thrombozytentransfusion oder rFVIIa, keine mechanistische Grundlage für FVIII |
| 4 | Erworbener Gerinnungsfaktormangel | 0,9988 | Am ehesten plausibel (z. B. erworbene Hämophilie A), doch Inhibitoren neutralisieren den FVIII; Standard sind Bypass-Präparate oder porcines FVIII |
| 5 | Scott-Syndrom | 0,9986 | Defekt der Phosphatidylserin-Exposition (TMEM16F/ANO6); lose Verbindung über den Tenase-Komplex, zusätzlicher FVIII ersetzt die fehlende Membranoberfläche nicht |
| 6 | Blutungsneigung durch Kollagenrezeptor-Defekt | 0,9973 | Thrombozyten-intrinsisches Problem, durch FVIII nicht korrigierbar |
| 7 | Hämorrhagische Störung durch konstitutionelle Thrombozytopenie | 0,9972 | FVIII beeinflusst die Thrombozytenzahl nicht |
| 8 | „Flood factor deficiency" | 0,9911 | Bezeichnung unklar, möglicherweise ein Ontologie- oder Eingabefehler; Identität vorab prüfen |

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000232 | ReFacto AF | – | Hämophilie A |

Hinweis: Diese Zulassung (Pfizer Europe MA EEIG) ist als erloschen/gelöscht geführt.

---

## Sicherheitsaspekte

Für Sicherheitsinformationen beachten Sie bitte die Packungsbeilage. Zu Wechselwirkungen wurden in den für diesen Bericht zusammengestellten Daten keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Alle vorhergesagten Indikationen stützen sich ausschließlich auf Modellwerte (Evidenzstufe L5) ohne Studien oder Publikationen. Zudem sprechen die Pathomechanismen überwiegend gegen eine Wirksamkeit von FVIII-Ersatz, und die deutsche Zulassung ist erloschen.

**Für ein Weiterkommen sind erforderlich:**
- Beschaffung und Auswertung der Packungsbeilage (Warnhinweise, Gegenanzeigen) als Voraussetzung für die Sicherheitsprüfung
- Daten zum Wirkmechanismus (z. B. aus DrugBank)
- Prüfung der Identität von „flood factor deficiency"
- Gezielte Literatur- und Studienrecherche, insbesondere zum erworbenen Gerinnungsfaktormangel (erworbene Hämophilie A) als mechanistisch plausibelstem Kandidaten
- Klärung der Applikationswege und der Übereinstimmung mit der ursprünglichen Indikation
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

