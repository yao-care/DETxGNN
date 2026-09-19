---
layout: default
title: Riluzole
parent: Nur Modellvorhersage (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzol: ALS-Behandlung — Keine TxGNN-Repurposing-Vorhersage verfügbar

## Zusammenfassung in einem Satz

Riluzol ist eine etablierte Behandlung für die Amyotrophe Lateralsklerose (ALS), die als Glutamat-Freisetzungshemmer mit neuroprotektiven Eigenschaften wirkt. Dieses Evidence Pack enthält jedoch **keine TxGNN-Vorhersagedaten** und **keine vorhergesagten Indikationen**, wodurch eine vollständige Repurposing-Evaluierung derzeit unmöglich ist. Mehrere blockierende Datenlücken – einschließlich fehlender ursprünglicher Indikationsdatensätze, MOA-Daten und Sicherheitsinformationen – müssen behoben werden, bevor diese Bewertung fortgesetzt werden kann.

---

## Schnelübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht eingetragen in diesem Evidence Pack (allgemeines Wissen: ALS / Motoneuronerkrankung) |
| Vorhergesagte neue Indikation | **Nicht verfügbar** — `predicted_indications`-Array ist leer |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | Kann nicht bestimmt werden |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aussetzen** |

---

## Warum Vorhersagedaten nicht verfügbar sind

Das Evidence Pack für Riluzol (DrugBank: DB00740) wurde mit erheblichen Datenlücken generiert. Konkret:

- `predicted_indications` ist ein **leeres Array** — die TxGNN-Pipeline wurde entweder nicht für diesen Kandidaten ausgeführt oder hat null Vorhersagen zurückgegeben.
- `original_indications` ist ebenfalls ein **leeres Array** — die TFDA-Abfrage gab 0 Ergebnisse zurück, was konsistent mit dem Arzneistoff ist, der **nicht in Taiwan/Deutschland vermarktet ist**.
- `original_moa` ist gekennzeichnet als `[Data Gap]` — die DrugBank-Abfrage protokollierte einen erfolgreichen Abruf (`result_count: 1`), aber es wurde kein MOA in das Ausgabeschema abgebildet.

Aus allgemeinem pharmakologischen Wissen: Riluzol (Rilutek®) ist in der EU und in den USA für **ALS/MND** zugelassen. Sein Mechanismus beinhaltet die Hemmung der präsynaptischen Glutamat-Freisetzung und die Blockade von spannungsgesteuerten Natriumkanälen, wodurch die exzitotoxische Neuronenschädigung reduziert wird. Dieser Kontext wird nur zu Informationszwecken bereitgestellt und ersetzt **nicht** ein ordnungsgemäß ausgefülltes Evidence Pack.

Derzeit sind detaillierte Wirkmechanismus-Daten in diesem Pack nicht verfügbar. Basierend auf bekannten Informationen gehört Riluzol zur Benzothiazol-Klasse und seine Wirksamkeit bei ALS wurde klinisch nachgewiesen; ein ordnungsgemäß ausgefülltes MOA-Feld wäre erforderlich, um die mechanistische Anwendbarkeit auf jede neue Indikation zu bewerten.

---

## Informationen zum deutschen Markt

Es wurden keine Zulassungen gefunden. Riluzol hat **0 registrierte Lizenzen** auf dem abgefragten Markt. Dieser Abschnitt kann nicht ausgefüllt werden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Alle Sicherheitsfelder – wichtige Warnungen, Kontraindikationen und DDI – führten zu `[Data Gap]` oder `not_found`. Die TFDA-Packungsbeilage-Abfrage protokollierte jedoch einen erfolgreichen Abruf (`result_count: 1`), was darauf hindeutet, dass Quelldaten existieren, aber nicht in das Evidence Pack-Schema geparst wurden.)*

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Das Evidence Pack ist strukturell unvollständig — keine TxGNN-vorhergesagten Indikationen, keine ursprünglichen Indikationsdatensätze, kein MOA und keine Sicherheitsdaten — weshalb jede Repurposing-Evaluierung verfrüht und möglicherweise irreführend ist.

**Um fortzufahren, wird Folgendes benötigt:**

| Priorität | Lücken-ID | Element | Erforderliche Maßnahme |
|-----------|-----------|--------|----------------------|
| 🔴 Blockierend | DG001 | TFDA/BfArM Packungsbeilage-Warnungen & Kontraindikationen | Parsen Sie die bereits abgerufene PDF (Abfrage-ID 4, `result_count: 1`) in das Sicherheitsschema |
| 🔴 Blockierend | — | `predicted_indications` ist leer | Führen Sie die TxGNN-Vorhersage-Pipeline für DB00740 erneut aus; überprüfen Sie die Input-Knoten-Zuordnung |
| 🟠 Hoch | DG002 | MOA (Wirkmechanismus) | DrugBank gab ein Ergebnis zurück (Abfrage-ID 3, `result_count: 1`); extrahieren Sie das `mechanism_of_action`-Feld aus der API-Antwort |
| 🟠 Hoch | — | `original_indications` | Riluzol ist nicht in Taiwan/Deutschland vermarktet — beschaffen Sie sich die EU-Fachinformation von der EMA oder das FDA-Label, um dieses Feld auszufüllen |
| 🟡 Mittel | — | DDI-Daten | Erweitern Sie die DDI-Abfrage auf DrugBank oder glaubwürdige Interaktionsdatenbanken; das aktuelle Ergebnis ist `not_found` |

Sobald diese Lücken geschlossen sind und TxGNN mindestens eine bewertete Indikation erzeugt, sollte dieser Bericht mit Evidence Pack v5+ neu generiert werden.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

