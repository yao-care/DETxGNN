---
layout: default
title: Tadalafil
parent: Nur Modellvorhersage (L5)
nav_order: 376
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **8** 
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

# Tadalafil: Von nicht aufgezeichneter ursprünglicher Indikation zu Ambras-Typ-Hypertrichosis universalis congenita

## Zusammenfassung in einem Satz

> Das Evidenzpaket verzeichnet die ursprüngliche zugelassene Indikation oder den Wirkmechanismus von Tadalafil nicht (beide sind als Datenlücken gekennzeichnet), und das Arzneimittel wird derzeit **in Deutschland nicht vermarktet**.
> Die Top-Vorhersage des TxGNN-Modells ist **Ambras-Typ-Hypertrichosis universalis congenita**, eine seltene angeborene Haarwuchsstörung,
> aber diese wird durch **0 klinische Studien** und **0 Publikationen** gestützt — und die Begründung des Evidenzpakets selbst kennzeichnet sie als wahrscheinliches Netzwerkartefakt statt eines echten Signals.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht aufgezeichnet im Evidenzpaket (keine zugelassenen Indikationen oder Lizenzen in der Datei) |
| Vorhergesagte neue Indikation | Ambras-Typ-Hypertrichosis universalis congenita |
| TxGNN-Vorhersage-Score | 99.98% (rank 438) |
| Evidenzebene | L5 |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (original_moa: Data Gap). Auf Grundlage des pharmakolagischen Hintergrunds, der im Evidenzpaket selbst zitiert wird, ist Tadalafil ein Phosphodiesterase-Typ-5-(PDE5)-Hemmer, der über den cGMP/NO-Weg wirkt.

Es gibt jedoch **keine etablierte biologische Verbindung** zwischen PDE5/cGMP-Signalisierung und Ambras-Typ-Hypertrichosis universalis congenita, die eine seltene angeborene Störung des Haarfollikelwachstums mit unterschiedlicher genetischer Ätiologie ist. Die Begründung des Evidenzpakets selbst macht explizit deutlich, dass diese Vorhersage "keine Wirkmechanismus-Hypothese" hat und "verdächtigt ist, Netzwerklärm zu sein" — d.h. eine indirekte, fehlerhafte Graphenverbindung zwischen dem Arzneimittel-Knoten und einem seltenen Krankheits-Genotyp-Knoten, kein echtes pharmakologisches Signal.

Angesichts der vollständigen Abwesenheit von Daten zur ursprünglichen Indikation, MOA-Daten, klinischen Studien und Fachliteratur sollte diese Top-Ranking-Vorhersage als ein hoher TxGNN-Score ohne unterstützende Evidenz behandelt werden, nicht als eine glaubwürdige Umpositionierungs-Hypothese.

---

## Evidenz aus klinischen Studien

Derzeit sind keine relevanten klinischen Studien registriert

---

## Literaturevidenz

Derzeit ist keine relevante Literatur verfügbar

---

## Informationen zum Marktstatus in Deutschland

Es sind derzeit keine Marktgenehmigungen in Deutschland aufgezeichnet (Marktstatus: Nicht vermarktet; total_licenses: 0).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

**Wichtiger Hinweis:** Das Evidenzpaket kennzeichnet **TFDA-Kennzeichnungswarnungen/Kontraindikationen** als eine **Blockierend**-Datenlücke (DG001) — ohne diese Daten kann dieser Kandidat nicht zur Sicherheitsvorprüfung (S1) voranschreiten, unabhängig von der vorhergesagten Indikation. Wirkmechanismus-Daten werden auch als Datenlücke mit hohem Schweregrad (DG002) gekennzeichnet.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Top-Ranking-Vorhersage (Ambras-Typ-Hypertrichosis universalis congenita) hat keine unterstützenden klinischen Studien, Literatur oder mechanistische Plausibilität — das Evidenzpaket selbst identifiziert sie als wahrscheinlich Graphenlärm. Kombiniert mit fehlender ursprünglicher Indikation, MOA- und TFDA-Sicherheitsdaten erfüllt dieser Kandidat nicht die minimale Evidenzschwelle zum Voranschreiten.

**Um voranzuschreiten, ist Folgendes erforderlich:**
- TFDA-Kennzeichnungswarnungen und Kontraindikationen (DG001, blockierend — vor jeder S1-Sicherheitsvorprüfung erforderlich)
- Wirkmechanismus von Tadalafil und ursprüngliche zugelassene Indikationen (DG002)
- Unabhängige Überprüfung, ob der TxGNN-Score für diesen spezifischen Kandidaten ein echtes Signal oder ein Graphen-Artefakt widerspiegelt, da der Begründungstext selbst ein Rausch-Flag setzt

**Hinweis zu anderen Kandidaten in diesem Paket:** Zwei Vorhersagen mit niedrigerem Rang verdienen separate Aufmerksamkeit statt Ablehnung zusammen mit Rank 1:
- **Rank 7 — Kyphoskoliotische Herzerkrankung** (Forschungsfrage-Phase): PDE5-Hemmer sind eine etablierte Medikamentenklasse für pulmonale arterielle Hypertonie (PAH), und durch Kyphoskoliose bedingte restriktive Lungenerkrankung kann zu sekundärer PAH führen. Dies ist eine plausible Klasseneffekt-Hypothese, die es wert ist zu überprüfen, ob Tadalafils bekannte PAH-Indikation (z.B. Adcirca) einfach aus dem original_indications-Feld dieses Evidenzpakets weggelassen wurde.
- **Rank 8 — Migräne mit Hirnstamm-Aura**: Die einzige unterstützende Zitierung ist ein Fallbericht von Tadalafil-*induzierter* Migräne-Aura (ein unerwünschtes Ereignis), nicht ein Behandlungseffizienz-Signal. Dies sollte als Sicherheitssignal gelesen werden, nicht als Umpositionierungs-Kandidat.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

