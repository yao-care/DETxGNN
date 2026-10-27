---
layout: default
title: Cetuximab
parent: Nur Modellvorhersage (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cetuximab: vorhergesagte neue Indikation Chondroid-Hamartom (Evidenzstufe L5). Ursprüngliche Indikation: Kopf-Hals-Tumoren"
monitor_inn: "CETUXIMAB"
predicted_indications: ["chondroid hamartoma", "non-seminomatous lesion", "ductal or ductular proliferation", "bronchial adenomas/carcinoids childhood", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "epiglottis neoplasm", "cystic neoplasm", "pre-malignant neoplasm"]
---

# Cetuximab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

## Cetuximab: Von Kopf-Hals- und Kolorektalkarzinom zu Chondroid-Hamartom (Top-Vorhersage) – mit Schwerpunkt auf besser belegten Kandidaten
{: .text-alpha }

## Kurzzusammenfassung

Cetuximab ist ein gegen den EGF-Rezeptor (EGFR) gerichteter Antikörper, der ursprünglich zur Behandlung von Kopf-Hals-Tumoren und kolorektalen Tumoren zugelassen wurde.
Das TxGNN-Modell sagt für den Spitzenkandidaten **Chondroid-Hamartom** einen sehr hohen Score voraus, jedoch ohne jegliche klinische Studien oder Publikationen. Besser belegt sind die Kandidaten **zystische Neoplasie** (insbesondere adenoid-zystisches Karzinom, **4 Studien**, **20 Publikationen**) und **prämaligne Neoplasie** (**4 Studien**, **2 Publikationen**).

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Kopf-Hals-Tumoren; kolorektale Tumoren |
| Vorhergesagte neue Indikation (Rang 1) | Chondroid-Hamartom |
| TxGNN-Vorhersagewert (Rang 1) | 99,95 % |
| Evidenzniveau (Rang 1) | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

Weitere Kandidaten im Überblick:

| Rang | Indikation | TxGNN-Score | Evidenzniveau | Empfehlung |
|------|------|------|------|------|
| 3 | Duktale/duktuläre Proliferation (vermutlich Pankreas-Adenokarzinom) | 99,95 % | L4 | Hold |
| 6 | Odontogene Zyste | 99,95 % | L4 | Hold |
| 9 | Zystische Neoplasie | 99,95 % | L2 | Forschungsfrage |
| 10 | Prämaligne Neoplasie | 99,95 % | L2 | Forschungsfrage |

Die übrigen Kandidaten (Rang 2, 4, 5, 7, 8) stützen sich ausschließlich auf die Modellvorhersage (L5).

---

## Warum ist diese Vorhersage plausibel?

Für diesen Bericht liegen derzeit keine detaillierten Daten zum Wirkmechanismus vor. Bekannt ist, dass Cetuximab ein Antikörper gegen den EGFR ist und bei EGFR-exprimierenden Kopf-Hals- und kolorektalen Tumoren eingesetzt wird. Mechanistisch kommt es daher vor allem für EGFR-abhängige Epithelumoren in Betracht.

Für den Spitzenkandidaten **Chondroid-Hamartom** ist keine EGFR-abhängige Biologie belegt; es handelt sich um eine gutartige Läsion. Dasselbe gilt für nicht-seminomatöse Läsionen, kindliche bronchiale Adenome/Karzinoide und die Thyreoglossus-Zyste. Die Vorhersage ist hier rein statistisch.

Plausibler sind zwei andere Kandidaten:

- **Prämaligne Neoplasie:** EGFR ist in prämalignen Läsionen des oberen Aerodigestivtrakts überexprimiert, und die Literatur stützt EGFR-gerichtete Chemoprävention bei Kopf-Hals-Tumoren. Eine abgeschlossene Phase-II-Studie prüfte Cetuximab als Monotherapie bei Hochrisikoläsionen.
- **Zystische Neoplasie:** Das stärkste Signal betrifft das adenoid-zystische Karzinom und Speicheldrüsenkarzinome, in denen EGFR exprimiert wird. Eine Phase-II-Studie zeigte allerdings nur begrenzte Aktivität.

Beim Kandidaten **duktale Proliferation** (wahrscheinlich Pankreas-Adenokarzinom) sind EGFR- und KRAS-Signalwege relevant, doch KRAS-vermittelte Resistenz gegen Anti-EGFR-Antikörper schwächt die Rationale, und die Zuordnung der Erkrankung ist unklar.

---

## Klinische Studienevidenz

**Rang 1 (Chondroid-Hamartom):** Derzeit sind keine zugehörigen klinischen Studien registriert.

**Rang 9 – Zystische Neoplasie**

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | Unbekannt | 49 | Cetuximab mit IMRT und Kohlenstoffionen-Boost beim adenoid-zystischen Karzinom; direkt relevant |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Phase 1 | Abgeschlossen | 43 | Erlotinib plus Cetuximab bei fortgeschrittenen Tumoren; nicht spezifisch |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Abgeschlossen | 66 | Erlotinib, Cetuximab und Bevacizumab bei soliden Tumoren; nur indirekt relevant |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Phase 1 | Abgeschlossen | 12 | Cetuximab plus RAD001 (Everolimus) bei soliden Tumoren; klein, unspezifisch |

**Rang 10 – Prämaligne Neoplasie**

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Phase 2 | Abgeschlossen | 35 | Cetuximab als Monotherapie bei prämalignen Hochrisikoläsionen des oberen Aerodigestivtrakts; direkt relevant |
| [NCT00482222](https://clinicaltrials.gov/study/NCT00482222) | Phase 3 | Unbekannt | 340 | Oxaliplatin/Fluoropyrimidin ± Cetuximab bei resektablen kolorektalen Lebermetastasen; Bezug zu prämalignen Läsionen unklar |
| [NCT00719199](https://clinicaltrials.gov/study/NCT00719199) | Phase 1 | Abgebrochen | 21 | FOLFIRI plus Cetuximab plus IMO-2055 bei kolorektalem Karzinom; kein prämaligner Bezug |
| [NCT00537823](https://clinicaltrials.gov/study/NCT00537823) | Phase 2 | Abgebrochen | 9 | Kurze neoadjuvante FOLFOX-Therapie vor Leberresektion; schwacher Bezug |

---

## Literaturevidenz

**Rang 9 – Zystische Neoplasie (Auswahl)**

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Phase-II-Studie | Oral Oncology | Cetuximab bei rezidivierenden/metastasierten Speicheldrüsenkarzinomen (30 Patienten, davon 23 adenoid-zystisch); Bewertung des klinischen Nutzens |
| [30141310](https://pubmed.ncbi.nlm.nih.gov/30141310/) | 2018 | Kohorte | Asian Pac J Cancer Prev | Hautreaktionen und Tumorlokalisation als Prognosefaktoren beim metastasierten kolorektalen Karzinom unter Cetuximab |
| [21234529](https://pubmed.ncbi.nlm.nih.gov/21234529/) | 2011 | Kohorte | Strahlenther Onkol | IMRT-Rebestrahlung mit Cetuximab bei rezidivierendem Kopf-Hals-Tumor |
| [32518035](https://pubmed.ncbi.nlm.nih.gov/32518035/) | 2020 | Fallbericht | Oral Oncology | Cetuximab-Monotherapie bei rezidivierendem hochgradigem Mukoepidermoidkarzinom |
| [39415301](https://pubmed.ncbi.nlm.nih.gov/39415301/) | 2024 | Fallbericht | J Med Case Rep | Erfolgreiche Cetuximab-Gabe per Dosissteigerung bei schweren Infusionsreaktionen |
| [26245271](https://pubmed.ncbi.nlm.nih.gov/26245271/) | 2016 | Studie | Clin Oral Investig | Phosphorylierte EGFR-Expression und KRAS-Status bei Speicheldrüsenkarzinomen |

**Rang 10 – Prämaligne Neoplasie**

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Review | Oral Oncology | EGFR als Ziel der Chemoprävention bei Kopf-Hals-Tumoren; EGFR-Überexpression in oralen prämalignen Läsionen |
| [33243986](https://pubmed.ncbi.nlm.nih.gov/33243986/) | 2020 | Review | Nat Rev Dis Primers | Überblick über das Plattenepithelkarzinom im Kopf-Hals-Bereich |

**Rang 3 – Duktale Proliferation (Auswahl)**

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [35300246](https://pubmed.ncbi.nlm.nih.gov/35300246/) | 2022 | Randomisierte Phase-II-Studie | Clin Transl Radiat Oncol | Langzeitergebnisse von Cetuximab, Gemcitabin und Strahlentherapie beim lokal fortgeschrittenen Pankreaskarzinom (PARC) |
| [21552097](https://pubmed.ncbi.nlm.nih.gov/21552097/) | 2012 | Phase-II-Studie | Am J Clin Oncol | Gemcitabin, Oxaliplatin und Cetuximab beim fortgeschrittenen Pankreaskarzinom |
| [22571859](https://pubmed.ncbi.nlm.nih.gov/22571859/) | 2012 | Studie | Ann Oncol | Neoadjuvantes Cetuximab, Gemcitabin und IMRT beim Pankreasadenokarzinom |
| [27797376](https://pubmed.ncbi.nlm.nih.gov/27797376/) | 2017 | Präklinisch | Oncogene | Cetuximab-Resistenz beim PDAC über Integrin-β1/Src-Akt-Bypass |
| [23992319](https://pubmed.ncbi.nlm.nih.gov/23992319/) | 2014 | Review | Curr Med Chem | Zielgerichtete Therapien beim Pankreaskarzinom |

**Rang 6 – Odontogene Zyste:** Nur zwei Fallberichte (PMID [41546361](https://pubmed.ncbi.nlm.nih.gov/41546361/), 2025; [30576676](https://pubmed.ncbi.nlm.nih.gov/30576676/), 2019) zu primär intraossären Karzinomen, ohne direkten Cetuximab-Bezug.

Für die übrigen Kandidaten (Rang 1, 2, 4, 5, 7, 8) liegt derzeit keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000558 | Erbitux (Merck Europe B.V.) | – | Kopf-Hals-Tumoren; kolorektale Tumoren (Status: erloschen) |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (monoklonaler Anti-EGFR-Antikörper), kein klassisches Zytostatikum |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenität | Bitte Fachinformation beachten |
| Monitoring | Hautreaktionen, Infusionsreaktionen, Elektrolyte; bei Kombinationen Blutbild sowie Leber- und Nierenfunktion |
| Handhabungsschutz | Bitte Fachinformation und lokale Vorgaben zum Umgang mit Zytostatika/Onkologika beachten |

---

## Sicherheitsaspekte

- **Arzneimittelinteraktionen:** Insgesamt wurden 20 Einträge erfasst. Als **schwerwiegend (Major)** eingestuft sind **Aminolävulinsäure** und **Thalidomid**. Als **moderat** eingestuft sind u. a. Protonenpumpenhemmer (Rabeprazol, Omeprazol, Dexlansoprazol, Esomeprazol, Lansoprazol, Pantoprazol), Capecitabin, Carboplatin, Cisplatin, Fluorouracil, Oxaliplatin, Idelalisib, Methoxsalen, Omacetaxin-Mepesuccinat, Verteporfin sowie topische Aminolävulinsäure-Derivate.
- **Pharmakologisches Ziel:** Der Epidermale Wachstumsfaktor-Rezeptor (EGFR).
- **Aus der Literatur:** Haut- und Infusionsreaktionen sind relevant; bei Chemoprävention in gesunden oder Niedrigrisikopopulationen ist ein starker Sicherheitsspielraum erforderlich.

Weitere Sicherheitsinformationen entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold** (für den Spitzenkandidaten Chondroid-Hamartom und die übrigen rein modellbasierten Kandidaten); **Forschungsfrage** für prämaligne Neoplasie und zystische Neoplasie (adenoid-zystisches Karzinom).

**Begründung:**
- Der Spitzenkandidat stützt sich nur auf einen Modellwert ohne Studien, Publikationen oder plausible EGFR-Biologie.
- Die am besten belegten Signale (prämaligne Läsionen des oberen Aerodigestivtrakts, Speicheldrüsen- bzw. adenoid-zystische Karzinome) bleiben auf kleine Phase-1/2-Studien beschränkt; die Phase-3-Studie NCT00482222 testet Cetuximab nicht in prämalignen Läsionen. Ein höheres Evidenzniveau (L1) ist daher nicht gerechtfertigt. Zudem besteht für Cetuximab in Deutschland derzeit nur eine erloschene Zulassung.

**Für das weitere Vorgehen sind erforderlich:**
- Detaillierte Mechanismusdaten (MOA) aus DrugBank
- Fachinformation (Warnhinweise, Gegenanzeigen) des BfArM zur Sicherheitsbewertung
- Auswertung der Ergebnisse von NCT00524017 (prämaligne Läsionen) und NCT01192087 (adenoid-zystisches Karzinom)
- Klärung der Erkrankungszuordnung bei „duktaler Proliferation" sowie der Zulassungs- und Verfügbarkeitslage in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

