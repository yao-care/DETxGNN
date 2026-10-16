---
layout: default
title: Oteracil
parent: Nur Modellvorhersage (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Oteracil: vorhergesagte neue Indikation Kolonneoplasie (colonic neoplasm) (Evidenzstufe L5). Ursprüngliche Indikation: Magenkarzinom (Stomach Neoplasms)"
monitor_inn: "OTERACIL"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "rectosigmoid junction neoplasm", "benign neoplasm of cecum", "colonic lymphangioma", "colon leiomyoma", "cavernous hemangioma of colon"]
---

# Oteracil
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

# Oteracil: Von Magenkarzinom zu Kolonneoplasie

## Zusammenfassung

Oteracil ist ein Bestandteil der S-1-Kombination (Tegafur/Gimeracil/Oteracil) und wurde ursprünglich zur Behandlung des Magenkarzinoms eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei **Kolonneoplasie** (Dickdarmtumor) wirksam sein könnte. Die vorliegenden Daten umfassen **6 klinische Studien** und **10 Publikationen**, die sich jedoch fast ausschließlich auf das gesamte S-1-Schema beziehen und nicht auf Oteracil als Einzelsubstanz.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Magenkarzinom (Stomach Neoplasms) |
| Vorhergesagte neue Indikation | Kolonneoplasie (colonic neoplasm) |
| TxGNN-Vorhersagewert | 99,99 % |
| Evidenzlevel | L1 (formal; Evidenz bezieht sich auf das S-1-Gesamtschema, nicht auf Oteracil allein) |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails (Fortsetzen mit Schutzmaßnahmen) |

---

## Warum ist diese Vorhersage plausibel?

Oteracil (Kaliumoxonat) ist ein Bestandteil der S-1-Kombination aus Tegafur, Gimeracil und Oteracil. Es hemmt die Orotat-Phosphoribosyltransferase in der Magen-Darm-Schleimhaut und verringert dadurch die lokale Aktivierung von 5-FU, wodurch die gastrointestinale Toxizität sinkt. **Oteracil besitzt keine eigene Antitumorwirkung.** Die Antitumorwirkung des S-1-Schemas wird von Tegafur (5-FU-Prodrug) und Gimeracil (DPD-Inhibitor) getragen.

Das Magenkarzinom und der Dickdarmtumor sind beides gastrointestinale Tumoren, die auf Fluoropyrimidine ansprechen. Die ursprüngliche Zulassung bezog sich ebenfalls auf die S-1-Kombination. Der Zusammenhang für Oteracil ist daher **unterstützend (Toxizitätsminderung)** und nicht direkt wirksamkeitsbezogen. Für das S-1-Schema liegen Phase-3-Daten bei Kolon- und Kolorektalkarzinom vor, diese lassen sich aber nicht Oteracil als Einzelsubstanz zuschreiben.

Detaillierte Mechanismusdaten (MOA) aus DrugBank liegen in den für diesen Bericht zusammengestellten Daten nicht vor; die obige Beschreibung stützt sich auf die mechanistische Begründung der Analyse.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Zentrale Ergebnisse |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Abgeschlossen | 1535 | UFT+Leucovorin vs. TS-1 (S-1) als adjuvante Therapie bei Kolonkarzinom Stadium III; stärkste Evidenz für das S-1-Schema |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unbekannt | 1191 | SOX (Oxaliplatin + S-1) vs. XELOX als adjuvante Chemotherapie bei kolorektalem Karzinom Stadium III |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unbekannt | 40 | S-1 + Bevacizumab bei nicht resezierbarem/rezidivierendem kolorektalem Karzinom nach Vorbehandlung |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unbekannt | 82 | Raltitrexed + S-1 bei metastasiertem kolorektalem Karzinom; Endpunkt: progressionsfreies Überleben |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Rekrutierung noch nicht begonnen | 52 | Fruquintinib + Tegafur/Gimeracil/Oteracil in der Drittlinie bei metastasiertem kolorektalem Karzinom (einarmig) |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Abgebrochen | 20 | S-1 bzw. Capecitabin mit Oxaliplatin; Auswirkungen auf den koronaren Blutfluss (Sicherheitsendpunkt) |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Zentrale Ergebnisse |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Retrospektive Kohortenstudie | Gan to Kagaku Ryoho | Risikofaktoren für schwere hämatologische Toxizität (Grad 3–4: 16,1 %) unter S-1/Irinotecan bei 87 Patienten mit fortgeschrittenem Kolonkarzinom |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Präklinisch (Xenograft) | Oncology Reports | Irinotecan überwindet die 5-FU-Resistenz in Kolonkarzinom-Xenografts; Kombination mit S-1 steigerte die Antitumoraktivität |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Fallbericht | J Oncol Pharm Pract | Hypertriglyzeridämie unter S-1 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Fallbericht | Eur J Dermatol | TS-1-induzierte Erythrodermie mit ausgedehntem Schleimhautbefall und Hand-Fuß-Syndrom |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Fallbericht | Gan to Kagaku Ryoho | Harnverhalt als Folge einer oxaliplatininduzierten akuten peripheren Neuropathie |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Fallbericht | Anticancer Research | Komplettremission bei Leberfiliae eines Kolonkarzinoms unter S-1 + CPT-11 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Fallbericht | Gan to Kagaku Ryoho | Zweizeitige Hepatektomie nach SOX plus Panitumumab bei nicht resektablen kolorektalen Lebermetastasen |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Fallbericht | Gan to Kagaku Ryoho | Wiederholte laparoskopische Resektion peritonealer Rezidive nach kolorektaler Resektion |

Hinweis: Es wurden keine randomisierten kontrollierten Studien oder systematischen Übersichten in der Literatur gefunden; die Evidenz besteht überwiegend aus Fallberichten.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/001242 | Teysuno | – | Stomach Neoplasms (Magenkarzinom); Status: erloschen |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Bestandteil eines konventionell zytotoxischen Fluoropyrimidin-Schemas (S-1); Oteracil selbst wirkt nicht antitumoral |
| Myelosuppressionsrisiko | Für das S-1-Schema relevant: In einer Kohorte unter S-1/Irinotecan traten bei 16,1 % hämatologische Toxizitäten Grad 3–4 auf |
| Emetogenitätsklassifikation | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Differentialblutbild, Leber- und Nierenfunktion |
| Handhabungsschutz | Handhabung gemäß den Vorschriften für Zytostatika |

---

## Sicherheitsaspekte

Für Oteracil liegen in den zusammengestellten Daten keine Warnhinweise, Kontraindikationen oder Wechselwirkungsdaten vor. Bitte die Fachinformation zu Sicherheitsinformationen heranziehen.

Aus der Literatur zum S-1-Schema sind folgende Nebenwirkungen berichtet: Hand-Fuß-Syndrom, Erythrodermie mit Schleimhautbeteiligung, Hypertriglyzeridämie und hämatologische Toxizität.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Für das S-1-Schema liegen Phase-3-Studien bei Kolon- und Kolorektalkarzinom vor, darunter eine abgeschlossene Studie mit 1535 Teilnehmern. Oteracil trägt jedoch nur über die Toxizitätsminderung bei und hat keine eigene Antitumorwirkung. Die Evidenz ist daher nicht auf Oteracil als Einzelsubstanz übertragbar. Zudem ist die einzige deutsche Zulassung erloschen.

**Für das weitere Vorgehen erforderlich:**
- Fachinformation (Warnhinweise und Kontraindikationen) von der BfArM-Website beschaffen und auswerten (blockierende Datenlücke für die Sicherheitsprüfung)
- Mechanismusdaten (MOA) aus DrugBank ergänzen
- Klären, ob eine Bewertung nur als Bestandteil des S-1-Gesamtschemas sinnvoll ist, und den regulatorischen Status in Deutschland prüfen (erloschene Zulassung)
- Sicherheits-Monitoringplan für das Fluoropyrimidin-Schema erstellen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

