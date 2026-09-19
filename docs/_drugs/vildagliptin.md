---
layout: default
title: Vildagliptin
parent: Nur Modellvorhersage (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: Vom Typ-2-Diabetes mellitus zum fokalen Stiff-Limb-Syndrom

## Zusammenfassung in einem Satz

> Vildagliptin ist ein DPP-4-(Dipeptidyl-Peptidase-4-)Hemmer, ursprünglich für Typ-2-Diabetes mellitus (T2DM) entwickelt, der die Glukosekontrolle durch Verlängerung der endogenen GLP-1-/GIP-Aktivität verbessert.
> Die Top-Vorhersage des TxGNN-Modells ist **Fokales Stiff-Limb-Syndrom** mit einer Vorhersagepunktzahl von **99.88%**,
> aber dieser Kandidat hat derzeit **0 klinische Studien** und **0 unterstützende Publikationen**, und das Evidenzpaket selbst deutet auf keinen plausiblen mechanistischen Zusammenhang hin — dies ist ein reiner Modell-Score-Hit, keine substantiierte Repurposing-Hypothese.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Typ-2-Diabetes mellitus *(abgeleitet aus Literatur im Evidenzpaket; nicht formal in behördlichen Daten erfasst, da das Arzneimittel in Deutschland nicht zugelassen ist)* |
| Vorhergesagte neue Indikation | Fokales Stiff-Limb-Syndrom |
| TxGNN-Vorhersagepunktzahl | 99.88% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | Nicht zugelassen (Nicht zugelassen) |
| Anzahl der Genehmigungen | 0 |
| Empfehlung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Daten zum Wirkungsmechanismus sind offiziell als Datenlücke gekennzeichnet (DrugBank-Abfrage ausstehend). Basierend auf Informationen aus der begleitenden Literatur und Studienevidence ist bekannt, dass Vildagliptin DPP-4 hemmt, wodurch die Halbwertszeit des endogenen GLP-1 und GIP verlängert wird, die glukoseabhängige Insulinsekretion verbessert und die unangemessene Glukagonfreisetzung unterdrückt wird — seine Wirksamkeit bei T2DM ist in dieser Arzneistoffklasse gut belegt.

Jedoch besteht für den Top-Kandidaten **Fokales Stiff-Limb-Syndrom** keine plausible mechanistische Verbindung. Das Stiff-Limb-/Stiff-Person-Syndrom ist eine autoimmune neurologische Erkrankung, die hauptsächlich durch anti-GAD65-Antikörper und gestörte GABAerge inhibitorische Neurotransmission angetrieben wird — eine Pathophysiologie, die völlig unabhängig von Inkretin-/Glukosesignalisierung ist. Die Begründung des Evidenzpakets erklärt explizit: *\"Kein erkennbarer mechanistischer Zusammenhang... Dies ist ein reines TxGNN-Vorhersagescore ohne biologische Unterstützung.\"* Die gleiche Situation gilt für TxGNNs weitere Top-5-Treffer (klassisches Stiff-Person-Syndrom, Thiamin-responsive Dysfunktionssyndrom, Opsismodysplasie) — alle sind seltene, strukturell oder genetisch bedingte Erkrankungen ohne bekannte DPP-4-Verbindung.

Angesichts des sehr hohen Rohscores, aber völliger Abwesenheit von bestätigender Evidenz, sollte diese Vorhersage derzeit als statistisches Artefakt der Knowledge-Graph-Einbettung betrachtet werden und nicht als glaubwürdige Repurposing-Hypothese.

---

## Klinische Studien-Evidenz

Derzeit keine verwandten klinischen Studien registriert.

---

## Literatur-Evidenz

Derzeit keine verwandte Literatur verfügbar.

---

## Marktstatus Deutschland

Vildagliptin ist in Deutschland derzeit **nicht zugelassen** (Nicht zugelassen) gemäß dieses Evidenzpakets, mit 0 registrierten Genehmigungen. Keine Produkt-/Lizenzunterlagen sind für diesen Kandidaten verfügbar.

---

## Sicherheitsüberlegungen

Bitte siehe Fachinformation für Sicherheitsinformationen. (Schlüsselwarnungen, Kontraindikationen und Wechselwirkungsdaten sind alle derzeit als Datenlücken gekennzeichnet — TFDA-Label-Abruf ist ein Blockierungsfaktor, siehe Schlussfolgerung.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Top-Vorhersage (Fokales Stiff-Limb-Syndrom) hat Evidenzstufe L5 — einen Modell-Score mit Null klinischen Studien, Null Literatur und keinem erkennbaren mechanistischen Anlass. Kombiniert mit dem fehlenden Marktzugang des Arzneimittels in Deutschland und fehlenden MOA-/Label-Daten (DG001 blockiert, DG002 hoher Schweregrad), gibt es keine Grundlage, diese Indikation über die exploratorische Sichtung hinaus voranzutreiben.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/Abruf der offiziellen Fachinformation (Warnungen, Kontraindikationen) — derzeit blockiert S1-Sicherheits-Screening
- Bestätigte DrugBank-MOA-Daten
- Beliebige präklinische oder mechanistische Evidenz, die DPP-4-/Inkretin-Signalwege mit autoimmun vermittelten Stiff-Person-Spektrum-Erkrankungen verbindet, bevor weitere Evaluierung gerechtfertigt ist

---

**Zusätzliche Notiz — Alternative Signale, die verfolgt werden sollten:**
Unter den 10 TxGNN-vorhergesagten Indikationen für dieses Arzneimittel sticht **Typ-1-Diabetes mellitus** (Rang 10, Score 99.37%) als der einzige Kandidat mit substantieller Evidenz hervor: Evidenzstufe **L2**, einschließlich einer abgeschlossenen Phase-2-RCT, die direkt Rapamycin + Vildagliptin zur Funktionswiederherstellung von β-Zellen bei langjährigem T1D testet (NCT02803892; entsprechende RCT-Publikation PMID 33124663), plus mechanistische RCT-Evidenz zur Glukagon-Gegenregulation bei T1D (PMID 22855332). Dies ist mechanistisch kohärent (Inkretin-vermittelte β-Zell-Erhaltung als Adjuvans, nicht als Insulinersatz) und ist ein besser zu rechtfertigender Kandidat für eine Evaluierung in der „Forschungsfrage"-Phase als der Top-Ranking-Stiff-Limb-Syndrom-Hit, obwohl die meisten seiner 40 und mehr aufgeführten Studien T2DM-Hintergrundrauschen sind und vor Gebrauch einzeln neu bewertet werden müssten.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

