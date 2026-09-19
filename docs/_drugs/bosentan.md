---
layout: default
title: Bosentan
parent: Nur Modellvorhersage (L5)
nav_order: 60
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Bosentan: Arzneimittelrepositioning-Bewertung — Unzureichende Daten für eine vollständige Bewertung

## Zusammenfassung in einem Satz

Bosentan (DrugBank ID: DB00559) ist ein Kandidat für die Arzneimittelrepositioning dieser Runde. Derzeit sind in der Evidence Pack jedoch **keine neuen durch TxGNN vorhergesagten Indikationen**, **keine Aufzeichnungen ursprünglicher Indikationen**, **keine Sicherheitsdaten** vorhanden, und das Arzneimittel ist in Taiwan noch nicht vermarktet, daher kann der Standard-Arzneimittelrepositioning-Bewertungsprozess in der gegenwärtigen Phase nicht durchgeführt werden. Es wird empfohlen, die Bewertung dieses Kandidaten auszusetzen, bis wichtige Datenlücken gefüllt sind.

---

## Schnellübersicht

| Eintrag | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Keine Aufzeichnung in vorliegenden Daten |
| Vorhergesagte neue Indikation | Keine (TxGNN erzeugte keine Vorhersageergebnisse) |
| TxGNN-Vorhersage-Bewertung | n. z. |
| Evidenzstufe | L5 (nur Modellebene, keine tatsächlichen Untersuchungen) |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage angemessen?

Derzeit können detaillierte Daten zum Wirkungsmechanismus nicht beschafft werden. Basierend auf vorliegenden Daten wurde Bosentan (DB00559) erfolgreich über die DrugBank-Abfrage aufgezeichnet, aber die Wirkungsmechanismus-Felder (MOA) sind weiterhin eine Datenlücke, die über die DrugBank-API nachgezogen werden müssen.

Ursprüngliche Zulassungsindikationen sind ebenfalls nicht in dieser Evidence Pack aufgezeichnet (`original_indications` ist ein leeres Array), die TFDA-Datenbankabfrage ergab 0 Ergebnisse, was darauf hinweist, dass dieses Arzneimittel in Taiwan keine zugelassenen Markteinträge enthält, auf die verwiesen werden kann.

Da TxGNN keine Vorhersageindikationen erzeugt hat (`predicted_indications` ist ein leeres Array), können weder die Wirkungsmechanismus-Assoziationsanalyse noch die Bewertung der Angemessenheit neuer Indikationen in der gegenwärtigen Phase durchgeführt werden.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studiendaten vorhanden.

---

## Literaturevidenz

Derzeit sind keine zugehörigen Literaturdaten vorhanden.

---

## Taiwan-Marktinformationen

Bosentan ist derzeit in Taiwan **nicht vermarktet**, die TFDA-Datenbankabfrage zeigt keine Arzneimittelzulassungsaufzeichnungen (Abfragedatum: 2026-03-29, Anzahl der Abfrageergebnisse: 0).

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Warnhinweise und Kontraindikationen in der Produktmonographie.

> **Hinweis**: Obwohl die TFDA-Monographie-Abfrage erfolgreich zurückgegeben wurde (`result_count: 1`), wurden die Sicherheitsfelder (Warnhinweise, Kontraindikationen) noch nicht in die Evidence Pack geparst. Dies ist eine **Datenlücke auf Blocking-Ebene (DG001)**, die die S1-Sicherheitsbewertung blockiert und kann nicht durchgeführt werden, bis dies behoben ist.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Diese Evidence Pack weist wichtige fehlende Felder auf, einschließlich TxGNN-Vorhersageindikationen, ursprünglicher Indikationen, MOA und Sicherheitsdaten, daher kann die Repositioning-Eignung von Bosentan in der gegenwärtigen Phase nicht wirksam bewertet werden; es wird empfohlen, bis zur Füllung wichtiger Datenlücken zu warten.

**Zum Fortfahren wird Folgendes benötigt:**

- **\[DG001 — Kritisch\]** TFDA-Monographie-PDF parsen, um Warnhinweise (key warnings) und Kontraindikationen (contraindications) zu extrahieren, um die S1-Sicherheitsbewertungssperre aufzuheben
- **\[DG002 — Hoch\]** Wirkungsmechanismus-Daten (MOA) über DrugBank API nachziehen, um die Wirkungsmechanismus-Assoziationsanalyse zu unterstützen
- Führen Sie den TxGNN-Vorhersageprozess erneut aus, um zu bestätigen, ob neue Indikationsvorhersageergebnisse für Bosentan erzeugt werden; falls weiterhin leer, müssen die Gründe geklärt werden (Knoten nicht erfasst, Bewertung zu niedrig oder bereits gefiltert)
- Ursprüngliche Zulassungsindikationen (`original_indications`) nachziehen, abrufbar von DrugBank, EMA oder FDA-Etiketten
- DDI-Datenbank erneut abfragen (aktueller Abfragestatus: `not_found`), um zu bestätigen, ob Arzneimittelwechselwirkungsdaten vorhanden sind

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

