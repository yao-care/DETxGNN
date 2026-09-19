---
layout: default
title: Ravulizumab
parent: Nur Modellvorhersage (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: Bewertung der Arzneimittel-Umwidmung — Evidenzpaket unvollständig

## Zusammenfassung in einem Satz

Ravulizumab (DrugBank-ID: DB11580) ist ein Arzneimittel, bei dem dieses Evidenzpaket unzureichende Daten für eine standardmäßige Bewertung der Arzneimittel-Umwidmung enthält. Das TxGNN-Modell hat **keine prognostizierten Indikationen** für diesen Kandidaten zurückgegeben, und sowohl die ursprünglichen Indikationsdaten als auch die Mechanismus-der-Wirkung-Informationen fehlen. Eine vollständige Bewertung kann erst durchgeführt werden, wenn die unten aufgeführten Datenlücken geschlossen werden.

---

## Schnelle Übersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | In diesem Evidenzpaket nicht verfügbar |
| Vorhergesagte neue Indikation | Keine TxGNN-Vorhersage zurückgegeben |
| TxGNN-Vorhersage-Score | N/A |
| Evidenz-Niveau | L5 — Modell hat keine Ausgabe zurückgegeben; keine unterstützenden Studien |
| Status am taiwanesischen Markt | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aussetzung** |

---

## Warum die Bewertung nicht fortgesetzt werden kann

Dieses Evidenzpaket fehlen drei Komponenten, die jeweils eigenständig erforderlich sind, bevor eine Bewertung der Arzneimittel-Umwidmung geschrieben werden kann:

**1. Keine prognostizierte Indikation.** Das Feld `predicted_indications` ist leer. Das TxGNN-Modell hat keine Kandidatenerkrankung für dieses Arzneimittel zurückgegeben. Ohne eine prognostizierte Zielindikation gibt es keine Umwidmungshypothese zu bewerten — die zentrale Frage „wirksam gegen welche neue Erkrankung?" hat keine Antwort.

**2. Keine ursprüngliche Indikation aufgezeichnet.** Das Feld `original_indications` ist ebenfalls leer. Dies verhindert die Etablierung des mechanistischen Ausgangspunkts — das „von" in der standardmäßigen Umwidmungserzählung. Ohne zu wissen, für welche Erkrankung das Arzneimittel entwickelt wurde, kann die Verwandtschaft mit einer neuen Indikation nicht bewertet werden.

**3. Wirkungsmechanismus nicht verfügbar.** Das Feld `original_moa` hat keine Daten zurückgegeben. Mechanistische Plausibilität — typischerweise das stärkste Argument dafür oder dagegen, eine Arzneimittel-Umwidmung durchzuführen — kann nicht bewertet werden.

Derzeit sind detaillierte Daten zum Wirkungsmechanismus nicht verfügbar. Basierend auf bekannten Registerdaten wird Ravulizumab unter der DrugBank-ID DB11580 klassifiziert, aber die spezifischen Daten zum pharmakologischen Angriffspunkt und zum Signalweg, die für diese Bewertung erforderlich sind, wurden nicht abgerufen.

---

## Informationen zum taiwanesischen Markt

Ravulizumab ist derzeit in Taiwan **nicht zugelassen und nicht im Handel erhältlich**. Es gibt keine von der TFDA ausgegebenen Arzneimittellizenzen auf Rekordhöhe.

| Artikel | Status |
|---------|--------|
| TFDA-Marktstatus | Nicht im Handel |
| Anzahl der Lizenzen | 0 |
| Genehmigte Darreichungsformen | Keine |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. In diesem Evidenzpaket waren keine Daten zu Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungen verfügbar.

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzung**

**Begründung:**
Das Evidenzpaket für Ravulizumab fehlen alle drei Elemente, die für eine Bewertung der Arzneimittel-Umwidmung erforderlich sind: eine prognostizierte Zielindikation, ein ursprünglicher Indikationsbasispunkt und Daten zum Wirkungsmechanismus. Eine Empfehlung unter diesen Bedingungen abzugeben wäre spekulativ.

**Um fortzufahren, wird Folgendes benötigt:**

- **TxGNN-Vorhersage-Pipeline für DB11580 erneut ausführen** — bestätigen Sie, warum `predicted_indications` leer zurückgegeben wurde (Modelllücke in der Abdeckung, Fehler in der Datenpipeline oder echtes Ergebnis ohne Vorhersage)
- **MOA aus DrugBank-API abrufen** (DG002, hoher Schweregrad) — Abfrage der DrugBank für pharmakologischen Angriffspunkt, Mechanismus und Arzneimittelkategorie von Ravulizumab
- **TFDA-Packungsbeilage-PDF herunterladen und analysieren** (DG001, blockierender Schweregrad) — Extrahieren Sie genehmigte Indikationen, wichtige Warnungen und Kontraindikationen für das taiwanesische Etikett
- **Ursprüngliche Indikation klären** — bestätigen Sie aus der DrugBank oder aus der EMA/FDA-Kennzeichnung, für welche Erkrankung Ravulizumab derzeit zur Behandlung zugelassen ist; dies verankert die Erzählung der Arzneimittel-Umwidmung
- **Evidenzpaket erneut einreichen**, sobald die vier oben genannten Elemente gelöst sind; eine vollständige Bewertung auf L1–L5-Evidenzniveau kann dann generiert werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

