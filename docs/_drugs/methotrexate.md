---
layout: default
title: Methotrexate
parent: Nur Modellvorhersage (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexat: Von unspezifizierten ursprünglichen Indikationen zu pulmonalem Blastom

## Zusammenfassung in einem Satz

Methotrexat (DrugBank DB00563) ist ein lang etabliertes Antifolatmittel, aber dieses Evidenzpaket enthält keine dokumentierte ursprüngliche Indikation, keinen Wirkmechanismus oder deutsches Marktinformationen für das Arzneimittel. Das TxGNN-Modell sagt eine mögliche neue Anwendung bei **pulmonalem Blastom** voraus, aber dieses Signal wird derzeit durch **0 klinische Studien** und **0 Veröffentlichungen** gestützt — es ist eine reine rechnergestützte Vorhersage ohne unterstützende klinische oder mechanistische Evidenz.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar — kein genehmigter Indikationstext in den Datensätzen vorhanden (Arzneimittel derzeit nicht in Deutschland vermarktet) |
| Vorhergesagte neue Indikation | Pulmonales Blastom |
| TxGNN-Vorhersage-Score | 99.45% |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage berechtigt?

Detaillierte Dokumentation zum Wirkmechanismus von Methotrexat ist in diesem Evidenzpaket nicht verfügbar (`original_moa: Datenlücke`). Kontextinformationen aus anderen Kandidatenindikationen in diesem Datensatz deuten darauf hin, dass Methotrexat als **Dihydrofolatreduktase (DHFR)-Inhibitor** wirkt und die Purinsynthese sowie die Thymidylatsynthese blockiert — ein Mechanismus, der in hämatologischen und ZNS-Malignomen weit verbreitet ist (z. B. ZNS-Lymphom, Non-Hodgkin-Lymphom, Rhabdomyosarkom), wie an anderer Stelle in diesem Datensatz dokumentiert.

Für die hier bewertete spezifische Kandidatenindikation **pulmonales Blastom** wurde keine mechanistische Rationale, keine klinische Studie und keine Literaturstütze ermittelt. Die Begründung des Evidenzpakets besagt: *„Es ist nur eine TxGNN-Modellvorhersage-Score vorhanden; es gibt keine klinische Studie oder Literaturstütze für eine mechanistische Verbindung oder klinische Anwendung von Methotrexat bei diesem seltenen pulmonalen Blastom."* Dies bedeutet, dass die Vorhersage derzeit vollständig auf dem Graph-Neural-Network-Signal (Evidenzlevel L5) beruht, ohne krankheitsspezifische wissenschaftliche oder klinische Grundlage.

---

## Klinische Studien-Evidenz

Derzeit keine zugehörigen klinischen Studien registriert

---

## Literatur-Evidenz

Derzeit keine zugehörige Literatur verfügbar

---

## Marktinformationen Deutschland

Methotrexat besitzt derzeit **keine Marktgenehmigung in Deutschland** in diesem Datensatz (0 Lizenzen in den Datensätzen vorhanden; Marktstatus: Nicht vermarktet).

---

## Zytotoxizität

Methotrexat wird als antineoplastisches/zytotoxisches Mittel (Antimetabolit-Klasse) klassifiziert, basierend auf seiner etablierten Verwendung in mehreren Chemotherapie-Regimen, auf die an anderer Stelle in diesem Evidenzpaket verwiesen wird (z. B. ZNS-Lymphom, Non-Hodgkin-Lymphom, Rhabdomyosarkom, kleinzelliges Lungenkarzinom).

| Element | Inhalt |
|---------|--------|
| Zytotoxizitäts-Klassifizierung | Konventionell zytotoxisch (Antimetabolit / Antifolat, DHFR-Inhibitor) |
| Myelosuppression-Risiko | Siehe Packungsbeilage: Warnungen und Vorsichtsmaßnahmen |
| Emetogenität-Klassifizierung | Siehe Packungsbeilage: Warnungen und Vorsichtsmaßnahmen |
| Überwachungspunkte | Siehe Packungsbeilage: Warnungen und Vorsichtsmaßnahmen |
| Handhabungsschutz | Muss Standardrichtlinien für zytotoxische Arzneimittelbehandlung befolgen (Antimetabolit-Chemotherapeutikum) |

---

## Sicherheitsaspekte

Siehe Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Rationale:**
Der TxGNN-Score für pulmonales Blastom ist hoch, aber es gibt keine klinische Studien- oder Literaturstütze spezifisch für diesen seltenen Tumortyp, und Arzneimittel-Ebene-Daten (Wirkmechanismus, TFDA/BfArM-Label-Warnungen, Kontraindikationen, Marktstatus) sind alle nicht verfügbar, was eine Sicherheitsvorabeinschätzung blockiert.

**Um fortzufahren, ist folgendes erforderlich:**
- DG001 (blockierend) beheben: TFDA/BfArM-Label-Warnungen und Kontraindikationen einholen
- DG002 (hoch) beheben: Wirkmechanismus von Methotrexat via DrugBank oder äquivalente Quelle bestätigen
- Zielgerichtete Literatur-/Studiensuche spezifisch für Methotrexat bei pulmonalem Blastom durchführen
- Deutschen Marketing-/Zulassungsstatus bestätigen, da derzeit 0 Autorisierungen in den Datensätzen vorhanden sind

**Anmerkung:** Dieses Evidenzpaket enthält auch andere Kandidatenindikationen für Methotrexat mit wesentlich stärkerer Evidenz — insbesondere **Hodgkin-Lymphom** (Evidenzlevel L2, „Mit Schutzmaßnahmen fortfahren", mehrere historische Phase-2/3-Regime) und **Rhabdomyosarkom** (Evidenzlevel L2, „Forschungsfrage", Phase-2-Studienevidenz). Diese könnten eine vorrangige Bewertung gegenüber dem oben bewerteten pulmonalen Blastom-Signal rechtfertigen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

