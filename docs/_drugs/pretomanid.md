---
layout: default
title: Pretomanid
parent: Nur Modellvorhersage (L5)
nav_order: 371
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pretomanid: vorhergesagte neue Indikation Candidiasis (Evidenzstufe L5). Ursprüngliche Indikation: Multiresistente Tuberkulose"
monitor_inn: "PRETOMANID"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery"]
---

# Pretomanid
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Pretomanid: Von multiresistenter Tuberkulose zu Candidiasis

## Zusammenfassung in einem Satz

Pretomanid ist ein Nitroimidazooxazin-Antibiotikum, das ursprünglich zur Behandlung der multiresistenten Tuberkulose eingesetzt wird.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Candidiasis** voraus (höchster Score), jedoch liegen dafür **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht ausschließlich auf einem Graphenmodell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Multiresistente Tuberkulose |
| Vorhergesagte neue Indikation | Candidiasis |
| TxGNN-Vorhersagewert | 99,69 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Für diesen Wirkstoff liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Mechanismusdaten (MOA) vor. Aus der Fachliteratur ist bekannt: Pretomanid ist ein Prodrug, das von der Deazaflavin-abhängigen Nitroreduktase (Ddn) von *Mycobacterium tuberculosis* aktiviert wird. Unter anaeroben Bedingungen setzt es Stickstoffmonoxid und reaktive Stickstoffspezies frei und hemmt in replizierenden Bakterien die Mykolsäuresynthese.

**Ehrliche Bewertung:** Für Candidiasis besteht kein etablierter mechanistischer Zusammenhang. Pilze wie *Candida* besitzen den Ddn/F420-abhängigen Aktivierungsweg nicht, daher ist eine antimykotische Wirkung nicht zu erwarten. Der hohe TxGNN-Wert (0,997) ist eine rein graphbasierte Vorhersage ohne gestützte Studien oder Literatur.

Weitere vorhergesagte Indikationen (zur Einordnung):
- **Lepra** (Score 99,27 %): mechanistisch plausibel, aber unbewiesen, da *M. leprae* nah mit *M. tuberculosis* verwandt ist. Unklar ist jedoch, ob *M. leprae* wegen starken Genomzerfalls ein funktionsfähiges Ddn/F420-System besitzt. Dies ist die biologisch am ehesten nachvollziehbare Vorhersage (Evidenzstufe L4, Einstufung „Forschungsfrage“).
- **Koronare Herzkrankheit, Myokardischämie, anomaler Abgang der linken Koronararterie aus der Pulmonalarterie** (Scores 99,25 %, 99,17 % bzw. 99,08 %): kein glaubwürdiger mechanistischer Zusammenhang; vermutlich Artefakte der Graphnähe.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für Candidiasis ist derzeit keine zugehörige Literatur verfügbar.

Zur Einordnung: Für die zweitplatzierte Vorhersage Lepra wurden 8 Publikationen abgerufen, die jedoch alle die medikamentenresistente Tuberkulose betreffen und Lepra nicht behandeln. Eine Auswahl:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [41263908](https://pubmed.ncbi.nlm.nih.gov/41263908/) | 2025 | Review | Archives of Microbiology | Umfassender Überblick zu Pretomanid bei medikamentenresistenter Lungentuberkulose (BPaL-Regime) |
| [41876996](https://pubmed.ncbi.nlm.nih.gov/41876996/) | 2026 | Kohorte | BMC Infectious Diseases | Wirksamkeit und Sicherheit von BPaLM bei resistenter TB in Äthiopien (retrospektive Multicenter-Studie) |
| [41080099](https://pubmed.ncbi.nlm.nih.gov/41080099/) | 2025 | Kohorte | Pan African Medical Journal | Behandlungsergebnisse unter BPaL/BPaLM in Südostnigeria |
| [41354901](https://pubmed.ncbi.nlm.nih.gov/41354901/) | 2025 | Kohorte | Communications Medicine | Genomsequenzierung zum Nachweis extensiv resistenter TB in Äthiopien |
| [37291443](https://pubmed.ncbi.nlm.nih.gov/37291443/) | 2023 | Präklinisch | AAPS PharmSciTech | Inhalative Zusatztherapie mit Pretomanid-Analoga bei MDR-TB |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005167 | Dovprela (zuvor Pretomanid FGK) | – | Multiresistente Tuberkulose (Status: erloschen) |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen** (14 Einträge gefunden, davon 7 als „Major“ eingestuft):

- **Schwerwiegend (Major):** Dexamethason, Lumacaftor, Apalutamid, Dabrafenib, Mitotan, Lorlatinib, Enzalutamid
- **Moderat:** Empagliflozin, Sitagliptin, Somatropin, Somatrem, Baricitinib, Clofarabin, Methotrexat

Für Warnhinweise und Gegenanzeigen siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für Candidiasis beruht allein auf dem Modell (Evidenzstufe L5). Es gibt weder Studien noch Literatur, und der bekannte Wirkmechanismus von Pretomanid spricht gegen eine Wirkung auf Pilze. Zudem ist die einzige deutsche Zulassung erloschen.

**Für eine Weiterverfolgung sind folgende Schritte nötig:**
- Prüfung, ob die Fachinformation (Warnhinweise, Gegenanzeigen) vorliegt; diese Sicherheitsdaten fehlen derzeit und blockieren die Sicherheitsprüfung
- Vollständige Mechanismusdaten (MOA) aus DrugBank
- Falls Interesse besteht, eher die Hypothese **Lepra** präklinisch prüfen (z. B. Analyse des F420-Wegs in *M. leprae*, Maus-Fußballen-Modell)
- Für Candidiasis: In-vitro-Empfindlichkeitstests an *Candida*-Stämmen, um die Hypothese überhaupt zu stützen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

