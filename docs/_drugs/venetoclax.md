---
layout: default
title: Venetoclax
parent: Nur Modellvorhersage (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

# Venetoclax: Von chronischer lymphatischer Leukämie zu myeloischer Leukämie

## Zusammenfassung

Venetoclax ist ein BCL-2-Inhibitor, der ursprünglich zur Behandlung der chronischen lymphatischen B-Zell-Leukämie (CLL) zugelassen wurde.
Das TxGNN-Modell sagt für die Substanz mehrere neue Einsatzgebiete voraus. Am besten belegt ist **myeloische Leukämie** (insbesondere akute myeloische Leukämie, AML) mit **über 30 klinischen Studien** und **18 Publikationen**, darunter eine laufende Phase-3-Studie.
Der Bericht konzentriert sich auf diese Indikation. Weitere Vorhersagen (CML, follikuläres Lymphom u. a.) werden am Ende kurz eingeordnet.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Chronische lymphatische B-Zell-Leukämie |
| Vorhergesagte neue Indikation | Myeloische Leukämie (Rang 4 der Vorhersageliste) |
| TxGNN-Vorhersagescore | 99,47 % |
| Evidenzniveau | L1 (laut Datenbewertung; die Phase-3-Studien laufen jedoch noch, siehe Hinweis unten) |
| Marktstatus in Deutschland | Nur gelöschte (erloschene) Zulassung |
| Anzahl der Zulassungen | 1 (gelöscht) |
| Empfohlene Entscheidung | Proceed with Guardrails |

Hinweis: Rang 1 und 2 der Vorhersageliste (CLL/SLL-Subtypen) sind keine echte Neuverwendung, da sie Untergruppen der bereits zugelassenen Indikation darstellen. Rang 4 (myeloische Leukämie) ist die erste Vorhersage mit substanziellem neuem Evidenzgewicht. Streng nach den Regeln (≥2 abgeschlossene Phase-3-RCTs) wäre L1 nicht erfüllt, da die gelisteten Phase-3-Studien teils noch rekrutieren. Die Stufe L1 stammt aus der Bewertung der Datengrundlage und sollte entsprechend vorsichtig gelesen werden.

---

## Warum ist diese Vorhersage plausibel?

Venetoclax hemmt selektiv das antiapoptotische Protein BCL-2. Detaillierte Mechanismusdaten aus DrugBank liegen für diesen Bericht nicht vor. Aus bekanntem Wissen und der Literatur gilt jedoch: Sowohl CLL-Zellen als auch AML-Blasten und leukämische Stammzellen sind von BCL-2 für ihr Überleben abhängig.

CLL und AML sind beides hämatologische Neoplasien, bei denen eine gestörte Apoptose zentral ist. Die Kombination von Venetoclax mit hypomethylierenden Substanzen (Azacitidin, Decitabin) hat sich bei AML-Patienten etabliert, die für eine intensive Chemotherapie nicht geeignet sind. Das stützt die Vorhersage des Modells.

Wichtige Einschränkungen: Resistenzmechanismen (z. B. über MCL-1 oder mitochondriale Veränderungen) sind beschrieben, und die Evidenz in den vorliegenden Daten bezieht sich überwiegend auf Kombinationsregime, nicht auf die Monotherapie.

---

## Evidenz aus klinischen Studien

Ausgewählt wurden die 10 relevantesten Studien (nach Relevanzbewertung und Studienphase):

| Studiennummer | Phase | Status | Teilnehmer | Kernaussage |
|---------|------|------|------|---------|
| [NCT06852222](https://clinicaltrials.gov/study/NCT06852222) | Phase 3 | Rekrutierend | 600 | Bleximenib + Venetoclax + Azacitidin vs. Placebo + Ven/Aza bei neu diagnostizierter AML mit NPM1-/KMT2A-Veränderung |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | Rekrutierend | 324 | Venetoclax plus fraktioniertes Busulfan bei Hochrisiko-AML/MDS vor Stammzelltransplantation |
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1/2 | Rekrutierend | 96 | Ivosidenib + Venetoclax ± Azacitidin bei IDH1-mutierten myeloischen Erkrankungen |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Aktiv, nicht rekrutierend | 116 | Venetoclax mit Busulfan/Cladribin/Fludarabin-Konditionierung vor allogener Transplantation |
| [NCT06696183](https://clinicaltrials.gov/study/NCT06696183) | Phase 2 | Rekrutierend | 60 | Gilteritinib + Venetoclax + Azacitidin bei FLT3-mutierter AML |
| [NCT07228273](https://clinicaltrials.gov/study/NCT07228273) | Phase 2 | Rekrutierend | 102 | Venetoclax + FLAG-IDA vs. Standardinduktion bei neu diagnostizierter AML |
| [NCT06429098](https://clinicaltrials.gov/study/NCT06429098) | Phase 2 | Aktiv, nicht rekrutierend | 40 | Anthrazyklin-freies Venetoclax-Regime bei CBFB::MYH11-positiver AML |
| [NCT03844815](https://clinicaltrials.gov/study/NCT03844815) | Phase 1 | Aktiv, nicht rekrutierend | 26 | Venetoclax + 10-Tage-Decitabin bei AML |
| [NCT05177731](https://clinicaltrials.gov/study/NCT05177731) | Phase 3 | Aktiv, nicht rekrutierend | 188 | Venetoclax + Decitabin vs. „7+3“-Induktion bei jungen Erwachsenen mit AML |
| [NCT07132684](https://clinicaltrials.gov/study/NCT07132684) | Phase 3 | Rekrutierend | 240 | Venetoclax + Azacitidin vs. Daunorubicin/Idarubicin + Cytarabin bei älteren, intensivtherapiefähigen AML-Patienten |

Hinweis: Keine der aufgeführten Phase-3-Studien ist als abgeschlossen mit Ergebnissen gekennzeichnet.

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Kernaussage |
|------|-----|------|------|---------|
| [29339097](https://pubmed.ncbi.nlm.nih.gov/29339097/) | 2018 | Phase-1b-Studie | Lancet Oncol | Sicherheit und vorläufige Wirksamkeit von Venetoclax mit Decitabin oder Azacitidin bei älteren, unbehandelten AML-Patienten |
| [39303729](https://pubmed.ncbi.nlm.nih.gov/39303729/) | 2024 | Phase-2-Studie | Lancet Haematol | Decitabin + Venetoclax + Ponatinib bei fortgeschrittener Ph+-myeloischer Erkrankung |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | Kohorte | Clin Cancer Res | Venetoclax + Azacitidin bei therapienaiver AML mit IDH1/2-Mutation |
| [40913104](https://pubmed.ncbi.nlm.nih.gov/40913104/) | 2025 | Post-hoc-Analyse (VIALE-A) | Leukemia | Ven + Aza vs. Aza allein, stratifiziert nach Alter und AML-Risikomodell |
| [31932844](https://pubmed.ncbi.nlm.nih.gov/31932844/) | 2020 | Molekulare Analyse | Blood | Molekulare Muster für Ansprechen und Therapieversagen unter Venetoclax-Kombinationen bei älteren AML-Patienten |
| [39486083](https://pubmed.ncbi.nlm.nih.gov/39486083/) | 2024 | Kohorte | Blood | ELN-2024-Risikostratifizierung verbessert die Prognose unter Venetoclax-basierter Therapie |
| [28161120](https://pubmed.ncbi.nlm.nih.gov/28161120/) | 2017 | PK/DDI-Studie | Clin Ther | Dosisanpassung von Venetoclax bei Wechselwirkung mit Posaconazol (starker CYP3A-Inhibitor) |
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Review | Biomed Pharmacother | Übersicht zu Venetoclax bei erwachsener AML |
| [38866760](https://pubmed.ncbi.nlm.nih.gov/38866760/) | 2024 | Review | Cell Death Dis | Resistenzmechanismen unter Venetoclax bei AML |
| [40266036](https://pubmed.ncbi.nlm.nih.gov/40266036/) | 2025 | Studie | Pediatr Blood Cancer | Venetoclax allein oder mit Chemotherapie bei pädiatrischer und junger erwachsener R/R-AML |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004106 | Venclyxto (AbbVie Deutschland GmbH & Co. KG) | nicht angegeben | Chronische lymphatische B-Zell-Leukämie |

Der Status dieser Zulassung ist „gelöscht“. Es liegt damit keine gültige Zulassung im Datensatz vor.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Klassifikation | Zielgerichtete Therapie (BCL-2-Inhibitor); in Kombination häufig mit zytotoxischen Substanzen |
| Myelosuppressionsrisiko | Hoch (Neutropenie und Zytopenien sind in der Literatur als häufig beschrieben; Tumorlysesyndrom-Risiko) |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Differenzialblutbild, Leber- und Nierenfunktion, Elektrolyte, Tumorlyse-Parameter (Harnsäure, Kalium, Phosphat, Calcium, LDH) |
| Schutzmaßnahmen beim Umgang | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Für Venetoclax wurden 100 Wechselwirkungen erfasst. Zu den als **schwerwiegend (Major)** eingestuften Partnern zählen unter anderem:
- Aprepitant
- Dexamethason
- Clarithromycin
- Eliglustat
- Rolapitant
- Fidaxomicin
- Cobicistat
- Deferipron
- Samarium (153Sm) Lexidronam

Mäßige (Moderate) Wechselwirkungen bestehen u. a. mit Alvimopan, Loperamid, Cimetidin, Miconazol und Rifaximin. Die Literatur zeigt zudem, dass starke CYP3A-Inhibitoren wie Posaconazol die Venetoclax-Exposition erhöhen und eine Dosisanpassung erfordern.

Für Warnhinweise und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Für Venetoclax-basierte Regime bei AML liegen zahlreiche Phase-2-Studien und mehrere laufende Phase-3-Studien vor, dazu eine solide Literaturbasis und ein plausibler Mechanismus (BCL-2-Abhängigkeit). Die Evidenz bezieht sich jedoch überwiegend auf Kombinationstherapien, die Phase-3-Studien sind noch nicht abgeschlossen, und in Deutschland besteht laut Datenlage keine gültige Zulassung.

**Für das weitere Vorgehen wird benötigt:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da diese Daten fehlen und als blockierende Lücke gelten
- Mechanismusdaten aus DrugBank
- Klärung des aktuellen Zulassungsstatus in Deutschland
- Ergebnisse der laufenden Phase-3-Studien (z. B. NCT06852222, NCT05177731)
- Überwachungskonzept für Zytopenien und Tumorlysesyndrom sowie Management von CYP3A-Interaktionen

---

## Einordnung der übrigen Vorhersagen

| Rang | Indikation | Evidenzniveau | Empfehlung | Kurzbewertung |
|---|---|---|---|---|
| 1–2 | CLL/SLL-Subtypen (unmutiert/mutiert IGHV) | L4 | Hold | Untergruppen der bereits zugelassenen Indikation, keine echte Neuverwendung; keine spezifischen Studien |
| 3 | Hodgkin-Lymphom | L3 | Research Question | Studien betreffen überwiegend andere B-Zell-Lymphome, keine Hodgkin-spezifische Evidenz |
| 5 | CML, BCR-ABL1-positiv | L2 | Research Question | Phase-2-Daten (Dasatinib + Venetoclax; Decitabin + Venetoclax + Ponatinib), klein und einarmig |
| 6 | Ewing-Sarkom | L5 | Hold | Nur präklinisch, teils widersprüchlich |
| 7 | Follikuläres Lymphom | L2 | Research Question | Mehrere Phase-2-Kombinationsstudien, begrenzte Einzelwirkung |
| 8 | Metastasierte Neoplasie | L3 | Research Question | Unspezifische Kategorie; Phase-1b-Daten bei ER+-Brustkrebs |
| 9 | Malignes Spiradenom | L5 | Hold | Keine Studien oder Literatur |
| 10 | AML mit t(8;21) | L4 | Hold | Indirekte Evidenz aus allgemeiner AML |
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

