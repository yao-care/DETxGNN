---
layout: default
title: Pazopanib
parent: Nur Modellvorhersage (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: Vom Nierenzellkarzinom / Weichteilsarkom zum ungeklassifizierten Nierenzellkarzinom

## Zusammenfassung in einem Satz

> Pazopanib ist ein Multi-Target-Tyrosinkinase-Inhibitor, dessen etablierte Anwendung – wie in der abgerufenen Literatur dokumentiert – das fortgeschrittene/metastasierende klarzelliges Nierenzellkarzinom (ccRCC) und nicht-lipomatöses Weichteilsarkom ist.
> Das TxGNN-Modell sagt voraus, dass es auch bei **ungeklassifiziertem Nierenzellkarzinom** wirksam sein könnte,
> mit **1 abgeschlossener Phase-3-Studie** und **6 Publikationen**, die diese Richtung derzeit unterstützen.
> Hinweis: Das Arzneimittel ist in Deutschland derzeit nicht auf dem Markt, und TFDA-Warnungs-/Kontraindikationsdaten sind eine **Blockierungslücke** für die vorläufige Sicherheitsbewertung.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Nicht im Evidence Pack aufgeführt (`taiwan_regulatory.licenses` und `drug.original_indications` sind beide leer). Basierend auf der abgerufenen Literatur in diesem Pack ist Pazopanib eine registrierte/Standardtherapie für fortgeschrittenes/metastasierendes klarzelliges RCC und nicht-lipomatöses Weichteilsarkom. |
| Vorhergesagte neue Indikation | Ungeklassifiziertes Nierenzellkarzinom |
| TxGNN-Vorhersage-Score | 99.63% |
| Evidenzstufe | L2 (1 abgeschlossene Phase-3-Studie + mehrere retrospektive/real-world Kohorten) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Warteposition |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Mechanismus-Daten nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der abgerufenen Literatur selbst ist Pazopanib ein Multi-Target-Tyrosinkinase-Inhibitor mit anti-angiogenischer Aktivität; mehrere Abstracts im Evidence Pack beschreiben es als „Standard-Erstlinienbehandlung für metastasierendes klarzelliges Nierenzellkarzinom (ccRCC)" (PMID 28108284) und vermerken, dass es für fortgeschrittenes RCC „registriert" ist (NCT01613846 Zusammenfassung).

Ungeklassifiziertes RCC ist ein seltener, nicht-klarzelliger histologischer Subtyp innerhalb der gleichen Organ-/Tumorfamilie wie die etablierte Indikation von Pazopanib. Da Behandlungsansätze für nicht-klarzelliges RCC (nccRCC) „häufig aus Daten von klarzelliger Nierenzellkarzinoma extrapoliert werden" (PMID 31921344), und Pazopanibs anti-angiogenischer Mechanismus nicht histologie-spezifisch ist, ist das mechanistische Konzept für die Ausweitung auf ungeklassifiziertes/nicht-klarzelliges RCC plausibel und wird in mehreren retrospektiven Kohorten widergespiegelt (PANORAMA-Studie, PMID 28108284; MD Anderson Kohorte, PMID 27568124; IMDC-Konsortiumsanalyse, PMID 41558869).

Allerdings ist „ungeklassifiziertes RCC" eine distinkte und seltenere diagnostische Kategorie als die nccRCC-Populationen, die in diesen Papieren tatsächlich untersucht wurden, und keine Studie oder Publikation in diesem Pack isoliert speziell den Subtyp „ungeklassifiziert". Dies führt zu residualer Unsicherheit über die direkte Anwendbarkeit.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Abgeschlossen | 544 | Randomisierte sequenzielle Studie zur Bewertung von Sorafenib→Pazopanib vs. Pazopanib→Sorafenib bei fortgeschrittenem/metastasiertem RCC; beide Wirkstoffe waren registriert/wirksam bei RCC, aber es existierten keine vorherigen Vergleichsdaten zur Sequenzierung. |

---

## Literatur-Evidenz

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase II, einartig | Cancer Research and Treatment | Prospektive Phase-II-Studie zur Bewertung der Wirksamkeit/Sicherheit von Pazopanib speziell bei nicht-klarzelliger RCC (nccRCC). |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world/Retrospektiv | Ecancermedicalscience | Vergleicht Sunitinib vs. Pazopanib in der Erstlinie bei nicht-klarzelliger und sarkomatoider Histologie mRCC; fragt, ob die beiden austauschbar sind. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospektiv multizentrisch | Clinical Genitourinary Cancer | Italienische PANORAMA-Studie: retrospektive Analyse der Wirksamkeit/Toxizität von Pazopanib in der Erstlinie bei nccRCC. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospektive Kohorte | Clinical Genitourinary Cancer | Ergebnisse bei Patienten mit metastasiertem nicht-klarzelliger RCC behandelt mit Pazopanib. |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Retrospektiv/Fallserie | Clinical Genitourinary Cancer | Histologische/immunhistochemische Charakterisierung und Ergebnisse mit Zieltherapien bei Karzinom unbekannter Primär präsentiert mit mRCC-Merkmalen (CUP-mRCC). |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospektive Datenbank-Kohorte | European Urology Oncology | IMDC-Konsortiumsanalyse zum Vergleich zeitgenössischer vs. traditioneller Erstlinientherapien über nccRCC-Histologie-Subtypen, einschließlich ungeklassifiziertem RCC. |

---

## Marktinformation für Deutschland

Pazopanib hält derzeit keine Zulassung auf dem deutschen Markt (Marktstatus: Nicht vermarktet; 0 Genehmigungen vorgesehen).

---

## Zytotoxizität

Die etablierten Indikationen von Pazopanib (Nierenzellkarzinom, Weichteilsarkom) sind antineoplastisch, und es ist ein Multi-Target-Tyrosinkinase-Inhibitor – was ihn unter diese Rubrik einordnet.

| Punkt | Inhalt |
|-------|--------|
| Zytotoxizität-Klassifizierung | Zielgerichtete Therapie (Multi-Target-Tyrosinkinase-Inhibitor; anti-angiogen, VEGFR/PDGFR/c-KIT-gerichtet) – kein konventionales Zytotoxikum |
| Risiko der Myelosuppression | Nicht speziell in diesem Evidence Pack dokumentiert; TKIs dieser Klasse sind mit geringerem Myelosuppressions-Risiko verbunden als konventionale Zytostatika – bitte siehe Fachinformation |
| Emetogenitäts-Klassifizierung | Bitte siehe Fachinformation Warnhinweise und Vorsichtsmaßnahmen |
| Überwachungspunkte | Bitte siehe Fachinformation Warnhinweise und Vorsichtsmaßnahmen |
| Handhabungsschutz | Bitte siehe Fachinformation Warnhinweise und Vorsichtsmaßnahmen |

---

## Sicherheitsaspekte

Bitte siehe die Fachinformation für Sicherheitsinformationen. (`key_warnings`, `contraindications` und DDI-Abfrage haben alle keine Daten geliefert – DDI-Abfrage-Status: `not_found`.)

**Hinweis:** Dies ist im Evidence Pack als **Blockierungslücke** gekennzeichnet (DG001 – TFDA-Warnungs-/Kontraindikations-Kennzeichnung noch nicht abgerufen), was bedeutet, dass dieser Kandidat noch nicht die S1-Sicherheits-Vor-Bewertung bestehen kann.

---

## Weitere vorhergesagte Indikationen (Zusammenfassung)

Zur Information: Das gleiche Evidence Pack bewertete 9 zusätzliche Kandidaten-Indikationen für Pazopanib. Die meisten haben schwache oder keine direkte Evidenz und sind in Warteposition; zwei verwandte Sarkom-Indikationen zeigen merklich stärkere, krankheitsspezifische Unterstützung:

| Rang | Erkrankung | TxGNN-Score | Evidenzstufe | Empfehlung |
|------|------------|-------------|-----------------|------------|
| 2 | Nierenzellkarzinom (Xp11.2/TFE3 Fusion) | 99.63% | L5 | Warteposition – keine Studien-/Literatur-Unterstützung |
| 3 | Nierenzellkarzinom mit Neuroblastom | 99.63% | L5 | Warteposition – keine Studien-/Literatur-Unterstützung |
| 4 | Liposarkom | 99.59% | L2 | **Mit Vorsichtsmaßnahmen fortfahren** – 2 krankheitsspezifische Phase-II-Studien (NCT01506596, NCT01692496) + randomisierte Phase-II-Kombinationsstudie (NCT01532687); PDGFRA-Amplifikation mechanistische Rationale |
| 5 | Nierenzellenkarziom im Kindesalter | 99.54% | L4 | Warteposition – die einzige aufgeführte Studie ist eine Erwachsenen-mRCC-Studie, wahrscheinlich Ontologie-Fehler; keine pädiatrischen PK/Sicherheitsdaten |
| 6 | Myxoides Ovarialliposarkom | 99.51% | L5 | Warteposition – keine Studien-/Literatur-Unterstützung |
| 7 | Herzfibrosarkom | 99.37% | L4 | Warteposition – nur breite STS-Studien, keine kardial-spezifischen Daten; Kardiotoxizitäts-Risiko bedarf Bewertung |
| 8 | Fibroblastisches Neoplasma | 99.35% | L3 (geschätzt) | Warteposition – reiche Literatur zu Desmoid-Tumor/Solitary-fibrous-tumor-Subtypen (inkl. einartige Phase II, PMID 30578023), aber „fibroblastisches Neoplasma" als Kategorie ist zu breit/heterogen für eine einzelne Empfehlung |
| 9 | Nierenfibrosarkom | 99.33% | L5 | Warteposition – keine Studien-/Literatur-Unterstützung |
| 10 | Dermatofibrosarcoma protuberans | 99.29% | L2 (geschätzt) | Mit Vorsichtsmaßnahmen fortfahren (vorsichtig) – krankheitsspezifische Phase-II-Studie (NCT01059656, beendet) + multizentrische Phase-II-Publikation (PMID 32956651); starke mechanistische Rationale via COL1A1-PDGFB Fusion |

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Warteposition**

**Rationale:**
Die Wirksamkeits-Evidenz für die Top-Vorhersage (ungeklassifiziertes RCC) ist moderat (L2) und mechanistisch plausibel, und zwei weitere Kandidaten (Liposarkom, Dermatofibrosarcoma protuberans) zeigen sogar stärkere krankheitsspezifische Studien-Evidenz. Dieser Kandidat kann jedoch nicht fortschreiten, weil (1) TFDA-Warnhinweise/Kontraindikationen eine **Blockierungslücke** sind, die eine Sicherheits-Vor-Bewertung (S1) verhindert, und (2) das Arzneimittel derzeit null Marktgenehmigungen in Deutschland hat, daher sind regulatorischer Weg und lokale Kennzeichnung undefined.

**Folgendes ist erforderlich, um fortfahren zu können:**
- Fachinformation von TFDA/BfArM abrufen (Warnhinweise, Kontraindikationen, DDI), um DG001 vor jeder Sicherheits-Vor-Bewertung zu lösen
- Formale DrugBank/MOA-Daten beschaffen, um DG002 zu lösen und mechanistische Link-Bewertung zu unterstützen
- Regulatorischen Weg bestätigen angesichts 0 aktueller Marktgenehmigungen in Deutschland
- Falls Liposarkom oder Dermatofibrosarcoma protuberans parallel verfolgt werden, diese aufgrund stärkerer krankheitsspezifischer Phase-II-Evidenz priorisieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

