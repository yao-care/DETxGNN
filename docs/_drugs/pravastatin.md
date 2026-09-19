---
layout: default
title: Pravastatin
parent: Hohe Evidenz (L1-L2)
nav_order: 316
evidence_level: L2
indication_count: 9
---

# Pravastatin
{: .fs-9 }

Evidenzniveau: **L2** | Vorhergesagte Indikationen: **9** 
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

# Pravastatin: Von Hypercholesterinämie zu HIV-assoziierter Dyslipidämie und kardiovaskulärem Risikomanagement

## Zusammenfassung in einem Satz

> Pravastatin ist ein HMG-CoA-Reduktase-Hemmer (Statin); die Evidenzbasis beschreibt es durchgehend als Behandlung für Hypercholesterinämie/Dyslipidämie, obwohl formale Aufzeichnungen zu ursprünglicher Indikation und Wirkmechanismus in diesem Paket als Datenlücken gekennzeichnet sind.
> Von **9 TxGNN-vorhergesagten Indikationen**, die für diesen Kandidaten gescreent wurden, **HIV-assoziierte Dyslipidämie / kardiovaskuläres Risikomanagement** erwies sich als die klinisch glaubwürdigste, unterstützt durch **16 klinische Studien** (einschließlich dedizierter Phase-2–4-RCTs von Pravastatin bei HIV-infizierten Patienten) und **20 Publikationen**.
> Dies ist Risikofaktor-Management bei HIV-Patienten unter antiretroviraler Therapie, keine antivirale Wirkung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht in Quelldaten verfügbar (`taiwan_regulatory.licenses` ist leer). Beschreibungen in Studien/Literatur in dieser Evidenzbasis identifizieren Pravastatin durchgehend als HMG-CoA-Reduktase-Hemmer bei Hypercholesterinämie/Dyslipidämie. |
| Vorhergesagte neue Indikation | HIV-Infektionskrankheit (ART-assoziierte Dyslipidämie / kardiovaskuläres Risikomanagement) |
| TxGNN-Vorhersagepunktzahl | 99,74% (Rang 3562) |
| Evidenzstufe | L2 |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfehlung zur Entscheidung | Fortschreiten mit Schutzmaßnahmen |

### Alle gescreenten vorhergesagten Indikationen (zur Transparenz)

| Rang | Krankheit | TxGNN-Punktzahl | Evidenzstufe | Entscheidung | Bemerkung |
|---|---|---|---|---|---|
| 1 | Homozygote familiäre Hypercholesterinämie | 99,95% | L4 | Zurückhalten | Statin-Wirksamkeit begrenzt durch nicht funktionsfähiges LDLR in HoFH |
| 2 | **HIV-Infektionskrankheit** | **99,74%** | **L2** | **Fortschreiten mit Schutzmaßnahmen** | Ausgewählt als primärer Kandidat (siehe unten) |
| 3 | Neuronale Entwicklungsstörung (ataktischer Gang/Sprachlosigkeit) | 99,62% | L5 | Zurückhalten | Keine Studien, keine Literatur, keine mechanistische Begründung |
| 4 | Erworbenes Immundefektsyndrom bei Katzen | 99,55% | L5 | Zurückhalten | Veterinärmedizinische Krankheit; Graph-Spillover via HIV-Homologie |
| 5 | Simian Immunodeficiency Virus-Infektion | 99,55% | L5 | Zurückhalten | Primen-Modellvirus; keine humanmedizinische Evidenz |
| 6 | Familiäre Hypercholesterinämie | 99,34% | L1 | Fortschreiten mit Schutzmaßnahmen | Bereits eine etablierte Statin-Indikation, keine Neurepurposing-Kandidatin |
| 7 | Hypoalphalipoproteinämie | 99,21% | L4 | Zurückhalten | Keine dedizierten Studien; Statin-Effekt auf HDL ist bescheiden/off-target |
| 8 | Hypercholesterinämie aufgrund von CYP7A1-Mangel | 99,07% | L5 | Zurückhalten | Ultraseltene Krankheit; nur mechanistische Spekulation |
| 9 | Cholesterinester-Transferprotein-Mangel | 99,04% | L5 | Zurückhalten | Keine mechanistische oder klinische Verbindung zu Statin-Pathway |

---

## Warum ist diese Vorhersage sinnvoll?

Das `original_moa`-Feld selbst ist als Datenlücke gekennzeichnet, aber die zugrundeliegende Evidenzbasis identifiziert Pravastatin wiederholt und durchgehend als kompetitiven HMG-CoA-Reduktase-Hemmer, der die hepatische Cholesterinsynthese senkt und die LDL-Rezeptor-Expression hochreguliert (z. B. PMID 1658544, NCT00227500). Dieser Mechanismus ist die pharmakologische Grundlage für seine Verwendung bei Hypercholesterinämie/Dyslipidämie.

HIV-Infektionen und ihre antiretrovirale Therapie (ART), besonders PI-basierte Regime, sind in dieser Evidenzbasis gut dokumentiert, um Dyslipidämie, chronische Immunaktivierung und beschleunigte Atherosklerose zu verursachen und erheblich das kardiovaskuläre Risiko bei Menschen mit HIV zu erhöhen. Statine sind daher eine rationale Ergänzung in dieser Population — nicht als antivirale Mittel, sondern als lipidsenkende und möglicherweise anti-inflammatorische/immunmodulatorische Therapie, die eine wichtige ART-assoziierte Komorbidität adressiert.

Pravastatin sticht unter Statinen für diese Population besonders hervor, da es nicht umfangreich über CYP3A4 metabolisiert wird, im Gegensatz zu Atorvastatin oder Simvastatin, was das Risiko klinisch signifikanter Arzneimittelwechselwirkungen mit Proteaseinhibitoren und anderen ART-Mitteln, die starke CYP3A4-Inhibitoren sind, reduziert. Dieser DDI-Vorteil ist explizit die Begründung hinter mehreren dedizierten Studien in diesem Evidenzpaket (z. B. NCT00000941, NCT00630734, NCT00117494), die Pravastatin als bevorzugtes Statin für HIV-infizierte, PI-behandelte Patienten mit Dyslipidämie etabliert haben.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT00006412](https://clinicaltrials.gov/study/NCT00006412) | Phase 3 | Abgeschlossen | 630 | Fenofibrat vs. Pravastatin bei HIV-infizierten Probanden mit Lipidabnormalitäten |
| [NCT00117494](https://clinicaltrials.gov/study/NCT00117494) | Phase 4 | Abgeschlossen | 86 | Rosuvastatin vs. Pravastatin bei ART-behandelten dyslipidämischen HIV-Patienten (ANRS 126) |
| [NCT00221754](https://clinicaltrials.gov/study/NCT00221754) | Phase 2 | Abgeschlossen | 21 | RCT von Pravastatin bei hypercholesterinämischen HIV-Patienten auf Proteaseinhibitoren |
| [NCT00147797](https://clinicaltrials.gov/study/NCT00147797) | N/A | Abgeschlossen | 84 | Pravastatin-Effekt auf Halsschlagader-Struktur/-funktion bei HIV-Patienten unter ART |
| [NCT00227500](https://clinicaltrials.gov/study/NCT00227500) | Phase 4 | Abgeschlossen | 40 | Randomisierte, doppelblinde, placebokontrollierte Pravastatin-Studie bei HIV-Hyperlipidämie |
| [NCT00000941](https://clinicaltrials.gov/study/NCT00000941) | Phase 1 | Abgeschlossen | 56 | PK-Wechselwirkungen zwischen Proteaseinhibitoren und Statinen (Pravastatin, Simvastatin, Atorvastatin) |
| [NCT02841774](https://clinicaltrials.gov/study/NCT02841774) | Phase 2 | Abgeschlossen | 10 | HILLCLIMBER: mitteldosiertes Pravastatin vs. hochdosiertes Rosuvastatin bei HIV-Patienten mit KHK |
| [NCT00630734](https://clinicaltrials.gov/study/NCT00630734) | Phase 4 | Abgeschlossen | 32 | SLCO1B1-genetische Prädiktoren von Darunavir/Ritonavir–Pravastatin-DDI |
| [NCT00982189](https://clinicaltrials.gov/study/NCT00982189) | N/A | Abgeschlossen | 37 | Kardiovaskuläres Risiko-Reduktions-Polypill-Pilot bei HIV-infizierten Personen |
| [NCT00843661](https://clinicaltrials.gov/study/NCT00843661) | Phase 4 | Unbekannt | 60 | Ezetimib+Fenofibrat vs. Pravastatin-Monotherapie bei HIV-Patienten auf Proteaseinhibitoren |

---

## Literaturische Evidenz

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Phase 4) | The Lancet HIV | INTREPID-Studie: Pitavastatin vs. Pravastatin bei HIV-1-Patienten mit Dyslipidämie, Vermeidung von CYP450-abhängigem Metabolismus |
| [25574964](https://pubmed.ncbi.nlm.nih.gov/25574964/) | 2014 | RCT | AIDS | Atorvastatin reduzierte T-Zell-Aktivierung; Pravastatin zeigte keinen signifikanten Effekt auf Immunaktivierung |
| [26148680](https://pubmed.ncbi.nlm.nih.gov/26148680/) | 2015 | RCT, Cross-over | BMC Research Notes | Pravastatin, Phytosterole und Kombinationstherapie verglichen für Lipidsenkung bei HIV |
| [28252528](https://pubmed.ncbi.nlm.nih.gov/28252528/) | 2017 | Kohortenstudie/RCT | AIDS | Pitavastatin und Pravastatin verglichen in Bezug auf Immunaktivierung und arterielle Entzündungsmarker bei HIV |
| [16603852](https://pubmed.ncbi.nlm.nih.gov/16603852/) | 2006 | RCT (placebokontrolliert) | AIDS | Pravastatin-Effekt auf Körperzusammensetzung und kardiovaskuläre Marker bei HIV-infizierten Männern |
| [17117030](https://pubmed.ncbi.nlm.nih.gov/17117030/) | 2006 | Kohorte | AIDS | Pravastatin hatte keinen signifikanten Einfluss auf Intima-Media-Dicke der Halsschlagader oder aortale Steifheit bei HIV-Patienten |
| [16218799](https://pubmed.ncbi.nlm.nih.gov/16218799/) | 2005 | RCT | AIDS Research and Human Retroviruses | ACTG 5087: Fenofibrat vs. Pravastatin für kombinierte Dyslipidämie bei HIV |
| [18991624](https://pubmed.ncbi.nlm.nih.gov/18991624/) | 2008 | Übersichtsarbeit | Current HIV Research | Vergleichende Übersicht von Rosuvastatin, Pravastatin und Atorvastatin für PI-assoziierte Hypercholesterinämie |
| [28364370](https://pubmed.ncbi.nlm.nih.gov/28364370/) | 2017 | Übersichtsarbeit/Leitlinie | American Journal of Cardiovascular Drugs | Empfehlungen zur Verwaltung von Statin–HIV-Medikamenten-Wechselwirkungen |
| [25907504](https://pubmed.ncbi.nlm.nih.gov/25907504/) | 2015 | Systematische Übersichtsarbeit | The American Journal of Cardiology | Systematische Übersichtsarbeit zur Nützlichkeit einer Statin-Therapie bei HIV-infizierten Patienten |

---

## Marktinformationen für Deutschland

Für diesen Kandidaten sind derzeit keine Marktgenehmigungen im Bestand (`total_licenses: 0`, Marktstatus: Nicht vermarktet). Es sind keine Produkt-/Darreichungsform-/Indikationsdetails verfügbar.

---

## Sicherheitsaspekte

Formale Sicherheitsfelder (wichtigste Warnungen, Kontraindikationen, DDI-Datenbank) sind alle leer oder Datenlücken in diesem Paket, und kein TFDA/BfArM-Etikett wurde bisher abgerufen (siehe DG001, Blockierend).

**Arzneimittelwechselwirkungen in Studienevidenz vermerkt (nicht aus einer formalen DDI-Datenbank):**
- Pravastatin wird wiederholt als Statin mit niedriger CYP3A4-Abhängigkeit in Probe-Substrat-DDI-Studien verwendet (NCT04425902, NCT02578277), und seine PK wird durch OATP1B1/SLCO1B1-Transporter-Varianten beeinflusst, wenn es mit Darunavir/Ritonavir co-verabreicht wird (NCT00630734) und Raltegravir (NCT00665717) — besonders relevant für die in dieser Bewertung betrachtete HIV-Indikation.

> Für alle anderen Sicherheitsinformationen verweisen Sie bitte auf das Packungsetikett, wenn es verfügbar ist.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Fortschreiten mit Schutzmaßnahmen**

**Begründung:**
Mehrere dedizierte Phase-2–4-RCTs (einschließlich einer 630-Patienten-Phase-3-Studie) etablieren Pravastatin's Wirksamkeit und DDI-günstiges Profil für das Management von ART-assoziierter Dyslipidämie und kardiovaskulärem Risiko bei HIV-infizierten Patienten — ein genuines, evidenzgestütztes Repurposing-Signal, das sich von Pravastatin's bereits etablierten Statin-Indikationen unterscheidet (z. B. familiäre Hypercholesterinämie, Rang 6, was nicht neu ist). Die restlichen 7 von 9 TxGNN-Vorhersagen (L4–L5) ermangeln ausreichender klinischer oder mechanistischer Unterstützung und werden zurückgehalten.

**Um fortzufahren, wird Folgendes benötigt:**
- Offizielles Produktetikett / Warnungen und Kontraindikationen (DG001, Blockierend — TFDA/BfArM-PDF-Abruf)
- Bestätigte Dokumentation des Wirkmechanismus (DG002 — DrugBank-Abfrage)
- Formale DDI-Datenbankabfrage speziell für ART-Regime (Proteaseinhibitoren, Integrase-Inhibitoren)
- Klärung der Zielpopulation und des Endpunkts (ART-assoziierte Dyslipidämie/CV-Risikoreduktion, keine antivirale Wirkung)
- Bewertung des deutschen/EU-Zulassungsweges in Anbetracht des derzeitigen Status „Nicht vermarktet"

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

