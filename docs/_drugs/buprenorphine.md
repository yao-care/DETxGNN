---
layout: default
title: Buprenorphine
parent: Nur Modellvorhersage (L5)
nav_order: 73
evidence_level: L5
indication_count: 6
---

# Buprenorphine
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

# Buprenorphin: Kandidat für Arzneimittelumwidmung — Keine Vorhersagedaten verfügbar

## Zusammenfassung in einem Satz

Buprenorphin (DB00921) ist ein zugelassenes Arzneimittel, aber dieses Evidence-Paket enthält keine erfassten Originalindikationen und keine TxGNN-prognostizierten neuen Indikationen.
Ohne eine Zielindikation kann eine formale Bewertung der Arzneimittelumwidmung in diesem Stadium nicht abgeschlossen werden.
Eine Datenbereinigung ist erforderlich, bevor die Bewertung fortgesetzt werden kann.

---

## Kurzer Überblick

| Element | Inhalt |
|---------|--------|
| Originalindikation | Nicht verfügbar |
| Prognostizierte neue Indikation | Keine Vorhersage generiert |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | N/A |
| Status auf dem taiwanischen Markt | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Sicherheitsaspekte

Weitere Informationen zur Sicherheit finden Sie in der Packungsbeilage.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Dieses Evidence-Paket enthält keine TxGNN-prognostizierten Indikationen und keine Originaldaten zur Indikation, was es unmöglich macht, eine Bewertung der Arzneimittelumwidmung durchzuführen oder die mechanistische Plausibilität zu evaluieren.

**Zum Fortfahren wird Folgendes benötigt:**

- **TxGNN-Vorhersage-Ausgabe** — `predicted_indications` ist derzeit leer; das Modell muss erneut ausgeführt oder die Ergebnisse für diesen Kandidaten aufgenommen werden
- **Originaldaten zur Indikation** — `original_indications` ist leer; diese aus der TFDA oder den zugelassenen Indikationsfeldern der DrugBank abrufen
- **Wirkungsmechanismus (MOA)** — gekennzeichnet als Datenlücke (DG002, hoher Schweregrad); DrugBank-API (DB00921) abfragen, um `original_moa` auszufüllen
- **Sicherheitsdaten** — `key_warnings` und `contraindications` sind beide als Datenlücke gekennzeichnet (DG001, blockierender Schweregrad); TFDA-Packungsbeilage-PDF herunterladen und analysieren, um die S1-Sicherheitsprüfung freizugeben
- **DDI-Daten** — Abfrage zu Arzneimittel-Wechselwirkungen ergab `not_found`; erwägen Sie, zusätzliche Quellen abzufragen (z. B. DrugBank-Interactions-Endpunkt, Lexicomp)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

