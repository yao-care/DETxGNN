---
layout: default
title: Reteplase
parent: Nur Modellvorhersage (L5)
nav_order: 396
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "RETEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "heparin cofactor 2 deficiency", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "antithrombin deficiency type 2", "hemolytic anemia due to glucophosphate isomerase deficiency"]
description: "Reteplase: vorhergesagte neue Indikation Congenital coronary artery anomaly (Evidenzstufe L5). Ursprüngliche Indikation: Myocardial Infarction"
---

# Reteplase
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

## Reteplase: Congenital coronary artery anomaly
{: .text-alpha }

## Zusammenfassung

Reteplase ist ein rekombinanter Gewebeplasminogenaktivator (Thrombolytikum), der ursprünglich zur Behandlung des akuten Myokardinfarkts zugelassen wurde. Das TxGNN-Modell sagt voraus, dass er bei **posterolateralem Myokardinfarkt** wirksam sein könnte. Dabei handelt es sich jedoch um einen anatomischen Untertyp der bereits zugelassenen Indikation und nicht um eine echte neue Indikation. Die Evidenz ist gering: **0 klinische Studien** und **1 Publikation** (ein Fallbericht, der Reteplase nicht untersucht).

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Myocardial Infarction |
| Vorhergesagte neue Indikation | Congenital coronary artery anomaly |
| TxGNN-Vorhersagewert | 0.9980 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Zentrale EU-Zulassung (EMA) erloschen (1 von 1) – nationale Zulassungen (BfArM) sind in den hier ausgewerteten Daten nicht enthalten |
| Anzahl der Zulassungen | 1 (gültig: 0) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut ChEMBL (EMBL-EBI) ist für Reteplase folgender Wirkmechanismus erfasst (inoffizielle Übersetzung): „Exogenes Gewebe-Plasminogenaktivator-Protein“. Englischer Originalwortlaut: "Tissue-type plasminogen activator exogenous protein" ([ChEMBL CHEMBL2107885 (reteplase): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2107885), CC BY-SA 3.0; abgerufen am 2026-11-19). Bekannt ist: Reteplase ist ein rekombinanter Gewebeplasminogenaktivator. Er aktiviert Plasminogen zu Plasmin und löst dadurch Fibrinthromben (Thrombolyse) in verschlossenen Koronararterien auf. Seine Wirksamkeit beim akuten Myokardinfarkt ist etabliert.

Der posterolaterale Myokardinfarkt ist ein anatomischer Untertyp des Myokardinfarkts. Der Mechanismus (Wiedereröffnung des thrombotisch verschlossenen Koronargefäßes) ist daher grundsätzlich übertragbar. Der sehr hohe TxGNN-Wert spiegelt wahrscheinlich die Nähe in der Krankheitsontologie zur ursprünglichen Indikation wider und nicht neue Evidenz. Es handelt sich somit nicht um einen echten Repurposing-Kandidaten.

Weitere Vorhersagen mit hohen Werten sind teils mechanistisch kaum plausibel (z. B. Chromosomendeletion, Glukosephosphat-Isomerase-Mangel). Die Werte stammen vom TxGNN-Modell (Deep Learning) und können vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen widerspiegeln, nicht biologische Evidenz.

---

## Klinische Studienevidenz

Derzeit sind keine einschlägigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Fallbericht | Catheterization and Cardiovascular Interventions | Primäre PCI mit Drug-Eluting-Stents bei ungeschütztem Hauptstamm in einem 37-jährigen Patienten mit posterolateralem Infarkt, unterstützt durch intrakoronares Reteplase. Einzelfall, keine Wirksamkeitsprüfung. |

---

## Marktinformationen Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000105 | Rapilysin | reteplase | Myocardial Infarction | Zurückgezogen |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Diese Zulassung ist erloschen bzw. widerrufen (Status: cancelled). Zulassungsinhaber war Actavis Group PTC ehf.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Die Abfrage ergab insgesamt 100 Wechselwirkungen (Quelle: DDInter). Beispiele:
  - **Schwerwiegend (Major)**: Abciximab, Apixaban, Betrixaban, Acalabrutinib, Avapritinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab. Meist handelt es sich um additive Blutungsrisiken.
  - **Moderat**: Acetylsalicylsäure, Ibuprofen, Ketorolac, Celecoxib, Diclofenac (topisch), Aminocapronsäure, Omega-3-Fettsäuren, Fenfluramin, Dexfenfluramin, Sibutramin.

Weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage betrifft einen Untertyp der bereits zugelassenen Indikation Myokardinfarkt, keine neue Indikation. Es gibt keine klinischen Studien, und der einzige Literaturnachweis ist ein Fallbericht, der Reteplase nicht untersucht. Zudem ist die deutsche/europäische Zulassung erloschen.

**Für ein Weiterkommen sind folgende Schritte erforderlich:**
- Klärung, ob eine Bewertung als eigenständige Indikation überhaupt sinnvoll ist (da Untertyp der zugelassenen Indikation)
- Daten zum Wirkmechanismus (MOA) aus DrugBank ergänzen
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM/EMA) beschaffen, da dies derzeit ein blockierender Datenmangel für die Sicherheitsprüfung ist
- Klärung der Gründe für das Erlöschen der Zulassung und der aktuellen Verfügbarkeit
- Prüfung der Studien GUSTO-V und SPEED (PMID 15800019, 11079647) auf Design und Relevanz, sofern ein breiterer Koronarkontext verfolgt wird

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt (überarbeitet am 2026-11-20; frühere Fassung im Protokoll erhalten) | [ChEMBL CHEMBL2107885 (reteplase): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2107885) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

