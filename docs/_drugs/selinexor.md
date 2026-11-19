---
layout: default
title: Selinexor
parent: Nur Modellvorhersage (L5)
nav_order: 422
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Selinexor: vorhergesagte neue Indikation Medikamenten-induzierte Osteoporose (Evidenzstufe L5). Ursprüngliche Indikation: Multiples Myelom"
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

## Selinexor: Medikamenteninduzierte Osteoporose
{: .text-alpha }

## Zusammenfassung

Selinexor wurde ursprünglich zur Behandlung des Multiplen Myeloms eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei **medikamenten-induzierter Osteoporose** wirksam sein könnte. Diese Vorhersage stützt sich bislang **ausschließlich auf den Modellscore**: Es liegen **keine klinischen Studien** und **keine Publikationen** vor.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Multiples Myelom |
| Vorhergesagte neue Indikation | Medikamenten-induzierte Osteoporose |
| TxGNN-Vorhersagescore | 0.9922 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Selinexor (inoffizielle Übersetzung): „In nichtklinischen Studien hemmt Selinexor reversibel den Kernexport von Tumorsuppressorproteinen (TSPs), Wachstumsregulatoren und mRNAs onkogener Proteine, indem es Exportin 1 (XPO1) blockiert. Die Hemmung von XPO1 durch Selinexor führt zur Akkumulation von TSPs im Zellkern und zur Verringerung mehrerer Onkoproteine wie c-myc und Cyclin D1, zum Zellzyklusarrest sowie zur Apoptose von Krebszellen.“ Englischer Originalwortlaut: "In nonclinical studies, selinexor reversibly inhibits nuclear export of tumor suppressor proteins (TSPs), growth regulators, and mRNAs of oncogenic proteins by blocking exportin 1 (XPO1). XPO1 inhibition by selinexor leads to accumulation of TSPs in the nucleus and reductions in several oncoproteins, such as c-myc and cyclin D1, cell cycle arrest, and apoptosis of cancer cells." ([DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8), Fassung vom 2026-05-12; abgerufen am 2026-11-19). Selinexor ist allgemein als Inhibitor von XPO1 (Exportin-1) bekannt, und seine Wirksamkeit beim Multiplen Myelom ist belegt. Mechanistisch könnte eine XPO1-Hemmung die Knochenumbauprozesse beeinflussen, etwa die Signalwege von Osteoklasten und Osteoblasten oder die myelombedingte Knochenerkrankung.

Dieser Zusammenhang ist **spekulativ** und durch die vorliegenden Daten nicht belegt. Vor einer klinischen Betrachtung wäre eine präklinische Validierung nötig, zum Beispiel in Knochenzell- oder Tiermodellen. Zudem könnten bekannte Nebenwirkungen von Selinexor (Übelkeit, Appetitlosigkeit, Gewichtsverlust, Müdigkeit) die Knochengesundheit beeinträchtigen. Die Sicherheit in einer Osteoporose-Population ist daher nicht etabliert.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005127 | Nexpovio | – | Multiples Myelom |

Die Zulassung ist gültig: Von 1 Zulassung ist 1 gültig; das Arzneimittel ist in diesem Land im Handel.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (XPO1-Inhibitor) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Emetogenitätsklassifikation | Bitte Fachinformation beachten (Übelkeit ist eine bekannte Nebenwirkung) |
| Überwachungsparameter | Bitte Fachinformation beachten |
| Schutzmaßnahmen beim Umgang | Bitte Fachinformation beachten |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 81 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind u. a.:
  - Deferipron
  - Samarium (153Sm) Lexidronam
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribin
  - Clozapin
- **Mäßig (Moderate)** eingestuft sind u. a.: Strontiumchlorid Sr-89, Roflumilast, Chloramphenicol, Zidovudin, Azathioprin, Alemtuzumab, Anakinra, Canakinumab sowie mehrere Impfstoffe (u. a. Tetanus-Toxoid, Anthrax, Cholera-Lebendimpfstoff).
- Weitere Warnhinweise und Gegenanzeigen entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht allein auf einem hohen TxGNN-Score (Evidenzniveau L5), ohne klinische Studien oder Literatur. Die Sicherheitsdaten sind lückenhaft.

<!-- review:begin de-lic-20261106-selinexor-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Zudem ist die Zulassung in Deutschland erloschen, und die Sicherheitsdaten sind lückenhaft.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-selinexor-1 -->

**Für ein Weiterkommen sind folgende Schritte erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) beschaffen und auswerten, da dies für das Sicherheitsscreening zwingend nötig ist
- Detaillierte Daten zum Wirkmechanismus (MOA) ergänzen
- Präklinische Validierung der XPO1-Hemmung im Knochenstoffwechsel (Knochenzell- und Tiermodelle)
- Sicherheitsbewertung für Osteoporose-Patienten, insbesondere im Hinblick auf Gewichtsverlust und Appetitlosigkeit
- Klärung des Zulassungsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Zudem ist die Zulassung in eutschland erloschen, und d“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

