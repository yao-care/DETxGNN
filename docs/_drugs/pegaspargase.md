---
layout: default
title: Pegaspargase
parent: Hohe Evidenz (L1-L2)
nav_order: 296
evidence_level: L1
indication_count: 10
---

# Pegaspargase
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **10** 
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

# Pegaspargase: Von der akuten lymphoblastischen Leukämie zum Precursor Lymphoblastischen Lymphom/Leukämie

## Zusammenfassung in einem Satz

> Pegaspargase ist ein pegyliertes Asparaginase-Enzym, das lange als Basis-Agent in der Behandlung der akuten lymphoblastischen Leukämie (ALL) und des lymphoblastischen Lymphoms (LBL) verwendet wird.
> Die beste von TxGNN vorhergesagte Indikation — **Precursor Lymphoblastisches Lymphom/Leukämie** — ist in Wirklichkeit eine Umformulierung der bereits etablierten Kernindikation des Arzneistoffs und keine genuinely neue Anwendung.
> Dieses Signal wird durch **über 60 klinische Studien** (viele Phase 3) und **20 Publikationen** gestützt, aber die Evidenz bestätigt bekannte Pharmakologie und eröffnet keine neue therapeutische Richtung. Mehrere niedriger bewertete, genuinely „neue" Kandidaten (z. B. Hodgkin-Lymphom, Lymphoid-Neoplasma insgesamt) tragen viel schwächere und teilweise nicht übereinstimmende Evidenz und werden separat unten aufgeführt.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Akute lymphoblastische Leukämie (ALL) / Lymphoblastisches Lymphom — international etablierte Anwendung; nicht in deutschen Zulassungsdaten dokumentiert (Arzneistoff nicht im Handel) |
| Vorhergesagte neue Indikation | Precursor Lymphoblastisches Lymphom/Leukämie *(überschneidet sich im Wesentlichen mit der ursprünglichen genehmigten Anwendung — siehe Warnung unten)* |
| TxGNN-Vorhersage-Score | 99,96% |
| Evidenzstufe | L1 |
| Marktstatus Deutschland | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Fortfahren mit Vorsichtsmaßnahmen |

⚠️ **Wichtiger Hinweis**: „Precursor lymphoblastisches Lymphom/Leukämie" ist klinisch gleichbedeutend mit der bestehenden Hauptindikation des Arzneistoffs (ALL/LBL), nicht ein neuer Krankheitsbereich. Die Repurposing-Begründung im Evidenzpaket bestätigt ausdrücklich, dass dies „ein bestehendes genehmigtes Wirkprinzip ist, keine neue Anwendung." Vorsichtsmaßnahmen hier betreffen die Behandlung bekannter Toxizitäten (Überempfindlichkeit, Pankreatitis, Thrombose), nicht de-novo Indikations-Risiko.

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind keine detaillierten strukturierten Wirkungsweise-Daten aus DrugBank in diesem Evidenzpaket verfügbar (als Datenlücke gekennzeichnet). Basierend auf der beigefügten Repurposing-Begründung und bekannten Pharmakologie hydrolysiert Pegaspargase zirkulierendes Asparagin. Lymphoblasten in ALL/LBL zeigen charakteristischerweise eine niedrige oder fehlende Asparagin-Synthetase-Expression, sodass sie auf exogenes Asparagin angewiesen sind; ein Abbau davon führt zur Zellstarvation und Apoptose-Einleitung. Dies ist ein klassisches, Jahrzehnte-etabliertes Wirkprinzip — keine neu entdeckte Stoffwechselweg.

Da die beste TxGNN-Vorhersage (Precursor lymphoblastisches Lymphom/Leukämie) und die 5.-beste Vorhersage (akute lymphoblastische Leukämie) beide die eigene genehmigte Indikation des Arzneistoffs beschreiben, reproduziert das Modell im Wesentlichen bekannte Biologie statt eine Repurposing-Gelegenheit zu identifizieren. Dies ist ein nützlicher Plausibilitätscheck für die Modellgültigkeit, sollte aber nicht gegenüber Stakeholdern als „neue Indikation" berichtet werden.

Die interessanteren Signale sitzen weiter unten in der Rankings-Liste — Hodgkin-Lymphom (Rank 8) und die breitere Kategorie „Lymphoid-Neoplasma" (Rank 7) — wo die Evidenz schwächer ist und bei näherer Betrachtung weitgehend aus einer *anderen* Krankheitsentität (extranodales NK/T-Zell-Lymphom, ein Non-Hodgkin-Subtyp) statt aus klassischem Hodgkin-Lymphom stammt. Diese Nichtübereinstimmung wird im Begründungstext ausdrücklich hervorgehoben und sollte vor jeder weiteren Evaluierung geklärt werden.

---

## Evidenz aus klinischen Studien

*(aus predicted_indications[0]: Precursor lymphoblastisches Lymphom/Leukämie)*

| Studiennummer | Phase | Status | Einschluss | Schlüsselergebnisse |
|---------|------|------|------|---------|
| [NCT03020030](https://clinicaltrials.gov/study/NCT03020030) | Phase 3 | Aktiv, keine Rekrutierung mehr | 560 | Großes pädiatrisches/adoleszentes Neu-ALL-Protokoll mit Pegaspargase als Basis-Agent (Grad-A-Relevanz) |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Aktiv, keine Rekrutierung mehr | 2044 | Französisches nationales pädiatrisches ALL-Protokoll zur Optimierung der L-Asparaginase-(Pegaspargase-)Dosierung/Anwendung (Grad-A-Relevanz) |
| [NCT04954326](https://clinicaltrials.gov/study/NCT04954326) | Phase 2 | Abgeschlossen | 89 | PK-Vergleich flüssiger vs. lyophilisierter Pegaspargase-(S95014-)Formulierungen bei neu diagnostiziertem pädiatrischem ALL |
| [NCT06195735](https://clinicaltrials.gov/study/NCT06195735) | N/A | Abgeschlossen | 649 | Große Beobachtungsstudie zur Vorhersage der Überempfindlichkeit gegen PEG-Asparaginase zur Optimierung von ALL-Ergebnissen |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Rekrutiert | 440 | Randomisierte Studie zu Levocarnitin zur Verhinderung von asparaginase-assoziierter Hepatotoxizität bei AYA-ALL/LBL-Patienten |
| [NCT00187083](https://clinicaltrials.gov/study/NCT00187083) | Phase 3 | Abgeschlossen | 40 | Vergleich native vs. PEG-Asparaginase während Induktion bei rückfälligem/refraktärem Kindheits-ALL |
| [NCT00003437](https://clinicaltrials.gov/study/NCT00003437) | Phase 3 | Unbekannt | 1800 | UK-Nationales Kindheits-ALL-Studium mit Vergleich von Steroid-/Chemotherapie-Regimen |
| [NCT01665001](https://clinicaltrials.gov/study/NCT01665001) | Phase 2 | Unbekannt | 200 | Individualisierte MRD-adaptive Therapie für Erwachsene mit Precursor-Lymphoid-Neoplasien (PALG) |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Abgeschlossen | 37 | Methotrexat/Vincristin/pegylierte-Asparaginase/Dexamethason-Salvage-Regime bei rückfälligem ALL |
| [NCT00882206](https://clinicaltrials.gov/study/NCT00882206) | Phase 2 | Beendet | 15 | Decitabin + Vorinostat + VPLD-Chemo (inklusive PEG-Asparaginase) bei rückfälligem/refraktärem ALL/LBL |

---

## Literaturevindenz

| PMID | Jahr | Typ | Journal | Schlüsselergebnisse |
|------|-----|------|------|---------|
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Kohort (Tier 1) | Blood Advances | GIMEMA LAL1913: pegaspargase-modifiziertes risiko-orientiertes Programm verbessert Ergebnisse in Erwachsenen-ALL/LBL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Kohort (Tier 1) | J Clin Oncol | DFCI 11-001: Wirksamkeit/Toxizität von Pegaspargase vs. Calaspargase Pegol in Kindheits-ALL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review (Tier 2) | Haematologica | Expertenkonzens zur Erkennung/Prävention/Behandlung von asparaginase-assoziierter Nebenwirkungen bei Erwachsenen |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Kohort/Phase 2 | Int J Hematol | Phase-2-Multizenterstudie von Pegaspargase bei japanischen Patienten mit unbehandeltem ALL |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Phase-3-RCT | J Clin Oncol | COG AALL1231: Bortezomib in neu diagnostiziertem T-ALL/T-LL (Pegaspargase als Basis-Agent) |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | Phase-3-RCT | J Clin Oncol | COG AALL0434: Nelarabin in neu diagnostiziertem T-ALL (Pegaspargase-haltige Basis-Therapie) |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 (Langzeit-F/u) | Leukemia | Venetoclax + Hyper-CVAD/Nelarabin/pegylierte Asparaginase in T-ALL/LBL |
| [35987855](https://pubmed.ncbi.nlm.nih.gov/35987855/) | 2022 | Konsens/Review | Bulletin du Cancer | Empfehlungen der Französischen Gesellschaft zur Prävention/Behandlung von Pegaspargase-Toxizitäten |
| [31571395](https://pubmed.ncbi.nlm.nih.gov/31571395/) | 2020 | Fallserie | Pediatr Blood Cancer | Schnelle Desensibilisierungsprotokoll ermöglicht kontinuierliche Pegaspargase-Nutzung bei überempfindlichen pädiatrischen Patienten |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Grundlegende Pharmakologie-Review von PEG-Asparaginase in Leukämie-Behandlung |

---

## Andere von TxGNN vorhergesagte Indikationen (vollständige Kandidatenliste)

Das Evidenzpaket bewertete 10 Kandidaten-Indikationen für Pegaspargase. Zur Transparenz wird angesichts des Multi-Kandidaten-Charakters dieses Pakets die vollständige Ranking unten zusammengefasst:

| Rank | Krankheit | Score | Evidenzstufe | Empfehlung | Anmerkung |
|------|---------|-------|-----------------|-----------------|------|
| 1 | Precursor lymphoblastisches Lymphom/Leukämie | 99,96% | L1 | Fortfahren mit Vorsichtsmaßnahmen | = bestehende genehmigte Indikation, nicht neu |
| 2 | Prä-Keimzentrum CLL/SLL | 99,95% | L5 | Halten | Keine mechanistische Stützung; wahrscheinlich Graph-Struktur-Artefakt |
| 3 | CLL/SLL mit IGHV-somatischer Hypermutation | 99,95% | L5 | Halten | Dasselbe wie oben |
| 4 | Follikuläres Lymphom | 99,90% | L5 | Halten | Reife B-Zellen; nicht asparagin-abhängig; keine Evidenz |
| 5 | Akute lymphoblastische Leukämie | 99,89% | L1 | Fortfahren mit Vorsichtsmaßnahmen | = bestehende genehmigte Indikation, nicht neu |
| 6 | Methylcobalamin-Mangel (cblE) | 99,74% | L5 | Halten | Mechanistisch unabhängig; wahrscheinlich Daten-/Ontologie-Artefakt |
| 7 | Lymphoid-Neoplasma (breite Kategorie) | 99,71% | L3 | Forschungsfrage | Evidenz ist ALL-spezifisch, nicht verallgemeinerbar auf alle lymphoiden Tumoren |
| 8 | Hodgkin-Lymphom | 99,71% | L2 | Forschungsfrage | ⚠️ Die meisten zitierten Evidenzen sind tatsächlich für NK/T-Zell-Lymphom (ein anderer NHL-Subtyp), nicht klassisches Hodgkin-Lymphom — Etikett-Nichtübereinstimmung muss geklärt werden |
| 9 | CLL/SLL | 99,68% | L5 | Halten | Keine mechanistische Stützung; keine Evidenz |
| 10 | CML-Blastenphase, BCR-ABL1+ | 99,61% | L4 | Forschungsfrage | Plausibel nur für lymphoides Blastenkrise-Subtyp; nicht unterschieden von myeloider Blastenkrise in Evidenz |

**Interpretation**: Nur Ranks 1 und 5 haben starke (L1) Evidenz, und beide formulieren einfach die bekannte Indikation um. Ranks 7, 8 und 10 sind genuine „Forschungsfrage"-Kandidaten, aber mit schwacher, teilweise nicht übereinstimmender Evidenz. Ranks 2, 3, 4, 6 und 9 sollten gehalten werden — kein plausibles Wirkprinzip und null unterstützende Studien/Literatur.

---

## Marktinformationen Deutschland

Pegaspargase hat derzeit **keine Zulassung in Deutschland** in diesem Datensatz (`market_status: Not marketed`, `total_licenses: 0`). Keine Produktlisten sind verfügbar zusammengefasst.

---

## Zytotoxizität

Pegaspargase ist ein antineoplastisches Mittel (asparagin-abbauendes Enzym), das als Kernkomponente von ALL/LBL-Chemotherapie-Regimen verwendet wird — es erfüllt die antineoplastischen Kriterien über die ursprüngliche Indikation und etablierte Arzneistoffklasse.

| Punkt | Inhalt |
|-------|--------|
| Zytotoxizitäts-Klassifizierung | Konventionell zytotoxisch — enzym-basiert (asparagin-abbauend), unterschiedlich von DNA-schädigenden oder gezielten Wirkstoffen |
| Myelosuppressions-Risiko | Niedrige direkte Myelosuppression durch Pegaspargase selbst; jedoch wird es fast immer mit myelosuppressiven Mitteln kombiniert (Vincristin, Anthrazykline, Corticosteroide), sodass Myelosuppressions-Risiko des Kombinationsregimes hoch ist |
| Emetogenitäts-Klassifizierung | Niedrig bis moderat |
| Überwachungspunkte | Gerinnungsanalytik (Fibrinogen, Antithrombin III), Leberfunktionsprüfung, Lipase/Amylase (Pankreatitis), Nüchtern-Glukose/Triglyceride, Zeichen von Überempfindlichkeit, CBC (Regimen-weit) |
| Schutzmaßnahmen bei der Handhabung | Ja — Standard-Zytotoxisch/Antineoplastisch-Arzneistoff-Handhabungsvorsichtsmaßnahmen gelten während Vorbereitung und Verabreichung |

---

## Sicherheitsaspekte

Bitte lesen Sie die Fachinformation für Sicherheitsinformationen. (Schlüsselwarnungen, Kontraindikationen und DDI-Daten sind alle als Datenlücken in diesem Evidenzpaket gekennzeichnet; keine DDI-Einträge wurden gefunden.)

---

## Fazit und nächste Schritte

**Entscheidung: Fortfahren mit Vorsichtsmaßnahmen** *(für den Kandidaten mit der besten Bewertung — mit dem Hinweis, dass dies bestätigend ist, nicht eine neue Indikation)*

**Begründung:**
- Die beste TxGNN-Vorhersage formuliert die bereits etablierte, leitlinienmäßige Anwendung von Pegaspargase in ALL/LBL um, gestützt durch mehrere Phase-3-Studien und konsistente Literatur — die Evidenz ist stark, aber es gibt keinen neuen Indikations-Wert zu erfassen.
- Genuinely explorative Kandidaten (Hodgkin-Lymphom, Lymphoid-Neoplasma insgesamt, CML Lymphoide Blastenphase) bleiben im „Forschungsfrage"-Stadium mit dünner oder nicht übereinstimmender Evidenz und sollten nicht weitergehen, ohne zusätzliche Arbeit.

**Zum Fortfahren ist Folgendes erforderlich:**
- DG001 (Blockierend) auflösen: TFDA/BfArM-Fachinformation Warnungen und Kontraindikationen beschaffen, bevor S1-Sicherheits-Vorbewertung durchgeführt werden kann.
- DG002 (Hoch) auflösen: strukturierte MOA-Daten aus DrugBank beschaffen, um formale mechanistische-Verbindungs-Bewertung zu unterstützen.
- Für den Hodgkin-Lymphom-Kandidaten (Rank 8): klären, ob die zugrunde liegende Evidenz (NK/T-Zell-Lymphom-Studien) fehlerhaft dem Hodgkin-Lymphom zugeordnet wurde, bevor jede weitere Evaluierung durchgeführt wird.
- Für „Lymphoid-Neoplasma" (Rank 7): Evidenzbasis auf Krankheits-Subtypen eingrenzen, die tatsächliche Asparagin-Synthetase-Mangel-Daten haben, anstatt es als einzelne breite Kategorie zu behandeln.
- Angesichts dessen, dass das Arzneimittel in Deutschland nicht im Handel ist, Regulierungs-Pathway/Relevanz für diesen Markt bestätigen, bevor weitere Evaluierungs-Ressourcen diesem Markt zugeordnet werden.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

