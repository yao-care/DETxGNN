---
layout: default
title: Leflunomide
parent: Nur Modellvorhersage (L5)
nav_order: 226
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Leflunomide: Von Rheumatoider Arthritis zum Brachydaktylie-Syndaktylie-Syndrom

## Zusammenfassung in einem Satz

> Leflunomide ist ein DHODH-Inhibitor, der konventionell zur Behandlung von Rheumatoider Arthritis und anderen entzündlichen/Autoimmunerkrankungen verwendet wird.
> Das TxGNN-Modell sagt eine mögliche Assoziation mit dem **Brachydaktylie-Syndaktylie-Syndrom**, einer seltenen angeborenen Skelettdeformation, voraus,
> aber diese Vorhersage wird derzeit durch **keine klinischen Studien und keine veröffentlichte Literatur** gestützt — es ist ein reines Modell-Score-Signal.

---

## Schnellübersicht

| Item | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Rheumatoide Arthritis / andere entzündliche Erkrankungen (basierend auf bekannter klinischer Anwendung; nicht aus strukturierten Lizenzdaten ableitbar — keine verfügbar) |
| Vorhergesagte neue Indikation | Brachydaktylie-Syndaktylie-Syndrom |
| TxGNN-Vorhersage-Score | 99.93% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkungsmechanismus-Daten für Leflunomide in diesem Evidence Pack nicht verfügbar (`[Data Gap]`). Basierend auf bekannten Informationen hemmt Leflunomide die Dihydroorotat-Dehydrogenase (DHODH) und blockiert die de novo Pyrimidinsynthese in aktivierten Lymphozyten, was einen immunomodulatorischen Effekt erzeugt, der klinisch bei entzündlichen Erkrankungen wie Rheumatoider Arthritis verwendet wird.

Das Brachydaktylie-Syndaktylie-Syndrom ist jedoch eine angeborene Skelettdeformationsstörung, die typischerweise mit angeborenen Genmutationen verbunden ist (z. B. HOXD Gencluster), die durch embryonale Gliedmaßen-Musterungsfehler getrieben werden, nicht durch entzündliche oder Autoimmunprozesse. Es gibt keinen etablierten biologischen Weg, der DHODH-Hemmung oder Pyrimidinsynthese-Blockade mit der angeborenen Gliedmaßenentwicklung verbindet.

Die an diesem Kandidaten angehängte Umwidmungsrationale vermerkt ausdrücklich, dass **derzeit keine mechanistische Verbindung hergestellt werden kann**, und die fehlenden ursprünglichen MOA-Daten schwächen das Vertrauen in diese Verbindung weiter. Diese Vorhersage sollte nur als algorithmisches Signal behandelt werden (TxGNN-Score 0.9993, Rang 1209), nicht als mechanistisch begründete Hypothese.

Ein zweiter, eng verwandter Kandidat — **kolobomatöse Mikrophtalmie-Rhizomelie-Dysplasie-Syndrom** (Score 0.9993, Rang 1235) — zeigt das gleiche Muster: eine seltene angeborene Augen-/Skelett-Entwicklungsstörung ohne plausible Verbindung zu Leflunomides bekanntem immunomodulatorischem Mechanismus und ohne unterstützende Studien oder Literatur.

---

## Klinische Studienevidenz

Derzeit keine registrierten relevanten klinischen Studien vorhanden

---

## Literaturevadenz

Derzeit keine relevante Literatur verfügbar

---

## Marktsituation in Deutschland

Leflunomide wird derzeit **nicht vermarktet** in Deutschland unter diesem Datensatz (`market_status: Not marketed`) und es sind keine Zulassungseinträge verfügbar (`total_licenses: 0`). Eine Produkt-/Lizenz-Tabelle kann nicht erstellt werden.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: TFDA/BfArM-Warnungen und Kontraindikationen werden als eine **blockierende** Datenlücke gekennzeichnet — DG001 — die den Eintritt in die S1-Sicherheits-Vor-Bewertungsphase verhindert.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Dieser Kandidat wird nur durch ein rohes TxGNN-Vorhersageergebnis gestützt, ohne klinische Studien, ohne Literatur und ohne plausible mechanistische Verbindung zwischen Leflunomides bekanntem immunomodulatorischem Effekt und einem angeborenen Skelettdeformationssyndrom. In Kombination mit einer blockierenden Datenlücke (fehlende Warnungen/Kontraindikationen) kann dieser Kandidat nicht über S0 hinausgehen.

**Um voranzukommen, wird Folgendes benötigt:**
- Leflunomides ursprünglicher Wirkungsmechanismus und bestätigte ursprüngliche Indikation(en) aus DrugBank/autorisierten Labeln
- TFDA/BfArM-Packungsbeilage Warnungen und Kontraindikationen (löst DG001 auf, blockiert derzeit)
- Präklinische oder genetische Evidenz, die einen biologischen Weg zwischen Pyrimidinsynthese/DHODH-Hemmung und Skelett-/Gliedmaßen-Entwicklungsstörungen etabliert
- Alle Fallberichte, Register oder mechanistische Studien für eine der vorhergesagten Indikationen vor Fortschritt über reinen Modell-Vorhersage-Status hinaus

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

