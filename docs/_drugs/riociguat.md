---
layout: default
title: Riociguat
parent: Nur Modellvorhersage (L5)
nav_order: 344
evidence_level: L5
indication_count: 0
---

# Riociguat
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

# Riociguat: Bewertung unvollständig — Unzureichende Daten für Umwidmungsanalyse

## Zusammenfassung in einem Satz

Riociguat (DrugBank-ID: DB08931) wurde als Kandidat für eine Umwidmungsbewertung identifiziert.
Das aktuelle Evidence Pack enthält jedoch **keine von TxGNN vorhergesagten Indikationen**, **keine Aufzeichnungen der Originalindikation** und **keine Sicherheitsdaten**,
was eine aussagekräftige mechanistische oder klinische Evidenzbewertung in diesem Stadium unmöglich macht.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|---------|
| Originalindikation | Nicht verfügbar in diesem Evidence Pack |
| Vorhergesagte neue Indikation | Keine TxGNN-Vorhersagen generiert |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | Nicht bewertbar |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aussetzen** |

---

## Warum keine Bewertung möglich ist

Dem Evidence Pack für Riociguat fehlen drei kritische Datenkategorien:

**1. Keine Daten zur Originalindikation**
Das Feld `original_indications` ist leer, und keine Daten des genehmigten Produktetiketts (Beipackzettel) wurden in strukturierte Form geparst. Ohne Kenntnis des genehmigten therapeutischen Kontexts des Arzneistoffs ist eine mechanistische Verknüpfung mit einer neuen Indikation nicht möglich.

**2. Kein Wirkmechanismus (MOA)**
MOA-Daten sind als kritische Lücke gekennzeichnet (`DG002`). Ohne Kenntnis darüber, wie Riociguat seine pharmakologische Wirkung ausübt, ist es nicht möglich, die mechanistische Anwendbarkeit auf andere Erkrankungen zu bewerten.

**3. Keine TxGNN-Vorhersagen**
Das Array `predicted_indications` ist leer. Das bedeutet, dass das TxGNN-Wissensgraph-Modell dieses Arzneimittel entweder noch nicht verarbeitet hat oder das Arzneimittel die Mindestpunktschwelle zur Generierung von Kandidatenindikationen nicht erfüllt hat. Bis Vorhersagen generiert werden, kann keine Evidenzprüfung fortgesetzt werden.

---

## Sicherheitsaspekte

Bitte beachten Sie den Beipackzettel für Sicherheitsinformationen.

> Hinweis: Eine Beipackzettel-Abfrage (`tfda_package_insert`) wurde am 2026-03-29 mit dem Status `success` ausgeführt, was darauf hinweist, dass Quellenmaterial vorhanden ist. Strukturierte Sicherheitsfelder (Warnhinweise, Gegenanzeigen, Arzneimittelwechselwirkungen) wurden jedoch nicht aus dieser Quelle in das Evidence Pack geparst.

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Es gibt derzeit keine von TxGNN vorhergesagten Indikationen und keine strukturierten Arzneimittel-Daten verfügbar; eine Fortführung zu einer beliebigen Phase der Umwidmungsanalyse wäre verfrüht und methodisch nicht vertretbar.

**Um fortzufahren, ist folgendes erforderlich:**

1. **Beipackzettel parsen** — Die `tfda_package_insert`-Abfrage hat ein Ergebnis zurückgegeben (2026-03-29). Extrahieren und strukturieren Sie die genehmigten Indikationen, Warnhinweise und Gegenanzeigen aus diesem Dokument in das Evidence Pack.
2. **MOA von DrugBank abrufen** — Die DrugBank-Abfrage hat ein Ergebnis zurückgegeben (`result_count: 1`). Extrahieren Sie den Wirkmechanismus, die pharmakologische Klasse und die Arzneimittelkategorien, um `original_moa` zu füllen.
3. **TxGNN-Vorhersage-Pipeline neu ausführen** — Nachdem die Arzneimittel-Metadaten gefüllt sind, reichen Sie Riociguat erneut beim TxGNN-Modell ein, um bewertete Kandidatenindikationen zu generieren.
4. **DDI-Abfrage erneut ausführen** — Die aktuelle DDI-Abfrage hat `not_found` zurückgegeben. Nachdem MOA und Arzneimittelklasse bestätigt sind, fragen Sie die DDI-Datenbank erneut mit erweiterten Arzneimittelprofilparametern ab.
5. **Aktualisiertes Evidence Pack generieren (v5)** — Erst nach Abschluss der Schritte 1–4 sollte ein vollständiger Bewertungsbericht generiert werden.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

