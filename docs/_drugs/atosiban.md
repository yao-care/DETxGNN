---
layout: default
title: Atosiban
parent: Nur Modellvorhersage (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: Von drohender Frühgeburt (Tokolyse) zum primären hereditären Glaukom

## Zusammenfassung in einem Satz

Atosiban ist ein kompetitiver Oxytocin-/Vasopressin-V1A-Rezeptorantagonist, der klinisch zur Tokolyse bei drohender Frühgeburt eingesetzt wird. Die Top-Vorhersage des TxGNN-Modells ist **Primäres hereditäres Glaukom**, aber diese Richtung wird derzeit durch **keine** klinischen Studien und **keine** Publikationen gestützt, und das Rationale des Evidenzpakets selbst kennzeichnet es als ein wahrscheinliches Wissensgraph-Assoziations-Artefakt statt einer biologisch fundierten Hypothese.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Drohende Frühgeburt / Tokolyse (gemäß Arzneimittel-Rationale-Text; es ist kein formales Indikations-Datensatz oder MOA-Feld in diesem Datensatz verfügbar) |
| Vorhergesagte neue Indikation | Primäres hereditäres Glaukom |
| TxGNN-Vorhersage-Score | 99.92% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkungsmechanismus in diesem Evidenzpaket nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf dem, was aus dem Arzneimittel-Rationale-Text hergeleitet werden kann, wirkt Atosiban als kompetitiver Oxytocin-/Vasopressin-V1A-Rezeptorantagonist und wird klinisch zur Tokolyse eingesetzt (Verzögerung der Frühgeburt).

Es gibt keine bekannte oder plausible mechanistische Verbindung zwischen Oxytocin-/V1A-Rezeptor-Antagonismus und der Pathophysiologie des primären hereditären Glaukoms, die durch Kammerwasser-Dynamik und Intraokulardruck-Regulation bestimmt wird. Das Rationale des Evidenzpakets selbst besagt explizit, dass diese Verbindung als ein **TxGNN-Wissensgraph-Assoziations-Artefakt ohne biologische Grundlage** beurteilt wird, und es wurden keine klinischen Studien oder Literaturbelege gefunden, die dies unterstützen.

Zum Kontext: Von den 10 TxGNN-vorhergesagten Indikationen, die bereitgestellt wurden, hat nur eine (Rang 6, „Gefäßerkrankung") unterstützende Literatur — und selbst dort befassen sich die zitierten Studien mit Oxytocin-**Agonismus**, der kardioprotektive/vasokonstriktive Effekte erzeugt, was mechanistisch die *entgegengesetzte Richtung* der antagonistischen Wirkung von Atosiban ist. Derzeit hat kein Kandidat in dieser Liste eine kohärente, evidenzgestützte Umwidmungs-Begründung.

---

## Klinische Studienevidenzen

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturbelege

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktstatus in Deutschland

Atosiban wird derzeit nicht in Deutschland vermarktet, und es sind keine Zulassungsdaten in diesem Datensatz verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Anmerkung: TFDA-Packungsbeilage-Warnungen/Gegenanzeigen werden als **blockierende** Datenlücke (DG001) gekennzeichnet — Sicherheits-Vorabprüfung (S1) kann ohne diese Daten nicht fortgesetzt werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Die höchstrangige Vorhersage (Primäres hereditäres Glaukom) hat keine unterstützenden klinischen Studien oder Literatur (L5, Entscheidungsstufe S0), und sein eigenes mechanistisches Rationale kennzeichnet es als ein wahrscheinliches Modell-Artefakt statt einer echten biologischen Hypothese. In Kombination mit dem Fehlen von Kern-Sicherheitsdaten gibt es derzeit keine Grundlage, diesen Kandidaten voranzutreiben.

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA/Packungsbeilage-Warnungen und Gegenanzeigen (DG001, Blockierend — erforderlich vor jeder S1-Sicherheitsprüfung)
- Detaillierte Wirkungsmechanismus-Daten aus DrugBank (DG002)
- Unabhängige biologische oder präklinische Belege, die V1A-Rezeptor-Antagonismus direkt mit Intraokulardruck oder Kammerwasser-Regulation verbinden (derzeit keine vorhanden)
- Falls alternative Kandidaten aus diesem Vorhersage-Set erkundet werden, beachten Sie, dass „Gefäßerkrankung" (Rang 6) die meiste Literatur-Unterstützung (L4) hat, aber die Auflösung des Agonist-vs-Antagonist-Mechanismus-Widerspruchs vor weiterer Investition erforderlich ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

