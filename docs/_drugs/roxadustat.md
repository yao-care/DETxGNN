---
layout: default
title: Roxadustat
parent: Nur Modellvorhersage (L5)
nav_order: 414
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Roxadustat: vorhergesagte neue Indikation Trockenes-Auge-Syndrom (dry eye syndrome) (Evidenzstufe L5). Ursprüngliche Indikation: Anämie"
monitor_inn: "ROXADUSTAT"
predicted_indications: ["dry eye syndrome", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma"]
---

# Roxadustat
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

## Roxadustat: Von renaler Anämie zu Trockenes-Auge-Syndrom
{: .text-alpha }

## Zusammenfassung

Roxadustat ist ein HIF-Prolylhydroxylase-Inhibitor, der ursprünglich zur Behandlung der Anämie bei chronischer Niereninsuffizienz zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er für das **Trockene-Auge-Syndrom** (dry eye syndrome) wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht ausschließlich auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Anämie; chronische Niereninsuffizienz |
| Vorhergesagte neue Indikation | Trockenes-Auge-Syndrom (dry eye syndrome) |
| TxGNN-Vorhersagewert | 0,9951 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut ChEMBL (EMBL-EBI) ist für Roxadustat folgender Wirkmechanismus erfasst (inoffizielle Übersetzung): „Hypoxie-induzierbarer-Faktor-Prolylhydroxylase-Inhibitor“. Englischer Originalwortlaut: "Hypoxia-inducible factor prolyl hydroxylase inhibitor" ([ChEMBL CHEMBL2338329 (roxadustat): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2338329), CC BY-SA 3.0; abgerufen am 2026-11-19). Bekannt ist, dass Roxadustat ein HIF-Prolylhydroxylase-Inhibitor ist: Es stabilisiert HIF-1α/2α und fördert dadurch unter anderem die Erythropoetin-Bildung, was seine Wirksamkeit bei Anämie bei chronischer Niereninsuffizienz erklärt. Die EMA hat Roxadustat im August 2021 für diese Indikation zugelassen.

Zwischen renaler Anämie und Trockenem Auge besteht keine unmittelbare klinische Verwandtschaft. Ein möglicher Zusammenhang ergibt sich nur über die HIF-Signalwege, die Entzündung der Augenoberfläche, die Epithelreparatur und die Angiogenese beeinflussen könnten. Die HIF-Aktivierung kann jedoch auch pathologische Neovaskularisation fördern. Die Verbindung ist daher spekulativ: Der TxGNN-Wert ist eine rein graphbasierte Vorhersage.

Weitere vom Modell genannte Kandidaten (alle ebenfalls nur Evidenzniveau L5, Empfehlung Hold):

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Paget-Krankheit des Knochens | 0,9912 | Theoretischer Bezug über HIF und Knochenumbau; Wirkrichtung unklar |
| 3 | Dentinogenesis imperfecta | 0,9906 | Mechanismus unklar; erbliche Strukturstörung kaum medikamentös korrigierbar |
| 4 | Plattenepithelkarzinom | 0,9902 | HIF-Aktivierung ist eher mit Tumorprogression verbunden; eher Sicherheitsbedenken als Therapieansatz |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/004871 | Evrenzo | roxadustat | Anemia; Kidney Failure, Chronic | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitshinweise

- **Wechselwirkungen / pharmakologische Interaktion:** Roxadustat hemmt das Ziel EGLN2 (egl-9 family hypoxia inducible factor 2), eine HIF-Prolylhydroxylase. Dies ist der pharmakologische Wirkmechanismus; ein Schweregrad ist nicht angegeben.
- **Theoretisches Risiko:** Da die HIF-Aktivierung Angiogenese und Tumorprogression fördern kann, ist bei Indikationen wie Plattenepithelkarzinom oder bei Erkrankungen mit pathologischer Neovaskularisation (z. B. am Auge) besondere Vorsicht geboten.

Für weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für das Trockene-Auge-Syndrom stützt sich allein auf das TxGNN-Modell (Evidenzniveau L5), ohne klinische Studien oder Publikationen. Die HIF-Aktivierung birgt theoretische Risiken (Neovaskularisation).

<!-- review:begin de-lic-20261106-roxadustat-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Zudem ist die Zulassung in Deutschland erloschen, und die HIF-Aktivierung birgt theoretische Risiken (Neovaskularisation).“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-roxadustat-1 -->

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen) als Voraussetzung für die Sicherheitsprüfung
- Ergänzung der Wirkmechanismus-Daten (z. B. aus DrugBank)
- Präklinische Daten zu HIF-Stabilisierung an der Augenoberfläche, einschließlich Abwägung gegen Neovaskularisationsrisiko
- Prüfung der Anwendungswege (z. B. topische Darreichung), da bisher nur eine systemische Anwendung bekannt ist
- Literatur- und Studienrecherche zu den vorhergesagten Indikationen

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Zudem ist die Zulassung in eutschland erloschen, und d“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt (überarbeitet am 2026-11-20; frühere Fassung im Protokoll erhalten) | [ChEMBL CHEMBL2338329 (roxadustat): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2338329) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

