---
layout: default
title: Galcanezumab
parent: Nur Modellvorhersage (L5)
nav_order: 175
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Galcanezumab: Von Migräneprophylaxe zu Heparin-Kofaktor-II-Mangel

## Zusammenfassung in einem Satz

Galcanezumab ist ein gegen CGRP (Calcitonin Gene-Related Peptide) gerichteter monoklonaler Antikörper; gemäß den mechanistischen Notizen in diesem Evidenzpaket wird es für die Migräneprophylaxe eingesetzt (dies wird durch deutsche/taiwanesische Regulierungsdaten nicht bestätigt, da das Produkt dort nicht vermarktet wird). TxGNN sagt eine mögliche Assoziation mit **Heparin-Kofaktor-II-Mangel** voraus, wobei die Vorhersage durch **0 klinische Studien** und **0 Veröffentlichungen** gestützt wird, und die Begründung des Modells selbst besagt, dass es keinen bekannten biologischen Mechanismus gibt, der die beiden Zustände verbindet.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in Regulierungsdaten dokumentiert (mechanistische Notizen beziehen sich auf Migräneprophylaxe, unbestätigt) |
| Vorhergesagte neue Indikation | Heparin-Kofaktor-II-Mangel |
| TxGNN-Vorhersage-Punktzahl | 99.50% |
| Evidenzstufe | L5 |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht in strukturierter Form verfügbar. Basierend auf den mechanistischen Notizen in diesem Evidenzpaket ist Galcanezumab ein gegen CGRP gerichteter monoklonaler Antikörper, der die Schmerzleitung im trigeminovaskulären System blockiert, und seine etablierte Verwendung ist die Migräneprophylaxe.

Die drei von TxGNN vorhergesagten Indikationen in diesem Evidenzpaket – Heparin-Kofaktor-II-Mangel, Antithrombin-Mangel Typ 2 und Faktor-V-Überschuss mit spontaner Thrombose – sind alle seltene, genetisch bedingte Gerinnungs-/Thrombophilie-Störungen (SERPIN- oder Gerinnungsfaktor-Gendefekte). Keine dieser Störungen ist am CGRP-Signalweg beteiligt, und die Begründung des Evidenzpakets besagt explizit, dass es **keinen bekannten gemeinsamen Molekülpfad, keine gemeinsamen Rezeptoren und keine Überlappung in der nachgelagerten Signalisierung** zwischen der CGRP-Antikörper-Pharmakologie und der Regulierung der Gerinnungskaskade gibt.

Mit anderen Worten: Dies ist ein Fall, in dem das TxGNN-Modell hohe Ähnlichkeitswerte (>99%) zugewiesen hat, ohne dass ein identifizierbarer biologischer Mechanismus diese unterstützt. Dieses Muster – hoher Wert, keine reale Evidenz und ein expliziter Mechanismus-Haftungsausschluss – sollte als ein Kandidat behandelt werden, der einer weiteren Überprüfung bedarf, statt als ein vielversprechender Repurposing-Lead.

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit keine verwandte Literatur verfügbar.

---

## Marktinformationen für Deutschland

Galcanezumab wird derzeit in Deutschland nicht vermarktet (0 Genehmigungen in den Unterlagen in diesem Evidenzpaket).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Alle drei von TxGNN vorhergesagten Indikationen (Heparin-Kofaktor-II-Mangel, Antithrombin-Mangel Typ 2, Faktor-V-Überschuss mit spontaner Thrombose) weisen keine unterstützenden klinischen Studien oder Literatur auf, und die mechanistische Begründung des Modells selbst besagt, dass es keinen biologisch plausiblen Zusammenhang zwischen einer CGRP-gezielten Therapie und diesen Gerinnungsstörungen gibt. In Kombination mit der unbestätigten Ursprungsindikation des Arzneimittels und der fehlenden Marktpräsenz in Deutschland gibt es keine ausreichende Grundlage, um diese Kandidaten voranzutreiben.

**Um fortzufahren, ist Folgendes erforderlich:**
- Bestätigte Ursprungsindikation und MOA-Daten (aus DrugBank-API oder Herstellerkennzeichnung, gemäß DG002)
- Warnhinweise/Gegenanzeigen in der Packungsbeilage (TFDA/BfArM-Label-Analyse, gemäß DG001 – derzeit wird die Sicherheitsbewertung blockiert)
- Präklinische oder mechanistische Literatur, die speziell die Modulation des CGRP-Signalwegs mit der Regulierung von Gerinnungsfaktoren verbindet, bevor dieser Kandidat über S0 hinausgehen kann
- Neubewertung, ob diese drei Vorhersagen ein systematisches TxGNN-Scoring-Anomalie (z. B. Seltene-Krankheits-Embedding-Artefakt) darstellen, statt echte Repurposing-Signale zu sein

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

