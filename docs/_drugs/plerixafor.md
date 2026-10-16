---
layout: default
title: Plerixafor
parent: Nur Modellvorhersage (L5)
nav_order: 362
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Plerixafor: vorhergesagte neue Indikation Indolentes Plasmazellmyelom (Evidenzstufe L5). Ursprüngliche Indikation: Multiples Myelom"
monitor_inn: "PLERIXAFOR"
predicted_indications: ["indolent plasma cell myeloma", "CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
---

# Plerixafor
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Plerixafor: Vom Multiplen Myelom zum indolenten Plasmazellmyelom

## Zusammenfassung

Plerixafor ist ein CXCR4-Antagonist, der in der Zulassung zur Mobilisierung hämatopoetischer Stammzellen bei Multiplem Myelom und Lymphom vor einer autologen Transplantation eingesetzt wird. Das TxGNN-Modell sagt eine mögliche Wirksamkeit beim **indolenten Plasmazellmyelom** voraus. Dafür liegen aktuell **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht allein auf der Modellberechnung. Für die ebenfalls vorhergesagte **myeloische Leukämie** gibt es dagegen **27 registrierte Studien** und **20 Publikationen** (siehe Zusatzabschnitt unten).

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Multiples Myelom; hämatopoetische Stammzelltransplantation; Lymphom |
| Vorhergesagte neue Indikation | Indolentes Plasmazellmyelom |
| TxGNN-Vorhersagewert | 99,97 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassungen |
| Anzahl der Zulassungen | 2 (beide erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Plerixafor blockiert den Chemokinrezeptor CXCR4. Laut den für diesen Bericht zusammengestellten Daten bindet es außerdem an ACKR3. Die Achse CXCL12/CXCR4 hält Zellen in der Knochenmarknische fest. Durch die Blockade lösen sich Stammzellen und Tumorzellen aus dieser Nische. Detaillierte Mechanismusdaten aus DrugBank liegen derzeit nicht vor. Die Beschreibung stützt sich daher auf die Zielstruktur-Daten und die mechanistische Einordnung.

Das Multiple Myelom, für das Plerixafor bereits zur Stammzellmobilisierung eingesetzt wird, und das indolente (schwelende) Plasmazellmyelom gehören zur selben Erkrankungsfamilie. Myelomzellen sind auf die Knochenmarknische angewiesen. Eine Störung des Zielens auf diese Nische ist deshalb biologisch denkbar.

Der hohe Vorhersagewert beruht jedoch im Wesentlichen auf der Nähe zur zugelassenen Myelom-Indikation. Für das indolente Stadium gibt es weder Studien noch Literatur.

---

## Klinische Studien

Derzeit sind keine klinischen Studien zu dieser Indikation registriert.

---

## Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen Deutschland

Beide Zulassungen sind erloschen. Es besteht keine gültige Zulassung. Die Zulassungsnummern sind EU-zentrale Zulassungen.

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/001030 | Mozobil (Sanofi B.V.) | – | Multiples Myelom; hämatopoetische Stammzelltransplantation; Lymphom |
| EMEA/H/C/005943 | Plerixafor Accord (Accord Healthcare S.L.U.) | – | Multiples Myelom; hämatopoetische Stammzelltransplantation |

---

## Zusatz: Besser belegte vorhergesagte Indikation – Myeloische Leukämie

Für die an Rang 7 vorhergesagte **myeloische Leukämie** (TxGNN-Wert 99,02 %) liegt die einzige substanzielle Evidenz im gesamten Datensatz vor. Das Evidenzlevel ist **L2**, die Einstufung lautet „Forschungsfrage“.

**Mechanismus:** Leukämiezellen und Leukämiestammzellen werden über CXCL12/CXCR4 in der Knochenmarknische gehalten und sind dadurch chemoresistent. Plerixafor mobilisiert sie in die Zirkulation und kann sie für Chemotherapie sensibilisieren.

**Einschränkungen:** Es gibt keine Phase-3-RCT. Sicherheits- und Ansprechsignale stammen überwiegend aus kleinen einarmigen Studien. Die Wirksamkeit ist nicht belegt. Die Studienliste im Datensatz ist gekürzt (10 von 27 Studien dargestellt).

### Klinische Studien (Auswahl)

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Abgeschlossen | 52 | AMD3100 plus Mitoxantron, Etoposid und Cytarabin bei rezidivierter/refraktärer AML |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Abgeschlossen | 39 | Chemosensibilisierung mit Plerixafor plus G-CSF bei rezidivierter/refraktärer AML |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Abgeschlossen | 36 | Dosiseskalation mit Cytarabin und Daunorubicin („7+3“) bei neu diagnostizierter AML |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Abgeschlossen | 20 | Plerixafor als Chemosensibilisator bei rezidivierter akuter Leukämie/MDS im Kindesalter |
| [NCT02605460](https://clinicaltrials.gov/study/NCT02605460) | Phase 2 | Unbekannt | 20 | CXCR4-Antagonist zur Chemosensibilisierung vor Stammzelltransplantation bei akuter Leukämie in Remission |
| [NCT01160354](https://clinicaltrials.gov/study/NCT01160354) | Phase 1/2 | Abgebrochen | 22 | Plerixafor plus Clofarabin bei älteren, unbehandelten AML-Patienten; vorzeitig beendet |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Abgeschlossen | 47 | G-CSF und Plerixafor mit Busulfan/Fludarabin vor allogener Transplantation bei myeloischen Leukämien |
| [NCT01141543](https://clinicaltrials.gov/study/NCT01141543) | k. A. | Abgeschlossen | 12 | Mobilisierung von Leukämiezellen im myeloablativen Konditionierungsregime bei AML |
| [NCT01455025](https://clinicaltrials.gov/study/NCT01455025) | Phase 1 | Abgebrochen | 11 | Dosiseskalation mit Induktions- und Konsolidierungschemotherapie bei rezidivierter AML |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Abgeschlossen | 71 | Decitabin plus Plerixafor-Priming bei AML ab 60 Jahren |

### Literatur (Auswahl)

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematische Übersicht/Metaanalyse | Leukemia Research | Plerixafor mit Chemotherapie und/oder Transplantation bei akuter Leukämie; Auswertung präklinischer und klinischer Studien |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | CXCR4 als therapeutisches Ziel bei AML |
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase-1/2-Studie | Blood | Chemosensibilisierung mit Plerixafor bei rezidivierter/refraktärer AML (52 Patienten) |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase-1/2-Studie | Annals of Hematology | PLERIFLAG-Regimen bei früh rezidivierter/refraktärer AML |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase-1-Studie | Haematologica | Plerixafor plus Decitabin bei älteren, neu diagnostizierten AML-Patienten (69 behandelt) |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase-1-Studie | American Journal of Hematology | Sorafenib, G-CSF und Plerixafor bei rezidivierter/refraktärer FLT3-ITD-mutierter AML (28 Patienten) |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Phase-1-Studie | Biology of Blood and Marrow Transplantation | Sicherheit und Verträglichkeit von Plerixafor im myeloablativen Konditionierungsregime bei AML |
| [32079173](https://pubmed.ncbi.nlm.nih.gov/32079173/) | 2020 | Review | Biology | CXCR4-Antagonisten als Mobilisatoren und Therapiesensibilisatoren bei AML und Glioblastom |

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph (PrimeKG, kein Packungsbeilagentext):** Thrombozytopenie, Nierenfunktionsstörung, Leukämie. Diese Angaben sind als Hinweis zu verstehen und müssen anhand der Fachinformation überprüft werden.
- **Wechselwirkungen (pharmakologische Zielstrukturen):** CXCR4 und ACKR3. Es handelt sich um Zielstrukturen, nicht um Arzneimittel-Wechselwirkungen mit Schweregrad.

Für Warnhinweise und Gegenanzeigen bitte die Packungsbeilage bzw. Fachinformation heranziehen. Die Daten daraus konnten für diesen Bericht nicht ausgewertet werden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für das indolente Plasmazellmyelom gibt es weder Studien noch Literatur. Der hohe Vorhersagewert beruht allein auf der Nähe zur zugelassenen Myelom-Indikation (Evidenzlevel L5). Zudem sind beide deutschen Zulassungen erloschen.

**Für das weitere Vorgehen wird Folgendes benötigt:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen) als Voraussetzung für die Sicherheitsprüfung
- Präklinische oder frühe klinische Daten zu Plerixafor beim schwelenden Myelom
- Mechanismusdaten aus DrugBank
- Klärung des Zulassungs- und Verfügbarkeitsstatus in Deutschland
- Alternativ: Fokus auf die myeloische Leukämie, wo mehrere Phase-1/2-Studien vorliegen. Dort wäre zunächst eine kontrollierte Phase-2/3-Studie nötig, um die Wirksamkeit zu prüfen.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

