---
layout: default
title: Efavirenz
parent: Mittlere Evidenz (L3-L4)
nav_order: 135
evidence_level: L3
indication_count: 3
---

# Efavirenz
{: .fs-9 }

Evidenzniveau: **L3** | Vorhergesagte Indikationen: **3** 
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

# Efavirenz: Von der HIV-1-Infektion zur Simian-Immunodeficiency-Virus-Infektion

## Zusammenfassung in einem Satz

Efavirenz ist ein Nicht-Nukleosid-Reverse-Transkriptase-Hemmer (NNRTI), ursprünglich für die HIV-1-Infektion entwickelt (basierend auf allgemeinem pharmakologischen Wissen; keine verifizierte BfArM-Kennzeichnung liegt in diesem Evidence Pack vor).
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam für **Simian-Immunodeficiency-Virus-Infektion (SIV-Infektion)** ist,
aber dieses Signal wird nur durch **1 klinische Studie (anderes Arzneimittel, zurückgezogen)** und **14 Publikationen, alle präklinische Makaken-Modellstudien** unterstützt – die Evidenz ist schwach und beschreibt größtenteils keine klinische Indikation beim Menschen.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar in diesem Evidence Pack – keine BfArM-Zulassung dokumentiert (0 Lizenzen); Efavirenz ist allgemein als HIV-1-NNRTI bekannt, dies wird hier jedoch nicht durch regulatorische Daten bestätigt |
| Vorhergesagte neue Indikation | Simian-Immunodeficiency-Virus-Infektion |
| TxGNN-Vorhersage-Score | 99.80% |
| Evidenzstufe | L3 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Pausieren |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (gekennzeichnet als Datenlücke DG002, hoher Schweregrad). Basierend auf allgemeinem pharmakologischen Wissen ist Efavirenz ein NNRTI, der die HIV-1-Reverse-Transkriptase blockiert; seine Wirksamkeit bei der HIV-1-Infektion ist in der Literatur gut belegt, konnte jedoch in diesem Pack nicht anhand strukturierter DrugBank-Daten verifiziert werden.

Die vorhergesagte „neue Indikation" – SIV-Infektion – ist keine natürlich auftretende menschliche Krankheit. Sie bezieht sich auf ein Labormodell: Forscher haben ein chimärisches Virus (RT-SHIV) entwickelt, indem sie das SIV-Reverse-Transkriptase-Gen durch das HIV-1-Reverse-Transkriptase-Gen ersetzt haben, wodurch es anfällig für NNRTIs wie Efavirenz in Rhesus-Makaken wird. Dies ermöglicht es Efavirenz, die Viruslast bei RT-SHIV-infizierten Makaken zu unterdrücken (z. B. PMID 15919889, 19889213), was fast sicher die Quelle der TxGNN-Assoziation ist. Natürliches, nicht-gentechnisch verändertes SIV ist von Natur aus resistent gegen Efavirenz, da sich die Wildtyp-SIV-Reverse-Transkriptase strukturell von der HIV-1-RT unterscheidet.

Dies bedeutet, dass die mechanistische Verbindung real ist, aber eng gefasst: Sie gilt nur für ein gentechnisch verändertes Laborwerkzeug, das zur Untersuchung der HIV-Pharmakokinetik und Arzneimittelresistenz bei nichtmenschlichen Primaten verwendet wird, nicht für eine echte neue therapeutische Indikation beim Menschen (oder bei Tieren). Rang 2 (Feline-AIDS) hat eine ähnliche Einschränkung – die FIV-Reverse-Transkriptase unterscheidet sich wesentlich von der HIV-1-RT, und humane NNRTIs einschließlich Efavirenz zeigen schwache Aktivität gegen Wildtyp-FIV. Rang 3 (eine seltene neurodevelopmentale Störung im Kindesalter) hat keine mechanistische Begründung und keine unterstützenden Belege, während Efavirenz mit bekannten ZNS-bezogenen Risiken (Schwindel, abnorme Träume, Suizidgedanken) verbunden ist, die bei dieser Population Bedenken aufwerfen würden.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Zurückgezogen | 0 | Untersuchte HIV-Virusdauer-Kinetik mit **Raltegravir** (ein Integrase-Hemmer), nicht Efavirenz; die Vergleichsgruppe verwies nur auf SIV-infizierte Makaken-Dauer-Kinetik als Hintergrund. Die Studie wurde zurückgezogen (Teilnehmerzahl 0) und wird bewertet mit **C (niedrige Relevanz)** – das Arzneimittel und die Studienpopulation entsprechen nicht diesem Kandidaten. |

*Es wurden keine Studien gefunden, die Efavirenz bei SIV-Infektion direkt evaluieren.*

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Kohorte (präklinisch) | Antimicrob Agents Chemother | Erste Demonstration, dass Efavirenz die RT-SHIV-Replikation (chimäres SIV mit HIV-1-RT) in Rhesus-Makaken unterdrückt |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Kohorte (präklinisch) | J Virol | Efavirenz + Lamivudin + Tenofovir-Kombination unterdrückte RT-SHIV-Viruslast bei Makaken, modelliert humane HAART |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Kohorte (präklinisch) | Retrovirology | Efavirenz-Monotherapie mit kurzer Dauer gefolgt von Kombinationstherapie bei RT-SHIV-infizierten Makaken; Verfolgung der Dynamik viraler Subpopulationen |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Übersicht/Kohorte | J Virol | Efavirenz-Monotherapie bei Schweinehals-Makaken vor Kombinationstherapie; genetische Vielfalt von RT-SHIV blieb trotz Behandlung bestehen |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Kohorte (präklinisch) | Antimicrob Agents Chemother | Verbesserte 4–5-Wirkstoff-ART-Regime (im Kontext werden Efavirenz-basierte Modelle berücksichtigt) verbesserten die RT-SHIV-Dauer-Kinetik bei Makaken |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Präklinisch | PLoS One | Charakterisierte virale Dauer-Kinetik im mit HAART behandelten RT-SHIV-Makaken-Modell des AIDS |
| [26559632](https://pubmed.ncbi.nlm.nih.gov/26559632/) | 2015 | Präklinisch | Retrovirology | Analyse der Plasma- und Gewebe-Viruspopulation bei RT-SHIV-Makaken unter ART deutet darauf hin, dass keine Residualreplikation im Gewebe auftritt |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Präklinisch | J Virol | Identifizierte virale Rückzugsorte, die während HAART im RT-SHIV-Nichtmenschliches-Primat-AIDS-Modell persistieren |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | In vitro | J Virol | Ultrasensitive PCR detektierte seltene präexistierende arzneimittelresistente RT-SHIV-Varianten bei Makaken vor ART |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | In vitro/Bildgebung | Antimicrob Agents Chemother | Massenspektrometrie-Bildgebung kartierte Antiretrovirale-Arzneimittelverteilung und Residual-RT-SHIV-RNA im Makaken-Milzgewebe |

**Anmerkung:** Die gesamte identifizierte Literatur beschreibt das gentechnisch veränderte RT-SHIV-Makaken-Forschungsmodell, das zur Untersuchung der menschlichen HIV-1-Pharmakologie und Resistenz verwendet wird – keine beschreibt die Behandlung von natürlich auftretender SIV-Infektion als Krankheitsziel.

---

## Informationen zum Markt Deutschland

Efavirenz besitzt derzeit **keine dokumentierte Marktgenehmigung** in diesem Evidence Pack (0 Lizenzen; Marktstatus: nicht vermarktet). Der BfArM-Labelinhalt (Warnhinweise, Kontraindikationen, zugelassene Indikationen) konnte nicht abgerufen werden und wird als **Datenlücke DG001 (blockierend)** dokumentiert.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Strukturierte Warnhinweise, Kontraindikations- und Arzneimittelwechselwirkungsdaten (TFDA/BfArM-Labeltext) sind derzeit für Efavirenz in diesem Evidence Pack nicht verfügbar – der Abruf der offiziellen Label-PDF ist als Datenlücke DG001 (blockierend) dokumentiert, was derzeit einen vollständigen S1-Sicherheitsreview verhindert.

---

## Fazit und nächste Schritte

**Entscheidung: Pausieren**

**Begründung:**
Die höchstrangige vorhergesagte Indikation (SIV-Infektion) spiegelt ein gentechnisch verändertes Laborforschungsmodell (RT-SHIV bei Makaken) wider, nicht ein echtes behandelbares Krankheitsziel; die einzige zugehörige klinische Studie ist unabhängig und zurückgezogen; und sowohl Regulierungssicherheitsdaten (DG001, blockierend) als auch Wirkmechanismus-Daten (DG002, hoch) fehlen, wodurch ein Fortschritt über S0 hinaus verhindert wird.

**Für einen Fortschritt ist folgendes erforderlich:**
- Abruf und Analyse der offiziellen TFDA/BfArM-Label-PDF für Warnhinweise und Kontraindikationen (DG001)
- Abfrage von DrugBank (oder gleichwertig) zur Bestätigung und Dokumentation des Efavirenz-Wirkmechanismus (DG002)
- Klärung mit der TxGNN/Evidence-Pipeline, ob „Simian-Immunodeficiency-Virus-Infektion" als nicht-menschlicher, nur Modell-relevanter Knoten ausgeschlossen werden sollte, da er kein verwertbares Repurposing-Ziel darstellt
- Erneute Überprüfung der Ränge 2 (Feline-AIDS – Veterinärmedizin, nicht humanmedizinisch) und 3 (ultra-seltene neurodevelopmentale Störung im Kindesalter – keine Evidenz, potenzieller ZNS-Sicherheitskonflikt) vor Erwägung einer weiteren Evaluierung dieses Kandidatensatzes

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

