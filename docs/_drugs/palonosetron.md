---
layout: default
title: Palonosetron
parent: Mittlere Evidenz (L3-L4)
nav_order: 291
evidence_level: L4
indication_count: 5
---

# Palonosetron
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **5** 
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

# Palonosetron: Von [Datenlücke – Ursprüngliche Indikation nicht vorhanden] zur Migränestörung

## Zusammenfassung in einem Satz

> Palonosetron (DB00377) ist ein selektiver 5-HT3-Rezeptor-Antagonist; seine ursprüngliche zugelassene Indikation ist in diesem Evidenzpaket nicht dokumentiert (Datenlücke).
> Das TxGNN-Modell sagt einen möglichen Zusammenhang mit **Migränestörung** mit einer **Konfidenzpunktzahl von 99,74%** voraus,
> aber dies wird derzeit nur durch **1 Fallbericht** gestützt (keine klinischen Studien), und dieser Bericht beschreibt tatsächlich, dass Palonosetron migräneähnliche Kopfschmerzen **auslöst** — ein Signal, das einer therapeutischen Hypothese entgegengesetzt ist.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar — `original_indications` ist leer und `original_moa` ist in diesem Evidenzpaket als Datenlücke gekennzeichnet |
| Vorhergesagte neue Indikation | Migränestörung |
| TxGNN-Vorhersagepunktzahl | 99,74% |
| Evidenzebene | L4 |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückhalten** |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Daten zum Wirkungsmechanismus nicht verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad, DG002). Basierend auf dem, was aus der Begründung der Umwidmung in diesem Evidenzpaket bekannt ist, ist Palonosetron ein **selektiver 5-HT3-Rezeptor-Antagonist**. Diese Rezeptorklasse ist kein primäres therapeutisches Ziel bei Migräne — die Migränebehandlung ist mechanistisch auf 5-HT1B/1D/1F-Rezeptoren zentriert (z. B. Triptane), nicht auf 5-HT3.

Die einzige identifizierte Literatur für diese Vorhersage ist ein einzelner Fallbericht mit dem Titel *"Palonosetron-induzierte migräneähnliche Kopfschmerzen"* (PMID 21132477). Anstatt eine therapeutische Verwendung von Palonosetron bei Migräne zu unterstützen, beschreibt dieser Bericht migräneähnliche Kopfschmerzen als **Nebenwirkung** des Arzneimittels — eine Richtung, die der Umwidmungshypothese entgegengesetzt ist. Es wurden keine klinischen Studien, präklinischen mechanistischen Studien oder unterstützende Literatur gefunden.

Zusammengenommen stimmen die mechanistische Begründung und die verfügbaren Belege nicht mit der TxGNN-Vorhersage überein. Die hohe TxGNN-Punktzahl scheint eher Ähnlichkeit im Embedding-Raum widerzuspiegeln als eine validierte pharmakologische oder klinische Beziehung.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturbelege

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|------|-----|--------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Fallbericht | Canadian Journal of Anaesthesia | Beschreibt migräneähnliche Kopfschmerzen, die **durch Palonosetron induziert** wurden — ein Bericht über unerwünschte Ereignisse, keine Evidenz für therapeutischen Nutzen bei Migräne |

---

## Informationen zum deutschen Markt

Palonosetron wird derzeit in Deutschland **nicht vermarktet** (BfArM) — in diesem Evidenzpaket existieren keine Zulassungsdatensätze (0 Lizenzen).

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind derzeit nicht in diesem Evidenzpaket verfügbar (Die Erfassung von TFDA/BfArM-Label-Daten ist als blockierende Lücke gekennzeichnet, DG001).

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
- Die Evidenzebene ist L4, basierend auf einem einzelnen Bericht über unerwünschte Ereignisse statt auf unterstützenden klinischen oder mechanistischen Daten; die einzige verfügbare Literatur weist tatsächlich in die entgegengesetzte Richtung (arzneimittelinduzierte Kopfschmerzen, nicht therapeutischer Effekt).
- Der vorgeschlagene Mechanismus (5-HT3-Antagonismus) hat keinen etablierten Zusammenhang mit der Migränepathophysiologie, die primär über 5-HT1B/1D/1F-Rezeptoren vermittelt wird.
- Das Arzneimittel wird derzeit in Deutschland nicht vermarktet, und kritische Sicherheitsdaten (Warnhinweise, Kontraindikationen, Arzneimittelwechselwirkungen) sind nicht verfügbar (blockierende Lücke, DG001).

**Um voranzukommen, ist Folgendes erforderlich:**
- Bestätigte Daten zum Wirkungsmechanismus aus DrugBank/Primärliteratur (DG002)
- TFDA/BfArM-Label-Daten (Warnhinweise, Kontraindikationen) zur Überwindung der S1-Sicherheitshürde (DG001)
- Präklinische oder mechanistische Studien, die speziell die Relevanz des 5-HT3-Signalwegs für Migräne untersuchen, angesichts des widersprüchlichen Signals über unerwünschte Ereignisse
- Neubewertung, falls neue unterstützende klinische Studien- oder Literaturbelege auftauchen

**Anmerkung zu anderen vorhergesagten Indikationen:** Die verbleibenden vier Kandidaten für dieses Arzneimittel (Migräne mit Hirnstammaura, Migräneanfälligkeit, Atrophodermia vermiculata, Ulerythema ophryogenesis) sind alle mit L5 bewertet und ohne unterstützende klinische oder Literaturbelege — der „Migräneanfälligkeits"-Literatursatz besteht aus Genetik-/Epilepsie-Studien, die nicht mit dem Arzneimittelmechanismus zusammenhängen, und die beiden dermatologischen Vorhersagen haben überhaupt keine Belege. Alle werden als **Zurückhalten** empfohlen und gelten als wahrscheinliche Falsch-Positive, die allein aus der Ähnlichkeit beim Embedding-Scoring stammen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

