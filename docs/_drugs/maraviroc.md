---
layout: default
title: Maraviroc
parent: Nur Modellvorhersage (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: Von HIV-1-Infektion zu Multipler Endokriner Neoplasie

## Zusammenfassung in einem Satz

> Maraviroc ist ein CCR5-Korezeptor-Antagonist, der ursprünglich für CCR5-tropische HIV-1-Infektion entwickelt wurde.
> Die Top-Vorhersage des TxGNN-Modells deutet auf mögliche Relevanz für **Multiple Endokrine Neoplasie** hin,
> diese wird aber derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — es handelt sich um eine reine Modell-Score-Vorhersage ohne unterstützende Evidenz.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-1-Infektion (CCR5-tropisch), verwendet als Teil einer kombinativen antiretroviralen Therapie — nicht dokumentiert in den `taiwan_regulatory` Daten dieses Evidenz-Pakets (Arzneimittel nicht in Deutschland vermarktet) |
| Vorhergesagte neue Indikation | Multiple Endokrine Neoplasie |
| TxGNN-Vorhersage-Score | 99.82% (Rang 2613) |
| Evidenzlevel | L5 (reine Modellvorhersage, keine unterstützenden Studien) |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Mechanismus-der-Wirkung-Daten in diesem Evidenz-Paket nicht verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad). Basierend auf allgemeinem klinischem Wissen ist Maraviroc ein kleinmolekularer CCR5-Antagonist, der den viralen Eintritt blockiert, indem er verhindert, dass gp120 an den CCR5-Korezeptor bindet; seine Wirksamkeit bei CCR5-tropischer HIV-1-Infektion ist gut etabliert.

Für die Top-Vorhersage ist jedoch die mechanistische Bewertung des Evidenz-Pakets selbst explizit und ungünstig: *"Es gibt keine bekannte Verbindung zwischen CCR5-Antagonismus und der Pathogenese von endokrinen Neoplasien; dies ist ein reiner TxGNN-Algorithmus-Score ohne unterstützende Literatur oder Studien."* Mit anderen Worten: TxGNN identifizierte eine statistische Assoziation in seinem Knowledge-Graph-Embedding-Raum, aber keine biologische Rationale verbindet derzeit CCR5-Blockade mit multipler endokriner Neoplasie.

Es ist erwähnenswert, dass mehrere der niedriger bewerteten Kandidaten unter den 10 Vorhersagen in diesem Paket kohärentere mechanistische Unterstützung haben — bemerkenswert ist **HER2-positives Mammakarzinom** (Rang 10), wo eine präklinische Studie zeigt, dass die CCL5–CCR5-autokrine Achse Trastuzumab-Resistenz über ERK-Aktivierung antreibt, wodurch eine konkrete Rationale für CCR5-Blockade als Resistenz-Umkehr-Strategie gegeben ist. Dieser Kandidat erreichte Entscheidungsstufe S1, im Gegensatz zur Top-Vorhersage, und könnte trotz seines niedrigeren TxGNN-Scores engere Nachverfolgung verdienen.

---

## Klinische Studien-Evidenz

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literatur-Evidenz

Derzeit ist keine verwandte Literatur verfügbar.

---

## Informationen zum deutschen Markt

Maraviroc wird **derzeit in Deutschland nicht vermarktet**, gemäß dieses Evidenz-Pakets (`market_status: Not marketed`, `total_licenses: 0`). Es sind keine Zulassungsunterlagen verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Derzeit sind keine wesentlichen Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungs-Daten für diesen Kandidaten verfügbar; das Einholen der offiziellen Kennzeichnung ist als **sperrende** Datenlücke (DG001) gekennzeichnet, die vor einer S1-Sicherheits-Vorabbeurteilung aufgelöst werden muss.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Top-Vorhersage des TxGNN (multiple Endokrine Neoplasie) hat keine klinische Studien- oder Literaturunterstützung und das Evidenz-Paket erklärt ausdrücklich, dass es keine bekannte mechanistische Verbindung gibt — dies ist ein reines Modell-Artefakt (L5) und erfüllt nicht die Schwelle für weitere Bewertung.

**Um fortfahren zu können, ist folgendes erforderlich:**
- DG001 (Sperrend) auflösen: offizielle TFDA/EMA-Verschreibungsinformationen einholen, um S1-Sicherheits-Vorabbeurteilung abzuschließen
- DG002 (Hoch) auflösen: bestätigte MOA-Daten von DrugBank/Kennzeichnung einholen, um mechanistische Verknüpfungsansprüche zu unterstützen oder zu widerlegen
- Falls Repurposing weiter verfolgt wird, erwägen Sie, den Fokus auf die stärkeren sekundären Signale des Pakets zu richten — besonders **HER2-positives Mammakarzinom** (S1-Stufe, in-vitro-mechanistische Evidenz zu CCL5-CCR5/ERK-vermittelter Trastuzumab-Resistenz) und in niedrigerer Priorität die Hypothesen zu kutanem T-Zell-Lymphom und CMV-Infektion (L4, Research-Question-Stufe) — statt der Top-Vorhersage, die mechanistisch nicht unterstützt ist und multiple endokrine Neoplasie betrifft

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

