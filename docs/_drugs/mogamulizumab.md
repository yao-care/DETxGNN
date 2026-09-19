---
layout: default
title: Mogamulizumab
parent: Nur Modellvorhersage (L5)
nav_order: 259
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Mogamulizumab: Von unbekannter ursprünglicher Indikation zu Urothelkarzinom der Prostataurethra

## Zusammenfassung in einem Satz

Die ursprüngliche zugelassene Indikation für mogamulizumab ist nicht in diesem Evidenzpaket erfasst (mogamulizumab ist öffentlich bekannt als anti-CCR4-Monoklonalantikörper, der bei T-Zell-Malignitäten verwendet wird, aber dies stammt nicht aus dem Paket selbst).
Die Top-Vorhersage des TxGNN-Modells ist **Urothelkarzinom der Prostataurethra**, mit einer Punktzahl von **99.44%**,
aber dieser Kandidat – und alle 6 anderen vorhergesagten Indikationen in diesem Paket – hat derzeit **null unterstützende klinische Studien und null veröffentlichte Literatur**.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Im Evidenzpaket nicht verfügbar |
| Vorhergesagte neue Indikation | Urothelkarzinom der Prostataurethra |
| TxGNN-Vorhersage-Punktzahl | 99.44% (Rang 6358) |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfehlung zur Entscheidung | Halten |

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten sind im strukturierten MOA-Feld dieses Pakets nicht verfügbar. Der in der Vorhersage selbst eingebettete Begründungstext beschreibt mogamulizumab jedoch als einen anti-CCR4-Monoklonalantikörper, der CCR4+-T-Zellen – einschließlich tumorinfiltrierende regulatorischer T-Zellen (Tregs) – durch ADCC (antikörperabhängige zelluläre Zytotoxizität) depletiert.

Alle sieben vorhergesagten Indikationen teilen einen gemeinsamen spekulativen Faden: Tumoren mit CCR4+-Treg-Infiltration oder T-Zell-vermittelter Immunevasion könnten theoretisch von der Treg-Depletion profitieren, wodurch die Antitumor-Immunität wiederhergestellt wird. Dies trifft am meisten auf die vier Varianten von Urothelkarzinom/Nierenbecken zu (Ränge 1–4) und HHV-8-assoziierte Tumoren (Rang 5), bei denen Immundysregulation ein anerkanntes Merkmal der Tumor-Mikroumgebung ist. Dies trifft viel weniger auf Ektomesenchymom (Rang 6) und malignes kutanes Granularzelltumor (Rang 7) zu, die keine bekannte Assoziation mit dem CCR4-Signalweg aufweisen.

Es ist wichtig zu beachten, dass die Modellränge (6358–8822) diese sieben Kandidaten im mittleren bis unteren Bereich des gesamten TxGNN-Vorhersage-Pools platzieren, nicht unter den Top-Kandidaten. Ohne klinische Studien- oder Literaturbestätigung sollten diese als rein computergestützte Hypothesen behandelt werden.

## Klinische Studienevidenz

Derzeit keine verwandten klinischen Studien registriert.

## Literaturevidenz

Derzeit keine verwandte Literatur verfügbar.

## Weitere TxGNN-vorhergesagte Indikationen (Ränge 2–7)

| Rang | Erkrankung | Punktzahl | Modellrang | Mechanistische Grundlage |
|------|-----------|-----------|-----------|------------------------|
| 2 | Sarkomatoides Übergangszellkarzinom des Nierenbeckens | 99.42% | 6569 | CCR4+-Treg-Depletion-Hypothese (spekulativ) |
| 3 | Infiltrierendes Urothelkarzinom der Blase, sarkomatoide Variante | 99.40% | 6724 | CCR4+-Treg-Depletion-Hypothese (spekulativ) |
| 4 | Papilläres Übergangszellkarzinom des Nierenbeckens | 99.37% | 6945 | CCR4+-Treg-Depletion-Hypothese (spekulativ) |
| 5 | Mit Humanes Herpesvirus 8 assoziierter Tumor | 99.24% | 8121 | Treg-vermittelte Immunwiederherstellung (spekulativ) |
| 6 | Ektomesenchymom | 99.15% | 8822 | Keine bekannte CCR4-Signalweg-Assoziation |
| 7 | Malignes kutanes Granularzelltumor | 99.15% | 8825 | Keine bekannten CCR4-Expressionsnachweise |

## Marktinformationen für Deutschland

Mogamulizumab ist derzeit in Deutschland nicht vermarktet, und es gibt keine Zulassungsunterlagen (0 Zulassungen).

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizitäts-Klassifizierung | Immuntherapie (anti-CCR4-Monoklonalantikörper, ADCC-vermittelt), keine konventionelle zytotoxische Chemotherapie |
| Knochenmarksuppression-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Überwachungspunkte | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Handhabungsschutz | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |

## Sicherheitsaspekte

Bitte beachten Sie die Sicherheitsinformationen in der Packungsbeilage.

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Alle sieben vorhergesagten Indikationen sind Evidenzstufe L5 (nur Modellvorhersage), ohne unterstützende klinische Studien oder Literatur für irgendeinen Kandidaten identifiziert. Kritische Eingaben, die für eine vorläufige Sicherheitsbewertung erforderlich sind – TFDA-Warnhinweise/Kontraindikationen (blockierend) und bestätigter Wirkmechanismus (hoher Schweregrad) – sind als Datenlücken im Paket selbst gekennzeichnet.

**Um fortfahren zu können, ist Folgendes erforderlich:**
- TFDA/Packungsbeilage-Warnhinweise und Kontraindikationen (blockieren derzeit die Sicherheitsbewertung)
- Bestätigter Wirkmechanismus von DrugBank
- Bestätigte ursprüngliche zugelassene Indikation(en) für mogamulizumab (derzeit nicht in diesem Paket erfasst)
- Gezielte Literatur- und klinische Studiensuche für CCR4/Treg-Biologie bei Urothelkarzinom und HHV-8-assoziierten Tumoren, da durch automatisierte Evidenzerfassung keine gefunden wurden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

