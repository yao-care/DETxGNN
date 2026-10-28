---
layout: default
title: Fentanyl
parent: Nur Modellvorhersage (L5)
nav_order: 194
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fentanyl: vorhergesagte neue Indikation Nephrogenes Syndrom der inadäquaten Antidiurese (Evidenzstufe L5). Ursprüngliche Indikation: Schmerz"
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

## Fentanyl: Nephrogenes Syndrom der inadäquaten Antidiurese
{: .text-alpha }

## Zusammenfassung in einem Satz

Fentanyl ist ein Opioid, das laut den zusammengestellten Daten ursprünglich zur Behandlung von Schmerzen bei Krebserkrankungen zugelassen war. Das TxGNN-Modell sagt voraus, dass es bei dem **nephrogenen Syndrom der inadäquaten Antidiurese** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien und keine Publikationen** vor; sie beruht ausschließlich auf einer graphbasierten Modellrechnung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Schmerz; Krebs |
| Vorhergesagte neue Indikation | Nephrogenes Syndrom der inadäquaten Antidiurese |
| TxGNN-Vorhersagewert | 0,9946 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 3 von 3) |
| Anzahl der Zulassungen | 3 (gültig: 3) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus liegen derzeit nicht vor. Bekannt ist, dass Fentanyl ein Agonist am μ-Opioid-Rezeptor ist und bei Schmerzen (u. a. Durchbruchschmerzen bei Krebs) eingesetzt wird.

Das nephrogene Syndrom der inadäquaten Antidiurese wird durch Gain-of-function-Mutationen im Vasopressin-V2-Rezeptor (AVPR2) oder in einzelnen Fällen in GNAS verursacht. Opioide können die Freisetzung des antidiuretischen Hormons über zentrale Mechanismen beeinflussen und SIADH-ähnliche Effekte auslösen. Das ist jedoch ein anderer Signalweg als der renale Defekt auf Rezeptorebene, der diese Erkrankung definiert.

Ein plausibler therapeutischer Zusammenhang ist daher nicht belegt. Ein möglicher Effekt wäre eher unerwünscht als nützlich. Der TxGNN-Wert ist als reiner Modellhinweis zu verstehen.

**Zweite vorhergesagte Indikation (Rang 2): Tourette-Syndrom** (Score 0,9905, ebenfalls L5, Empfehlung Hold). Das Opioidsystem moduliert dopaminerge und striatale Aktivität, und es gibt begrenzte Forschung zur Beteiligung des Opioidsystems bei Tic-Störungen. Das ist ein spekulativer, indirekter Ansatz. Wegen des hohen Missbrauchs- und Abhängigkeitspotenzials, des Risikos einer Atemdepression und des Marktstatus wäre Fentanyl ohne erhebliche zusätzliche Evidenz ungeeignet. Sinnvoller wären opioidmodulierende Substanzen mit günstigerem Sicherheitsprofil.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000833 | Effentora | – | Schmerz; Krebs |
| EMEA/H/C/001164 | PecFent | – | Schmerz; Krebs |
| EMEA/H/C/000959 | Instanyl | – | Schmerz; Krebs |

Alle drei Zulassungen sind aufgehoben (Status: cancelled).

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind u. a.: Alvimopan, Aprepitant, Bupropion, Clarithromycin, Clotrimazol, Dexamethason, Dexfenfluramin, Dolasetron, Fenfluramin, Granisetron und Lorcaserin. Als **mittelschwer (Moderate)** eingestuft sind u. a.: Atropin, Cimetidin, Clidinium, Dicyclomin, Dronabinol, Eluxadolin, Glyceroltriphenylbutyrat, Glycopyrronium und Hyoscyamin.
- **Kontraindikationen laut Wissensgraph (nicht aus Packungsbeilage):** Der TxGNN-Wissensgraph (PrimeKG) verzeichnet Kontraindikationen u. a. für Bluthochdruck, orthostatische Hypotonie, Long-QT-Syndrom, Torsades de pointes, Leberversagen und Lebererkrankungen, Nierenerkrankungen, chronisch obstruktive Lungenerkrankung (COPD), Asthma, Pankreatitis, Gallenblasenerkrankungen, chronisch-entzündliche Darmerkrankungen, benigne Prostatahyperplasie, Angststörungen sowie Substanzmissbrauch/-abhängigkeit.

Angaben zu Warnhinweisen und Kontraindikationen aus der Packungsbeilage liegen nicht vor; bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für beide vorhergesagten Indikationen gibt es ausschließlich eine Modellvorhersage (Evidenzlevel L5) ohne klinische Studien oder Publikationen. Beim nephrogenen SIAD fehlt zudem ein plausibler Wirkzusammenhang, und alle deutschen Zulassungen sind aufgehoben.

**Für ein Weiterkommen wird Folgendes benötigt:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Kontraindikationen aus der BfArM-Packungsbeilage (derzeit blockierend für die Sicherheitsprüfung)
- Präklinische oder klinische Evidenz, die einen Zusammenhang mit den vorhergesagten Indikationen stützt
- Prüfung der Darreichungswege und Alternativen mit günstigerem Sicherheitsprofil
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

