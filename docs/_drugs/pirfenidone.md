---
layout: default
title: Pirfenidone
parent: Nur Modellvorhersage (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: Von idiopathischer Lungenfibrose zu extrakutanem Mastozytom

## Eine-Satz-Zusammenfassung

Pirfenidone ist ein antifibrotisches Mittel, dessen etablierte klinische Verwendung — gemäß Literaturzitat (PMID 29702057) — die idiopathische Lungenfibrose (IPF) ist; kein offizieller behördlicher Indikationstext ist in diesem Datensatz verfügbar. Die Top-Vorhersage des TxGNN-Modells ist **Extrakutanes Mastozytom**, aber dieser Kandidat wird derzeit durch **null klinische Studien und null Publikationen** gestützt — der Score spiegelt eine reine Knowledge-Graph-Vorhersage ohne externe Validierung wider.

> ⚠️ Hinweis: Alle 10 vorhergesagten Indikationen in dieser Evidenzsammlung sind mit **L5 (nur Modellvorhersage)** bewertet, mit Ausnahme von Rang 9 (Fibroblastisches Neoplasma), das L4 erreichte — angetrieben hauptsächlich durch **negative Sicherheitssignale** (Fallberichte über das Auftreten von Sarkom und Verschlimmerung von Dermatofibrom), nicht durch positive Wirksamkeitsevidenz.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Originalindikation | Idiopathische Lungenfibrose (IPF) — *nur aus Literaturzitat entnommen; offizieller behördlicher Indikationstext nicht verfügbar (Datenlücke)* |
| Vorhergesagte neue Indikation | Extrakutanes Mastozytom |
| TxGNN-Vorhersagescore | 99.71% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | ✗ Nicht auf dem Markt (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückgestellt** |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (`original_moa: [Datenlücke]`). Basierend auf externer Literatur, die in dieser Evidenzsammlung eingebettet ist, ist bekannt, dass Pirfenidone die TGF-β1–vermittelte Signalisierung hemmt (einschließlich nicht-SMAD-Pfade), die Fibroblastproliferation reduziert und die Kollagenablagerung verringert — ein Wirkmechanismus, der für fibrotische Erkrankungen wie IPF und Morbus Dupuytren gut dokumentiert ist.

Für den Top-Kandidaten **Extrakutanes Mastozytom** wird dieser Wirkmechanismus nicht sauberer auf die Krankheitsbiologie abgebildet. Mastozytom wird durch Mastzellproliferation vorangetrieben (häufig KIT-Signalweg-bezogen), nicht durch Fibroblasten-/TGF-β–vermittelte Fibrose. Das Rationale der Evidenzsammlung selbst kennzeichnet dies explizit als „schwache, rein inferenzielle" Verbindung, die wahrscheinlich die Graph-Embedding-Nähe zwischen fibrosebezogenen und Mastzell-bezogenen Knoten widerspiegelt, anstatt einer echten pharmakologischen Beziehung.

Bemerkenswert ist, dass sich die meisten der zehn Vorhersagen (Mastozytom, Fibrosarkom-Subtypen, Dermatofibrosarcoma protuberans) um eine „TGF-β/Anti-Fibroblasten"-Hypothese für Weichteilneoplasien konzentrieren. Die einzige Vorhersage mit tatsächlicher Literaturunterstützung (Rang 9, fibroblastisches Neoplasma) zeigt jedoch ein **Sicherheitsbedenken in der entgegengesetzten Richtung** — Fallberichte von Pirfenidone-assoziiertem pleomorphem undifferenziertem Sarkom und verschlimmertem Dermatofibrom — was die „Anti-Fibrose = Anti-Tumor"-Annahme, die mehreren dieser Vorhersagen zugrunde liegt, untergräbt.

---

## Klinische Studienevidenz

Derzeit keine registrierten klinischen Studien zu dieser Indikation.

---

## Literaturevidenz

Derzeit keine Literaturbelege für die Top-Indikation (Extrakutanes Mastozytom) verfügbar.

*(Hinweis: Literaturbelege existieren nur für Rang 9 — Fibroblastisches Neoplasma — siehe Sicherheitsaspekte unten.)*

---

## Marktinformationen zu Deutschland

Pirfenidone hat derzeit **keine Marktzulassungen** auf Datensatzebene (total_licenses: 0). Es sind keine Produkt-/Darreichungsform-Informationen verfügbar.

---

## Sicherheitsaspekte

Alle primären Sicherheitsfelder (wichtige Warnungen, Kontraindikationen, Arzneimittelwechselwirkungen) sind in diesem Datensatz als Datenlücken gekennzeichnet:

> Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

**Beachtenswertes literaturgestütztes Sicherheitssignal** (aus Evidenz für eine niedriger bewertete Vorhersage, nicht aus formalen Sicherheitsdaten):
- Ein Fallbericht beschreibt **pleomorphes undifferenziertes Sarkom**, das nach Pirfenidone-Anwendung auftrat (PMID 29702057).
- Ein separater Fallbericht beschreibt **Verschlimmerung mehrerer eruptiver Dermatofibromen** bei einem Patienten unter Pirfenidone + Mycophenolat-Mofetil (PMID 32572469).

Dies sind isolierte Fallberichte, nicht kausal etabliert, aber sie erfordern Vorsicht, bevor eine Repurposing-Hypothese im Zusammenhang mit Fibroblasten-/Weichteilneoplasma für dieses Medikament verfolgt wird.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückgestellt**

**Begründung:**
Jede vorhergesagte Indikation in dieser Evidenzsammlung ist entweder durch keine klinische Studie oder Literatur gestützt (L5), oder wird nur durch Literatur gestützt, die ein Sicherheitsbedenken aufzeigt, anstatt Wirksamkeitsevidenz zu liefern (L4, Rang 9). In Kombination mit fehlenden MOA-Daten, fehlender behördlicher/Sicherheitsdokumentation und null Marktzulassungen gibt es derzeit keine Grundlage, um einen Kandidaten über die Modellvorhersage-Stufe hinaus voranzubringen.

**Um fortzufahren, wird folgendes benötigt:**
- TFDA/BfArM-Fachinformation (Warnungen, Kontraindikationen) — derzeit blockierend (DG001)
- Bestätigter Wirkmechanismus aus DrugBank API — derzeit hochschwereige Lücke (DG002)
- Bestätigte Originalindikation und behördlicher Genehmigungstext (derzeit fehlend in `taiwan_regulatory.licenses`)
- Präklinische oder klinische Evidenz speziell für extrakutanes Mastozytom vor weiterer Bewertung
- Klärung des Sicherheitssignals bezüglich Sarkomauftreten und Dermatofibrom-Verschlimmerung vor der Verfolgung von Indikationen aus der Familie fibroblastischer Neoplasien

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

