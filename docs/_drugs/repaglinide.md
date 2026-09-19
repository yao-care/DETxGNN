---
layout: default
title: Repaglinide
parent: Nur Modellvorhersage (L5)
nav_order: 336
evidence_level: L5
indication_count: 0
---

# Repaglinide
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

# Repaglinide: Evaluierung der Neuindikation — Unvollständiges Nachweispaket (Keine TxGNN-Vorhersagen verfügbar)

---

## Zusammenfassung in einem Satz

Repaglinide (DB00912) ist ein kurzwirksames Insulinsekretagogum der Meglitinid-Klasse, das für Diabetes mellitus Typ 2 indiziert ist. Dieses Nachweispaket (v4, Datenschnitt 2026-04-20) enthält **keine TxGNN-prognostizierten Indikationen**, was eine standardmäßige Evaluierung der Neuindikation in dieser Phase unmöglich macht. Kritische Datenlücken bestehen in der MOA-Dokumentation, Sicherheitsinformationen und dem deutschen Marktstatus – alle müssen behoben werden, bevor die Evaluierung fortgesetzt werden kann.

---

## Schnellübersicht

| Element | Inhalt |
|---|---|
| Ursprüngliche Indikation | Diabetes mellitus Typ 2 (Meglitinid-Klasse Insulinsekretagogum; Quelle: DrugBank DB00912) |
| Prognostizierte neue Indikation | Nicht verfügbar — `predicted_indications`-Array ist leer |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzstufe | N/A |
| Marktstatus Deutschland | Nicht zugelassen (0 Zulassungen erfasst) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** — unzureichende Daten zur Evaluierung |

---

## Warum ist diese Evaluierung unvollständig?

Das Nachweispaket enthält zwei blockierende Lücken, die verhindern, dass ein standardmäßiger Bericht zur Neuindikation erstellt wird:

**1. Keine TxGNN-prognostizierten Indikationen.** Das Feld `predicted_indications` ist ein leeres Array. Ohne ein Kandidaten-Krankheitsziel können keine der standardmäßigen Abschnitte – Zuordnung klinischer Studien, Literaturübersicht, mechanistische Begründung oder Zytotoxizitätsbewertung – gefüllt werden. Dies könnte darauf hindeuten, dass die TxGNN-Pipeline für dieses Arzneimittel noch nicht ausgeführt wurde, oder dass Ergebnisse vor der Zusammenstellung dieses Pakets gefiltert wurden.

**2. Wirkmechanismus (MOA)-Daten fehlen (DG002, Schweregrad: Hoch).** Bekannt ist, dass Repaglinide ATP-sensitive Kaliumkanäle auf pankreatischen β-Zellen schließt und die glukoseabhängige Insulinsekretion stimuliert. Diese Information ist jedoch nicht im Nachweispaket vorhanden und wurde als Datenlücke gekennzeichnet. Der Lösungsweg (DrugBank-API-Abfrage) wurde identifiziert, aber noch nicht ausgeführt.

**3. Sicherheitsdaten fehlen vollständig (DG001, Schweregrad: Blockierend).** Alle Einträge in `key_warnings`, `contraindications` und DDI tragen den Status `[Data Gap]` oder `not_found`. Dies wird im Meta-Bereich als blockierende Lücke klassifiziert, was bedeutet, dass die Pipeline nicht zum Sicherheitsscreening (S1) voranschreiten sollte, ohne zunächst das Beipackzettel-PDF von der TFDA/BfArM-offiziellen Quelle herunterzuladen und zu analysieren.

---

## Informationen zum Marktstatus Deutschland

Für Repaglinide sind derzeit keine Zulassungen in diesem Nachweispaket erfasst. Die `taiwan_regulatory`-Abfrage (BfArM) gab am 2026-03-29 0 Ergebnisse zurück.

> **Hinweis:** Repaglinid-haltige Produkte (z. B. NovoNorm®) sind in mehreren Märkten weltweit zugelassen. Das Fehlen von Einträgen hier spiegelt wahrscheinlich eine Datenbeschaffungslücke wider und nicht eine echte Nicht-Zulassung. Dies sollte vor der Schlussfolgerung „nicht zugelassen" direkt in der BfArM-Produktdatenbank überprüft werden.

---

## Sicherheitsaspekte

Alle Sicherheitsfelder in diesem Nachweispaket sind `[Data Gap]`. Nach Berichterstattungsregeln sind keine Sicherheitselemente aufgeführt.

> Bitte beachten Sie das Beipackzettel für Sicherheitsinformationen. Besondere Aufmerksamkeit sollte auf Hypoglykämierisiko, Kontraindikation bei Leberfunktionsstörung und CYP2C8/CYP3A4-vermittelte Arzneimittelwechselwirkungen gelegt werden, die für diese Arzneimittelklasse etabliert sind.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Nachweispaket ist strukturell unvollständig – es gibt keine TxGNN-Vorhersagen zur Evaluierung, und zwei blockierende Datenlücken (Sicherheitsdaten, MOA) verhindern, dass die Evaluierungs-Pipeline zu einer nachgelagerten Phase voranschreitet.

**Zum Fortfahren ist Folgendes erforderlich:**

- [ ] **TxGNN-Pipeline neu ausführen** für Repaglinide (DB00912) und `predicted_indications` mit mindestens den Top-bewerteten Krankheitskandidaten und ihren Scores füllen.
- [ ] **DG001 (Blockierend) beheben:** Beipackzettel-PDF für Repaglinide von TFDA/BfArM herunterladen und analysieren, um wichtige Warnungen und Kontraindikationen zu extrahieren.
- [ ] **DG002 (Hoch) beheben:** DrugBank-API für den vollständigen MOA-Eintrag abfragen und `original_moa` füllen.
- [ ] **Marktstatus Deutschland überprüfen:** BfArM-Produktdatenbank auf Zulassungen für NovoNorm® oder äquivalente Repaglinide-Produkte überprüfen; das aktuelle 0-Ergebnis ist wahrscheinlich eine Datenlücke und kein tatsächliches Fehlen der behördlichen Zulassung.
- [ ] **Nachweispaket neu generieren** (v5+), sobald die oben genannten Lücken geschlossen sind, und dann diese Berichtvorlage mit gefülltem `predicted_indications[0]` neu ausführen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

