---
layout: default
title: Regadenoson
parent: Nur Modellvorhersage (L5)
nav_order: 331
evidence_level: L5
indication_count: 4
---

# Regadenoson
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Regadenoson: Pharmakologisches Stressmittel — Repurposing-Bewertung unvollständig

Der Skill „txgnn-pipeline" deckt die Pipeline-Verwaltung ab und ändert nichts an der Aufgabe der Berichterstellung. Es wird mit dem Bewertungsbericht fortgefahren.

---

**Analyse des Evidence Packs:**

| Feld | Wert |
|---|---|
| `predicted_indications` | **Leer** — keine TxGNN-Ausgabe |
| `original_indications` | Leer |
| `original_moa` | [Datenlücke] |
| `taiwan_regulatory.market_status` | Nicht im Handel (0 Zulassungen) |
| `safety` | Alle [Datenlücke] |

---

Da `predicted_indications` leer ist, kann der Standardbericht im Format „From X → Y" nicht erstellt werden. Der nachstehende Bericht spiegelt den tatsächlichen Zustand des Packs mit einer **Zurückstellen**-Entscheidung wider.

---

```markdown
# Regadenoson: Pharmakologisches Stressmittel — Repurposing-Bewertung unvollständig

## Ein-Satz-Zusammenfassung

Regadenoson (Lexiscan®) ist ein selektiver Adenosin-A2A-Rezeptor-Agonist, der in den
Vereinigten Staaten als pharmakologisches Stressmittel für die Myokardperfusionsszintigraphie
(MPI) mittels Radionuklid zugelassen ist.
Dieses Evidence Pack **enthält keine TxGNN-Repurposing-Vorhersagen** für Regadenoson, und
das Arzneimittel ist **derzeit nicht in Taiwan im Handel**.
Die Bewertung kann erst zu einer vollständigen Repurposing-Analyse fortschreiten, wenn die
unten dokumentierten kritischen Datenlücken geschlossen sind.

## Kurzübersicht

| Punkt | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Pharmakologisches Stressmittel für die Myokardperfusionsszintigraphie (USA; in Taiwan nicht zugelassen) |
| Vorhergesagte neue Indikation | Keine Vorhersage verfügbar |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzgrad | L5 — Modellvorhersage fehlt; keine unterstützenden Studien im Pack |
| Marktstatus Taiwan | ✗ Nicht im Handel (0 Zulassungen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

## Sicherheitshinweise

Bitte entnehmen Sie die Sicherheitsinformationen der Packungsbeilage.

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Dieses Evidence Pack enthält keine TxGNN-Repurposing-Vorhersagen für Regadenoson, und
sämtliche arzneimittelbezogenen Sicherheitsdaten (Warnhinweise, Kontraindikationen,
Arzneimittelinteraktionen) fehlen, wodurch eine Repurposing-Bewertung in diesem Stadium
nicht möglich ist.

**Für die Weiterbearbeitung wird Folgendes benötigt:**

- **TxGNN-Vorhersageergebnis** — die TxGNN-Pipeline mit Regadenoson als Eingabe erneut
  ausführen, um mögliche Repurposing-Indikationen und Konfidenzwerte zu erhalten
- **Wirkmechanismus (MOA)** — über die DrugBank-API (DB06213) abrufen; im Pack als
  Schweregrad Hoch gekennzeichnet
- **Sicherheitsdaten aus der taiwanesischen Packungsbeilage** — die TFDA-Packungsbeilage
  (PDF) herunterladen und auswerten, um Warnhinweise und Kontraindikationen zu extrahieren
  (als Blockierend gekennzeichnet)
- **Arzneimittel-Interaktionsprofil** — die DDI-Abfrage ergab `not_found`; eine gezielte
  Literaturrecherche oder eine DrugBank-DDI-Abfrage wird empfohlen
- **Bestätigung der ursprünglichen Indikation** — das Feld `original_indications` ist leer;
  die zugelassene(n) Indikation(en) anhand der maßgeblichen Fachinformation (FDA:
  MPI-Stresstest) bestätigen und das Evidence Pack vor erneuter Einreichung vervollständigen
```

---

**Anmerkung zum Bericht:**

Dieses Evidence Pack (`TW-DB06213-multi v4`) weist zwei zentrale Lücken auf:

1. **`predicted_indications` ist ein leeres Array** — TxGNN hat noch keine Vorhersage für Regadenoson erzeugt, sodass das Standardformat „From X to Y" nicht angewendet werden kann.
2. **Alle Sicherheitsfelder sind als [Datenlücke] markiert** — TFDA-Warnhinweise/Kontraindikationen (DG001, Blockierend) wurden noch nicht eingetragen.

Gemäß der Berichtsregel „Abschnitte nur bei vorhandenen Daten aufführen" wurden folgende Abschnitte weggelassen: klinische Studienevidenz, Literaturevidenz, Marktinformationen Taiwan (0 Zulassungen), Zytotoxizität (kein Onkologikum). Es wird empfohlen, die oben genannten Lücken zu schließen und das Evidence Pack erneut einzureichen, bevor die formale Bewertung durchgeführt wird.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

