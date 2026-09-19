---
layout: default
title: Rimegepant
parent: Nur Modellvorhersage (L5)
nav_order: 343
evidence_level: L5
indication_count: 6
---

# Rimegepant
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

# RIMEGEPANT: Umwidmungsbewertung — Unzureichende Daten zum Abschluss der Bewertung

## Zusammenfassung

RIMEGEPANT (DrugBank: DB12457) ist ein Kleinmolekül-Wirkstoff, der am 2026-03-29 durch die TxGNN-Umwidmungs-Pipeline abgefragt wurde.
Das aktuelle Evidence Pack enthält **keine von TxGNN vorhergesagten Indikationen**, keine bestätigte Ursprungsindikation und keine Wirkmechanismus-Daten.
Eine vollständige Umwidmungsbewertung kann in dieser Phase nicht durchgeführt werden; dieser Bericht dokumentiert den aktuellen Datenzustand und definiert die Mindestanforderungen zum Fortfahren.

---

## Kurzübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Im aktuellen Evidence Pack nicht verfügbar |
| Vorhergesagte neue Indikation | Keine Vorhersagen zurückgegeben |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | N/A — Keine Vorhersagen zur Bewertung |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten — Kritische Daten fehlen** |

---

## Taiwan-Marktinformationen

RIMEGEPANT hat derzeit **keine Arzneimittellizenzen, die in Taiwan registriert sind**. Es gibt keine zugelassenen Produkte, Darreichungsformen oder Indikationen im Datensatz der TFDA zum Stichtag (2026-04-20).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack hat keine TxGNN-Vorhersagen zurückgegeben und es fehlen sowohl die Daten zur ursprünglichen Indikation als auch die Wirkmechanismus-Informationen, was es unmöglich macht, die Umwidmungs-Begründung, die Evidenzstärke oder die Sicherheitsrelevanz zu diesem Zeitpunkt zu bewerten.

**Um fortzufahren, wird folgendes benötigt:**

- **TxGNN-Vorhersagen** — Führen Sie die TxGNN-Pipeline für DB12457 erneut aus und bestätigen Sie, dass `predicted_indications` mit Daten gefüllt ist, bevor Sie einen vollständigen Bericht generieren
- **Ursprüngliche Indikation** — Rufen Sie zugelassene Indikation(en) von DrugBank oder dem FDA/EMA-Label ab (RIMEGEPANT ist außerhalb Taiwans unter Markennamen wie Nurtec ODT und Vydura im Handel erhältlich)
- **Wirkmechanismus** — Fragen Sie die DrugBank-API nach MOA ab; RIMEGEPANT ist ein CGRP-Rezeptor-Antagonist – dies sollte aus dem öffentlichen DrugBank-Datensatz bestätigt werden können
- **Sicherheitsdaten** — Laden Sie die TFDA-Packungsbeilage als PDF herunter und analysieren Sie sie, um wichtige Warnhinweise und Gegenanzeigen zu extrahieren (Datenlücke DG001, Schweregrad: Blockierend)
- **DDI-Profil** — Führen Sie die DDI-Datenbank erneut ab; die aktuelle Abfrage hat `not_found` zurückgegeben, was eine Datenbeschaffungslücke widerspiegeln kann, anstatt eines Fehlens von Wechselwirkungen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

