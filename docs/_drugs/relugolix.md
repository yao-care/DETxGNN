---
layout: default
title: Relugolix
parent: Nur Modellvorhersage (L5)
nav_order: 334
evidence_level: L5
indication_count: 0
---

# Relugolix
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **0** 
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

# RELUGOLIX: Bewertung der Umwidmung — Ausstehende TxGNN-Vorhersagen

## Zusammenfassung

Relugolix (DrugBank: DB11853) ist ein oral wirksamer GnRH-Rezeptor-Antagonist, der in mehreren Märkten (USA, EU, Japan) für fortgeschrittenes Prostatakarzinom zugelassen ist und in Kombination für Uterusmyome und Endometriose. Das aktuelle Evidence Pack ist kritisch unvollständig: TxGNN-Umwidmungsvorhersagen wurden noch nicht generiert, und sowohl Sicherheitsmarkierung als auch MOA-Daten fehlen. **Bis die beiden vorgelagerten Datenlücken gelöst sind, ist eine Hold-Entscheidung erforderlich.**

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Vorhergesagte neue Indikation | Ausstehend — TxGNN-Vorhersagen noch nicht generiert |
| Empfehlung zur Entscheidung | Hold |

---

## Über dieses Arzneimittel

Relugolix ist ein nicht-peptidischer, oral wirksamer GnRH-(Gonadotropin-Releasing-Hormon-)Rezeptor-Antagonist. Durch kompetitives Blockieren von hypophysären GnRH-Rezeptoren unterdrückt es schnell die LH- und FSH-Sekretion und treibt Testosteron (Männer) oder Estradiol (Frauen) auf Kastrationsspiegel. Dies unterscheidet es von GnRH-Agonisten, die vor der Suppression zunächst zu einem Hormonflare führen.

Wichtige außerhalb Deutschlands zugelassene Indikationen:

- **Fortgeschrittenes Prostatakarzinom** — Orgovyx® (FDA, EMA, PMDA zugelassen)
- **Uterusmyome / Endometriose** — Myfembree® (in Kombination mit Estradiol + Norethindronacetat)

Da Relugolix für hormonempfindliche Krebserkrankungen zugelassen ist und über die Unterdrückung der Hormonachse wirkt, qualifiziert es sich für den Zytotoxizitätsabschnitt als ein gezieltes hormonelles Mittel.

---

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Gezielt wirkende Therapie — GnRH-Rezeptor-Antagonist (hormonelles Mittel) |
| Myelosuppressions-Risiko | Niedrig (nicht-zytotoxischer Mechanismus; kein direkter Knochenmarkeffekt) |
| Emetogenitätsklassifizierung | Niedrig |
| Überwachungselemente | Serum-Testosteron / Estradiol, kardiovaskuläres Risiko (QTc, Lipide, Blutdruck), Knochenmineraldichte (Langzeit-ADT) |
| Handhabungsschutz | Standardhandhabung — kein konventionelles Zytotoxikum; keine spezielle Entsorgung zytotoxischer Abfälle erforderlich |

---

## Sicherheitserwägungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Das Evidence Pack enthält keine TxGNN-Umwidmungskandidaten und es fehlen sowohl MOA-Details als auch Sicherheitsmarkierung, was es unmöglich macht, irgendeine neue Indikation in dieser Phase zu bewerten. Ein Fortschritt kann nicht erfolgen, bis die vorgelagerte Datenerfassung abgeschlossen ist.

**Zum Fortfahren ist Folgendes erforderlich:**

- **[Blockierend]** Packungsbeilage von EMA/TFDA abrufen und analysieren für Warnungen und Kontraindikationen (Datenlücke DG001)
- **[Hoch]** Vollständige MOA-Datenintegration von DrugBank API abschließen (Datenlücke DG002)
- **[Erforderlich]** TxGNN-Inferenz-Pipeline ausführen, um Umwidmungskandidaten-Vorhersagen für RELUGOLIX (DB11853) zu generieren
- **[Erforderlich]** Klinische Versuchs- und Literaturbeweise für die am höchsten bewertete vorhergesagte Indikation sammeln
- **[Erforderlich]** Ein vollständiges Evidence Pack (v5+) erneut einreichen, sobald alle Datenlücken behoben sind

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

