---
layout: default
title: Atazanavir
parent: Nur Modellvorhersage (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Atazanavir: vorhergesagte neue Indikation Felines erworbenes Immundefizienz-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektion"
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Atazanavir
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Atazanavir: Von HIV-Infektion zu felinem erworbenem Immundefizienz-Syndrom

## Zusammenfassung in einem Satz

Atazanavir ist ein HIV-1-Proteaseinhibitor und war ursprünglich zur Behandlung der HIV-Infektion zugelassen.
Das TxGNN-Modell sagt voraus, dass es bei **felinem erworbenem Immundefizienz-Syndrom** (einer tiermedizinischen Erkrankung) wirksam sein könnte.
Für diese Vorhersage liegen in den für diesen Bericht zusammengestellten Daten **keine klinischen Studien** und **keine Publikationen** vor, es handelt sich um eine reine Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektion |
| Vorhergesagte neue Indikation | Felines erworbenes Immundefizienz-Syndrom |
| TxGNN-Vorhersagewert | 99,98 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassungen (keine gültige Zulassung) |
| Anzahl der Zulassungen | 3 (alle erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Atazanavir ein HIV-1-Proteaseinhibitor ist, dessen Wirksamkeit bei der HIV-Infektion belegt ist. Das feline Immundefizienzvirus (FIV) ist ein mit HIV-1 verwandtes Lentivirus, sodass eine konservierte virale Protease als Zielstruktur grundsätzlich denkbar ist.

Die FIV-Protease unterscheidet sich jedoch von der HIV-1-Protease in Substratspezifität und Inhibitorempfindlichkeit. Es gibt keine Daten, die eine Aktivität von Atazanavir gegen sie zeigen. Der hohe TxGNN-Wert beruht auf der Nähe zu HIV in der Krankheitsontologie und wird durch keine Studie oder Publikation gestützt.

Hinzu kommt: Es handelt sich um eine tiermedizinische Indikation und damit um einen Bereich außerhalb des üblichen Rahmens des Drug Repurposing für den Menschen.

### Weitere vorhergesagte Indikationen (zur Einordnung)

| Rang | Vorhergesagte Indikation | Score | Evidenzstufe | Einschätzung |
|------|------|------|------|------|
| 2 | Infektion mit dem Simianen Immundefizienzvirus | 99,98 % | L4 | Nur eine Tierstudie (Makaken) zu HAART, Atazanavir nicht isoliert; Hold |
| 3 | Neuroentwicklungsstörung mit ataktischem Gang, fehlender Sprache und verminderter kortikaler weißer Substanz | 99,98 % | L5 | Kein erkennbarer mechanistischer Zusammenhang, vermutlich ein Artefakt des Wissensgraphen; Hold |
| 4 | Familiäre kombinierte Hyperlipidämie (veralteter Begriff) | 99,82 % | L5 | Begriff in der Ontologie veraltet; Proteaseinhibitoren sind eher mit Dyslipidämie als Nebenwirkung verbunden; Hold |
| 5 | AIDS-related complex | 99,71 % | L4 | Historischer Begriff innerhalb des HIV-Spektrums, überschneidet sich mit der zugelassenen Indikation, kein echtes Repurposing; Hold |
| 6 | Kongenitale HIV-Infektion | 99,71 % | L3 | Perinataler Kontext, nahe an der ursprünglichen Indikation; Evidenz vor allem zu Sicherheit und Pharmakokinetik in der Schwangerschaft; Forschungsfrage |

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für die Hauptvorhersage (felines erworbenes Immundefizienz-Syndrom) liegen derzeit keine zugehörigen Publikationen vor.

Zum Vergleich die Literatur zur Vorhersage mit der meisten Evidenz (kongenitale HIV-Infektion, Rang 6):

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Kohortenstudie | Antiviral Therapy | Atazanavir-Exposition in der Schwangerschaft ist unabhängig von der Tenofovir-Gabe wirksam (Pharmakokinetik/Wirksamkeit) |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Kohortenstudie | JAMA Pediatrics | Angeborene Fehlbildungen und intrauterine antiretrovirale Exposition bei HIV-exponierten, nicht infizierten Säuglingen |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Kohortenstudie | Frontiers in Immunology | PHACS-SMARTT-Studie zur Sicherheit der intrauterinen Exposition gegenüber antiretroviralen Medikamenten |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Fall/Nicht-Fall-Studie | European Journal of Clinical Pharmacology | Risiko angeborener Anomalien nach fetaler Exposition gegenüber antiretroviralen Medikamenten (europäische Registerdaten) |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Kohortenstudie | Journal of AIDS and Immune Research | Neugeborenen-Hörscreening bei HIV-exponierten, nicht infizierten Säuglingen |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | Präklinisch | Reproductive Toxicology | Wechselwirkungen von Atazanavir und Ritonavir mit ABCB1-, ABCG2- und ABCC2-Transportern; Plazentapassage bei Ratten |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmakovigilanz | Clinical Infectious Diseases | Analyse zu Dolutegravir in der Schwangerschaft (betrifft nicht Atazanavir) |

Zur Vorhersage Rang 2 (SIV) liegt zudem [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) (2010, J Infect Dis) vor: eine präklinische Makakenstudie zu HAART mit reduzierter Virusreplikation im ZNS, jedoch persistierender viraler DNA; sie betrifft nicht Atazanavir allein.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000494 | Reyataz | – | HIV-Infektion |
| EMEA/H/C/004048 | Atazanavir Viatris (zuvor Atazanavir Mylan) | – | HIV-Infektion |
| EMEA/H/C/003904 | Evotaz | – | HIV-Infektion |

Alle drei Zulassungen sind erloschen; derzeit besteht keine gültige Zulassung.

---

## Sicherheitsaspekte

**Kontraindikationen laut Wissensgraph (keine Packungsbeilagen-Angaben):** Lebererkrankung und Leberversagen, Gallenblasenerkrankung, Hyperglykämie, Diabetes mellitus, diabetische Ketoazidose, chronische Hepatitis-C- und Hepatitis-B-Virusinfektion, Hämophilie, Hyperbilirubinämie (auch hereditär), Gilbert-Syndrom, Nephrolithiasis, akute Uratnephropathie, atrioventrikulärer Block, Laktatazidose.

**Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind unter anderem:
- Famotidin, Ranitidin, Rabeprazol, Omeprazol (Säureblocker/Protonenpumpenhemmer)
- Loperamid
- Triamcinolon, Budesonid (Kortikosteroide)

Als **moderat** eingestuft sind unter anderem Acarbose, Metformin, Pioglitazon, Alogliptin, Albiglutid, Acetohexamid, Hydrocortison, Betamethason, Alosetron, Aprepitant, Aluminiumhydroxid und Calciumcarbonat.

Weitere Warnhinweise und Kontraindikationen aus der Fachinformation liegen nicht vor; bitte die Packungsbeilage bzw. Fachinformation konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage zum felinen Immundefizienz-Syndrom beruht allein auf einem Modellwert (Evidenzstufe L5) ohne Studien oder Publikationen; zudem handelt es sich um eine tiermedizinische Indikation, und in Deutschland besteht keine gültige Zulassung. Auch die übrigen Vorhersagen liefern keine belastbare Evidenz für eine echte neue Indikation beim Menschen.

**Für ein Weiterkommen sind erforderlich:**
- Daten zum Wirkmechanismus (MOA)
- Sicherheitsrelevante Angaben aus der Fachinformation (Warnhinweise, Kontraindikationen), die für das Sicherheits-Screening noch fehlen
- Präklinische Daten, ob Atazanavir die FIV-Protease hemmt
- Falls der menschliche Kontext priorisiert wird: Weiterverfolgung der perinatalen HIV-Indikation (Rang 6) als Forschungsfrage, mit Klärung der Marktverfügbarkeit
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

