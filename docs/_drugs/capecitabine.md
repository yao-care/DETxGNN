---
layout: default
title: Capecitabine
parent: Nur Modellvorhersage (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabin (DB01101): Bewertung der Umnutzung – Unzureichende Daten zum Fortfahren

## Zusammenfassung in einem Satz

Capecitabin (DB01101) ist ein Fluoropyrimidin-Zytostatikum. Dieses Evidence Pack enthält jedoch keine TxGNN-vorhergesagten Indikationen, keine bestätigten Wirkmechanismus-Daten und keine taiwanischen behördlichen Aufzeichnungen – was eine vollständige Umnutzungsbewertung in diesem Stadium unmöglich macht. **Die Pipeline muss erneut ausgeführt und Datenlücken geschlossen werden, bevor eine Umnutzungsrichtung bewertet werden kann.**

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht im Evidence Pack verfügbar |
| Vorhergesagte neue Indikation | Nicht verfügbar – `predicted_indications`-Array ist leer |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzgrad | L5 (keine Vorhersagen zurückgegeben; keine unterstützenden Studien abrufbar) |
| Taiwan-Marktstatus | Nicht auf dem Markt (0 TFDA-Genehmigungen gefunden) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage angemessen?

Keine TxGNN-vorhergesagten Indikationen wurden in diesem Evidence Pack zurückgegeben. Ohne mindestens eine Kandidaten-Indikation ist es nicht möglich, mechanistische Plausibilität zu bewerten, gezielt klinische Studienevidenz abzurufen oder klinische Machbarkeit zu evaluieren. Dieser Abschnitt wird abgeschlossen, sobald die Vorhersage-Pipeline eine gültige Ausgabe liefert.

Darüber hinaus sind detaillierte Wirkmechanismus-Daten nicht im aktuellen Evidence Pack verfügbar. Capecitabin ist strukturell als Fluoropyrimidin klassifizierbar, aber kein DrugBank-MOA-Datensatz wurde erfolgreich in dieses Pack geladen, daher kann die mechanistische Analyse nicht formal begründet werden.

---

## Klinische Studienevidenz

Derzeit keine zugehörigen klinischen Studien registriert. *(Dieser Abschnitt erfordert mindestens eine vorhergesagte Indikation, um den Suchbereich zu definieren.)*

---

## Literaturevidenz

Derzeit keine zugehörige Literatur verfügbar. *(Dieser Abschnitt erfordert mindestens eine vorhergesagte Indikation, um den Suchbereich zu definieren.)*

---

## Zytotoxizität

Capecitabin fällt in die Fluoropyrimidin-Klasse der konventionellen zytotoxischen Chemotherapie und erfüllt damit Kriterium 3 der Zytostatika-Bestimmungsregeln. Dieser Abschnitt ist daher enthalten.

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifikation | Konventionell zytotoxisch – Fluoropyrimidin-Klasse (orales Prodrug) |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Gebrauchsinformation |
| Emetogenitätsklassifikation | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Gebrauchsinformation |
| Überwachungselemente | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Gebrauchsinformation |
| Schutzmaßnahmen bei der Handhabung | Muss den Bestimmungen für die Handhabung von Zytostatika entsprechen |

> Hinweis: Detaillierte Toxizitätsparameter (Myelosuppressions-Grad, Emetogenitätsniveau) konnten nicht ausgefüllt werden, da die DrugBank-Toxizitätsfelder und TFDA-Gebrauchsinformationen nicht erfolgreich in dieses Evidence Pack geladen wurden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack ist strukturell unvollständig – keine TxGNN-vorhergesagten Indikationen, keine MOA-Daten und keine taiwanischen behördlichen Sicherheitsdaten sind verfügbar. Es gibt keine Umnutzungshypothese zu evaluieren und keine Sicherheits-Baseline zum Vergleichen.

**Zum Fortfahren ist Folgendes erforderlich:**

- **TxGNN-Vorhersage-Pipeline erneut ausführen** für DB01101 und mindestens eine vorhergesagte Indikation bestätigen, bevor dieser Bericht neu generiert wird
- **DG002 (Hohe Schweregrad) beheben:** MOA aus der DrugBank-API (`/drugs/DB01101`) abrufen, um mechanistische Plausibilitätsanalyse zu ermöglichen
- **DG001 (Blockierender Schweregrad) beheben:** TFDA-Gebrauchsinformation-PDF herunterladen und analysieren, um wichtige Warnhinweise und Kontraindikationen für den S1-Sicherheitsbildschirm auszufüllen
- **TFDA-Abfrageergebnis verifizieren:** Die Abfrage hat 0 Genehmigungen für Capecitabin zurückgegeben – bestätigen Sie, ob dies das völlige Fehlen einer TFDA-Genehmigung widerspiegelt oder ein Datenpipeline-Problem ist (z. B. Handelsname-Alias nicht durchsucht)
- **DDI-Quelle erneut überprüfen:** Die DDI-Abfrage hat `not_found` zurückgegeben; bestätigen Sie, ob es sich um eine Datenbankslücke oder einen Abfrageparameter-Fehler handelt

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

