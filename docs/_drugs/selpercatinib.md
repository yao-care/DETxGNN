---
layout: default
title: Selpercatinib
parent: Nur Modellvorhersage (L5)
nav_order: 361
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

# Selpercatinib: Von RET-alterierten Krebserkrankungen zur Pulmonalen Hypertonie

## Eine Zusammenfassung in einem Satz

Selpercatinib ist ein selektiver RET-Kinase-Inhibitor, der ursprünglich für RET-Fusion/Mutation-positive nicht-kleinzellige Lungenkrebserkrankungen (NSCLC) und medulläres Schilddrüsenkarzinom (MTC) verwendet wird. Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam für **Pulmonale Hypertonie** ist, aber dieser Ansatz wird derzeit durch **0 klinische Studien** und **keine Literatur, die sich direkt mit dieser Indikation befasst**, gestützt – die verfügbaren Publikationen behandeln nur die ursprüngliche onkologische Anwendung des Arzneimittels und sein Sicherheitsprofil.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | RET-Fusion/Mutation-positive NSCLC und medulläres Schilddrüsenkarzinom (gemäß Umwidmungsrationale; nicht durch formale Lizenzierungsdaten bestätigt) |
| Vorhergesagte neue Indikation | Pulmonale Hypertonie |
| TxGNN-Vorhersage-Score | 99.18% |
| Evidenzstufe | L5 |
| Status auf deutschem Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Daten zum Wirkmechanismus (DrugBank MOA-Feld) nicht verfügbar – dies ist eine dokumentierte Datenlücke (DG002, hoher Schweregrad). Basierend auf dem verfügbaren Umwidmungsrationale ist Selpercatinib ein hochselektiver RET-Kinase-Inhibitor, der für RET-Fusion/Mutation-positive Tumoren zugelassen ist, und seine Wirksamkeit bei NSCLC und MTC ist gut belegt.

Die Verbindung zwischen RET-Signalisierung und vaskulärem Umbau der Lunge ist nur schwach gestützt: zerstreute Grundlagenliteratur hat RET-Expression in glatten Muskelzellen des vaskulären Systems beobachtet, aber es gibt keinen validierten mechanistischen Weg, der RET-Kinase-Inhibition zu therapeutischem Nutzen bei pulmonaler Hypertonie verbindet. Der hohe TxGNN-Score spiegelt wahrscheinlich am meisten indirekte Graph-Embedding-Nähe zwischen RET–Onkologie–Endothelzellen-Knoten im Wissensgraphen wider, anstatt direkter pathophysiologischer Evidenz.

Angesichts des fehlenden präklinischen, klinischen oder fallgestützten Nachweises speziell für pulmonale Hypertonie sollte diese Vorhersage in diesem Stadium nur als hypothesengenerierend behandelt werden, nicht als klinisch umsetzbares Signal.

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Sicherheitsvergleich in der klinischen Praxis/retrospektiv | Frontiers in Pharmacology | Vergleich der Nebenwirkungsprofile zwischen Pralsetinib und Selpercatinib anhand von FDA FAERS-Daten; nicht mit pulmonaler Hypertonie verbunden |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospektive Analyse (RET+ NSCLC) | Therapeutic Advances in Medical Oncology | Wirksamkeit von Selpercatinib in der klinischen Praxis bei RET-Fusions-positiven NSCLC-Patienten, die über ein Zugriffsprogramm behandelt wurden |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Fallbericht (MEN2B/MTC) | Cureus | Fall von metastasiertem medullärem Schilddrüsenkarzinom bei MEN2B mit RET M918T-Mutation, Diskussion des Langzeitmanagements und der zielgerichteten Therapie |

**Hinweis:** Keine der abgerufenen Literaturquellen befasst sich direkt mit pulmonaler Hypertonie; alle drei Publikationen beziehen sich auf die ursprünglichen onkologischen Indikationen des Arzneimittels oder sein Sicherheitsprofil.

---

## Marktinformationen Deutschland

Keine Marktgenehmigungen gefunden – Selpercatinib ist derzeit **nicht vermarktet** in Deutschland (0 Zulassungen dokumentiert).

---

## Zytotoxizität

Selpercatinib ist ein zielgerichteter RET-Kinase-Inhibitor, der für RET-alterierte Krebserkrankungen (NSCLC, MTC) verwendet wird, und wird daher in diesem Abschnitt bewertet.

| Element | Inhalt |
|------|------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie (RET-Kinase-Inhibitor) |
| Risiko für Myelosuppression | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Klassifizierung der Emetogenität | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Überwachungspunkte | Bitte beachten Sie die Überwachungspunkte in der Fachinformation |
| Handhabungsschutz | Bitte beachten Sie die Schutzmaßnahmen bei der Handhabung in der Fachinformation |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

*(Schlüsselwarnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind derzeit alle nicht verfügbar – TFDA/BfArM-Etikettierungsdaten werden als blockierende Datenlücke gekennzeichnet, DG001.)*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Der TxGNN-Vorhersage-Score ist hoch, aber die Evidenzstufe ist L5 – nur Modellvorhersage, ohne klinische Studien und ohne spezifische Literatur zur pulmonalen Hypertonie. Die mechanistische Verbindung zwischen RET-Inhibition und pulmonaler Gefäßerkrankung ist spekulativ und nicht validiert, und das Arzneimittel ist derzeit nicht in Deutschland vermarktet, daher gibt es keinen praktischen Sicherheits- oder Regulierungskontext, um eine weitere Bewertung zu unterstützen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Fachinformation (Warnhinweise, Kontraindikationen) – derzeit eine blockierende Datenlücke (DG001)
- Bestätigte DrugBank-Wirkmechanismus-Daten (DG002)
- Präklinische oder mechanistische Studien, die speziell RET-Signalisierung bei pulmonalem vaskulärem Umbau untersuchen
- Mindestens ein Fallbericht, eine Beobachtungsstudie oder eine frühe klinische Studie, die sich direkt mit Selpercatinib bei pulmonaler Hypertonie befasst, bevor man über S0 hinausgeht

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

