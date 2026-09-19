---
layout: default
title: Brivaracetam
parent: Nur Modellvorhersage (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: Fokale Epilepsie — Keine TxGNN-Umwidmungsprognose verfügbar

## Zusammenfassung in einem Satz

Brivaracetam ist ein Antiepileptikum der dritten Generation (AED), das zur Behandlung von fokalen Anfällen bei Erwachsenen und Kindern zugelassen ist. Das aktuelle Evidenz-Paket enthält **keine von TxGNN generierten Umwidmungsprognosen** für dieses Arzneimittel, und die Marktzulassungsabfrage für Deutschland ergab null Datensätze – was darauf hindeutet, dass die Datenpipeline unvollständig ist und eine vollständige Umwidmungsbewertung in dieser Phase nicht durchgeführt werden kann.

---

## Schnellübersicht

| Element | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Fokale Anfälle / Epilepsie |
| Vorhergesagte neue Indikation | — (keine Prognose generiert) |
| TxGNN-Prognosescore | — |
| Evidenzstufe | L5 — Modellprognosedaten nicht verfügbar |
| Marktstatus Deutschland | Nicht vermarktet (0 Datensätze abgerufen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Prognose sinnvoll?

Für Brivaracetam wurde von TxGNN in diesem Evidenz-Paket keine neue Indikation vorhergesagt, daher kann keine formale Analyse der Mechanismus-zu-Indikation-Verknüpfung durchgeführt werden.

Detaillierte Wirkmechanismus-Daten sind im Evidenz-Paket nicht verfügbar. Basierend auf öffentlich verfügbaren Informationen bindet sich Brivaracetam selektiv an das synaptische Vesikelprotein 2A (SV2A) mit hoher Affinität – ein Mechanismus, der mit Levetiracetam geteilt wird, aber mit ungefähr 15–30× höherer SV2A-Bindungsselektivität. SV2A moduliert den synaptischen Vesikelzyklus und die Neurotransmitterfreisetzung, was die Grundlage für seine antikonvulsive Wirksamkeit ist. Dieses Ziel hat exploratives Interesse in anderen neurologischen Erkrankungen geweckt (z. B. neuropathischer Schmerz, traumatische Hirnverletzung), aber kein Umwidmungssignal wurde durch die aktuelle Pipeline generiert.

Das Fehlen von Prognosen kann fehlende Eingabemerkmale im Wissensgraph oder ein Datenabrufproblem in vorgelagerten Schritten widerspiegeln, anstatt einen Mangel an biologischer Rationale. Eine manuelle Überprüfung der Pipeline wird empfohlen, bevor darauf geschlossen wird, dass keine Umwidmungskandidaten vorhanden sind.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidenz-Paket ist strukturell unvollständig – keine TxGNN-Prognosen, keine Regulierungsdaten für Deutschland und keine Sicherheitsdaten wurden erfolgreich geladen. Eine Umwidmungsbewertung erfordert mindestens einen bewerteten Indikationskandidaten; ein Vorgehen ohne diesen würde spekulativ sein.

**Um weiterzumachen, wird Folgendes benötigt:**

- **Führen Sie die TxGNN-Prognosepipeline erneut aus** für DB05541 (BRIVARACETAM), um rangierte Indikationskandidaten zu generieren
- **Rufen Sie Deutschland-/EMA-Zulassungsdaten ab** – Brivaracetam (Briviact®) erhielt 2016 die EMA-Genehmigung; das Null-Datensatz-Ergebnis deutet auf einen Datenabruffehler hin, nicht auf tatsächliche Abwesenheit
- **Beziehen Sie MOA-Daten von der DrugBank-API** (DB05541), um die Mechanismus-zu-Indikation-Verknüpfung zu ermöglichen
- **Laden Sie die Packungsbeilage von der Regulierungsbehörde herunter und analysieren Sie sie**, um wichtige Warnungen und Gegenanzeigen einzutragen
- **Führen Sie erneut eine Bewertung durch**, sobald eine bewertete vorhergesagte Indikation und ein vollständiges Sicherheitsprofil verfügbar sind

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

