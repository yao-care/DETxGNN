---
layout: default
title: Trastuzumab Deruxtecan
parent: Nur Modellvorhersage (L5)
nav_order: 411
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Trastuzumab Deruxtecan: Von HER2-exprimierenden Tumoren zu arzneimittelinduzierter Osteoporose

## Zusammenfassung in einem Satz

Trastuzumab deruxtecan ist ein HER2-gezieltes Antikörper-Wirkstoff-Konjugat (ADK), das einen zytotoxischen Topoisomerase-I-Inhibitor (DXd) zu HER2-exprimierenden Tumorzellen transportiert. Das TxGNN-Modell prognostiziert, dass es bei **arzneimittelinduzierter Osteoporose** wirksam sein könnte, aber diese Richtung wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt, und die zugrunde liegende Rationale deutet darauf hin, dass das Signal wahrscheinlich ein Wissensgraph-Artefakt ist, anstatt eines echten therapeutischen Effekts.

---

## Schnellübersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar — `original_indications` ist leer und kein formaler Indikationstext liegt vor (Datenlücke) |
| Prognostizierte neue Indikation | Arzneimittelinduzierte Osteoporose |
| TxGNN-Prognosescore | 99.31% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus Deutschland | Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Ausgesetzt |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten in diesem Evidenzpaket nicht verfügbar (`original_moa` ist eine Datenlücke). Basierend auf den an diesen Kandidaten angehängten mechanistischen Notizen ist bekannt, dass Trastuzumab deruxtecan als ein HER2-gezieltes ADK fungiert, das eine zytotoxische Topoisomerase-I-Inhibitor-Nutzlast zu HER2-exprimierenden Tumorzellen transportiert — ein Mechanismus, der für die Onkologie relevant ist, nicht für den Knochenstoffwechsel.

Es gibt keinen bekannten oder in der Literatur gestützten Mechanismus, durch den dieses Arzneimittel die Aktivität von Osteoklasten/Osteoblasten oder Knochenumbaupfade wie RANKL/OPG modulieren würde. Klinisch sind zytotoxische Chemotherapien und ADKs viel häufiger mit arzneimittelinduzierter Osteoporose als **Ursache** (Behandlungsnebenwirkung) verbunden, anstatt als **Behandlung** dafür.

Angesichts des hohen TxGNN-Scores (0.993) in Kombination mit dem völligen Fehlen klinischer Studien oder Literatur ist die plausibelste Erklärung, dass der Wissensgraph eine Kopräsenz-Beziehung zwischen „Krebstherapie-Arzneimittel"-Knoten und „Chemotherapie-assoziierter Knochenverlust"-Knoten aufgreift, anstatt ein echtes therapeutisches Signal. Diese Vorhersage sollte als biologisch implausibel behandelt werden, bis sie durch neue Evidenz widerlegt wird.

---

## Klinische Studienevidenz

Derzeit keine registrierten klinischen Studien vorhanden

---

## Literaturevidenz

Derzeit keine verwandte Literatur verfügbar

---

## Marktstatus Deutschland

Trastuzumab deruxtecan hat derzeit keine deutsche Marktzulassung in der Akte (`total_licenses = 0`, `market_status = Not marketed / Not marketed`).

---

## Zytotoxizität

| Artikel | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie — Antikörper-Wirkstoff-Konjugat (ADK) mit zytotoxischem Topoisomerase-I-Inhibitor-Nutzlast |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |
| Überwachungspunkte | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |
| Handhabungsschutz | Muss den Bestimmungen für die Handhabung zytotoxischer/ADK-Arzneimittel entsprechen |

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Hinweis: Eine kritische Datenlücke liegt vor — Warnungen im TFDA-Etikett und Kontraindikationen (DG001) wurden nicht abgerufen. Dies verhindert eine formale S1-Sicherheitsvoruntersuchung für diesen Kandidaten.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Ausgesetzt**

**Begründung:**
Die Vorhersage wird durch keine klinischen Studien, keine Literatur und keine plausible mechanistische Verbindung gestützt — der bekannte zytotoxische ADK-Mechanismus des Arzneimittels ist konsistenter mit der *Verursachung* von Knochenverlust als mit dessen Behandlung. Kombiniert mit einer kritischen Datenlücke bei der TFDA-Sicherheitskennzeichnung ist dieser Kandidat nicht bereit, über Stadium S0 hinaus voranzuschreiten.

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA/BfArM-Packungsbeilage (Warnungen, Kontraindikationen) zur Behebung von DG001
- Bestätigte ursprüngliche Indikation und Wirkmechanismus (DG002)
- Präklinische oder mechanistische Evidenz, die HER2-ADK/Topoisomerase-I-Hemmung mit Knochenmetabolismuspfaden verbindet, falls dieses Signal weiter verfolgt werden soll
- Unabhängige Überprüfung, um Wissensgraph-Kopräsenz-Artefakte auszuschließen, bevor weitere Investitionen getätigt werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

