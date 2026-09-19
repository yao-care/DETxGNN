---
layout: default
title: Rasagiline Tartrate
parent: Nur Modellvorhersage (L5)
nav_order: 328
evidence_level: L5
indication_count: 0
---

# Rasagiline Tartrate
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

# RASAGILINE TARTRATE: Bewertung unvollständig — Daten ausstehend

## Zusammenfassung in einem Satz

RASAGILINE TARTRATE ist ein Arzneimittel ohne Zulassung in Taiwan und ohne in der Regulierungsdatenbank eingetragene zugelassene Indikationen.
Die TxGNN-Vorhersage-Pipeline hat keine neuen Indikationskandidaten für diese Verbindung im aktuellen Evidence Pack zurückgegeben, und kritische Daten – einschließlich Wirkmechanismus und Sicherheitsprofil – bleiben ungeklärte Datenlücken.
Eine vollständige Arzneimittelneupositionierungs-Bewertung kann nicht durchgeführt werden, bis diese Lücken behoben sind.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar |
| Vorhergesagte neue Indikation | Nicht verfügbar |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzlevel | L5 — Keine Vorhersagen erhalten |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar, und das TxGNN-Modell hat in der aktuellen Pipeline-Ausführung keine vorhergesagten Indikationen für diese Verbindung zurückgegeben.

Erwähnenswert ist, dass die Abfrage-Logs zeigen, dass sowohl die DrugBank-Abfrage (ID: 3) als auch die TFDA-Packungsbeilage-Abfrage (ID: 4) jeweils 1 Ergebnis zurückgegeben haben, was darauf hindeutet, dass Quelldaten *tatsächlich* existieren. Diese Daten wurden jedoch nicht in die strukturierten Felder des Evidence Pack propagiert (z. B. `drugbank_id`, `original_indications`, `original_moa` bleiben leer oder `[Data Gap]`). Dies ist ein Datenpipeline-Problem, das gelöst werden muss, bevor eine mechanistische Analyse fortgesetzt werden kann.

Bis die MOA-, ursprünglichen Indikationen und TxGNN-Vorhersage-Ausgaben ordnungsgemäß ausgefüllt werden, kann keine Bewertung der biologischen Plausibilität vorgenommen werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine einschlägigen klinischen Studien zur Bewertung im Rahmen dieses Evidence Pack registriert.

---

## Literaturbeweise

Derzeit ist keine einschlägige Literatur im Rahmen dieses Evidence Pack verfügbar.

---

## Taiwan-Marktinformationen

RASAGILINE TARTRATE hat derzeit keine Zulassung in Taiwan. Es sind keine Zulassungsunterlagen verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Dem Evidence Pack fehlen die drei Mindestanforderungen für die Bewertung: (1) TxGNN-Vorhersage-Indikationen, (2) Wirkmechanismus und (3) Sicherheitsprofil. Ohne diese können weder biologische Plausibilität noch Risiko bewertet werden.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[Blockierend — DG001]** Analysieren Sie die TFDA-Packungsbeilage-PDF (Abfrage bestätigt 1 Ergebnis vorhanden), um Folgendes zu extrahieren: zugelassene Indikationen, wichtige Warnhinweise und Kontraindikationen
- **[Hoch — DG002]** Rufen Sie Wirkmechanismus und DrugBank-ID aus dem DrugBank-Datensatz ab (Abfrage bestätigt 1 Ergebnis vorhanden) und füllen Sie die Felder `drugbank_id`, `original_moa` und `original_indications` aus
- **[Erforderlich]** Führen Sie die TxGNN-Vorhersage-Pipeline erneut aus, um `predicted_indications` auszufüllen – die aktuelle Ausgabe ist leer, was auf ein Problem bei der Verbindungsnamenabfrage hindeuten kann (erwägen Sie eine Abfrage unter „Rasagiline" ohne das Salz-Suffix „tartrate")
- **[Empfohlen]** Bestätigen Sie die Verbindungsidentität: Überprüfen Sie, ob RASAGILINE TARTRATE und Rasagiline-Mesilat (die häufiger vermarktete Salzform) in diesem Zusammenhang ein und derselbe Kandidat sind, um zu vermeiden, dass vorhandene Evidenz übersehen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

