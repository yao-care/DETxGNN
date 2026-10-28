---
layout: default
title: Simvastatin
parent: Nur Modellvorhersage (L5)
nav_order: 430
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Simvastatin: vorhergesagte neue Indikation Hirnstamminfarkt (Evidenzstufe L1). Ursprüngliche Indikation: Dyslipidämien"
monitor_inn: "SIMVASTATIN"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Simvastatin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

## Simvastatin: Von Dyslipidämien zu Hirnstamminfarkt
{: .text-alpha }

## Zusammenfassung

Simvastatin ist ein HMG-CoA-Reduktase-Hemmer und war ursprünglich zur Behandlung von **Dyslipidämien** zugelassen. Das TxGNN-Modell sagt voraus, dass es bei **familiärer Hypercholesterinämie** wirksam sein könnte. Diese Vorhersage wird durch **8 klinische Studien** und **18 Publikationen** gestützt. Es handelt sich allerdings faktisch um eine Anwendung im Rahmen oder nahe der bestehenden Indikation und nicht um ein echtes Repurposing.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Dyslipidämien |
| Vorhergesagte neue Indikation | Familiäre Hypercholesterinämie |
| TxGNN-Vorhersagewert | 0,9941 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Proceed with Guardrails (Fortführung mit Schutzmaßnahmen) |

---

## Warum ist diese Vorhersage plausibel?

Simvastatin hemmt die HMG-CoA-Reduktase. Dadurch sinkt die hepatische Cholesterinsynthese, und die Zahl der LDL-Rezeptoren auf den Leberzellen steigt. Der LDL-Cholesterin-Abbau nimmt zu. Dieser Mechanismus passt unmittelbar zur familiären Hypercholesterinämie, die durch einen gestörten LDL-Abbau gekennzeichnet ist.

Die ursprüngliche Indikation (Dyslipidämien) und die vorhergesagte Indikation überschneiden sich stark. Die Wirkung hängt davon ab, dass mindestens ein funktionsfähiges LDL-Rezeptor-Allel vorhanden ist. Bei homozygoter Erkrankung oder LDL-Rezeptor-Nullmutation ist die Wirksamkeit begrenzt, dort sind Zusatztherapien nötig.

Die für diesen Bericht zusammengestellten Daten enthalten keine detaillierten Angaben zum Wirkmechanismus aus einer Arzneimitteldatenbank. Die obige Beschreibung beruht auf der bekannten Pharmakologie der Statine.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Abgeschlossen | 720 | ENHANCE: Ezetimib plus hochdosiertes Simvastatin vs. Simvastatin allein, Progression der Atherosklerose der Halsschlagader bei heterozygoter FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Abgeschlossen | 248 | Ezetimib plus Simvastatin bei Jugendlichen (10–17 Jahre) mit heterozygoter FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Abgeschlossen | 442 | Nierenwirkungen von Rosuvastatin und Simvastatin bei Dyslipidämie Typ IIa/IIb, einschließlich heterozygoter FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Abgeschlossen | 249 | Alirocumab vs. Placebo bei heterozygoter FH (Simvastatin vermutlich Hintergrundtherapie) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Abgeschlossen | 44 | Langzeitsicherheit von Ezetimib zusätzlich zu Atorvastatin oder Simvastatin bei homozygoter FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Abgeschlossen | 50 | Wirksamkeit und Sicherheit von Ezetimib zusätzlich zu Atorvastatin oder Simvastatin bei homozygoter FH |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Abgeschlossen | 153 | Alirocumab bei Kindern und Jugendlichen mit heterozygoter FH (Rolle von Simvastatin unklar) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Abgeschlossen | 18 | Alirocumab bei Kindern und Jugendlichen mit homozygoter FH |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Abgeschlossen | 527 | Dosisfindung von LY3015014 (PCSK9-Antikörper) bei primärer Hypercholesterinämie |

Hinweis: Die meisten Studien untersuchen andere Substanzen, und Simvastatin ist lediglich Hintergrund- oder Kombinationstherapie. Direkt relevant sind vor allem ENHANCE und die Jugendlichenstudie.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Klinische Studie (ENHANCE) | N Engl J Med | Simvastatin mit oder ohne Ezetimib bei familiärer Hypercholesterinämie, Effekt auf die Progression der Atherosklerose |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematischer Review (Cochrane) | Cochrane Database Syst Rev | Statine bei Kindern mit familiärer Hypercholesterinämie |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Nutzen und Risiken von Simvastatin bei familiärer Hypercholesterinämie |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Nutzen-Risiko-Bewertung von Simvastatin bei familiärer Hypercholesterinämie |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | Klinische Studie | J Am Coll Cardiol | Wirksamkeit und Sicherheit von Ezetimib plus Simvastatin bei Jugendlichen mit heterozygoter FH |
| [2679083](https://pubmed.ncbi.nlm.nih.gov/2679083/) | 1989 | Klinische Studie | Am J Med | Simvastatin 20 mg senkte LDL-C nach 8 Wochen im Mittel um 38 %, 40 mg nach weiteren 16 Wochen um 42 % |
| [2028634](https://pubmed.ncbi.nlm.nih.gov/2028634/) | 1991 | Review | DICP | Pharmakologie und klinische Anwendung von Simvastatin |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Leitlinie | J Am Coll Cardiol | ACC/AHA-Leitlinie 2026 zum Management von Dyslipidämien |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Leitlinie | Endocr Pract | AACE/ACE-Leitlinien zu Dyslipidämie und kardiovaskulärer Prävention |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Querschnittsstudie | J Clin Med | Zelluläre Immunität bei Kindern mit FH unter Simvastatin 10 mg |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002559 | Cholib | – | Dyslipidämien |

Diese Zulassung (Inhaber: Viatris Healthcare Limited) ist gültig.

---

## Sicherheitsaspekte

**Wechselwirkungen (100 Einträge in der Interaktionsabfrage, Auswahl):**
- **Schwerwiegend (Major):** Amiodaron, Amlodipin, Fenofibrat
- **Moderat:** u. a. Zidovudin, Paclitaxel, Nifedipin, Adalimumab, Omeprazol, Ethanol, Aprepitant, Alpelisib
- **Gering (Minor):** Albiglutid

**Kontraindikationen aus dem Wissensgraphen** (Wissensgraph-Kanten, nicht der Packungsbeilagentext): Pankreatitis, Lebererkrankung, Gallenblasenerkrankung, Thrombozytopenie, Hyperglykämie, Myopathie, Rhabdomyolyse, Diabetes mellitus, Diabetische Ketoazidose, Gicht, Gerinnungsstörungen, akutes Koronarsyndrom, Myokardinfarkt, koronare Herzkrankheit, Magengeschwür u. a.

**Praktische Hinweise:** Bei HIV-Patienten ist Simvastatin mit geboosteten Proteaseinhibitoren und Cobicistat wegen CYP3A4-Hemmung und Myopathierisiko zu vermeiden. Bei Kindern und Jugendlichen sind Dosierung sowie Myopathie- und Wechselwirkungsmonitoring besonders wichtig.

Detaillierte Warnhinweise und Gegenanzeigen aus der Packungsbeilage liegen nicht vor. Bitte die Fachinformation heranziehen.

---

## Weitere vorhergesagte Indikationen (kurz)

| Indikation | Score | Evidenzlevel | Empfehlung |
|---|---|---|---|
| HIV-Infektion | 0,9922 | L3 | Forschungsfrage (betrifft Management der Dyslipidämie und Wechselwirkungen, keine antivirale Wirkung) |
| Hirnstamminfarkt | 0,9941 | L5 | Hold (keine direkte Evidenz) |
| CETP-Mangel | 0,9939 | L5 | Hold (schwache mechanistische Begründung) |
| ABri-Amyloidose | 0,9913 | L5 | Hold |
| Neuroentwicklungsstörung mit ataxischem Gang | 0,9910 | L5 | Hold (vermutlich Netzwerkartefakt) |

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Mehrere abgeschlossene Phase-3-Studien (u. a. ENHANCE und die Jugendlichenstudie mit Ezetimib plus Simvastatin) sowie Cochrane-Reviews und Leitlinien stützen den Einsatz bei familiärer Hypercholesterinämie. Der Mechanismus ist direkt plausibel. Da dies im Kern der bestehenden Indikation Dyslipidämie entspricht, handelt es sich nicht um ein echtes Repurposing. Zudem ist die einzige deutsche Zulassung erloschen.

**Für das weitere Vorgehen sind erforderlich:**
- Auswertung der Fachinformation zu Warnhinweisen und Gegenanzeigen (Sicherheitsprüfung ist bislang nicht abgeschlossen)
- Klärung des aktuellen Zulassungsstatus von Simvastatin-Monopräparaten in Deutschland (die erfasste Zulassung betrifft ein Kombinationspräparat und ist erloschen)
- Detaillierte Wirkmechanismus-Daten aus einer Arzneimitteldatenbank
- Sicherheitsüberwachung (Myopathie, Leberwerte, Wechselwirkungen), besonders bei Kindern und Jugendlichen
- Zusatztherapiekonzept für homozygote FH oder LDL-Rezeptor-Nullmutationen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

