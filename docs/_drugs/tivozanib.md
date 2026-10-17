---
layout: default
title: Tivozanib
parent: Nur Modellvorhersage (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tivozanib: vorhergesagte neue Indikation Endozervikales Karzinom (Evidenzstufe L5). Ursprüngliche Indikation: Nierenzellkarzinom"
monitor_inn: "TIVOZANIB"
predicted_indications: ["endocervical carcinoma", "uterine ligament adenocarcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma", "cervical mucinous adenocarcinoma, minimal deviation variant"]
---

# Tivozanib
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

# Tivozanib: Vom Nierenzellkarzinom zum endozervikalen Karzinom

## Zusammenfassung in einem Satz

Tivozanib ist ein VEGF-Rezeptor-Tyrosinkinase-Hemmer und wurde ursprünglich zur Behandlung des fortgeschrittenen Nierenzellkarzinoms entwickelt.
Das TxGNN-Modell sagt voraus, dass er bei **endozervikalem Karzinom** wirksam sein könnte.
Dafür liegen in den für diesen Bericht zusammengestellten Daten **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nierenzellkarzinom |
| Vorhergesagte neue Indikation | Endozervikales Karzinom |
| TxGNN-Vorhersagewert | 99,81 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Tivozanib hemmt alle drei VEGF-Rezeptor-Tyrosinkinasen (VEGFR-1/FLT1, VEGFR-2/KDR und VEGFR-3/FLT4) mit gleicher Potenz. Detaillierte Daten zum Wirkmechanismus aus DrugBank liegen derzeit nicht vor; diese Beschreibung stützt sich auf pharmakologische Zielstrukturdaten und allgemeines Wissen über den Wirkstoff.

Beim Nierenzellkarzinom ist die VEGF-getriebene Angiogenese ein zentraler Krankheitsmechanismus, weshalb die Hemmung dieses Signalwegs dort wirksam ist. Auch beim Zervixkarzinom spielt die VEGF-vermittelte Angiogenese eine Rolle. Die Anti-VEGF-Therapie mit Bevacizumab hat bei dieser Erkrankung einen Nutzen gezeigt. Daraus ergibt sich eine plausible, aber nur indirekte Begründung.

Der sehr hohe TxGNN-Wert ist eine rein rechnerische Vorhersage. Er ersetzt keine klinischen Belege. Die weiteren vorhergesagten Indikationen (u. a. seltene Adenokarzinome des Uterusbandes und seltene Zervixkarzinom-Subtypen) liegen alle bei Werten um 99,8 %, ebenfalls ohne Evidenz. Sie dürften vor allem auf Ähnlichkeiten in der Krankheitsontologie beruhen.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004131 | Fotivda (Recordati Netherlands B.V.) | – | Nierenzellkarzinom (Status: erloschen) |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (VEGFR-Tyrosinkinase-Inhibitor) |
| Myelosuppressionsrisiko | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenitätsklassifikation | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Handhabungsschutz | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen** (7 Einträge in den Daten, davon 4 mit Schweregrad-Einstufung):

| Wechselwirkungspartner | Schweregrad |
|------|------|
| Phenobarbital | Schwerwiegend (Major) |
| Johanniskraut | Schwerwiegend (Major) |
| Riociguat | Mäßig (Moderate) |
| Medroxyprogesteronacetat | Mäßig (Moderate) |

Die übrigen drei Einträge betreffen die Zielstrukturen des Wirkstoffs (VEGFR-1, VEGFR-2, VEGFR-3) und sind keine Wechselwirkungen im klinischen Sinn.

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation beachten.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf dem Modell (Evidenzstufe L5), ohne klinische Studien oder Publikationen. Zudem ist die einzige deutsche Zulassung erloschen, und die Sicherheitsdaten aus der Fachinformation fehlen.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Systematische Recherche zu klinischen Studien und Literatur zu VEGFR-Inhibitoren bei Zervixkarzinom und gynäkologischen Adenokarzinomen
- Detaillierte Wirkmechanismus-Daten (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM)
- Klärung des aktuellen Zulassungs- und Vermarktungsstatus in Deutschland
- Präklinische Daten oder frühe Studien zur Wirksamkeit bei den vorhergesagten Zervixkarzinom-Subtypen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

