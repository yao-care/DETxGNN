---
noindex: true
sitemap: false
layout: default
title: Repaglinide
parent: Nur Modellvorhersage (L5)
nav_order: 394
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
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

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Repaglinide: Evaluierung der Neuindikation — Unvollständiges Nachweispaket (Keine TxGNN-Vorhersagen verfügbar)
{: .text-alpha }

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
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 5 von 6) |
| Anzahl der Zulassungen | 6 (gültig: 5) |
| Empfohlene Entscheidung | **Halten** — unzureichende Daten zur Evaluierung |

---

## Warum ist diese Evaluierung unvollständig?

Das Nachweispaket enthält zwei blockierende Lücken, die verhindern, dass ein standardmäßiger Bericht zur Neuindikation erstellt wird:

**1. Keine TxGNN-prognostizierten Indikationen.** Das Feld `predicted_indications` ist ein leeres Array. Ohne ein Kandidaten-Krankheitsziel können keine der standardmäßigen Abschnitte – Zuordnung klinischer Studien, Literaturübersicht, mechanistische Begründung oder Zytotoxizitätsbewertung – gefüllt werden. Dies könnte darauf hindeuten, dass die TxGNN-Pipeline für dieses Arzneimittel noch nicht ausgeführt wurde, oder dass Ergebnisse vor der Zusammenstellung dieses Pakets gefiltert wurden.

**2. Wirkmechanismus (MOA)-Daten fehlen (DG002, Schweregrad: Hoch).** Bekannt ist, dass Repaglinide ATP-sensitive Kaliumkanäle auf pankreatischen β-Zellen schließt und die glukoseabhängige Insulinsekretion stimuliert. Diese Information ist jedoch nicht im Nachweispaket vorhanden und wurde als Datenlücke gekennzeichnet. Der Lösungsweg (DrugBank-API-Abfrage) wurde identifiziert, aber noch nicht ausgeführt.

**3. Sicherheitsdaten fehlen vollständig (DG001, Schweregrad: Blockierend).** Alle Einträge in `key_warnings`, `contraindications` und DDI tragen den Status `[Data Gap]` oder `not_found`. Dies wird im Meta-Bereich als blockierende Lücke klassifiziert, was bedeutet, dass die Pipeline nicht zum Sicherheitsscreening (S1) voranschreiten sollte, ohne zunächst das Beipackzettel-PDF von der BfArM-offiziellen Quelle herunterzuladen und zu analysieren.

<!-- review:begin de-lic-20261106-repaglinide-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Dies wird im Meta-Bereich als blockierende Lücke klassifiziert, was bedeutet, dass die Pipeline nicht zum Sicherheitsscreening (S1) voranschreiten sollte, ohne zunächst das Beipackzettel-PDF von der TFDA/BfArM-offiziellen Quelle herunterzuladen und zu analysieren.“ Entfernt: Textbaustein aus der taiwanischen Vorlage (TFDA), der für diese Seite nicht gilt. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-repaglinide-2 -->

---

## Informationen zum Marktstatus Deutschland

> **Hinweis:** Repaglinid-haltige Produkte (z. B. NovoNorm®) sind in mehreren Märkten weltweit zugelassen.

<!-- review:begin de-lic-20261106-repaglinide-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Für Repaglinide sind derzeit keine Zulassungen in diesem Nachweispaket erfasst. Die `taiwan_regulatory`-Abfrage (BfArM) gab am 2026-03-29 0 Ergebnisse zurück.“ Entfernt: Textbaustein aus der taiwanischen Vorlage (TFDA), der für diese Seite nicht gilt. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-repaglinide-1 -->

<!-- review:begin de-lic-20261106-repaglinide-3 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „NovoNorm®) sind in mehreren Märkten weltweit zugelassen. Das Fehlen von Einträgen hier spiegelt wahrscheinlich eine Datenbeschaffungslücke wider und nicht eine echte Nicht-Zulassung. Dies sollte vor der Schlussfolgerung „nicht zugelassen" direkt in der BfArM-Produktdatenbank überprüft werden.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 6 Zulassungen erfasst, davon 5 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-repaglinide-3 -->

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
- [ ] **DG001 (Blockierend) beheben:** Beipackzettel-PDF für Repaglinide von BfArM herunterladen und analysieren, um wichtige Warnungen und Kontraindikationen zu extrahieren.
- [ ] **DG002 (Hoch) beheben:** DrugBank-API für den vollständigen MOA-Eintrag abfragen und `original_moa` füllen.
- [ ] **Marktstatus Deutschland überprüfen:** BfArM-Produktdatenbank auf Zulassungen für NovoNorm® oder äquivalente Repaglinide-Produkte überprüfen.
- [ ] **Nachweispaket neu generieren** (v5+), sobald die oben genannten Lücken geschlossen sind, und dann diese Berichtvorlage mit gefülltem `predicted_indications[0]` neu ausführen.

<!-- review:begin de-lic-20261106-repaglinide-4 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „[ ] **DG001 (Blockierend) beheben:** Beipackzettel-PDF für Repaglinide von TFDA/BfArM herunterladen und analysieren, um wichtige Warnungen und Kontraindikationen zu extrahieren.“ Entfernt: Textbaustein aus der taiwanischen Vorlage (TFDA), der für diese Seite nicht gilt. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-repaglinide-4 -->

<!-- review:begin de-lic-20261106-repaglinide-5 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „[ ] **Marktstatus Deutschland überprüfen:** BfArM-Produktdatenbank auf Zulassungen für NovoNorm® oder äquivalente Repaglinide-Produkte überprüfen; das aktuelle 0-Ergebnis ist wahrscheinlich eine Datenlücke und kein tatsächliches Fehlen der behördlichen Zulassung.“ Entfernt: Die Aussage widersprach den Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 6 Zulassungen erfasst, davon 5 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-repaglinide-5 -->

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Für Repaglinide sind derzeit keine Zulassungen in diesem Nachweispaket erfasst. Die `taiwan_regulatory`-Abfrage (BfArM) gab am 2026-03-29 0 “ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „TFDA/“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „Das Fehlen von Einträgen hier spiegelt wahrscheinlich eine Datenbeschaffungslücke wider und nicht eine echte Nicht-Zulassung. Dies sollte vo“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „TFDA/“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „das aktuelle 0-Ergebnis ist wahrscheinlich eine Datenlücke und kein tatsächliches Fehlen der behördlichen Zulassung“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

