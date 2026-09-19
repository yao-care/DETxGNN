---
layout: default
title: Trametinib
parent: Nur Modellvorhersage (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: Von BRAF-V600-mutantem Melanom zu zusätzlichen Melanom-Subtypen

## Zusammenfassung in einem Satz

> Trametinib ist ein MEK1/2-Inhibitor, dessen etablierte Anwendung – dokumentiert in allen klinischen Studien dieser Evidenzsammlung – die Kombinationstherapie mit Dabrafenib für BRAF-V600-Mutations-positives Melanom ist. TxGNN identifiziert darüber hinaus mehrere histologische und anatomische Melanom-Subtypen (nodulär, oberflächlich ausbreitend, nicht-kutane/mukös-okular) als Kandidaten für denselben Wirkmechanismus, die durch unterschiedlich starke Phase-2/3-Studien und Fallberichte unterstützt werden, während eine Teilmenge der Vorhersagen (Choroiderämie, Hodensack-Melanom, CDK4-verknüpftes Melanom, Ballonzellen-Melanom) überhaupt keine klinische oder mechanistische Unterstützung hat. Dies ist ein **Multi-Indikations-Kandidatenpaket (10 Vorhersagen, Evidenzstufen L1–L5)**, daher wird jeder Kandidat nachfolgend unabhängig bewertet, anstatt als einzelne Go/No-Go-Entscheidung.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Nicht verfügbar in Taiwan/Deutschland-Regulierungsdaten (0 Lizenzen auf Datei). Basierend auf klinischen Studienbeschreibungen in diesem Paket ist die etablierte Verwendung von Trametinib die Kombinationstherapie mit Dabrafenib für **BRAF-V600E/K-Mutations-positives Melanom** (nicht resektabel/metastasiert und adjuvante Settings) |
| Am besten unterstützte neue Indikationen | **Oberflächlich ausbreitendes Melanom** und **Nodales malignes Melanom** (histologische Subtypen von kutanem Melanom) |
| TxGNN-Vorhersage-Score (Top-Kandidat) | 99,14% (beide Indikationen, gleichauf) |
| Evidenzstufe | L2 (1 abgeschlossene Phase-2-Studie + unterstützende Kohorten-/Fallliteratur) |
| Marktstatus Deutschland | Nicht vermarktet (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Mit Schutzmaßnahmen fortfahren** (für Melanom-Subtyp-Erweiterungen, bedingt durch BRAF-V600-Testung) – siehe vollständige Rangfolge nachfolgend für andere Kandidaten |

### Vollständige Rangfolge der vorhergesagten Indikationen

| Rang | Erkrankung | TxGNN-Score | Evidenzstufe | Empfehlung |
|------|-----------|-----------|-----------|-----------|
| 1 | Choroiderämie | 99,31% | L5 | Beibehalten |
| 2 | Nicht-kutanes Melanom | 99,30% | L1 | Forschungsfrage |
| 3 | Epitheloide Zell-Melanom | 99,28% | L4 | Forschungsfrage |
| 4 | Augenlid-Melanom | 99,26% | L4 | Forschungsfrage |
| 5 | Hodensack-Melanom | 99,21% | L5 | Beibehalten |
| 6 | Nodales malignes Melanom | 99,14% | L2 | **Mit Schutzmaßnahmen fortfahren** |
| 7 | Ballonzellen-Melanom | 99,14% | L5 | Beibehalten |
| 8 | Oberflächlich ausbreitendes Melanom | 99,14% | L2 | **Mit Schutzmaßnahmen fortfahren** |
| 9 | CDK4-verknüpftes Melanom | 99,14% | L5 | Beibehalten |
| 10 | Amelanotisches Haut-Melanom | 99,14% | L4 | Forschungsfrage |

*Hinweis: Die Evidenzstufe hier korreliert nicht monoton mit dem TxGNN-Score – ein hoher Ähnlichkeitsscore spiegelt die Nähe in der Wissensgraph wider, nicht die klinische Unterstützung. Rang 2 ist in der Quell-Bewertung als L1 gekennzeichnet, wird aber zu „Forschungsfrage" herabgestuft, da die angeführten Studien kutane-Melanom-Zulassungsstudien sind, die indirekt auf eine nicht-kutane Population angewendet werden, nicht krankheitsspezifische RCTs.*

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Texte von DrugBank sind in dieser Evidenzsammlung nicht verfügbar (Datenlücke DG002). Jedoch beschreibt jeder Klinische-Studien-Eintrag in diesem Paket konsistent Trametinib als oralen **MEK1/2-Inhibitor**, der in Kombination mit dem BRAF-Inhibitor Dabrafenib verwendet wird, um die MAPK/ERK-Signalkaskade unterhalb von BRAF-V600-Mutationen zu blockieren. Diese Kombination bildet das Rückgrat der pivotalen Zulassungsstudien, die hier vorhanden sind (z.B. NCT01245062, NCT01584648, NCT01597908), die die Wirksamkeit bei BRAF-V600E/K-mutantem nicht resektablem oder metastasiertem **kutanem** Melanom etabliert haben.

Die Vorhersagen in den Rängen 6 und 8 (nodulär und oberflächlich ausbreitend Melanom) sind histologische *Subtypen* des kutanen Melanoms und nicht unterschiedliche Erkrankungen – sie teilen die gleiche BRAF-V600-Mutations-Biologie wie die bereits behandelte Population, daher ist die mechanistische Extrapolation nah an direkt anstatt neuartig. Rang 2 (nicht-kutanes Melanom) und die okularen/mukosa-Vorhersagen (Ränge 3, 4, 10) sind biologisch weiter entfernt: Die BRAF-V600-Mutations-Prävalenz bei konjunktivalem, Augenlid- und Mukosa-Melanom ist erheblich niedriger als bei kutanem Melanom, daher ist die Ansprechrate plausibel nur in der BRAF-mutant-positiven Teilmenge, wie durch isolierte Fallberichte von konjunktivalem Melanom, das auf BRAF/MEK-Hemmung anspricht, illustriert (PMID 27893585, 31361915).

Umgekehrt haben Choroiderämie (Rang 1), Hodensack-Melanom (Rang 5), Ballonzellen-Melanom (Rang 7) und CDK4-verknüpftes Melanom (Rang 9) keine klinischen Studien, keine Literatur und keine plausible mechanistische Verbindung zu MEK-Hemmung (Choroiderämie ist eine CHM/REP1-Netzhaut-Degeneration, unabhängig von MAPK-Signalisierung; CDK4-getriebenes Melanom wirkt über Zellzyklus anstatt MAPK-Wege). Diese sollten als reine Wissensgraph-Artefakte behandelt werden.

---

## Klinische Studienevidenz

Die nachfolgenden Studien bilden die Kernevidenz-Grundlage, die Trametinibs BRAF/MEK-Wirkmechanismus untermauert; sie unterstützen die Melanom-Subtyp-Erweiterungen (nicht-kutane, nodulär, oberflächlich ausbreitend) als Hintergrund-mechanistische Evidenz anstatt subtyp-spezifische bestätigende Studien.

| Studiennummer | Phase | Status | Einschluss | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT01245062](https://clinicaltrials.gov/study/NCT01245062) | Phase 3 | Abgeschlossen | 322 | Pivotale Studie: Trametinib-Monotherapie vs. Chemotherapie bei BRAF-V600E/K-positivem kutanem Melanom |
| [NCT01584648](https://clinicaltrials.gov/study/NCT01584648) | Phase 3 | Abgeschlossen | 423 | COMBI-d: Dabrafenib+Trametinib vs. Dabrafenib allein, nicht resektables/metastasiertes BRAF-V600E/K kutanes Melanom |
| [NCT01597908](https://clinicaltrials.gov/study/NCT01597908) | Phase 3 | Abgeschlossen | 704 | COMBI-v: Dabrafenib+Trametinib vs. Vemurafenib, BRAF-V600E/K kutanes Melanom |
| [NCT03551626](https://clinicaltrials.gov/study/NCT03551626) | Phase 3b | Abgeschlossen | 552 | COMBI-APlus: Adjuvantes Dabrafenib+Trametinib nach vollständiger Resektion, Stadium III BRAF-V600 Melanom; Pyrexie-Nebenwirkungsmanagement-Algorithmus |
| [NCT01072175](https://clinicaltrials.gov/study/NCT01072175) | Phase 1/2 | Abgeschlossen | 430 | Originale Dosiseskalations-/Kombinationsstudie von Dabrafenib+Trametinib bei BRAF-mutantem metastasiertem Melanom |
| [NCT02039947](https://clinicaltrials.gov/study/NCT02039947) | Phase 2 | Abgeschlossen | 127 | Dabrafenib+Trametinib bei BRAF-mutantem Melanom mit Hirnmetastasen (4 Mutations-Kohorten) |
| [NCT02645149](https://clinicaltrials.gov/study/NCT02645149) | Phase 2 | Abgeschlossen | 216 | Molekulare Profilierung mit abgestimmter gezielter Therapie bei BRAF/NRAS Wildtyp nicht resektablem/metastasiertem Melanom, das unter Immunotherapie progredient ist |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Aktiv, nicht rekrutierend | 52 | Tripletts-Nivolumab+Dabrafenib+Trametinib (TRIDeNT) vs. Encorafenib+Binimetinib+Nivolumab (TRIBECA), BRAF-mutantes Stadium III-IV Melanom |
| [NCT05171374](https://clinicaltrials.gov/study/NCT05171374) | N/A | Unbekannt | 500 | Prospektive Real-World-Outcomes von Dabrafenib+Trametinib bei resektablem/metastasiertem BRAF+ Melanom |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Phase 4 | Rekrutierung läuft | 100 | Langzeit-Sicherheits-Roll-Over-Studie für Patienten, die Dabrafenib/Trametinib nach Abschluss der Mutterstudie fortsetzen |

*Keine Studien in diesem Paket rekrutieren spezifisch Patienten mit Choroiderämie, Hodensack-Melanom, Ballonzellen-Melanom oder CDK4-verknüpftem Melanom.*

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Review | JAMA | Übersicht über kutane Melanom-Epidemiologie und Behandlungslandschaft, einschließlich BRAF/MEK-gezielte Therapie |
| [30376465](https://pubmed.ncbi.nlm.nih.gov/30376465/) | 2019 | Kohorte | Melanoma Research | Multizentrische Real-Life-Studie von BRAF/MEK-Inhibitor-Kombination bei Melanom-Patienten mit aktiven Hirnmetastasen (n=65) |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Fallbericht/Review | Clin Exp Dermatol | BRAF-mutiertes bulbäres konjunktivales (epitheloide) Melanom, behandelt mit Vemurafenib; Literaturübersicht |
| [27893585](https://pubmed.ncbi.nlm.nih.gov/27893585/) | 2017 | Fallbericht | Ophthalmic Plast Reconstr Surg | Konjunktivales Melanom mit BRAF-V600E, ansprechbar auf systemische BRAF/MEK-Inhibitor-Kombination |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Fallbericht/Review | J Investig Med High Impact Case Rep | Malignes Melanom der Tränendrüse (epitheloider Typ); Übersicht von 15 japanischen Fällen |
| [41310270](https://pubmed.ncbi.nlm.nih.gov/41310270/) | 2025 | Fallbericht | Child's Nervous System | Pädiatrisches amelanotisches ZNS-Melanom mit systemischer Ausbreitung, assoziiert mit angeborenen melanozytären Nävi |
| [41209431](https://pubmed.ncbi.nlm.nih.gov/41209431/) | 2026 | Fallbericht | Oncology Letters | Kombinierte BRAF/MEK-Hemmung für BRAF-mutant Hirnmetastasen von oberflächlich ausbreitendem Melanom während der Schwangerschaft |
| [37756677](https://pubmed.ncbi.nlm.nih.gov/37756677/) | 2025 | Fallbericht | Retinal Cases & Brief Reports | Schnelle Auflösung von chorioidaler Metastase von kutanem Melanom nach kombinierter gezielter Therapie |
| [24879511](https://pubmed.ncbi.nlm.nih.gov/24879511/) | 2014 | Fallserie (Sicherheit) | Am J Dermatopathol | Panniculitis als Nebenwirkung von BRAF/MEK-Inhibitor-Therapie (Dabrafenib, Dabrafenib+Trametinib) |
| [32614358](https://pubmed.ncbi.nlm.nih.gov/32614358/) | 2020 | Fallbericht | La Clinica Terapeutica | PET-gesteuerte Umstellung von Immunotherapie zu BRAF/MEK-gezielte Therapie bei nodalem Melanom mit kutanen/skelettalen Metastasen |

*Für Choroiderämie, Hodensack-Melanom, Ballonzellen-Melanom oder CDK4-verknüpftes Melanom wurde keine Literatur zurückgegeben.*

---

## Marktsituation Deutschland

Trametinib ist derzeit **nicht vermarktet** in Deutschland gemäß der Regulierungsdatenquelle dieses Evidenzpakets (Marktstatus: Not marketed, 0 Zulassungen auf Datei). Es kann keine Lizenztabelle erstellt werden.

---

## Zytotoxizität

Trametinib ist ein antineoplastisches Agens (alle Studienpopulationen in diesem Paket sind Onkologie-/Melanom-Patienten), daher ist dieser Abschnitt anwendbar.

| Punkt | Inhalt |
|-------|--------|
| Zytotoxizitäts-Klassifizierung | Gezielte Therapie (MEK1/2-Inhibitor) – kein konventionales zytotoxisches Chemotherapeutikum |
| Myelosuppression-Risiko | Bitte beziehen Sie sich auf die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |
| Emetogenitäts-Klassifizierung | Bitte beziehen Sie sich auf die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |
| Überwachungspunkte | Bitte beziehen Sie sich auf die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |
| Handhabungsschutz | Bitte beziehen Sie sich auf die Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage |

---

## Sicherheitsaspekte

Bitte beziehen Sie sich auf die Packungsbeilage für Sicherheitsinformationen. (TFDA/BfArM-Warnhinweise, Gegenanzeigen und Arzneimittelwechselwirkungs-Daten sind in dieser Evidenzsammlung nicht verfügbar – gekennzeichnet als blockierende Datenlücke, DG001.)

---

## Fazit und nächste Schritte

**Entscheidung: Mit Schutzmaßnahmen fortfahren** (für die Melanom-Subtyp-Erweiterungen: nodales Melanom, oberflächlich ausbreitendes Melanom, nicht-kutanes Melanom) / **Beibehalten** (für Choroiderämie, Hodensack-Melanom, Ballonzellen-Melanom, CDK4-verknüpftes Melanom) / **Forschungsfrage** (für epitheloide Zell-Melanom, Augenlid-Melanom, amelanotisches Melanom)

**Begründung:**
- Nodales und oberflächlich ausbreitendes Melanom sind histologische Subtypen, die bereits in der biologischen Population (BRAF-V600-mutant kutanes Melanom) enthalten sind, in die die pivotalen Dabrafenib+Trametinib-Studien eingeschlossen haben – der mechanistische Fall ist stark, aber subtyp-spezifische bestätigende Studien fehlen, daher sind Schutzmaßnahmen (obligatorische BRAF-V600-Testung, subtyp-stratifizierte Überwachung) angebracht.
- Nicht-kutane, okulare und Mukosa-Melanom-Vorhersagen stützen sich nur auf Fallbeweise in einer Population mit niedrigerer BRAF-Mutations-Prävalenz, und Choroiderämie-/Hodensack-/Ballonzellen-/CDK4-verknüpfte Melanom-Vorhersagen haben null klinische oder mechanistische Unterstützung – diese sollten ohne neue primäre Evidenz nicht fortfahren.

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA/BfArM-Packungsbeilage (Warnhinweise, Gegenanzeigen, DDI) – derzeit eine blockierende Datenlücke (DG001)
- Von DrugBank stammender Wirkmechanismus und Toxizitätsprofil (DG002)
- BRAF-V600-Mutations-Status-Stratifizierungsdaten für jedes subtyp-spezifische Studiendesign
- Bestätigung des genehmigten Label-Umfangs von Trametinib (kutane vs. alle Melanome) aus einer vertrauenswürdigen Regulierungsquelle, da es in den hier bereitgestellten Regulierungsdaten fehlt

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

