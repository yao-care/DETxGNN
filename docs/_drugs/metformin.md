---
layout: default
title: Metformin
parent: Nur Modellvorhersage (L5)
nav_order: 251
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Metformin: Von Diabetes mellitus Typ 2 zu fünf Kandidaten seltener Erkrankungen (Nur-Modell-Signal)

## Zusammenfassung in einem Satz

Metformin ist ein weit verbreitetes Biguanid-Antidiabetikum, obwohl dieses spezifische Evidenzpaket seine ursprüngliche Indikation oder seinen Wirkmechanismus nicht erfasst (das Medikament wird in dieser Gerichtsbarkeit derzeit nicht vermarktet). Das TxGNN-Modell identifiziert fünf Kandidaten-Indikationen – angeführt durch **Focal Stiff Limb Syndrome** und **Classic Stiff Person Syndrome** – aber **keine wird durch klinische Studien oder Literatur gestützt**, und die begleitenden mechanistischen Begründungen sind explizit als schwach oder nicht vorhanden gekennzeichnet. Dies ist ein reines Modellsignal (L5) mit Kandidaten, die einen vollständigen Evidenzaufbau vor jeder klinischen Berücksichtigung benötigen.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | In diesem Evidenzpaket nicht erfasst (Medikament wird lokal nicht vermarktet; Feld `original_indications` ist leer) |
| Vorhergesagte neue Indikation | Focal Stiff Limb Syndrome (Spitzenrang; 4 weitere Kandidaten darunter) |
| TxGNN-Vorhersage-Score | 99.45% (Rang 1); Bereich 99.06%–99.45% über alle 5 Kandidaten |
| Evidenzstufe | L5 (nur Modellvorhersage – keine Studien, keine Literatur, für alle 5 Kandidaten) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Halten** |

### Alle vorhergesagten Indikationen

| Rang | Krankheit | TxGNN-Score | Modell-Rang | Evidenzstufe | Empfehlung |
|------|-----------|------------|------------|--------------|------------|
| 1 | Focal Stiff Limb Syndrome | 99.45% | 6338 | L5 | Halten |
| 2 | Classic Stiff Person Syndrome | 99.45% | 6339 | L5 | Halten |
| 3 | Opsismodysplasia | 99.40% | 6707 | L5 | Halten |
| 4 | Thiamine-Responsive Dysfunction Syndrome | 99.40% | 6765 | L5 | Halten |
| 5 | Drug-Induced Localized Lipodystrophy | 99.06% | 9580 | L5 | Halten |

---

## Warum ist diese Vorhersage vernünftig?

Detaillierte Wirkmechanismus-Daten sind in diesem Evidenzpaket nicht verfügbar. Metformin ist allgemein als ein Biguanid bekannt, das AMPK aktiviert und die hepatische Glukoneogenese unterdrückt – eine Wirkung, die üblicherweise mit der Behandlung von Diabetes mellitus Typ 2 verbunden ist – aber dieses Evidenzpaket dokumentiert selbst keine ursprüngliche Indikation, daher sollte dieser Kontext als Hintergrund angesehen werden, nicht als verifizierte Quelldaten.

Bei allen fünf vorhergesagten Indikationen bestätigt die Begründung des Modells nur schwache oder fehlende biologische Verbindungen:

- **Stiff Limb / Stiff Person Syndrome** (Ränge 1–2): Autoimmune, anti-GAD65-vermittelte GABAerge Störungen. Keine bekannte mechanistische Überlappung mit AMPK/Glukosestoffwechsel-Signalwegen – die Begründung besagt explizit, dass es „keine bekannte Schnittmenge" gibt, und führt den Score nur auf graphbasierte Assoziation zurück.
- **Opsismodysplasia** (Rang 3): Verursacht durch *INPPL1 (SHIP2)*-Mutationen, ein Protein in der Insulin-Signalisierungsbahn, das eine entfernte topologische Beziehung zum Zielweg von Metformin hat – aber es gibt keine Tier- oder Humanversuche, die eine Auswirkung auf den Skelettphenotyp stützen.
- **Thiamine-Responsive Dysfunction Syndrome** (Rang 4): Der einzige plausible Zusammenhang ist die symptomatische Glykämie-Kontrolle bei mit TRMA assoziiertem Diabetes, nicht die Korrektur des zugrunde liegenden Thiamin-Transportdefekts.
- **Drug-Induced Localized Lipodystrophy** (Rang 5): Metformins AMPK-vermittelte Auswirkungen auf den Adipozyten-Stoffwechsel bieten einen theoretischen, aber direktional mehrdeutigen Zusammenhang; es gibt keinen Beweis, dass es lipodystrophische Läsionen verhindert oder rückgängig macht.

Zusammenfassend stammen alle fünf Signale aus der Grapheinbettungs-Ähnlichkeit in TxGNN, nicht von einer identifizierbaren, evidenzgestützten biologischen Hypothese.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien für eine der fünf vorhergesagten Indikationen registriert (Focal Stiff Limb Syndrome, Classic Stiff Person Syndrome, Opsismodysplasia, Thiamine-Responsive Dysfunction Syndrome, Drug-Induced Localized Lipodystrophy).

---

## Literaturevidenz

Derzeit ist keine verwandte Literatur für eine der fünf vorhergesagten Indikationen verfügbar.

---

## Marktstatus in Deutschland

Metformin hält derzeit keine Marktzulassungen in dieser Gerichtsbarkeit (`market_status`: nicht vermarktet; `total_licenses`: 0). Es sind keine Produkteinträge zur Überprüfung verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Hinweis: Dieses Evidenzpaket konnte Warnhinweise der Kennzeichnung, Kontraindikationen oder Arzneimittel-Wechselwirkungsdaten nicht abrufen (Quelle: TFDA/BfArM-Kennzeichnung PDF), was als **Blockierend** gekennzeichnet ist und eine vorläufige Sicherheitsüberprüfung (S1) für eine dieser Kandidaten verhindert.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Alle fünf vorhergesagten Indikationen beruhen ausschließlich auf TxGNN-Modellleistung (L5) ohne klinische Studien oder Literaturstütze, und die eigenen mechanistischen Begründungen des Modells beschreiben die biologischen Verbindungen als schwach, indirekt oder vollständig fehlend. In Kombination mit fehlenden MOA- und Sicherheitskennzeichnungsdaten gibt es keine Grundlage, einen Kandidaten über das Modellsignalstadium hinaus zu fördern.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Kennzeichnung abrufen und analysieren (Warnhinweise, Kontraindikationen, Arzneimittel-Wechselwirkungen) – derzeit Blockierend (DG001)
- Metformins Wirkmechanismus über DrugBank-API bestätigen – derzeit hochpriorige Lücke (DG002)
- Gezielte Literatur- und klinische Studiensuche für jede der fünf Kandidaten-Indikationen (Autoimmun-Neurologie, Skeletale Dysplasie, Thiamin-Stoffwechsel-Störungen, Lipodystrophie), um festzustellen, ob einer über L5 hinausgeht
- Unabhängige mechanistische/pharmakologische Überprüfung vor Berücksichtigung einer Kandidatin für S1-Eintrag

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

