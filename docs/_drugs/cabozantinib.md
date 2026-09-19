---
layout: default
title: Cabozantinib
parent: Nur Modellvorhersage (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: Kandidat für Arzneimittelneuzulassung — Ausstehende TxGNN-Bewertung

## Zusammenfassung in einem Satz

Cabozantinib (DB08875) ist ein Kleinmolekül-Kinase-Inhibitor mit etablierter antineoplastischer Aktivität, derzeit **nicht auf dem taiwanischen Markt** und ohne eingetragene zugelassene Indikationen in diesem Nachweispaket. Das Feld der durch TxGNN vorhergesagten Indikationen ist im aktuellen Nachweispaket **leer**, was bedeutet, dass noch kein Neuzulassungsziel generiert wurde. Dieser Bericht kann keine vollständige Neuzulassungsbewertung durchführen, bis die fehlenden Daten – insbesondere TxGNN-Vorhersagen, ursprüngliche Indikationsdaten und MOA-Details – bereitgestellt werden.

---

## Kurzübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Nicht in diesem Nachweispaket verfügbar |
| Vorhergesagte neue Indikation | Nicht verfügbar — `predicted_indications` Array ist leer |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Beweisniveau | L5 — Modellvorhersage noch nicht generiert |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Zytotoxizität

Cabozantinib ist ein gut charakterisierter Multi-Kinase-Inhibitor (VEGFR2, MET, RET, AXL), der klinisch in der Onkologie eingesetzt wird und das antineoplastische Kriterium nach Arzneimittelklasse erfüllt. Obwohl das aktuelle Nachweispaket keine DrugBank-Kategorietags oder bestätigte MOA-Texte enthält, identifizieren der Arzneimittelname und die DrugBank-ID (DB08875) das Arzneimittel eindeutig als einen gezielten antineoplastischen Wirkstoff.

| Punkt | Inhalt |
|-------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie — Multi-Kinase-Inhibitor (kein konventionelles Zytotoxikum) |
| Myelosuppressions-Risiko | Niedrig bis moderat (zielgerichtete Wirkstoffe führen zu einer geringeren hämatologischen Toxizität als konventionelle Zytotoxika; bitte mit der Gebrauchsinformation bestätigen) |
| Emetogenitätsklassifizierung | Niedrig |
| Überwachungselemente | CBC mit Differenzierung, Leberfunktion (AST/ALT), Nierenfunktion, Schilddrüsenfunktion, Blutdruck, Urinprotein |
| Handhabungsschutz | Standardvorsichtsmaßnahmen für zielgerichtete Wirkstoffe; bitte die Anforderungen für die zytotoxische Handhabung gegen institutionelle Protokolle und genehmigte Kennzeichnung bestätigen |

> Vollständige Toxizitätsdetails (Myelosuppressions-Inzidenz, spezifische Schwellenwerte) sind in diesem Nachweispaket nicht verfügbar. Bitte beachten Sie die genehmigten Warnhinweise und Vorsichtsmaßnahmen in der Gebrauchsinformation.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

> Wichtige Warnhinweise, Kontraindikationen und Arzneimittel-Wechselwirkungsdaten fehlen alle in diesem Nachweispaket (Datenlücke DG001). Die DDI-Abfrage hat null Ergebnisse zurückgegeben und kein TFDA-Kennzeichnungstext wurde analysiert. Es können keine Sicherheitsdaten hier ohne das Risiko von Ungenauigkeit gemeldet werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Nachweispaket ist strukturell unvollständig – das `predicted_indications` Array ist leer und zwei blockierende/hochgradig schwere Datenlücken (DG001: TFDA-Kennzeichnungstext; DG002: MOA) bleiben ungelöst. Es gibt kein Neuzulassungsziel zu bewerten, und es steht keine Zusammenfassung von Sicherheitssignalen für die Risikobewertung zur Verfügung.

**Um fortzufahren, wird Folgendes benötigt:**

- **TxGNN-Vorhersagen** — führen Sie die TxGNN-Pipeline für DB08875 erneut aus und füllen Sie `predicted_indications` mit mindestens einer Kandidatenkrankheit
- **Ursprüngliche Indikationsdaten** — rufen Sie den genehmigten Indikationstext aus der TFDA-Gebrauchsinformation ab (Abhilfe: TFDA-PDF herunterladen und analysieren)
- **Wirkungsmechanismus (MOA)** — Abfrage der DrugBank-API für DB08875 Pharmakodynamik und Zielprofilierung (Abhilfe gemäß DG002)
- **Sicherheitskennzeichnungstext** — analysieren Sie TFDA 仿單 auf wichtige Warnhinweise und Kontraindikationen (Abhilfe gemäß DG001)
- **DDI-Daten** — erneute Abfrage der DDI-Datenbank; aktuelles Ergebnis ist `not_found` mit null Wechselwirkungen, was möglicherweise einen Abfragefehler widerspiegelt, anstatt eines echten Mangels an Wechselwirkungen
- **Behördliche Quervalidierung** — obwohl Taiwan 0 Lizenzen aufweist, verfügt Cabozantinib über Genehmigungen in anderen Rechtsordnungen (EMA, FDA); eine länderübergreifende behördliche Recherche würde den behördlichen Kontext bereichern

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

