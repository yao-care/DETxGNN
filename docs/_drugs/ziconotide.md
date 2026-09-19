---
layout: default
title: Ziconotide
parent: Mittlere Evidenz (L3-L4)
nav_order: 433
evidence_level: L4
indication_count: 10
---

# Ziconotide
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **10** 
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

# Ziconotide: Vom unzureichend dokumentierten ursprünglichen Indikationsgebiet zur vorhergesagten Migräne

## Zusammenfassung in einem Satz

> Ziconotide (DrugBank DB06283) ist ein Blocker des N-Typ-(Cav2.2)-spannungsgesteuerten Calciumkanals; sein offiziell zugelassenes Indikationsgebiet und der Text zum Wirkmechanismus sind in diesem Evidenzpaket nicht verfügbar, und das Arzneimittel ist derzeit **nicht auf dem deutschen Markt erhältlich**.
> Das TxGNN-Modell prognostiziert, dass es bei **Migränestörungen** wirksam sein könnte, mit einer Vorhersagequote von **99,92%**, aber dies wird derzeit nur durch **0 klinische Studien** und **1 Fallbericht** gestützt.

---

## Schnellübersicht

| Element | Inhalt |
|--------|--------|
| Ursprüngliches Indikationsgebiet | Keine Daten verfügbar – Arzneimittel nicht auf dem deutschen Markt, kein zugelassener Indikationstext dokumentiert (Datenlücke) |
| Vorhergesagtes neues Indikationsgebiet | Migränestörungen |
| TxGNN-Vorhersagequote | 99,92% |
| Evidenzstufe | L4 |
| Marktstatus Deutschland | ✗ Nicht erhältlich |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Wirkmechanismus-Daten in diesem Evidenzpaket nicht verfügbar (gekennzeichnet als Datenlücke DG002, Schweregrad Hoch). Basierend auf der für diesen Kandidaten erfassten Literatur wird Ziconotide als Blocker des N-Typ-(Cav2.2)-spannungsgesteuerten Calciumkanals beschrieben, verabreicht intrathekale für die Behandlung von schweren chronischen Schmerzen – diese Beschreibung stammt aus einem Fallbericht (PMID 26392785) und nicht aus einer offiziellen Marktzulassungsquelle und sollte nur als unterstützendes Kontext-Material behandelt werden, nicht als bestätigte Verschreibungsinformation.

Die vorgeschlagene Begründung für Migräne ist eher mechanistisch als klinisch: N-Typ-Calciumkanäle im Dorsalhorn regulieren die Freisetzung von Substanz P und CGRP, und CGRP-Signalisierung ist zentral für die Pathophysiologie der Migräne über das trigeminovaskuläre System. Theoretisch könnte eine intrathekale Calciumkanal-Blockade diesen Schmerzsignalisierungsweg abschwächen. Dies bleibt jedoch eine einzelne Fallbeobachtung mit Hypothesen-generierendem Charakter – es gibt eine erhebliche praktische Lücke zwischen Ziconotides einzig zugelassener Verabreichungsroute (implantierte intrathekale Pumpe) und der standardmäßigen Migränetherapie-Praxis (orale, injizierbare oder nasale Therapien), was die klinische Anwendbarkeit einschränkt, selbst wenn die mechanistische Hypothese in die richtige Richtung weist.

---

## Klinische Studien-Evidenz

Derzeit keine damit verbundenen klinischen Studien registriert

---

## Literatur-Evidenz

| PMID | Jahr | Publikationstyp | Fachzeitschrift | Wesentliche Ergebnisse |
|-----|------|---------|---------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Fallbericht | Journal of Pain Research | Einzelner Fall der Remission von chronischen Migränekopfschmerzen nach intrathekaler Ziconotide-Gabe, dargestellt als Off-Label-Beobachtung bei einem Patienten mit chronischen schweren Schmerzen |

---

## Marktsituation Deutschland

Keine Genehmigungen dokumentiert. Ziconotide ist derzeit **nicht auf dem deutschen Markt erhältlich** (`market_status: Not marketed`, `total_licenses: 0`), daher kann keine Produkt-/Indikations-Tabelle aus diesem Evidenzpaket generiert werden.

---

## Sicherheitsaspekte

Weitere Informationen finden Sie in der Gebrauchsinformation.

*Hinweis: Das Sicherheitsmodul in diesem Evidenzpaket (wichtige Warnhinweise, Kontraindikationen, Arzneimittel-Wechselwirkungen) ist vollständig leer und ist als **Blockierendes** Datenproblem gekennzeichnet (DG001 – Warnhinweise und Kontraindikationen der deutschen Zulassung). Dies bedeutet, dass eine formale Sicherheitsvorbewertung der Stufe S1 nicht durchgeführt werden kann, bis Angaben der Gebrauchsinformation eingegangen sind.*

---

## Zusätzlicher Hinweis zu niedriger bewerteten Vorhersagen

Neun weitere TxGNN-prognostizierte Indikationen (Migräne mit Hirnstammaurasymptomen, Cauda-equina-Syndrom, Adipositas, TIA, Glaukom-Subtypen, neurogene Blasenentleerungsstörung, Migräneanfälligkeit, Präeklampsie) wurden ebenfalls generiert, alle mit Evidenzstufe L5 (nur Modellvorhersage, keine klinischen Studien oder direkt relevante Literatur) und alle mit der Markierung **Halten** versehen. Eine davon – das **Cauda-equina-Syndrom** – verdient ausdrückliche Vorsicht: Diese Erkrankung ist eine bekannte unerwünschte Ereignisassoziation bei der intrathekalen Ziconotide-Pumpentherapie, kein therapeutisches Ziel. Sie sollte als Sicherheitssignal-Artefakt aus dem Wissensgraph behandelt werden und nicht als Kandidat für Umwidmung.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Top-Vorhersage (Migränestörungen) basiert auf einem einzelnen Fallbericht ohne unterstützende klinische Studien, und das ursprüngliche Indikationsgebiet, der Wirkmechanismus und die Sicherheitsdaten des Arzneimittels fehlen alle in diesem Evidenzpaket – einschließlich einer Datenlücke mit **Blockiertem** Schweregrad, die sogar eine vorläufige Sicherheitsbewertung (S1) verhindert. Die einzige zugelassene Verabreichungsroute (intrathekale Pumpe) ist auch schlecht mit der standardmäßigen Migränetherapie vereinbar.

**Um fortfahren zu können, ist Folgendes erforderlich:**
- Abruf der offiziellen Gebrauchsinformation/Warnhinweise und Kontraindikationen von der zuständigen Zulassungsbehörde (Behebung von DG001) zur Freigabe der S1-Sicherheitsprüfung
- Abruf des bestätigten ursprünglichen Indikationsgebiets und des Wirkmechanismus aus DrugBank oder der offiziellen Gebrauchsinformation (Behebung von DG002)
- Identifizierung zusätzlicher Fallserien oder präklinischer mechanistischer Studien, die eine N-Typ-Calciumkanal-Blockade speziell mit der Migränepathophysiologie verknüpfen
- Bewertung der Machbarkeit einer mit der Verabreichungsroute kompatiblen Formulierung (aktuelle Evidenz ist intrathekale-nur; Migränetherapie-Standards erfordern nicht-invasive Routen), bevor weitere Entwicklungsschritte in Betracht gezogen werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

