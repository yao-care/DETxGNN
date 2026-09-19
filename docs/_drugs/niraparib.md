---
layout: default
title: Niraparib
parent: Nur Modellvorhersage (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: Von Ovarialkarzinom zu Epiglottis-Neoplasma

## Zusammenfassung in einem Satz

Niraparib ist ein international zugelassener PARP1/2-Inhibitor zur Erhaltungstherapie von rezidiviertem epithelialem Ovarialkarzinom, Eileitertumor und primärem Peritonealkarzinom (derzeit nicht in Taiwan auf dem Markt erhältlich). Die Top-Vorhersage des TxGNN-Modells für dieses Medikament ist **Epiglottis-Neoplasma**, aber dieses Signal wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — es ist eine reine rechnergestützte Vorhersage ohne identifizierte biologische Plausibilität im Evidenzpaket.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in Taiwan lizenziert; international zugelassen zur Erhaltungstherapie von rezidiviertem epithelialem Ovarialkarzinom, Eileitertumor oder primärem Peritonealkarzinom |
| Vorhergesagte neue Indikation | Epiglottis-Neoplasma |
| TxGNN-Vorhersage-Score | 99.99% (Modellrang #289) |
| Evidenzstufe | L5 |
| Taiwan-Markt-Status | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalt |

## Warum ist diese Vorhersage begründet?

Detaillierte Daten zum Wirkmechanismus sind im strukturierten Arzneimittelbestand nicht verfügbar. Basierend auf der Umnutzungs-Rationale für verwandte Kandidaten-Indikationen in diesem Evidenzpaket ist bekannt, dass Niraparib als PARP1/2-Inhibitor wirkt, der synthetische Letalität in Tumoren mit Homologe-Rekombinations-Defizienz (HRD), einschließlich BRCA1/2-mutierter Karzinome, ausnutzt — dies ist die Grundlage für seine etablierte Verwendung in der Ovarialkarzinom-Erhaltungstherapie.

Speziell für das Epiglottis-Neoplasma besagt die mechanistische Anmerkung des Evidenzpakets, dass dieser Tumortyp überwiegend ein Plattenepithelkarzinom des Kopf- und Halsbereichs mit sehr niedriger HRD/BRCA-Mutationsprävalenz ist, was bedeutet, dass **es keine etablierte molekulare Rationale für PARP-Inhibitor-Aktivität** in dieser Erkrankung gibt. Die Anmerkung charakterisiert dies explizit als „reine Modellvorhersage ohne klinische oder Literaturunterstützung."

Diese Vorhersage sollte nur als rechnergestützte Hypothese mit geringem Konfidenz-Niveau behandelt werden, nicht als mechanistisch oder klinisch substantiierte Umnutzungs-Kandidat.

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert.

## Evidenz aus der Literatur

Derzeit ist keine relevante Literatur verfügbar.

## Marktinformation (Taiwan)

Niraparib ist derzeit nicht auf dem Taiwan-Markt erhältlich — 0 Zulassungen in den Aufzeichnungen.

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizität-Klassifizierung | Zielgerichtete Therapie (PARP-Inhibitor) |
| Myelosuppressions-Risiko | Hoch — Niraparib verursacht bekanntermaßen signifikante Thrombozytopenie, Anämie und Neutropenie; eine regelmäßige hämatologische Überwachung ist bei allen zugelassenen Indikationen erforderlich |
| Emetogenitäts-Klassifizierung | Gering bis moderat |
| Überwachungspunkte | CBC (wöchentlich für den ersten Monat, dann monatlich), Blutdruck, Nieren- und Leberfunktion |
| Handhabungsschutz | Orales niedermolekulares Zieltherapeutikum; Handhabung gemäß institutioneller Protokolle für Gefahrstoffe (PARP-Inhibitoren werden häufig aufgrund ihres gentoxischen Potenzials als Gefahrstoffe klassifiziert) |

## Sicherheitsaspekte

Bitte schlagen Sie die Packungsbeilage für Sicherheitsinformationen nach.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalt**

**Begründung:**
Es gibt keine klinischen Studien- oder Literaturbefunde, die die Verwendung von Niraparib bei Epiglottis-Neoplasma unterstützen, und die zugrundeliegende Tumorbiologie (niedrige HRD/BRCA-Prävalenz im Plattenepithelkarzinom des Kopf- und Halsbereichs) stimmt nicht mit dem PARP-Inhibitions-Wirkmechanismus des Medikaments überein. Dies ist eine L5 (nur Modell-) Vorhersage ohne unterstützende reale Daten.

**Um fortzufahren, ist folgendes erforderlich:**
- Präklinische/Biomarker-Daten, die HRD- oder BRCA-Pathway-Alterationen in Subpopulationen des Epiglottis-/Larynx-Plattenepithelkarzinoms bestätigen
- Mechanistische Studien zur Bewertung der PARP-Inhibitor-Sensitivität in diesem Tumortyp
- Unabhängige Validierung, dass das „epiglottis neoplasm" TxGNN-Etikett eine klinisch kohärente Krankheitsentität widerspiegelt, anstatt eines Ontologie-Mapping-Artefakts

**Zusätzliche Anmerkung:** Dieses Evidenzpaket enthält auch eine wesentlich stärker unterstützte Vorhersage — **„cystic neoplasm"** (TxGNN Rang #292, L2, *Mit Sicherheitsvorkehrungen fortfahren*) — entsprechend hochgradigem serösem Ovarial-/Endometriumkarzinom, unterstützt durch 3 klinische Studien und 9 Publikationen, die direkt relevant für Niraparibs etablierten Wirkmechanismus sind. Dieser Kandidat könnte einen separaten, dedizierten Bewertungsbericht rechtfertigen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

