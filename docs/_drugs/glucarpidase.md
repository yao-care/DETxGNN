---
layout: default
title: Glucarpidase
parent: Nur Modellvorhersage (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glucarpidase: vorhergesagte neue Indikation Diabetischer Katarakt (Evidenzstufe L5). Ursprüngliche Indikation: Stoffwechsel-Nebenwirkungen von Arzneimitteln und Substanzen"
monitor_inn: "GLUCARPIDASE"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "tetanic cataract", "mature cataract", "craniostenosis cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "nuclear senile cataract", "senile cataract"]
---

# Glucarpidase
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

## Glucarpidase: Von Stoffwechsel-Nebenwirkungen von Arzneimitteln zum diabetischen Katarakt
{: .text-alpha }

## Zusammenfassung in einem Satz

Glucarpidase ist ein rekombinantes Enzym, das laut der in Deutschland (BfArM) hinterlegten Zulassung bei Stoffwechsel-Nebenwirkungen von Arzneimitteln und Substanzen eingesetzt wird. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **diabetischem Katarakt** voraus. Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht ausschließlich auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Stoffwechsel-Nebenwirkungen von Arzneimitteln und Substanzen |
| Vorhergesagte neue Indikation | Diabetischer Katarakt |
| TxGNN-Vorhersagewert | 99,85 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Glucarpidase ist eine rekombinante bakterielle Carboxypeptidase G2 (ca. 83 kDa, Dimer), die Methotrexat und andere Antifolate in inaktive Metaboliten spaltet. Sie wird intravenös zur Methotrexat-Rescue bei toxischen Plasmaspiegeln und verzögerter Ausscheidung infolge Niereninsuffizienz eingesetzt.

Ein glaubwürdiger mechanistischer Zusammenhang mit dem diabetischen Katarakt ist nicht erkennbar. Glucarpidase wirkt weder auf den Polyolweg, die Aldose-Reduktase, die Glykierung von Linsenproteinen noch auf oxidativen Stress in der Linse. Zudem ist es unwahrscheinlich, dass ein großes, intravenös verabreichtes Protein die Linse erreicht.

Der hohe Score (0,9985) ist sehr wahrscheinlich ein Artefakt des Wissensgraphen, vermutlich bedingt durch die Zuordnung zu einer Kategorie „metabolische Nebenwirkungen“ und die Netzwerknähe zu diabetesbezogenen Knoten. Auffällig ist, dass zehn Katarakt- und Retinopathie-Vorhersagen nahezu identische Scores (0,998–0,9985) aufweisen; dies spricht für ein systematisches Graph-Artefakt und nicht für ein indikationsspezifisches Signal.

Weitere vorhergesagte Indikationen (alle ohne Evidenz, alle L5, alle Hold):

| Rang | Vorhergesagte Indikation | Score |
|------|------|------|
| 2 | Diabetische Retinopathie | 99,84 % |
| 3 | Tetanischer Katarakt | 99,83 % |
| 4 | Reifer Katarakt (Cataracta matura) | 99,83 % |
| 5 | Kraniostenose-Katarakt | 99,83 % |
| 6 | Unreifer Katarakt | 99,83 % |
| 7 | Katarakt bei Diabetes mellitus Typ 2 | 99,83 % |
| 8 | Kortikaler Katarakt | 99,83 % |
| 9 | Nukleärer seniler Katarakt | 99,83 % |
| 10 | Seniler Katarakt | 99,82 % |

Für alle diese Indikationen wurde kein plausibler mechanistischer Bezug identifiziert.

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
| EMEA/H/C/005467 | Voraxaze (SERB SAS) | – | Stoffwechsel-Nebenwirkungen von Arzneimitteln und Substanzen |

Der Status dieser Zulassung ist „aufgehoben/erloschen“; es gibt keine gültige Zulassung.

---

## Zytotoxizität

Glucarpidase ist kein antineoplastisches Arzneimittel, sondern ein Enzym zur Entgiftung von Methotrexat. Es wird daher keine zytotoxische Einstufung vorgenommen.

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Es wurden 8 Wechselwirkungen mittleren (moderaten) Schweregrades identifiziert (Quelle: DDInter):

- Proguanil
- Trimethoprim
- Levoleucovorin
- Pemetrexed
- Pralatrexat
- Pyrimethamin
- Leucovorin
- Trimetrexat

Zu Warnhinweisen und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation für weitere Sicherheitsinformationen heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf einen hohen Modellscore (L5) ohne klinische Studien, Publikationen oder plausiblen Wirkmechanismus. Hinzu kommen die systemische Gabe eines großen Enzyms (geringe Wahrscheinlichkeit für Linsen-/Augenpenetration) und die aufgehobene Zulassung in Deutschland.

**Für ein Weiterverfolgen wären erforderlich:**
- Belastbare mechanistische Hinweise (z. B. präklinische Daten zu Polyolweg, Glykierung oder Augengewebe-Penetration)
- Vollständige Wirkmechanismus-Daten (MOA)
- Sicherheitsdaten aus der Fachinformation (Warnhinweise, Gegenanzeigen), die für das weitere Sicherheitsscreening zwingend erforderlich sind
- Klärung des Zulassungsstatus und der Verfügbarkeit in Deutschland
- Prüfung der Applikationsweg-Kompatibilität (intravenöses Enzym gegenüber okulärer Zielstruktur)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

