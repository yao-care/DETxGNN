---
layout: default
title: Rilpivirine
parent: Nur Modellvorhersage (L5)
nav_order: 340
evidence_level: L5
indication_count: 5
---

# Rilpivirine
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

# Rilpivirine: Evaluierung der Arzneimittelumwidmung – Paket mit unzureichenden Belegen

## Zusammenfassung in einem Satz

Rilpivirine (DrugBank: DB08864) ist ein antiretrovirales Mittel der NNRTI-Klasse, das zur Behandlung der HIV-1-Infektion verwendet wird.
Dieses Beweispaket enthält keine durch TxGNN vorhergesagten Umwidmungsindikationen, und das Arzneimittel hat keine behördlichen Zulassungen in Taiwan.
Eine **Zurückstellung**-Entscheidung wird empfohlen, bis Vorhersageergebnisse und Sicherheitsdokumentation vorliegen.

---

## Schnellübersicht

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Nicht in behördlichen Daten erfasst |
| Vorhergesagte neue Indikation | In diesem Beweispaket nicht verfügbar |
| TxGNN-Vorhersagepunktzahl | N/A |
| Beweisstufe | L5 – Keine unterstützenden Studien; Modellausgabe nicht vorhanden |
| Marktstatus Taiwan | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellung |

---

## Informationen zum Taiwan-Markt

Es wurden keine zugelassenen Produkte für Rilpivirine in der Taiwan-Regulierungsdatenbank gefunden. Null Lizenzen sind aktenkundig.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Die TFDA-Packungsbeilage-Abfrage gab einen Datensatz zurück (siehe Abfrageprotokoll-ID 4), aber Warnhinweise und Kontraindikations-Inhalte wurden nicht in dieses Beweispaket eingefügt. Arzneimittelwechselwirkungs-Daten wurden nicht gefunden (Abfrageprotokoll-ID 2).

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Das Array `predicted_indications` ist leer – es gibt keine TxGNN-Umwidmungskandidaten zur Bewertung dieser Verbindung. Ohne eine Zielindikation können weder die mechanistische Relevanz, klinische Belege noch eine Nutzen-Risiko-Bewertung durchgeführt werden.

**Um fortzufahren, wird Folgendes benötigt:**

- **Wirkungsmechanismus-Daten** (DG002 – Hohe Schwere): Wirkungsmechanismus von DrugBank API abrufen, um Analyse der mechanistischen Plausibilität zu ermöglichen
- **Sicherheitsdokumentation** (DG001 – Blockierend): TFDA-Packungsbeilage PDF bereits abgerufen (Abfrageprotokoll-ID 4) analysieren, um wichtige Warnhinweise, Kontraindikationen und Einschränkungen für spezielle Populationen vor S1-Sicherheitsscreening zu extrahieren
- **Zielmarkt-Überprüfung**: Bestätigen, ob Deutschland (BfArM) oder Taiwan (TFDA) die beabsichtigte Regulierungsjurisdiktion für diesen Kandidaten ist, und das Evidenzpaket entsprechend abstimmen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

