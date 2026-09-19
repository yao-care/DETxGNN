---
layout: default
title: Remdesivir
parent: Nur Modellvorhersage (L5)
nav_order: 335
evidence_level: L5
indication_count: 6
---

# Remdesivir
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

# Remdesivir: Evaluation der Arzneimittelumwidmung (Daten unzureichend)

## Zusammenfassung in einem Satz

Remdesivir (DB14761) ist ein international anerkanntes Breitspektrum-Antivirus-Mittel zur COVID-19-Behandlung. Dieses Evidence Pack enthält jedoch **keine von TxGNN vorhergesagten Indikationen** und entbehrt kritischer Dateneingaben — einschließlich Wirkungsmechanismus, Sicherheitswarnungen und taiwanesischer Regulierungsunterlagen. Eine vollständige Bewertung der Arzneimittelumwidmung **kann in dieser Phase nicht durchgeführt werden**; der nachstehende Bericht spiegelt nur das wider, was derzeit verfügbar ist.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht erfasst in diesem Evidence Pack |
| Vorhergesagte neue Indikation | Keine Vorhersagen generiert |
| TxGNN-Vorhersage-Score | — |
| Evidenzstufe | L5 (Modell-Vorhersage-Pipeline unvollständig) |
| Status auf dem taiwanesischen Markt | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum ist diese Vorhersage angemessen?

In `predicted_indications` sind keine TxGNN-Vorhersagen vorhanden. Ohne eine Zielindikation können keine mechanistischen Verbindungen oder Umwidmungsrationale konstruiert werden.

Das Wirkungsmechanismus-Feld ist als Datenlücke aufgeführt (DG002, hoher Schweregrad). Remdesivir wird allgemein als RNA-abhängige RNA-Polymerase (RdRp)-Inhibitor verstanden; dies wurde jedoch **durch die aktuellen Dateneingaben nicht bestätigt** und sollte für diesen Bericht nicht als verifiziert behandelt werden.

Bis sowohl TxGNN-Vorhersagen als auch MOA-Daten verfügbar sind, kann die biologische Plausibilität einer potenziellen neuen Indikation nicht bewertet werden.

---

## Taiwan-Marktinformation

Remdesivir verfügt derzeit über **keine genehmigten Lizenzen in Taiwan** (TFDA-Abfrage ergab 0 Ergebnisse). Es gibt keine Dosierungsformen oder genehmigten Indikationen in den Unterlagen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

> **Hinweis:** Die TFDA-Fachinformations-Abfrage (query_log ID 4) lieferte ein Ergebnis, aber die Sicherheitsfelder — Warnungen, Kontraindikationen und Arzneimittelwechselwirkungen — bleiben in diesem Evidence Pack ungefüllt. Dies wird als Blocking-Datenlücke (DG001) identifiziert, die behoben werden muss, bevor eine Sicherheitsvor-Bewertung beginnen kann.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die TxGNN-Vorhersage-Pipeline hat keine Kandidaten-Indikationen für Remdesivir erzeugt, und zwei kritische Datenlücken (MOA und TFDA-Sicherheitsdaten) bleiben ungelöst. Es gibt derzeit kein Umwidmungssignal zu bewerten.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[DG001 — Blocking]** TFDA-Fachinformations-PDF abrufen und Warnungen/Kontraindikationen analysieren, bevor die Sicherheitsvor-Bewertung beginnt
- **[DG002 — High]** DrugBank-API abfragen, um bestätigte Wirkungsmechanismus-Daten zu erhalten; die aktuelle DrugBank-Abfrage (query_log ID 3) lieferte 1 Datensatz, aber befüllte das MOA-Feld nicht — Extraktionslogik untersuchen
- **TxGNN-Vorhersage-Pipeline erneut ausführen**, um `predicted_indications` zu generieren; ohne Vorhersagen gibt es kein Umwidmungsziel
- Sobald eine Zielindikation bestätigt ist, entsprechend klinische Studien- und Fachliteraturbelege sammeln
- Drug Interaction Profiling durchführen (DDI-Abfrage ergab 0 Ergebnisse; überprüfen, ob dies ein echtes Fehlen oder ein Abfrage-Scope-Problem widerspiegelt)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

