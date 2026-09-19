---
layout: default
title: Pegvaliase
parent: Nur Modellvorhersage (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Pegvaliase
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

# Pegvaliase: Von Phenylketonurie zu diabetischer Retinopathie

## Ein-Satz-Zusammenfassung

Pegvaliase (DB12839) ist eine PEGylierte Phenylalanin-Ammoniak-Lyase (PAL)-Enzymtherapie, die klinisch zur Senkung des Blutphenylalanin-Spiegels bei Patienten mit Phenylketonurie (PKU) eingesetzt wird. Das TxGNN-Modell sagt eine hohe Assoziationspunktzahl für **diabetische Retinopathie** voraus, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt, und es wurde keine mechanistische Verbindung zwischen Phenylalanin-Stoffwechsel und diabetischer Retinopathie etabliert.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Phenylketonurie (PKU) *(abgeleitet von bekannter klinischer Anwendung — kein formales Indikationstext oder MOA-Datensatz im vorliegenden Evidence-Pack verfügbar)* |
| Vorhergesagte neue Indikation | Diabetische Retinopathie |
| TxGNN-Vorhersage-Score | 99.17% |
| Evidence-Niveau | L5 |
| Taiwan-Marktstatus | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Daten zum Wirkmechanismus im strukturierten Arzneimittel-Datensatz nicht verfügbar (gekennzeichnet als High-Severity-Datenlücke). Basierend auf der Repurposing-Begründung, die der Vorhersage beiliegt, ist Pegvaliase ein PEGyliertes Phenylalanin-Ammoniak-Lyase (PAL)-Enzym, das Phenylalanin in trans-Zimtsäure und Ammoniak umwandelt und klinisch zur Kontrolle des Blutphenylalanin-Spiegels bei PKU-Patienten eingesetzt wird.

Es gibt keine bekannte biologische Beziehung zwischen Phenylalanin-Stoffwechsel und der Pathophysiologie der diabetischen Retinopathie, die primär durch chronische Hyperglykämie, VEGF-vermittelte Angiogenese und vaskuläre Entzündung angetrieben wird. Dieselbe fehlende mechanistische Verbindung gilt auch für zwei eng verwandte Vorhersagen, die für dieses Medikament ebenfalls generiert wurden — **schwere nichtproliferative diabetische Retinopathie** (Score 99.16%) und **diabetische Katarakt** (Score 99.11%, stattdessen mit dem Aldose-Reduktase/Polyol-Weg verknüpft, der ebenfalls nicht mit PAL-Aktivität zusammenhängt).

Die hohen TxGNN-Scores über alle drei Vorhersagen von diabetischer Augenkrankheit hinweg spiegeln am wahrscheinlichsten topologische Ähnlichkeit innerhalb des Knowledge Graph wider (z.B. gemeinsame Graph-Nachbarn oder Embedding-Nähe) statt einer zugrunde liegenden pharmazeutischen Begründung. Ohne klinische, präklinische oder Literaturbelege zur Bestätigung der Verbindung sollte diese Vorhersage nur als explorativ betrachtet werden.

---

## Evidenz aus klinischen Studien

Aktuell keine verwandten klinischen Studien registriert

---

## Literaturbeweise

Aktuell sind keine verwandten Publikationen verfügbar

---

## Deutschland-Marktinformationen

Aktuell sind keine vermarkteten Produkte für Pegvaliase in Taiwan registriert (0 Genehmigungen, Marktstatus: Nicht vermarktet).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: TFDA-Kennzeichnungswarnungen/Kontraindikationen sind als Blocking-Datenlücke gekennzeichnet — erforderlich, bevor eine Sicherheits-Vorprüfung (S1) durchgeführt werden kann.)*

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Vorhersage wird nur durch einen TxGNN-Modell-Score gestützt (L5, keine klinischen Studien, keine Literatur, keine mechanistische Plausibilität). Das Medikament ist auch nicht aktuell in Taiwan vermarktet, und wesentliche Sicherheitsdaten (TFDA-Kennzeichnung, MOA) fehlen, daher kann dieser Kandidat nicht über das initiale Screening hinausgehen.

**Um voranzuschreiten, ist Folgendes erforderlich:**
- TFDA-Kennzeichnung/Warnungen und Kontraindikationen (Blocking-Datenlücke, DG001)
- Bestätigter Wirkmechanismus von DrugBank oder Primärliteratur (High-Priority-Datenlücke, DG002)
- Präklinische oder mechanistische Evidenz, die den PAL/Phenylalanin-Stoffwechsel mit diabetischer Retinal- oder Linsenopathologie verknüpft
- Mindestens eine Beobachtungsstudie oder Fallserie, bevor eine Progression über S0 hinaus in Betracht gezogen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

