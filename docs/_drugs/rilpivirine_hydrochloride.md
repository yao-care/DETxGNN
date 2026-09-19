---
layout: default
title: Rilpivirine Hydrochloride
parent: Nur Modellvorhersage (L5)
nav_order: 341
evidence_level: L5
indication_count: 0
---

# Rilpivirine Hydrochloride
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

# Rilpivirine Hydrochlorid: Bewertung der Arzneistoff-Neuindikation — Vorhersagen noch nicht verfügbar

## Zusammenfassung in einem Satz

Rilpivirine Hydrochlorid ist ein nicht-nukleosidischer Reverse-Transkriptase-Inhibitor (NNRTI) der antiretroviralen Wirkstoffklasse mit etabliertem Einsatz zur Behandlung der HIV-1-Infektion auf globalen Märkten. Das aktuelle Evidence Pack enthält **keine TxGNN-vorhergesagten neuen Indikationen**, und das Arzneimittel **ist nicht in Taiwan vermarktet** mit null TFDA-Genehmigungen in der Aufzeichnung. Aufgrund kritischer Datenlücken beim Wirkmechanismus, Sicherheitsdaten und Modellausgabe kann eine vollständige Bewertung der Arzneistoff-Neuindikation in diesem Stadium nicht erstellt werden.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Nicht in Evidence Pack aufgeführt (NNRTI-Klasse; weltweit für HIV-1-Infektion angezeigt) |
| Vorhergesagte neue Indikation | Keine Vorhersagen generiert |
| TxGNN-Vorhersage-Score | — |
| Evidenzstufe | L5 — Keine Modellausgabe verfügbar |
| Taiwan Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Aussetzen** |

---

## Warum ist diese Vorhersage angemessen?

Keine vorhergesagten Indikationen wurden von der TxGNN-Pipeline für dieses Arzneimittel im aktuellen Evidence Pack zurückgegeben. Eine mechanistische Begründung für eine Neuindikations-Hypothese kann daher nicht dargelegt werden.

Detaillierte Daten zum Wirkmechanismus sind in diesem Evidence Pack nicht verfügbar. Basierend auf der pharmakologischen Klasse ist Rilpivirine Hydrochlorid weltweit als NNRTI bekannt, der die HIV-1-Reverse-Transkriptase selektiv hemmt, indem er an einer allosterischen Stelle bindet und die virale RNA-abhängige und DNA-abhängige DNA-Polymerase-Aktivität blockiert. Seine etablierte klinische Rolle liegt in der HIV-1-Infektion – typischerweise als Teil vollständiger Behandlungsschemata (z. B. kombiniert mit emtricitabine/tenofovir). Da jedoch weder die Felder `original_moa` noch `original_indications` in diesem Evidence Pack gefüllt wurden, kann dieser Hintergrund anhand der bereitgestellten Daten nicht formal bestätigt werden.

Neuindikations-Hypothesen für NNRTIs sind in Onkologie- und Immunologieliteratur erschienen (z. B. Reverse-Transkriptase-Hemmung von endogenen Retroelementen bei Krebs), aber ohne einen TxGNN-Vorhersage-Score zum Verankern der Analyse würde jede weitere Diskussion spekulativ sein und wird daher weggelassen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Das Evidence Pack enthält nicht alle Komponenten, die für eine Bewertung der Arzneistoff-Neuindikation erforderlich sind: keine TxGNN-vorhergesagten Indikationen, kein Wirkmechanismus, keine Sicherheits- oder Kontraindikationsdaten und keine Behördengenehmigungen aus Taiwan. Eine Weiterleitung zu klinischer oder behördlicher Bewertung ist im gegenwärtigen Zustand nicht möglich.

**Um fortzufahren, ist Folgendes erforderlich:**

- **TxGNN-Vorhersage-Pipeline erneut ausführen** — das Array predicted_indications ist leer; bestätigen, ob das Modell ausgeführt wurde und keine Ergebnisse zurückgab oder ob die Pipeline in einem früheren Schritt fehlgeschlagen ist
- **MOA aus DrugBank extrahieren** — das Abfragelog zeigt, dass DrugBank 1 Ergebnis zurückgab (`result_count: 1`); diese Daten wurden nicht in das Feld `drug.original_moa` propagiert und sollten abgerufen werden
- **Sicherheitswarnungen aus der TFDA-Fachinformation extrahieren** — das Abfragelog zeigt, dass `tfda_package_insert` 1 Ergebnis zurückgab (`result_count: 1`); key_warnings und Kontraindikationen sollten aus dieser Quelle gefüllt werden
- **original_indications ausfüllen** — das Feld ist leer, obwohl DrugBank- und Fachinformationsdaten verfügbar sind; mit der abgerufenen behördlichen Dokumentation abgleichen
- **Taiwan-Marktstatus bestätigen** — das Arzneimittel wird weltweit unter Markennamen vermarktet (z. B. Edurant, Odefsey, Juluca); prüfen, ob es in Taiwan unter einem Kombinationsprodukt oder unter unterschiedlicher INN-Schreibweise registriert ist
- **DG001 (Blocking) lösen** — Warnungen/Kontraindikationen in der TFDA-Fachinformation müssen gelöst werden, bevor eine Sicherheitsstufenbewertung beginnen kann

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

