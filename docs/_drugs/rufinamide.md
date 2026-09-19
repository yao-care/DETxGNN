---
layout: default
title: Rufinamide
parent: Nur Modellvorhersage (L5)
nav_order: 356
evidence_level: L5
indication_count: 5
---

# Rufinamide
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

# Rufinamid: Von Lennox-Gastaut-Syndrom zu Fieber-Infektions-assoziiertem Epilepsie-Syndrom

## Zusammenfassung in einem Satz

> Rufinamid ist ein Antikonvulsivum, das historisch mit dem Lennox-Gastaut-Syndrom (LGS) assoziiert ist und in der mechanistischen Begründung dieses Nachweispakets referenziert wird, obwohl formale Felder für ursprüngliche Indikation und Wirkmechanismus derzeit Datenlücken darstellen.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam beim **Fieber-Infektions-assoziierten Epilepsie-Syndrom (FIRES)** sein könnte,
> aber **es gibt derzeit keine klinischen Studien** und **keine Fachliteratur**, die diese Richtung unterstützen — dies ist ein reines Modellvorhersage-Signal.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Lennox-Gastaut-Syndrom (LGS) — abgeleitet aus dem Text der mechanistischen Begründung; formale Felder `original_indications`/`original_moa` sind Datenlücken |
| Vorhergesagte neue Indikation | Fieber-Infektions-assoziiertes Epilepsie-Syndrom (FIRES) |
| TxGNN-Vorhersage-Score | 99.57% |
| Evidenzgrad | L5 (nur Modellvorhersage, keine klinischen Studien oder Fachliteratur) |
| Marktstatus in Taiwan | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind detaillierte Wirkmechanismus-Daten für Rufinamid nicht verfügbar (Datenlücke). Basierend auf Informationen, die in anderen Wirkmechanismus-Feldern dieses Nachweispakets eingebettet sind, wird Rufinamid als breitspektrales Natriumkanal-modulierendes Antikonvulsivum beschrieben, mit einer genehmigten Indikation beim Lennox-Gastaut-Syndrom (LGS).

FIRES ist eine schwere, therapieresistente epileptische Enzephalopathie, die wie LGS eine diffuse kortikale Hyperexzitabilität aufweist und oft mit breitspektralen Antiepileptika behandelt wird, wenn die Standardtherapie versagt. Dies bietet eine plausible mechanistische Begründung für die Erweiterung von Natriumkanal-orientierten Antikonvulsiva wie Rufinamid auf FIRES. Es wurden jedoch keine Repurposing-Begründungstexte, klinische Studien oder Fachliteraturbelege für diese spezifische Top-Indikation (Rang 1) bereitgestellt, daher bleibt dies eine theoretische Extrapolation statt einer durch Evidenz gestützten Hypothese.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Fachliteratur

Derzeit ist keine zugehörige Fachliteratur verfügbar.

---

## Marktinformationen für Taiwan

Rufinamid hat derzeit keine Marktzulassungen in Taiwan (0 Lizenzen dokumentiert); es sind keine Produkt-/Darreichungsformdaten verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: TFDA-Kennzeichnungswarnungen/Kontraindikationen und Arzneimittel-Wechselwirkungs-Daten (DDI) sind als **blockierende** Datenlücke (DG001) in diesem Nachweispaket gekennzeichnet — dies muss behoben werden, bevor eine S1-Sicherheitsvorbewertung durchgeführt werden kann.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage wird nur durch einen TxGNN-Ähnlichkeitsscore (L5) mit null klinischen Studien und null Fachliteraturbelegen gestützt, und das Arzneimittel ist derzeit nicht in Taiwan vermarktet. Eine blockierende Sicherheitsdatenlücke (fehlende TFDA-Kennzeichnungsdaten/Kontraindikationsdaten) verhindert auch eine vorläufige Sicherheitsbewertung.

**Zur Fortführung ist Folgendes erforderlich:**
- Lösen Sie DG001 auf: TFDA-Kennzeichnung (Warnungen, Kontraindikationen, DDI) über PDF-Parsing der Packungsbeilage abrufen
- Lösen Sie DG002 auf: bestätigten Wirkmechanismus über DrugBank-API-Abfrage abrufen
- Bestätigen Sie formale ursprüngliche Indikation(en) für Rufinamid (derzeit leer in den Quelldaten)
- Generieren oder beschaffen Sie klinische Studien-/Fachliteraturbelege speziell für FIRES, bevor Sie über S0 hinaus voranschreiten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

