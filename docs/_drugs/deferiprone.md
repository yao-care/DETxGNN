---
layout: default
title: Deferiprone
parent: Nur Modellvorhersage (L5)
nav_order: 116
evidence_level: L5
indication_count: 9
---

# Deferiprone
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

# Deferiprone: Von der Eisenchelationstherapie zur hepatischen Porphyrie

## Ein-Satz-Zusammenfassung

Deferiprone ist ein orales Eisenchelator; basierend auf Daten in diesem Evidenzpaket besteht seine etablierte klinische Rolle in der Verwaltung von **Transfusioneller Eisenüberladung** (z. B. bei Beta-Thalassämie — siehe Rangplatz-8-Kandidat unten), obwohl die formale ursprüngliche Indikation und TFDA-Zulassung in diesem Paket nicht dokumentiert sind.
Die Top-Vorhersage des TxGNN-Modells für dieses Arzneimittel ist **Hepatische Porphyrie** mit einer Vorhersage-Genauigkeit von 99,20% — aber **keine klinischen Studien und keine Fachliteratur** unterstützen derzeit diese spezifische Richtung, und die eigene mechanistische Rationale des Modells kennzeichnet den biologischen Zusammenhang als schwach.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert in diesem Evidenzpaket (`original_indications` leer; siehe DG001/DG002). Kontext der Arzneimittelklasse aus Paket: orales Eisenchelator, etablierte Anwendung bei Transfusioneller Eisenüberladung (siehe Beta-Thalassämie-Kandidat, Rang 8) |
| Vorhergesagte neue Indikation | Hepatische Porphyrie |
| TxGNN-Vorhersage-Genauigkeit | 99,20% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine klinischen oder Fachliteratur-Belege) |
| Markt-Status in Deutschland | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (`original_moa: [Datenlücke]`, gekennzeichnet als DG002 in diesem Paket). Basierend auf anderswo in diesem Evidenzpaket vorhandenen Informationen (Begründung für Rang 8) ist Deferiprone ein orales Tris-Hydroxypyridion-Eisenchelator, das Zellmembranen durchdringt, freies Eisen(III) bindet und dessen urinäre Ausscheidung fördert — ein Wirkmechanismus, der direkt für Eisenüberladungszustände wie die bei chronisch transfundierten Patienten relevant ist.

Für **Hepatische Porphyrie** ist der biologische Zusammenhang jedoch, wie die eigene Umpositionierungs-Begründung des Modells ausdrücklich darlegt, schwach: Hepatische Porphyrie resultiert aus Enzymmängeln im Häm-Biosynthese-Weg, die zur Ansammlung giftiger Zwischenprodukte führen, nicht aus Gewebeeisen-Überladung. Die eisenchelatbildende Wirkung von Deferiprone hat keinen etablierten pathophysiologischen Zusammenhang mit diesem Krankheitsprozess. Dieser Top-Kandidat nach Rangplatz reflektiert daher ein **statistisches Ähnlichkeitssignal von TxGNN**, nicht eine Mechanismus- oder evidenzgestützte Hypothese.

**Anmerkung zu diesem Multi-Kandidaten-Paket:** Unter den 9 bewerteten vorhergesagten Indikationen für Deferiprone wird nur **Beta-Thalassämie mit anderen Manifestationen** (Rang 8) durch tatsächliche Fachliteratur unterstützt (2 Veröffentlichungen, Evidenzstufe L3) und trägt eine Empfehlung „Weiterverfolgen mit Schutzmechanismen" — konsistent mit der realen Verwendung von Deferiprone bei Transfusions-abhängiger Eisenüberladung. Der Top-Kandidat nach Genauigkeit (hepatische Porphyrie, Gegenstand dieses Berichts) hat weder Studien noch Fachliteratur und wird mit **Abwarten** empfohlen. Reviewer sollten Evidenzstärke, nicht Rangplatz-Score allein, bei der Priorisierung von Kandidaten aus diesem Paket berücksichtigen.

---

## Klinische Studien-Evidenz

Derzeit keine zugehörigen klinischen Studien registriert

---

## Fachliteratur-Evidenz

Derzeit keine zugehörige Fachliteratur verfügbar

---

## Markt-Information Deutschland

Für dieses Arzneimittel werden derzeit keine Marktzulassungen in Deutschland/Taiwan gehalten (`total_licenses: 0`).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Anmerkung: `key_warnings`, `contraindications` und DDI-Daten sind alle als Datenlücken in diesem Paket gekennzeichnet. DG001 — fehlende TFDA-Packungsbeilage-Warnhinweise/Kontraindikationen — ist als eine **Blockierende** Schweregrad-Datenlücke gekennzeichnet, was bedeutet, dass sie derzeit eine formale S1-Sicherheitsprüfung für jede Indikation unter diesem Arzneimittel verhindert.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die Vorhersage für hepatische Porphyrie hat keine unterstützenden klinischen Studien oder Fachliteratur, und die eigene mechanistische Rationale des Modells bewertet die biologische Plausibilität als schwach (L5, keine direkte Krankheitsmechanismus-Überlappung mit Eisenchelation). In Kombination mit einer Blockierenden-Schweregrad-TFDA-Sicherheitsdatenlücke für das Arzneimittel insgesamt kann dieser Kandidat nicht über das initiale Screening hinaus vorankommen.

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA-Packungsbeilage (Warnhinweise, Kontraindikationen) — erforderlich, um die Blockierende Lücke (DG001) zu klären, bevor eine S1-Sicherheitsprüfung erfolgen kann
- Dokumentierter Wirkmechanismus (DG002), um die mechanistische Plausibilität über alle Kandidaten-Indikationen hinweg ordnungsgemäß zu bewerten
- Präklinische oder mechanistische Studien, die Eisenchelation spezifisch zu Störungen des Häm-Biosynthese-Weges verknüpfen, wenn diese Indikation weiterverfolgt werden soll
- Alternativ sollten Sie erwägen, Evaluierungsressourcen auf den **Beta-Thalassämie-mit-anderen-Manifestationen-Kandidaten** (Rang 8) umzuleiten, der bereits Fachliteratur-Unterstützung und einen Status „Weiterverfolgen mit Schutzmechanismen" hat

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

