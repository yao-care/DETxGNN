---
layout: default
title: Canagliflozin
parent: Nur Modellvorhersage (L5)
nav_order: 82
evidence_level: L5
indication_count: 0
---

# Canagliflozin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **0** 
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

# Canagliflozin: Evaluierung der Arzneimittelumwidmung — Keine TxGNN-Vorhersagedaten verfügbar

## Zusammenfassung in einem Satz

Canagliflozin ist ein Natriumglucose-Cotransporter-2-(SGLT2)-Hemmer, der international weit verbreitet für Typ-2-Diabetes, Herzinsuffizienz und chronische Nierenerkrankung verwendet wird.
Dieses Evidenzpaket enthält jedoch **keine TxGNN-prognostizierten Indikationen**, und das Arzneimittel besitzt **keine dokumentierten taiwanischen regulatorischen Genehmigungen**.
Eine vollständige Evaluierung der Arzneimittelumwidmung kann nicht erstellt werden, bis Vorhersagedaten und Informationen zum Wirkmechanismus abgerufen werden.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Keine taiwanische Genehmigung in den Unterlagen |
| Prognostizierte neue Indikation | Keine Vorhersagedaten verfügbar |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzgrad | Unter L5 — keine Prognosen, keine unterstützenden Studien abgerufen |
| Taiwan-Marktstatus | Nicht auf dem Markt |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum diese Evaluierung nicht fortgesetzt werden kann

Diesem Evidenzpaket fehlen zwei grundlegende Datenelemente, die für eine Evaluierung der Arzneimittelumwidmung erforderlich sind:

1. **Keine TxGNN-Prognosen** — Das `predicted_indications`-Array ist leer. Ohne eine Modellvorhersage gibt es keine zu bewertende Kandidatenindikation und keine Richtung für die Evidenzsuche.

2. **MOA-Daten fehlen** — Das Wirkmechanismus-Feld konnte trotz Rückgabe eines Ergebnisses nicht erfolgreich von DrugBank abgerufen werden. Ohne MOA kann die biologische Plausibilität einer Arzneimittelumwidmungshypothese nicht bewertet werden.

Canagliflozin ist ein international gut charakterisiertes Arzneimittel (SGLT2-Hemmung, renale Glucoseausscheidung, hämodynamische und kardioprotektive Effekte), aber diese Fakten können die strukturierte Pipeline-Ausgabe, die erforderlich ist, um mit diesem Arbeitsablauf fortzufahren, nicht ersetzen.

---

## Evidenz aus klinischen Studien

Gegenwärtig sind keine zugehörigen klinischen Studien in diesem Evidenzpaket aufgeführt.

---

## Literaturdaten

Gegenwärtig ist keine zugehörige Literatur in diesem Evidenzpaket aufgeführt.

---

## Taiwan-Marktinformationen

Canagliflozin hat zum Zeitpunkt des Datenschlusses dieses Evidenzpakets (2026-04-20) keine registrierten Arzneimittelgenehmigungen in Taiwan.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Keine Warnungen, Gegenanzeigen oder Arzneimittelwechselwirkungsdaten sind in diesem Evidenzpaket vorhanden. Alle Sicherheitsfelder lieferten keine Daten oder konnten nicht abgefragt werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Das Evidenzpaket enthält keine TxGNN-Vorhersageausgabe und keine MOA-Daten – die zwei Eingaben, die jeden nachgelagerten Abschnitt eines Umwidmungsberichts antreiben. Ein Fortfahren ohne diese würde die Erfindung analytischer Inhalte erfordern, was nicht akzeptabel ist.

**Um fortzufahren, wird Folgendes benötigt:**

- [ ] **TxGNN-Pipeline erneut ausführen** — Bestätigen Sie, ob Canagliflozin durch das Modell verarbeitet wurde; rufen Sie `predicted_indications` mit Scores, Links zu klinischen Studien und Literatur-PMIDs ab
- [ ] **MOA aus DrugBank abrufen** — Die DrugBank-Abfrage lieferte ein Ergebnis (Abfrage-Logeintrag #3), aber MOA wurde nicht extrahiert; analysieren Sie den DrugBank-Datensatz erneut auf Mechanismus, Pharmakodynamik und Kategorien
- [ ] **Taiwan-Packungsbeilage herunterladen** — Die TFDA-Abfrage lieferte ein Ergebnis (Abfrage-Logeintrag #4); extrahieren Sie Warnungen, Gegenanzeigen und genehmigte Indikationen aus der PDF
- [ ] **DDI-Abfrage erneut ausführen** — Die Arzneimittelwechselwirkungsabfrage lieferte `not_found` zurück; überprüfen Sie, ob dies ein echtes Fehlen oder ein Abfrageparameter-Problem widerspiegelt
- [ ] **Marktumfang klären** — Wenn der Zielmarkt Deutschland (BfArM) statt Taiwan (TFDA) ist, wechseln Sie die regulatorische Abfragequelle entsprechend; Canagliflozin (Invokana®) ist in der EU zugelassen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

