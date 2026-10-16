---
layout: default
title: Sacituzumab Govitecan
parent: Nur Modellvorhersage (L5)
nav_order: 417
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Sacituzumab Govitecan: vorhergesagte neue Indikation Medikamenteninduzierte Osteoporose (Evidenzstufe L5). Ursprüngliche Indikation: Brustneubildungen"
monitor_inn: "SACITUZUMAB GOVITECAN"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
---

# Sacituzumab Govitecan
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Sacituzumab Govitecan: Von Brustkrebs zu medikamenteninduzierter Osteoporose

## Zusammenfassung

Sacituzumab Govitecan ist ein Antikörper-Wirkstoff-Konjugat, das ursprünglich zur Behandlung von Brustneubildungen, einschließlich des triple-negativen Mammakarzinoms, eingesetzt wird. Das TxGNN-Modell sagt voraus, dass es bei **medikamenteninduzierter Osteoporose** wirksam sein könnte. Diese Vorhersage wird jedoch durch **keine klinische Studie** und **keine Publikation** gestützt; sie beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Brustneubildungen; triple-negatives Mammakarzinom |
| Vorhergesagte neue Indikation | Medikamenteninduzierte Osteoporose |
| TxGNN-Vorhersagewert | 99,78 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Sacituzumab Govitecan ein gegen Trop-2 gerichtetes Antikörper-Wirkstoff-Konjugat ist, dessen Nutzlast SN-38 ein Topoisomerase-I-Inhibitor ist. Es wirkt gegen proliferierende Epithelzellen von Tumoren.

Ein mechanistischer Zusammenhang zwischen dieser Wirkung und der Behandlung der medikamenteninduzierten Osteoporose ist anhand der vorliegenden Daten nicht erkennbar. Zytotoxische Nutzlasten gelten eher als knochenschädigend denn als knochenschützend, und eine knochenprotektive Wirkung ist nicht bekannt. Der hohe TxGNN-Wert (0,998) ist wahrscheinlich ein Artefakt der Konnektivität im Wissensgraphen.

Weitere vorhergesagte Indikationen (jeweils ebenfalls nur Modellvorhersage, Evidenzgrad L5, Empfehlung Hold):

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Schwere nichtproliferative diabetische Retinopathie | 99,69 % | Kein direkter mechanistischer Zusammenhang; ein myelosuppressives Zytostatikum wäre bei einer nicht-onkologischen Augenerkrankung ein ungünstiges Nutzen-Risiko-Verhältnis. |
| 3 | Diabetische Retinopathie | 99,60 % | Stark mit Rang 2 korreliert, daher kein unabhängiges Signal; etablierte Therapien (Anti-VEGF, Laser, Kortikosteroide) sind deutlich besser belegt. |
| 4 | Diabetische Katarakt | 99,12 % | Entsteht vor allem durch Polyolweg-Aktivität und oxidativen Stress in der Linse, ohne Bezug zu Trop-2 oder Topoisomerase I; Standard ist die Operation. |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005182 | Trodelvy | – | Brustneubildungen; triple-negatives Mammakarzinom |

Der Status dieser Zulassung lautet „erloschen/widerrufen“; es besteht derzeit keine gültige Zulassung.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Antikörper-Wirkstoff-Konjugat mit zytotoxischer Nutzlast (Topoisomerase-I-Inhibitor SN-38) |
| Myelosuppressionsrisiko | Hoch (Neutropenie wird für diese Wirkstoffklasse erwartet) |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Differenzialblutbild, Leber- und Nierenfunktion |
| Handhabungsschutz | Vorschriften für den Umgang mit zytotoxischen Arzneimitteln beachten |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Für diesen Bericht wurden 40 Wechselwirkungen erfasst. Die ausgewerteten Beispiele umfassen:

- **Schwerwiegend (Major):** Deferipron, Fostamatinib, Adalimumab, Apalutamid, Certolizumab pegol, Cladribin, Dacomitinib, Irinotecan, Leflunomid, Natalizumab, Nilotinib, Ozanimod
- **Moderat (Moderate):** Alefacept, Alemtuzumab, Anakinra, Canakinumab, Dimethylfumarat, Lorlatinib, Ocrelizumab, Omacetaxin-Mepesuccinat

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersagen beruhen ausschließlich auf dem Modell (Evidenzgrad L5), ohne Studien oder Literatur und ohne plausiblen Mechanismus. Zudem ist das Sicherheitsprofil eines myelosuppressiven Zytostatikums für nicht-onkologische Indikationen ungünstig, und in Deutschland besteht keine gültige Zulassung.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) von BfArM beschaffen und auswerten (blockierende Datenlücke)
- Daten zum Wirkmechanismus ergänzen (z. B. über DrugBank)
- Präklinische Belege für einen Zusammenhang mit Knochenstoffwechsel oder den anderen vorhergesagten Indikationen prüfen
- Klärung des Zulassungsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

