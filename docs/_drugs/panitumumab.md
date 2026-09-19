---
layout: default
title: Panitumumab
parent: Nur Modellvorhersage (L5)
nav_order: 292
evidence_level: L5
indication_count: 2
---

# Panitumumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# PANITUMUMAB: Vom metastasierten Kolorektalkarzinom zur arzneimittelbedingten Osteoporose

## Zusammenfassung in einem Satz

> Panitumumab ist ein bekannter anti-EGFR-Monoklonalantikörper, von dem angenommen wird, dass er ursprünglich für das RAS-Wildtyp-metastasierte Kolorektalkarzinom verwendet wurde (dies kann aus dem Datenpaket nicht bestätigt werden, da `original_indications` und `original_moa` beide Datenlücken sind).
> Das TxGNN-Modell sagt voraus, dass er möglicherweise für die **arzneimittelinduzierte Osteoporose** wirksam ist,
> aber derzeit **gibt es keine klinischen Studien** und **keine Publikationen**, die diese Richtung unterstützen — die Vorhersage ist nur eine Modellausgabe.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Nicht aus Regulierungsdaten extrahierbar (0 Lizenzen, Arzneimittel nicht in Deutschland vermarktet). Der öffentlich bekannte Kontext deutet auf RAS-Wildtyp-metastasiertes Kolorektalkarzinom hin, aber dies ist nicht überprüft gegenüber diesem Datenpaket |
| Vorhergesagte neue Indikation | Arzneimittelinduzierte Osteoporose |
| TxGNN-Vorhersagepunktzahl | 99.13% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (gekennzeichnet als eine Datenlücke mit hohem Schweregrad, DG002). Basierend auf der Begründung zu dieser Vorhersage wird Panitumumab als anti-EGFR-Monoklonalantikörper verstanden. Die EGFR-Signalisierung hat eine gewisse grundlagenforschungsrelevante Bedeutung für die Differenzierung von Osteoklasten und Osteoblasten, aber dies ist eine indirekte, nicht-spezifische Pfad-Verbindung — es gibt keine Literatur, die zeigt, dass EGFR-Inhibition arzneimittelinduzierte Osteoporose behandelt. Falls überhaupt, konzentriert sich die veröffentlichte Sicherheitsdaten über EGFR-Inhibitor-Arzneimittelklassen eher auf die Überwachung des Knochendichtrisikos während der Langzeitanwendung, nicht auf therapeutischen Nutzen für Knochenerkrankungen.

Eine zweite Kandidaten-Indikation in diesem Datenpaket, schwere nicht-proliferative diabetische Retinopathie, zeigt das gleiche Muster: ihre Pathophysiologie wird primär von VEGF angetrieben, nicht von EGFR, und anti-EGFR-Wirkstoffe sind tatsächlich mit bekannten okulären Toxizitäten (Konjunktivitis, Trichomegalie, Keratitis) verbunden, anstatt mit Schutzeffekten.

Angesichts des Fehlens von klinischen Studien- oder Literaturbelegen für eine der beiden Vorhersagen sollte der hohe TxGNN-Score als eine Knowledge-Graph-Assoziation interpretiert werden, anstatt als ein validierter therapeutischer Mechanismus — höchstwahrscheinlich ein falsch-positives Signal, das aus indirektem Pfad-Quergespräch entsteht (z.B. EGFR–MAPK/PI3K-Überlappung mit VEGF-Signalisierung), anstatt einer echten Umwidmungsmöglichkeit.

---

## Klinische Studien-Evidenz

Derzeit keine verwandten klinischen Studien registriert

---

## Literatur-Evidenz

Derzeit keine verwandte Literatur verfügbar

---

## Marktstatus Deutschland

Panitumumab ist derzeit nicht in Deutschland vermarktet (0 Genehmigungen, keine Lizenzunterlagen in diesem Datenpaket verfügbar).

---

## Zytotoxizität

Panitumumab ist ein anti-EGFR-Monoklonalantikörper, der in der Onkologie verwendet wird, daher ist dieser Abschnitt auf der Grundlage seiner bekannten Arzneimittelklasse enthalten.

| Punkt | Inhalt |
|------|--------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (anti-EGFR-Monoklonalantikörper, nicht-zytotoxischer Mechanismus) |
| Myelosuppressions-Risiko | Niedrig — Mak-Klasse EGFR-Inhibitoren sind typischerweise nicht myelosuppressiv; bitte beziehen Sie sich auf die Fachinformationen Warnungen und Vorsichtsmaßnahmen zur Bestätigung |
| Emetogenitätsklassifikation | Niedrig — konsistent mit Monoklonalantikörper-Wirkstoffen im Allgemeinen |
| Überwachungspunkte | Infusionsbezogene Reaktionen, dermatologische Toxizität, Serumelektrolyte (Magnesium/Kalzium, ein bekannter Klasseneffekt von EGFR-Inhibitoren), Nierenfunktion |
| Schutz bei der Handhabung | Bitte beziehen Sie sich auf die institutionelle Richtlinie für die Handhabung gefährlicher Arzneimittel; viele onkologische Monoklonalantikörper werden trotz nicht-zytotoxischem Mechanismus als gefährliche Arzneimittel klassifiziert (z.B. NIOSH-Liste) |

---

## Sicherheitsüberlegungen

Bitte beziehen Sie sich auf die Fachinformation für Sicherheitsinformationen.

*(Hinweis: `BfArM Fachinformation Warnungen/Kontraindikationen` ist als eine **blockierende** Datenlücke gekennzeichnet — DG001. Dies muss behoben werden, bevor dieser Kandidat zu S1-Sicherheitsbewertung fortfahren kann.)*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Beide vorhergesagten Indikationen sind L5 (nur Modellvorhersage), ohne unterstützende klinische Studien oder Literatur, und die vorgeschlagenen mechanistischen Verbindungen sind indirekt und spekulativ. Darüber hinaus verhindert eine blockierende Datenlücke (fehlende TFDA-Etikettenwarnungen/Kontraindikationen), dass dieser Kandidat überhaupt die Sicherheits-Vorprüfung (S1) betritt.

**Für den Fortschritt ist Folgendes erforderlich:**
- Lösen Sie DG001 (TFDA-Etikettenwarnungen/Kontraindikationen) — Blockierend, erforderlich vor jeder S1-Sicherheitsbewertung
- Lösen Sie DG002 (bestätigter MOA aus DrugBank) — erforderlich für die Bewertung der mechanistischen Plausibilität
- Bestätigen Sie die tatsächlichen ursprünglichen Indikation(en) über eine autoritative Regulierungsquelle (das Feld original_indications ist derzeit leer)
- Überwachen Sie aufkommende klinische Studien oder Literatur zur EGFR-Pfad-Beteiligung an Knochenstoffwechsel oder diabetischer Retinopathie, bevor Sie die Evidenzstufe überdenken

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

