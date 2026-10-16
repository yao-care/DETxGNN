---
layout: default
title: Olaparib
parent: Hohe Evidenz (L1-L2)
nav_order: 326
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Olaparib: vorhergesagte neue Indikation Weibliches Mammakarzinom (Evidenzstufe L1). Ursprüngliche Indikation: Ovarialkarzinom"
---

# Olaparib
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **1** 
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

# Olaparib: Von Ovarial-, Brust-, Pankreas- und Prostatakarzinom zum weiblichen Mammakarzinom

## Zusammenfassung

Olaparib ist ein oraler PARP-Inhibitor (Handelsname Lynparza), der ursprünglich zur Behandlung von Ovarial-, Brust-, Pankreas- und kastrationsresistentem Prostatakarzinom zugelassen wurde.
Das TxGNN-Modell sagt eine Wirksamkeit beim **weiblichen Mammakarzinom** voraus.
Die Richtung wird derzeit durch **29 klinische Studien** und **19 Publikationen** gestützt, darunter mehrere große randomisierte Phase-3-Studien (u. a. OlympiAD und OlympiA).

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Ovarialkarzinom; Mammakarzinom; Pankreaskarzinom; kastrationsresistentes Prostatakarzinom |
| Vorhergesagte neue Indikation | Weibliches Mammakarzinom |
| TxGNN-Vorhersagewert | 99,09 % |
| Evidenzstufe | L1 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine Angaben vor. Nach allgemeinem pharmakologischem Wissen hemmt Olaparib das Enzym PARP. Dadurch bleiben Einzelstrangbrüche der DNA unrepariert und werden bei der Replikation zu Doppelstrangbrüchen. Zellen ohne funktionierende BRCA-vermittelte homologe Rekombination (z. B. bei Keimbahnmutationen in BRCA1/2) können diese Brüche nicht reparieren und sterben ab (synthetische Letalität).

Der Mechanismus ist derselbe, der den bereits zugelassenen Indikationen (Ovarial-, Pankreas- und Prostatakarzinom) zugrunde liegt. Die Daten führen das Mammakarzinom bereits unter den ursprünglichen Indikationen auf. Es handelt sich daher eher um eine bereits validierte Indikation als um ein echtes Repurposing. Der hohe TxGNN-Wert ist mit diesem Mechanismus konsistent.

Zu beachten sind Resistenzmechanismen (z. B. Stabilisierung der PARP1-mRNA über PCBP2, PMID 40773674) sowie der Nutzen, der auf biomarkerselektierte Populationen (Keimbahn-BRCA, HRR-Mutationen) beschränkt ist.

---

## Evidenz aus klinischen Studien

Es werden die relevantesten Studien aufgeführt (Bewertung A/B zuerst, dann weitere).

| Studiennummer | Phase | Status | Teilnehmerzahl | Zentrale Ergebnisse |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Abgeschlossen | 99 | Offene, nicht randomisierte Studie mit Olaparib (AZD2281) bei BRCA-Mutationsträgern mit Brust- und Ovarialkarzinom; direkter Wirksamkeitsnachweis (Proof of Concept) |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Abgeschlossen | 202 | Post-Marketing-Studie in Indien bei platinsensitivem Ovarialkarzinom und metastasiertem BRCA-mutiertem Mammakarzinom; Sicherheitsdaten |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Rekrutierend | 34 | Pembrolizumab + ablative Strahlentherapie ± Olaparib bei metastasiertem Mammakarzinom (TNBC bzw. HR+/HER2−) |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | Abgeschlossen | 118 | PI3K-Inhibitor (BKM120/BYL719) + Olaparib bei rezidiviertem TNBC oder serösem Ovarialkarzinom; Dosisfindung und Sicherheit |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | Abgeschlossen | 77 | PK/PD-Studie mit Olaparib + Carboplatin bei refraktären/rezidivierten gynäkologischen Tumoren |
| [NCT02684318](https://clinicaltrials.gov/study/NCT02684318) | Phase 1/2 | Unbekannt | 100 | Lurbinectedin (PM01183) + Olaparib bei fortgeschrittenen soliden Tumoren; keine bestätigten Ergebnisse |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | Aktiv, nicht rekrutierend | 155 | Cediranib + Olaparib vs. Olaparib allein bei rezidiviertem Ovarial- oder triple-negativem Mammakarzinom |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Abgeschlossen | 25 | Carboplatin-Olaparib gefolgt von Olaparib vs. Capecitabin bei BRCA-mutiertem HER2-negativem fortgeschrittenem Mammakarzinom |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Abgeschlossen | 24 | Olaparib mit Strahlentherapie bei TNBC |
| [NCT07695259](https://clinicaltrials.gov/study/NCT07695259) | Phase 4 | Rekrutierend | 45 | Olaparib + Trastuzumab/Pertuzumab neoadjuvant bei älteren Patientinnen mit HER2-positivem Mammakarzinom |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Zentrale Ergebnisse |
|------|-----|------|------|---------|
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: Olaparib bei metastasiertem Mammakarzinom mit Keimbahn-BRCA-Mutation |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvantes Olaparib bei BRCA1/2-mutiertem Mammakarzinom |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | Gesamtüberleben in OlympiA bei Hochrisiko-Mammakarzinom im Frühstadium mit gBRCA1/2-Variante |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD, finale Gesamtüberlebens- und Verträglichkeitsanalyse gegenüber Chemotherapie nach Arztwahl |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | Verlängerte Nachbeobachtung | Eur J Cancer | OlympiAD: medianes Gesamtüberleben 19,3 vs. 17,1 Monate (P = 0,513) in der finalen Analyse; verlängerte Nachbeobachtung zu Überleben und Sicherheit |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | Randomisierte Phase-2/3-Studie | Nature | PARTNER: neoadjuvantes Olaparib + Chemotherapie bei TNBC ohne Keimbahn-BRCA-Mutation (n = 559) |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase-2-Studie | J Clin Oncol | TBCRC 048: Olaparib bei metastasiertem Mammakarzinom mit Mutationen in HR-Reparaturgenen |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase-2-Studie | Cancer Cell | I-SPY2: Durvalumab + Olaparib + Paclitaxel bei HER2-negativem Hochrisiko-Mammakarzinom |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Phase-2-Studie | J Clin Oncol | Olaparib-Monotherapie bei fortgeschrittenen Krebserkrankungen mit Keimbahn-BRCA1/2-Mutation |
| [39742383](https://pubmed.ncbi.nlm.nih.gov/39742383/) | 2024 | Systematische Übersicht | Breast J | Zielgerichtete Therapie des metastasierten triple-negativen Mammakarzinoms |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003726 | Lynparza (AstraZeneca AB) | – | Ovarialkarzinom; Mammakarzinom; Pankreaskarzinom; kastrationsresistentes Prostatakarzinom (Status: erloschen) |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Klassifikation | Zielgerichtete Therapie (PARP-Inhibitor) |
| Myelosuppressionsrisiko | In den Daten nicht angegeben; bitte Fachinformation beachten |
| Emetogenität | In den Daten nicht angegeben; bitte Fachinformation beachten |
| Überwachungsparameter | Bitte Fachinformation beachten (üblicherweise Blutbild sowie Leber- und Nierenfunktion) |
| Handhabungsschutz | Bitte Fachinformation und Vorschriften für den Umgang mit zytotoxischen Arzneimitteln beachten |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Die Abfrage ergab insgesamt 100 Wechselwirkungen. Die ausgewerteten Einträge (DDInter) umfassen unter anderem:

- **Schwerwiegend (Major):** Aprepitant, Dexamethason, Clarithromycin
- **Mäßig (Moderate):** Metformin, Bupropion, Cimetidin, Miconazol, Clotrimazol, Glibenclamid, Ondansetron, Repaglinid, Rosuvastatin, Simvastatin sowie weitere
- **Gering (Minor):** Prucaloprid

Zu Warnhinweisen und Gegenanzeigen bitte die Fachinformation beachten.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Die Evidenz ist stark (L1): Mehrere große randomisierte Phase-3-Studien (OlympiAD, OlympiA) belegen den Nutzen bei biomarkerselektiertem Mammakarzinom (Keimbahn-BRCA). Der Nutzen ist jedoch auf bestimmte Populationen begrenzt, und die deutsche Zulassung ist derzeit nur als erloschen geführt.

**Für das weitere Vorgehen sind erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) von der BfArM-Webseite beschaffen und auswerten; dies ist für die Sicherheitsprüfung zwingend
- Daten zum Wirkmechanismus (MOA) aus DrugBank ergänzen
- Klärung des Zulassungsstatus in Deutschland (erloschene Zulassung) und Abgleich mit dem zentralen EU-Verfahren
- Festlegung der Zielpopulation (Keimbahn-BRCA, HER2-negativ, HRR-Mutationen) und Plan für Biomarkertestung
- Plan zur Überwachung von Wechselwirkungen (insbesondere CYP3A-Inhibitoren/-Induktoren) und Blutbildkontrollen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

