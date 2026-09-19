---
layout: default
title: Linaclotide
parent: Nur Modellvorhersage (L5)
nav_order: 233
evidence_level: L5
indication_count: 3
---

# Linaclotide
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

# Linaclotide: Von fehlend dokumentierter ursprünglicher Indikation zu vorhergesagtem Cauda-Equina-Syndrom

## Zusammenfassung in einem Satz

> Die ursprüngliche zugelassene Indikation von Linaclotide ist im aktuellen Datenpaket nicht dokumentiert, obwohl sein bekannter Wirkmechanismus (ein Guanylatcyclase-C-Agonist, der lokal auf das Darmepithel wirkt) eher auf einen gastrointestinalen sekretorischen als auf einen neurologischen Kontext hindeutet.
> Das TxGNN-Modell sagt einen möglichen Zusammenhang mit dem **Cauda-Equina-Syndrom** mit einer sehr hohen Bewertung (**99.96%**) voraus,
> doch diese Vorhersage wird durch **0 klinische Studien** und **0 Publikationen** gestützt, und die eigene Begründung des Modells kennzeichnet die Assoziation als wahrscheinlich ein Datenartefakt statt als ein echter Behandlungsmechanismus.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht im Datenpaket dokumentiert (Datenlücke — `original_indications` leer, `original_moa` = [Data Gap]) |
| Vorhergesagte neue Indikation | Cauda-Equina-Syndrom |
| TxGNN-Vorhersage-Bewertung | 99.96% (Rang 766) |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktststatus in Deutschland | Nicht vermarktet (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Daten zum Wirkmechanismus sind in diesem Datenpaket formal als Datenlücke gekennzeichnet. Allerdings beschreibt die eigene Repurposing-Begründung des Modells Linaclotide als einen **Guanylatcyclase-C (GC-C)-Agonisten**, der ausschließlich auf Rezeptoren auf der intestinalen Epitheloberfläche wirkt, mit systemischer Absorption unter 0.1% und ohne Fähigkeit, die Blut-Hirn-Schranke zu durchqueren oder auf spinale/Cauda-equina-Nervenstrukturen zu wirken.

Das Cauda-Equina-Syndrom ist ein chirurgischer Notfall, der durch mechanische Kompression der Cauda-equina-Nervenwurzeln verursacht wird und eine dringende Dekompression erfordert – es hat keine etablierte pharmakologische Beziehung zu intestinaler Sekretionsfunktion. Nach der eigenen Begründung des Datenpakets spiegelt die hohe TxGNN-Bewertung höchstwahrscheinlich **Störfaktoren durch Symptomüberlappung** im Wissensgraphen wider: „Verstopfung" als Symptomknoten ist häufig mit der Darm-/Blasendysfunktion assoziiert, die üblicherweise bei Cauda-equina-Syndrom-Patienten beobachtet wird, spiegelt aber keinen echten krankheitsmodifizierenden Wirkmechanismus wider.

Kurz gesagt, der in diesem Datenpaket vorgestellte mechanistische Zusammenhang wird explizit als **nicht behandlungsrelevant** bewertet – er ist eine plausible Erklärung dafür, *warum das Modell diese Paarung hoch bewertet hat*, nicht ein Beweis dafür, dass die Paarung klinisch sinnvoll ist.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktinformationen für Deutschland

Linaclotide wird in Deutschland nicht vermarktet (`market_status: Not marketed`), und es sind keine Zulassungsunterlagen im Datenpaket vorhanden (0 Lizenzen).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

Hinweis: Das Datenpaket kennzeichnet TFDA-Etikettenwarnungen/Kontraindikationen (DG001) als **blockierende** Datenlücke – dies verhindert jede Sicherheits-Vorabprüfung (S1-Stufe) für diesen Kandidaten unabhängig von der vorhergesagten Indikation.

---

## Zusätzlicher Kontext: Muster über alle vorhergesagten Indikationen hinweg

Dieses Datenpaket enthält zwei weitere hochbewertete Vorhersagen für Linaclotide — **veraltete neurogene Blase** (99.89%, Rang 1766) und **Insomnie** (99.51%, Rang 5775) – beide zeigen das gleiche Profil: keine klinischen Studien, keine Literatur, Evidenzstufe L5, und der Begründungstext identifiziert die Bewertung explizit als wahrscheinlich angetrieben durch Symptom-Koexistenz im Wissensgraphen (z. B. neurogene Darm-/Blasenkomorbidität, IBS-C/Insomnie-Komorbidität) statt eines echten pharmakologischen Mechanismus. Dieses konsistente Muster über alle drei bewerteten Kandidaten hinweg bekräftigt, dass keine der aktuellen Vorhersagen für Linaclotide den Maßstab für weitere Evaluierung erfüllt.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Vorhersage hat keine unterstützende klinische Studien- oder Literaturevidenz (L5, nur Modell), und die mechanistische Begründung selbst identifiziert die Assoziation als wahrscheinlich ein Wissensgraph-Artefakt (Symptom-Koexistenz) statt eines plausiblen Behandlungsmechanismus. Eine blockierende Datenlücke bei TFDA-Sicherheitskennzeichnung verhindert auch den Eintritt in jede formelle Sicherheits-Vorabprüfung.

**Zum Fortfahren ist Folgendes erforderlich:**
- Bestätigte ursprüngliche Indikation und MOA-Daten für Linaclotide (derzeit fehlend im Datenpaket)
- TFDA-Etikettenwarnungen/Kontraindikationen (DG001 — blockierend), um Sicherheits-Vorabprüfung S1 zu ermöglichen
- Unabhängige mechanistische oder präklinische Evidenz, die GC-C-Agonismus direkt mit Cauda-equina-Pathophysiologie verknüpft, wenn diese Hypothese weiter verfolgt werden soll
- Angesichts des völligen Mangels an biologischer Begründung wird dieser Kandidat nicht für weitere Entwicklung empfohlen, es sei denn, es liegt neue primäre Evidenz vor

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

