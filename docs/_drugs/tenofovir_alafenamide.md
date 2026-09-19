---
layout: default
title: Tenofovir Alafenamide
parent: Nur Modellvorhersage (L5)
nav_order: 388
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Tenofovir Alafenamid (TAF): Von der antiretroviralen Therapie zur Felinen Immunodefizienzkrankheit

## Zusammenfassung in einem Satz

> Tenofovir Alafenamid ist ein Nukleotid-Reverse-Transkriptase-Inhibitor (NRTI), der zur Behandlung von HIV-1-Infektionen und chronischer Hepatitis B verwendet wird (basierend auf dem Wirkmechanismus, der im Text der Modellbegründung beschrieben ist; es sind jedoch keine formalen Taiwan-Lizenzdaten verfügbar).
> Die Top-Vorhersage des TxGNN-Modells ist **Feline Immunodefizienzkrankheit** – eine veterinärmedizinische (Katzen-)Krankheit – mit **null klinischen Studien und null Literatur**, die sie derzeit stützen.
> Ein zweiter Kandidat, **Simian-Immunodefizienzvirus (SIV)-Infektion**, verfügt über 1 gering relevante Studie und 9 präklinische Makaken-Studien, diese belegen aber TAFs *bereits bekannten* HIV-Prä-Expositions-Prophylaxe (PrEP)-Mechanismus und keine wirklich neue menschliche Indikation.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar aus Taiwan-Lizenzdaten (0 Lizenzen vorhanden); basierend auf dem eigenen Begründungstext des Modells ist TAF ein bekannter NRTI für HIV-1 / chronische Hepatitis B |
| Vorhergesagte neue Indikation | Feline Immunodefizienzkrankheit (Rang 1) |
| TxGNN-Vorhersagepunktzahl | 99,89% |
| Evidenzlevel | L5 (nur Modellvorhersage – keine klinischen Studien oder Literatur an diesen Kandidaten gebunden) |
| Marktstatus in Taiwan | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage vernünftig?

Detaillierte Wirkmechanismus-Daten sind als Datenlücke (DG002) in diesem Dossier gekennzeichnet. Basierend auf dem Begründungstext, der den anderen beiden Kandidaten in diesem Dossier beigefügt ist, wird verstanden, dass TAF als NRTI wirkt, der die retroviralen (und HBV) Reverse-Transkriptase/Polymerase hemmt – dies ist standardisierte, gut etablierte Pharmakologie, keine neuen Informationen, die für diesen Bericht generiert wurden.

Die Top-Vorhersage, **Feline Immunodefizienzkrankheit**, wird durch das Feline Immunodefizienzvirus (FIV) verursacht – ein Lentivirus, das mit HIV/SIV verwandt ist, aber sich davon unterscheidet. Eine gemeinsame Lentivirus-Familie könnte plausibel erklären, warum der Wissensgraph TAF mit dieser Krankheit verband (Reverse-Transkriptase-Inhibitoren haben in der Literatur generell bei einigen Cross-Lentivirus-Aktivitäten in vitro gezeigt). Dieses Dossier enthält jedoch **keine klinischen Studien, keine Literatur und keine abgeschlossene Bewertung** (`decision_stage: pending`) für diesen Kandidaten – die mechanistische Plausibilität oben ist Schlussfolgerung, nicht im Dossier bereitgestellte Evidenz.

Der besser dokumentierte Kandidat ist Rang 2, **SIV-Infektion**: SIV und HIV-1 sind beide Lentiviren mit hochgradig homologer Reverse-Transkriptase, und TAF/Tenofovir-Diphosphat hemmt direkt SIV-RT – dies ist das tatsächliche Primaten-Modell ohne Menschen, das während des eigenen HIV-PrEP-Entwicklungsprogramms von TAF verwendet wurde, reproduziert über 9 unabhängige Makaken-Studien. Die eigene Begründung des Dossiers ist explizit, dass **SIV-Infektion selbst keine menschliche Krankheit ist** und diese Evidenz wirklich TAFs *bestehende* HIV-PrEP-Indikation stützt, statt eine neue Indikation. Rang 3 (eine seltene monogene neurodevelopmentale Störung) ist direkt im Dossier als mechanistisch implausibel und möglicherweise durch TAFs bekanntes mitochondriales Toxizitätsprofil widersprochen gekennzeichnet – es sollte als Rauschen, nicht als Lead behandelt werden.

---

## Evidenz aus klinischen Studien

**Für die Top-Vorhersage (Feline Immunodefizienzkrankheit):** Derzeit keine damit verbundenen klinischen Studien registriert.

*Zusätzlicher Kontext – Studie, die dem Rang-2-Kandidat (SIV-Infektion) gebunden ist, zur Transparenz enthalten, aber als gering relevant bewertet:*

| Studiennummer | Phase | Status | Einschluss | Wichtigste Befunde |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unbekannt | 12 | Untersucht Vedolizumab + ART für HIV-virologische Remission; TAF ist nicht das Studienmedikament und dies ist eine menschliche HIV (nicht SIV) Studie. Relevanzgrad **C** – als wahrscheinlich falsch verknüpfte Studie gekennzeichnet. |

---

## Evidenz aus der Literatur

**Für die Top-Vorhersage (Feline Immunodefizienzkrankheit):** Derzeit keine damit verbundene Literatur verfügbar.

*Zusätzlicher Kontext – präklinische Literatur, die dem Rang-2-Kandidat (SIV-Infektion) gebunden ist; alle sind präklinische Tiermodellstudien (Makaken/Maus) (Tier 3), keine klinischen Humandaten:*

| PMID | Jahr | Typ | Journal | Wichtigste Befunde |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Präklinisch (Makake) | Nature Communications | Orale FTC/TAF + langwirksame Cabotegravir/Rilpivirine erreicht SHIV-Remission bei früh behandelten Makaken |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Präklinisch (Makake) | J Infect Dis | TAF/Elvitegravir-Vaginaleinlagen bieten erweiterten Post-Expositions-Schutz gegen SHIV |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Präklinisch (humanisierte Maus) | Frontiers in Immunology | Doppel-Mausmodell zum Testen antiviraler Strategien gegen SIV und HIV |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Präklinisch (Makake, Device) | J Antimicrob Chemother | Biologisch abbaubares TAF-Implantat schützt Makaken vor vaginaler SHIV-Infektion |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Präklinisch (Makaken-PrEP) | J Infect Dis | Orale TAF/FTC oder TAF allein verhindern vaginale SHIV-Infektion bei Makaken |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Präklinisch (Methodik) | PLoS One | Protokoll für tägliche orale ARV-Dosierungstreue in Makaken-SIV/SHIV-Modellen |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Präklinisch (Makaken-PrEP) | J Infect Dis | Orale FTC/TAF-Chemoprophylaxe schützt Makaken vor rektaler SHIV-Infektion |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Präklinisch (Makake) | J Infect Dis | Orale PrEP reduziert Entzündung/CD4-Verlust bei akuter SHIV-Durchbruchinfektion |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Präklinisch (Primatenmakake) | J Acquir Immune Defic Syndr | Orale Tenofovir-DF / topisches GS-7340 schützen Primatenmakaken vor oraler SIV-Exposition |

---

## Marktinformationen zu Taiwan

Nicht vermarktet in Taiwan (`market_status: Not marketed`, 0 Genehmigungen vorhanden). Es sind keine Lizenzdatensätze verfügbar, um diese zusammenzufassen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Wichtigste Warnungen, Kontraindikationen und Daten zu Arzneimittelwechselwirkungen sind alle derzeit in diesem Dossier nicht verfügbar – die DDI-Abfrage ergab keine Ergebnisse.)

**Hinweis:** DG001 (TFDA-Etikettwarnungen/Kontraindikationen) ist als **blockierende** Datenlücke gekennzeichnet – sein Fehlen bedeutet, dass dieser Kandidat noch nicht in eine formale S1-Sicherheits-Vorbewertung eintreten kann.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Top-Vorhersage (Feline AIDS) hat eine hohe TxGNN-Punktzahl, aber null unterstützende Studien oder Literatur und unvollständige Bewertung (L5, nur Modellvorhersage). Der am besten evidenzgestützte Kandidat (SIV-Infektion) ist explizit ein Tiermodell, das TAFs *bereits genehmigten* HIV-PrEP-Mechanismus reproduziert, statt eine neue menschliche Indikation darzustellen, und seine eigene Begründung empfiehlt Halten. Der dritte Kandidat ist durch das eigene Verfahren des Modells als mechanistisch implausibel gekennzeichnet. Darüber hinaus verhindert eine **blockierende** Datenlücke (TFDA-Etikett nicht verfügbar) eine formale S1-Sicherheits-Vorbewertung, und TAF ist derzeit nicht in Taiwan vermarktet.

**Um fortzufahren, ist Folgendes erforderlich:**
- Beheben Sie DG001: Beschaffen Sie TFDA-Etikett (Warnungen/Kontraindikationen) vor jeder S1-Sicherheits-Vorbewertung
- Beheben Sie DG002: Beschaffen Sie DrugBank-MOA-Daten, um mechanistische Plausibilität richtig zu bewerten
- Fordern Sie von TxGNN Neuordnung/Filterung an, um Ontologie-Begriffe, die nicht der menschlichen Krankheit entsprechen (z. B. Feline/Veterinär-MONDO oder Einträge, die nur Tiermodelle sind) aus der Kandidatenliste auszuschließen
- Wenn SIV/PrEP-bezogene Umnutzung von Interesse ist, reformulieren Sie den Kandidaten als „TAF für menschliche HIV-PrEP" (eine bereits etablierte Indikation) statt „SIV-Infektion" als neues Ziel

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

