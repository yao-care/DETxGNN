---
layout: default
title: Risperidone
parent: Nur Modellvorhersage (L5)
nav_order: 348
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Risperidon: Bewertung ausstehend — Keine Umwidmungsprognose verfügbar

## Zusammenfassung in einem Satz

Risperidon (DB00734) ist ein bekanntes atypisches Antipsychotikum, das häufig bei Schizophrenie und verwandten Erkrankungen eingesetzt wird. Das aktuelle Evidence Pack enthält jedoch **keine von TxGNN vorhergesagten Umwidmungsindikationen**, keine Wirkmechanismus-Daten und keine Sicherheitsdatensätze – was eine aussagekräftige Umwidmungsbewertung in diesem Stadium unmöglich macht. **Sofortige Datenkorrekturen sind erforderlich, bevor dieser Kandidat voranschreiten kann.**

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | In diesem Evidence Pack nicht dokumentiert |
| Vorhergesagte neue Indikation | K.A. — Keine Vorhersagen verfügbar |
| TxGNN-Prognosescore | K.A. |
| Evidenzstufe | L5 (nur Modellvorhersage — derzeit nicht einmal erreicht) |
| Status auf taiwanesischem Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum keine Bewertung durchgeführt werden kann

Die TxGNN-Prognosepipeline hat **null vorhergesagte Indikationen** für Risperidon in dieser Evidence-Pack-Version (v4, Datenstand 2026-04-20) zurückgegeben. Dies ist ein Problem in der vorgelagerten Pipeline und kein Ausdruck des klinischen Potenzials von Risperidon.

Zwei kritische Datenlücken wurden formal identifiziert:

| Lücken-ID | Kategorie | Fehlendes Element | Schweregrad | Auswirkung |
|-----------|-----------|-------------------|-------------|-----------|
| DG001 | Arzneimitteleben | Packungsbeilage-Warnungen / Kontraindikationen | **Blockierend** | S1-Sicherheitsscreening kann nicht durchgeführt werden |
| DG002 | Arzneimitteleben | Wirkmechanismus (MOA) | Hoch | Analyse der mechanistischen Relevanz kann nicht durchgeführt werden |

Bis die TxGNN-Pipeline mindestens eine vorhergesagte Indikation erzeugt und bis DG001 gelöst ist, können keine nachgelagerten Bewertungen (Mechanismus-Analyse, Zuordnung klinischer Studien oder Sicherheitsprofilerstellung) voranschreiten.

---

## Evidence aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien für diesen Kandidaten registriert.

*(Voraussetzung: Eine von TxGNN vorhergesagte Indikation muss verfügbar sein, bevor die Studien-Zuordnung durchgeführt wird.)*

---

## Literatur-Evidence

Derzeit ist keine verwandte Literatur verfügbar.

*(Voraussetzung: Eine von TxGNN vorhergesagte Indikation muss verfügbar sein, bevor die Literatursuche durchgeführt wird.)*

---

## Marktsituation in Taiwan

Risperidon hat nach der aktuellen TFDA-Abfrage **keine registrierten Lizenzen** auf dem taiwanesischen Markt (abgefragt 2026-03-29, Ergebnisanzahl: 0).

> Anmerkung: Die TFDA-Packungsbeilage-Abfrage (Abfrage-ID 4) hat 1 Ergebnis zurückgegeben – dies könnte darauf hindeuten, dass eine Packungsbeilage für Referenzzwecke vorhanden ist, auch ohne aktive Vermarktungsgenehmigung. Die Packungsbeilage sollte abgerufen und analysiert werden, um DG001 zu beheben.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Alle Sicherheitsfelder – Hauptwarnungen, Kontraindikationen und Arzneimittel-Wechselwirkungen – haben im aktuellen Evidence Pack keine Daten zurückgegeben. DDI-Abfragestatus: nicht gefunden.)*

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack für Risperidon (v4) ist strukturell unvollständig – es wurden keine TxGNN-Umwidmungsprognosen erstellt, und zwei kritische Datenlücken (DG001, DG002) blockieren das Sicherheitsscreening und die mechanistische Analyse. Es gibt derzeit keine bewertbare Umwidmungshypothese.

**Zum Fortfahren ist Folgendes erforderlich:**

1. **TxGNN-Prognosepipeline neu ausführen** für DB00734 und bestätigen, dass mindestens eine vorhergesagte Indikation zurückgegeben wird
2. **DG001 beheben** — Die TFDA-Packungsbeilage-PDF (1 Dokument im Abfragelog gefunden) herunterladen und analysieren, um Warnungen und Kontraindikationen zu extrahieren
3. **DG002 beheben** — DrugBank-API für den vollständigen Wirkmechanismus, die pharmakologische Klasse und die Ziele von Risperidon abfragen
4. **DDI-Abfrage neu ausführen** — Der aktuelle Status ist `not_found`; Abfrageparameter überprüfen und erneut versuchen
5. **Evidence Pack neu generieren** (v5+) sobald die obigen Daten verfügbar sind, dann erneut zur Bewertung einreichen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

