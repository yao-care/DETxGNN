---
layout: default
title: Risankizumab
parent: Nur Modellvorhersage (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# RISANKIZUMAB: Evidenzpaket unvollständig — Bewertung ausstehend

## Zusammenfassung in einem Satz

Risankizumab ist ein humanisierter monoklonaler Antikörper, der auf den IL-23-Weg abzielt, mit etablierter Anwendung bei immunvermittelten Entzündungserkrankungen wie Plaque-Psoriasis und entzündlicher Darmerkrankung. Dieses Evidenzpaket (v4, Datenschnitt 2026-04-20) enthält jedoch **keine TxGNN-vorhergesagten Indikationen**, **keine Wirkmechanismus-Daten** und **keine Sicherheitsprofil-Daten** — der Bericht kann in seinem aktuellen Zustand nicht zu einer vollständigen Bewertung zur Neuindikation fortschreiten. Drei kritische Datenlücken wurden identifiziert, von denen zwei als **Blockierend** oder **Hoher Schweregrad** bewertet sind und die Standardbewertung sowie Entscheidungsfindung verhindern.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Im aktuellen Evidenzpaket nicht verfügbar |
| Vorhergesagte neue Indikation | Keine Vorhersagen generiert — siehe Abschnitt Datenlücke |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzebene | L5 (Nur Modellvorhersage — noch nicht verfügbar) |
| Taiwan-Marktstatus | ✗ Nicht vermarktet (0 Zulassungen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aufschub** — unzureichende Daten zur Bewertung |

---

## Warum dieser Bericht nicht zu einer vollständigen Bewertung fortschreiten kann

Das Evidenzpaket für RISANKIZUMAB vermisst derzeit die zwei grundlegenden Eingaben, die für einen Bericht zur Bewertung einer Neuindikation erforderlich sind:

**1. TxGNN-vorhergesagte Indikationen (leer)**
Das Array `predicted_indications` ist leer. Ohne eine vorhergesagte Zielindikation ist es nicht möglich, relevante klinische Studien, Literaturquellen oder einen pharmakologischen Ansatz zur Bewertung zu identifizieren. Dies kann darauf hindeuten, dass die TxGNN-Pipeline für diesen Kandidaten noch nicht ausgeführt wurde, oder dass Vorhersagen in früheren Schritten herausgefiltert wurden.

**2. Wirkmechanismus (Datenlücke DG002 — Hoher Schweregrad)**
Das Feld `original_moa` wird als Datenlücke gekennzeichnet. Der Wirkmechanismus ist erforderlich, um zu beurteilen, ob sich der pharmakologische Wirkmechanismus des Arzneimittels plausibel auf eine neue Indikation übertragen lässt. Abhilfe: DrugBank-API für DB14762 abfragen.

**3. Sicherheitswarnungen und Kontraindikationen (Datenlücke DG001 — Blockierender Schweregrad)**
Sowohl `key_warnings` als auch `contraindications` enthalten nur `[Datenlücke]`. Dies wird mit dem Schweregrad **Blockierend** klassifiziert — die Bewertung kann die S1-Sicherheitsprüfung nicht ohne diese Informationen bestehen. Abhilfe: PDF der TFDA-Gebrauchsinformation herunterladen und analysieren.

---

## Taiwan-Marktinformationen

Für RISANKIZUMAB wurden in der TFDA-Datenbank (Taiwan) zum 2026-04-20 keine Zulassungen gefunden. Keine Produkteinträge vorhanden.

> **Hinweis zum Kontext:** Risankizumab (Handelsname Skyrizi®, AbbVie) ist in mehreren großen Märkten (FDA, EMA, PMDA) für Plaque-Psoriasis, Psoriasis-Arthritis, Morbus Crohn und Colitis ulcerosa zugelassen, diese Informationen werden jedoch nicht im aktuellen Evidenzpaket widergespiegelt und können daher nicht als Grundlage für eine formale Bewertung unter dieser Pipeline verwendet werden.

---

## Sicherheitsaspekte

Alle Sicherheitsfelder im aktuellen Evidenzpaket werden als Datenlücken gekennzeichnet. Bitte konsultieren Sie die offizielle Gebrauchsinformation und die TFDA-Arzneimittelinformationsdatenbank zu Warnungen, Kontraindikationen und Arzneimittelwechselwirkungen, bevor Sie fortfahren.

---

## Fazit und nächste Schritte

**Entscheidung: Aufschub**

**Begründung:**
Das Evidenzpaket für RISANKIZUMAB (DB14762) ist strukturell unvollständig — sowohl die TxGNN-Vorhersageergebnisse als auch die grundlegenden Sicherheits- und Wirkmechanismus-Daten fehlen, weshalb derzeit keine sinnvolle Bewertung zur Neuindikation oder Evidence-Scoring möglich ist.

**Zum Fortfahren wird folgendes benötigt:**

- [ ] **TxGNN-Pipeline erneut ausführen** für DB14762, um vorhergesagte Indikationen mit Scores zu generieren; überprüfen Sie, dass die Vorhersageausgabe nicht stillschweigend gefiltert wurde
- [ ] **DG002 auflösen (Blockierend):** PDF der TFDA-Gebrauchsinformation herunterladen und analysieren, um Sicherheitswarnungen und Kontraindikationen zu extrahieren — erforderlich zum Bestehen der S1-Sicherheitsprüfung
- [ ] **DG001 auflösen (Hoher Schweregrad):** DrugBank-API für `DB14762` abfragen, um den Wirkmechanismus (p19/IL-23-Untereinheit-Hemmung) und pharmakologische Kategorien abzurufen
- [ ] **Pipeline-Eingaben überprüfen:** Das Feld `meta.inputs_received` enthält nur `"drugbank"` — überprüfen Sie, ob die TFDA-, klinische Studien- (ClinicalTrials.gov) und Literaturquellen (PubMed) abgefragt wurden und leer zurückgegeben wurden, oder überhaupt nicht aufgerufen wurden
- [ ] **Evidenzpaket neu einreichen**, sobald die obigen Punkte geklärt sind; dieser Bericht sollte ab Version 5 oder später neu generiert werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

