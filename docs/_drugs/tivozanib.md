---
layout: default
title: Tivozanib
parent: Nur Modellvorhersage (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: Von unbestimmter ursprünglicher Indikation bis Endozervixkarzinom (vorhergesagt)

## Zusammenfassung in einem Satz

Tivozanib wird in diesem Beweispaket als hochselektiver VEGFR-1/2/3-Tyrosinkinase-Inhibitor beschrieben, aber seine ursprünglich zugelassene Indikation ist hier nicht dokumentiert — das Arzneimittel ist in Deutschland nicht registriert (0 Zulassungen) und sowohl der Wirkmechanismus als auch die regulatorischen Sicherheitsdaten sind als Datenlücken gekennzeichnet (DG001/DG002). Das TxGNN-Modell sagt mögliche Wirksamkeit bei **Endozervixkarzinom** vorher, aber dies wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — eine rein computergestützte (L5) Vorhersage.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in diesem Beweispaket dokumentiert (keine Lizenzeinträge, `original_indications` leer) |
| Vorhergesagte neue Indikation | Endozervixkarzinom |
| TxGNN-Vorhersage-Punktzahl | 99.81% |
| Evidenzebene | L5 |
| Marktstatus Deutschland | Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

## Warum ist diese Vorhersage sinnvoll?

Das formale `original_moa`-Feld ist als Datenlücke gekennzeichnet (DG002). Das Beweispaket beschreibt Tivozanib jedoch als hochselektiven VEGFR-1/2/3-Tyrosinkinase-Inhibitor, der mechanistisch durch die Unterdrückung der Tumorangiogenese wirkt.

Da es in diesem Beweispaket keine zugelassene Indikation und keinen Lizenznachweis gibt, kann die Beziehung zwischen der ursprünglichen (realen) Indikation von Tivozanib und der vorhergesagten neuen Indikation anhand der hier bereitgestellten Daten nicht hergestellt werden — diese Lücke sollte vor weiterer Bewertung behoben werden.

Das mechanistische Argument für Endozervixkarzinom ist rein analogisch: Antiangiogene Mittel (z. B. Bevacizumab) werden bereits bei Gebärmutterhalskrebs verwendet, daher ist VEGFR-Blockade grundsätzlich plausibel. Bemerkenswert ist, dass alle Top-10-TxGNN-Vorhersagen für dieses Arzneimittel seltene gynäkologische (Gebärmutterhals-/Uterusligament-)Karzinom-Subtypen sind, die jeweils als L5/Halten ohne unterstützende Studien oder Literatur bewertet werden — was darauf hindeutet, dass das Modell eine breite „VEGF-abhängige gynäkologische Tumor"-Assoziation erfasst hat, statt indikationsspezifische Evidenz.

## Klinische Studiennachweise

Derzeit keine verwandten klinischen Studien registriert.

## Literaturnachweis

Derzeit keine verwandte Literatur verfügbar.

## Informationen zum Markt in Deutschland

Tivozanib wird derzeit in Deutschland nicht vermarktet; es gibt keine Zulassungseinträge in diesem Beweispaket (0 Lizenzen).

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie (VEGFR-1/2/3-Tyrosinkinase-Inhibitor / antiangiogen) |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |
| Überwachungspunkte | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |
| Handhabungsschutz | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Alle vorhergesagten Indikationen für dieses Arzneimittel sind Evidenzebene L5 (nur Modellvorhersage, keine unterstützenden Studien oder Literatur), und eine blockierende Datenlücke (DG001 — TFDA-Warnhinweise/Gegenanzeigen) verhindert derzeit das S1-Sicherheits-Screening.

**Um fortzufahren, ist Folgendes erforderlich:**
- DG001 beheben: TFDA-/regulatorische Kennzeichnungswarnhinweise und Gegenanzeigen erhalten (blockierend)
- DG002 beheben: Wirkmechanismus über DrugBank-API bestätigen
- Tatsächliche zugelassene Indikation(en) von Tivozanib identifizieren, da es in diesem Beweispaket keinen Lizenz-/Indikationseintrag gibt
- Gezielte Literatur- und klinische Studiensuche nach VEGFR-Inhibitoren bei gynäkologischen (Gebärmutterhals-/Uterusligament-)Karzinom-Subtypen
- Neubewertung, sobald die Evidenzebene über L5 hinausgeht

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

