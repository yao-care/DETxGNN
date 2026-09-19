---
layout: default
title: Eptifibatide
parent: Nur Modellvorhersage (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# EPTIFIBATIDE: Von akutem Koronarsyndrom bis zu Hämoglobinopathie (Sichelzellkrankheit)

> **Anmerkung zur Indikationsauswahl:** Dieses Evidence Pack (`TW-DB00063-multi`) enthält 10 TxGNN-prognostizierte Indikationen für Eptifibatide. Die #1-rangierte Vorhersage nach Rohwert (**rheumatoide Arthritis**, 99.99%) hat **null klinische Studien, null Literatur und eine ungefüllte („ausstehend") Begründung** — dies ist ausschließlich ein unvalidiertes Modelloutput. Im Gegensatz dazu hat die Rangfolge #7 (**Hämoglobinopathie / Sichelzellkrankheit**) die einzige Vorhersage in diesem Paket mit abgeschlossener Evidenzüberprüfung (1 klinische Studie + 4 Publikationen, Evidenzstufe L2, Entscheidungsphase S1). Um diesen Bericht tatsächlich für die Entscheidungsfindung nützlich zu machen, wurde er um diesen Kandidaten herum aufgebaut. Alle 10 Vorhersagen — einschließlich rheumatoider Arthritis — werden zum Zweck der Transparenz im Abschnitt „Weitere TxGNN-prognostizierte Indikationen" unten aufgelistet.

---

## Zusammenfassung in einem Satz

Eptifibatide ist ein GPIIb/IIIa (αIIbβ3)-Thrombozytenrezeptor-Antagonist; basierend auf der in diesem Evidenzpaket enthaltenen Literatur ist es für die Anwendung bei **akutem Koronarsyndrom (ACS)** etabliert.
Das TxGNN-Modell sagt voraus, dass es möglicherweise auch wirksam gegen **Hämoglobinopathie (Sichelzellkrankheit)** ist, und – im Gegensatz zu den anderen 9 Vorhersagen in diesem Paket – wird diese Richtung durch **1 abgebrochene Phase-1/2-Klinische Studie** und **4 Publikationen** gestützt, einschließlich zweier Studien, die Eptifibatide direkt bei Patienten mit Sichelzellkrankheit testeten.

---

## Schneller Überblick

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht in strukturierten Zulassungsdaten verzeichnet (Arzneistoff nicht vermarktet; 0 Lizenzen). Die Literatur in diesem Paket zeigt etablierte Anwendung bei **akutem Koronarsyndrom (ACS)** als GPIIb/IIIa-Antagonist. |
| Prognostizierte neue Indikation | Hämoglobinopathie (Sichelzellkrankheit-Spektrum) |
| TxGNN-Prognosewert | 99.98% (Rang 485 in Modelloutput) |
| Evidenzstufe | **L2** (pro Pipeline-Bewertung – siehe Caveat unten) |
| MarktStatus Deutschland | ✗ Nicht vermarktet (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aufhalten** |

**Caveat zur Evidenzstufe:** Die einzige Studie (NCT00834899) war Phase 1/2, wurde aber **abgebrochen** mit nur 13 von einer geplanten größeren Kohorte, und die erste Humanstudie (PMID 17916103) testete nur 4 Patienten. Nach dem formalen Regelwerk (L2 = „1 abgeschlossene Phase-2/3-RCT") ist diese Evidenz eher als *vorläufig/frühe Phase* zu beschreiben, nicht als vollständig abgeschlossene konfirmatorische Studie — das L2-Label spiegelt wider, dass echte menschliche Tests vorhanden sind, nicht dass diese schlüssig sind.

---

## Warum ist diese Vorhersage sinnvoll?

Eptifibatide ist ein synthetisches zyklisches Heptapeptid, das den Thrombozyten-αIIbβ3 (GPIIb/IIIa)-Rezeptor antagonisiert und den endgültigen gemeinsamen Weg der Thrombozytenaggregation blockiert. Dieser Mechanismus ist beim akuten Koronarsyndrom gut etabliert, wo die Hemmung der plättchenabhängigen Thrombusbildung ischämische Komplikationen während und nach der perkutanen Koronaren Intervention reduziert.

Sichelzellkrankheit (und das breitere Hämoglobinopathie-Spektrum) teilt ein pathophysiologisches Merkmal mit ACS: Gefäßverschluss. Bei der Sichelzellkrankheit werden schmerzhafte Krisen teilweise durch abnormale Thrombozytenhyperreaktivität, Thrombozyten-Leukozyten-Endothel-Wechselwirkungen und CD40-Liganden-Freisetzung getrieben, die zusammen die Mikrovaskuläre Verschluss und Entzündung fördern — ein Prozess mechanistisch ähnlich der thrombozytenvermittelten Thrombose, die Eptifibatide beim ACS blockieren soll. Diese gemeinsame Mechanismus ist die Begründung, die Ermittler verwendeten, um Eptifibatide direkt bei Sichelzellpatienten zu testen, anstatt einer rein rechnergestützten Schlussfolgerung.

Da diese exakte Hypothese bereits bei Menschen getestet wurde (Phase-1-Pharmakodynamik-Studie, eine Pilot-Wirksamkeitsstudie und eine abgebrochene Phase-1/2-RCT), handelt es sich um einen Fall, in dem TxGNNs Vorhersage mit bereits vorhandener echter klinischer Untersuchung konvergiert — was das Vertrauen im Vergleich zu den anderen 9 Vorhersagen in diesem Paket verstärkt, die alle reine graphbasierte Schlussfolgerungen ohne klinische Nachverfolgung sind.

---

## Klinische Studienbeweise

| Studiennummer | Phase | Status | Registrierungen | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Abgebrochen | 13 | Randomisierte, doppelblinde, placebokontrollierte Studie zur Bewertung der Sicherheit von Eptifibatide bei akuten Schmerzepisoden bei Sichelzellkrankheit. Hypothese: Thrombozytenhyperreaktivität und daraus resultierende Entzündung tragen zu vasookulusiven Krisen bei. Vorzeitig mit nur 13 der geplanten Kohorte abgebrochen, was auf Machbarkeits-/Rekrutierungsprobleme hindeutet. |

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase-1-Studie | British Journal of Haematology | Erste Humantests von Eptifibatide bei Sichelzellkrankheit (4 Patienten, nicht-krisenhafte/stabile Phase). Begründung: Thrombozytenhyperreaktivität und CD40-Liganden-Freisetzung bei SCD entsprechen der ACS-Pathophysiologie; Sicherheits- und pharmakodynamische Daten wurden nach Infusion gewonnen. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot-klinische Studie | Thrombosis Research | Pilot-Studie von Eptifibatide (αIIbβ3-Antagonist) zur Behandlung von akuten Schmerzepisoden bei SCD, Bewertung von Sicherheit und Wirksamkeit; der Beitrag der Thrombozytenhyperreaktivität zur SCD-Pathogenese blieb anfangs unsicher. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Klinische Teilanalyse | American Journal of Hematology | Begleitende Analyse, die die Auswirkung von Eptifibatide auf Entzündungsmarker während akuter Schmerzepisoden bei SCD untersuchte (verbunden mit der obigen Pilot-Studie). |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In-vitro-/Mikrofluidikal-Modell | The Journal of Clinical Investigation | Entwickelte ein „endothelisiertes" mikrofluidikal-Mikrovaskulatur-Modell, das Mikrovaskuläre Verschluss und Thrombose bei SCD und hämolytisch-urämischem Syndrom nachbildet. Unterstützt die zugrundeliegende mechanistische Begründung, testet aber nicht direkt Eptifibatide. |

---

## Marktinformation Deutschland

Eptifibatide hat derzeit **keine Marktgenehmigung auf Datei** für diesen Markt (Nicht vermarktet / Not Marketed, 0 Lizenzen registriert). Es sind keine Produkt-/Darreichungsform-/Indikationsdaten verfügbar, die tabellarisch dargestellt werden könnten.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Keine strukturierten Warnhinweise, Kontraindikationen oder Wechselwirkungsdaten wurden für dieses Evidenzpaket ermittelt — dies wird in den Quell-Metadaten als **Datenlücke mit Blockierungsschweregrad (DG001)** gekennzeichnet, was bedeutet, dass dieser Kandidat **unabhängig von der Indikation nicht zur formalen S1-Sicherheitsbewertung übergehen kann**, bis die TFDA/BfArM-Fachinformation erhalten und analysiert wird.

---

## Weitere TxGNN-prognostizierte Indikationen für diesen Arzneistoff

Aus Transparenzgründen werden die übrigen 9 Vorhersagen in diesem Multi-Indikations-Evidenzpaket nachfolgend zusammengefasst (alle erheblich niedriger in Evidenzmaturität als Hämoglobinopathie):

| Rang | Prognostizierte Indikation | TxGNN-Wert | Evidenzstufe | Empfehlung |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Rheumatoide Arthritis | 99.99% | L5 (keine Studien/Literatur; Begründung ungefüllt) | Ausstehend |
| 2 | Hereditäre Persistenz von fötalem Hämoglobin–Sichelzell-Krankheit-Syndrom | 99.98% | L5 | Aufhalten |
| 3 | Sichelzell–Hämoglobin-C-Krankheit-Syndrom | 99.98% | L4 (1 tangentieles ACS-Blutungsrisiko-Papier, nicht krankheitsspezifisch) | Aufhalten |
| 4 | Sichelzell–Hämoglobin-E-Krankheit-Syndrom | 99.98% | L5 | Aufhalten |
| 5 | Sichelzell–Beta-Thalassämie-Krankheit-Syndrom | 99.98% | L5 | Aufhalten |
| 6 | Sichelzell–Hämoglobin-D-Krankheit-Syndrom | 99.98% | L5 | Aufhalten |
| **7** | **Hämoglobinopathie (dieser Bericht)** | **99.98%** | **L2** | **Forschungsfrage / Aufhalten** |
| 8 | Weibliches Mammakarzinom | 99.97% | L4 (in-vitro-pro-apoptotischer Effekt auf MCF-7-Zellen; keine in-vivo-/klinischen Daten) | Forschungsfrage |
| 9 | Beta-Thalassämie mit anderen Manifestationen | 99.97% | L5 | Aufhalten |
| 10 | Partielle Deletion des kurzen Arms von Chromosom 16 | 99.96% | L5 (mechanistischer Link als schwach erachtet — wahrscheinlich ein Artefakt genomischer Nähe, nicht ein pharmakologisches) | Aufhalten |

Bemerkenswerterweise werden alle 10 Werte in einem engen Band von 99.96%–99.99% zusammengefasst, daher sollte TxGNNs Rohranking nicht als bedeutungsvolle Anordnung der klinischen Plausibilität gelesen werden — die Unterschiede bei der Evidenzstufe (L2 vs. L4 vs. L5) sind das entscheidungsrelevantere Signal hier.

---

## Fazit und nächste Schritte

**Entscheidung: Aufhalten**

**Begründung:**
Hämoglobinopathie/Sichelzellkrankheit ist die einzige Vorhersage in diesem Paket, die durch echte menschliche Tests gestützt wird (eine Phase-1-Pharmakodynamik-Studie und eine Pilot-Wirksamkeitsstudie), aber die bestätigende RCT (NCT00834899) wurde mit einer kleinen Kohorte vorzeitig abgebrochen, und eine Datenlücke mit Blockierungsschweregrad (fehlende TFDA/BfArM-Fachinformation und Sicherheitsdaten, DG001) hindert diesen Kandidaten unabhängig von der Indikation an der Einleitung formaler Sicherheitsbewertung.

**Zum Fortfahren ist folgendes erforderlich:**
- Lösen Sie DG001: Erhalten und analysieren Sie die TFDA/BfArM-Fachinformation (Warnhinweise, Kontraindikationen, DDI) — derzeit blockiert
- Lösen Sie DG002: Erhalten Sie detaillierte Wirkmechanismus-Daten aus DrugBank, um die mechanistische-Link-Analyse zu stärken
- Bestimmen Sie, warum NCT00834899 abgebrochen wurde (Rekrutierung, Sicherheitssignal oder Sponsorentscheidung), bevor Sie einen erneuerten Versuch in Betracht ziehen
- Wenn die Verfolgung weiterer Forschung in Betracht kommt, priorisieren Sie Hämoglobinopathie/Sichelzellkrankheit vor den anderen 9 Vorhersagen, da dies die einzige mit realen früheren Humandaten ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

