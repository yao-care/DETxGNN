---
layout: default
title: Trametinib
parent: Nur Modellvorhersage (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Trametinib: vorhergesagte neue Indikation Choroideremie (Evidenzstufe L5). Ursprüngliche Indikation: Melanom"
monitor_inn: "TRAMETINIB"
predicted_indications: ["choroideremia"]
---

# Trametinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Trametinib: Vom Melanom zum Choroideremie

Hinweis: Die Vorhersage mit dem höchsten TxGNN-Score (Rang 1) ist Choroideremie. Für diese Indikation liegen jedoch weder klinische Studien noch Literatur vor. Die Bewertung dieser Indikation wird daher unten ausgewiesen. Die Rangfolgen 2 bis 10 sind überwiegend Melanom-Subtypen und werden am Ende ergänzend eingeordnet.

---

## Zusammenfassung

Trametinib ist ein MEK-Inhibitor, der ursprünglich zur Behandlung des Melanoms zugelassen wurde. Das TxGNN-Modell sagt für **Choroideremie** die höchste Wirksamkeit voraus. Dafür gibt es jedoch **keine klinischen Studien und keine Publikationen**. Die Vorhersage ist wahrscheinlich ein Artefakt des Wissensgraphen.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Melanom |
| Vorhergesagte neue Indikation | Choroideremie |
| TxGNN-Vorhersagewert | 99,31 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/gelöschte Zulassung |
| Anzahl der Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Aus den pharmakologischen Daten ist bekannt, dass Trametinib die Kinasen MEK1 (MAP2K1) und MEK2 (MAP2K2) hemmt und damit den MAPK-Signalweg unterhalb von BRAF/RAS blockiert. Beim BRAF-V600-mutierten Melanom ist dieser Signalweg dauerhaft aktiviert, daher die Wirksamkeit.

Für Choroideremie lässt sich dieser Zusammenhang **nicht** herstellen. Die Erkrankung ist eine X-chromosomal vererbte Netzhautdegeneration durch Funktionsverlust des CHM-Gens (REP1). Sie wird nicht durch eine MAPK-Aktivierung getrieben. Eine plausible MEK-Hemmungs-Begründung ist nicht erkennbar. Die Ähnlichkeit zur ursprünglichen Indikation wurde bislang nicht bewertet.

---

## Klinische Studienevidenz

Derzeit sind keine relevanten klinischen Studien zu Choroideremie registriert.

---

## Literaturevidenz

Derzeit ist keine relevante Literatur zu Choroideremie verfügbar.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002643 | Mekinist (Novartis Europharm Limited) | nicht angegeben | Melanom |

Die einzige erfasste Zulassung hat den Status „erloschen“.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (MEK-Inhibitor) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Bitte Fachinformation beachten |
| Handhabungsschutz | Bitte Fachinformation beachten |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen** (17 Einträge, davon 15 mit Schweregrad „moderat“):
Fostamatinib, Elagolix, Apalutamid, Brigatinib, Dabrafenib, Encorafenib, Isavuconazonium, Lasmiditan, Midostaurin, Sarecyclin, Enzalutamid, Erdafitinib, Gilteritinib, Idelalisib, Tucatinib.

Zusätzlich sind die pharmakologischen Zielstrukturen MEK1 und MEK2 aufgeführt.

Zu Warnhinweisen und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation heranziehen.

---

## Ergänzend: Weitere Vorhersagen (Rang 2 bis 10)

| Rang | Indikation | Score | Evidenzstufe | Empfehlung |
|---|---|---|---|---|
| 2 | Nicht-kutanes Melanom | 99,30 % | L2 | Forschungsfrage |
| 3 | Epitheloidzelliges Melanom | 99,28 % | L4 | Forschungsfrage |
| 4 | Lidmelanom | 99,26 % | L4 | Hold |
| 5 | Skrotummelanom | 99,21 % | L5 | Hold |
| 6 | Noduläres malignes Melanom | 99,14 % | L3 | Proceed with Guardrails |
| 7 | Ballonzell-Melanom | 99,14 % | L5 | Hold |
| 8 | Superfiziell spreitendes Melanom | 99,14 % | L3 | Proceed with Guardrails |
| 9 | CDK4-assoziiertes Melanom | 99,14 % | L5 | Hold |
| 10 | Amelanotisches Hautmelanom | 99,14 % | L4 | Hold |

Die Melanom-Subtypen sind überwiegend Varianten der bereits bekannten Indikation. Am besten belegt ist das nicht-kutane Melanom, mit 10 gelisteten Studien (u. a. NCT02296112, Phase 2, abgeschlossen, n = 9). Die Daten sind jedoch heterogen und nicht subtypspezifisch.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für Choroideremie fehlen sowohl Studien als auch Literatur, und es gibt keinen plausiblen mechanistischen Zusammenhang zur MEK-Hemmung. Zudem ist die deutsche Zulassung erloschen und die Sicherheitsdaten der Fachinformation fehlen.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Beschaffung der Fachinformation (Warnhinweise, Gegenanzeigen) als Voraussetzung für das Sicherheits-Screening
- Detaillierte Wirkmechanismus-Daten (MOA)
- Präklinische Hinweise auf eine Rolle der MAPK-Signalkaskade bei Choroideremie, andernfalls Verwerfen der Vorhersage
- Klärung des Zulassungsstatus in Deutschland/EU
- Gegebenenfalls Priorisierung der Melanom-Subtypen (Rang 2 und 6 bis 8) mit BRAF-Mutationstest als Schutzmaßnahme
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

