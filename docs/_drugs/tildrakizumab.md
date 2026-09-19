---
layout: default
title: Tildrakizumab
parent: Nur Modellvorhersage (L5)
nav_order: 397
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Tildrakizumab: Von unbestätigter ursprünglicher Indikation zu schwerer nicht-proliferativer diabetischer Retinopathie

## Zusammenfassung in einem Satz

> Die ursprüngliche Indikation für Tildrakizumab konnte anhand des aktuellen Evidenzpakets nicht bestätigt werden — das Arzneimittel ist in Deutschland noch nicht auf dem Markt und es gibt keine Zulassungsunterlagen.
> Das TxGNN-Modell prognostiziert möglicherweise Wirksamkeit bei **schwerer nicht-proliferativer diabetischer Retinopathie**,
> aber derzeit gibt es **0 klinische Studien** und **0 Veröffentlichungen**, die diese Richtung unterstützen — die Vorhersage basiert rein auf Knowledge-Graph-Inferenz.

---

## Kurzüberblick

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar (keine Zulassungsunterlagen; das Feld `original_indications` ist leer) |
| Vorhergesagte neue Indikation | Schwere nicht-proliferative diabetische Retinopathie |
| TxGNN-Vorhersage-Score | 99.63% |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nicht auf dem Markt (Nicht auf dem Markt) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (`original_moa` ist in diesem Evidenzpaket als Datenlücke gekennzeichnet). Basierend auf Informationen, die in der Umwidmungsrationale eingebettet sind, wird Tildrakizumab als **monoklonaler Antikörper gegen IL-23p19** identifiziert. Diese Mechanismus-Klasse ist in der Dermatologie gut etabliert (Hemmung des IL-23/Th17-Signalwegs), obwohl die bestätigte ursprüngliche Indikation selbst nicht in diesem Datenpaket dokumentiert ist.

Die theoretische Verbindung zur diabetischen Retinopathie beruht auf der Hypothese, dass die IL-23/Th17-Achse zu chronischer Netzhautentzündung und pathologischer Neovaskularisierung beiträgt, daher könnte die IL-23-Blockade theoretisch entzündungsbedingte Netzhautschäden reduzieren. Dies ist jedoch nur eine **mechanistische Hypothese** — es gibt keine Tier- oder Humanstudien in der aktuellen Datenbasis, die einen Zusammenhang zwischen IL-23-Hemmung und Ergebnissen bei diabetischer Augenerkrankung belegen.

Insgesamt spiegelt der hohe TxGNN-Score die strukturelle Ähnlichkeit innerhalb des Knowledge Graph wider, nicht validierte biologische oder klinische Evidenz. Dieser Kandidat sollte als frühe Hypothese behandelt werden, die vor jeder klinischen Berücksichtigung erhebliche zusätzliche Daten benötigt.

### Andere vorhergesagte Indikationen (noch nicht priorisiert)

Das gleiche Evidenzpaket hat auch drei weitere Kandidaten gekennzeichnet, alle auf der gleichen Evidenzstufe:

| Rang | Vorhergesagte Indikation | TxGNN-Score | Evidenzgrad | Empfehlung |
|------|--------------------------|-------------|-------------|-----------|
| 2 | Diabetische Retinopathie | 99.53% | L5 | Abwarten |
| 3 | Diabetische Katarakt | 99.21% | L5 | Abwarten |
| 4 | Arzneimittelinduzierte Osteoporose | 99.20% | L5 | Abwarten |

Unter diesen hat arzneimittelinduzierte Osteoporose die relativ stärkste mechanistische Plausibilität (die IL-23/IL-17/Th17-Signalisierung reguliert bekanntermaßen die Osteoklasten-Aktivierung über RANKL), während diabetische Katarakt die schwächste mechanistische Verbindung hat, da ihre Pathologie primär durch hyperglykämie-induzierte Linsenprotein-Glykation angetrieben wird, nicht durch Entzündung. Alle vier Kandidaten haben derzeit null unterstützende klinische Studien oder Literatur.

---

## Evidenz aus klinischen Studien

Derzeit sind keine damit verbundenen klinischen Studien registriert.

---

## Literaturische Evidenz

Derzeit ist keine damit verbundene Literatur verfügbar.

---

## Marktinformationen für Deutschland

Tildrakizumab ist derzeit nicht in Deutschland auf dem Markt, und es sind keine Zulassungsunterlagen in diesem Evidenzpaket verfügbar (`total_licenses: 0`).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind alle als Datenlücken in diesem Evidenzpaket gekennzeichnet. Besonders zu beachten ist, dass der meta-Abschnitt „TFDA-Etikett-Warnungen/Kontraindikationen" als eine **blockierende** Datenlücke kennzeichnet, was bedeutet, dass dieser Kandidat derzeit nicht in die Phase S1-Sicherheitsbewertung eintreten kann.)*

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Rationale:**
Alle vier vorhergesagten Indikationen werden nur durch TxGNN-Modell-Scores (L5, S0-Phase) mit null klinischen Studien oder literarischer Evidenz gestützt. Darüber hinaus verhindert derzeit eine blockierende Datenlücke (fehlende TFDA-Etikett-Warnungen/Kontraindikationen), dass dieser Kandidat zu einer Sicherheitsbewertungsphase übergeht.

**Um fortzufahren, ist folgendes erforderlich:**
- Beheben Sie DG001 (Blockierung): Erhalten Sie TFDA/offizielle Etikett-Warnungen und Kontraindikationen
- Beheben Sie DG002 (Hoch): Bestätigen Sie den Wirkmechanismus über die DrugBank-API-Abfrage
- Bestätigen Sie die ursprünglichen zugelassenen Indikationen des Arzneimittels, die derzeit in diesem Paket nicht dokumentiert sind
- Identifizieren Sie mindestens vorklinische oder Beobachtungsevidenz, die IL-23-Hemmung mit einer der vier Kandidatenindikationen verbindet, bevor Sie über S0 hinaus vorankommen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

