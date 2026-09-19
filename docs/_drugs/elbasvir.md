---
layout: default
title: Elbasvir
parent: Nur Modellvorhersage (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Elbasvir
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

# Elbasvir: Von Hepatitis-C-Virus-Infektion zu Hepatitis-B-Virus-Infektion

## Einzeilige Zusammenfassung

> Elbasvir ist ein NS5A-Replikationskomplex-Inhibitor, entwickelt als Bestandteil der Fixkombination Grazoprevir/Elbasvir (Zepatier), etabliert für chronische **Hepatitis-C-Virus-(HCV)-Infektion** Genotyp 1, 4 und 6 — obwohl dies aus Kontext von Studien und Literatur hergeleitet wird, da keine strukturierten Originaldaten zur Indikation zurückgeliefert wurden.
> Das TxGNN-Modell ordnet **Hepatitis-B-Virus-(HBV)-Infektion** als seine höchste Vorhersage für neue Indikationen ein, mit **13 klinischen Studien** und **18 Veröffentlichungen**, die als unterstützende Belege angehängt sind.
> Bei Überprüfung ist jedoch jede einzelne dieser Studien tatsächlich eine HCV-Studie oder HCV-fokussierte Veröffentlichung — keine betrifft HBV-Patienten oder HBV-virologische Endpunkte — daher unterstützen die Belege diese spezifische Vorhersage nicht.

---

## Kurzübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Chronische Hepatitis-C-Virus-(HCV)-Infektion Genotyp 1/4/6 (aus Kontext von Studien/Literatur hergeleitet; nicht im strukturierten Arzneimittelregister vorhanden) |
| Vorhergesagte neue Indikation | Hepatitis-B-Virus-Infektion |
| TxGNN-Vorhersage-Score | 99.71% |
| Evidenzlevel | L5 (nur Modellvorhersage, keine HBV-spezifische Studie) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aufschub |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten wurden für diesen Datensatz nicht zurückgeliefert. Basierend auf etablierter Pharmakologie ist Elbasvir ein Inhibitor des HCV-NS5A-Proteins, eines Nichtstrukturproteins, das einzigartig für die Gattung *Hepacivirus* (Familie *Flaviviridae*) ist. Es wird zusammen mit dem NS3/4A-Protease-Inhibitor Grazoprevir formuliert und wird ausschließlich für chronische HCV-Infektion Genotyp 1, 4 und 6 verwendet.

HBV ist dagegen ein Hepadnavirus — ein teilweise doppelsträngiges DNA-Virus, das sich durch Reverse Transkription eines RNA-Intermediats repliziert. Es hat kein NS5A-Homolog und keinen bekannten pharmakologischen Angriffspunkt, der HCV-NS5A-Inhibitoren gemeinsam ist. Die beiden Viren teilen nur die klinische Bezeichnung „virale Hepatitis", nicht einen gemeinsamen Replikationsmechanismus oder Arzneimittelziel.

Konsistent damit stellt die mechanistische Überprüfung des Evidenzpakets selbst fest, dass die HBV-Vorhersage höchstwahrscheinlich ein **TxGNN-Embedding-Artefakt** ist: weil HBV und HCV eng im Krankheits-Embedding-Raum zusammengruppieren (beide sind „virale Hepatitis"-Entitäten), präsentiert das Modell HCV-spezifische Studienbelege unter der HBV-Vorhersage, auch wenn keine davon HBV-Patienten oder -Endpunkte betreffen. Dies sollte als falsch positiv behandelt werden, bis es unabhängige mechanistische oder In-vitro-Signale gibt, die spezifisch für HBV sind.

---

## Evidenz aus klinischen Studien

Alle Studien unten wurden als „unterstützende Belege" für die HBV-Vorhersage abgerufen. Bei Inspektion studiert jede Studie tatsächlich HCV (Genotyp 1/4/6, mit oder ohne HIV-Koinfektion oder hepatische/renale Beeinträchtigung) — keine rekrutierte HBV-Patienten oder maß HBV-Ergebnisse.

| Studiennummer | Phase | Status | Einschlussanzahl | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Abgeschlossen | 87 | HCV-Eradikation und kardiovaskuläres Risiko bei HIV/HCV-Koinfektion — kein HBV-Arm |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Phase 2/3 | Abgeschlossen | 40 | Grazoprevir+Elbasvir bei HCV GT1/4/6 mit Child-Pugh-B-Leberinsuffizienz |
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Phase 2 | Abgeschlossen | 15 | Pembrolizumab bei HCV-positiven/negativen HCC — Elbasvir nicht das Studienarzneimittel |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Abgeschlossen | 573 | Grazoprevir+Elbasvir ± Ribavirin, chronisches HCV, SVR12-Endpunkt |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Abgeschlossen | 80 | Grazoprevir+Elbasvir bei akutem HCV Genotyp 1/4 |
| [NCT01932762](https://clinicaltrials.gov/study/NCT01932762) | Phase 2 | Abgeschlossen | 98 | Grazoprevir ± Elbasvir/Ribavirin bei HCV GT2/4/5/6, therapienaiv |
| [NCT01532973](https://clinicaltrials.gov/study/NCT01532973) | Phase 1 | Abgeschlossen | 48 | Elbasvir-Monotherapie PK/PD bei HCV-infizierten Männern |
| [NCT03797066](https://clinicaltrials.gov/study/NCT03797066) | Phase 4 | Beendet | 13 | Point-of-Care-HCV-Test-and-Treat mit Grazoprevir/Elbasvir in obdachloser Bevölkerung |
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Abgeschlossen | 413 | Grazoprevir+Uprifosbuvir mit Elbasvir oder Ruzasvir, HCV GT3/4/5/6 |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Abgeschlossen | 301 | Grazoprevir/Elbasvir bei HCV GT1/4/6-Patienten unter Opioid-Substitutionstherapie |

*Anmerkung: 3 weitere Studien im Evidenzpaket erhielten die Relevanzbeurteilung „C" (d.h., als nicht relevant für HBV eingestuft) und werden hier aus Gründen der Kürze weggelassen.*

---

## Evidenz aus der Literatur

Keine der 18 Veröffentlichungen, die dieser Vorhersage beigefügt sind, berichten eine HBV-spezifische Studie von Elbasvir. Zwei (unten markiert) behandeln HBV nur beiläufig, als Kontrast zu HCV.

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Übersichtsartikel | Liver International | „Richtung Ausrottung von HCV und eine Heilung für HBV" — diskutiert die beiden Viren als unterschiedliche Krankheitsentitäten, nicht einen gemeinsamen Arzneimittelmechanismus |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Querschnittstudie | Annals of Hepatology | Vergleicht HBV vs. HCV-Antiviral-Arzneimittelpreise — wirtschaftlich, nicht mechanistisch, Vergleich |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Übersichtsartikel | Acta Pharmaceutica Sinica B | Übersicht der direktwirkenden Anti-HCV-Mittel; bemerkt ausdrücklich, dass HCV heilbar ist, im Gegensatz zu HIV/HBV |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Phase 4-Studie | Antimicrobial Agents and Chemotherapy | Grazoprevir/Elbasvir bei HCV GT1b Leber-/Nierentransplantationsempfänger |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Grundlagenforschung | Hepatology | Evolution von HCV-Protease-Inhibitor-Resistenz-Varianten |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Reale-Welt-Studie | Journal of Viral Hepatitis | Elbasvir/Grazoprevir Leber- und Nierensicherheit bei taiwanesischen HCV-Patienten |
| [29077864](https://pubmed.ncbi.nlm.nih.gov/29077864/) | 2018 | RCT | Clinical Infectious Diseases | Sofosbuvir+Grazoprevir/Elbasvir-Retreatment von HCV GT1/4 nach vorherigem DAA-Versagen |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Übersichtsartikel | Klinická Mikrobiologie a Infekční Lékařství | Antivirale Behandlung von chronischem HBV **und** HCV bei Kindern — kombinierte Übersicht, keine HBV-spezifischen Elbasvir-Daten |
| [32306039](https://pubmed.ncbi.nlm.nih.gov/32306039/) | 2020 | Kohortenstudie | Journal of Antimicrobial Chemotherapy | Grazoprevir/Elbasvir für kürzlich erworbenes HCV GT1/4 bei MSM |
| [30049677](https://pubmed.ncbi.nlm.nih.gov/30049677/) | 2018 | Fallbericht | BMJ Case Reports | HCV-assoziierte Dermatomyositis-Fall; nicht bezogen auf HBV |

---

## Informationen zum deutschen Markt

Elbasvir hat derzeit **keine Zulassung auf dem deutschen Markt** — das Arzneimittelregister zeigt 0 Lizenzen und Marktstatus „Nicht vermarktet". Keine deutsche Produkttabelle kann aus diesem Evidenzpaket erstellt werden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Zwei strukturelle Datenlücken wurden in diesem Evidenzpaket gekennzeichnet, die eine vollständige Sicherheitsbewertung blockieren:

- **TFDA/BfArM-Kennzeichnungswarnungen und Kontraindikationen** — noch nicht abgerufen (blockierende Schweregrad; erforderlich, bevor dieser Kandidat die Sicherheits-Vorscreening betreten kann).
- **Wirkmechanismus-Detail** — noch nicht aus DrugBank abgerufen (hohe Schweregrad; erforderlich, um die mechanistische Plausibilität für eine neue Indikation angemessen zu bewerten).

Es wurden keine Arzneimittel-Wechselwirkungsdaten gefunden (Abfrage gab keine Ergebnisse zurück).

---

## Fazit und nächste Schritte

**Entscheidung: Aufschub**

**Begründung:**
Die HBV-Vorhersage trägt die eigene L5-Evidenzbewertung des Modells (nur Vorhersage, keine unterstützende Studie), und die manuelle Überprüfung bestätigt, dass alle 13 beigefügten Studien und 18 Veröffentlichungen HCV-spezifisch sind und keine HBV-Patienten oder -Endpunkte betreffen — was darauf hindeutet, dass das Signal höchstwahrscheinlich ein Krankheits-Embedding-Artefakt und nicht eine echte Umwidmungschance ist. Dies wird noch dadurch verschärft, dass Elbasvir keine Zulassung in Deutschland hat und eine blockierende Datenlücke bei den Kennzeichnungssicherheitsinformationen vorliegt, sodass es nicht voranschreiten kann, unabhängig von der Indikationsfrage.

**Zum Fortfahren ist folgendes erforderlich:**
- Bestätigte Arzneimittel-Kennzeichnung (TFDA/BfArM) Warnungen, Kontraindikationen und DDI-Profil
- DrugBank-beschaffter Wirkmechanismus-Bestätigung für Elbasvir
- Alle unabhängigen In-vitro- oder In-vivo-Belege für Elbasvir-Aktivität gegen HBV-Replikation (derzeit keine identifiziert)
- Falls keine HBV-spezifischen mechanistischen oder präklinischen Signale auftauchen, sollte dieser Kandidat zugunsten der anderen vorhergesagten Indikationen der Pipeline priorisiert werden, von denen keine (HEV, HAV, tierische Hepatitis, Omsk-Blutungsfieber, Kyasanur-Waldkrankheit, HIV, FIV, SIV oder die neurodevelopmentale Störung) derzeit eine unterstützende mechanistische Begründung haben — alle tragen die gleiche „Aufschub"-Empfehlung in diesem Evidenzpaket

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

