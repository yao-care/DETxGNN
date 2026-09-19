---
layout: default
title: Tocilizumab
parent: Nur Modellvorhersage (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: Von rheumatoider Arthritis zu ankyloser Spondylitis

## Zusammenfassung in einem Satz

Tocilizumab ist ein humanisierter monoklonaler Antikörper gegen den IL-6-Rezeptor, der ursprünglich für rheumatoide Arthritis (und später juvenile idiopathische Arthritis) entwickelt wurde.
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **ankylose Spondylitis** ist, mit einem sehr hohen Ähnlichkeitsscore, doch zeigen **9 klinische Studien** und **19 Veröffentlichungen** im Evidenzpaket, dass diese Hypothese bereits direkt getestet wurde — und die beiden pivotalen Phase III-Studien wurden **wegen mangelnder Wirksamkeit beendet**.

## Kurzübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Rheumatoide Arthritis *(keine strukturierten Lizenzierungsdaten verfügbar; bestätigt durch Literatur innerhalb dieses Evidenzpakets, z. B. PMID 19368420, 28841363)* |
| Vorhergesagte neue Indikation | Ankylose Spondylitis |
| TxGNN-Vorhersage-Score | 99,99% |
| Evidenzebene | L1 (Phase II/III RCT-ähnliche Evidenz — **negatives** Ergebnis) |
| Marktstatus in Deutschland | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfehlung zur Entscheidung | **Zurückhalten** |

## Warum ist diese Vorhersage angemessen?

Detaillierte strukturierte Daten zum Wirkmechanismus sind für dieses Arzneimittel nicht verfügbar (Datenlücke). Basierend auf der in diesem Evidenzpaket enthaltenen Literatur ist Tocilizumab ein humanisierter monoklonaler Antikörper, der den Interleukin-6-Rezeptor (IL-6R) blockiert und die IL-6-vermittelte pro-entzündliche Signalgebung hemmt. Seine Wirksamkeit ist bei rheumatoider Arthritis und juveniler idiopathischer Arthritis gut etabliert (anderweitig in diesem Evidenzpaket durch Pivot-Studien wie NCT00988221, NCT00144625 und NCT00144664 bestätigt).

IL-6 ist ein Akute-Phase-, pro-entzündliches Zytokin, das auch bei Krankheitsaktivität bei ankyloser Spondylitis (AS) erhöht ist, weshalb AS historisch als eine plausible Erweiterung der IL-6R-Blockade von RA angesehen wurde. Der sehr hohe TxGNN-Score spiegelt wahrscheinlich die enge topologische Ähnlichkeit zwischen RA und AS als entzündliche Gelenkerkrankungen im Knowledge Graph wider.

Allerdings weist die mechanistische Bewertung des Evidenzpakets selbst auf einen wichtigen Vorbehalt hin: Im Gegensatz zu RA ist die dominante pathogene Achse in AS/axialer Spondyloarthritis eher die IL-17/IL-23–Th17-Signalgebung als IL-6. Dies ist genau der mechanistische Hintergrund für das klinische Versagen von IL-6R-Antagonisten (sowohl Tocilizumab als auch Sarilumab) in AS. Zwei dedizierte Phase II/III-Placebokontrollierte RCTs — NCT01209702 (n=306) und NCT01209689 (n=113) — wurden beide **wegen mangelnder Wirksamkeit beendet**, und diese Ergebnisse wurden anschließend veröffentlicht (PMID 23765873, BUILDER-1/2). Dies ist echte, direkte negative klinische Evidenz und nicht nur das Fehlen von Evidenz, daher wird die Repurposing-Hypothese trotz des hohen Vorhersage-Scores des Modells nicht unterstützt.

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Beendet | 306 | Placebokontrollierte RCT von Tocilizumab 8 mg/kg IV alle 4 Wochen bei NSAR-refraktären, TNF-naiven AS-Patienten — **beendet wegen mangelnder Wirksamkeit** |
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Beendet | 113 | Placebokontrollierte RCT von Tocilizumab (4 oder 8 mg/kg IV) bei AS-Patienten mit unzureichendem Ansprechen auf vorherige TNF-Antagonisten — **beendet wegen mangelnder Wirksamkeit** |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unbekannt | 750.000 | Große Registerstudie zum Risiko immunvermittelter Erkrankungen bei Patienten mit biologischer Behandlung; nicht AS-Wirksamkeit-spezifisch |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Rekrutierend | 10.000 | Koreanisches bundesweites Biologika-/tsDMARD-Register für RA, AS und PsA-Sicherheit; Beobachtungsstudie, keine Wirksamkeitshypothese |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Rekrutierend | 2.500 | Zytokin-/Biomarker-Profilerstellung bei systemischen Entzündungserkrankungen; keine AS-Behandlungsstudie |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Abgeschlossen | 60 | Mechanistische Studie zur Tocilizumab-Wirkung auf T-Follikelzellen bei RA-Patienten; nicht AS-spezifisch |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Noch nicht rekrutierend | 80 | Perioperatives Immunsuppressiva-Management bei allgemeinen Rheumapatienten, die sich einer Schulterarthroplastie unterziehen; nicht AS-Wirksamkeit-spezifisch |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Abgeschlossen | 1.431 | Real-World-Observatorium — Hinweis: bewertet Infliximab (Inflectra), nicht Tocilizumab |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Noch nicht rekrutierend | 52 | Secukinumab bei Takayasu-Arteriitis — anderes Arzneimittel und andere Krankheit, geringe Relevanz |

## Literaturbeleg

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | BUILDER-1/2 RCTs zur Bewertung der kurzfristigen symptomatischen Wirksamkeit und Sicherheit von Tocilizumab in AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematische Übersicht / Netzwerk-Metaanalyse | Medicine | Vergleichende Wirksamkeit aller verfügbaren biologischen Regimen für AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Metaanalyse (Kohorte) | Clin Rheumatol | Risiko schwerwiegender Infektionen mit Biologika in AS und nicht-radiographischer axialer SpA |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Übersicht | Semin Arthritis Rheum | Optimierung der Zweitlinien-Biologika-Therapie in RA, PsA und AS |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Übersicht | Inflamm Allergy Drug Targets | Kurze Übersicht speziell zur IL-6-Antagonisierung in AS |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Übersicht | Joint Bone Spine | Biologische Wirkstoffe für AS über TNFα-Antagonisten hinaus |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Übersicht | Curr Opin Rheumatol | Behandlungsmöglichkeiten für TNF-Inhibitor-refraktäre AS |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Übersicht | Clin Exp Rheumatol | Biologika in der Behandlung von RA und AS |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2017 | Übersicht | Curr Pharm Biotechnol | Biologika in entzündlicher und immunvermittelter Arthritis, einschließlich AS |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Fallbericht | Front Med | Zwei Fälle erfolgreicher Behandlung von AA-Amyloidose sekundär zu AS mit Tocilizumab |

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

## Fazit und Nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Zwei dedizierte Phase II/III-Placebokontrollierte RCTs von Tocilizumab in ankyloser Spondylitis (NCT01209702, NCT01209689) wurden beide wegen mangelnder Wirksamkeit beendet, und dies steht im Einklang mit der mechanistischen Begründung im Evidenzpaket — AS-Pathogenese wird primär durch die IL-17/IL-23–Th17-Achse angetrieben, nicht durch IL-6. Dies ist direkte negative klinische Evidenz, nicht nur unzureichende Evidenz, daher sollte dieser spezifische Repurposing-Kandidat nicht vorangetrieben werden.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Fachinformation (Warnhinweise, Gegenanzeigen) — derzeit eine **blockierende** Datenlücke (DG001), erforderlich vor jeder S1-Sicherheitsbewertung von Tocilizumab für *jede* Indikation
- Strukturierte Daten zum Wirkmechanismus aus der DrugBank-API — **hochrangige** Datenlücke (DG002)
- Falls die Repurposing-Exploration für dieses Arzneimittel fortgesetzt wird, sollten andere Kandidaten in diesem Evidenzpaket mit günstigeren (oder zumindest nicht-negativen) Evidenzprofilen wie **rheumatoide Vaskulitis** (L4, gekennzeichnet als „Forschungsfrage" statt „Zurückhalten") Vorrang vor weiteren Arbeiten zur AS-Hypothese haben

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

