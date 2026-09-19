---
layout: default
title: Ibuprofen
parent: Nur Modellvorhersage (L5)
nav_order: 190
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Ibuprofen: Von analgetischer/entzündungshemmender Anwendung bis Acromesomele Dysplasie, Hunter-Thompson-Typ

## Zusammenfassung in einem Satz

Ibuprofen ist ein weit verbreitetes NSAID (Mechanismusdaten sind in diesem Nachweispaket nicht vorhanden); kein ursprünglicher Indikationstext wurde ebenfalls bereitgestellt. TxGNNs Top-Vorhersage ist **Acromesomele Dysplasie, Hunter-Thompson-Typ**, eine seltene autosomal-rezessive Skelettdysplasie, aber diese wird durch **null klinische Studien** und **null Veröffentlichungen** gestützt, und die Begründung des Modells selbst kennzeichnet den Zusammenhang als wahrscheinlich ein Ko-Auftritts-Artefakt aus dem Wissensgraph, statt einer echten mechanistischen Beziehung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | In diesem Nachweispaket nicht verfügbar (keine `original_indications` oder Lizenzdaten bereitgestellt) |
| Vorhergesagte neue Indikation | Acromesomele Dysplasie, Hunter-Thompson-Typ |
| TxGNN-Vorhersageergebnis | 99.74% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine klinischen/Literaturbelege) |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Daten zum Wirkungsmechanismus für Ibuprofen in diesem Nachweispaket nicht verfügbar (gekennzeichnet als kritische Datenlücke, DG002). Ohne diese kann keine glaubwürdige pharmakologische Brücke zwischen der bekannten COX-Hemmung/entzündungshemmenden Aktivität von Ibuprofen und der vorhergesagten Indikation errichtet werden.

Acromesomele Dysplasie, Hunter-Thompson-Typ wird durch Mutationen des *NPR2*-Gens verursacht, die die CNP-(C-Typ natriuretisches Peptid)-Signalisierung in Wachstumsplatten-Chondrozyten unterbrechen — eine Entwicklungs-/genetische Störung, keine entzündliche Erkrankung. Die Begründung dieser Vorhersage besagt ausdrücklich, dass es keine direkte kausale Beziehung zur COX-Hemmung von Ibuprofen gibt, und führt den hohen TxGNN-Wert auf Ko-Auftritte von „Skelett-/Gelenksymptom"-Knoten im Wissensgraph zurück, statt auf einen echten krankheitsmodifizierenden Effekt.

Dieses Muster wiederholt sich über alle sieben bewerteten Vorhersagen in diesem Nachweispaket (Brachydaktylie-Amelogenesis-Imperfecta-Syndrom, Myosklerose, Brachydaktylie, Brachydaktylie-Syndaktylie-Syndrom, Pseudoachondroplasie, Colobomatöse Mikrophthalmie-Rhizomelie-Dysplasie-Syndrom) — alle sind seltene strukturelle/genetische Skelett- oder Entwicklungsstörungen ohne entzündliche Pathophysiologie, ohne unterstützende Studien und ohne unterstützende Literatur. Die einzige teilweise Ausnahme ist Pseudoachondroplasie, wo NSAIDs plausibel *symptomatische* Schmerzlinderung bei assoziiertem frühen arthrose-ähnlichen Gelenkschmerz bieten könnten, aber dies wäre Symptommanagement, kein krankheitsmodifizierendes Repurposing, und bleibt völlig unstudiert in dieser Population.

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

## Literaturbeweise

Derzeit ist keine verwandte Literatur verfügbar.

## Marktinformation Deutschland

Es sind keine Zulassungsdaten verfügbar — Ibuprofen wird in diesem Datensatz als **nicht vermarktet** verzeichnet, mit insgesamt 0 Lizenzen.

## Sicherheitserwägungen

Weitere Informationen finden Sie in der Packungsbeilage.

*(Wichtige Warnhinweise, Gegenanzeigen und WW-Daten sind alle als Datenlücken in diesem Nachweispaket gekennzeichnet; die TFDA/BfArM-Labelbewertung ist separat als blockierende Datenlücke gekennzeichnet — DG001 — erforderlich, bevor eine S1-Sicherheitsbewertung durchgeführt werden kann.)*

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Dieser Kandidat mangelt es an den drei erforderlichen Säulen zum Voranschreiten: keine MOA-Daten zur Unterstützung mechanistischer Plausibilität, keine klinischen oder Literaturbelege für eine der sieben vorhergesagten Indikationen und keine deutsche Marktpräsenz. Die Begründung der Vorhersage selbst kennzeichnet die Top-bewertete Indikation ausdrücklich als wahrscheinliches Ko-Auftritts-Artefakt aus dem Wissensgraph, statt eines echten Signals.

**Um voranzuschreiten, wird Folgendes benötigt:**
- Ibuprofen-Wirkungsmechanismus-(MOA-)Daten (DG002)
- TFDA/BfArM-Label — Warnhinweise und Gegenanzeigen (DG001, blockierend)
- Unabhängige mechanistische Überprüfung, warum TxGNN hohe Werte für genetisch bedingte Skelettdysplasien ohne entzündliche Komponente vergibt (mögliches Modellkalibrierungsproblem)
- Falls das Pseudoachondroplasie-Signal speziell verfolgt wird: Literatur-/Fallbelege zur NSAID-Anwendung bei Gelenkschmerzen in COMP-assoziierten Skelettdysplasien, da dies die einzige Vorhersage mit einer plausiblen (symptomatischen) Begründung ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

