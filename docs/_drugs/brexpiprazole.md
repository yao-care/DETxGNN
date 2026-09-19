---
layout: default
title: Brexpiprazole
parent: Nur Modellvorhersage (L5)
nav_order: 64
evidence_level: L5
indication_count: 0
---

# Brexpiprazole
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

# Brexpiprazole: Bewertung unvollständig – Keine Repurposing-Vorhersagen verfügbar

## Zusammenfassung in einem Satz

Brexpiprazole ist ein atypisches Antipsychotikum (Serotonin-Dopamin-Aktivitätsmodulator), das in mehreren Jurisdiktionen für Schizophrenie und die adjuvante Behandlung einer Major Depression zugelassen ist.
Das aktuelle Evidence Pack (v4) enthält **keine TxGNN-Repurposing-Vorhersagen**, und zwei kritische Datenlücken – MOA-Details und Informationen zur Packungsbeilage-Sicherheit – wurden als Blocking/High-Schweregrad gekennzeichnet, was eine vollständige Repurposing-Bewertung verhindert.
Eine Hold-Entscheidung wird empfohlen, bis die Datenlücken behoben sind.

---

## Schnellübersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Schizophrenie; Major Depression (adjuvant) |
| Vorhergesagte neue Indikation | Nicht verfügbar – keine TxGNN-Vorhersagen in diesem Evidence Pack |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | N/A |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum ist diese Vorhersage angemessen?

Es gibt keine vorhergesagte neue Indikation in diesem Evidence Pack, daher kann eine mechanistische Repurposing-Rationale in diesem Stadium nicht generiert werden.

Detaillierte MOA-Daten sind nicht im Evidence Pack verfügbar (DG002, High-Schweregrad). Basierend auf öffentlich verfügbaren Informationen wird Brexpiprazole als Serotonin-Dopamin-Aktivitätsmodulator (SDAM) klassifiziert. Es wirkt als partieller Agonist an Dopamin D2/D3- und Serotonin 5-HT1A-Rezeptoren und als Antagonist an 5-HT2A-, adrenergischen α1B- und α2C-Rezeptoren – ein Rezeptorprofil, das es von Antipsychotika der ersten Generation unterscheidet und seine geringere extrapyramidale Nebenwirkungslast erklärt. Seine Wirksamkeit bei Schizophrenie und MDD wurde in Phase-3-Studien nachgewiesen, und es erhielt 2023 die FDA-Zulassung für Agitiertheit im Zusammenhang mit Alzheimer-Demenz, was auf zunehmende Evidenz für neurodegenerative Indikationen hindeutet.

Um eine aussagekräftige Repurposing-Rationale zu erstellen, müssen zunächst TxGNN-Vorhersagen generiert werden, wonach mechanistische Zusammenhänge zwischen der bestätigten MOA und Kandidaten-Indikationen bewertet werden können.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Warnhinweise und Kontraindikationen aus der Packungsbeilage konnten nicht extrahiert werden – markiert als DG001, Blocking-Schweregrad. DDI-Abfrage ergab keine Ergebnisse.)*

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Das Evidence Pack enthält keine TxGNN-Vorhersagen und zwei ungeklärte Datenlücken mit Blocking/High-Schweregrad; eine Repurposing-Bewertung kann nicht abgeschlossen werden, ohne diese Lücken zunächst zu beheben.

**Zum Fortfahren ist Folgendes erforderlich:**

- **[DG001 – Blocking]** Laden Sie die Packungsbeilage der TFDA (oder EMA/BfArM) herunter und analysieren Sie diese, um Warnhinweise und Kontraindikationen zu extrahieren; dies muss behoben werden, bevor ein Sicherheits-Screening eingeleitet werden kann.
- **[DG002 – High]** Fragen Sie die DrugBank API ab, um die vollständigen MOA-, Pharmakodynamik- und Toxizitätsdaten für DB09128 abzurufen.
- **TxGNN-Inferenz** Führen Sie die TxGNN-Pipeline für Brexpiprazole aus, um vorhergesagte Indikationskandidaten zu generieren; ohne Vorhersagen kann die Repurposing-Bewertung in diesem Stadium nicht voranschreiten.
- **DDI-Daten** Fragen Sie eine Datenbank für Arzneimittel-Wechselwirkungen erneut ab (z. B. DrugBank DDI, CREDIBLEMEDS) mit den korrekten Suchparametern; die aktuelle Abfrage ergab keine Ergebnisse.
- **Deutschland (BfArM) Zulassung** Bestätigen Sie den aktuellen EMA/BfArM-Zulassungsstatus direkt, da das regulatorische Feld keine Lizenzen aufweist.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

