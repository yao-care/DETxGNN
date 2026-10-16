---
layout: default
title: Caplacizumab
parent: Nur Modellvorhersage (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Caplacizumab: vorhergesagte neue Indikation Primäre Plättchen-Freisetzungsstörung (Evidenzstufe L5). Ursprüngliche Indikation: Thrombotische thrombozytopenische Purpura (TTP)"
---

# Caplacizumab
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

# Caplacizumab: Von der thrombotischen thrombozytopenischen Purpura zur thrombotischen thrombozytopenischen Purpura (Top-Vorhersage: primäre Plättchen-Freisetzungsstörung)

## Zusammenfassung

Caplacizumab ist ein gegen den von-Willebrand-Faktor (vWF) gerichteter Nanobody und wurde ursprünglich zur Behandlung der thrombotischen thrombozytopenischen Purpura (TTP) entwickelt. Das TxGNN-Modell sagt für die Top-Vorhersage **primäre Plättchen-Freisetzungsstörung** einen sehr hohen Score voraus, jedoch **ohne jegliche klinische Studie und ohne Publikation**. Die einzige Vorhersage mit belastbarer Evidenz (**7 klinische Studien**, **20 Publikationen**) ist die **thrombotische thrombozytopenische Purpura** – also die bereits zugelassene Originalindikation, keine echte Neuindikation.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Thrombotische thrombozytopenische Purpura (TTP) |
| Vorhergesagte neue Indikation (Rang 1) | Primäre Plättchen-Freisetzungsstörung |
| TxGNN-Vorhersagescore | 99,99 % |
| Evidenzlevel | L5 (Rang 1: nur Modellvorhersage); L1 für TTP (Originalindikation) |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold (für die Neuindikation); TTP selbst: Proceed with Guardrails |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Detaillierte Mechanismusdaten (MOA) sind in den für diesen Bericht zusammengestellten Daten nicht hinterlegt. Bekannt ist jedoch: Caplacizumab ist ein Nanobody, der an die A1-Domäne des vWF bindet und so die vWF-Interaktion mit dem Plättchen-Glykoprotein GPIb blockiert. Bei der erworbenen TTP fehlt wegen eines ADAMTS13-Mangels die Spaltung ultragroßer vWF-Multimere; diese binden unkontrolliert an Plättchen und führen zu Mikrothrombosen. Caplacizumab verhindert diese Adhäsion direkt.

Die vom Modell vorhergesagten Top-Indikationen (primäre Plättchen-Freisetzungsstörung, Pseudo-von-Willebrand-Erkrankung, Glanzmann-Thrombasthenie, Scott-Syndrom u. a.) sind überwiegend **Blutungsneigungen mit Plättchenfunktionsstörung**. Hier wäre die Hemmung der vWF-Plättchen-Adhäsion mechanistisch nicht heilsam, sondern würde die Hämostase weiter beeinträchtigen und das Blutungsrisiko erhöhen. Die hohen Scores sind sehr wahrscheinlich ein Artefakt der Nähe dieser Erkrankungen zur TTP im Wissensgraphen.

Auch die Hämophilie (Rang 9) ist nicht plausibel: Die dort zugeordneten 20 Publikationen behandeln ausschließlich TTP und Caplacizumab, nicht Hämophilie, und stellen daher Rauschen aus der Literatursuche dar. Die Vorhersage „TTP“ (Rang 5) ist dagegen die validierte Originalindikation.

---

## Evidenz aus klinischen Studien

Da die Top-Vorhersage (primäre Plättchen-Freisetzungsstörung) keine Studien hat, werden hier die Studien zur TTP (Originalindikation, Rang 5) dargestellt:

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Abgeschlossen | 145 | HERCULES: doppelblinde, placebokontrollierte RCT zu Caplacizumab bei erworbener TTP (Zulassungsstudie) |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Abgeschlossen | 104 | Post-HERCULES: Langzeitsicherheit und -wirksamkeit, inkl. Wiederholungsbehandlung |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Abgeschlossen | 51 | Einarmige Studie: Caplacizumab plus Immunsuppression ohne primären Plasmaaustausch bei iTTP |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Abgeschlossen | 75 | TITAN: einfachblinde, randomisierte, placebokontrollierte Studie; kürzere Zeit bis zur Plättchennormalisierung |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Abgeschlossen | 21 | Offene Studie bei japanischen Patienten mit aTTP (Rezidivprävention) |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Phase 2 | Abgebrochen | 58 | Personalisiertes Caplacizumab-Schema nach ADAMTS13-Aktivität, einarmig |
| [NCT05263193](https://clinicaltrials.gov/study/NCT05263193) | k. A. | Abgeschlossen | 4 | Retrospektive Datenerhebung bei Kindern mit iTTP |
| [NCT05785468](https://clinicaltrials.gov/study/NCT05785468) | k. A. | Unbekannt | 1 | Retrospektive italienische Beobachtungsstudie (ROSCAPLI) |

Für die übrigen vorhergesagten Indikationen sind derzeit keine einschlägigen klinischen Studien registriert.

---

## Literaturevidenz

Auswahl zur TTP (Originalindikation); für die Top-Vorhersage liegt keine Literatur vor:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | RCT | N Engl J Med | Caplacizumab hemmt die Interaktion von vWF-Multimeren mit Plättchen bei erworbener TTP |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | RCT | N Engl J Med | Caplacizumab bei erworbener TTP (TITAN) |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Leitlinie | J Thromb Haemost | ISTH-Leitlinie zur Behandlung der TTP |
| [37689812](https://pubmed.ncbi.nlm.nih.gov/37689812/) | 2023 | Leitlinie | Int J Hematol | Japanische Leitlinien zu Diagnose und Behandlung der TTP |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Kohorte | EClinicalMedicine | Internationale retrospektive Kohorte (Capla 1000+) zum Einsatz bei iTTP |
| [38838300](https://pubmed.ncbi.nlm.nih.gov/38838300/) | 2024 | Kohorte | Blood | Management der iTTP ohne therapeutischen Plasmaaustausch (42 Fälle, Österreich/Deutschland) |
| [33881463](https://pubmed.ncbi.nlm.nih.gov/33881463/) | 2021 | Kohorte | Blood Adv | Integrierte Analyse: Caplacizumab senkt Refraktärität und Mortalität |
| [36138517](https://pubmed.ncbi.nlm.nih.gov/36138517/) | 2022 | Kohorte | J Thromb Haemost | Post-HERCULES: Langzeitverlauf und Wiederholungsanwendung |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Review | JAMA | Übersicht zur immunvermittelten TTP |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | J Clin Med | Pathophysiologie, Diagnose und Management der TTP |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004426 | Cablivi | – | Thrombotische thrombozytopenische Purpura (Status: erloschen) |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Es wurden 100 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind u. a. Acetylsalicylsäure, Deferasirox, Abciximab, Acalabrutinib, Fondaparinux, Alteplase, Anagrelid, Ibritumomab tiuxetan, Tositumomab und Trastuzumab-Emtansin. Als **moderat** eingestuft sind u. a. Ibuprofen, Celecoxib, Ketorolac, Fluvoxamin, Fenfluramin, Dexfenfluramin und Sibutramin. Überwiegend handelt es sich um Substanzen mit Einfluss auf Blutung/Gerinnung.
- **Blutungsrisiko:** Aus dem Wirkmechanismus (Hemmung der vWF-Plättchen-Adhäsion) ergibt sich ein erhöhtes Blutungsrisiko, besonders relevant bei den vorhergesagten Blutungserkrankungen sowie bei Neugeborenen und in der Schwangerschaft.

Weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) bitte der Fachinformation entnehmen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold** (für die Top-Vorhersage und die übrigen Neuindikationen); für die TTP als Originalindikation: Proceed with Guardrails.

**Begründung:**
- Die höchstbewerteten Vorhersagen beruhen ausschließlich auf der Graphnähe im Wissensgraphen, haben keine klinische oder literarische Evidenz, und der Mechanismus würde das Blutungsrisiko eher erhöhen. Evidenzlevel L5.
- Die einzige gut belegte Indikation ist die TTP (L1; HERCULES, Post-HERCULES, TITAN, ISTH-Leitlinie) – eine bereits zugelassene Anwendung, kein Repurposing.

**Für ein Weiterkommen erforderlich:**
- Mechanistische und präklinische Daten, die einen Nutzen bei Plättchenfunktionsstörungen plausibel machen (derzeit nicht erkennbar)
- Sicherheitsbewertung des Blutungsrisikos in den vorhergesagten Zielpopulationen
- Fachinformation (Warnhinweise, Gegenanzeigen) und Klärung der Mechanismusdaten
- Klärung des Zulassungsstatus in Deutschland (die erfasste Zulassung ist erloschen)
- Bei TTP: Blutungsmonitoring, ADAMTS13-gesteuerte Behandlungsdauer, Anwendung zusammen mit Plasmaaustausch und Immunsuppression
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

