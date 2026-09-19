---
layout: default
title: Glucarpidase
parent: Nur Modellvorhersage (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: Von Methotrexat-Toxizität zu Diabetischem Katarakt

## Zusammenfassung in einem Satz

Glucarpidase (DrugBank DB08898) ist ein rekombinantes bakterielles Enzym (Carboxypeptidase G2), das als Notfallantidot zur Inaktivierung toxischer Methotrexat-Spiegel verwendet wird. Das TxGNN-Modell sagt einen möglichen Effekt auf **Diabetischen Katarakt** und neun weitere Katarakt-/Retinopathie-bedingte Zustände voraus, aber **es gibt derzeit keine klinischen Studien oder Literatur, die diese Vorhersagen unterstützen**, und die bereitgestellte mechanistische Begründung wird explizit als biologisch implausibel bewertet.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Methotrexat-(MTX-)Toxizität — Notfall-Entgiftung (abgeleitet vom Rationale des Evidenzpakets; kein formaler Indikationstext vorhanden) |
| Vorhergesagte neue Indikation | Diabetischer Katarakt |
| TxGNN-Vorhersage-Score | 99.85% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus Deutschland | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (Datenlücke). Basierend auf den in diesem Evidenzpaket enthaltenen Informationen ist die einzige gut etablierte biologische Aktivität von Glucarpidase die Hydrolyse des terminalen Glutamat-Rests von Methotrexat, was das Medikament inaktiviert und klinisch zur Rettung bei MTX-Überdosierung verwendet wird. Dies ist eine hochspezifische Ein-Substrat-enzymatische Funktion ohne bekannte Beteiligung an Linsenmetabolismus, Akkumulation von Advanced-Glykationsendprodukten (AGE), oxidativem Stress, retinaler Mikrogefäßpathologie oder Kalzium-/Nebenschilddrüsen-Signalwegen — den Mechanismen, die typischerweise bei Katarakt und diabetischer Retinopathie impliziert sind.

Die Begründung der Umpositionierung des Evidenzpakets für jede der Top-10-Vorhersagen (alle Katarakt-Subtypen und diabetische Retinopathie) besagt, dass es **keinen bekannten mechanistischen Link** zwischen Glucarpidase und diesen Zuständen gibt, und schreibt die hohen TxGNN-Scores spärlichen indirekten Graph-Verbindungen zu (z. B. gemeinsames Auftreten von „Enzym-Klasse-Medikament"- und „metabolische Augenkrankheit"-Knoten) statt auf echte pharmakologische Plausibilität.

Angesichts der Tatsache, dass die ursprüngliche Indikation (akute MTX-Toxizität, eine Einzel-Dosis-IV-Rettungstherapie) keine logische oder mechanistische Beziehung zu chronischen ophthalmologischen Zuständen wie Katarakt aufweist, sollte dieses Vorhersage-Cluster als Graph-Topologie-Artefakt mit niedriger Konfidenz behandelt werden, nicht als glaubwürdige Umpositionierungshypothese.

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Literatur-Evidenz

Derzeit keine relevante Literatur verfügbar

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Alle 10 vorhergesagten Indikationen (diabetischer Katarakt, diabetische Retinopathie und 8 weitere Katarakt-Subtypen) haben Evidenzstufe L5 mit null unterstützenden klinischen Studien oder Literatur, und die mechanistische Analyse des Evidenzpakets selbst kommt explizit zu dem Ergebnis, dass es keinen biologischen Plausibilitylink zwischen der bekannten enzymatischen Aktivität von Glucarpidase und einer dieser ophthalmologischen Zustände gibt.

**Um fortzufahren, wird Folgendes benötigt:**
- Bestätigte Wirkmechanismus-Daten (MOA) für Glucarpidase (derzeit Datenlücke, DG002)
- TFDA/Hersteller-Packungsbeilage-Warnungen und Kontraindikationen (derzeit Datenlücke, DG001 — Blockierend)
- Unabhängige präklinische oder mechanistische Studien, die einen plausiblen Weg zwischen der Carboxypeptidase-G2-Aktivität und Linsen-/Retina-Pathologie etablieren, bevor eine weitere Bewertung gerechtfertigt ist
- Eine Neubewertung sollte nur ausgelöst werden, wenn neue Literatur- oder Studiendaten auftauchen; derzeit wird keine aktive Investition empfohlen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

