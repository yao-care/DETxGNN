---
layout: default
title: Relebactam
parent: Nur Modellvorhersage (L5)
nav_order: 389
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Relebactam: vorhergesagte neue Indikation Hyperamylasämie (Evidenzstufe L5). Ursprüngliche Indikation: Gramnegative bakterielle Infektionen"
monitor_inn: "Relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
---

# Relebactam
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Relebactam: Von gramnegativen bakteriellen Infektionen zu Hyperamylasämie
{: .text-alpha }

## Zusammenfassung

Relebactam ist ein Beta-Lactamase-Inhibitor, der ursprünglich zur Behandlung gramnegativer bakterieller Infektionen eingesetzt wird. Das TxGNN-Modell sagt voraus, dass er bei **Hyperamylasämie** wirksam sein könnte. Für diese Richtung liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Gramnegative bakterielle Infektionen |
| Vorhergesagte neue Indikation | Hyperamylasämie |
| TxGNN-Vorhersagewert | 99,22 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus von Relebactam liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Relebactam hemmt Serin-Beta-Lactamasen der Klassen A und C und wird mit Imipenem/Cilastatin kombiniert, um die Carbapenem-Aktivität gegen gramnegative Bakterien wiederherzustellen.

Ein mechanistischer Zusammenhang zwischen dieser Wirkung und der Regulation der Amylase, der Pankreasfunktion oder der Speicheldrüsenphysiologie konnte nicht hergestellt werden. Hyperamylasämie ist eher ein Laborbefund oder ein Signal für unerwünschte Wirkungen als eine behandelbare Indikation für ein antibakterielles Begleitmittel. Der hohe TxGNN-Wert ist eine rein graphbasierte Vorhersage.

Die weiteren Vorhersagen weisen ebenfalls keinen plausiblen Mechanismus auf:

- **Polyklonales Hyperviskositätssyndrom** (Wert 99,22 %): Die Ursache sind erhöhte Immunglobuline oder Proteine; die Behandlung zielt auf die Grunderkrankung oder erfolgt per Plasmapherese. Relebactam hat keine immunmodulierende oder proteinsenkende Wirkung. Der identische Wert wie bei Hyperamylasämie deutet auf ein unspezifisches Artefakt der Graph-Einbettung hin.
- **Kongenitale Analbuminämie** (Wert 99,08 %): Es handelt sich um eine seltene autosomal-rezessive Erkrankung mit Funktionsverlust im ALB-Gen. Relebactam beeinflusst weder Expression noch Synthese von Albumin. Die Vorhersage spiegelt wahrscheinlich Netzwerknähe über gemeinsame Knoten wider, keine therapeutische Begründung.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004808 | Recarbrio | – | Gramnegative bakterielle Infektionen |

Der Status dieser Zulassung ist „erloschen/zurückgezogen"; es gibt keine aktuell gültige Zulassung.

---

## Sicherheitsaspekte

Bitte entnehmen Sie die Sicherheitsinformationen der Packungsbeilage. Für Wechselwirkungen wurden in den zusammengestellten Daten keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für alle drei vorhergesagten Indikationen gibt es weder klinische Studien noch Literatur (Evidenzstufe L5), und ein plausibler pharmakologischer Zusammenhang ließ sich nicht herstellen. Zudem besteht in Deutschland keine gültige Zulassung.

**Für ein Weiterverfolgen sind folgende Schritte nötig:**
- Wirkmechanismusdaten (MOA) aus DrugBank ergänzen
- Packungsbeilage mit Warnhinweisen und Gegenanzeigen beschaffen und auswerten (Voraussetzung für die Sicherheitsprüfung)
- Prüfen, ob die Vorhersage durch ein unspezifisches Modellartefakt erklärt wird, und gegebenenfalls Präklinik- oder Mechanismusbelege suchen
- Klären, ob Hyperamylasämie eher als Nebenwirkungssignal denn als Therapieziel einzuordnen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

