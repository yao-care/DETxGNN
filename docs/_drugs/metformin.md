---
layout: default
title: Metformin
parent: Nur Modellvorhersage (L5)
nav_order: 293
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metformin: vorhergesagte neue Indikation Fokales Stiff-Limb-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: Diabetes mellitus Typ 2"
monitor_inn: "METFORMIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Metformin: Vom Typ-2-Diabetes zum fokalen Stiff-Limb-Syndrom

## Zusammenfassung

Metformin wird seit Langem zur Behandlung des **Diabetes mellitus Typ 2** eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei dem **fokalen Stiff-Limb-Syndrom** wirksam sein könnte. Für diese Vorhersage liegen in den für diesen Bericht zusammengestellten Daten **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf der Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Diabetes mellitus Typ 2 |
| Vorhergesagte neue Indikation | Fokales Stiff-Limb-Syndrom |
| TxGNN-Vorhersagewert | 99,45 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen |
| Anzahl der Zulassungen | 19 (alle erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus von Metformin liegen in den zusammengestellten Daten derzeit keine detaillierten Angaben vor. Bekannt ist, dass Metformin die AMPK aktiviert, die hepatische Glukoneogenese verringert und den mitochondrialen Komplex I moduliert. Seine Wirksamkeit bei Typ-2-Diabetes ist belegt.

Das fokale Stiff-Limb-Syndrom gehört zum Spektrum des Stiff-Person-Syndroms, einer seltenen autoimmun-neurologischen Erkrankung mit gestörter GABAerger Hemmung. Ein belegter mechanistischer Zusammenhang mit Metformin besteht nicht. Denkbar, aber rein spekulativ, wären immunmodulatorische oder entzündungshemmende Effekte oder eine Verbindung über GAD-Antikörper, die auch bei autoimmunem Diabetes auftreten.

Der Vorhersagewert ist identisch mit dem der klassischen Stiff-Person-Erkrankung (Rang 2). Das deutet darauf hin, dass das Modell beide Krankheitsknoten als nahezu gleichwertig behandelt und keine unabhängige Evidenz liefert.

**Weitere vorhergesagte Indikationen (jeweils nur Modellvorhersage, L5, Hold):**

| Rang | Erkrankung | Score | Anmerkung |
|---|---|---|---|
| 2 | Klassisches Stiff-Person-Syndrom | 99,45 % | Kein belegter Zusammenhang mit Metformin |
| 3 | Opsismodysplasie | 99,40 % | Lose Verbindung über INPPL1/SHIP2 und PI3K/AKT-Signalweg; Hypothese |
| 4 | Thiaminabhängiges Dysfunktionssyndrom | 99,40 % | Eher Sicherheitsaspekt (Transporter) als therapeutische Begründung |
| 5 | Medikamenteninduzierte lokalisierte Lipodystrophie | 99,06 % | Systemische Insulinsensitivierung vermutlich wenig wirksam bei lokaler Gewebereaktion |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

Alle 19 Zulassungen sind erloschen; es besteht keine gültige Zulassung. Die folgende Tabelle zeigt fünf Beispiele (Zulassungen der Europäischen Arzneimittel-Agentur, jeweils Kombinationspräparate mit Metformin).

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002654 | Vipdomet | – | Diabetes mellitus Typ 2 |
| EMEA/H/C/001235 | Ristfor | – | Diabetes mellitus Typ 2 |
| EMEA/H/C/003770 | Synjardy | – | Diabetes mellitus Typ 2 |
| EMEA/H/C/002279 | Jentadueto | – | Diabetes mellitus Typ 2 |
| EMEA/H/C/000861 | Janumet | – | Diabetes mellitus Typ 2 |

---

## Sicherheitsaspekte

**Kontraindikationen laut Wissensgraph** (TxGNN/PrimeKG, Beziehungen zwischen Wirkstoff und Erkrankung, kein Packungsbeilagentext):
- Leberversagen und Lebererkrankung
- Nierenerkrankung
- Pankreatitis
- Gallenblasenerkrankung
- Dekompensierte Herzinsuffizienz
- Pyoureter
- Hypopituitarismus und verschiedene Formen des Hypophysenhormonmangels (u. a. Sheehan-Syndrom, kongenitaler hypogonadotroper Hypogonadismus, Kallmann-Syndrom, isolierter Wachstumshormonmangel)
- Erkrankung der Thymusdrüse
- Nebennierenrindeninsuffizienz

**Arzneimittelwechselwirkungen** (100 Einträge insgesamt, Auswahl der als schwerwiegend eingestuften):
- **Schwerwiegend (Major):** Acetazolamid, Ethanol
- **Moderat (Auswahl):** Dolutegravir, Abemaciclib, Phenylephrin, Ranitidin, Formoterol, Pseudoephedrin, Ketorolac, Nifedipin, Epinephrin, Ibuprofen, Ethinylestradiol, Hydrocortison, Salbutamol, Hydrochlorothiazid, Acetohexamid
- **Gering (Minor):** Acarbose, topisches Hydrocortison, topisches Alclometason

Für weitere Sicherheitsinformationen, insbesondere Warnhinweise, siehe die Packungsbeilage.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzlevel L5). Es gibt weder Studien noch Publikationen, und ein mechanistischer Zusammenhang mit dem Stiff-Person-Spektrum ist nicht belegt. Zudem existiert in Deutschland derzeit keine gültige Zulassung für Metformin-Präparate in den erfassten Daten.

**Für ein Weiterkommen sind erforderlich:**
- Gezielte Literaturrecherche zu Metformin beim Stiff-Person-Syndrom bzw. Stiff-Limb-Syndrom
- Daten zum Wirkmechanismus (MOA) von Metformin
- Auswertung der Packungsbeilage (Warnhinweise und Gegenanzeigen) von BfArM
- Prüfung des aktuellen Zulassungs- und Marktstatus in Deutschland
- Klärung der Applikationswege und der Ähnlichkeit zur ursprünglichen Indikation
- Präklinische oder mechanistische Studien, die eine Beteiligung von AMPK/mTOR oder immunmodulatorischen Effekten bei GABAerger Dysfunktion stützen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

