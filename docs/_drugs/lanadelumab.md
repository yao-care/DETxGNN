---
layout: default
title: Lanadelumab
parent: Nur Modellvorhersage (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: Von der Prophylaxe des hereditären Angioödems zur C1-Inhibitor-Defizienz

## Zusammenfassung in einem Satz

Lanadelumab ist ein vollständig humaner monoklonaler Antikörper, der Plasma-Kallikrein inhibiert und bereits in mehreren Ländern zugelassen und vermarktet ist (z. B. Japan, Südkorea, China, Argentinien – wie in den Studienunterlagen dokumentiert), zur Langzeitprophylaxe von Angioödem-Anfällen bei hereditärem Angioödem (HAE). Die Top-Vorhersage des TxGNN-Modells, **C1-Inhibitor-Defizienz**, wird durch **24 klinische Studien** und **20 Publikationen** gestützt. Es ist jedoch zu beachten, dass C1-Inhibitor-Defizienz der zugrunde liegende genetische Defekt ist, der HAE verursacht – die Erkrankung, die Lanadelumab bereits behandelt – sodass dieses Ergebnis in erster Linie **die Genauigkeit des Modells bestätigt**, statt eine echte neuartige Repurposing-Möglichkeit zu identifizieren.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Prophylaxe des hereditären Angioödems (HAE) (gemäß Studienunterlagen; formale MOA/Felder zur ursprünglichen Indikation in diesem Evidence Pack sind als Datenlücken gekennzeichnet) |
| Vorhergesagte neue Indikation | C1-Inhibitor-Defizienz |
| TxGNN-Vorhersage-Score | 99.9955% |
| Evidence Level | L2 (1 abgeschlossene Phase-3-RCT – HELP Study; verbleibende Phase-3-Studien sind Open-Label/Expanded-Access/Observational) |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage sinnvoll?

Das Feld `original_moa` in diesem Evidence Pack ist als Datenlücke gekennzeichnet. Basierend auf der in diesem Pack gesammelten Literaturevidenz (PMID 30267321) ist Lanadelumab jedoch als vollständig humaner monoklonaler Antikörper dokumentiert, der Plasma-Kallikrein inhibiert und die Bradykinin-Generierung innerhalb der Kallikrein-Kinin-Bahn reduziert.

C1-Inhibitor (kodiert durch *SERPING1*) ist der physiologische Regulator der Plasma-Kallikrein-Aktivität. Wenn C1-INH mangelhaft oder dysfunktional ist (HAE Typ I/II), wird die Kallikrein-Aktivität unkontrolliert und treibt die Überproduktion von Bradykinin und die Gefäßpermeabilität an, die HAE-Anfälle verursacht. Lanadelumab ersetzt C1-INH selbst nicht, sondern inhibiert das gleiche nachgelagerte Enzym (Kallikrein), das C1-INH normalerweise reguliert – weshalb es bereits eine zugelassene, First-Line-Langzeitprophylaxe-Therapie für HAE aufgrund von C1-INH-Defizienz in zahlreichen Märkten ist, auf die in den nachfolgenden Studienunterlagen verwiesen wird (Japan, Südkorea, China, Argentinien, Vereinigtes Königreich, Polen, Saudi-Arabien).

Da „C1-Inhibitor-Defizienz" im Wesentlichen gleichbedeutend mit der Krankheitspopulation ist, die Lanadelumab bereits behandelt, sollte diese TxGNN-Vorhersage als ein **Validierungssignal** für das Modell interpretiert werden und nicht als eine neue therapeutische Hypothese, die unabhängige Proof-of-Concept-Evidenz erfordert.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Befunde |
|---------|------|--------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Abgeschlossen | 125 | HELP Study – pivotale randomisierte, doppelblinde, placebokontrollierte Studie zum Nachweis der Wirksamkeit von Lanadelumab (DX-2930) in der Prävention von HAE-Anfällen (Typ I/II) |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Abgeschlossen | 212 | HELP Study Extension – Open-Label-Langzeitsicherheits- und Wirksamkeitsverfolgung |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Abgeschlossen | 20 | Sicherheit, PK und Wirksamkeit von Lanadelumab bei chinesischen HAE-Patienten über 26 Wochen |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Abgeschlossen | 12 | Wirksamkeit und Sicherheit von Lanadelumab bei japanischen HAE-Patienten Typ I/II |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Abgeschlossen | 21 | SPRING Study – PK/PD und Wirksamkeit von Lanadelumab bei pädiatrischen Patienten (2–<12 Jahre) |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Abgeschlossen | 73 | Langzeitsicherheit/-wirksamkeit bei nicht-histaminergem Angioödem mit normalem C1-INH |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Abgeschlossen | 12 | Japan Expanded-Access-Programm für HAE Typ I/II |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Phase 1 | Abgeschlossen | 32 | First-in-Human-Einzeldosis-Aufwärts-Studie zur Sicherheit/PK (gesunde Probanden) |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Phase 1 | Abgeschlossen | 38 | Mehrfach-Dosisaufwärts-Studie zur Sicherheit/Verträglichkeit/PK bei HAE-Probanden |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Abgeschlossen | 168 | EMPOWER Study – Real-World-Observational-Anfall-Häufigkeits-Vergleich (USA/Kanada) |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wichtigste Befunde |
|------|-----|------|--------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab reduzierte die HAE-Anfallshäufigkeit vs. Placebo signifikant (HELP Study primäre Publikation) |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Übersicht | N Engl J Med | Übersicht der HAE-Pathophysiologie, C1-INH-Defizienz und Behandlungslandschaft |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematische Übersicht | Clin Rev Allergy Immunol | Durchbruch-Anfälle bei HAE-Patienten unter Langzeitprophylaxe, einschließlich Lanadelumab |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Übersicht | J Investig Allergol Clin Immunol | Aktuelle und neue Therapien für C1-INH-HAE, einschließlich Kallikrein-Inhibition |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Übersicht | Drugs | „Lanadelumab: First Global Approval" – MOA und regulatorische Zulassungszusammenfassung |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-Label-Extension | Allergy | HELP OLE Study – Langzeiteffektivitäts-/Sicherheitsdaten (NCT02741596) |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Real-World/Observational | J Allergy Clin Immunol Pract | Länderübergreifende INTEGRATED-Studie zur realen Wirksamkeit von Lanadelumab |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Netzwerk-Metaanalyse | Drugs R D | Vergleichende Wirksamkeit/Sicherheit von HAE-Langzeitprophylaxe-Mitteln (Lanadelumab, Garadacimab, Berotralstat, C1-INH) |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Übersicht | J Allergy Clin Immunol | Krankheitslast der C1-INH-Defizienz in der Asien-Pazifik-Region |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Übersicht | BioDrugs | Präklinische und Phase-I-Daten-Übersicht von Lanadelumab zur C1-INH-HAE-Prophylaxe |

---

## Marktinformationen für Deutschland

Lanadelumab hat derzeit **keine Marktgenehmigung in den Aufzeichnungen dieses Evidence Pack** (`market_status`: Nicht vermarktet; `total_licenses`: 0). Es kann keine Lizenztabelle erstellt werden.

---

## Sicherheitsüberlegungen

Detaillierte Sicherheitsdaten (Wichtigste Warnhinweise, Kontraindikationen, Arzneimittelwechselwirkungen) werden in diesem Evidence Pack als Datenlücken gekennzeichnet (DG001, Schweregrad: **Blockierend**) und konnten nicht aus einer formalen Quelle (z. B. BfArM/EMA-Kennzeichnung) abgerufen werden. Diese Lücke **blockiert speziell den Fortschritt zur S1-Sicherheits-Vorabprüfungsstufe**.

> Bitte beachten Sie die offizielle Gebrauchsinformation/EMA SmPC für Sicherheitsinformationen, sobald diese verfügbar sind.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
- Die Wirksamkeitsevidenz für Lanadelumab bei HAE/C1-INH-Defizienz-bezogenen Indikationen ist stark (1 abgeschlossene Phase-3-RCT plus umfangreiche unterstützende Phase-3- und Real-World-Daten), aber dies spiegelt in erster Linie die **bereits etablierte** Indikation des Arzneimittels wider und stellt keinen neuartigen Repurposing-Kandidaten dar.
- Eine **Blockierend**-Schweregrad-Datenlücke (DG001: fehlende formale Warnhinweise/Kontraindikationen) verhindert, dass dieser Kandidat zur S1-Sicherheits-Vorabprüfung voranschreitet, gemäß der Lücken-Klassifizierung des Evidence Pack selbst.

**Zur Weiterleitung ist Folgendes erforderlich:**
- Rufen Sie offizielle Kennzeichnungs-/SmPC-Daten (Warnhinweise, Kontraindikationen, DDI) von BfArM/EMA ab, um DG001 vor jeder Sicherheits-Vorabprüfung zu schließen.
- Bestätigen und dokumentieren Sie die ursprüngliche MOA (DG002) aus einer primären regulatorischen Quelle statt sekundärer Literatur.
- Klären Sie den Umfang: Da sich „C1-Inhibitor-Defizienz" mit Lanadelumabs bekannter genehmigter Verwendung überlappt, bestimmen Sie, ob dieser Kandidat stattdessen als **Markteingangs-Bewertung** für Deutschland verfolgt werden sollte und nicht als Repurposing-Kandidat.
- Wenn echter Repurposing-Wert angestrebt wird, bewerten Sie niedriger eingestufte Kandidaten (z. B. nicht-histaminerges Angioödem mit normalem C1-INH, unterstützt durch NCT04444895), die distinkteren Indikationen aus dem genehmigten Etikett darstellen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

