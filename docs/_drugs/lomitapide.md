---
layout: default
title: Lomitapide
parent: Nur Modellvorhersage (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lomitapide: vorhergesagte neue Indikation Makrothrombozytopenie mit Mitralklappeninsuffizienz (Evidenzstufe L5). Ursprüngliche Indikation: Hypercholesterinämie"
monitor_inn: "LOMITAPIDE"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "hyperlipoproteinemia", "platelet storage pool deficiency"]
---

# Lomitapide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Lomitapid: Von Hypercholesterinämie zu Makrothrombozytopenie mit Mitralklappeninsuffizienz

## Zusammenfassung in Kürze

Lomitapid ist ein oraler MTP-Hemmer (mikrosomales Triglycerid-Transferprotein), der ursprünglich zur Behandlung der **Hypercholesterinämie** zugelassen wurde (insbesondere der homozygoten familiären Hypercholesterinämie, HoFH). Das TxGNN-Modell sagt für Lomitapid mit dem höchsten Score eine Wirksamkeit bei **Makrothrombozytopenie mit Mitralklappeninsuffizienz** voraus. Für diese Vorhersage gibt es jedoch **keine klinischen Studien und keine Publikationen**, sie beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hypercholesterinämie |
| Vorhergesagte neue Indikation | Makrothrombozytopenie mit Mitralklappeninsuffizienz |
| TxGNN-Vorhersagewert | 99,92 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene bzw. widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Lomitapid hemmt das mikrosomale Triglycerid-Transferprotein (MTP). Dadurch wird der Aufbau und die Sekretion von apoB-haltigen Lipoproteinen blockiert (VLDL in der Leber, Chylomikronen im Darm), und das LDL-Cholesterin sinkt. Die ursprüngliche Wirkmechanismus-Angabe fehlt in den für diesen Bericht zusammengestellten Daten. Die obige Beschreibung stützt sich auf die mechanistische Einordnung der Kandidatenbewertung.

Ein mechanistischer Zusammenhang zwischen der MTP-Hemmung und Thrombozytopenien oder Mitralklappeninsuffizienz ist nicht erkennbar. Der hohe Score ist vermutlich ein Artefakt des Wissensgraphen: Lomitapid teilt dort offenbar Nachbarknoten mit einer Gruppe verwandter Thrombozytenerkrankungen. Die Vorhersage ist daher als rein rechnerische Hypothese ohne belastbare biologische Begründung zu verstehen.

Das gilt auch für die anderen Top-Vorhersagen (erbliche Thrombozytopenie, Dense-Granule-Krankheit, transiente neonatale Thrombozytopenie, Thrombozytopenie, primäre Thrombozyten-Freisetzungsstörung, Pseudo-von-Willebrand-Erkrankung, Glanzmann-Thrombasthenie, Thrombozyten-Speicherpool-Defekt). Für alle gibt es weder Studien noch Literatur und keine mechanistische Begründung. Bei der neonatalen Thrombozytopenie kommen Bedenken wegen Lebertoxizität und Teratogenität hinzu.

---

## Klinische Evidenz

Für die vorhergesagte Indikation (Makrothrombozytopenie mit Mitralklappeninsuffizienz) sind derzeit keine relevanten klinischen Studien registriert.

Die einzige Vorhersage mit Studienlage ist **Hyperlipoproteinämie** (Rang 9, Score 99,74 %). Sie entspricht im Wesentlichen der ursprünglichen Indikation und ist daher keine echte Neuausrichtung:

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) | Phase 3 | Abgeschlossen | 29 | Pivotale einarmige Studie zu Lomitapid (AEGR-733) bei HoFH unter laufender Lipidsenkung |
| [NCT00943306](https://clinicaltrials.gov/study/NCT00943306) | Phase 3 | Abgeschlossen | 19 | Offene Langzeit-Folgestudie zu Sicherheit und Wirksamkeit bei HoFH |
| [NCT04681170](https://clinicaltrials.gov/study/NCT04681170) | Phase 3 | Abgeschlossen | 46 | Einarmige, offene Studie bei pädiatrischen HoFH-Patienten |
| [NCT02173158](https://clinicaltrials.gov/study/NCT02173158) | Phase 3 | Abgeschlossen | 9 | Einarmige, offene Studie bei japanischen HoFH-Patienten |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Abgeschlossen | 6 | Offene Dosiseskalationsstudie zu Sicherheit, Verträglichkeit und Wirksamkeit bei HoFH |
| [NCT02135705](https://clinicaltrials.gov/study/NCT02135705) | N/A | Abgeschlossen | 260 | LOWER-Register: prospektive Beobachtungsstudie zu Langzeitsicherheit und Wirksamkeit |
| [NCT02765841](https://clinicaltrials.gov/study/NCT02765841) | Phase 3 | Zurückgezogen | 0 | Pädiatrische HoFH-Studie, nie gestartet, liefert keine Evidenz |
| [NCT02399852](https://clinicaltrials.gov/study/NCT02399852) | N/A | Zurückgezogen | 0 | Bildgebungsstudie zur Atherosklerose (CAPTURE), nie gestartet |

Alle abgeschlossenen Phase-3-Studien sind einarmig und unkontrolliert. Das L1-Level dieser Vorhersage bestätigt damit vor allem die bestehende Anwendung bei HoFH.

---

## Literatur

Für die vorhergesagte Indikation (Makrothrombozytopenie mit Mitralklappeninsuffizienz) ist derzeit keine relevante Literatur vorhanden.

Zur Hyperlipoproteinämie (Rang 9) liegen unter anderem folgende Arbeiten vor:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [39426393](https://pubmed.ncbi.nlm.nih.gov/39426393/) | 2024 | Klinische Phase-3-Studie | Lancet Diabetes & Endocrinology | Wirksamkeitsphase der offenen Phase-3-Studie zu Lomitapid bei Kindern mit HoFH |
| [37130090](https://pubmed.ncbi.nlm.nih.gov/37130090/) | 2023 | Konsensus-Review | European Heart Journal | Aktualisierter EAS-Konsensus zur HoFH mit neuen Therapien und klinischer Anleitung |
| [25053660](https://pubmed.ncbi.nlm.nih.gov/25053660/) | 2014 | Positionspapier | European Heart Journal | EAS-Leitlinie zu Erkennung und Management der HoFH |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Überblick über neue LDL-C-senkende Therapien bei HoFH |
| [40211340](https://pubmed.ncbi.nlm.nih.gov/40211340/) | 2025 | Klinische Studie | European Journal of Medical Research | Lomitapid verändert die HDL-Funktion bei HoFH |
| [31741187](https://pubmed.ncbi.nlm.nih.gov/31741187/) | 2019 | Review | Current Atherosclerosis Reports | Hemmung von MTP (Lomitapid) und apoB100-Synthese (Mipomersen) |
| [28598687](https://pubmed.ncbi.nlm.nih.gov/28598687/) | 2017 | Review | Expert Opinion on Pharmacotherapy | Lomitapid zur Behandlung der Hypercholesterinämie |
| [25702706](https://pubmed.ncbi.nlm.nih.gov/25702706/) | 2015 | Review (Wirkstoffprofil) | British Journal of Clinical Pharmacology | Wirkstoffprofil Lomitapid |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Überblick über die familiäre Hypercholesterinämie und ihre Therapieoptionen |
| [21846156](https://pubmed.ncbi.nlm.nih.gov/21846156/) | 2011 | Review (Wirkstoffprofil) | American Journal of Cardiovascular Drugs | Frühes Entwicklungsprofil von Lomitapid |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002578 | Lojuxta (Chiesi Farmaceutici SpA) | – | Hypercholesterinämie (Status: erloschen/widerrufen) |

Es besteht keine gültige Zulassung. Die regionale Verfügbarkeit sollte vor jeder weiteren Planung geprüft werden.

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** In den zusammengestellten Daten sind 100 Wechselwirkungen verzeichnet. Eine Auswahl:

- **Schwerwiegend (Major):** Acarbose, Pioglitazon, Doxycyclin, Tetracyclin, Minocyclin, Bupropion, Aprepitant, Clarithromycin, Chenodesoxycholsäure, Naltrexon, Oxandrolon, Oxymetholon
- **Mäßig (Moderate):** Ranitidin, Cimetidin, Loperamid, Budesonid (auch nasal), Saxagliptin, Linagliptin, Eliglustat

**Weitere Hinweise aus der Kandidatenbewertung:** Lebertoxizität (Überwachung nach REMS-Art), Leberverfettung, gastrointestinale Nebenwirkungen, zahlreiche CYP3A4-bedingte Wechselwirkungen und Bedenken wegen Teratogenität.

Für Warnhinweise und Gegenanzeigen siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für Makrothrombozytopenie mit Mitralklappeninsuffizienz beruht ausschließlich auf dem Modell (Evidenzlevel L5). Es gibt weder Studien noch Literatur noch einen plausiblen Mechanismus. Zudem ist das Sicherheitsprofil von Lomitapid belastend (Lebertoxizität, Teratogenität, viele Wechselwirkungen). Die Marktzulassung in Deutschland ist erloschen.

**Für eine Weiterverfolgung ist Folgendes nötig:**
- Eine biologisch nachvollziehbare Hypothese, die MTP-Hemmung mit Thrombozytenbildung bzw. -funktion oder Herzklappenerkrankungen verbindet, sowie präklinische Daten dazu
- Klärung, ob die Vorhersage lediglich ein Graph-Artefakt ist (Prüfung der gemeinsamen Nachbarknoten im Wissensgraphen)
- Vollständige Fachinformation mit Warnhinweisen und Gegenanzeigen
- Detaillierte Wirkmechanismus-Daten, z. B. aus DrugBank
- Klärung der regionalen Verfügbarkeit und des Zulassungsstatus von Lomitapid
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

