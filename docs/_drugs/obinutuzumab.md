---
layout: default
title: Obinutuzumab
parent: Hohe Evidenz (L1-L2)
nav_order: 275
evidence_level: L1
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **3** 
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

# Obinutuzumab: Von der Anti-CD20-Antikörpertherapie zum Follikulären Lymphom

## Zusammenfassung in einem Satz

Obinutuzumab ist ein glykotechnisch modifizierter Typ-II-Anti-CD20-Monoklonalantikörper; dieses Evidenzpaket enthält keinen bestätigten lokalen Originalindikationsdatensatz oder Markteintrag für das Arzneimittel (derzeit **nicht vermarktet** in dieser Gerichtsbarkeit). Das TxGNN-Modell sagt voraus, dass es wirksam für **Follikuläres Lymphom** sein könnte, mit **50 klinischen Studien** und **20 Publikationen**, die während der Evidenzsammlung identifiziert wurden — von denen die 10 relevantesten von jedem nachstehend zusammengefasst sind.

---

## Schnellüberblick

| Punkt | Inhalt |
|-------|--------|
| Originalindikation | Nicht verfügbar — keine zugelassene Indikation in den Unterlagen; das Arzneimittel ist derzeit in dieser Gerichtsbarkeit nicht vermarktet |
| Vorhergesagte neue Indikation | Follikuläres Lymphom |
| TxGNN-Vorhersage-Score | 99,18 % |
| Evidenzebene | L1 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl Genehmigungen | 0 |
| Empfohlene Entscheidung | Weitermachen mit Vorkehrungen |

**Hinweis zur Datenqualität:** Das gleiche Evidenzpaket stuft auch „CLL/SLL mit IGHV-Keimbahn-Hypermutation" (Score 99,21 %) und „pregerminal-center CLL/SLL" (Score 99,21 %) als die zwei besten TxGNN-Vorhersagen ein, aber beide haben 0 übereinstimmende klinische Studien und 0 Literatureinträge (Evidenzebene L5, Entscheidung: Zurückhalten). Die Rationale des Evidenzpakets selbst vermerkt explizit, dass dies im Widerspruch zu der öffentlich bekannten Tatsache steht, dass Obinutuzumab in mehreren Ländern für CLL zugelassen ist, und empfiehlt, die Datenquelle zu überprüfen, bevor eine Entscheidung zu diesen zwei Indikationen getroffen wird. Sie werden in diesem Bericht nicht weiter analysiert und sollten erneut abgefragt werden, anstatt als echte negative Befunde behandelt zu werden.

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkungsmechanismus-Daten sind nicht im strukturierten Feld `original_moa` dieses Evidenzpakets vorhanden (als Datenlücke gekennzeichnet). Jedoch beschreibt die unterstützende Literatur, die in der Evidenzgrundlage erfasst wurde, Obinutuzumab durchgehend als einen rekombinanten, humanisierten, glykotechnisch optimierten Typ-II-Anti-CD20-Monoklonalantikörper (z. B. PMID 28324270, PMID 31360086), der antikörperabhängige zelluläre Zytotoxizität (ADCC), komplementabhängige Zytotoxizität (CDC) und direkte B-Zell-Abtötung stärker fördert als Erste-Generation-Anti-CD20-Antikörper wie Rituximab.

Follikuläres Lymphom ist ein indolentes Keimzentrum-B-Zell-Lymphom, dessen bösartige Zellen charakteristischerweise CD20 auf ihrer Oberfläche exprimieren — das gleiche Zielantigen, das Anti-CD20-Antikörper (Rituximab, Obinutuzumab, Ofatumumab) bereits in anderen B-Zell-Malignomen behandeln. Dies verleiht der TxGNN-Vorhersage schon vor der Berücksichtigung von Studiendaten starke biologische Plausibilität: Sie verbindet ein bekanntes Wirkziel (CD20) mit einer Krankheit, die durch die Expression dieses Ziels definiert wird.

Kritisch ist, dass dies keine rein rechnerische Vorhersage ist — sie wird durch eine ungewöhnlich große und reife Sammlung von direkter klinischer Evidenz gestützt, einschließlich der pivotalen Phase-3-GALLIUM-Studie (PMID 28976863, 29856692, 37404773), die direkt eine obinutuzumab-basierte Immunchemotherapie gegen eine rituximab-basierte Immunchemotherapie in zuvor unbehandeltem follikulärem Lymphom verglich und eine überlegene progressionsfreie Überlebensdauer demonstrierte. Dies macht Follikuläres Lymphom zum am stärksten gestützten Repurposing-Kandidaten in diesem Evidenzpaket, im Gegensatz zu den zwei CLL/SLL-Vorhersagen oben, die derzeit keine abgeglichene Evidenz in diesem Datensatz haben.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---|---|---|---|---|
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Rekrutierung läuft | 1095 | EPCORE™FL-2: Epcoritamab + Lenalidomid/Rituximab vs. Chemoimmunotherapie in zuvor unbehandeltem FL |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Rekrutierung läuft | 190 | GAZEBO-Studie: Radiotherapie allein vs. Radiotherapie + Obinutuzumab in frühen FL-Stadien |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | Rekrutierung läuft | 780 | Zanubrutinib + Anti-CD20-Antikörper vs. Lenalidomid + Rituximab in rezidiviertem/refraktärem FL/MZL |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Abgeschlossen | 217 | Zanubrutinib + Obinutuzumab vs. Obinutuzumab-Monotherapie in rezidiviertem/refraktärem FL (ROSEWOOD) |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | Abgeschlossen | 96 | Obinutuzumab + Lenalidomid in zuvor unbehandeltem FL (Grad 1-3a, Stadium II-IV) |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1b/2 | Abgeschlossen | 317 | Obinutuzumab + Lenalidomid bei zuvor unbehandeltem und rezidiviertem/refraktärem FL und anderen B-Zell-Lymphomen |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Aktiv, keine Rekrutierung | 40 | Obinutuzumab + Ibrutinib + Venetoclax in zuvor unbehandeltem FL |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Abgeschlossen | 114 | Sicherheit von Obinutuzumab-Kurzinfusion bei zuvor unbehandeltem fortgeschrittenem FL |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | k. A. (Real-World) | Rekrutierung läuft | 332 | Real-World-Wirksamkeit/Sicherheit von Obinutuzumab-basierter Therapie in zuvor unbehandeltem FL |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | Aktiv, keine Rekrutierung | 33 | Obinutuzumab + CC-99282 in zuvor unbehandeltem, hochgradig tumorbelastestem FL |

---

## Literaturbeweise

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|---|---|---|---|---|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | The New England Journal of Medicine | Pivotale GALLIUM-Studie: Obinutuzumab- vs. Rituximab-basierte Chemotherapie in zuvor unbehandeltem fortgeschrittenem FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM-Subanalyse: Einfluss des Chemotherapie-Backbones (CHOP/CVP/Bendamustin) auf Wirksamkeit und Sicherheit |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM-Finalanalyse: Dauerhafter PFS-Vorteil von Obinutuzumab vs. Rituximab-Immunchemotherapie in FL/MZL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: Zanubrutinib + Obinutuzumab vs. Obinutuzumab-Monotherapie in rezidiviertem/refraktärem FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN-Studie: Obinutuzumab + Lenalidomid in rezidivierter/refraktärer follikulärer B-Zell-Lymphom |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | RCT | Haematologica | Polatuzumab Vedotin + Bendamustin/Rituximab oder Obinutuzumab in rezidiviertem/refraktärem FL (Phase Ib/II) |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Übersicht | Blood and Lymphatic Cancer: Targets and Therapy | Übersicht über Obinutuzumab-Aktivität allein und in Kombination in FL |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Übersicht | Targeted Oncology | Übersicht über Obinutuzumab bei Rituximab-refraktärem/rezidiviertem FL, einschließlich GADOLIN-Studie |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Übersicht | Turkish Journal of Haematology | Umfassende Übersicht über Staging, Prognose und Behandlungsoptionen in FL |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Übersicht | Frontiers in Pharmacology | Schnellübersicht über Wirksamkeit, Sicherheit und Kosteneffektivität von Obinutuzumab in FL |

---

## Marktinformationen Deutschland

Es sind keine Genehmigungsunterlagen verfügbar — `taiwan_regulatory.market_status` ist „Not marketed" mit 0 Lizenzen insgesamt in den Unterlagen. Obinutuzumab hat derzeit keinen registrierten Produkteintrag in dieser Gerichtsbarkeit der Regulierungsdatenbank.

---

## Zytotoxizität

Obinutuzumab ist ein antineoplastisches Arzneimittel (CD20-gerichteter Monoklonalantikörper, verwendet bei B-Zell-Malignomen, einschließlich Follikulärem Lymphom), daher gilt dieser Abschnitt.

| Punkt | Inhalt |
|-------|--------|
| Zytotoxizitätsklassifizierung | Gezielte Therapie / Immuntherapie (Anti-CD20-Monoklonalantikörper) — keine konventionelle zytotoxische Chemotherapie |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Überwachungselemente | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Schutzausrüstung bei Handhabung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |

---

## Sicherheitsüberlegungen

Bitte lesen Sie die Fachinformation für Sicherheitsinformationen.

---

## Schlussfolgerung und Nächste Schritte

**Entscheidung: Weitermachen mit Vorkehrungen**

**Begründung:**
Die vorhergesagte Assoziation zwischen Obinutuzumab und Follikulärem Lymphom wird durch eine starke CD20-gerichtete mechanistische Rationale und eine reife Evidenzbasis unterstützt, einschließlich einer pivotalen Phase-3-RCT (GALLIUM) sowie mehrerer abgeschlossener und laufender Phase-2/3-Studien — erfüllt den L1-Evidenzschwellenwert. Jedoch ist das Arzneimittel derzeit nicht registriert/nicht vermarktet in dieser Gerichtsbarkeit, und grundlegende Sicherheits-, MOA- und Regulierungsdaten bleiben unbestätigt, daher sollte eine Fortführung nur unter zusätzlichen Vorkehrungen erfolgen.

**Zum Fortschreiten ist Folgendes erforderlich:**
- Bestätigung der Wirkungsmechanismus- und DrugBank-Kategoriedaten (derzeit als Datenlücke gekennzeichnet, DG002)
- Beschaffung und Analyse der lokalen Fachinformation für Warnhinweise, Kontraindikationen und Wechselwirkungsdaten (derzeit als blockierende Datenlücke gekennzeichnet, DG001)
- Überprüfung des Status des lokalen Registrierungswegs, da derzeit 0 Genehmigungen in den Unterlagen eingetragen sind
- Erneute Abfrage der Datenquelle für die zwei CLL/SLL-Vorhersagen (Ränge 1–2), um die oben gekennzeichnete scheinbare Evidenzsammlungslücke zu beheben, bevor eine Entscheidung zu diesen Indikationen getroffen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

