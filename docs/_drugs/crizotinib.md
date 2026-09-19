---
layout: default
title: Crizotinib
parent: Nur Modellvorhersage (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: Vom ALK/ROS1-positiven nicht-kleinzelligen Lungenkrebs zur gingivalen Fibromatose

## Zusammenfassung in einem Satz

Crizotinib ist ein ALK/ROS1/MET-Tyrosinkinase-Inhibitor, der für ALK/ROS1-rearrangierte nicht-kleinzellige Lungenkrebse (NSCLC) etabliert ist.
Die Top-Rang-Vorhersage des TxGNN-Modells für dieses Arzneimittel ist **gingivale Fibromatose**, aber dieser Kandidat hat derzeit **0 klinische Studien** und **0 Veröffentlichungen**, und die eigene Begründung des Modells kennzeichnet ihn als reines Embedding-Score-Signal ohne bekannte biologische Grundlage.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | In dieser Gerichtsbarkeit nicht verfügbar (Arzneimittel hier nicht zugelassen; international ist Crizotinib für ALK/ROS1-positive NSCLC gemäß der in diesem Paket enthaltenen Literaturbelege indiziert) |
| Prognostizierte neue Indikation | Gingivale Fibromatose |
| TxGNN-Vorhersage-Score | 99.81% |
| Evidenzebene | L5 |
| Deutschland-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

## Warum ist diese Vorhersage begründet?

Derzeit ist kein formales Wirkmechanismus-Dokument für dieses Arzneimittel im Evidenzpaket verfügbar. Basierend auf wiederholten Beschreibungen in den Begründungen der prognostizierten Indikationen ist bekannt, dass Crizotinib als ein ATP-kompetitiver Kleinmolekül-Inhibitor der Rezeptortyrosinkinasen ALK, ROS1 und MET wirkt und eine etablierte klinische Wirksamkeit bei ALK/ROS1-rearrangiertem NSCLC aufweist.

Für die Top-Rang-Vorhersage, **gingivale Fibromatose**, wurde keine mechanistische oder biologische Verbindung zum ALK/ROS1/MET-Signalweg identifiziert. Die eigene Begründung des Modells für die Umnutzung besagt ausdrücklich, dass dies „eine reine TxGNN-Embedding-High-Score-Vorhersage ohne biologische Hypothesenstützung ist." Es gibt keine klinischen Studien oder Literatureinträge, die diesen Kandidaten unterstützen.

Es ist erwähnenswert, dass unter den 10 für dieses Arzneimittel generierten Vorhersagen mehrere niedriger bewertete Kandidaten wesentlich stärkere und biologisch kohärentere Signale zeigen – besonders bemerkenswert **Lungenhiluskarziom** (Rang 4, Evidenzebene L3, Entscheidungsstufe S2, „Forschungsfrage"), das den bereits etablierten ALK/ROS1-getriebenen NSCLC-Mechanismus des Arzneimittels widerspiegelt, anstatt eine wirklich neuartige Indikation zu sein. Im Gegensatz dazu scheint der hier berichtete Rang-1-Kandidat (gingivale Fibromatose) Embedding-Rauschen zu sein und rechtfertigt zu diesem Zeitpunkt keine weiteren Maßnahmen.

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

## Literaturevidenz

Derzeit keine verwandte Literatur verfügbar

## Deutschland-Marktinformationen

Dieses Arzneimittel hat derzeit keine Zulassung auf diesem Markt (0 Lizenzen registriert).

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie (ALK/ROS1/MET-Tyrosinkinase-Inhibitor) |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Überwachungselemente | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Handhabungsschutz | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die Top-Rang-Vorhersage (gingivale Fibromatose) hat keine Unterstützung durch klinische Studien oder Literatur, und die eigene Begründung des Modells kennzeichnet sie als ein unbegründetes Embedding-Score-Artefakt. Kombiniert mit dem Fehlen lokaler Marktzulassung und grundlegenden Arzneimittel-Daten (Wirkmechanismus, ursprüngliche Indikation, Sicherheit) gibt es eine unzureichende Grundlage, um diesen spezifischen Kandidaten voranzubringen.

**Zum Fortfahren ist Folgendes erforderlich:**
- Behebung der blockierenden Datenlücke DG001: TFDA/BfArM-Beschriftungswarnhinweise und Kontraindikationen (erforderlich vor einer S1-Sicherheitsvorbewertung)
- Behebung der schwerwiegenden Datenlücke DG002: formales Wirkmechanismus-Dokument von DrugBank
- Falls das Interesse an der Umnutzung anhält, leiten Sie die Bewertung zum besser belegten Kandidaten um, der in diesem Datensatz identifiziert wurde — **Lungenhiluskarziom** (L3, Entscheidungsstufe S2) — anstelle der aktuellen Top-Rang-Vorhersage
- Manuelle Ontologie-/Mapping-Überprüfung, da mehrere andere Vorhersagen in diesem Datensatz (z. B. Ränge 5, 8, 10) Literatursätze zeigen, die nicht mit der vorhergesagten Krankheitsbezeichnung übereinstimmen, was systematisches Mapping-Rauschen suggeriert, das vor zukünftigen Scoring-Durchläufen korrigiert werden sollte

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

