---
layout: default
title: Insulin Detemir
parent: Nur Modellvorhersage (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: Vom Diabetes mellitus (Originale Indikationsdaten fehlend) zur Signalbestätigung für Typ-1-Diabetes mellitus

## Zusammenfassung in einem Satz

> Insulin Detemir (Levemir®) ist ein langwirksames Basis-Insulinanalogon, dessen ursprüngliche Zulassungsindikation in diesem Datensatz nicht dokumentiert ist, aber bekanntermaßen als Basis-Insulintherapie für Typ-1- und Typ-2-Diabetes verwendet wird. TxGNN prognostiziert eine hohe Relevanz für **Typ-1-Diabetes mellitus** (Score 99,77%), unterstützt durch **über 60 abgeschlossene klinische Studien** und **20 Publikationen** — es ist jedoch zu beachten: Dies ist eine **Signalbestätigung einer bestehenden zugelassenen Indikation** des Arzneistoffs und keine echte „Repurposing".

---

## Schnellübersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Keine Daten vorhanden (taiwan_regulatory.licenses leer; Arzneistoff nicht auf deutschem Markt); bekannt als Basis-Insulin zur Blutzuckerkontrolle bei Diabetes |
| Prognostizierte neue Indikation | Typ-1-Diabetes mellitus — **Anmerkung: Dies ist tatsächlich eine bereits genehmigte Marktindikation von Levemir®, kein echtes Repurposing** |
| TxGNN-Prognosescore | 99,77% (Rang 3222) |
| Evidenzgrad | L1 (≥2 abgeschlossene Phase-3-RCTs) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Lizenzanzahl | 0 |
| Entscheidungsempfehlung | Proceed with Guardrails |

---

## Warum ist diese Prognose sinnvoll?

Derzeit liegen keine detaillierten Angaben zum Wirkmechanismus (MOA) vor. Nach verfügbaren Informationen ist Insulin Detemir ein langwirksames Basis-Insulinanalogon, das durch reversible Bindung einer 14-Kohlenstoff-Fettsäureseitenkette an Albumin eine verzögerte Absorption und Wirkungsdauer von etwa 24 Stunden erreicht. Pharmakodynamisch ist die Wirkung stabiler als NPH-Insulin und das Hypoglykämierisiko geringer.

Insulin Detemir ersetzt direkt die durch Autoimmunzerstörung von Pankreas-β-Zellen verlorene endogene Insulinsekretion bei Typ-1-Diabetes, wobei der Wirkmechanismus-Zusammenhang **direkt und klinisch validiert** ist und nicht auf indirekten Hypothesenketten (klassisches Repurposing) beruht.

**Wichtiger Hinweis**: Das Feld `original_indications` in diesem Datensatz ist leer — dies ist eine Datenlücke. Insulin Detemir (Handelsname Levemir®) ist jedoch in vielen Ländern bereits für die Behandlung von Typ-1- und Typ-2-Diabetes zugelassen. Daher ist die TxGNN-Prognose mit Rang 1 für „Typ-1-Diabetes" praktisch eine **Bestätigung einer bereits etablierten Indikation** und nicht die Entdeckung einer neuen Anwendung. Der analytische und wissenschaftliche Wert liegt in der Validierung der Vorhersagegenauigkeit des TxGNN-Modells bei bekannten Arzneistoff-Krankheits-Beziehungen, was als positive Kontrolle für die Modellglaubwürdigkeit dient, aber kein kommerzielles „Repurposing"-Potenzial darstellt.

---

## Klinische Studienbelege

| Studienmummer | Phase | Status | Patientenzahl | Wichtigste Befunde |
|--------|----------|--------|------------|----------|
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Abgeschlossen | 50 | Vergleich täglich eine vs. zwei Injektionen Insulin Detemir bei Kindern und Jugendlichen mit T1DM hinsichtlich metabolischer Kontrolle |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Abgeschlossen | 131 | RCT Crossover-Vergleich, Detemir vs. NPH-Insulin bei T1DM-Patienten hinsichtlich Hypoglykämiehäufigkeit |
| [NCT00537303](https://clinicaltrials.gov/study/NCT00537303) | Phase 4 | Abgeschlossen | 296 | Einmal täglich Detemir mit stufenweisem Zusatz von schnellwirksamem Aspart hinsichtlich Sicherheit und Wirksamkeit |
| [NCT00184665](https://clinicaltrials.gov/study/NCT00184665) | Phase 3 | Abgeschlossen | 501 | 2-Jahres-Vergleich Detemir vs. NPH bei T1DM bezüglich Wirksamkeit (HbA1c) und Sicherheit (Hypoglykämie, Körpergewicht, Antikörper) |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Abgeschlossen | 347 | Kinder und Jugendliche mit T1DM, Detemir einmal oder zweimal täglich vs. NPH hinsichtlich Wirksamkeit und Sicherheit |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Abgeschlossen | 470 | Schwangere Frauen mit T1DM, Vergleich Detemir vs. NPH hinsichtlich Blutzuckerkontrolle und Sicherheit |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Abgeschlossen | 752 | 6-Monats-Studie, T1DM-Patienten unter Basis-Bolus-Therapie mit Detemir (2400 nmol/mL-Formulierung) vs. NPH hinsichtlich Wirksamkeit und Sicherheit |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Abgeschlossen | 114 | Erwachsene mit T1DM, Detemir + Aspart vs. NPH + Aspart hinsichtlich Wirksamkeit und Sicherheit |
| [NCT02922179](https://clinicaltrials.gov/study/NCT02922179) | N/A | Abgeschlossen | 103,951 | Große deskriptive Analyse zur Charakterisierung von Erwachsenen mit Diabetes, die lang-/mittelfristig wirkendes Insulin verwenden (indirekt unterstützende epidemiologische Daten) |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | N/A | Abgeschlossen | 4,464 | Große postmarketing-Beobachtungsstudie zur Bewertung von Sicherheit, Blutzuckerkontrolle und Körpergewicht unter Levemir® bei T1DM/T2DM-Patienten |

---

## Publikationsbelege

| PMID | Jahr | Typ | Journal | Wichtigste Befunde |
|------|--------|--------|---------|----------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT-Studie: Nicht-Unterlegenheitsvergleich Insulin Degludec vs. Detemir (beide mit Aspart) bei schwangeren Frauen mit T1DM |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematische Übersicht/Netzwerk-Meta-Analyse | Value in Health | Relative Wirksamkeit und Sicherheit von Basis-Insulintherapien bei erwachsenem T1DM im Netzwerk-Meta-Analyse-Vergleich |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane-Systematische Übersicht | Cochrane Database Syst Rev | Systematische Übersicht zu (Ultra-)langwirksamen Insulinanaloga bei T1DM-Patienten |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematische Übersicht/Meta-Analyse | Pol Arch Med Wewn | Systematische Übersicht und Meta-Analyse: Detemir vs. NPH bei T1DM |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematische Übersicht/Meta-Analyse | Clin Ther | Vergleich Insulin Degludec mit anderen langwirksamen Basis-Insulinen (einschließlich Detemir) bezüglich Wirksamkeit und Verträglichkeit bei T1DM/T2DM |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Aktualisierung zur Behandlung von Typ-1-Diabetes in der Schwangerschaft: Lebensstil, Arzneimittel und neue Technologien |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | Überblick über die Anwendung von Insulinanaloga bei Kindern und Jugendlichen mit T1DM |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Überblick über Insulin Detemir bei der Behandlung von Typ-1- und Typ-2-Diabetes |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Überblick über Insulin Detemir in der Therapie von Typ-1- und Typ-2-Diabetes |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Fokussierte Übersicht über Insulin Detemir bei Typ-1- und Typ-2-Diabetes |

---

## Marktinformationen Deutschland

Insulin Detemir ist derzeit **nicht auf dem deutschen Markt zugelassen** (`total_licenses = 0`); im Datensatz sind keine Lizenzeinträge vorhanden.

---

## Sicherheitserwägungen

Bitte beachten Sie die vollständigen Sicherheitsinformationen in der Fachinformation.

(Im Datensatz stehen keine Daten zu kritischen Warnhinweisen, Kontraindikationen und Wechselwirkungen zur Verfügung; Fachinformations-Warnhinweise und Kontraindikationen wurden als Blocking-Level-Datenlücken klassifiziert und müssen vorrangig ergänzt werden.)

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
- Für Typ-1-Diabetes liegen mehrere abgeschlossene Phase-3-RCTs vor (wie NCT01697657, NCT00184665, NCT03220425 u.a.) sowie systematische Übersichten/Cochrane-Übersichten, mit Evidenzgrad L1; die Modellvorhersage ist in die richtige Richtung ausgerichtet.
- Dies ist jedoch eine **bestehende zugelassene Indikation von Insulin Detemir**, nicht eine neu entdeckte Anwendung, daher stellt dies keine typische „Repurposing"-Geschäftsmöglichkeit dar; der Wert liegt in der Validierung der Modellzuverlässigkeit; die strategische Entscheidung sollte sich auf „Verfolgung der Markteinführung in Deutschland" konzentrieren, nicht auf „Entwicklung neuer Indikationen".

**Vor dem Voranschreiten erforderliche Ergänzungen:**
- TFDA/Fachinformations-Warnhinweise und Kontraindikationen (Blocking, DG001) — Voraussetzung für Eintritt in S1 Sicherheitsinitialbeurteilung
- DrugBank-Wirkmechanismus (MOA) explizite Beschreibung (High, DG002)
- Bei Erwägung einer deutschen Markteinführungsstrategie sind vollständige klinische Datenpakete und Arzneimittelwechselwirkungsinformationen erforderlich, wie für BfArM-Anträge notwendig

**Empfohlene Behandlung der verbleibenden 9 Prognosen (Rang 2–10):**
- Rang 4 (thiaminansprechende Dysfunktionssyndrom) und Rang 7 (Pankreasagenesie) sind mechanistisch plausibel, aber ohne direkte klinische Belege als Forschungsfragen (L4, Research Question) einzustufen; können als zukünftige Einzelfallforschungsrichtung dienen, gegenwärtig keine Ressourcenallokation erforderlich.
- Rang 2, 3, 5, 6 (Autoimmun-Oophoritis, Opsismodysplasie, fokales/klassisches Stiff-Person-Syndrom-Spektrum): Evidenzgrad L5, keine mechanistischen oder klinischen Belege, Empfehlung: Hold.
- Rang 8, 9, 10 (verschiedene Lipodystrophie/Lipoatrophie): Existieren **Richtungsbedenken** — diese sind höchstwahrscheinlich bekannte unerwünschte Ereignisse der Insulininjektionsstelle (Fettgewebsstoffwechseländerungen), die von TxGNN als therapeutische Verknüpfung fehlbewertet wurden; Empfehlung: Aus der Kandidatenliste entfernen oder zusätzlich als Sicherheitssignal kennzeichnen, nicht nach Indikationsprozess behandeln.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

