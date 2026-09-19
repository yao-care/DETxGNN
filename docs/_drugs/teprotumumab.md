---
layout: default
title: Teprotumumab
parent: Nur Modellvorhersage (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: Von der endokrinen Orbitopathie zu Monosomie X

## Einzeiliger Summary

teprotumumab ist ein IGF-1R-blockierender monoklonaler Antikörper, der zur **endokrinen Orbitopathie (EOO)** zugelassen ist. TxGNN ordnet seinen Top-Kandidaten für eine neue Indikation, **Monosomie X**, einen hohen Rohscore (99.79%) zu, aber dieses Paket enthält **null klinische Studien oder Fachliteratur**, und die mechanistische Begründung des Arzneimittels selbst kennzeichnet die Verbindung explizit als wahrscheinlich Graphenrauschen statt als echte pharmakologische Hypothese.

---

## Schneller Überblick

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Endokrine Orbitopathie (EOO) — abgeleitet aus mechanistischem Begründungstext; kein formales Indikationsdatenbank-Eintrag in diesem Paket |
| Vorhergesagte neue Indikation | Monosomie X |
| TxGNN-Vorhersage-Score | 99.79% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkungsmechanismus nicht in strukturierter Form verfügbar (`original_moa`: [Data Gap]). Die Begründung zur Umwidmung bestätigt jedoch, dass teprotumumab ein **IGF-1R-Antagonist-Antikörper** ist, zugelassen für endokrine Orbitopathie durch die Blockade des IGF-1R/TSHR-Signalkomplexes auf orbitalen Fibroblasten.

Monosomie X (die zytogenetische Grundlage des Turner-Syndroms) ist eine **strukturelle Chromosomenaberration**, keine Signalweg-Erkrankung — es gibt keinen etablierten kausalen Zusammenhang zwischen IGF-1R-Blockade und Chromosomenverlust oder seinen nachgelagerten Phänotypen. Die wahrscheinlichste Erklärung für den hohen TxGNN-Score ist, dass das Turner-Syndrom eine erhöhte Prävalenz von Autoimmun-Schilddrüsenerkrankung (einschließlich Basedow/EOO) aufweist, und der Wissensgraph wahrscheinlich Monosomie X durch diese Komorbiditätsassoziation in die Nähe von EOO einordnet — **nicht** durch einen echten "teprotumumab behandelt Monosomie X"-Mechanismus. Bemerkenswert ist, dass die IGF-1R-Blockade theoretisch kontraproduktiv für wachstumsbezogene Ziele sein könnte, die für das Management des Turner-Syndroms relevant sind, was die Begründung weiter schwächt.

Kurz gesagt: Dies ist ein **statistisches/Graph-Topologie-Artefakt**, keine pharmakologisch fundierte Hypothese. Das gleiche Muster gilt für die anderen 9 eingestuften Kandidaten in diesem Paket (Ösophagusvarizen, gemischte Gonadendysgenese, Mitochondrienerkrankung, Krampfadern usw.) — keiner hat eine identifizierte mechanistische Verbindung zu IGF-1R-Antagonismus, und alle werden mit L5/Hold bewertet.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Fachliteratur-Evidenz

Derzeit ist keine verwandte Fachliteratur verfügbar.

---

## Informationen zum deutschen Marktstatus

Derzeit sind keine Marktzulassungen für teprotumumab in Deutschland registriert (Marktstatus: Nicht vermarktet, 0 Genehmigungen registriert).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind derzeit nicht in diesem Evidenzpaket verfügbar — gekennzeichnet als **Blocking**-Datenlücke DG001.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Es gibt keine klinische Studien- oder Fachliteratur-Evidenz, die diese Indikation unterstützt, und die mechanistische Begründung des Arzneimittels selbst identifiziert die Assoziation als wahrscheinlich ein Wissensgraph-Artefakt statt eine plausible pharmakologische Hypothese. In Kombination mit einer Blocking-Datenlücke zur TFDA-/behördlichen Sicherheitskennzeichnung erfüllt dieser Kandidat nicht die Anforderungen, um über S0 hinauszugehen.

**Um fortzufahren, ist folgendes erforderlich:**
- Beheben Sie DG001 (TFDA-Kennzeichnung / Warnhinweise & Kontraindikationen), bevor eine Sicherheitsvorkontrolle (S1) durchgeführt werden kann
- Bestätigen Sie den formalen MOA-Eintrag von DrugBank (DG002), um die aktuelle aus der Begründung abgeleitete Zusammenfassung zu ersetzen
- Überprüfen Sie unabhängig, ob die TxGNN-Assoziation ein echtes biologisches Signal widerspiegelt (z. B. Überprüfung von Embedding-Nachbarn/Erklärbarkeit) versus Komorbiditäts-getriebenes Graphclustering
- Falls diese Kandidatenklasse überhaupt verfolgt wird, sollte ein erneutes Scoring/Ranking gegen Krankheiten mit plausiblem IGF-1R-Pfad-Beteiligung Vorrang haben, anstatt des aktuellen chromosomalen/vaskulären Kandidatensatzes, von denen keiner einen mechanistischen Fit aufweist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

