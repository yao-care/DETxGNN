---
layout: default
title: Ezetimibe
parent: Hohe Evidenz (L1-L2)
nav_order: 162
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **4** 
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

# Ezetimib: Von Hypercholesterinämie zur Hyperlipoproteinämie

## Zusammenfassung in einem Satz

> Ezetimib ist ein Cholesterin-Absorptionshemmer, dessen etablierte klinische Anwendung die Senkung von LDL-Cholesterin bei Hypercholesterinämie und gemischter Dyslipidämie ist, typischerweise als Zusatztherapie zur Statin-Therapie.
> Das TxGNN-Modell prognostiziert, dass es für **Hyperlipoproteinämie** wirksam sein könnte,
> mit **50 klinischen Studien** und **19 Publikationen**, die diese Richtung derzeit unterstützen.
> ⚠️ Hinweis: Dieses Evidenzpaket selbst kennzeichnet ein Datenqualitätsproblem — siehe „Warum ist diese Vorhersage angemessen?" unten.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert in diesem Datensatz (Lizenzenliste ist leer) — klinisch bekannt als Hypercholesterinämie/Dyslipidämie; behandelt als Datenblockade (DG001), nicht als echte „keine ursprüngliche Indikation" |
| Vorhergesagte neue Indikation | Hyperlipoproteinämie |
| TxGNN-Vorhersagepunktzahl | 99.63% |
| Evidenzstufe | L1 |
| Deutschland Marktstatus | ✗ Nicht vermarktet *(gemäß diesem Datensatz — siehe Datenqualitätsanmerkung unten)* |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Mit Vorsichtsmaßnahmen fortfahren |

---

## Warum ist diese Vorhersage angemessen?

Ezetimib hemmt den intestinalen Niemann-Pick C1-ähnlichen 1-(NPC1L1-)Transporter, wodurch die Aufnahme von Cholesterin aus der Nahrung und Galle im Dünndarm verringert wird. Dies senkt die Cholesterin-Zufuhr zur Leber, erhöht die Expression von hepatischen LDL-Rezeptoren und führt zu einer klinisch bedeutsamen Reduktion von LDL-Cholesterin, typischerweise in Kombination mit Statinen verwendet, um einen additiven Senkungseffekt zu erzielen.

Hyperlipoproteinämie ist ein übergeordneter Begriff, der erhöhte LDL-C/gemischte Lipidstörungen umfasst — mechanistisch und klinisch überlappt dies direkt mit der bereits etablierten Verwendung von Ezetimib bei Hypercholesterinämie und gemischter Hyperlipidämie (wie sich in Dutzenden abgeschlossener Phase-3-Studien zeigt, einschließlich Kombinationen mit Fenofibrat, Statinen, Bempedoat und Obicetrapib).

**Datenqualitätsvorbehalt:** Die `repurposing_rationale` des Evidenzpakets kennzeichnet explizit eine interne Inkonsistenz: Dieser Datensatz verzeichnet `market_status = "Not marketed" (nicht vermarktet)` und eine leere `original_indications`-Liste, was dem bekannten Faktum widerspricht, dass Ezetimib (Zetia®/Ezetrol®) ein weltweit zugelassener Lipidsenker ist. Das Evidenzpaket selbst schlussfolgert, dass dies kein echtes Drug-Repurposing-Kandidat ist, sondern eher ein Fall von fehlenden/unvollständigen regulatorischen Quelldaten (BfArM-Kennzeichnung noch nicht aufgenommen — DG001, Blockade) kombiniert mit einem fehlenden MOA-Feld (DG002, Hoch). Die klinischen Studien und Literaturbeweise unten sind real und substanziell, aber sie unterstützen weitgehend eine bereits anerkannte Indikation anstatt einer echten innovativen Repositionierungshypothese. Dies muss gelöst werden, bevor eine nachgelagerte Entscheidung finalisiert wird.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Einschreibung | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Abgeschlossen | 50 | Ezetimib 10 mg + Atorvastatin/Simvastatin bei homozygöter familiärer Hypercholesterinämie |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Abgeschlossen | 576 | Fenofibrat + Ezetimib Coadministration bei gemischter Hyperlipidämie |
| [NCT00652431](https://clinicaltrials.gov/study/NCT00652431) | Phase 1 | Abgeschlossen | 18 | PK-Interaktionsstudie: Vytorin (Ezetimib/Simvastatin) + Niaspan (Niacin ER) |
| [NCT04929249](https://clinicaltrials.gov/study/NCT04929249) | Phase 3 | Abgeschlossen | 450 | „Inclisiran First"-Strategie vs. übliche Behandlung bei ASCVD mit erhöhtem LDL-C unter maximaler Statin ± Ezetimib |
| [NCT05255094](https://clinicaltrials.gov/study/NCT05255094) | Phase 3 | Abgeschlossen | 464 | AK102 (PCSK9-Inhibitor) bei primärer Hypercholesterinämie/gemischter Hyperlipidämie; Überschneidung der Ezetimib-relevanten Population |
| [NCT00552097 (ENHANCE)](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Abgeschlossen | 720 | Ezetimib + hochdosiertes Simvastatin vs. Simvastatin allein bei Progression der Karotis-Atherosklerose bei heterozygötem FH |
| [NCT03337308](https://clinicaltrials.gov/study/NCT03337308) | Phase 3 | Abgeschlossen | 382 | Bempedoat 180 mg + Ezetimib 10 mg FDK vs. Komponenten/Placebo zusätzlich zur maximalen Statin-Therapie |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Abgeschlossen | 407 | Obicetrapib 10 mg + Ezetimib 10 mg FDK bei HeFH und/oder ASCVD/Hochrisikopatienten |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Abgeschlossen | 135 | Langzeitsicherheit/Verträglichkeit von Ezetimib + Rosuvastatin FDK bei japanischen Patienten mit Hypercholesterinämie |
| [NCT01043380 (PRECISE-IVUS)](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Abgeschlossen | 245 | IVUS-gemessene koronare Plaques-Regression: Cholesterin-Absorptionshemmer (Ezetimib) vs. Synthesehemmer |

---

## Literaturbeweise

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM-Studie: Obicetrapib + Ezetimib FDK reduziert LDL-C signifikant |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oraler PCSK9-Inhibitor Enlicitid bei HeFH-Patienten, die LDL-C-Ziele unter bestehender Therapie incl. Ezetimib nicht erreichen |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Editorial/Kommentar | N Engl J Med | Editorial zur Cholesterinsenkung und Ezetimib (ENHANCE-Studien-Kontroverse) |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Übersichtsartikel | Drug and Therapeutics Bulletin | Ezetimib-Update: Wirksamkeits-/Sicherheitsübersicht, kein bewiesener CV-Mortalitäts-/Morbiditätsvorteil zum Zeitpunkt des Schreibens |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Übersichtsartikel | Cardiology Clinics | Übersicht der familären Hypercholesterinämie-Behandlung einschließlich Statine, Ezetimib und anderer LDL-senkender Mittel |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Übersichtsartikel | Indian Heart Journal | FH-Epidemiologie, Unterdiagnose und Behandlungslandschaft |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Übersichtsartikel | Int J Mol Sci | Postprandiale Hyperlipidämie-Pathophysiologie, Diagnose und Behandlung |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Übersichtsartikel | J Am Coll Cardiol | Aufstrebende LDL-C/ApoB-senkende Therapien incl. Ezetimib-basierte Kombinationen |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Übersichtsartikel | J Cardiovasc Pharmacol Ther | Umfassende Übersicht der PCSK9-Inhibitoren, statin-intolerant/FH-Populationen |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Übersichtsartikel | Circulation Research | Übersicht der Cholesterin-senkenden Wirkstoffklassen einschließlich Ezetimib |

---

## Informationen zum Deutschland-Markt

Es gibt keine BfArM-Genehmigungsdatensätze in diesem Evidenzpaket (`total_licenses = 0`, `licenses = []`). Dies widerspricht der bekannten langjährigen Marktpräsenz von Ezetimib in Deutschland/EU (z.B. Ezetrol®, Inegy®/Vytorin® Kombinationsprodukte) und wurde als Datenlücke **DG001 (Blockade)** erfasst — die regulatorischen Kennzeichnungs-/Genehmigungsdaten wurden noch nicht aus der BfArM-Quelle aufgenommen. Diese Lücke muss geschlossen werden, bevor Sicherheits- oder Genehmigungsaussagen über diesen Kandidaten gemacht werden können.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. *(Alle Sicherheitsfelder in diesem Datensatz — wichtigste Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungen — sind derzeit nicht verfügbar; DDI-Abfrage ergab keine Ergebnisse.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Mit Vorsichtsmaßnahmen fortfahren**

**Begründung:**
Die Grundlage der klinischen Studien und Literatur für Ezetimib bei LDL-C/Hyperlipoproteinämie-typischen Indikationen ist umfangreich und hochwertig (L1-Evidenz, mehrere abgeschlossene Phase-3-RCTs einschließlich der pivotalen ENHANCE-Studie und moderner FDK-Studien). Allerdings sind die regulatorischen und MOA-Felder dieses Datensatzes unvollständig und intern inkonsistent mit dem bekannten realen Genehmigungsstatus von Ezetimib, daher sollte dies als Evidenzkonsolidierung für eine plausible/wahrscheinlich bereits zugelassene Verwendung behandelt werden, anstatt ein validiertes neues Repurposing-Signal, bis die Datenlücken gelöst sind.

**Zum Fortfahren ist Folgendes erforderlich:**
- Beheben Sie DG001 (Blockade): Rufen Sie die eigentliche BfArM/TFDA-Kennzeichnung PDF ab und analysieren Sie sie, um den tatsächlichen Marktstatus, Lizenzen und genehmigten Indikationstext zu bestätigen
- Beheben Sie DG002 (Hoch): Fragen Sie die DrugBank-API für bestätigte MOA ab, um den aktuellen Platzhalter zu ersetzen
- Gleichen Sie die `market_status = "Not marketed"`/leeren `original_indications`-Felder mit den bekannten genehmigten Indikationen von Ezetimib ab, um zu bestimmen, ob „Hyperlipoproteinämie" eine echte neue Kennzeichnungserweiterung oder eine bestehende zulassungskonforme Verwendung ist
- Beschaffen Sie Sicherheits-/Kontraindikationsdaten (wichtigste Warnhinweise, DDI), sobald die Kennzeichnungsquelle verfügbar ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

