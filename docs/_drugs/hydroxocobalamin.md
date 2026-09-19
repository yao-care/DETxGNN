---
layout: default
title: Hydroxocobalamin
parent: Nur Modellvorhersage (L5)
nav_order: 189
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Hydroxocobalamin: Vom Vitamin-B12-Mangel zur blutenden Ösophagusvarizenblutung

## Zusammenfassung in einem Satz

> Hydroxocobalamin ist ein Vitamin-B12-Analogon, das klinisch für B12-Mangel etabliert ist und als Wirkstoff des Zyanidvergiftungs-Gegenmittels Cyanokit dient.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam sein könnte für **blutende Ösophagusvarizenblutungen**,
> aber derzeit **unterstützen keine klinischen Studien oder Veröffentlichungen** diese Richtung — die Vorhersage basiert allein auf dem Modellscore und einer mechanistischen Hypothese.

---

## Kurzer Überblick

| Element | Inhalt |
|------|------|
| Originalindikation | Nicht dokumentiert (keine deutsche Marktgenehmigung im Nachweispaket); bekannte Anwendungen sind Vitamin-B12-Mangel und Gegenmittel gegen Zyanidvergiftung |
| Vorhergesagte neue Indikation | Blutende Ösophagusvarizenblutung |
| TxGNN-Vorhersage-Score | 99.23% |
| Nachweisstufe | L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur) |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage vertretbar?

Derzeit sind detaillierte Daten zum Wirkmechanismus im Nachweispaket nicht verfügbar. Basierend auf bekannten Informationen ist Hydroxocobalamin ein Vitamin-B12-Analogon in Hydroxyl-Form, das für B12-Mangel verwendet wird und bei hohen Dosen als Stickstoffmonoxid (NO)-Fänger im Zyanidvergiftungs-Gegenmittel Cyanokit wirkt.

Die Begründung für die Arzneimittelumpositionierung ist rein mechanistisch: Die NO-Fänger-Aktivität von Hydroxocobalamin kann eine Vasokonstriktion induzieren — eine Eigenschaft, die bereits beim vasoplegischen Schock genutzt wird. Die Standard-Pharmakotherapie für blutende Ösophagusvarizenblutungen (terlipressin, octreotide, vasopressin) wirkt durch Splanchnikusvasokonstriktion zur Senkung des Pfortaderdrucks, daher gibt es eine theoretische Überlappung der Wirkmechanismen.

Diese Verbindung ist jedoch spekulativ. Es gibt keine Tier-, pharmakodynamischen oder klinischen Belege dafür, dass Hydroxocobalamin den Pfortaderdruck senkt oder Varizenblutungen kontrolliert, und es gibt keine Daten über Sicherheit/Metabolismus bei Patienten mit Zirrhose und beeinträchtigter hepatischer Clearance. Eine zweite, eng verwandte Vorhersage — Ösophagusvarizenblutungen *ohne* Blutung (gleicher TxGNN-Score) — ist mechanistisch sogar schwächer, da diese Indikation eine chronische prophylaktische Drucksenkung erfordert (typischerweise nicht selektive Beta-Blocker) statt eines akuten vasokonstriktiven Mittels, und es existieren keine Langzeitsicherheitsdaten für diesen Anwendungsfall.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine verwandte Literatur verfügbar.

---

## Informationen zum deutschen Markt

Hydroxocobalamin ist derzeit unter diesem Nachweispaket nicht in Deutschland vermarktet; es sind keine BfArM-Genehmigungsdatensätze verfügbar (0 Lizenzen registriert).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die Vorhersage wird nur durch einen TxGNN-Modellscore (L5) und einen theoretischen NO-Fänger-/Vasokonstriktionsmechanismus gestützt, ohne klinische Studien, Literatur oder präklinische Daten, die Wirksamkeit oder Sicherheit bei Pfortalhypertonie/Varizenblutung bestätigen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Packungsbeilage mit Warnhinweisen und Kontraindikationen (derzeit eine blockierende Datenlücke — erforderlich vor jeglicher S1-Sicherheitsprüfung)
- Bestätigter Wirkmechanismus (DrugBank-API-Abfrage, derzeit eine High-Severity-Datenlücke)
- Präklinische/pharmakodynamische Belege für eine Pfortaderdrucksenkung mit Hydroxocobalamin in zirrotischen Modellen
- Frühe klinische oder Fall-basierte Daten vor Fortschritt über die Modellvorhersage-Phase hinaus

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

