---
layout: default
title: Zanubrutinib
parent: Nur Modellvorhersage (L5)
nav_order: 432
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Zanubrutinib: Von B-Zell-Neoplasien zu Myeloischer Leukämie

## Zusammenfassung in einem Satz

> Zanubrutinib ist ein Bruton-Tyrosinkinase-(BTK-)Inhibitor, dessen etablierte Evidenzgrundlage (basierend auf der Fachliteratur in diesem Paket) auf B-Zell-Neoplasien wie CLL/SLL und Waldenström-Makroglobulinämie konzentriert ist.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam bei **myeloischer Leukämie** ist, mit einem Vorhersagescore von **99.65%**,
> aber **keiner der angeführten klinischen Studien oder Publikationen untersucht direkt Zanubrutinib bei myeloischer Leukämie** — die Studien betreffen unterschiedliche investigative Arzneistoffe, und die Literatur unterstützt nur seine bekannten lymphoiden Malignomindikationen.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht formal dokumentiert in diesem Paket (keine BfArM-Zulassungsdaten; Fachliteratur deutet darauf hin, dass Zanubrutinib eine etablierte BTK-Inhibitor-Therapie für CLL/SLL und andere B-Zell-Neoplasien ist) |
| Prognostizierte neue Indikation | Myeloische Leukämie |
| TxGNN Vorhersagescore | 99.65% |
| Evidenzgrad | L5 (nur Modellprognose — angeführte Studien betreffen nicht verwandte Arzneistoffe; angeführte Fachliteratur behandelt nicht myeloische Leukämie) |
| Marktstatus Deutschland | ✗ Nicht vertrieben |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellung |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Mechanismus-der-Wirkung-Daten von DrugBank sind derzeit nicht verfügbar (blockierende Datenlücke, DG002). Basierend auf den in diesem Evidenzpaket verfügbaren Informationen ist Zanubrutinib ein Inhibitor der nächsten Generation mit hoher Selektivität für BTK, der die B-Zell-Rezeptor-Signalisierung blockiert — ein Signalweg, der zentral für B-Zell-Neoplasien ist. Seine klinische Evidenz (SEQUOIA, ALPINE und verwandte Studien) konzentriert sich nahezu vollständig auf CLL/SLL und Waldenström-Makroglobulinämie.

Myeloische Leukämie entsteht aus einer anderen hämatopoetischen Linie als CLL/SLL, und BTK ist nicht als Schlüsseltreiber in myeloischen Neoplasien etabliert, wie es in B-Zell-Lymphoid-Erkrankungen der Fall ist. Die beiden unter dieser prognostizierten Indikation gefundenen klinischen Studien (NCT04477291, NCT05665530) testen tatsächlich nicht Zanubrutinib bei myeloischer Leukämie — sie betreffen unterschiedliche investigative Substanzen (Luxeptinib/CG-806 und PRT2527), die zufällig in der gleichen Trialregister-Suche vorkommen, oder verwenden Zanubrutinib nur als Vergleichs-Kombination in nicht verwandten hämatologischen Neoplasien. Zusammen betrachtet reflektiert diese Vorhersage wahrscheinlich eher eine Übergeneralisierung des TxGNN-Embeddings für die breite Krankheitskategorie „Leukämie" als eine mechanistisch fundierte Hypothese.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Anzahl der Studienteilnehmer | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | Beendet | 45 | Testet **Luxeptinib (CG-806)**, nicht Zanubrutinib, in rezidivierten/refraktären AML/MDS; Studie beendet — nicht als unterstützender Beweis verwendbar |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Abgeschlossen | 86 | Testet **PRT2527 (CDK9-Inhibitor)** als Monotherapie und in Kombination mit Zanubrutinib oder Venetoclax in rezidivierten/refraktären hämatologischen Neoplasien; Zanubrutinib ist ein Kombinationsarm-Komparator, nicht das Studienmedikament speziell für myeloische Leukämie |

**Anmerkung:** Keine der beiden Studien bietet direkte Evidenz für die Monotherapie-Wirksamkeit von Zanubrutinib bei myeloischer Leukämie.

---

## Fachliteratur-Evidenz

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 5-Jahres-Nachbeobachtung: Zanubrutinib vs. Bendamustin+Rituximab in unbehandelter CLL/SLL |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Kohortenstudie | Blood Advances | Zanubrutinib gut verträglich/wirksam bei CLL/SLL-Patienten, die Ibrutinib/Acalabrutinib nicht vertragen |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Übersichtsarbeit | Blood Advances | Gepoolte Analyse von Zanubrutinib bei del(17p)/TP53-mutierter CLL/SLL über SEQUOIA und ALPINE |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Kohortenstudie | Lancet Haematol | Phase-2-Einzelarm-Studie von Zanubrutinib bei BTK-Inhibitor-Intoleranz in B-Zell-Neoplasien |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Übersichtsarbeit | Pharmaceutics | TKI-Ära-Übersicht zu CML und CLL, allgemeiner Kontext zu Tyrosinkinase-Signalwegen |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Übersichtsarbeit | Leukemia | BTK-Inhibitoren, einschließlich Zanubrutinib, in Waldenström-Makroglobulinämie |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Fallbericht | Front Immunol | Fallbericht einer koexistierenden WM und B-ALL, nicht im Zusammenhang mit Zanubrutinib-Behandlungsergebnissen |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Übersichtsarbeit | Clin Lymphoma Myeloma Leuk | Risiko der HBV-Reaktivierung bei Patienten, die BTK-Inhibitoren erhalten, einschließlich Zanubrutinib |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Übersichtsarbeit | Anticancer Agents Med Chem | Allgemeine Übersichtsarbeit zur Synthese-Chemie von FDA-zugelassenen Krebsmedikamenten (2018–2021), nicht erkrankungsspezifisch |

**Wichtig:** Keine der oben angeführten Publikationen untersucht Zanubrutinib speziell bei myeloischer Leukämie. Sie repräsentieren die etablierte Evidenzgrundlage des Arzneistoffs für B-Zell-Neoplasien (CLL/SLL, Waldenström) sowie allgemeine Sicherheits-/Chemie-Übersichten. **Keine direkte Fachliteratur-Evidenz für die prognostizierte myeloische Leukämie-Indikation wurde gefunden.**

---

## Marktsituation Deutschland

Zanubrutinib ist derzeit **nicht auf dem deutschen Markt** (0 BfArM-Zulassungen gemäß Dokumentation in diesem Paket).

---

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizitäts-Klassifizierung | Zielgerichtete Therapie (BTK-Inhibitor; orales Small-Molecule-Kinase-Inhibitor, nicht konventionelle zytotoxische Chemotherapie) |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation (in diesem Paket sind keine quantitativen Toxizitätsdaten verfügbar) |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Überwachungs-Punkte | Blutbild mit Differenzierung; Hepatitis-B-Serologie/Viruslast — HBV-Reaktivierung wurde bei BTK-Inhibitoren einschließlich Zanubrutinib berichtet (PMID [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/)) |
| Handhabungsschutz | Bitte beachten Sie die Fachinformation und die institutionelle Richtlinie zum Umgang mit gefährlichen Arzneistoffen |

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen (Schlüsselwarnhinweise, Kontraindikationen und Wechselwirkungsdaten sind alle derzeit nicht in diesem Paket verfügbar — DG001, blockierend).

**Signal aus der Fachliteratur (nicht formales Sicherheitslabel):** BTK-Inhibitoren als Klasse, einschließlich Zanubrutinib, wurden mit einer Reaktivierung des Hepatitis-B-Virus assoziiert (PMID [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/)); ein HBV-Screening sollte vor Einleitung einer Therapie in Betracht gezogen werden, unter Vorbehalt der Bestätigung durch die offizielle Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Der TxGNN-Score ist hoch, aber die unterstützende Evidenz ist nicht substanziell — die beiden gefundenen klinischen Studien betreffen unterschiedliche investigative Arzneistoffe, und alle gefundene Fachliteratur unterstützt die *etablierten* B-Zell-Neoplasien-Indikationen von Zanubrutinib statt myeloischer Leukämie. In Kombination mit einer blockierenden Datenlücke zu zugelassenen-Label-Warnhinweisen/Kontraindikationen (DG001) und der Tatsache, dass der Arzneistoff derzeit nicht in Deutschland vertrieben wird, kann dieser Kandidat nicht über S0 hinausgehen.

**Um voranzukommen, ist folgendes erforderlich:**
- Behebung von DG001: BfArM/Hersteller-Label-Warnhinweise und Kontraindikationen, erforderlich vor jedem S1-Sicherheits-Screening
- Behebung von DG002: Bestätigte Mechanismus-der-Wirkung-Daten von DrugBank
- Jegliche dedizierte präklinische, mechanistische oder klinische Evidenz, die BTK-Signalisierung mit myeloischer Leukämie-Pathogenese verbindet (derzeit nicht vorhanden)
- Korrektur der klinischen-Studien-Zuordnungs-Pipeline, da beide gefundenen Studien Arzneistoff-nicht-übereinstimmend sind und nicht diesem Kandidaten zugeordnet hätten werden sollen

**Zusätzliche Anmerkung:** Platzierungen 2–6 (Wirbelkörperanomalie-Syndrom, Ganglioneurom, retroperitoneales Neoplasma, Ewing-Sarkom, Neuroblastom) sind alle Evidenzgrad L5 mit null oder nahezu null unterstützenden Studien/Fachliteratur und keinem plausiblen mechanistischen Zusammenhang mit BTK-Inhibition. Diese sollten mit niedriger Priorität behandelt werden, wenn nicht neue externe Evidenz auftaucht.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

