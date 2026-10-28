---
layout: default
title: Oxybutynin
parent: Nur Modellvorhersage (L5)
nav_order: 334
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Oxybutynin: vorhergesagte neue Indikation Restless-Legs-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: Dranginkontinenz"
monitor_inn: "OXYBUTYNIN"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
---

# Oxybutynin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Oxybutynin: Von dranginkontinenz zu Restless-Legs-Syndrom
{: .text-alpha }

## Zusammenfassung

Oxybutynin ist ein Antimuskarinikum und wurde ursprünglich zur Behandlung der Dranginkontinenz (überaktive Blase) eingesetzt.
Das TxGNN-Modell sagt voraus, dass es bei **Restless-Legs-Syndrom** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Dranginkontinenz |
| Vorhergesagte neue Indikation | Restless-Legs-Syndrom |
| TxGNN-Vorhersagewert | 0,9974 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

Weitere vom Modell vorhergesagte Indikationen (jeweils ohne klinische Studien):

| Rang | Indikation | TxGNN-Wert | Evidenzgrad | Empfehlung |
|---|---|---|---|---|
| 2 | Gastroduodenitis | 0,9962 | L5 | Hold |
| 3 | Peptisches Ulkus | 0,9931 | L5 | Hold |

---

## Warum ist diese Vorhersage plausibel?

Für diesen Bericht liegen keine detaillierten Daten zum Wirkmechanismus vor. Bekannt ist, dass Oxybutynin ein Muskarinrezeptor-Antagonist mit zusätzlicher direkter krampflösender (spasmolytischer) Wirkung auf die glatte Muskulatur ist. Seine Wirksamkeit bei Dranginkontinenz gilt als etabliert.

Ein mechanistischer Zusammenhang zum Restless-Legs-Syndrom ist durch die vorliegenden Daten **nicht belegt**. RLS ist eine sensomotorische Störung, die mit dem dopaminergen System und dem Eisenstoffwechsel in Verbindung gebracht wird. Anticholinergika können RLS-Symptome bei manchen Patienten sogar verschlechtern. Der hohe Vorhersagewert ist daher als rein rechnerischer Hinweis zu verstehen, nicht als Beleg.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für Restless-Legs-Syndrom liegt derzeit keine zugehörige Literatur vor.

Zur drittplatzierten Vorhersage (peptisches Ulkus) wurden folgende Quellen gefunden, alle von geringer Aussagekraft:

| PMID | Jahr | Typ | Journal | Kernaussage |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Fallbericht (Nebenwirkung) | DICP: the annals of pharmacotherapy | Oxybutynin-induzierte Refluxösophagitis, vermutlich durch verminderten Tonus des unteren Ösophagussphinkters |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Klinische Auswertung (unkontrolliert) | Current Therapeutic Research | Klinische Bewertung von Oxybutynin bei gastrointestinalen Erkrankungen |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Pharmakologische Übersicht | Archives Internationales de Pharmacodynamie et de Therapie | Oxybutynin als muskulotropes Spasmolytikum mit moderater anticholinerger Wirkung |

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000532 | Kentera (zuvor Oxybutynin Nicobrand), Teva B.V. | – | Dranginkontinenz (Status: gültig) |

---

## Sicherheitsaspekte

**Kontraindikationen aus dem Wissensgraphen** (abgeleitet aus Arzneimittel-Krankheits-Beziehungen in PrimeKG, nicht aus dem Beipackzettel):
- Magen-Darm: Paralytischer Ileus, Darmverschluss, toxisches Megakolon, Colitis ulcerosa bzw. chronisch-entzündliche Darmerkrankungen, gastroösophageale Refluxkrankheit, Ösophagitis, Hiatushernie
- Auge: Engwinkelglaukom
- Neuromuskulär: Myasthenia gravis
- Urogenital: Blasenhalsobstruktion, benigne Prostatahyperplasie
- Herz-Kreislauf: Hypertonie, koronare Herzkrankheit, Herz-Reizleitungsstörungen, plötzlicher Herzstillstand
- Weitere: Nieren- und Lebererkrankungen, Gallenblasenerkrankungen, Hyperthyreose

**Arzneimittelwechselwirkungen** (100 Einträge erfasst; Auswahl):
- **Schwerwiegend (Major):** Kaliumcitrat, Kaliumchlorid
- **Moderat:** weitere Anticholinergika (u. a. Atropin, Hyoscyamin, Glycopyrronium, Trospium, Dicyclomin, Propantheline), Opioide (Morphin, Opium), Loperamid, Metoclopramid, Aprepitant, Eluxadoline, Pramlintid

**Relevante Hinweise zu den Vorhersagen:** Anticholinergika können den Tonus des unteren Ösophagussphinkters senken und Reflux fördern. Das ist für Gastroduodenitis und peptisches Ulkus ein klares Sicherheitssignal. Angaben aus dem Beipackzettel (Warnhinweise, Gegenanzeigen) liegen nicht vor; bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der Vorhersagewert für Restless-Legs-Syndrom ist hoch, es gibt jedoch weder klinische Studien noch Literatur, und ein plausibler Mechanismus fehlt. Zudem ist die einzige deutsche Zulassung erloschen. Für die anderen beiden Vorhersagen gilt dasselbe, bei peptischem Ulkus kommen ein Sicherheitssignal und die weitgehende Ablösung der Anticholinergika durch Protonenpumpenhemmer hinzu.

**Für ein Weiterkommen sind erforderlich:**
- Daten zum Wirkmechanismus (MOA), etwa aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (derzeit blockierende Datenlücke für die Sicherheitsbewertung)
- Systematische Literaturrecherche zu Anticholinergika bei RLS, einschließlich möglicher Symptomverschlechterung
- Klärung der Marktverfügbarkeit in Deutschland und möglicher Darreichungswege
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

