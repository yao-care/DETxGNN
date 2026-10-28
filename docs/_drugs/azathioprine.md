---
layout: default
title: Azathioprine
parent: Nur Modellvorhersage (L5)
nav_order: 50
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "AZATHIOPRINE"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
description: "Azathioprine: vorhergesagte neue Indikation Colobomatous microphthalmia-rhizomelic dysplasia syndrome (Evidenzstufe L5). Ursprüngliche Indikation: Graft Rejection"
---

# Azathioprine
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

## Azathioprine: Colobomatous microphthalmia-rhizomelic dysplasia syndrome
{: .text-alpha }

## Zusammenfassung

Azathioprin ist ein Purin-Antimetabolit mit immunsuppressiver Wirkung und wurde ursprünglich zur Behandlung der Transplantatabstoßung zugelassen. Das TxGNN-Modell sagt für die Substanz mehrere neue Indikationen voraus. Der höchste Score entfällt formal auf seltene Entwicklungsstörungen ohne jede Evidenz. Die einzige klinisch belastbare Richtung ist die **chronisch-entzündliche Darmerkrankung (CED, einschließlich Colitis ulcerosa)**. Dafür liegen **mindestens 24 registrierte klinische Studien** und zahlreiche Publikationen vor, darunter mehrere Cochrane-Übersichten. Es handelt sich dabei aber überwiegend um etablierten Einsatz und nicht um ein neues Repurposing-Signal.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Graft Rejection |
| Vorhergesagte neue Indikation (Rang 1 laut Modell) | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| Klinisch relevanteste Kandidaten | Chronisch-entzündliche Darmerkrankung (Score 99,52 %) und Colitis ulcerosa (Score 99,33 %) |
| TxGNN-Score (Rang 1) | 1.0000 |
| Evidenzstufe | L5 für Rang 1; L1 für CED und Colitis ulcerosa |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Rang 1: Hold; CED / Colitis ulcerosa: Proceed with Guardrails |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben aus der Arzneistoffdatenbank vor. Aus der Literatur ist jedoch bekannt: Azathioprin wird zu 6-Thioguaninnukleotiden verstoffwechselt, die die Purinsynthese hemmen und die Apoptose von T-Zellen fördern (u. a. über die Hemmung von Rac1). Dadurch wird die Aktivierung des Immunsystems unterdrückt, die auch bei Transplantatabstoßung zentral ist.

Bei der CED und der Colitis ulcerosa spielt eine überschießende, T-Zell-getriebene Immunaktivierung der Darmschleimhaut eine zentrale Rolle. Der Wirkmechanismus passt daher gut. Die Substanz wird in der Praxis seit Jahrzehnten als steroidsparender Immunmodulator zur Remissionserhaltung eingesetzt.

Bei den meisten übrigen vorhergesagten Erkrankungen (z. B. seltene Skelett- und Fehlbildungssyndrome, Osteoarthrose-Suszeptibilität) besteht dagegen kein erkennbarer mechanistischer Zusammenhang. Das WHIM-Syndrom ist sogar ungünstig, da die myelosuppressive und lymphozytensuppressive Wirkung die Zytopenien wahrscheinlich verschlechtern würde. Die hohen Scores dieser Kandidaten sind reine Graphvorhersagen.

---

## Evidenz aus klinischen Studien

Dargestellt sind die relevantesten Studien für die CED, die Colitis ulcerosa wird dabei mitabgedeckt (Auswahl von 10).

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Rekrutierend | 300 | Mirikizumab (Top-down) vs. Azathioprin-Standardtherapie bei neu diagnostizierter mittelschwerer bis schwerer Colitis ulcerosa |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Abgebrochen | 242 | Infliximab als Monotherapie oder mit Azathioprin vs. Azathioprin-Monotherapie bei Colitis ulcerosa |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Abgeschlossen | 211 | Infliximab plus Antimetabolit vs. Monotherapien bei Morbus Crohn in steroidfreier Remission |
| [NCT01235689](https://clinicaltrials.gov/study/NCT01235689) | Phase 3 | Abgeschlossen | 252 | Zwei Behandlungsalgorithmen bei mittelschwerem bis schwerem Morbus Crohn; Azathioprin indirekt beteiligt |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Abgeschlossen | 83 | Azathioprin vs. Mesalazin zur Prävention des postoperativen Rezidivs bei Morbus Crohn |
| [NCT01564823](https://clinicaltrials.gov/study/NCT01564823) | Phase 3 | Abgeschlossen | 86 | Adalimumab vs. Azathioprin zur Prävention des postoperativen Rezidivs bei Morbus Crohn |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Abgeschlossen | 65 | Früh Azathioprin plus Infliximab vs. Kortikosteroide plus Azathioprin bei akuter schwerer Colitis |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | Abgebrochen | 28 | Konventionelles Step-up (mit Azathioprin) vs. Infliximab-Monotherapie; wegen geringer Fallzahl wenig aussagekräftig |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Abgebrochen | 31 | Dosisfindung von Azathioprin (IMURAN) bei aktivem Morbus Crohn |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unbekannt | 84 | Niedrig dosiertes Azathioprin plus Allopurinol vs. Azathioprin-Monotherapie bei Colitis ulcerosa |

Für die übrigen vorhergesagten Erkrankungen (insbesondere die Rangplätze 1–4, 6, 8 und 10) sind derzeit keine relevanten klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Systematische Übersicht | Cochrane Database Syst Rev | Aktualisierte Bewertung von Azathioprin/6-MP zur Remissionserhaltung bei Colitis ulcerosa |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE-Studie: Top-down Infliximab plus Azathioprin vs. Azathioprin allein bei akuter schwerer Colitis ulcerosa |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Systematische Übersicht | Cochrane Database Syst Rev | Wirksamkeit von Azathioprin/6-MP zur Remissionserhaltung bei Colitis ulcerosa |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Systematische Übersicht | Cochrane Database Syst Rev | Frühere Fassung der Cochrane-Analyse zur Remissionserhaltung |
| [17253451](https://pubmed.ncbi.nlm.nih.gov/17253451/) | 2007 | Systematische Übersicht | Cochrane Database Syst Rev | Erste Fassung der Cochrane-Analyse zur Remissionserhaltung |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohns Colitis | Aktueller Überblick zu Thiopurinen bei CED |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | Pharmakogenetik und Metabolitenmonitoring von Azathioprin und 6-MP bei CED |
| [34287682](https://pubmed.ncbi.nlm.nih.gov/34287682/) | 2021 | Review | J Gastroenterol | Thiopurin-Pharmakogenomik (NUDT15) und Schwangerschaft bei CED |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Mechanistische Studie | Cell Rep Med | Kommensale Bakterien fördern Therapieversagen von Azathioprin durch geringere 6-MP-Bioverfügbarkeit |
| [32799195](https://pubmed.ncbi.nlm.nih.gov/32799195/) | 2020 | Review | Digestion | Malignome bei CED |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005055 | Jayempi (Lipomed GmbH) | – | Transplantatabstoßung (Zulassung gültig) |

---

## Zytotoxizität

Azathioprin ist kein klassisches Antineoplastikum, wirkt aber als Purin-Antimetabolit zytotoxisch auf proliferierende Lymphozyten. Zu Zytotoxizitätsklassifikation, Emetogenität und Handhabungsvorschriften liegen in den zusammengestellten Daten keine Angaben vor. Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten.

---

## Sicherheitsaspekte

- **Kontraindikationen bzw. Risikoerkrankungen aus dem Wissensgraphen (kein Fachinformationstext):** Pankreatitis, Thrombozytopenie, Anämie (auch makrozytär), Niereninsuffizienz, Pilz- und andere Infektionskrankheiten (u. a. Dermatophytose), Lymphome (einschließlich primärem ZNS-Lymphom, Lymphosarkom und hepatosplenischem T-Zell-Lymphom), Lebervenenthrombose und Budd-Chiari-Syndrom.
- **Wechselwirkungen (100 gemeldete):**
  - Moderat: Mesalazin, Balsalazid, Olsalazin, Sulfasalazin.
  - Gering: Zinkacetat, Zinkgluconat, Zinksulfat.
  - Weitere Wechselwirkungen mit unbekanntem Schweregrad, u. a. Amphotericin B, Acetylsalicylsäure, Pantoprazol, Omeprazol, Metformin, Doxycyclin und Morphin.
- **Leitplanken aus der Literatur:** TPMT-/NUDT15-Genotypisierung vor Therapiebeginn, Kontrolle von Blutbild und Leberenzymen sowie Überwachung auf Infektionen und Malignome (Lymphome, Hautkrebs).

Ergänzend bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails (für CED / Colitis ulcerosa); Hold (für alle übrigen vorhergesagten Indikationen, einschließlich Rang 1)**

**Begründung:**
- Für CED und Colitis ulcerosa sprechen mehrere Phase-3- und Phase-4-Studien, Cochrane-Übersichten und ein publizierter RCT (ACTIVE) für die Wirksamkeit. Die Studien nutzen Azathioprin jedoch häufig als Vergleichs- oder Kombinationspartner, sodass dies etablierten Einsatz widerspiegelt und kein neues Repurposing-Signal darstellt.
- Die höchstbewerteten Vorhersagen (Rang 1 und 2) sind seltene Entwicklungsstörungen ohne plausiblen Mechanismus und ohne Studien- oder Literaturbasis. Der Score ist dort rein graphbasiert.

**Für das weitere Vorgehen erforderlich:**
- Fachinformation (Warnhinweise, Kontraindikationen) aus der BfArM-Quelle beschaffen, da diese Daten fehlen und die Sicherheitsprüfung sonst nicht abgeschlossen werden kann.
- Detaillierte Wirkmechanismusdaten aus der Arzneistoffdatenbank ergänzen.
- Klären, dass in Deutschland nur eine erloschene Zulassung vorliegt, und den regulatorischen Status der Indikation CED prüfen.
- Sicherheitsüberwachungsplan (TPMT/NUDT15-Testung, Blutbild, Leberwerte, Malignomrisiko) für die Zielpopulation festlegen.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

