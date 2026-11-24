---
layout: default
title: Safinamide
parent: Nur Modellvorhersage (L5)
nav_order: 419
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Safinamide: vorhergesagte neue Indikation Rasmussen-Enzephalitis (Rasmussen subacute encephalitis) (Evidenzstufe L5). Ursprüngliche Indikation: Parkinson-Krankheit"
monitor_inn: "safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Safinamide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Safinamid: Von Parkinson-Krankheit zu Rasmussen-Enzephalitis
{: .text-alpha }

## Zusammenfassung

Safinamid wurde ursprünglich zur Behandlung der Parkinson-Krankheit zugelassen. Das TxGNN-Modell sagt voraus, dass es bei **Rasmussen-Enzephalitis (subakute Enzephalitis)** wirksam sein könnte. Hierfür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Parkinson-Krankheit |
| Vorhergesagte neue Indikation | Rasmussen-Enzephalitis (Rasmussen subacute encephalitis) |
| TxGNN-Vorhersagewert | 0,9963 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Safinamide (inoffizielle Übersetzung): „Der genaue Mechanismus, über den XADAGO seine therapeutische Wirkung bei PD ausübt, ist nicht bekannt. XADAGO ist ein Inhibitor der Monoaminoxidase B (MAO-B). Es wird angenommen, dass die Hemmung der MAO-B-Aktivität durch Blockade des Dopaminabbaus zu einem Anstieg der Dopaminspiegel und in der Folge zu einer Zunahme der dopaminergen Aktivität im Gehirn führt.“ Englischer Originalwortlaut: "The precise mechanism by which XADAGO exerts its therapeutic effects in PD is unknown. XADAGO is an inhibitor of monoamine oxidase B (MAO-B). Inhibition of MAO-B activity, by blocking the catabolism of dopamine, is thought to result in an increase in dopamine levels and a subsequent increase in dopaminergic activity in the brain." ([DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2), Fassung vom 2026-10-05; abgerufen am 2026-11-19). Aus der Literatur ist jedoch bekannt, dass Safinamid ein reversibler MAO-B-Hemmer ist, der zudem spannungsabhängige Natriumkanäle blockiert und die Glutamatfreisetzung hemmt. Diese Eigenschaften könnten theoretisch neuronale Übererregbarkeit und Exzitotoxizität verringern.

Die Rasmussen-Enzephalitis ist eine chronisch-entzündliche Epilepsie mit T-Zell-vermitteltem neuronalem Schaden und therapieresistenten Anfällen. Eine antikonvulsive bzw. neuroprotektive Wirkung von Safinamid wäre daher denkbar. Allerdings wird die Erkrankung überwiegend durch immunvermittelte Prozesse getrieben, die Safinamid nicht adressiert.

Die Verbindung ist damit eine plausible, aber nicht belegte Hypothese, die allein auf dem hohen TxGNN-Wert beruht.

Weitere vorhergesagte Indikationen (ebenfalls L5, jeweils Hold):
- **Myelitis** (Score 0,9946): unspezifischer Zusammenhang; mögliche neuroprotektive Effekte ohne Hinweis auf Wirkung bei entzündlicher oder demyelinisierender Rückenmarksschädigung.
- **PLA2G6-assoziierte Neurodegeneration** (Score 0,9922): biologisch am stimmigsten, da einige Phänotypen Parkinsonismus und Dystonie umfassen; der zugrunde liegende Lipidstoffwechseldefekt würde jedoch nicht behandelt.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/002396 | Xadago | safinamide methanesulfonate | Parkinson Disease | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Insgesamt wurden 110 Wechselwirkungen erfasst. Auszug:
- **Schwerwiegend (Major):** Bupropion
- **Moderat:** Isomethepten, Chlorpropamid, Diethylpropion, Phentermin, Metoclopramid, Rosuvastatin sowie mehrere Antidiabetika (u. a. Empagliflozin, Glimepirid, Nateglinid, Repaglinid, Acetohexamid) und verschiedene Insuline (u. a. Insulin aspart, degludec, detemir, glargin, glulisin, Humaninsulin)

Für Warnhinweise und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (Evidenzgrad L5); es gibt weder klinische Studien noch Publikationen. Zudem ist das Arzneimittel in Deutschland in Verkehr (1 von 1 Zulassungen gültig), und die Krankheitsursache der Rasmussen-Enzephalitis (Immunpathologie) wird durch den Wirkmechanismus von Safinamid nicht adressiert.

**Für ein Weiterkommen sind erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) zur Sicherheitsbewertung, derzeit ein blockierender Datenmangel
- Detaillierte Wirkmechanismusdaten (z. B. aus DrugBank)
- Präklinische Daten oder Fallberichte zur Rasmussen-Enzephalitis
- Klärung des Zulassungs- und Verfügbarkeitsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-12 | Tabelle: Xadago (EMEA/H/C/002396) ist gültig, nicht erloschen | Durch die programmatisch erzeugte Zulassungstabelle ersetzt (vorher: Korrigiert) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

