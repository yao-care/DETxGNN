---
layout: default
title: Agomelatine
parent: Nur Modellvorhersage (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: Von Major Depressive Disorder zu einem Multi-Indikations-Kandidaten-Portfolio

## Anmerkung zum Umfang

Dieses Evidence Pack (`TW-DB06594-multi`) ist eine **Multi-Indikations-Analyse** — TxGNN generierte 10 nach Rang geordnete Kandidaten-Indikationen für Agomelatine statt einer einzigen Top-Vorhersage. Die Anwendung der Standard-Single-Indikations-Vorlage nur auf Rang #1 (*benign paroxysmal torticollis of infancy*) wäre irreführend: Das Evidence Pack selbst klassifiziert diese Vorhersage als wahrscheinlich ein False-Positive des Knowledge-Graph. Dieser Bericht behandelt daher das gesamte Kandidaten-Portfolio, bohrt dann in die zwei Indikationen mit der stärksten Evidenzunterstützung.

---

## Zusammenfassung in einem Satz

Agomelatine ist ein melatonerges (MT1/MT2-Agonist) und serotonerges (5-HT2C-Antagonist) Antidepressivum mit **Major Depressive Disorder (MDD)** als etablierte Anwendung der Literatur (kein formaler regulatorischer Indikationstext war abrufbar — siehe Datenlücken unten). TxGNN identifizierte **10 Kandidaten-Indikationen**, aber nur **2 der 10** (Melancholie, neurotische Depression) erreichen ein hohes Evidenzniveau (**L1**), und beide sind im Wesentlichen Umformulierungen von Agomelatines bekannter antidepressiver Aktivität statt echter neuer Indikationen; die verbleibenden Kandidaten sind entweder schwach unterstützte psychiatrische Spektrum-Störungen (**L4**) oder nicht unterstützte seltene genetische Syndrome (**L5**), die das Evidence Pack selbst als Modellrauschen klassifiziert.

---

## Schnellübersicht

**Arznei-Ebenen-Fakten**

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Major Depressive Disorder (abgeleitet aus Literaturkontext, z.B. EMA-Zulassungsbewertung PMID 19777735; nicht vorhanden in formalen regulatorischen Daten — siehe Datenlücken) |
| Markt-Status in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Gesamtempfehlung | **Halten** (Portfolio-Ebene; siehe Tabelle pro Indikation) |

**Portfolio der vorhergesagten Indikationen (alle 10, nach TxGNN-Score geordnet)**

| Rang | Vorhergesagte Indikation | TxGNN-Score | Evidenzniveau | Entscheidungsstufe | Empfehlung |
|------|--------------------------|-------------|----------------|--------------------|------------|
| 1 | Benign paroxysmal torticollis of infancy | 99,96 % | L5 | S0 | Halten |
| 2 | Agoraphobia | 99,95 % | L4 | S1 | Forschungsfrage |
| 3 | Neurotic disorder | 99,90 % | L4 | S1 | Forschungsfrage |
| 4 | Melancholia | 99,88 % | L1 | S3 | Weitermachen mit Schutzmaßnahmen |
| 5 | Neurotic depression | 99,88 % | L1 | S3 | Weitermachen mit Schutzmaßnahmen |
| 6 | Ohdo syndrome and variants | 99,87 % | L5 | S0 | Halten |
| 7 | Dysthymic disorder | 99,86 % | L4 | S1 | Forschungsfrage |
| 8 | Ligneous conjunctivitis | 99,83 % | L5 | S0 | Halten |
| 9 | Blepharophimosis–intellectual disability syndrome, Ohdo type | 99,82 % | L5 | S0 | Halten |
| 10 | Keppen-Lubinsky syndrome | 99,81 % | L5 | S0 | Halten |

Anmerkung: TxGNN-Scores clustern eng (99,81–99,96 %) und verfolgen hier **nicht** die Evidenzqualität — mehrere der höchstbewerteten Kandidaten (Rang 1, 6, 8, 9, 10) haben Null klinische Studien, Null Literatur und keinen plausiblen mechanistischen Zusammenhang laut der Begründungstextoptik des Evidence Pack selbst.

---

## Warum sind diese Vorhersagen plausibel (oder nicht)?

Derzeit sind detaillierte Wirkmechanismus-Daten aus einer strukturierten Quelle (z.B. DrugBank-MOA-Feld) nicht verfügbar — dies wird als Datenlücke **DG002 (hohe Schwere)** protokolliert. Basierend auf der für dieses Pack überprüften Literatur wirkt Agomelatine als **MT1/MT2-melatonergischer Rezeptor-Agonist und 5-HT2C-serotonerger Rezeptor-Antagonist**, der gestörte zirkadiane Rhythmen resynchronisiert, langsames Schlafen verbessert und Dopamin-/Noradrenalin-Freisetzung im präfrontalen Kortex erhöht — Mechanismen, die durch seine genehmigte Anwendung bei Major Depressive Disorder etabliert sind.

Die 10 Kandidaten teilen sich in zwei eindeutig verschiedene Cluster:

- **Stimmungs-/Angst-Spektrum-Cluster** (Agoraphobia, Neurotic disorder, Melancholie, Neurotic depression, Dysthymic disorder): diese sind mechanistisch kohärent, da alle innerhalb oder angrenzend des depressiven/Angst-Spektrums fallen, wo Agomelatines monoaminerge und zirkadiane Mechanismen direkt anwendbar sind. Aber **Melancholie** und **Neurotic depression** sind klinische Subtypen/ältere nosologische Bezeichnungen für MDD selbst — die starke (L1) Evidenz dahinter spiegelt Agomelatines *bereits-etablierte* antidepressive Wirksamkeit wider, nicht ein echtes Repurposing-Signal. Die genuine unterschiedlichen Kandidaten in diesem Cluster — **Agoraphobia**, **Neurotic disorder**, **Dysthymic disorder** — erreichen nur L4, unterstützt durch indirekte, Klassen-Ebenen oder einzelne nicht-spezifische Studien statt agomelatine-spezifische Studien.
- **Seltene-genetische-Syndrom-Cluster** (Ohdo syndrome und seine Varianten ×2, Keppen-Lubinsky syndrome, ligneous conjunctivitis): diese haben Null klinische Studien, Null Literatur und keinen plausiblen Rezeptor-Ebenen-Zusammenhang zur melatonergischen/serotonergen Pharmakologie. Die Begründung des Evidence Pack selbst schreibt diese explizit Nähe-Artefakten im Knowledge Graph zu statt echtem biologischem Signal. Sie sollten als Rauschen behandelt werden, nicht als Kandidaten für weitere Arbeit.

---

## Klinische Studien-Evidenz

Über alle 10 vorhergesagten Indikationen hinweg sind **keine klinischen Studien registriert** auf ClinicalTrials.gov oder ICTRP (bestätigt durch 30 separate Null-Ergebnis-Abfragen im Abfrage-Protokoll, IDs 5, 8, 11, 14, 17, 20, 23, 26, 29, 32).

---

## Literatur-Evidenz

Literatur wurde pro Indikation abgefragt; Ergebnisse überlappen stark zwischen Melancholie und Neurotic depression (beide ordnen sich zur gleichen MDD-Literaturbasis). Unten sind die 10 relevantesten, deduplizierten Publikationen über das Portfolio hinweg, priorisiert nach Studien-Tier und Agomelatine-Spezifität.

| PMID | Jahr | Typ | Zeitschrift | Zugehörige Indikation(en) | Wichtigste Erkenntnisse |
|------|------|-----|-----------|-----------|----------|
| [39684343](https://pubmed.ncbi.nlm.nih.gov/39684343/) | 2024 | Systematische Übersicht/Metaanalyse (agomelatine-spezifisch) | Int J Mol Sci | Melancholie, Neurotic depression | Wirksamkeit und Sicherheit von Agomelatine bei depressiven Patienten mit komorbidem Diabetes |
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Netzwerk-Metaanalyse (21 Antidepressiva inkl. Agomelatine) | Lancet | Melancholie, Neurotic depression | Vergleichende Wirksamkeits-/Akzeptanz-Rangliste von Antidepressiva zur akuten MDD-Behandlung |
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Metaanalyse von placebokontrollierten RCTs | J Clin Psychiatry | Dysthymic disorder | Antidepressive Wirksamkeit bei Dysthymie vs. MDD, Klassen-Ebene (nicht agomelatine-spezifisch) |
| [32568567](https://pubmed.ncbi.nlm.nih.gov/32568567/) | 2020 | Übersicht (agomelatine-spezifisch) | Expert Opin Drug Discov | Melancholie, Neurotic depression | Präklinische Entdeckung und Entwicklung von Agomelatine; erstes Antidepressivum, das über monoamine Wege hinausgeht |
| [30759026](https://pubmed.ncbi.nlm.nih.gov/30759026/) | 2019 | Übersicht (agomelatine-spezifisch) | Expert Opin Pharmacother | Neurotic depression | Duale MT-Agonist-/5-HT2C-Antagonist-Wirkung von Agomelatine; Anwendung bei Depression komorbid mit somatischen Störungen |
| [19777735](https://pubmed.ncbi.nlm.nih.gov/19777735/) | 2009 | Übersicht (agomelatine-spezifisch) | Med Monatsschr Pharm | Melancholie | Berichtet EMA-Zulassung von Agomelatine (Valdoxan) für Erwachsenen-MDD, Februar 2009 |
| [26560173](https://pubmed.ncbi.nlm.nih.gov/26560173/) | 2015 | Cochrane Systematische Übersicht | Cochrane Database Syst Rev | Melancholie | Agomelatine und Melatonin bewertet für Prävention von Seasonal Affective Disorder |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematische Übersicht/Netzwerk-Metaanalyse | Mol Psychiatry | Melancholie, Neurotic depression | Antidepressive Wirksamkeit/Sicherheit in der Erhaltungsphase von MDD (Klassen-Ebene) |
| [25911132](https://pubmed.ncbi.nlm.nih.gov/25911132/) | 2015 | Systematische Übersicht | J Affect Disord | Melancholie, Neurotic depression | Evidenz-basierte Antidepressiva-Dosisäquivalenz-Empfehlungen aus RCTs |
| [21183900](https://pubmed.ncbi.nlm.nih.gov/21183900/) | 2010 | Kohorten-/Beobachtungsstudie | Zh Nevrol Psikhiatr Im S S Korsakova | Agoraphobia | Klinische Prädiktoren der therapeutischen Reaktion auf Agomelatine (Valdoxan) bei mittelschwerer bis schwerer Depression; nicht agoraphobia-spezifisch |

---

## Deutschland Markt-Informationen

Agomelatine wird derzeit **nicht vermarktet** in Deutschland laut verfügbarer regulatorischer Daten (`market_status: Not marketed`), mit **0 Zulassungen** auf Datensatz. Keine BfArM-Lizenzdetails waren für dieses Evidence Pack abrufbar.

---

## Sicherheitsüberlegungen

Bitte sehen Sie in der Packungsbeilage nach Sicherheitsinformationen. Keine strukturierten Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungs-Daten waren für dieses Evidence Pack abrufbar (DDI-Abfrage gab `not_found` zurück).

---

## Fazit und nächste Schritte

**Entscheidung: Halten** (Portfolio-Ebene)

**Begründung:**
- Die zwei höchstevidenz-Kandidaten (Melancholie, Neurotic depression; L1) sind keine echten Repurposing-Chancen — sie sind alternative klinische Labels für Agomelatines bereits-genehmigte Indikation (MDD), daher fügen sie begrenzte neue kommerzielle oder klinische Wertschöpfung hinzu.
- Die drei Kandidaten mit plausiblem mechanistischem Neuheitswert (Agoraphobia, Neurotic disorder, Dysthymic disorder) erreichen nur L4, unterstützt durch indirekte, nicht-agomelatine-spezifische oder Klassen-Ebenen-Literatur — unzureichend zum Weitermachen ohne dedizierte Studien.
- Fünf Kandidaten (benign paroxysmal torticollis of infancy, Ohdo syndrome und seine zwei Varianten, ligneous conjunctivitis, Keppen-Lubinsky syndrome) haben keine klinische, Literatur- oder mechanistische Unterstützung und sollten als wahrscheinlich Modell-Artefakte deprioritiert werden.
- Eine **Blocking**-Schwere-Datenlücke (DG001) bedeutet, dass TFDA/BfArM-äquivalente Etikett-Warnungen und Kontraindikationen nicht verfügbar sind, was diesen Kandidaten von selbst davon abhält, die S1-Sicherheits-Vorprüfungs-Stufe unabhängig von der Indikation zu räumen.

**Um Weitermachen zu können, ist folgendes erforderlich:**
- Beheben Sie DG001 (Blocking): erhalten und parsen Sie die offizielle Packungsbeilage (Warnungen/Kontraindikationen) von der relevanten regulatorischen Quelle.
- Beheben Sie DG002 (Hoch): erhalten Sie einen strukturierten Wirkmechanismus-Datensatz von der DrugBank API um Mechanismus-Link-Bewertung zu unterstützen.
- Für Agoraphobia, Neurotic disorder und Dysthymic disorder: suchen Sie agomelatine-spezifische (nicht Klassen-Ebenen) klinische Evidenz — idealerweise eine registrierte Studie oder eine dedizierte Systematische Übersicht — bevor Sie die "Forschungsfrage"-Stufe vorantreiben.
- Deprioritieren Sie weitere Evidenz-Sammlung zu den fünf L5-seltenen-Syndrom-Kandidaten, sofern eine zukünftige Modellversion keine glaubhafte mechanistische Begründung hervorgebracht hat.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

