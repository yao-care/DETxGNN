---
layout: default
title: Rufinamide
parent: Nur Modellvorhersage (L5)
nav_order: 415
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "RUFINAMIDE"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: vorhergesagte neue Indikation Perioral myoclonia with absences (Evidenzstufe L5). Ursprüngliche Indikation: Epilepsy"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## Zusammenfassung

Rufinamid ist ein Antikonvulsivum, das ursprünglich zur Behandlung von Epilepsie zugelassen wurde. Das TxGNN-Modell sagt voraus, dass es bei dem **febrilen infektionsassoziierten Epilepsiesyndrom (FIRES)** wirksam sein könnte. Für diese Vorhersage liegen derzeit **keine klinischen Studien und keine Publikationen** vor; sie beruht allein auf der Modellberechnung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Epilepsy |
| Vorhergesagte neue Indikation | Perioral myoclonia with absences |
| TxGNN-Vorhersagewert | 0.9951 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Rufinamide (inoffizielle Übersetzung): „Der genaue Mechanismus bzw. die genauen Mechanismen, durch die Rufinamid seine antiepileptische Wirkung entfaltet, ist bzw. sind unbekannt. Die Ergebnisse von In-vitro-Studien deuten darauf hin, dass der hauptsächliche Wirkmechanismus von Rufinamid in der Modulation der Aktivität von Natriumkanälen und insbesondere in der Verlängerung des inaktiven Zustands des Kanals besteht.“ Englischer Originalwortlaut: "The precise mechanism(s) by which rufinamide exerts its antiepileptic effect is unknown. The results of in vitro studies suggest that the principal mechanism of action of rufinamide is modulation of the activity of sodium channels and, in particular, prolongation of the inactive state of the channel." ([DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d), Fassung vom 2022-12-15; abgerufen am 2026-11-19). Nach allgemeinem Wissen moduliert Rufinamid spannungsabhängige Natriumkanäle und verlängert deren inaktiven Zustand. Es ist bei Epilepsie, insbesondere beim Lennox-Gastaut-Syndrom, zugelassen.

**Weitere vorhergesagte Indikationen** (jeweils ohne Studien oder Literatur, Evidenzgrad L5, Empfehlung Hold):

| Rang | Erkrankung | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Perioralle Myoklonien mit Absencen | 0,9951 | Generalisiertes Epilepsiesyndrom; Natriumkanalblocker können manche generalisierten Anfallsformen verschlechtern, daher ist die Passung unsicher |

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000660 | Inovelon | rufinamide | Epilepsy | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Diese Zulassung ist gültig; in Deutschland besteht derzeit 1 gültige Zulassung von 1.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (TxGNN/PrimeKG, nicht aus dem Beipackzettel): Leberversagen, Angststörung, neurotische Störung, dysthyme Störung, Lebererkrankung, Gallenblasenerkrankung, Leukopenie.
- **Arzneimittelwechselwirkungen**: Es wurden 100 Wechselwirkungen erfasst, die gezeigten Einträge sind alle von mittlerem Schweregrad (Moderate). Beispiele: Hydrocortison, Prednison, Betamethason, Triamcinolon, Cholecalciferol, Calcitriol, Pioglitazon, Bupropion, Morphin, Metoclopramid, Ondansetron, Dronabinol, Nabilon.

Für weitere Sicherheitsinformationen (Warnhinweise, Kontraindikationen laut Fachinformation) bitte die Packungsbeilage bzw. Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das TxGNN-Modell (Evidenzgrad L5), ohne klinische Studien oder Publikationen.

**Für ein Weiterkommen sind erforderlich:**
- Daten zum Wirkmechanismus (MoA) aus DrugBank
- Warnhinweise und Kontraindikationen aus der Fachinformation (BfArM/EMA); ohne diese ist die Sicherheitsprüfung nicht möglich
- Literaturrecherche und Prüfung von Studienregistern zu Rufinamid bei FIRES und den weiteren vorhergesagten Epilepsiesyndromen
- Klärung des Zulassungsstatus und der verfügbaren Darreichungsformen und Applikationswege

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

