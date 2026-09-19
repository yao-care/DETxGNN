---
layout: default
title: Aliskiren
parent: Nur Modellvorhersage (L5)
nav_order: 24
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Aliskiren: Von Hypertonie zu Pulmonaler Hypertonie aufgrund von Lungenerkrankung/Hypoxie

## Zusammenfassung in einem Satz

> Aliskiren ist ein direkter Reninhibitor, der ursprünglich zur Behandlung der essentiellen Hypertonie eingesetzt wird. Die höchste Vorhersage des TxGNN-Modells ist **Pulmonale Hypertonie aufgrund von Lungenerkrankung und/oder Hypoxie**, wird jedoch derzeit nur von **0 klinischen Studien** und **20 Publikationen** gestützt, von denen keine aliskiren, Reninhibition oder pulmonale Hypertonie spezifisch untersucht hat. Dieses Evidence Pack enthält tatsächlich **7 vorhergesagte Indikationen** für aliskiren mit stark unterschiedlicher Evidenzqualität — von einer mechanistisch direkten, aber untesteten Hypothese (renovaskuläre Hypertonie) bis hin zu einem gut untersuchten RCT-Signal, das eher auf **Schaden als auf Nutzen** hindeutet (zerebrovaskuläre Erkrankung, über die ALTITUDE-Studie).

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Hypertonie (essentielle Hypertonie) — Grundwissen der Arzneistoffklasse; kein formales Fachinformationstext ist verfügbar, da das Produkt in diesem Datensatz nicht in Deutschland vermarktet wird |
| Vorhergesagte neue Indikation | Pulmonale Hypertonie aufgrund von Lungenerkrankung und/oder Hypoxie |
| TxGNN-Vorhersagepunktzahl | 99.98% (Rang 466 aus der vollständigen Vorhersageliste) |
| Evidenzgrad | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

## Übersicht aller vorhergesagten Indikationen in diesem Pack

Dieses Kandidaten-Pack (`TW-DB09026-multi`) enthält 7 von TxGNN vorhergesagte Indikationen für aliskiren. Die Evidenzqualität unterscheidet sich erheblich zwischen ihnen und sollte eher zusammenhängend als isoliert gelesen werden:

| Rang | Vorhergesagte Indikation | TxGNN-Score | Evidenzgrad | Entscheidungsphase | Empfehlung |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Pulmonale Hypertonie aufgrund von Lungenerkrankung und/oder Hypoxie | 99.98% | L5 | S0 | Abwarten |
| 2 | Pulmonale Hypertonie mit unklar multifaktoriellem Mechanismus | 99.98% | L5 | S0 | Abwarten |
| 3 | Bösartige hypertensive Nierenschädigung | 99.98% | L4 | S0 | Abwarten |
| 4 | Bösartige renovaskuläre Hypertonie | 99.98% | L3 | S1 | Forschungsfrage |
| 5 | Braddock-Syndrom | 99.97% | L5 | S0 | Abwarten |
| 6 | Chronische pulmonale Herzerkrankung (Cor pulmonale) | 99.78% | L5 | S0 | Abwarten |
| 7 | Zerebrovaskuläre Erkrankung | 99.19% | **L1** | S1 | Abwarten — **RCT-Evidenz zeigt Schaden, nicht Nutzen** |

Zu beachten ist, dass der reine TxGNN-Score hier nicht diskriminierend ist — alle 7 Kandidaten erreichen über 99 %. Der eigentliche Unterschied liegt in der Evidenzanalyse unten, insbesondere Rang 7, wo die stärkste klinische Studienbeweise im gesamten Pack (Phase-3-RCT, ALTITUDE) *gegen* Umwidmung sprechen statt dafür.

## Warum ist diese Vorhersage vernünftig?

Detaillierte Wirkmechanismus-Daten für aliskiren sind in diesem Evidence Pack nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der in diesem Pack erfassten Literatur (z. B. PMID 17485026, „Aliskiren, der erste Reninhibitor zur Behandlung von Hypertonie") ist aliskiren ein **direkter Reninhibitor der ersten Klasse**: Er blockiert den geschwindigkeitsbestimmenden Schritt des Renin-Angiotensin-Aldosteron-Systems (RAAS), und seine Wirksamkeit bei essentieller Hypertonie ist gut etabliert.

Die 7 oben vorhergesagten Indikationen clustern um Bedingungen, bei denen eine RAAS-Überaktivierung eine Rolle spielen soll — renale, pulmonalvaskuläre und zerebrovaskuläre Pathologie. Die mechanistische Plausibilität ist jedoch keineswegs einheitlich:

- **Am direktesten** (Rang 4, bösartige renovaskuläre Hypertonie): Nierenarterien-Stenose-getriebene Hypertonie ist pathophysiologisch durch übermäßige Reninsekretion der unterversorgten Niere definiert, daher zielt ein Reninhibitor direkt auf den vorgelagerten Treiber ab. Die eine stützende Referenz (PMID 17485026) ist arzneistoffspezifisch, warnt aber auch, dass *reaktive* Reninsekretion die langfristige antihypertensive Wirkung von aliskiren genau in dieser Situation abschwächen kann.
- **Plausibel aber indirekt** (Rang 3, bösartige hypertensive Nierenschädigung; Rang 6, chronische pulmonale Herzerkrankung): RAAS-Aktivierung ist ein anerkannter Beitrag zu glomerulären Druckverletzungen und zu Rechtsherzvolumenbelastung, aber die zitierte Literatur ist nicht aliskiren-spezifisch (eine Komplementpfad-Fibrose-Studie und eine ARNI-Herzinsuffizienz-Post-hoc-Analyse mit einer anderen Arzneistoffklasse).
- **Schwach/generisch** (Ränge 1–2, hypoxie-getriebene pulmonale Hypertonie): Hypoxie-induziertes pulmonales vaskuläres Remodeling beinhaltet RAAS-Signalisierung in einigen präklinischen Berichten, daher ist die Hypothese grundsätzlich nicht implausibel. Allerdings sind alle 20 abgerufenen Publikationen allgemeine Hypoxie-Biologie-Arbeiten (Neurodegeneration, Kognition, Tumorstoffwechsel, Höhenphysiologie) — **keine erwähnen aliskiren, Reninhibitoren oder Pulmonalhypertonie-Behandlung**, daher ist dieser Link derzeit spekulativ statt nachgewiesen.
- **Wahrscheinlich Rauschen** (Rang 5, Braddock-Syndrom): Eine CHARGE-ähnliche Ziliopathie ohne bekannte RAAS-/Renin-Biologie und ohne Unterstützungsliteratur oder Studien — am wahrscheinlichsten eine spurlose Wissensgraph-Verbindung über einen gemeinsamen Hypertonie-Komorbiditätsknoten.
- **Nachgewiesen, aber negativ** (Rang 7, zerebrovaskuläre Erkrankung): Dies ist der einzige Kandidat mit echten Phase-2/3-RCT-Daten (ALTITUDE-Studie und ihre Post-hoc-Analysen). Die Studie wurde frühzeitig beendet, weil aliskiren, wenn es in Kombination mit ACE-Hemmern oder ARBs bei diabetischen Patienten mit Nierenfunktionsstörung gegeben wurde, **erhöhte** Raten von Schlaganfall, Hypotonie und Hyperkaliämie statt neuroprotektiver Wirkung zeigte — trotz günstiger präklinischer (Nager-)Neuroprotektions-Daten.

## Evidenz aus klinischen Studien

Nur zwei der sieben Kandidaten-Indikationen haben registrierte Studien.

**Chronische pulmonale Herzerkrankung (Rang 6):**

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Abgeschlossen | 19 | Apotheker-geleitetes, datengestütztes Verschreibungssicherheits-QI-Programm in der Primärversorgung (Schottland). Grad-C-Relevanz — kein direkter Bezug zur aliskiren-Pharmakologie oder dieser Indikation; wahrscheinlich eine niedrig-Relevanz-Pipeline-Übereinstimmung. |

**Zerebrovaskuläre Erkrankung (Rang 7):**

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT01417104](https://clinicaltrials.gov/study/NCT01417104) | Phase 2/3 | **Beendet** | 71 | ALPINE-Studie: aliskiren vs. Placebo zur Verlangsamung der atherosklerotischen Plaqueprogression in Aorta thoracalis/abdominalis durch MRT. Grad-A-Relevanz (arzneistoff- und mechanismusspezifisch) aber vorzeitig beendet, weit unter der angestrebten Rekrutierungszahl — der Zeitpunkt fällt mit dem ALTITUDE-Sicherheitssignal 2011–2012 zusammen, das Novartis veranlasste, verwandte aliskiren-Kombinationsstudien zu stoppen; der Beendigungsgrund sollte direkt überprüft werden. |
| [NCT01454583](https://clinicaltrials.gov/study/NCT01454583) | N/A | Abgeschlossen | 15,337 | Deutsches 3A-Register: großes Real-World-Observatories-Register von RAS-Inhibitor- (einschließlich aliskiren) Ambulanzbehandlungsmuster bei Hypertonie. Grad-B-Relevanz — Observationsdaten, nicht um zerebrovaskuläre Endpunkte herum entworfen. |

Für pulmonale Hypertonie (Ränge 1–2), bösartige hypertensive Nierenschädigung (Rang 3), bösartige renovaskuläre Hypertonie (Rang 4) und Braddock-Syndrom (Rang 5): **derzeit keine verwandten klinischen Studien registriert.**

## Evidenz aus der Literatur

### Zerebrovaskuläre Erkrankung (Rang 7) — stärkste und arzneistoffspezifischste Evidenz in diesem Pack

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [26523993](https://pubmed.ncbi.nlm.nih.gov/26523993/) | 2015 | RCT-Untergruppe (ALTITUDE/AQUARIUS) | Atherosclerosis | Aliskiren's Wirkung auf Koronaratherom-Progression und MACE bei diabetischen vs. nicht-diabetischen KHK-Patienten; verstärkt das Schaden-Signal bei diabetischer Bevölkerung. |
| [23418282](https://pubmed.ncbi.nlm.nih.gov/23418282/) | 2013 | RCT-Post-hoc-Sicherheitsanalyse | J Renin Angiotensin Aldosterone Syst | Hypotonie und ischämischer Schlaganfall assoziiert mit aliskiren in ALTITUDE, vorgeschlagener Mechanismus über Bezold-Jarisch-Reflex-Sensibilisierung. |
| [26188211](https://pubmed.ncbi.nlm.nih.gov/26188211/) | 2015 | RCT-Post-hoc (ALTITUDE) | European Heart Journal | Mortalität nach kardiovaskulärem oder renalen Ereignis bei T2DM-Patienten in ALTITUDE — etabliert die Hochrisiko-Population, in der aliskiren + ACEi/ARB schädlich ist. |
| [24621979](https://pubmed.ncbi.nlm.nih.gov/24621979/) | 2013 | Klinische Übersicht/Analyse | JACC: Heart Failure | Untersucht, ob duale RAAS-Blockade (einschließlich aliskiren-Kombinationen) mit erhöhtem Schlaganfallrisiko assoziiert ist. |
| [23541666](https://pubmed.ncbi.nlm.nih.gov/23541666/) | 2013 | Real-World-Datenbankstudien | Canadian J Cardiology | Ontario-Verwaltungsdaten-Studie fand **keine** Zunahme unerwünschter Ereignisse mit aliskiren + ACEi/ARB in der Routinepraxis — bietet ein teilweise beruhigendes, kontrastierendes Real-World-Signal zu den RCT-Ergebnissen. |
| [40013543](https://pubmed.ncbi.nlm.nih.gov/40013543/) | 2025 | Cochrane-Systematische-Übersicht/Meta-Analyse | Cochrane Database Syst Rev | Reninhibitoren vs. ARBs für primäre Hypertonie — vergleichbare Blutdruck-Senkung, günstige Verträglichkeit, aber nicht auf zerebrovaskuläre Ergebnisse ausgerichtet. |
| [37439548](https://pubmed.ncbi.nlm.nih.gov/37439548/) | 2023 | Cochrane-Systematische-Übersicht | Cochrane Database Syst Rev | First-Line-Diuretika vs. andere antihypertensive Klassen — allgemeiner Comparative-Effectiveness-Kontext, nicht aliskiren-spezifisch. |
| [23541659](https://pubmed.ncbi.nlm.nih.gov/23541659/) | 2013 | Übersicht | Canadian J Cardiology | Kombinationsbehandlung mit aliskiren und RAAS-Blockern — „Beruhigung aber mit einer Note der Vorsicht", Kommentar antizipierend die ALTITUDE-Ergebnisse. |
| [21859961](https://pubmed.ncbi.nlm.nih.gov/21859961/) | 2011 | Präklinisch (Mausmodell) | Hypertension | Direkte Reninhibition verringerte Gehirnschäden und kognitive Beeinträchtigung bei chronischer zerebraler Hypoperfusion bei Mäusen — stützendes mechanistisches/präklinisches Signal, widersprochen durch spätere menschliche RCT-Daten. |
| [27180190](https://pubmed.ncbi.nlm.nih.gov/27180190/) | 2016 | Präklinisch (Mausmodell) | Neurochemical Research | Aliskiren zeigte neuroprotektive Effekte (PI3K/AKT/Bcl-2-Pfad) in experimentellem ischämischem Schlaganfall — wiederum nur präklinisch. |

### Pulmonale Hypertonie aufgrund von Lungenerkrankung und/oder Hypoxie (Rang 1) — nicht-arzneistoffspezifische Hypoxie-Biologie-Literatur

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Übersicht | Ageing Research Reviews | Allgemeine Übersicht der Rolle der Hypoxie bei Gehirnalterung und Neurodegeneration; nicht aliskiren- oder Pulmonalhypertonie-spezifisch. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Übersicht | Metabolic Brain Disease | Klinische und molekulare Mechanismen der hypoxie-induzierten kognitiven Beeinträchtigung. |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Übersicht | J Cellular Biochemistry | Allgemeine hypoxie-vermittelte biologische Kontrolle über Organsysteme. |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Übersicht | Clinical Oncology | Therapeutische Modifikation von Tumorhypoxie in der Onkologie; unabhängig von Pulmonalvaskulärerkrankung. |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Übersicht | Trends in Cancer | Deubiquitinasen und Hypoxie-Signalisierung bei Krebs. |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Übersicht | Respiratory Care Clinics of North America | Mechanismen der Hypoxämie (Ventilations-Perfusions-Mismatch, Shunt, etc.) — reine Hintergrund-Atemwegsphysiologie. |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Übersicht | Rev Med Inst Mex Seguro Soc | Hypoxie in Höhenlage und physiologische Anpassung. |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Übersicht | Redox Biology | Rolle der Hypoxie bei der Pathologie der Multiplen Sklerose. |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Präklinisch | Advanced Science | ac4C/NAT10/HIF-1α-Rückkopplungsschleife treibt Glykolyse in Magenkrebs unter Hypoxie. |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Leitartikel | J Applied Physiology | Kurzes Leitartikel zu Hypoxie-Forschung („Übersetzung im Gange"); kein Abstract verfügbar. |

**Keine dieser 10 (oder der verbleibenden 10 in der vollständigen Abrufsatz) diskutiert aliskiren, Reninhibition oder Pulmonalhypertonie-Behandlung.** Dies ist die Schlüsselbeschränkung hinter der L5/Abwarten-Bewertung für Ränge 1–2.

### Bösartige hypertensive Nierenschädigung (Rang 3)

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [37919077](https://pubmed.ncbi.nlm.nih.gov/37919077/) | 2023 | Präklinisch (Mechanismus-Studie) | Frontiers in Bioscience | C3aR-Antagonismus stellt mitochondriale Fettsäure-Oxidation wieder her und reduziert tubuläre profibriotische Veränderungen bei renin-abhängiger Hypertonie — eine Komplementpfad-Mechanismus-Studie, keine aliskiren-Effektivitätsstudie. |

### Bösartige renovaskuläre Hypertonie (Rang 4)

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [17485026](https://pubmed.ncbi.nlm.nih.gov/17485026/) | 2007 | Arzneistoffspezifische Pharmakologie-Übersicht | American Journal of Hypertension | Übersicht von 6 klinischen Studien (>5,000 Patienten) — aliskiren ist nicht wirksamer als ACEi/ARB/Diuretika bei Blutdrucksenkung; warnt, dass reaktive Reninsekretion die langfristige Wirksamkeit begrenzen kann, direkt relevant für die renovaskuläre-Hypertonie-Hypothese. |

### Chronische pulmonale Herzerkrankung (Rang 6)

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [39210725](https://pubmed.ncbi.nlm.nih.gov/39210725/) | 2024 | RCT-Post-hoc | JAMA Cardiology | Sacubitril/Valsartan (ARNI — eine andere Arzneistoffklasse) Wirkung auf alle-Ursachen-Hospitalisierung bei Herzinsuffizienz (PARADIGM-HF/PARAGON-HF); keine Reninhibitor-Studie. |
| [17890152](https://pubmed.ncbi.nlm.nih.gov/17890152/) | 2007 | Konferenz-Übersicht | European Journal of Heart Failure | ESC-2007-Herzinsuffizienz-Studienübersicht (3CPO, ALOFT, PROSPECT, Statine); nur allgemeiner Hintergrund. |

## Marktinformationen für Deutschland

Aliskiren wird derzeit **nicht in Deutschland vermarktet** nach diesem Datensatz (`market_status: Not marketed`, `total_licenses: 0`). Es sind keine Marketingzulassungsunterlagen verfügbar zum Zusammenfassen.

## Sicherheitserwägungen

Bitte beziehen Sie sich auf die Packungsbeilage für Sicherheitsinformationen — die strukturierten Sicherheitsfelder in diesem Evidence Pack (`key_warnings`, `contraindications`, `ddi`) sind alle als Datenlücken gekennzeichnet, und der TFDA/BfArM-Packungsbeilage ist noch nicht abgerufen worden (siehe `DG001`, Blocking).

**⚠️ Wichtiges Sicherheitssignal aus der Literaturevidenz identifiziert (nicht aus den formalen Sicherheitsdatenfeldern oben):** Mehrere abgerufene Publikationen für den zerebrovaskulären-Erkrankung-Kandidaten (Rang 7) verweisen auf die **ALTITUDE-Studie**, eine Phase-3-RCT, die **frühzeitig beendet** wurde, weil aliskiren, wenn kombiniert mit einem ACE-Hemmer oder ARB bei Patienten mit Typ-2-Diabetes und Nierenfunktionsstörung, signifikant erhöhte Raten von Schlaganfall, Hypotonie und Hyperkaliämie verursachte (PMID 23418282, 26188211, 26523993). Dies ist ein gut dokumentiertes, arzneistoffspezifisches Schaden-Signal und sollte als harte Beschränkung auf jede Umwidmungsarbeit bei Patienten mit Nieren- oder kardiovaskulären Komorbiditäten behandelt werden, bis die formalen Packungsbeilage-Warnungen abgerufen und überprüft werden.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten** (Top-Ranking-Kandidat, und Programm-Standard bei Erwartung weiterer Daten)

**Begründung:**
- Die im Mittelpunkt stehende Top-Vorhersage (pulmonale Hypertonie aufgrund von Lungenerkrankung/Hypoxie) hat keine aliskiren-spezifische klinische Studien- oder Literaturunterstützung (L5) — der TxGNN-Score allein reicht nicht aus, um voranzukommen.
- Über alle 7 Kandidaten in diesem Pack hinweg hat nur **bösartige renovaskuläre Hypertonie (Rang 4)** eine mechanistisch direkte, arzneistoffspezifische Rationale und ist **Forschungsfrage** statt Abwarten — aber auch dort warnt die Literatur selbst, dass reaktive Reninsekretion die Wirksamkeit von aliskiren begrenzen kann.
- Der Kandidat mit der stärksten klinischen Evidenz, **zerebrovaskuläre Erkrankung (Rang 7, L1)**, sollte **nicht** verfolgt werden: Die Phase-3-RCT-Evidenz (ALTITUDE) zeigt erhöhte Schlaganfall- und Nierenschäden bei der relevanten Patientenpopulation, nicht Nutzen.
- Eine Blocking-Datenlücke besteht (`DG001`): TFDA/BfArM-Packungsbeilage-Warnungen und Kontraindikationen sind nicht abgerufen worden, daher kann kein Kandidat unabhängig von der Effektivitäts-Evidenz die anfängliche Sicherheitsprüfung (S1) überschreiten.

**Um voranzukommen, ist folgendes erforderlich:**
- TFDA/BfArM-Packungsbeilage (Warnungen, Kontraindikationen) abrufen und analysieren — derzeit Blocking (`DG001`)
- Bestätigte Wirkmechanismus-Daten von DrugBank abrufen (`DG002`), um die mechanistischen Rationale-Abschnitte oben zu stärken
- Falls Rang 4 (bösartige renovaskuläre Hypertonie) als Forschungsfrage verfolgt wird, eine gezielte Literatur-/Studienbasis von dieser Indikation spezifisch in Auftrag geben (aktuelle Wissensbasis ist eine einzelne 2007-Übersicht)
- Beendigungsgrund für NCT01417104 (ALPINE) überprüfen, um zu bestätigen, ob es sich auf das ALTITUDE-Sicherheitssignal bezieht
- Rang 7 (zerebrovaskuläre Erkrankung) als geschlossen/Nicht-Verfolgen behandeln, bis neue Evidenz auftaucht, die die ALTITUDE-Ergebnisse umkehrt
- Rang 2 (keine Evidenz) und Rang 5 (Braddock-Syndrom, biologisch implausibel) als wahrscheinliche Wissensgraph-Rauschen ignorieren, es sei denn, es taucht neue Evidenz auf

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

