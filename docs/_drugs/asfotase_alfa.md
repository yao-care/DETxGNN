---
layout: default
title: Asfotase Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# ASFOTASE ALFA: Von Hypophosphathasie (HPP) zu mitochondrialem Oxidative-Phosphorylierungs-Defekt (verursacht durch Kern-DNA-Anomalien)

## One-Sentence Summary

> Asfotase alfa ist eine Enzymersatztherapie mit rekombinanter humaner gewebsunspezifischer alkalischer Phosphatase (TNSALP), ursprünglich zur Behandlung der Hypophosphathasie (HPP) entwickelt.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam bei **mitochondrialen Oxidative-Phosphorylierungs-Störungen (verursacht durch Anomalien der Kern-DNA)** sein könnte,
> jedoch gibt es derzeit **keine klinischen Studien und keine Literaturbelege**, die diesen Ansatz unterstützen, und die Mechanismus-Analyse im Evidenzpaket weist selbst darauf hin, dass zwischen den beiden Pathophysiologien keine bekannte Assoziation besteht.

---

## Quick Overview

| Eintrag | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Hypophosphathasie (HPP) ※nach der Mechanismus-Beschreibung im Evidenzpaket zusammengefasst, keine offizielle Indikationsliste (`original_indications` Feld ist leer) |
| Vorhergesagte neue Indikation | Mitochondrialer Oxidative-Phosphorylierungs-Defekt verursacht durch Anomalien der Kern-DNA |
| TxGNN-Prognosescore | 99.95% |
| Evidenzstufe | L5 (nur Modellprognose, keine tatsächliche Forschung) |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Why is This Prediction Reasonable?

Das Feld `drug.original_moa` ist als Datenlücke gekennzeichnet, aber `repurposing_rationale` der höchstbewerteten Kandidaten im Evidenzpaket bietet bereits eine Mechanismusbeschreibung: Asfotase alfa ist ein rekombinantes humanes gewebsunspezifisches alkalisches Phosphatase-Enzym (TNSALP) mit dem Wirkmechanismus der Hydrolyse von Pyrophosphat (PPi), um die Knochenmineralisierung zu fördern, hauptsächlich zur Behandlung der Hypophosphathasie (HPP) — einer Mineralisierungsstörung der extrazellulären Matrix — verwendet.

Mitochondriale Oxidative-Phosphorylierungs-Störungen (verursacht durch Kern-DNA-Anomalien) gehören zu mitochondrialen Atmungskettendefekten, deren Pathophysiologie völlig unabhängig von Knochenmineralisierung und Phosphatstoffwechsel ist. Das Evidenzpaket selbst verweist explizit darauf: „Es gibt keine bekannte Mechanismus-Assoziation mit dem mitochondrialen Oxidative-Phosphorylierungs-Weg (Atmungskettendefekt verursacht durch Kern-DNA-Mutationen); die beiden Pathophysiologien folgen völlig unterschiedlichen pathologischen Achsen; dies ist eine statistische Assoziation im Wissensgraphen, der biologische Plausibilität fehlt."

Mit anderen Worten: Diese Prognose basiert auf statistischen Assoziationen im TxGNN-Wissensgraphen, nicht auf mechanismusgesteuerten Hypothesen. Die Kandidaten auf Platz 2–10 (Steel-Syndrom, exokrine Pankreasinsuffizienz, MPS-I-Serie, Hurler/Scheie-Syndrom, familiärer ApoC-II-Mangel, Ösophagus-Varizen, Zystinose usw.) wurden ebenfalls vom Evidenzpaket selbst als „phänotypische Ebenen-Assoziationen" oder „biologisch implausibel" charakterisiert; nur wenige (wie Zystinose, Hurler/Scheie-Syndrom, lysosomale Speicherkrankheit mit begleitenden Skelettveränderungen) zeigen indirekte Ähnlichkeiten auf der Skelettphänotyp-Ebene, aber die molekularen Mechanismen überlappen sich nicht.

---

## Clinical Trial Evidence

Derzeit sind keine verwandten klinischen Studien registriert

---

## Literature Evidence

Derzeit ist keine verwandte Literatur verfügbar

---

## Germany Market Information

Derzeit sind keine Arzneimittelzulassungen vorhanden (`total_licenses = 0`; Marktstatus ist „Not marketed").

---

## Safety Considerations

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Conclusion and Next Steps

**Entscheidung: Hold**

**Begründung:**
Die Top-10-Vorhersagen für Indikationen sind alle L5-Stufe (nur TxGNN-Modellscore, keine klinischen Studien, keine Literaturunterstützung), und die Mechanismus-Analyse des Top-1-Kandidaten wurde bereits vom Evidenzpaket selbst als biologisch implausibel identifiziert; es handelt sich um statistische Assoziationen im Wissensgraphen, nicht um mechanismusgesteuerte Hypothesen; derzeit gibt es keine ausreichende Evidenzbasis für den Übergang zur nächsten Bewertungsphase.

**Um fortzufahren, wird Folgendes benötigt:**
- Vervollständigung der TFDA-Fachinformation Warnhinweise/Kontraindikationen-Daten (DG001, Blocking, derzeit kann keine S1-Sicherheitsprüfung durchgeführt werden)
- Überprüfung des vollständigen Wirkmechanismus (MOA) von asfotase alfa in der DrugBank (DG002, High)
- Literatur- und Studienrecherche für biologisch plausiblere Kandidaten durchführen (wie Zystinose, MPS-I-Serie und andere skelettphänotyp-assoziierte Erkrankungen), um zu bestätigen, ob über die Wissensgraph-Assoziation hinaus tatsächliche Evidenzen vorhanden sind
- Falls biologische Plausibilität oder empirische Unterstützung nicht vervollständigt werden können, wird empfohlen, Hold beizubehalten und nicht in S1 oder später Phasen überzugehen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

