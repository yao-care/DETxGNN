---
layout: default
title: Fluoxetine
parent: Nur Modellvorhersage (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluoxetine: vorhergesagte neue Indikation Phobische Störung (höchstbewertete Vorhersage im Datensatz: schizotyp… (Evidenzstufe L5). Ursprüngliche Indikation: Angststörung, neurotische Störung, dysthy…"
monitor_inn: "FLUOXETINE"
predicted_indications: ["schizotypal personality disorder", "paranoid personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "benign paroxysmal torticollis of infancy", "agoraphobia", "manic bipolar affective disorder", "phobic disorder", "Ohdo syndrome and variants", "melancholia"]
---

# Fluoxetine
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

# Fluoxetin: Von Depression und Angststörungen zu Phobischen Störungen

## Zusammenfassung

Fluoxetin ist ein selektiver Serotonin-Wiederaufnahmehemmer (SSRI), der ursprünglich zur Behandlung von Depressionen, Zwangsstörungen, Bulimia nervosa und weiteren psychischen Erkrankungen eingesetzt wird.
Das TxGNN-Modell sagt voraus, dass er bei **phobischen Störungen** wirksam sein könnte (weitere hoch bewertete Kandidaten: Agoraphobie, manische bipolare Störung, Melancholie).
Für die Hauptvorhersage liegen **2 klinische Studien** und **19 Publikationen** vor.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Angststörung, neurotische Störung, dysthyme Störung, bipolare Störung, unipolare Depression, endogene Depression, Major Depression, Bulimia nervosa, Zwangsstörung (laut Wissensgraph; keine Zulassungstexte verfügbar) |
| Vorhergesagte neue Indikation | Phobische Störung (höchstbewertete Vorhersage im Datensatz: schizotype Persönlichkeitsstörung; dort jedoch nur L3-Evidenz – siehe unten) |
| TxGNN-Vorhersagewert | 99,63 % (phobische Störung); 99,92 % (schizotype Persönlichkeitsstörung) |
| Evidenzlevel | L1 (phobische Störung) |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (aufgehoben) |
| Empfohlene Entscheidung | Proceed with Guardrails (Mit Auflagen fortfahren) |

**Hinweis zur Auswahl:** Die Rangfolge nach TxGNN-Score führt schizotype, paranoide, schizoide und histrionische Persönlichkeitsstörung an. Für diese ist die Evidenz jedoch schwach (L3–L5, keine Studien). Für diesen Bericht wird daher die Indikation mit der stärksten Evidenzlage, die **phobische Störung**, als Schwerpunkt herangezogen.

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Fluoxetin als SSRI die Wiederaufnahme von Serotonin hemmt. Seine Wirksamkeit bei Depression, Zwangsstörung und Angststörungen ist belegt, und mechanistisch kann es auch bei phobischen Störungen anwendbar sein.

SSRI gelten als Erstlinientherapie bei sozialer Angststörung und verwandten phobischen Zuständen. Der vermutete Wirkweg ist die serotonerge Modulation der Amygdala-präfrontalen Furchtschaltkreise. Die ursprünglichen Indikationen (Angststörung, Zwangsstörung, Depression) und die phobische Störung teilen dabei ein gemeinsames serotonerges Krankheitsmodell. Teile der Evidenz sind allerdings auf Klassenebene (SSRI allgemein) und nicht fluoxetinspezifisch.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Zentrale Ergebnisse |
|---------|------|------|------|---------|
| [NCT00043537](https://clinicaltrials.gov/study/NCT00043537) | Phase 3 | Abgeschlossen | 139 | Langzeitvergleich von Verhaltenstherapie, Fluoxetin und Placebo bei sozialer Phobie im Kindes- und Jugendalter |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | Nicht zutreffend | Unbekannt | 8.800 | Metaanalyse mit Einzelpatientendaten zur Wirksamkeit von Antidepressiva bei Angststörungen in Abhängigkeit vom Ausgangsschweregrad |

Für weitere Kandidaten (Auswahl):
| Studiennummer | Indikation | Phase | Status | Teilnehmerzahl | Zentrale Ergebnisse |
|---|---|---|---|---|---|
| [NCT00961961](https://clinicaltrials.gov/study/NCT00961961) | Bipolare Störung | Phase 4 | Abgeschlossen | 177 | Antidepressivum plus Stimmungsstabilisator vs. Stabilisator allein zur Rückfallprävention bei bipolarer Depression |
| [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) | Melancholie/Major Depression | Phase 4 | Abgeschlossen | 53 | Behandlungseffekte auf Entscheidungsverhalten bei Major Depression |

---

## Literaturevidenz (phobische Störung)

| PMID | Jahr | Typ | Zeitschrift | Zentrale Ergebnisse |
|------|-----|------|------|---------|
| [15466674](https://pubmed.ncbi.nlm.nih.gov/15466674/) | 2004 | Kontrollierte Studie | Arch Gen Psychiatry | Fluoxetin, kognitive Verhaltenstherapie und Placebo bei generalisierter sozialer Phobie |
| [9812120](https://pubmed.ncbi.nlm.nih.gov/9812120/) | 1998 | RCT | Am J Psychiatry | Fluoxetin vs. Placebo bei Panikstörung; Beitrag einzelner Symptome zur Gesamtbesserung |
| [24845944](https://pubmed.ncbi.nlm.nih.gov/24845944/) | 2014 | Metaanalyse | Expert Opin Drug Saf | Wirksamkeit von Antidepressiva bei Angststörungen (ohne Zwang) im Kindes- und Jugendalter |
| [16714326](https://pubmed.ncbi.nlm.nih.gov/16714326/) | 2007 | Metaanalyse | J Psychopharmacol | Wirksamkeit von SSRI bei sozialer Angststörung in doppelblinden, placebokontrollierten Studien |
| [36519357](https://pubmed.ncbi.nlm.nih.gov/36519357/) | 2023 | Übersichtsarbeit | Expert Opin Pharmacother | Aktueller Überblick zur Pharmakotherapie der sozialen Angststörung; SSRI/SNRI als Erstlinie |
| [17092192](https://pubmed.ncbi.nlm.nih.gov/17092192/) | 2006 | Übersichtsarbeit | J Clin Psychiatry | Evidenz zur Pharmakotherapie der sozialen Angststörung; Fluoxetin gehört zu den wirksamen SSRI |
| [11588653](https://pubmed.ncbi.nlm.nih.gov/11588653/) | 2001 | Übersichtsarbeit | Arq Neuropsiquiatr | Antidepressiva bei sozialer Angststörung |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Übersichtsarbeit | Int Clin Psychopharmacol | SSRI (inkl. Fluoxetin) bei Panikstörung und Agoraphobie placebo-überlegen |
| [9192539](https://pubmed.ncbi.nlm.nih.gov/9192539/) | 1997 | Offene Pilotstudie | J Child Adolesc Psychopharmacol | Fluoxetin bei gemischten Angststörungen bei Kindern und Jugendlichen |
| [12502021](https://pubmed.ncbi.nlm.nih.gov/12502021/) | 2002 | Retrospektive Analyse | Prog Neuropsychopharmacol Biol Psychiatry | Hyperhidrose bei sozialer Angststörung in Studien u. a. mit Fluoxetin |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/V/C/000133 | Reconcile | – | – (Status: aufgehoben) |

Das Produkt ist eine zentral (EMA) registrierte Zulassung mit dem Status „aufgehoben". Aktuell gibt es in den zusammengestellten Daten keine gültige Zulassung in Deutschland.

---

## Sicherheitsaspekte

- **Kontraindikationen/Risikokonstellationen (aus dem Wissensgraphen, nicht aus Fachinformationstexten):** u. a. Epilepsie, bipolare Störung, Leberinsuffizienz und Leberzirrhose, Diabetes mellitus und diabetische Ketoazidose, Neutropenie/Agranulozytose, Blutgerinnungsstörungen, benigne Prostatahyperplasie, orthostatische Hypotonie, Schlaganfall und zerebrovaskuläre Erkrankungen, Myokardinfarkt, Hyperlipidämie und Adipositas.
- **Arzneimittelwechselwirkungen (100 Einträge insgesamt, Auswahl):**
  - *Schwerwiegend (Major):* Bupropion, Lorcaserin, Diethylpropion, Dolasetron, Eliglustat, Palonosetron, Cisaprid
  - *Moderat:* u. a. Acetylsalicylsäure, Morphin, Clarithromycin, Famotidin, Loperamid, Chlorpropamid
- **Indikationsspezifische Warnhinweise:**
  - Bipolare Störung: Risiko des Umschlagens in die Manie bei Antidepressiva-Monotherapie; Kombination mit Stimmungsstabilisator und Überwachung nötig.
  - Kinder und Jugendliche: Überwachung auf Suizidalität.
  - Schizotype Persönlichkeitsstörung: Fallbericht über transiente Psychose mit psychogener Polydipsie unter Fluoxetin.
  - Weitere Literatur beschreibt Absetzsymptome, Überdosierung und Interaktion mit Imipramin.

Die vollständigen Warnhinweise und Gegenanzeigen der Fachinformation lagen nicht vor; bitte die Packungsbeilage bzw. Fachinformation konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails (Mit Auflagen fortfahren)**

**Begründung:**
- Für phobische Störungen (Evidenzlevel L1) liegen eine abgeschlossene Phase-3-Studie sowie mehrere Metaanalysen und Übersichtsarbeiten zu SSRI vor; Fluoxetin ist zudem in der Nähe bereits etablierter Anwendungen (Angststörungen) angesiedelt. Ein Teil der Evidenz gilt aber nur auf SSRI-Klassenebene.
- Einordnung der übrigen Kandidaten: Agoraphobie (L2, ebenfalls mit Auflagen), Melancholie (L1, im Wesentlichen bestehende Anwendung bei Major Depression), manische bipolare Störung (L2, Forschungsfrage – Fluoxetin wirkt auf die depressive Phase, nicht auf Manie). Die Persönlichkeitsstörungen (schizotyp L3; paranoid, schizoid L4; histrionisch L5) sowie benigner paroxysmaler Torticollis des Säuglingsalters und Ohdo-Syndrom (jeweils L5) sind zurückzustellen (Hold).

**Für das weitere Vorgehen erforderlich:**
- Detaillierte Wirkmechanismus-Daten (MOA)
- Fachinformation von BfArM/EMA zu Warnhinweisen und Gegenanzeigen (derzeit blockierende Datenlücke für die Sicherheitsprüfung)
- Fluoxetinspezifische Ergebnisse der Studien NCT00043537 und NCT02476136 (Studienarm, Endpunkte, Effektstärken)
- Klärung der aktuellen Zulassungslage in Deutschland (derzeit nur erloschene Zulassung)
- Sicherheitsüberwachungsplan (Suizidalität bei Jugendlichen, Umschlagrisiko bei bipolarer Störung, relevante Wechselwirkungen)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

