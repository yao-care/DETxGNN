---
layout: default
title: Golimumab
parent: Mittlere Evidenz (L3-L4)
nav_order: 184
evidence_level: L4
indication_count: 5
---

# Golimumab
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **5** 
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

# Golimumab: Von genehmigten Indikationen bei entzündlicher Arthritis zu rheumatoider Vaskulitis

## Zusammenfassung in einem Satz

Golimumab ist ein vollständig humaner Anti-TNF-α-Antikörper mit etablierten Indikationen bei entzündlicher Arthritis (rheumatoide Arthritis, Psoriasis-Arthritis, Spondylitis ankylosans und polyartikuläre juvenile idiopathische Arthritis gemäß Fachliteratur). Die Vorhersage des TxGNN-Modells deutet auf eine potenzielle Wirksamkeit bei **rheumatoider Vaskulitis** hin, aber die Beweise sind gemischt — **3 indirekt verwandte klinische Studien** und **6 Publikationen**, einschließlich Fallberichte, die beschreiben, dass Anti-TNF-Therapie sowohl Vaskulitis *behandelt* als auch *paradoxerweise induziert*. Dieses Evidenzpaket (`TW-DB06674-multi`) enthält vier weitere Kandidaten-Indikationen; zwei davon (Rang #3 und #5) sind erheblich besser unterstützt und werden am Ende dieses Berichts zusammengefasst.

---

## Kurzübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar aus formalen Zulassungsdaten (Golimumab ist derzeit in dieser Jurisdiktion nicht vermarktet); Fachliteratur bestätigt genehmigte Anwendung für rheumatoide Arthritis, Psoriasis-Arthritis, Spondylitis ankylosans und polyartikuläre JIA anderswo |
| Vorhergesagte neue Indikation | Rheumatoide Vaskulitis |
| TxGNN-Vorhersagepunktzahl | 99,73% (Rang 3700 in Modellausgabe) |
| Evidenzstufe | L4 |
| Status auf dem Markt Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Strukturierte Wirkmechanismus-Daten von DrugBank sind in diesem Evidenzpaket nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der abgerufenen Fachliteratur ist Golimumab ein vollständig humaner Anti-TNF-α-IgG1κ-Antikörper, der subkutan (oder intravenös) verabreicht wird und für rheumatoide Arthritis, Psoriasis-Arthritis und axiale Spondylarthritis zugelassen ist (PMID 28530020, 20065639).

Rheumatoide Vaskulitis ist eine schwerwiegende extraartikuläre Manifestation von langdauernder, seropositiver rheumatoider Arthritis, angetrieben durch Immunkomplexablagerung und TNF-vermittelte vaskuläre Entzündung. Mechanistisch könnte die Unterdrückung von TNF-α diesen vaskulitischen Prozess plausibel reduzieren, und ein Fallbericht vermerkt, dass die Inzidenz rheumatoider Vaskulitis seit der Einführung von Biologika-DMARDs (einschließlich Anti-TNF-Mitteln) abgenommen hat (PMID 29075910).

Die Beweise sind jedoch nicht eindeutig. Ein Fallbericht von zwei Patienten, die **Takayasu-Arteritis unter Anti-TNF-Therapie entwickelten** (PMID 22999907), veranschaulicht ein anerkanntes Phänomen der „paradoxen Vaskulitis", das mit dieser Wirkstoffklasse assoziiert ist — Anti-TNF-Mittel können bei einigen Patienten vaskulitische Erkrankungen auslösen oder offenbaren, anstatt sie zu behandeln. Dieses richtungsmäßig inkonsistente Signal ist der Hauptgrund, warum die Evidenzstufe auf L4 (Wirkmechanismus-/Fallbericht-Ebene) begrenzt ist, trotz des sehr hohen TxGNN-Scores, und warum die aktuelle Empfehlung lautet, bis zur Sicherheitsklarifizierung zu halten.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschreibung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Noch nicht rekrutierend | 80 | Bewertet perioperatives Immunsuppressiva-Management (einschließlich Anti-TNF) bei Rheumatologe-Patienten, die sich einer Schulterarthroplastie unterziehen; nur Populationsüberlappung, keine Vaskulitis-Spezifität |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unbekannt | 750.000 | Große Real-World-Studie zum Risiko des Neuauftretens von immunvermittelter entzündlicher Erkrankung (IMID) nach Biologika-Behandlung einer einzelnen IMID; kann Vaskulitis als Ergebnis erfassen, aber nicht als primären Endpunkt |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Abgeschlossen | 184 | Nicht-interventionelle Studie eines Biologikums (Tocilizumab, nicht Golimumab) bei RA-Patienten mit unzureichendem DMARD-Ansprechen; einbezogen wegen RA-Populationsüberlappung, nicht Golimumab- oder Vaskulitis-spezifisch |

---

## Fachliteratur-Evidenz

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Netzwerk-Metaanalyse | Int J Mol Sci | Vergleicht Golimumab und andere TNF-Inhibitoren über 36 RCTs zur radiographischen Gelenkdestruktion bei RA; starke vergleichende Effektivitätsdaten, aber kein Vaskulitis-Endpunkt |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Übersicht | BMC Medicine | Übersicht über Biologika-Therapien (einschließlich Anti-TNF-Mittel) für Autoimmunerkrankung/rheumatologische Erkrankungen, allgemeiner Effektivitäts-/Sicherheitskontext |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Kohorte | Semin Arthritis Rheum | Häufigkeit und Ursachen der Nierenerkrankung im Endstadium bei RA-Patienten; relevant für extraartikuläre RA-Last, aber nicht Vaskulitis-spezifisch |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Fallbericht | Rheumatol Int | Schwere Sepsis (Pyoderma gangrenosum/pyogene Arthritis) bei RA-Patienten auf Golimumab; merkt an, dass die Inzidenz rheumatoider Vaskulitis seit der Einführung von Anti-TNF-Mitteln abgenommen hat |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Fallbericht | Joint Bone Spine | Zwei Fälle von **Takayasu-Arteritis unter Anti-TNF-Therapie** — paradoxes Vaskulitis-Induktsions-Signal, das der therapeutischen Hypothese widerspricht |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Fallbericht | Ocul Immunol Inflamm | Behçet-Erkrankung-assoziierte Uveitis (eine vaskulitis-verwandte Erkrankung) erfolgreich mit Golimumab behandelt — ein positives Gegen-Signal |

---

## Marktinformationen Deutschland

Golimumab wird derzeit **nicht vermarktet** in dieser Jurisdiktion — es liegen keine Zulassungsunterlagen vor (`total_licenses: 0`).

---

## Sicherheitserwägungen

Strukturierte Sicherheitsdaten (Wichtigste Warnungen, Kontraindikationen, DDI) sind derzeit für diesen Wirkstoff in diesem Evidenzpaket nicht verfügbar.

**Aus Fachliteratur abgeleitetes Sicherheitssignal (nicht aus strukturierten Sicherheitsdaten):** Die Literatur enthält einen Fallbericht über Anti-TNF-assoziierte **paradoxe Vaskulitis** (Takayasu-Arteritis-Auftreten unter Anti-TNF-Therapie, PMID 22999907). Dieses direkt relevante Sicherheitssignal sollte geklärt werden, bevor rheumatoide Vaskulitis als Indikation verfolgt wird.

Bitte beachten Sie die Fachinformation für vollständige Sicherheitsinformationen, sobald diese verfügbar sind (siehe Datenlücke DG001 unten).

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die mechanistische Begründung für Anti-TNF-Therapie bei rheumatoider Vaskulitis ist plausibel, aber nicht einheitlich unterstützt — die Fachliteratur-Evidenz umfasst sowohl ein Schutz-Signal (abnehmende Vaskulitis-Inzidenz seit Anti-TNF-Einführung) als auch ein widersprehendes Signal (Anti-TNF-induzierte Vaskulitis-Fallberichte). Es gibt keine klinische Studie, die Golimumab direkt und angemessen für diese Indikation bewertet. Die Evidenzstufe ist L4 (nur Fallbericht/Wirkmechanismus).

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA/BfArM-Fachinformation Warnungen und Kontraindikationen (Datenlücke DG001, Blockierend — erforderlich vor jeglichem S1-Sicherheits-Screening)
- Strukturierte Wirkmechanismus-Daten von DrugBank (Datenlücke DG002, Hoch)
- Eine dedizierte Literaturübersicht zur Versöhnung des therapeutisch-vs-paradoxen Vaskulitis-Signals für Anti-TNF-Mittel
- Eine klinische Studie oder Registerstudie mit rheumatoider Vaskulitis als primärer oder expliziter sekundärer Endpunkt

---

## Andere Kandidaten-Indikationen in diesem Evidenzpaket

Dieses Evidenzpaket bewertete 5 Kandidaten-Indikationen für Golimumab. Die anderen vier, nach TxGNN gereiht, sind unten zusammengefasst — zwei sind erheblich besser unterstützt als die oben genannte Top-Vorhersage und rechtfertigen separate, dedizierte Bewertung.

| Rang | Indikation | TxGNN-Punktzahl | Evidenzstufe | Entscheidung | Anmerkung |
|------|-----------|-------------|-----------------|----------|------|
| 3 | **Entzündliche Spondylopathie** | 99,66% | **L1** | **Mit Vorsichtsmaßnahmen fortfahren** | Stärkster Kandidat — Golimumab ist bereits eine genehmigte Anti-TNF-Therapie für Spondylitis ankylosans, nr-axSpA und Psoriasis-Arthritis, unterstützt durch zahlreiche abgeschlossene Phase-3/4-RCTs (z. B. NCT00265083, NCT02186873, NCT03270501) und systematische Übersichten (PMID 36270657, 38503473). Dies ist weitgehend eine Erweiterung der bestehenden Indikation statt neuartige Umwidmung. |
| 5 | **Polyartikuläre juvenile rheumatoide Arthritis** | 99,59% | **L1** | **Mit Vorsichtsmaßnahmen fortfahren** | Auch stark unterstützt — Golimumab (subkutan und intravenös) ist bereits FDA-zugelassen für polyartikuläre JIA, unterstützt durch abgeschlossene Phase-3-RCTs (NCT01230827, NCT02277444) und Langzeit-Sicherheitsdaten (PMID 33493312, 28507219, 39089836). Kontinuierliche Überwachung erforderlich für pädiatrisches Langzeit-Immunsuppressionsrisiko (Infektion, Malignität). |
| 2 | Hypermobilität des Steißbeins | 99,67% | L5 | Halten | Keine klinischen Studien oder Fachliteratur; keine plausible biologische Verbindung zur TNF-α-Hemmung. Wahrscheinlich Knowledge-Graph-Rauschen. |
| 4 | Kummell-Erkrankung | 99,61% | L5 | Halten | Keine klinischen Studien oder Fachliteratur; vertebraler ischämischer Kollaps hat keine mechanistische Verbindung zu Golimumab. Wahrscheinlich Knowledge-Graph-Rauschen. |

**Empfehlung:** Priorisieren Sie separate, dedizierte Bewertungsberichte für **entzündliche Spondylopathie** und **polyartikuläre JIA** (Rang 3 und 5) — diese stellen die stärksten, am meisten handlungsfähigen Ergebnisse in diesem Evidenzpaket dar und sind viel entscheidungsbereiter als die Top-Vorhersage rheumatoider Vaskulitis. Ränge 2 und 4 können als niedrig-vertrauenswürdige Modellausgabe deprioritiert werden.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

