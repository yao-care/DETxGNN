---
layout: default
title: Andexanet Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 31
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Andexanet alfa: Von der Antagonisierung von Faktor-Xa-Inhibitoren zur Glanzmann-Thrombasthenie

## Zusammenfassung in einem Satz

Andexanet alfa ist ein rekombinantes Faktor-Xa-Decoy-Protein, das ursprünglich entwickelt wurde, um lebensbedrohliche Blutungen bei Patienten, die orale Faktor-Xa-Inhibitoren (z. B. Rivaroxaban, Apixaban) erhalten, zu antagonisieren. Das TxGNN-Modell sagt eine mögliche Verbindung zur **Glanzmann-Thrombasthenie** voraus, aber diese Vorhersage weist derzeit **keine klinischen Studien** und **keine unterstützenden Publikationen** auf – sie beruht vollständig auf Modell-Ähnlichkeit.

## Kurzübersicht

| Eintrag | Inhalt |
|------|------|
| Ursprüngliche Indikation | Antagonisierung der antikoagulanten Wirkung von Faktor-Xa-Inhibitoren bei Patienten mit schweren/lebensbedrohlichen Blutungen (abgeleitet aus dem Literaturkontext in diesem Paket; nicht in strukturierten Regulierungsdaten vorhanden) |
| Vorhergesagte neue Indikation | Glanzmann-Thrombasthenie |
| TxGNN-Vorhersage-Score | 99.77% |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfehlung | Zurückhalten |

## Warum ist diese Vorhersage plausibel?

Detaillierte Wirkmechanismus-Daten sind im strukturierten Datensatz nicht verfügbar (gekennzeichnet als Datenlücke). Basierend auf der in diesem Evidenzpaket erfassten Literatur wirkt Andexanet alfa als modifiziertes, katalytisch inaktives Faktor-Xa-Decoy – es bindet und sequestriert orale Faktor-Xa-Inhibitoren und stellt dadurch endogene Xa-Aktivität wieder her. Es liefert keine Gerinnungsfaktoren und wirkt nicht auf Thrombozytenaggregationspfade.

Die Glanzmann-Thrombasthenie ist dagegen eine angeborene Thrombozytenstörung, die durch einen GPIIb/IIIa-Rezeptormangel verursacht wird, welcher die Thrombozyten-zu-Thrombozyten-Aggregation unabhängig von der Gerinnungskaskade beeinträchtigt. Es gibt weder ein gemeinsames molekulares Ziel noch einen gemeinsamen Pfad zwischen der Antagonisierung eines Faktor-Xa-Inhibitors und der Korrektur eines GPIIb/IIIa-Defizits.

Die mechanistische Begründung des Evidenzpakets selbst ist auf diesem Punkt explizit: Der hohe TxGNN-Score spiegelt sehr wahrscheinlich die semantische Nähe des Modells zwischen den Konzepten „Blutungs-/Gerinnungsstörung" im Wissensgraph wider, anstatt eine echte pharmakologische Beziehung zu sein. Die gleiche Diskrepanz gilt für die beiden anderen Top-Kandidaten (primäre Thrombozyten-Freisetzungsstörung, Pseudo-von-Willebrand-Erkrankung), und sogar für Hämophilie (Rang 4), wo Literatur vorhanden ist, aber die Rolle von Andexanet alfa bei der *Interferenz mit* Faktor-Assays und *Antagonisierung* der Antikoagulation beschreibt – nicht bei der Behandlung des Faktor-Defizits selbst. Alle vier Kandidaten erhielten aus diesem Grund die Bewertung **Zurückhalten**.

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert.

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar.

### Zusätzliche betrachtete Kandidaten (nicht primärer Fokus)

| Rang | Erkrankung | TxGNN-Score | Evidenzgrad | Literatur | Empfehlung |
|------|---------|-------------|-----------------|------------|-----------------|
| 2 | Primäre Thrombozyten-Freisetzungsstörung | 99.76% | L5 | Keine | Zurückhalten |
| 3 | Pseudo-von-Willebrand-Erkrankung | 99.65% | L5 | Keine | Zurückhalten |
| 4 | Hämophilie | 99.10% | L4 | 11 Publikationen (hauptsächlich zur DOAC-Antagonisierung/Laborinterferenz, keine unterstützen therapeutische Anwendung bei Hämophilie) | Zurückhalten |

## Informationen zum deutschen Markt

Andexanet alfa wird derzeit in Deutschland nicht vermarktet (Marktstatus: nicht vermarktet), und es sind keine Zulassungsunterlagen in diesem Evidenzpaket vorhanden.

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Hinweis: TFDA/BfArM-Labelwarnungen und Kontraindikationen werden in diesem Evidenzpaket als **blockierende Datenlücke** gekennzeichnet, was bedeutet, dass eine Sicherheits-Vorabprüfung (S1) nicht abgeschlossen werden kann, bis dies behoben ist.

## Fazit und nächste Schritte

**Empfehlung: Zurückhalten**

**Begründung:**
Alle vier TxGNN-vorhergesagten Indikationen für Andexanet alfa zeigen keine Unterstützung durch klinische Studien oder Literatur, und die eigene mechanistische Analyse des Evidenzpakets kommt zu dem Ergebnis, dass die am höchsten bewertete Vorhersage (Glanzmann-Thrombasthenie) sehr wahrscheinlich ein Wissensgraph-Artefakt ist, anstatt ein echtes pharmakologisches Signal zu sein. In Kombination mit einer blockierenden Sicherheitsdatenlücke erfüllt dieser Kandidat nicht die Schwelle zur Weiterleitung.

**Um fortzufahren, wird folgendes benötigt:**
- Bestätigter Wirkmechanismus von DrugBank/Primärquellen (derzeit eine Datenlücke)
- TFDA/BfArM-Fachinformation (Warnungen, Kontraindikationen) — blockierende Lücke, erforderlich vor jeder S1-Sicherheits-Vorabprüfung
- Alle präklinischen oder mechanistischen Studien, die die Faktor-Xa-Decoy-Aktivität spezifisch mit Thrombozytenfunktionsstörungen verknüpfen, falls solche Belege entstehen
- Neubewertung, wenn neue klinische Studien oder Publikationen zu einer der vier Kandidaten-Indikationen registriert werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

