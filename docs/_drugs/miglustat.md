---
layout: default
title: Miglustat
parent: Nur Modellvorhersage (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: Von der Gaucher-Krankheit zur Tay-Sachs-Krankheit (GM2-Gangliosidose)

## Zusammenfassung in einem Satz

Miglustat ist ein Glukosylceramid-Synthase-Inhibitor (Substratreduktionstherapie), der ursprünglich in der EU für die Gaucher-Krankheit Typ 1 zugelassen wurde. Unter den zehn von TxGNN vorhergesagten Indikationen ist die **Tay-Sachs-Krankheit (GM2-Gangliosidose)** der einzige Kandidat, der durch Daten aus der Praxis gestützt wird — **5 klinische Studien** (einschließlich einer abgeschlossenen randomisierten kontrollierten Studie) und **20 Publikationen** — obwohl er auf der rohen TxGNN-Punktzahl niedriger rangiert als mehrere mechanistisch schwächer begründete, evidenzfreie Kandidaten.

> **Anmerkung zur Kandidatenauswahl:** Die #1-bewertete Vorhersage von TxGNN („autosomal rezessives Ichthyose-Syndrom mit tödlichem Krankheitsverlauf") hat keine unterstützenden Studien oder Literatur und weist laut der eigenen Begründungsnotiz des Modells einen „schwachen mechanistischen Bezug" auf. Die Tay-Sachs-Krankheit (Rang 7 nach Punktzahl) ist die einzige Vorhersage in diesem Paket mit wesentlichen klinischen Belegen, daher konzentriert sich dieser Bericht auf sie als umsetzbarer Kandidat.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Gaucher-Krankheit Typ 1 (gemäß Literaturbelegen in diesem Paket; amtlicher behördlicher Indikationstext nicht verfügbar — siehe Datenlücken) |
| Vorhergesagte neue Indikation | Tay-Sachs-Krankheit (GM2-Gangliosidose) |
| TxGNN-Vorhersagepunktzahl | 99.75% (Rang 3492 von gesamtem Kandidatensatz) |
| Beweisstufe | L2 (1 abgeschlossene randomisierte kontrollierte Studie + unterstützende systematische Übersicht) |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage sinnvoll?

Ausführliche DrugBank-Wirkmechanismus-Daten sind in diesem Paket als Datenlücke gekennzeichnet, aber der Wirkmechanismus ist in den gesammelten Literaturbelegen gut dokumentiert: Miglustat ist ein oral applizierter **Glukosylceramid-Glukosyltransferase (Glukosylceramid-Synthase)-Inhibitor**, der als **Substratreduktionstherapie (SRT)** bei Glykosphingolipid-Speicherkrankheiten (GSL) wirkt (PMID 12808890, 11227045, 16763917).

Die Tay-Sachs-Krankheit wird durch einen β-Hexosaminidase-A-Mangel verursacht, der zu einer lysosomalen Ansammlung von GM2-Gangliosid führt — einem Glykosphingolipid, das über den gleichen oberen Glukosylceramid-Weg synthetisiert wird, den Miglustat hemmt. Da Miglustat die *Produktion* von GSL-Substraten (einschließlich GM2-Gangliosid-Vorläufern) reduziert, statt das fehlende Enzym zu ersetzen, ist die mechanistische Begründung für die Erweiterung von der Gaucher-Krankheit (Glukosylceramid-Ansammlung) auf die Tay-Sachs-Krankheit (GM2-Gangliosid-Ansammlung) direkt und biologisch plausibel — im Gegensatz zu den meisten anderen TxGNN-vorhergesagten Kandidaten in diesem Paket, deren Zielkrankheiten verschiedene Speicherwege betreffen (Cholesterin-Ester, Sulfatide, Steroid-Sulfat).

Diese mechanistische Plausibilität spiegelt sich auch in der Studienprotokolle wider: Miglustat wird bereits seit dem späten 20. Jahrhundert in Tiermodellen und Patienten mit Tay-Sachs/Sandhoff-Krankheit (GM2-Gangliosidose) untersucht, gipfelnd in einer RCT und einer systematischen Übersicht von 2023 — was dies zu dem am weitesten entwickelten Umwidmungskandidaten in diesem Paket macht, trotz gemischter Wirksamkeitsergebnisse (siehe unten).

---

## Klinische Studienbelege

| Studiennummer | Phase | Status | Einschluss | Wichtige Ergebnisse |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Abgeschlossen | 10 | PK, Sicherheit und Verträglichkeit von Miglustat bei infantiler GM2-Gangliosidose (Einzel-/Steady-State-Oralgabe) |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Abgeschlossen | 5 | PK und Verträglichkeit von Miglustat bei juveniler GM2-Gangliosidose, Einzel- und Mehrfachdosen |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Beendet | 30 | Umfrage zur therapeutischen Wirkung von Miglustat auf neurologische/systemische Symptome bei infantiler Sandhoff- und Tay-Sachs-Krankheit |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Beendet | 16 | Miglustat + Ketogene-Diät-Kombinationstherapie für infantile/juvenile Gangliosidosen (Syner-G-Studie) |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Rekrutierend | 21 | Langzeitsicherheit/-wirksamkeit von Nizubaglustat bei GM2-Gangliosidose/NPC-Patienten, einschließlich derjenigen, die zuvor Miglustat erhielten |

**Anmerkung:** Zwei Studien (NCT03822013, NCT02030015) wurden beendet, und die beiden abgeschlossenen Phase-2/3-Studien waren PK-/Verträglichkeitsstudien statt wirksamkeitsgesteuerte RCTs — dies schwächt die Stärke der klinischen Studienevidenz trotz der Anzahl der Studien.

---

## Literaturbelege

| PMID | Jahr | Typ | Journal | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genet Med | 12-Monats-randomisierte kontrollierte Studie (+24-Monats-Erweiterung) zur Bewertung von Sicherheit/Wirksamkeit von Miglustat bei spätmanifestierender Tay-Sachs-Krankheit |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematische Übersicht | Eur J Neurol | Systematische Übersicht findet frühere Studien zur Wirksamkeit/Sicherheit von Miglustat bei GM2-Gangliosidose **inkonsistent** |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Übersichtsartikel | Int J Mol Sci | Übersicht über klinische Merkmale, Pathophysiologie und aktuelle Therapien von GM2-Gangliosidose, einschließlich SRT |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Übersichtsartikel | Expert Rev Endocrinol Metab | Substratreduktionstherapie mit Miglustat bei Glykosphingolipid-Speicherkrankheiten, die das Gehirn betreffen |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Übersichtsartikel (Medikamentenprofil) | Curr Opin Investig Drugs | Bestätigt EU-Zulassung von Miglustat für Gaucher-Krankheit und seine Entwicklung für Tay-Sachs-, Fabry- und NPC-Krankheiten |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Übersichtsartikel | Front Physiol | Übersicht über neue therapeutische Ansätze zur Tay-Sachs-Krankheit, einschließlich Substratreduktionstherapie |
| [11227045](https://pubmed.ncbi.nlm.nih.gov/11227045/) | 2001 | Übersichtsartikel | Expert Opin Investig Drugs | Frühe Übersicht zur Begründung der Substratreduktionstherapie bei Glykosphingolipid-Speicherkrankheiten |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Pilotstudie | J Inherit Metab Dis | Neurokongnitive Testpilotstudie bei spätmanifestierender Tay-Sachs-Krankheit als potenzielles Endpunkt-Messinstrument |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Fallbericht | Neurology | SRT mit Miglustat bei 2 infantilen Tay-Sachs-Patienten: **konnte neurologische Verschlechterung nicht aufhalten**, obwohl CSF-Medikamentenspiegel und Makrozephalus-Prävention beobachtet wurden |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Beobachtungsstudie | Mol Genet Metab | Natürliche Verlaufskartierung der infantilen Gangliosidose; vermerkt, dass die Miglustat-Anwendung durch GI-Nebenwirkungen begrenzt ist |

---

## Marktinformationen für Deutschland

Miglustat ist derzeit **nicht vermarktet** in dieser Gerichtsbarkeit (`market_status: Not marketed`) und keine Genehmigungsdatensätze sind in diesem Evidenzpaket vorhanden (`total_licenses: 0`). Es kann keine Produkt-/Genehmigungstabelle erstellt werden.

---

## Sicherheitsaspekte

Weitere Sicherheitsinformationen finden Sie in der Gebrauchsinformation.

⚠️ **Kritische Datenlücke:** Ausführliche TFDA-Gebrauchsinformations-Warnhinweise und Kontraindikationen (DG001) sind als **Blocking** Lücke in diesem Evidenzpaket markiert, das bedeutet, dieser Kandidat **kann noch nicht zu S1-Sicherheits-Vorab-Bewertung voranschreiten**. Bekannte Sicherheitsprobleme mit Miglustat aus seiner zugelassenen Anwendung bei Gaucher/NPC umfassen Magen-Darm-Nebenwirkungen (Durchfall, Gewichtsverlust) und periphere Neuropathie, aber diese stammen nicht aus den strukturierten Sicherheitsfeldern dieses Pakets und sollten vor klinischer Anwendung unabhängig überprüft werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Obwohl Miglustat eine mechanistisch fundierte Begründung und einen ungewöhnlich umfangreichen Studien-/Literatur-Datensatz im Vergleich zu anderen Kandidaten in diesem Paket hat, ist die Evidenz gemischt — zwei Studien wurden beendet, die einzige RCT und die systematische Übersicht von 2023 berichten von inkonsistenter Wirksamkeit, und eine abgeschlossene Fallserie fand keine Unterbrechung neurologischer Verschlechterung bei infantiler Tay-Sachs-Krankheit. In Kombination mit einer **Blocking** Datenlücke zur TFDA-Sicherheitskennzeichnung ist der Kandidat noch nicht bereit zum Fortschritt.

**Um voranzuschreiten, ist Folgendes erforderlich:**
- DG001 auflösen: TFDA/amtliche Gebrauchsinformations-Warnhinweise und Kontraindikationen einholen
- DG002 auflösen: bestätigten DrugBank-Wirkmechanismus-Datensatz einholen (derzeit nur aus Literatur abgeleitet)
- Unabhängige Wirksamkeitsbewertung, die die Befunde der 2023-Systematischen Übersicht „inkonsistent" mit den positiven Erweiterungsdaten der 2009-RCT abstimmt
- Root-Cause-Überprüfung, warum NCT03822013 und NCT02030015 beendet wurden (Sicherheit vs. Einschluss vs. Futilität)
- Regulatorischer Pathway-Bewertung angesichts der Tatsache, dass das Medikament derzeit in dieser Gerichtsbarkeit nicht vermarktet ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

