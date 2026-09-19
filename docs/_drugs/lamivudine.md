---
layout: default
title: Lamivudine
parent: Nur Modellvorhersage (L5)
nav_order: 220
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Lamivudin: Von antiretroviraler Therapie (HIV/chronische Hepatitis B) zum felinen erworbenen Immunmangelsyndrom (menschliche Anwendbarkeit fraglich)

## Ein-Satz-Zusammenfassung

Lamivudin (3TC) ist ein Nukleosid-Reverse-Transkriptase-Inhibitor (NRTI), und die Literatur sowie klinische Studiendaten zeigen, dass es international bereits zur antiviralen Behandlung von HIV-1-Infektionen und chronischer Hepatitis B eingesetzt wird. Die vom TxGNN-Modell mit Rang eins vorhergesagte Indikation ist das **feline erworbene Immunmangelsyndrom (feline AIDS, FIV-Infektion)**, wobei es sich um eine **tierärztliche Krankheit, keine menschliche Indikation** handelt, die nicht in die Arzneimittelrepurposing-Pipeline für den Menschen gehört; die Gesamtevidenz für diesen Kandidaten ist qualitativ schwach, und fünf vorhergesagte Indikationen weisen zahlreiche Fälle von Spezies-Mismatch oder fehlerhafte Krankheitskennzeichnungen auf, weshalb ein **Hold** empfohlen wird.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Keine lokalen Zulassungsdaten; international bekannt für die Verwendung bei HIV-1-Infektion und chronischer Hepatitis B (NRTI-Hintergrundtherapie, basierend auf textuellem Beweis abgeleitet) |
| Vorhergesagte neue Indikation | Feline acquired immunodeficiency syndrome (felini erworbenes Immunmangelsyndrom, nicht-menschliche Krankheit) |
| TxGNN-Vorhersagescore | 99.93% (0.9992823) |
| Evidenzklasse | L4 (präklinische/mechanistische Studien, hochgradig zweifelhaft) |
| Marktstatus in Taiwan | Not marketed |
| Anzahl genehmigter Lizenzen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum diese Vorhersage rational ist (und Bedenken aufweist)

Derzeit fehlen vollständige DrugBank-Wirkmechanismus-Daten (DG002, High severity). Basierend auf dem Inhalt der Beweispackage ist Lamivudin ein NRTI-Arzneimittel, dessen menschliche Indikationen sich auf die Kombinationstherapie von HIV-1-Infektionen und chronischer Hepatitis B konzentrieren, mit dem Wirkmechanismus der Hemmung der viralen Reverse-Transkriptase.

Die Indikation mit Rang eins lautet jedoch „feline acquired immunodeficiency syndrome", also die **FIV-Infektion (feline immunodeficiency virus) bei Feliden**, eine tierärztliche Indikation. Obwohl FIV und HIV beide zu den Lentiviren gehören und ähnliche Reverse-Transkriptase-Mechanismen aufweisen, was bedeutet, dass Lamivudin theoretisch in vitro eine FIV-hemmende Wirkung hat, ist dies keine menschliche Krankheit und **sollte nicht in die Arzneimittelrepurposing-Pipeline für den Menschen aufgenommen werden**. Dieser Punkt wurde auch in der `repurposing_rationale.mechanistic_link` der Beweispackage eindeutig gekennzeichnet.

Darüber hinaus zeigen die übrigen vier vorhergesagten Indikationen dieses Kandidaten ebenfalls systematische Probleme:
- **Rang 2 (SIV-Infektion)**: Primatenvirus-Modell, keine klinischen Studien, nur Tierstudien, präklinisches Signal (L5).
- **Rang 3 (Neuronale Entwicklungsstörung)**: Keine Literatur- oder Studienunterstützung, reine Modellhypothese (L5).
- **Rang 4 (Familiäre gemischte Hyperlipoproteinämie)**: Der Wirkmechanismus läuft der bekannten Pharmakologie entgegen (NRTIs sind bekannt dafür, Lipidabnormalitäten zu induzieren, nicht zu behandeln), verdächtiger Modellkodierungsfehler.
- **Rang 5 (chronische Hepatitis C)**: Die aufgeführten Studien und Literatur beziehen sich tatsächlich hauptsächlich auf Forschungen zur chronischen Hepatitis B (HBV, hat Reverse-Transkriptionsschritt), nicht zur HCV (keine Reverse-Transkriptase), was einen systemischen Fehler bei der Datenkennzeichnung darstellt.

Insgesamt ist die Signalqualität des Wissensgraphen für diesen Kandidaten niedrig, und es wird empfohlen, eine Neubewertung nach Datenkorrektur durchzuführen.

---

## Klinische Studiendaten

Die folgenden Studien stammen aus dem Evidenzbestand von Rang 1 (feline AIDS), sind aber **alle klinische HIV-1-Studien beim Menschen, ohne Bezug zur felinen Krankheit** (Relevanzbewertung C), und wurden nur wegen gemeinsamen Lamivudin-Auftretens fehlerhaft verknüpft:

| Studienkennziffer | Phase | Status | Rekrutierungszahl | Wichtigste Erkenntnisse |
|------------------|-------|--------|------------------|----------------------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | DTG+abacavir/lamivudine vs. Atripla, HIV-1-Erstlinien-Studie beim Menschen, kein Bezug zu FIV |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | DTG+ABC/3TC CNS/Plasma-PK-Studie, HIV-1 beim Menschen, keine Tierstudie |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Darunavir+lamivudine vs. Vergleichsschemata, HIV-1-Erstlinien-Patienten beim Menschen |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | DTG vs. Raltegravir (+ ABC/3TC oder TDF/FTC), HIV-1-Erstlinien-Patienten beim Menschen |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | DTG-Dosisauswahlstudie (+ ABC/3TC oder TDF/FTC), HIV-1-Erstlinien-Patienten beim Menschen |

> ⚠️ Alle oben genannten Studien haben keine direkte Relevanz für die FIV-Infektion bei Feliden und unterstützen nicht die vorhergesagte Indikation.

---

## Literaturbeweise

Die folgende Literatur befasst sich zwar mit der FIV-Infektion bei Feliden (tierärztliches Feld) und ist konsistent mit der Indikation Rang 1, gehört aber zu **Tierstudien** und ist nicht auf die menschliche Arzneimittelzulassungsbewertung anwendbar:

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|------|-----|--------|----------------------|
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro (tierärztlich) | Am J Vet Res | Vergleich der in-vitro-Replikationsdynamik zwischen FIV-Isolaten und 3TC-resistenten Stämmen |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Review | Vet Immunol Immunopathol | Bewertung der Wirksamkeit von AZT/3TC-Kombination bei FIV-Infektion/Immunopathologie |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Kohortenstudie (tierärztlich) | J Feline Med Surg | Langzeitverfolgung antiretroviraler Behandlung bei FIV-infizierten Katzen |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Kohortenstudie (tierärztlich) | Viruses | Bewertung verschiedener antiretroviraler Schemata bei asymptomatischen später-Stadium-FIV-Katzen |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Fallserie (tierärztlich) | Antiviral Res | Hemmwirkung der ZDV+3TC+ABC-Kombination auf die FIV-Replikation in vitro |

---

## Marktstatus in Taiwan

Dieses Arzneimittel ist auf dem taiwanesischen Markt (lokaler Markt) **Not marketed, keine genehmigten Lizenzdaten vorhanden** (`total_licenses = 0`). Es können keine Darreichungsform, Produktname oder genehmigte Indikationstexte bereitgestellt werden. Dies ist eine Datenlücke (DG001, Blocking severity), die durch die Analyse von BfArM-Website-Dokumenten ergänzt werden muss.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Gebrauchsinformation/das Informationsblatt des Arzneimittels für vollständige Sicherheitsinformationen.

> Derzeit sind `key_warnings` und `contraindications` beide als Datenlücke gekennzeichnet, und die DDI-Abfrageergebnisse sind `not_found` (DG001, Blocking severity), sodass die S1-Sicherheitsinitialprüfung nicht abgeschlossen werden kann.

---

## Fazit und nachfolgende Empfehlungen

**Entscheidung: Hold**

**Gründe:**
Die fünf höchstrangigen vorhergesagten Indikationen dieses Kandidaten weisen alle Probleme mit der Evidenzqualität auf – die erste rangiert als nicht-menschliche (feline) Krankheit und ist nicht auf die Arzneimittelrepurposing-Pipeline für den Menschen anwendbar; die übrigen vier sind jeweils präklinische Tiermodell-Signale, modellgestützte Hypothesen ohne Beweise, Wirkmechanismus-Richtungskonflikte sowie systematische Fehler bei der Krankheitskennzeichnung (HBV-Studien werden fälschlicherweise als HCV gekennzeichnet). Gleichzeitig fehlen lokale TFDA-Sicherheitsdaten (Blocking severity), Cannot proceed to S1 safety screening.

**Zur Fortsetzung sind erforderlich:**
- Ergänzung von TFDA-Gebrauchsinformation Warnhinweisen/Kontraindikationen (DG001, durch BfArM-Website-PDF-Analyse)
- Ergänzung von DrugBank-Wirkmechanismus-Daten (MOA) (DG002, über DrugBank-API-Abfrage)
- Korrektur des Spezies-Mismatch-Problems im Wissensgraphen (feline/simian-Krankheiten sollten nicht zusammen mit menschlichen Indikationskandidaten aufgeführt werden)
- Korrektur der Krankheitskennzeichnungsfehler bei Rang 5 (chronische Hepatitis C) und des Evidenz-Mismatch-Problems, Neukennzeichnung mit HBV-bezogenen Studien/Literatur
- Falls die Bewertung menschlicher HIV/HBV-unabhängiger neuer Indikationen angestrebt wird, wird empfohlen, das TxGNN-Team zu bitten, Nicht-Mensch-Art-Knoten auszuschließen und die Kandidatenliste neu zu generieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

