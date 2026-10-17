---
layout: default
title: Niraparib
parent: Nur Modellvorhersage (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Niraparib: vorhergesagte neue Indikation Zystische Neoplasie (Cystic Neoplasm) (Evidenzstufe L5). Ursprüngliche Indikation: Tuben-, Peritoneal- und Ovarialkarzinom"
monitor_inn: "NIRAPARIB"
predicted_indications: ["epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of hypopharynx", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "tumor of testis and paratestis", "inner ear neoplasm", "pre-malignant neoplasm", "schwannoma of jugular foramen"]
---

# Niraparib
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

# Niraparib: Von Eierstockkrebs zu zystischer Neoplasie (Cystic Neoplasm)

## Zusammenfassung

Niraparib ist ein PARP-Inhibitor, der ursprünglich zur Behandlung von Tuben-, Peritoneal- und Ovarialkarzinomen sowie (in Kombination, als Akeega) des kastrationsresistenten Prostatakarzinoms zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **zystischer Neoplasie (Cystic Neoplasm)** wirksam sein könnte. Die Evidenz dafür stützt sich auf **3 klinische Studien** (davon nur eine laufende Phase-2-Studie mit relevanten Daten) und **10 Publikationen**, die überwiegend das Ovarial- und Endometriumkarzinom betreffen.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Tuben-, Peritoneal- und Ovarialkarzinom |
| Vorhergesagte neue Indikation | Zystische Neoplasie (Cystic Neoplasm) |
| TxGNN-Vorhersagewert | 99,99 % |
| Evidenzgrad | L2 (vorläufig) |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassungen |
| Anzahl der Zulassungen | 2 (beide aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Für diesen Wirkstoff liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben zum Wirkmechanismus vor. Bekannt ist, dass Niraparib PARP1/2 hemmt und in Tumoren mit Defekten der homologen Rekombination (HRD) eine synthetische Letalität auslöst. Die Wirksamkeit bei Ovarialkarzinomen ist belegt.

Die Bezeichnung „zystische Neoplasie“ ist ein breiter Ontologiebegriff. Die zugeordnete Evidenz bezieht sich hauptsächlich auf seröse Ovarial- und Endometriumkarzinome, die den ursprünglichen Indikationen stark ähneln. Der Treffer ist daher teilweise ein Ontologie-Artefakt und kein klar abgegrenztes Repurposing-Signal. Die plausibelste Evidenz für eine neue Indikation ist die Phase-2-Studie zum serösen Endometriumkarzinom, das molekular dem hochgradig serösen Ovarialkarzinom ähnelt (Chromosomeninstabilität, Kopienzahlveränderungen, somatische Mutationen).

Die übrigen Top-10-Vorhersagen (z. B. Epiglottis-Neoplasie, gutartige Neoplasien von Zunge und Mundboden, Schwannom des Foramen jugulare) haben nur Modellgrundlage (L5), ohne Studien oder Literatur, und teils ohne mechanistische Begründung.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Teilnehmerzahl | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Phase 2 | Rekrutierend | 83 | Niraparib-Monotherapie als Erhaltungs- und Rezidivtherapie beim serösen Endometriumkarzinom; Ergebnisse liegen noch nicht vor |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Phase 2/3 | Abgebrochen | 11 | Multi-Arm-Studie zur Erstlinien- und Erhaltungstherapie bei serösem/p53-mutiertem Endometriumkarzinom; wegen sehr geringer Teilnehmerzahl nicht aussagekräftig |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Frühe Phase 1 | Zurückgezogen | 0 | Präoperatives Niraparib bei hochgradigem Endometriumkarzinom; keine Teilnehmer, keine Evidenz |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | Studienprotokoll (Phase 2) | BMJ Open | Niraparib-Erhaltungstherapie beim fortgeschrittenen oder rezidivierenden uterinen serösen Karzinom |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | Genomprofilierung | Pathology Oncology Research | HRD-Profilierung (FoundationOne CDx) zur Steuerung der PARP-Inhibitor-Therapie beim hochgradig serösen Ovarialkarzinom |
| [42442041](https://pubmed.ncbi.nlm.nih.gov/42442041/) | 2026 | Real-World-Kohorte | Gynecologic Oncology | HRD-Testung bei BRCA1/2-Wildtyp-HGSC; MYC-Amplifikation als möglicher Surrogatmarker |
| [42157333](https://pubmed.ncbi.nlm.nih.gov/42157333/) | 2026 | Retrospektive Kohorte | Clinical Epigenetics | Nomogramm auf Basis der HRR-Genpromotor-Methylierung zur Vorhersage des PARPi-Ansprechens |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | Fallbericht | BMJ Case Reports | Niraparib-Erhaltungstherapie bei Ovarialkarzinom mit Hirnmetastasen |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | Präklinisch | Cancer Research | Verlust der RAD51C-Promotormethylierung verursacht PARPi-Resistenz beim HGSC |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | Präklinisch | Cancer Biology & Therapy | Carboplatin plus PARPi in HGSC-Sphäroiden und -Organoiden |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | Präklinisch | Int J Mol Sci | Proteomanalyse der polypharmakologischen Effekte von PARP-Inhibitoren |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | Präklinisch | Scientific Reports | Claudin-4 als Regulator von Genomstabilität und Immunevasion beim HGSC |
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | Bioinformatik | J Ovarian Research | Stammzellbasierte Subtypen und Prognosemodell beim HGSOC |

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004249 | Zejula | – | Tuben-, Peritoneal- und Ovarialkarzinom (aufgehoben) |
| EMEA/H/C/005932 | Akeega | – | Kastrationsresistentes Prostatakarzinom (aufgehoben) |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (PARP-Inhibitor) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten (in der Literatur: Risiko für Myelosuppression und myelodysplastisches Syndrom bei Langzeitanwendung) |
| Emetogenitätsklassifikation | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Blutbild, Leber- und Nierenfunktion |
| Handhabungsschutz | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind u. a. **Deferipron** und **Samarium-(153Sm)-Lexidronam**. Zahlreiche **moderate** Wechselwirkungen betreffen u. a. Acetylsalicylsäure, Apixaban, Abciximab, Alteplase, Cilostazol, Dipyridamol, Bivalirudin sowie radioaktive Arzneimittel (Iobenguan I-131, Ibritumomab tiuxetan, Tositumomab, Strontium-89-chlorid). Insbesondere die Kombination mit Antikoagulanzien und Thrombozytenaggregationshemmern sowie mit knochenmarksuppressiven Substanzen erfordert Vorsicht.

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation beachten.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der TxGNN-Wert ist sehr hoch, die Evidenz stützt jedoch keine eindeutig neue Indikation: Die einzige relevante Studie (Phase 2, seröses Endometriumkarzinom) rekrutiert noch ohne Ergebnisse, und der Treffer „zystische Neoplasie“ ist teilweise ein Ontologie-Artefakt, das stark mit den bereits zugelassenen Ovarialindikationen überlappt. Zudem sind beide deutschen Zulassungen aufgehoben, und die Sicherheitsdaten aus der Fachinformation fehlen, sodass keine Sicherheitsprüfung möglich ist.

**Für das weitere Vorgehen sind erforderlich:**
- Fachinformation des BfArM (Warnhinweise, Gegenanzeigen) beschaffen und auswerten
- Daten zum Wirkmechanismus (z. B. über DrugBank) ergänzen
- Ergebnisse der Studie NCT04716686 abwarten und bewerten
- Klärung, welche konkrete Erkrankung hinter dem Begriff „zystische Neoplasie“ steht, und Abgrenzung von den bestehenden Ovarialindikationen
- Klärung des regulatorischen Status (Gründe für die Aufhebung der Zulassungen)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

