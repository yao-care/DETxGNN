---
layout: default
title: Pembrolizumab
parent: Nur Modellvorhersage (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: Von Onkologie-Indikationen zur Gingivalen Fibromatose

## Zusammenfassung in einem Satz

> Pembrolizumab ist ein Anti-PD-1-Immune-Checkpoint-Inhibitor, dessen etablierte Onkologie-Anwendungen (durchgehend in der Literatur des Nachweispakets dokumentiert, z. B. fortgeschrittenes nicht-kleinzelliges Lungenkarzinom, Melanom) gut dokumentiert sind, obwohl dieses Nachweispaket keinen formalen Zulassungstext oder genehmigte Indikation für die aktuelle Jurisdiktion enthält.
> Die Spitzenvorhersage des TxGNN-Modells ist **Gingivale Fibromatose**, wird aber durch **0 klinische Studien** und **0 Publikationen** unterstützt, und die eigene Begründung des Modells identifiziert sie als wahrscheinliche Knowledge-Graph-Rauschverbindung statt einer mechanistisch fundierten Hypothese.

---

## Schnelläbersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | In diesem Nachweispaket nicht dokumentiert (keine lokalen Zulassungsunterlagen; `original_moa` als Datenlücke markiert). Literatur innerhalb des Pakets bezieht sich durchgehend auf etablierte Anwendung bei fortgeschrittenem NSCLC und Melanom über PD-1-Blockade. |
| Vorhergesagte neue Indikation | Gingivale Fibromatose |
| TxGNN-Vorhersage-Score | 99.40% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Ausgesetzt |

---

## Warum ist diese Vorhersage begründet?

Detaillierte Mechanismus-der-Wirkung-Daten werden als Datenlücke in diesem Nachweispaket markiert. Literatureinträge anderorts im Paket beschreiben Pembrolizumab jedoch durchgehend als humanisierten IgG4-Antikörper, der den PD-1-Rezeptor blockiert, PD-1/PD-L1-Ligierung verhindert und erschöpfte T-Zell-vermittelte Anti-Tumor-Immunität wiederherstellt – die Grundlage für seine etablierte Wirksamkeit bei Krebsarten wie NSCLC, Melanom und MSI-H/dMMR-Tumoren.

Gingivale Fibromatose ist dagegen eine gutartige Erkrankung, die durch Fibroblastenproliferation und übermäßige Kollagen-/extrazelluläre-Matrix-Ablagerung im gingivalen Bindegewebe getrieben wird – ein fibrotischer, nicht-immuner, nicht-neoplastischer Prozess. Sie hat keine etablierte Verbindung zu Tumor-Immune-Evasion, PD-L1-Überexpression oder T-Zell-Erschöpfung – die biologischen Achsen, auf die Pembrolizumab wirkt.

Die Begründung des Nachweispakets zur Umwidmung dieses Kandidaten schlussfolgert explizit, dass es „keine bekannte Schnittstelle" zwischen den beiden Mechanismen gibt, und dass trotz des hohen rohen TxGNN-Scores die völlige Abwesenheit von Nachweisen in einer klinischen Studie oder Literatur darauf hindeutet, dass dies ein indirektes oder verrauschtes Artefakt innerhalb des Knowledge-Graph statt eines echten biologischen Signals ist. Diese Bewertung wird dadurch unterstützt, dass keine Publikationen oder Studien – selbst lose verwandte – für diese Kombination abrufbar waren.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literatur-Evidenz

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktstatus Deutschland

Für dieses Arzneimittel wurden im aktuellen Datensatz keine Vermarktungszulassungen gefunden (Marktstatus: Nicht vermarktet, Gesamtzulassungen: 0).

---

## Zytotoxizität

| Punkt | Inhalt |
|------|--------|
| Zytotoxizitäts-Klassifizierung | Immuntherapie (Anti-PD-1-Immune-Checkpoint-Inhibitor, IgG4-Antikörper) – kein konventionelles zytostatisches Chemotherapie-Mittel |
| Myelosuppressionsrisiko | Niedrig – als Checkpoint-Inhibitor statt klassisches zytostatisches Mittel ist direkte Knochenmarksuppression keine charakteristische Toxizität; das dominante Risikoprofil besteht in immunbezogenen unerwünschten Ereignissen (irAEs) statt Myelosuppression |
| Emetogenitäts-Klassifizierung | Minimal – Immune-Checkpoint-Inhibitoren werden als Wirkstoffklasse generell als minimal emetogen klassifiziert |
| Überwachungsposten | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Fachinformation (keine arzneimittelspezifischen Überwachungsdaten in diesem Nachweispaket bereitgestellt) |
| Handhabungsschutz | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Fachinformation (keine arzneimittelspezifischen Handhabungsdaten in diesem Nachweispaket bereitgestellt) |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Ausgesetzt**

**Begründung:**
Der Spitzenkandidat trägt einen hohen rohen TxGNN-Score, aber null unterstützende klinische Studien oder Literatur, und die eigene mechanistische Begründung des Modells identifiziert ihn als wahrscheinliches Knowledge-Graph-Artefakt ohne biologische Plausibilität, das PD-1-Blockade mit einer gutartigen fibrotischen gingivalen Erkrankung verbindet.

**Um voranzukommen, wird folgendes benötigt:**
- Bestätigte Dokumentation des Wirkmechanismus (derzeit eine blockierende/High-Severity-Datenlücke)
- TFDA/BfArM-Kennzeichnungswarnungen und Kontraindikationen (derzeit eine blockierende Datenlücke)
- Unabhängige Literatur-/Pathologie-Überprüfung, um festzustellen, ob eine PD-L1- oder Immune-vermittelte Komponente bei refraktärer gingivaler Fibromatose existiert, bevor eine weitere Bewertung durchgeführt wird
- Hinweis: Andere Kandidaten in diesem Nachweispaket – *Lungenhilus-Karzinom* (L4, S1, Research Question) und *Lungenkeimzelltumor* (L3, S1, Research Question) – tragen stärkere mechanistische und Literaturunterstützung und könnten vor diesem Spitzenkandidaten zur Bewertung in Betracht gezogen werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

