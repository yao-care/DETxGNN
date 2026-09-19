---
layout: default
title: Lonoctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 237
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
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

# Lonoctocog Alfa: Von Hämophilie A zu Pseudo-von-Willebrand-Erkrankung

## Zusammenfassung in einem Satz

> Lonoctocog alfa ist eine rekombinante Faktor-VIII-Ersatztherapie (rFVIII), die für die Behandlung von **Hämophilie A** eingesetzt wird.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam bei der **Pseudo-von-Willebrand-Erkrankung** sein könnte,
> aber derzeit **keine klinischen Studien** und **keine Veröffentlichungen** unterstützen diese Richtung — die Vorhersage ist modellgestützt, und die mechanistische Überprüfung des Evidenzpakets selbst kennzeichnet sie als wahrscheinlich falsch-positiv.

## Schnellübersicht

| Element | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | Hämophilie A (aus bekannter rFVIII-Pharmakologie hergeleitet; nicht im aktuellen Datensatz bestätigt — `original_indications` ist leer und TFDA-Labeldaten stellen eine blockierende Datenlücke dar) |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Erkrankung |
| TxGNN-Vorhersageergebnis | 99.85% |
| Evidenzlevel | L5 |
| Marktstatus Taiwan | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Abwarten |

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad). Basierend auf bekannter Pharmakologie ist Lonoctocog alfa ein rekombinantes Faktor-VIII-Produkt, das defizientes oder dysfunktionales Koagulations-Faktor VIII ersetzt, und seine Wirksamkeit bei Hämophilie A ist gut etabliert.

Allerdings gehören die vier wichtigsten TxGNN-prognostizierten Indikationen — Pseudo-von-Willebrand-Erkrankung, primäre Thrombozytensekretionstörung, Glanzmann-Thrombasthenie und Scott-Syndrom — alle zu **Thrombozyten-Funktions- oder Thrombozyten-Rezeptor-Störungen**, nicht zu Koagulationsfaktor-Mängeln. Nach der eigenen mechanistischen Analyse des Evidenzpakets entstehen die hohen Ähnlichkeitsergebnisse des Modells wahrscheinlich aus einer indirekten Assoziation im Wissensgraph zwischen FVIII und von-Willebrand-Faktor (die beiden zirkulieren normalerweise als Komplex und werden oft zusammen diagnostisch gemessen), anstatt einen echten gemeinsamen therapeutischen Mechanismus widerzuspiegeln.

Keine der vier Kandidatenkrankheiten hat eine Pathophysiologie, die durch FVIII-Ersatz korrigiert werden würde (GPIbα-Funktionsgewinn, Speicherpool-Defekt von Thrombozyten, GPIIb/IIIa-Mangel und TMEM16F-Scramblase-Mangel). Das Evidenzpaket charakterisiert diese Assoziationen explizit als mechanistisch implausibel und nicht unterstützt durch klinische oder Literaturbeweise.

## Evidenz aus klinischen Studien

Derzeit sind keine damit verbundenen klinischen Studien registriert.

## Literaturbeweise

Derzeit ist keine verwandte Literatur verfügbar.

## Zusätzliche prognostizierte Kandidaten (nicht weiter bewertet)

| Rang | Krankheit | TxGNN-Ergebnis | Evidenzlevel | Empfehlung | Wichtigste Bedenken |
|------|-----------|----------------|--------------|------------|-------------------|
| 2 | Primäre Sekretionstörung von Thrombozyten | 99.84% | L5 | Abwarten | Defekt der Thrombozyten-Granulensekretion; kein bekannter FVIII-Mechanismus, keine unterstützenden Beweise |
| 3 | Glanzmann-Thrombasthenie | 99.76% | L5 | Abwarten | GPIIb/IIIa-Mangel; nicht mit dem FVIII-Pathway verwandt |
| 4 | Scott-Syndrom | 99.44% | L5 | Abwarten | Membran-Scramblase (TMEM16F) Defekt; nicht durch FVIII-Ersatz korrigierbar |

## Marktinformationen für Deutschland

Lonoctocog alfa ist **noch nicht auf dem taiwanesischen Markt eingeführt** — es gibt keine Genehmigungsakten (`total_licenses = 0`, `licenses = []`).

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Alle vier TxGNN-prognostizierten Indikationen werden nur durch das Modell-Ergebnis unterstützt (Evidenzlevel L5), ohne klinische Studien und ohne Veröffentlichungen. Die eigene mechanistische Rationale des Evidenzpakets argumentiert, dass dies wahrscheinlich falsch-positive Assoziationen sind, die durch die FVIII–vWF-Diagnostik-Komplex-Beziehung anstatt einer echten Umdestinierungshypothese verursacht werden. In Kombination mit einer blockierenden Datenlücke zu TFDA-Label-Warnhinweisen/Kontraindikationen erfüllt dieser Kandidat nicht den Standard, um S0 zu verlassen.

**Um voranzukommen, ist Folgendes erforderlich:**
- TFDA-Label (Warnhinweise/Kontraindikationen) — derzeit eine blockierende Datenlücke (DG001)
- Bestätigter Wirkmechanismus aus DrugBank/maßgeblicher Quelle (DG002)
- Bestätigte ursprüngliche Indikation und behördlicher Status (aktueller Datensatz hat leere `original_indications` und 0 Taiwan-Lizenzen)
- Unabhängige mechanistische Überprüfung zur Bestätigung oder Widerlegung der Hypothese „falsch-positiv über vWF-FVIII-Komplex", bevor weitere Evidenzsammlung beauftragt wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

