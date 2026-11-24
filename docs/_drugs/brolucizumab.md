---
layout: default
title: Brolucizumab
parent: Nur Modellvorhersage (L5)
nav_order: 79
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Brolucizumab: vorhergesagte neue Indikation Mitochondriale Störung der oxidativen Phosphorylierung durch Kern-DNA-Anomalien (Evidenzstufe L5). Ursprüngliche Indikation: Feuchte Makuladegeneration"
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices without bleeding", "esophageal varices with bleeding", "exocrine pancreatic insufficiency"]
---

# Brolucizumab
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

## Brolucizumab: Von feuchter Makuladegeneration zu Mitochondriale Störung der oxidativen Phosphorylierung durch Kern-DNA-Anomalien
{: .text-alpha }

## Zusammenfassung

Brolucizumab ist ein gegen VEGF-A gerichtetes Antikörperfragment (scFv), das ins Auge injiziert wird und ursprünglich zur Behandlung der **feuchten Makuladegeneration** zugelassen wurde.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei einer **mitochondrialen Störung der oxidativen Phosphorylierung durch nukleäre DNA-Anomalien** voraus.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Feuchte Makuladegeneration |
| Vorhergesagte neue Indikation | Mitochondriale Störung der oxidativen Phosphorylierung durch nukleäre DNA-Anomalien |
| TxGNN-Vorhersagewert | 0,9967 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Brolucizumab (inoffizielle Übersetzung): „Brolucizumab ist ein humaner VEGF-Inhibitor. Brolucizumab bindet an die drei Hauptisoformen von VEGF-A (z. B. VEGF 110, VEGF 121 und VEGF 165 ) und verhindert dadurch die Interaktion mit den Rezeptoren VEGFR-1 und VEGFR-2. Durch die Hemmung von VEGF-A unterdrückt Brolucizumab die Endothelzellproliferation, die Neovaskularisation und die Gefäßpermeabilität.“ Englischer Originalwortlaut: "Brolucizumab is a human VEGF inhibitor. Brolucizumab binds to the three major isoforms of VEGF-A (e.g., VEGF 110, VEGF 121, and VEGF 165 ), thereby preventing interaction with receptors VEGFR-1 and VEGFR-2. By inhibiting VEGF-A, brolucizumab suppresses endothelial cell proliferation, neovascularization, and vascular permeability." ([DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d), Fassung vom 2026-10-26; abgerufen am 2026-11-19). Bekannt ist, dass Brolucizumab ein VEGF-A-Inhibitor in Form eines Einzelketten-Antikörperfragments ist, der für die intravitreale Anwendung mit sehr geringer systemischer Exposition vorgesehen ist.

Primäre mitochondriale Störungen der oxidativen Phosphorylierung entstehen durch Defekte in nukleär kodierten Untereinheiten oder Assemblierungsfaktoren der Atmungskette. Die Hemmung von VEGF-A greift an dieser Ursache nicht an. Ein klarer mechanistischer Zusammenhang zur ursprünglichen Indikation ist daher nicht erkennbar.

Der sehr hohe TxGNN-Wert spiegelt lediglich eine Vorhersage des TxGNN-Modells (Deep Learning) wider und wird durch keine Studie gestützt. Zudem könnte eine systemische VEGF-Blockade bei metabolisch vulnerablen Patienten eher schaden als nützen.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

<!-- review:begin de-lic-20261106-brolucizumab-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Diese Zulassung ist erloschen (Status: Cancelled).“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-brolucizumab-1 -->

---

## Marktinformationen Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/004913 | Beovu | brolucizumab | Wet Macular Degeneration | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (PrimeKG, nicht aus der Fachinformation):** Uveitis, Iriserkrankung, Ziliarkörpererkrankung, Panuveitis, infektiöse Augenerkrankung, Konjunktivitis.
- **Hinweis zur Klasse:** Anti-VEGF-Wirkstoffe sind mit Blutungs-, Thromboembolie- und Wundheilungsrisiken verbunden; bei einer systemischen Anwendung in einer metabolisch vulnerablen Population ist Vorsicht geboten.
- **Arzneimittelwechselwirkungen:** Keine Einträge gefunden.

Für weitere Sicherheitsinformationen ist die Fachinformation heranzuziehen.

---

## Weitere vorhergesagte Indikationen

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Evidenzniveau | Einschätzung |
|---|---|---|---|---|
| 2 | Ösophagusvarizen ohne Blutung | 0,9912 | L5 | Hold. Spekulativer Zusammenhang über VEGF-getriebene Angiogenese bei portaler Hypertonie; bei intravitrealer Anwendung ist keine relevante splanchnische Wirkung zu erwarten. Etablierte Standardtherapie vorhanden. |
| 3 | Ösophagusvarizen mit Blutung | 0,9912 | L5 | Hold. Gleiche Überlegung, zusätzlich Sicherheitsbedenken (Blutungsrisiko unter Anti-VEGF) bei akuter Varizenblutung. |
| 4 | Exokrine Pankreasinsuffizienz | 0,9907 | L5 | Hold. Kein plausibler mechanistischer Zusammenhang; Therapie erfolgt durch Enzymersatz. |

Für alle drei Indikationen liegen weder Studien noch Literatur vor.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (L5) ohne Studien oder Publikationen. Es gibt keinen plausiblen mechanistischen Zusammenhang. Zudem könnte eine systemische VEGF-Blockade bei dieser Patientengruppe schädlich sein.

<!-- review:begin de-lic-20261106-brolucizumab-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Es gibt keinen plausiblen mechanistischen Zusammenhang, und die einzige deutsche Zulassung ist erloschen.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-brolucizumab-2 -->

**Für ein Weiterverfolgen wären erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Präklinische Belege für einen Zusammenhang zwischen VEGF-A-Hemmung und mitochondrialen Erkrankungen
- Bewertung der Applikationsroute (intravitreal vs. systemisch) und der Sicherheit bei systemischer Exposition

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Diese Zulassung ist erloschen (Status: Cancelled)“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „und die einzige deutsche Zulassung ist erloschen“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

