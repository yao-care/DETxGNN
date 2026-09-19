---
layout: default
title: Iron
parent: Hohe Evidenz (L1-L2)
nav_order: 213
evidence_level: L2
indication_count: 6
---

# Iron
{: .fs-9 }

Evidenzniveau: **L2** | Vorhergesagte Indikationen: **6** 
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

# Eisen (Iron, DB01592): Von einer nicht dokumentierten ursprünglichen Indikation zu eisenmangelbedingten Erkrankungen

## Zusammenfassung in einem Satz

Dieses Evidenzpaket enthält keine bestätigte ursprüngliche Indikation, keinen Wirkmechanismus und keine deutsche Marktzulassung für Eisen (DrugBank-ID DB01592) — der Wirkstoff ist derzeit in Deutschland **nicht vermarktet**, mit 0 erfassten Zulassungen. TxGNN generierte **sechs** Kandidatenindikationen; nach Evidenzprüfung sind nur zwei klinisch schlüssige Erweiterungen der bekannten Rolle von Eisen bei der Korrektur von Eisenmangel — **Vitamin-/Mineralstoffmangelerkrankung** (L2-Evidenz, mehrere abgeschlossene Phase-2–4-RCTs) und **Plummer-Vinson-Syndrom** (L4-Evidenz, 20 unterstützende Publikationen) —, während den übrigen vier Kandidaten die mechanistische Plausibilität fehlt und sie als wahrscheinliches Vorhersagerauschen markiert werden.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | In diesem Evidenzpaket nicht dokumentiert (Datenlücke) |
| Vorhergesagte neue Indikation (primär) | Vitamin-/Mineralstoffmangelerkrankung (d. h. Korrektur von Eisenmangel) |
| Vorhergesagte neue Indikation (sekundär) | Plummer-Vinson-Syndrom |
| TxGNN-Vorhersage-Score (primär) | 99.68% |
| TxGNN-Vorhersage-Score (sekundär) | 99.89% |
| Evidenzgrad (primär) | L2 |
| Evidenzgrad (sekundär) | L4 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Mit Leitplanken fortfahren (nur eisenmangelbedingte Indikationen) |

### Alle sechs Kandidaten im Überblick

| Rang | Vorhergesagte Indikation | Score | Evidenzgrad | Entscheidungsstufe | Empfehlung | Anmerkung |
|---|---|---|---|---|---|---|
| 1 | Vitamin-B12-/Folat-unabhängige megaloblastäre Anämie | 99.89% | L5 | S0 | Zurückstellen | Keine Studien oder Literatur vorhanden; die TxGNN-Begründung weist dies als wahrscheinlich falsche semantische Assoziation über „Anämie" aus — Eisen hat keinen bekannten Mechanismus, um diese genetische Erkrankung zu korrigieren |
| 2 | **Plummer-Vinson-Syndrom** | 99.89% | L4 | S2 | **Mit Leitplanken fortfahren** | 20 unterstützende Publikationen; Eisenmangel ist die etablierte Ätiologie dieses Syndroms |
| 3 | Nicht-syndromale ösophageale Fehlbildung | 99.86% | L5 | S0 | Zurückstellen | Struktureller angeborener Defekt; keine Evidenz, kein plausibler Mechanismus |
| 4 | Biotin-Stoffwechselerkrankung | 99.74% | L4 | S0 | Zurückstellen | Die zitierten Studien sind generische Multi-Mikronährstoff-Studien (überwiegend mit Relevanzgrad C bewertet), nicht spezifisch für die Biotin-Erkrankung |
| 5 | **Vitaminmangelerkrankung** | 99.68% | L2 | S2 | **Mit Leitplanken fortfahren** | Stärkste Evidenzbasis aller sechs Kandidaten; zu beachten ist, dass die Krankheitsbezeichnung eine Ontologie-Diskrepanz darstellt (Eisen ist ein Mineralstoff, kein Vitamin) |
| 6 | Ösophaguserkrankung | 99.42% | L4 | S1 | Forschungsfrage | Gemischte Evidenzlage; nur eisenmangelassoziierte ösophageale Subtypen (z. B. Schleimhautstege) sind relevant |

---

## Warum sind diese Vorhersagen plausibel?

Derzeit liegen für diesen Wirkstoffeintrag keine detaillierten Daten zum Wirkmechanismus vor. Nach bekanntem Kenntnisstand ist Eisen (DB01592) ein essenzielles Spurenelement, das in zahlreichen Arzneiformen zur Korrektur von Eisenmangel und Eisenmangelanämie eingesetzt wird; seine zentrale Rolle liegt in der Hämoglobinsynthese, dem Sauerstofftransport und der Funktion als mitochondrialer/enzymatischer Kofaktor.

Die beiden evidenzgestützten Kandidaten stellen keine wirklich „neuartigen" Indikationen dar, sondern vielmehr **direkte Erweiterungen der bereits etablierten therapeutischen Rolle von Eisen**:

- **Vitamin-/Mineralstoffmangelerkrankung**: Die klinische Studienevidenz (Schwangerschaft, Herzinsuffizienz mit reduzierter Ejektionsfraktion, nach bariatrischer Chirurgie, pädiatrisches Wachstum, ungeklärte Anämie im Alter) untersucht durchgängig die Eisensupplementierung zur Korrektur eines messbaren Eisenmangels. Die Bezeichnung „Vitamin" ist ein taxonomisches Artefakt der von TxGNN verwendeten Krankheitsontologie — Eisenmangel ist ein Mineralstoffmangel, kein Vitaminmangel —, aber das zugrunde liegende klinische Signal ist real und mechanistisch direkt.

- **Plummer-Vinson-Syndrom**: Die Kernpathophysiologie dieser seltenen Erkrankung (Dysphagie, ösophagealer Schleimhautsteg, Eisenmangelanämie) wird *durch* chronischen Eisenmangel *verursacht*, und die Eisensubstitution ist bereits Standardtherapie, die in den zitierten Fallserien und Übersichtsarbeiten Symptome und Schleimhautstege nachweislich zur Rückbildung bringt. Dies ist weniger eine „neue Hypothese" als vielmehr eine Bestätigung, dass TxGNN eine gut etablierte klinische Beziehung korrekt erfasst hat.

Im Gegensatz dazu zeigen Kandidaten wie die megaloblastäre Anämie (B12-/Folat-unabhängig, d. h. nicht durch Eisenmangel verursacht), die nicht-syndromale ösophageale Fehlbildung (ein struktureller angeborener Defekt) und die Biotin-Stoffwechselerkrankung keine mechanistische Überschneidung mit dem Eisenstoffwechsel, und ihre unterstützende „Evidenz" besteht aus generisch verwandten Multi-Mikronährstoff-Studien statt aus krankheitsspezifischen Daten — im Einklang mit der eigenen Einschätzung der Scoring-Engine, dass es sich hierbei eher um Artefakte semantischer Ähnlichkeit im zugrunde liegenden Wissensgraphen als um ein echtes biologisches Signal handelt.

---

## Klinische Studienevidenz (Primärer Kandidat: Vitamin-/Mineralstoffmangelerkrankung)

| Studiennummer | Phase | Status | Teilnehmerzahl | Wesentliche Ergebnisse |
|---------|------|------|------|---------|
| [NCT01953107](https://clinicaltrials.gov/study/NCT01953107) | Phase 4 | Abgeschlossen | 200 | Präoperatives Eisen(II)-fumarat 300mg vs. Placebo bei neu diagnostizierten gynäkologisch-onkologischen Patientinnen |
| [NCT01904864](https://clinicaltrials.gov/study/NCT01904864) | Phase 4 | Abgeschlossen | 80 | NovaFerrum® vs. Eisen(II)-sulfat zur Behandlung der nutritiven Eisenmangelanämie bei Säuglingen/Kleinkindern |
| [NCT04764955](https://clinicaltrials.gov/study/NCT04764955) | Phase 3 | Abgeschlossen | 1,300 | Wirkung der mütterlichen Vitamin-D3-Supplementierung auf den Eisenstatus während Schwangerschaft und früher Säuglingszeit |
| [NCT03079518](https://clinicaltrials.gov/study/NCT03079518) | Phase 2 | Abgeschlossen | 23 | Wirkung einer einmaligen hochdosierten Ferric-Carboxymaltose-Infusion auf FGF23/Phosphatstoffwechsel bei HFrEF mit Eisenmangel |
| [NCT05185024](https://clinicaltrials.gov/study/NCT05185024) | N/A | Abgeschlossen | 152 | Wirksamkeit/Sicherheit von drei oralen eisenhaltigen Nahrungsergänzungsmitteln zur Korrektur hämatologischer Indizes bei eisenmangelbetroffenen Erwachsenen |
| [NCT01609387](https://clinicaltrials.gov/study/NCT01609387) | Phase 4 | Abgeschlossen | 300 | Doppelblinde RCT zur postoperativen Vitamin-/Mineralstoffsupplementierung bei morbid adipösen Patienten |
| [NCT03247816](https://clinicaltrials.gov/study/NCT03247816) | N/A | Abgeschlossen | 59 | Real-World-Wirksamkeit von Eisen(III)-Maltol (Feraccru®) bei Eisenmangelanämie bei CED-Patienten |
| [NCT01572506](https://clinicaltrials.gov/study/NCT01572506) | Phase 1 | Abgeschlossen | 58 | Mechanistische Studie zur ungeklärten Anämie im Alter (Erythrozytenlebensdauer, eisenbezogen) |
| [NCT04561635](https://clinicaltrials.gov/study/NCT04561635) | N/A | Abgeschlossen | 98 | Cluster-randomisierte Studie zur Multi-Mikronährstoffsupplementierung hinsichtlich Wachstum und Eisenstatus bei indigenen Kindern (Malaysia) |
| [NCT03762148](https://clinicaltrials.gov/study/NCT03762148) | N/A | Abgeschlossen | 46 | Dosisabhängige Wirkung von Galacto-Oligosacchariden (GOS) auf die Eisenresorption bei Frauen mit niedrigen Eisenspeichern |

*Hinweis: Für die Kandidaten Rang 1 (megaloblastäre Anämie), Rang 3 (ösophageale Fehlbildung) und Rang 2 (Plummer-Vinson-Syndrom) liegen in diesem Evidenzpaket derzeit keine registrierten klinischen Studien vor.*

---

## Literaturevidenz (Primärer Kandidat: Vitamin-/Mineralstoffmangelerkrankung)

| PMID | Jahr | Typ | Zeitschrift | Wesentliche Ergebnisse |
|------|-----|------|------|---------|
| [28034892](https://pubmed.ncbi.nlm.nih.gov/28034892/) | 2017 | Übersichtsarbeit (Tier 1) | Blood | Klinisches Management-Framework für Anämie in der Schwangerschaft mit Berücksichtigung von Eisen-, Cobalamin- und Folatmangel |
| [34534708](https://pubmed.ncbi.nlm.nih.gov/34534708/) | 2022 | Übersichtsarbeit (Tier 2) | Bone | Umfassende Übersicht zur Hypophosphatämie nach intravenöser Eisentherapie mit Managementempfehlungen |
| [10595751](https://pubmed.ncbi.nlm.nih.gov/10595751/) | 1999 | Übersichtsarbeit (Tier 2) | Seminars in Hematology | Überblick über nutritive Anämien mit Schwerpunkt auf Folat-, B12- und Eisenstoffwechsel |
| [1596590](https://pubmed.ncbi.nlm.nih.gov/1596590/) | 1992 | Übersichtsarbeit (Tier 2) | Bailliere's Clinical Haematology | Globale Public-Health-Perspektive auf nutritive Anämie, Eisenmangel als Hauptursache |
| [7603852](https://pubmed.ncbi.nlm.nih.gov/7603852/) | 1995 | Übersichtsarbeit (Tier 2) | Nursing Times | Klinische Testprotokolle für Eisen-, B12- und Folatmangel |
| [39667365](https://pubmed.ncbi.nlm.nih.gov/39667365/) | 2025 | Übersichtsarbeit | Nutrition Reviews | Historische und mechanistische Übersicht über den Einfluss von Vitamin-A-Mangel auf den Eisenstoffwechsel |
| [35163110](https://pubmed.ncbi.nlm.nih.gov/35163110/) | 2022 | Systemübersicht | Int J Mol Sci | Systembiologische Analyse der Wechselbeziehungen zwischen Eisen- und Vitamin-A-Status |
| [31256475](https://pubmed.ncbi.nlm.nih.gov/31256475/) | 2019 | Übersichtsarbeit | Australian Journal of General Practice | Leitfaden für das hausärztliche Management der Anämie in der Schwangerschaft |
| [35807896](https://pubmed.ncbi.nlm.nih.gov/35807896/) | 2022 | Narrative Übersichtsarbeit | Nutrients | Kombinierte Rolle von Vitamin-D- und Eisenstatus für Skelettmuskelmasse, -kraft und -funktion |
| [24998947](https://pubmed.ncbi.nlm.nih.gov/24998947/) | 2014 | Grundlagenforschung | J Nutr Biochem | Tierstudie zeigt, dass Vitamin-A-Mangel den Eisenstoffwechsel über ineffektive Erythropoese moduliert |

---

## Zusätzliche Evidenz: Plummer-Vinson-Syndrom (Sekundärer Kandidat, L4)

Für diese Indikation sind keine klinischen Studien registriert, jedoch ist die Literaturbasis umfangreich (20 Publikationen) und klinisch gut etabliert. Repräsentative Zitate:

| PMID | Jahr | Typ | Zeitschrift | Wesentliche Ergebnisse |
|------|-----|------|------|---------|
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Übersichtsarbeit | Journal of Blood Medicine | Aktuelle Erkenntnisse zu Eisenmangelanämie und Plummer-Vinson-Syndrom (PVS); Eisenmangel ist zentral für die Pathogenese |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Übersichtsarbeit | Orphanet Journal of Rare Diseases | Klassische Trias aus Dysphagie, Eisenmangelanämie und ösophagealen Schleimhautstegen |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Übersichtsarbeit | Diseases of the Esophagus | Zwei PVS-Fälle erfolgreich mit Eisensupplementierung behandelt, was zur vollständigen Symptombeseitigung führte |
| [26502163](https://pubmed.ncbi.nlm.nih.gov/26502163/) | 2015 | Übersichtsarbeit | J Pediatr Gastroenterol Nutr | PVS bei Kindern, assoziiert mit häufigem Eisenmangel |
| [37013208](https://pubmed.ncbi.nlm.nih.gov/37013208/) | 2023 | Fallserie | Pan African Medical Journal | Tunesische Fallserie mit 23 Patienten zur Beschreibung der Epidemiologie und therapeutischen Ergebnisse von PVS |

---

## Kandidaten mit geringerer Konfidenz (nicht zur Weiterverfolgung empfohlen)

Die folgenden drei Kandidaten wurden geprüft und werden auf Basis dieses Evidenzpakets **nicht** zur weiteren Bearbeitung empfohlen:

- **Vitamin-B12-/Folat-unabhängige megaloblastäre Anämie (Rang 1)**: Keine klinischen Studien oder Literatur vorhanden; hierbei handelt es sich um eine genetische Störung der DNA-Synthese, die nicht mit dem Eisenstatus zusammenhängt. Die eigene Begründung von TxGNN weist dies als wahrscheinlich falsche Stichwortassoziation mit „Anämie" aus.
- **Nicht-syndromale ösophageale Fehlbildung (Rang 3)**: Ein struktureller angeborener Defekt ohne Evidenz und ohne plausiblen biologischen Zusammenhang mit Eisen.
- **Biotin-Stoffwechselerkrankung (Rang 4)**: Die zitierten Studien sind generische pädiatrische/ernährungsbezogene Mikronährstoffstudien (überwiegend mit Relevanzgrad C bewertet), nicht spezifisch für die Biotin-Erkrankung; die Literatur wird von randständigen Verbindungen zum mitochondrialen Stoffwechsel dominiert.
- **Ösophaguserkrankung (Rang 6, breite Kategorie)**: Die Evidenzqualität ist gemischt — tatsächlich unterstützt werden nur die eisenmangelassoziierten Subtypen (z. B. ösophageale Schleimhautstege); die meisten zitierten Studien betreffen Magen-/Ösophaguskarzinome oder bariatrische Chirurgie, ohne Bezug zu Eisen.

---

## Marktinformationen für Deutschland

Für diesen Wirkstoffeintrag sind keine deutschen Marktzulassungen verzeichnet — der Marktstatus lautet **Nicht vermarktet**, mit **0** insgesamt erfassten Zulassungen in diesem Evidenzpaket.

---

## Sicherheitshinweise

Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen. In diesem Evidenzpaket liegen keine zentralen Warnhinweise, Kontraindikationen oder Daten zu Arzneimittelwechselwirkungen vor (DDI-Abfragestatus: nicht gefunden).

---

## Fazit und nächste Schritte

**Entscheidung: Mit Leitplanken fortfahren** (beschränkt auf Vitamin-/Mineralstoffmangelerkrankung und Plummer-Vinson-Syndrom) **/ Zurückstellen** (für die verbleibenden vier Kandidaten)

**Begründung:**
Zwei der sechs von TxGNN vorhergesagten Indikationen (Korrektur von Eisen-/Vitaminmangel sowie Plummer-Vinson-Syndrom) sind mechanistisch schlüssig und evidenzgestützt, stellen jedoch eher eine Bestätigung der bereits bekannten therapeutischen Rolle von Eisen dar als eine wirklich neuartige Repurposing-Möglichkeit. Den übrigen vier Kandidaten fehlt es an mechanistischer Plausibilität, klinischer Studienevidenz oder krankheitsspezifischer Literatur; sie sind mit höherer Wahrscheinlichkeit Artefakte semantischer Ähnlichkeit im zugrunde liegenden Wissensgraphen.

**Für die Weiterverfolgung wird Folgendes benötigt:**
- Wirkmechanismusdaten aus DrugBank (derzeit eine blockierende Datenlücke mit hoher Schwere — DG002)
- Offizielle TFDA-/deutsche Fachinformations-Warnhinweise und Kontraindikationen (blockierende Datenlücke — DG001), erforderlich, bevor ein S1-Sicherheits-Vorscreening erfolgen kann
- Klärung der ursprünglich zugelassenen Indikation(en) für diesen spezifischen Wirkstoffeintrag, die derzeit nicht dokumentiert sind
- Bei Weiterverfolgung des Plummer-Vinson-Syndroms als formale Indikation: Klärung, ob dies eine tatsächlich neue regulatorische Indikation darstellen würde oder lediglich eine bereits gängige Off-Label-Praxis dokumentiert
- Bei Weiterverfolgung des Kandidaten „Vitaminmangelerkrankung": Abgleich der Ontologie-Diskrepanz (Eisen ist ein Mineralstoff) mit der regulatorischen Nomenklatur, bevor eine Indikationsformulierung entworfen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

