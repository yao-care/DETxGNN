---
layout: default
title: Givosiran
parent: Nur Modellvorhersage (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: Von akuter hepatischer Porphyrie zur primitiven Pfortaderthrombose

## One-Sentence Summary

> Givosiran ist ein GalNAc-konjugiertes siRNA-Therapeutikum; das Evidence Pack enthält keine bestätigte ursprüngliche Indikation oder zugelassene Produktinformation (das Arzneimittel ist in dieser Jurisdiktion nicht vermarktet), obwohl es extern als Behandlung für akute hepatische Porphyrie bekannt ist.
> Die Topvorhersage des TxGNN-Modells ist **primitive Pfortaderthrombose**, aber dieser Kandidat weist derzeit **0 klinische Studien** und **0 unterstützende Publikationen** auf, und die begleitende Begründung erklärt explizit, dass es keine bekannte mechanistische Verbindung gibt.
> Die Evidenz für diesen spezifischen Kandidaten ist daher nur Modellausgabe (L5), und die Empfehlung lautet **Halten**.

---

## Quick Overview

| Merkmal | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar — kein Lizenz-/zugelassener Indikationstext im Evidence Pack (Arzneimittel nicht vermarktet in dieser Jurisdiktion) |
| Vorhergesagte neue Indikation | Primitive Pfortaderthrombose |
| TxGNN-Vorhersage-Score | 99.9986% |
| Evidenzniveau | L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur) |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Why is This Prediction Reasonable?

Derzeit sind detaillierte Wirkungsmechanismus-Daten nicht verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad, DG002). Externes Hintergrundwissen deutet darauf hin, dass Givosiran eine kleine interferierende RNA (siRNA) ist, die von Hepatozyten über GalNAc-Konjugation aufgenommen wird und die Translation von hepatischer ALAS1-mRNA unterdrückt, wodurch die Ansammlung der neurotoxischen Häm-Vorläufer ALA und PBG verringert wird — dieser Wirkmechanismus wird durch den an einen niedriger bewerteten Kandidaten im gleichen Evidence Pack angehängten Begründungstext gestützt (Rang 9, Porphyrie durch ALA-Dehydratase-Mangel), obwohl er für den höchstbewerteten Kandidaten selbst nicht bestätigt wird.

Für die Topvorhersage **primitive Pfortaderthrombose** ist die Begründung des Evidence Pack selbst explizit: *„Keine bekannte mechanistische Verbindung. Givosiran wirkt auf den ALAS1/Häm-Biosynthese-Weg, der keine direkte Verbindung zur Koagulations-/Gefäßpathologie zugrunde der Pfortaderthrombose hat. Der hohe TxGNN-Score spiegelt wahrscheinlich repräsentationale Ähnlichkeit zwischen ‚Lebererkrankungs'-Knoten im Wissensgraph wider, anstatt eines echten biologischen Weges."* Ränge 2–5, 7, 8 und 10 in diesem Batch weisen einen identischen oder nahezu identischen TxGNN-Score (~0.99999) und den gleichen Vorbehalt auf, was auf ein Score-Clustering-Artefakt um Lebererkrankungs-Knoten hindeutet, anstatt auf unabhängig validierte Signale.

Im Gegensatz dazu weist ein Kandidat in diesem Batch — Porphyrie durch ALA-Dehydratase-Mangel (Rang 9) — durchaus eine kohärente mechanistische Begründung auf (gemeinsamer ALAS1/Häm-Weg mit der bekannten klinischen Anwendung des Arzneimittels bei akuter hepatischer Porphyrie) und 8 unterstützende Publikationen auf, einschließlich einer Phase-3-post-hoc-Analyse. Dieser Kandidat erhielt eine niedrigere Bewertung als die Topvorhersage, was weiterhin unterstützt, die hohe Bewertung des Rang-1-Kandidaten mit Vorsicht zu behandeln.

---

## Clinical Trial Evidence

Derzeit keine zugehörigen klinischen Studien registriert.

---

## Literature Evidence

Derzeit keine zugehörige Literatur verfügbar.

---

## Germany Market Information

Für dieses Arzneimittel wurden in der aktuellen Datenbank keine Vermarktungszulassungen gefunden (Marktstatus: nicht vermarktet; Gesamtzulassungen: 0).

---

## Safety Considerations

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen. Hinweis: Eine Datenlücke mit Blocking-Schweregrad (DG001) bedeutet, dass TFDA-/Etikett-Warnungen und Kontraindikationen nicht abgerufen werden konnten, so dass dieses Arzneimittel noch nicht die erste Sicherheitsprüfung (S1) für eine Indikation durchlaufen kann.

---

## Conclusion and Next Steps

**Entscheidung: Halten**

**Begründung:**
Die Topvorhersage (primitive Pfortaderthrombose) weist keine klinischen Studien, keine Literatur und einen explizit angegebenen Mangel an mechanistischer Plausibilität auf — dies ist ein reines Modell-Score-Artefakt, kein verwertbares Umpositionierungssignal. Kombiniert mit der Datenlücke mit Blocking-Schweregrad in den Etikett-/Sicherheitsdaten kann dieser Kandidat nicht über S0 hinausgehen.

**Um weiterzumachen, wird das Folgende benötigt:**
- TFDA-/EMA-Etikettendaten (Warnungen, Kontraindikationen) zum Beheben der Blocking-Datenlücke (DG001)
- Bestätigte ursprüngliche Indikation und DrugBank-Wirkmechanismus-Daten (DG002)
- Unabhängige mechanistische oder präklinische Evidenz, die ALAS1/Häm-Biosynthese-Hemmung mit der Pfortaderthrombose-Pathologie verbindet, falls dieser Kandidat weiterhin verfolgt werden soll

**Separate Anmerkung für das Forschungsteam:** Innerhalb des gleichen Batch weist Rang 9 (*Porphyrie durch ALA-Dehydratase-Mangel*) ein materiell stärkeres Evidenzprofil auf — kohärenter Wirkmechanismus über gemeinsame Wege, 8 Literaturzitate einschließlich einer Phase-3-post-hoc-Analyse (L3, Forschungsfrage-Phase) — und könnte sein eigenes Evaluierungsgleis rechtfertigen, anstatt einfach nur deshalb deprioritiert zu werden, weil sein roher TxGNN-Rang niedriger ist.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

