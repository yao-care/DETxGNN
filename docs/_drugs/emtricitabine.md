---
layout: default
title: Emtricitabine
parent: Mittlere Evidenz (L3-L4)
nav_order: 145
evidence_level: L4
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **3** 
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

# Emtricitabin: Von der HIV-1-Infektion zum Feline Acquired Immunodeficiency Syndrome

## Zusammenfassung in einem Satz

Emtricitabin ist ein Nukleosid-Reverse-Transkriptase-Inhibitor (NRTI), ursprünglich für die HIV-1-Infektion als Bestandteil von Kombinationsantiretroviralregimen entwickelt (z. B. Truvada, Atripla). Das Top-Prediction des TxGNN-Modells deutet auf das **Feline Acquired Immunodeficiency Syndrome (FIV)** — eine veterinäre, keine menschliche Erkrankung — hin, aber die unterstützende Evidenz besteht aus **4 klinischen Studien** (alle bei HIV-1-Patienten, überwiegend mit Medikamenten außer Emtricitabin) und **1 Publikation** (eine kleine Kohortenstudie, die direkt eine Emtricitabin-haltige Therapie bei FIV-infizierten Katzen testet). Die Evidenz ist daher preklinisch/mechanistisch von Natur, nicht klinisch.

---

## Schnellübersicht

| Element | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | HIV-1-Infektion (Kombinationsantiretroviraltherapie) — kein BfArM-/deutsches Lizenzierungsdatensatz existiert in diesem Datensatz; hergeleitet aus den in der Trial-Evidenz referenzierten Kombinationsregimen (Atripla, Truvada) |
| Vorhergesagte neue Indikation | Felines Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN-Vorhersagepunktzahl | 99.92% |
| Evidenzstufe | L4 |
| Deutscher Marktstatus | ✗ Nicht auf dem Markt |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückgestellt |

---

## Warum ist diese Vorhersage sinnvoll?

Der detaillierte DrugBank-Text zum Wirkmechanismus ist in diesem Evidenzpaket für Emtricitabin nicht verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad). Basierend auf dem bekannten Wissen ist Emtricitabin ein Cytidin-Analogon-NRTI und eine Kernkomponente von Fixdosis-Kombinationsantiretroviralregimen (z. B. Truvada [mit Tenofovir], Atripla [mit Efavirenz + Tenofovir]), wo es die HIV-1-Reverse-Transkriptase blockiert und die virale DNA-Synthese stoppt. Seine Effizienz bei der HIV-1-Infektion ist durch zahlreiche abgeschlossene Phase-3-Studien gut etabliert.

Die mechanistische Begründung für die Erweiterung auf FIV ist, dass das Feline Immunodeficiency Virus, wie HIV, ein Lentivirus ist, das für die Replikation von der Reverse-Transkriptase abhängt, und die beiden Enzyme sind über die Arten hinweg strukturkonserviert. Grundsätzlich könnte ein NRTI, das gegen HIV-Reverse-Transkriptase wirksam ist, auch FIV-Reverse-Transkriptase hemmen.

Diese Vorhersage muss jedoch mit einem wichtigen Vorbehalt gelesen werden: **drei der vier als „Evidenz" zurückgegebenen klinischen Studien beinhalten Emtricitabin überhaupt nicht** (sie testen Kombinationen von Dolutegravir, Darunavir oder Raltegravir) und **alle vier sind menschliche HIV-1-Studien, keine Katzenstudien** — das Evidenzpaket selbst kennzeichnet dies als wahrscheinliche Knowledge-Graph-Ontologie-Fehlanpassung, bei der Studien auf den generischen Begriff „Immundefizienz" statt auf echte Relevanz für FIV abgestimmt wurden. Der einzige wirklich relevante Datenpunkt ist eine 2023-Kohortenstudie, die direkt ein Kombinationsantiretroviralregimen mit Emtricitabin bei FIV-infizierten Hauskatzen evaluierte — eine echte, aber kleine, nicht-klinische (veterinärpharmakokinetische/Ergebnis-)Studie. Kontextlich wird eine eng verwandte TxGNN-Vorhersage in diesem Evidenzpaket (Rang 2, Simian Immunodeficiency Virus-Infektion) durch wesentlich stärkere Translationsevidenz unterstützt — 20 Publikationen, viele davon Makaken-Challenge-Studien, die Emtricitabin direkt verabreichen — und trägt eine höhere Evidenzstufe (L3, Mit Vorsichtsmaßnahmen fortfahren), obwohl SIV selbst eher ein Primaten-Forschungsmodell als eine zugelassene menschliche Indikation ist.

---

## Klinische Studienevidenz

| Studienshummer | Phase | Status | Einschreibung | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Abgeschlossen | 844 | Dolutegravir + Abacavir/Lamivudin vs. Atripla (Efavirenz/Emtricitabin/Tenofovir) bei ART-naiven HIV-1-Erwachsenen. Humane Studie; bewertet mit niedriger Relevanz (C) — keine FIV-Studie, Medikament nicht der primäre Vergleich. |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Abgeschlossen | 145 | Geboostertes Darunavir + Lamivudin vs. Darunavir + Emtricitabin/Tenofovir oder Lamivudin/Tenofovir bei naiven HIV-1-Patienten. Humane Studie; bewertet mit niedriger Relevanz (C). |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Abgeschlossen | 828 | Dolutegravir vs. Raltegravir, beide mit dualem NRTI-Rückgrat (ABC/3TC oder TDF/FTC), bei ART-naiven HIV-1-Erwachsenen. Humane Studie; bewertet mit niedriger Relevanz (C) — primärer Vergleich nicht Emtricitabin. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Abgeschlossen | 208 | Dosierungsselektionsstudie von Dolutegravir mit Abacavir/Lamivudin oder Tenofovir/Emtricitabin bei ART-naiven HIV-1-Erwachsenen. Humane Studie; bewertet mit niedriger Relevanz (C). |

**Anmerkung:** Alle vier Studien sind mit „C" (niedrige Relevanz) bewertet — es sind humane HIV-1-Studien, keine FIV-Studien, und in den meisten Fällen ist Emtricitabin nicht das unter primärer Untersuchung stehende Medikament.

---

## Literaturbeweise

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Kohorte (Tierimmunophänotypisierung) | Viruses | Evaluierte Kombinationsantiretroviraltherapie (Dolutegravir 2,5 mg/kg, Tenofovir 20 mg/kg, Emtricitabin 40 mg/kg) bei FIV-infizierten Hauskatzen — das einzige Evidenzelement, das Emtricitabin direkt in der vorhergesagten felinen Indikation testet. |

---

## Deutsche Marktinformation

Emtricitabin hat derzeit **keine BfArM-Marktzulassung im Datensatz** (0 Lizenzen, Marktstatus: Nicht auf dem Markt). Es kann nur als Teil von Fixdosis-Kombinationsprodukten (z. B. Truvada, Atripla) existieren, die unter dieser Drogeneinheit im Evidenzpaket nicht erfasst sind.

---

## Sicherheitsüberlegungen

Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen. (TFDA/BfArM-Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten konnten für dieses Arzneimittel nicht abgerufen werden — das Abrufen der offiziellen Packungsbeilage ist als **blockierende** Datenlücke gekennzeichnet, die vor jeder Phase-1-Sicherheitsbewertung gelöst werden muss.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückgestellt**

**Begründung:**
Die top-bewertete Vorhersage (FIV) basiert auf einer einzigen kleinen Tier-Kohortenstudie und vier klinischen Studien, die sich bei genauer Prüfung als menschliche HIV-1-Studien erweisen, die weitgehend unabhängig von Emtricitabin oder der felinen Indikation sind — konsistent mit der eigenen Bewertung des Evidenzpakets, dass diese Übereinstimmung wahrscheinlich eine Knowledge-Graph-Ontologie-Überlappung („Immundefizienz") statt echter Translationsevidenz widerspiegelt. In Kombination mit der ungelösten blockierenden Lücke bei der TFDA/BfArM-Sicherheitskennzeichnung gibt es nicht genug Evidenz, um über S0 hinauszugehen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Packungsbeilagedaten (Warnungen, Kontraindikationen) — derzeit eine blockierende Datenlücke
- Bestätigte DrugBank-Wirkmechanismus-Details für Emtricitabin
- Zusätzliche präklinische oder klinische Daten, die Emtricitabin speziell (nicht andere NRTIs) bei FIV-infizierten Katzen evaluieren
- Berücksichtigung der verwandten Rang-2-Vorhersage (Simian Immunodeficiency Virus-Infektion), die durch wesentlich mehr Literatur (20 Publikationen, einschließlich direkter Makaken-Dosierungsstudien) und eine höhere Evidenzstufe (L3) unterstützt wird, als möglicherweise defensiblere Forschungsrichtung — unter Beachtung, dass SIV selbst ein Tiermodus für die Forschung ist, keine zugelassene menschliche Indikation

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

