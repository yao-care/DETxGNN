---
layout: default
title: Orlistat
parent: Nur Modellvorhersage (L5)
nav_order: 332
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat: vorhergesagte neue Indikation Hypervitaminose (hypervitaminosis) (Evidenzstufe L5). Ursprüngliche Indikation: Obesity"
---

# Orlistat
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

## Orlistat: Hypervitaminose (hypervitaminosis)
{: .text-alpha }

## Zusammenfassung

Orlistat ist ein Lipasehemmer, der ursprünglich zur Behandlung von **Adipositas** zugelassen wurde. Das TxGNN-Modell sagt voraus, dass der Wirkstoff bei **Hypervitaminose** wirksam sein könnte. Für diese Richtung liegen derzeit **keine klinischen Studien und keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Obesity |
| Vorhergesagte neue Indikation | Hypervitaminose (hypervitaminosis) |
| TxGNN-Vorhersagewert | 0.9942 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl der Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Orlistat (inoffizielle Übersetzung): „Orlistat ist ein reversibler Inhibitor gastrointestinaler Lipasen. Es entfaltet seine therapeutische Wirkung im Lumen des Magens und des Dünndarms, indem es eine kovalente Bindung mit dem aktiven Serinrest der Magen- und Pankreaslipasen eingeht.“ Englischer Originalwortlaut: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), Fassung vom 2026-09-30; abgerufen am 2026-11-19). Bekannt ist, dass Orlistat ein Hemmer der gastrischen und pankreatischen Lipase ist und die Absorption von Nahrungsfett um etwa 30 % senkt. Die Wirksamkeit bei Adipositas ist belegt.

Da durch die verminderte Fettresorption auch fettlösliche Vitamine (A, D, E, K) schlechter aufgenommen werden, ließe sich theoretisch ein Nutzen bei einer Hypervitaminose durch fettlösliche Vitamine ableiten. Diese Verbindung beruht jedoch auf einer bekannten Nebenwirkung (Vitaminmalabsorption) und nicht auf therapeutischen Belegen. Der hohe TxGNN-Wert spiegelt vermutlich den bekannten Einfluss auf Vitaminspiegel wider und nicht ein validiertes Therapiesignal.

Hinzu kommt, dass eine Hypervitaminose in der Regel durch Absetzen des Präparats oder der Vitaminquelle behandelt wird. Der klinische Zusatznutzen eines weiteren Wirkstoffs mit gastrointestinalen Nebenwirkungen ist daher unklar.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000154 | Xenical | orlistat | Obesity | Gültig |
| EMEA/H/C/000854 | Alli (previously Orlistat GSK) | orlistat | Obesity | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph (TxGNN/PrimeKG, nicht aus dem Beipackzettel):** Leberversagen, primäre Hyperoxalurie, Anorexia nervosa, Bulimia nervosa, Vitaminmangelerkrankungen, Cholestase, benigne rekurrente intrahepatische Cholestase, familiäre intrahepatische Cholestase, arzneimittelinduzierte Leberschädigung.
- **Arzneimittelwechselwirkungen:** Es wurden 100 Wechselwirkungen erfasst (Quelle: DDInter). Beispiele:
  - *Moderat:* Abacavir, Lamivudine, Emtricitabine, Atazanavir, Acarbose, Albiglutide, Alogliptin, Metformin, Canagliflozin, Chlorpropamide, Amiodarone, Cannabidiol, Clofarabine, Brentuximab vedotin, Asparaginase (E. coli und Erwinia chrysanthemi), Calaspargase pegol
  - *Gering:* Cholecalciferol, Calcifediol, Calcitriol

Besonders relevant für die vorgeschlagene Indikation: Mit den Vitamin-D-Präparaten (Cholecalciferol, Calcifediol, Calcitriol) bestehen Wechselwirkungen, und die Kontraindikation bei Vitaminmangelerkrankungen betrifft genau den Wirkmechanismus. Weitere Sicherheitsinformationen entnehmen Sie bitte der Packungsbeilage.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf ein Modell (Evidenzgrad L5), ohne Studien oder Publikationen. Der postulierte Mechanismus leitet sich aus einer Nebenwirkung ab, und die Standardtherapie (Absetzen der Vitaminquelle) ist einfach und wirksam.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Vollständige Wirkmechanismus-Daten (MOA), z. B. aus DrugBank
- Warnhinweise und Kontraindikationen aus der Fachinformation (z. B. über BfArM bzw. EMA), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Präklinische oder klinische Hinweise, dass Orlistat Vitaminspiegel bei Hypervitaminose sinnvoll senken kann
- Bewertung der Nutzen-Risiko-Relation gegenüber dem Absetzen der Vitaminquelle sowie der Vereinbarkeit mit den Kontraindikationen
- Klärung der Zulassungs- und Verfügbarkeitslage in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

