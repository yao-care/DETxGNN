---
layout: default
title: Canakinumab
parent: Nur Modellvorhersage (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: Bewertung unvollständig — Keine TxGNN-Vorhersage verfügbar

## Zusammenfassung in einem Satz

Canakinumab (DB06168, Handelsname: Ilaris) ist ein vollständig humanisierter monoklonaler Antikörper gegen Interleukin-1β (IL-1β), der weit verbreitet bei autoinflammatorischen Erkrankungen eingesetzt wird.
Das aktuelle Evidence Pack enthält **keine von TxGNN vorhergesagten Indikationen** und mehrere blockierende Datenlücken, was eine umfassende Bewertung der Arzneimittelumpositionierung in diesem Stadium unmöglich macht.
**Sofortige Datenbereinigung ist erforderlich, bevor dieser Kandidat voranschreitet.**

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht im Evidence Pack verfügbar |
| Vorhergesagte neue Indikation | Keine — TxGNN-Ergebnisse nicht geladen |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | N/A — keine Vorhersagen verfügbar |
| Taiwan-Marktstatus | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum diese Bewertung nicht fortgesetzt werden kann

Das Evidence Pack für Canakinumab (DB06168) weist Eingaben auf zwei Ebenen auf:

**1. Kein Umpositionierungsziel identifiziert**
Das Array `predicted_indications` ist leer. Ohne eine von TxGNN vorhergesagte Indikation gibt es keine Umpositionierungshypothese zum Bewerten, und die Kernstruktur dieses Berichts — mechanistische Plausibilität, Evidenz aus klinischen Studien und Literaturunterstützung — kann nicht zusammengestellt werden.

**2. Datenlücken auf Arzneimittelebene blockieren Sicherheits- und Mechanismusbewertung**

| Lücken-ID | Element | Schweregrad | Auswirkung |
|-----------|---------|-------------|-----------|
| DG001 | TFDA-Packungsbeilage (Warnhinweise / Kontraindikationen) | **Blockierend** | Sicherheits-Vorprüfung (S1) kann nicht abgeschlossen werden |
| DG002 | Wirkmechanismus (MOA) | Hoch | Analyse der mechanistischen Plausibilität blockiert |

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar. Basierend auf allgemeinem pharmakologischen Wissen ist Canakinumab ein Anti-IL-1β-Biologikum; seine Wirksamkeit bei autoinflammatorischen Erkrankungen wurde etabliert, und sein entzündungshemmender Mechanismus ist mechanistisch relevant für eine breite Palette von entzündlichen und metabolischen Erkrankungen. Allerdings kann eine formale MOA-zu-Indikations-Zuordnung ohne bestätigte DrugBank-Daten im Evidence Pack nicht generiert werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Kein Umpositionierungskandidat wurde von TxGNN identifiziert, und zwei blockierende/schwerwiegende Datenlücken verhindern sowohl Sicherheits- als auch mechanistische Bewertung. Der Kandidat kann nicht voranschreiten, bis das Evidence Pack abgeschlossen und erneut ausgeführt wird.

**Um fortzufahren, ist folgendes erforderlich:**

- **Führe die TxGNN-Vorhersage-Pipeline aus** für DB06168, um `predicted_indications`-Einträge mit Scores, klinischen Studien und Literatur zu generieren
- **Rufe MOA von der DrugBank-API ab** (DG002-Behebung) — rufe `/drugs/DB06168` ab für `mechanism-of-action`, `pharmacodynamics` und `targets`
- **Lade die TFDA-Packungsbeilage-PDF herunter und analysiere sie** (DG001-Behebung) — extrahiere Warnhinweise, Kontraindikationen und spezielle Populationsbeschränkungen
- **Regeneriere das Evidence Pack** mit allen bestätigten Eingaben, bevor der nächste Bewertungszyklus eingeleitet wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

