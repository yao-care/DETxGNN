---
layout: default
title: Posaconazole
parent: Mittlere Evidenz (L3-L4)
nav_order: 313
evidence_level: L4
indication_count: 1
---

# Posaconazole
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **1** 
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

# POSACONAZOL: Von der antimykotischen Prophylaxe zur Pneumocystose

## Zusammenfassung in einem Satz

Posaconazol ist ein Triazol-Antimykotikum, dessen etablierte Anwendung die Prophylaxe von invasiven Pilzerkrankungen ist (gemäß Literaturbelegen in diesem Datenpaket; im Quelldatenmaterial wurde kein formeller Indikationstext bereitgestellt). Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam bei **Pneumocystose** ist, aber dies wird derzeit nur durch indirekte Hintergundinformationen gestützt — **2 klinische Studien** (von denen keine Posaconazol direkt gegen Pneumocystose testet) und **5 Publikationen** (hauptsächlich Übersichtsartikel/Richtlinien, keine dedizierte RCT).

## Kurzübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Im Evidenzpaket nicht angegeben (drug-level `original_indications` ist leer); Literaturbelege beschreiben Posaconazol als „Schimmel-wirksames" Mittel für antimykotische Prophylaxe bei Hochrisiko-hämatoonkologischen Patienten |
| Vorhergesagte neue Indikation | Pneumocystose |
| TxGNN-Vorhersage-Score | 99.77% |
| Evidenzstufe | L4 |
| Marststatus Deutschland | Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückgestellt |

## Warum ist diese Vorhersage nachvollziehbar?

Formale Wirkmechanismus-Daten (`original_moa`) werden in diesem Evidenzpaket als Datenlücke aufgeführt. Das bereitgestellte Feld zur Repurposing-Rationale beschreibt jedoch Posaconazols Wirkmechanismus: Es hemmt das fungale CYP51 (14α-Demethylase) und blockiert die Ergosterolsynthese — der klassische Wirkmechanismus für breitzuständige Triazol-Antimykotika.

Die vorgeschlagene Verbindung zur Pneumocystose ist mechanistisch schwach. *Pneumocystis jirovecii* ist taxonomisch ein Pilz, aber seine Zellmembran basiert auf Cholesterin statt Ergosterol, was bedeutet, dass der Azol-Ergosterol-Weg, der der Aktivität von Posaconazol zugrunde liegt, nicht unmittelbar anwendbar ist. Die verfügbare Literatur erwähnt Posaconazol nur im breiteren Kontext des Managements invasiver Pilzerkrankungen (einschließlich *Pneumocystis*-Pneumonie als eine von mehreren in Übersichtsartikeln erörterten Pilzerkrankungen) und als mögliche Alternative bei Patienten, die TMP-SMX nicht vertragen — dies ist eine indirekte Schlussfolgerung, keine mechanistisch oder klinisch validierte Aussage.

Angesichts der atypischen Zielbiologie und des Fehlens von Studien, die Posaconazol direkt gegen Pneumocystose testen, sollte diese Vorhersage eher als Forschungshypothese als als klinisch verwertbares Signal in dieser Phase behandelt werden.

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Enrollment | Wesentliche Ergebnisse |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Abgeschlossen | 602 | Testet **Rezafungin** (ein Echinocandin, nicht Posaconazol) vs. Standardantimikrobielles Schema zur Prävention invasiver Pilzerkrankung bei allogenen KMT-Patienten; kein Fokus auf Pneumocystose und keine Posaconazol-Studie — nur Hintergrundrelevanz (Grad C). |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Rekrutierung läuft | 358 | Plattformstudie, die GVHD-Prophylaxe-Regimen bei nicht übereinstimmenden Unverwandten-Spender-Transplantatempfängern vergleicht; kann Antimykotika-Prophylaxe-Arme einschließen (möglicherweise Posaconazol), aber primäre Endpunkte sind GVHD-bezogen, nicht Pneumocystose-Wirksamkeit/Sicherheit (Grad C). |

Keine Studie liefert direkte Wirksamkeits- oder Sicherheitsevidenz für Posaconazol bei Pneumocystose.

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Wesentliche Ergebnisse |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Übersichtsartikel/Richtlinie | The Lancet. Infectious Diseases | UK-Update zu Best-Practice der Diagnostik schwerwiegender Pilzerkrankungen; allgemeine Diagnose-Landschaft, keine Posaconazol-spezifischen Therapiedaten. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Übersichtsartikel | Swiss Medical Weekly | Übersicht über Candidiasis, Aspergilllose, Kryptokokkose und *Pneumocystis*-Pneumonie; vermerkt, dass Schimmel-wirksame Posaconazol-Prophylaxe invasive Candidiasis bei Hochrisiko-hämatoonkologischen Patienten reduzierte — der nächstliegende Evidenzverbindung in diesem Paket, aber immer noch ein allgemeiner Übersichtsartikel, keine Pneumocystose-spezifischen Studiendaten. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Übersichtsartikel/Richtlinie | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 Chinese Clinical Practice Guideline für Diagnose/Management invasiver pulmonaler Pilzerkrankung; allgemeiner Richtlinienkontext. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | PK/PD-Studie | Clinical Pharmacokinetics | Überprüft die Penetration antimykotischer/antituberkulöser Wirkstoffe in die pulmonale Epithelflüssigkeit; nur pharmakokinetischer Hintergrund, keine Wirksamkeitsdaten für Pneumocystose. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Kohortenstudie | Transplant Infectious Disease | Retrospektive Kohorte infektiöser Komplikationen bei akutem GVHD nach Lebertransplantation; beschreibt Antimikrobielle-Management-Muster, keine Posaconazol-Pneumocystose-Wirksamkeitsstudie. |

Keine RCT oder dedizierte klinische Studie evaluiert direkt Posaconazol für Pneumocystose-Behandlung oder -Prophylaxe.

## Marktinformationen für Deutschland

Posaconazol hat derzeit **keine Marktgenehmigung** in diesem Evidenzpaket (`market_status`: Not marketed / Nicht zugelassen; `total_licenses`: 0; `licenses`: keine angegeben). Es kann keine Zulassungstabelle erstellt werden.

## Sicherheitsaspekte

Bitte verweisen Sie auf die Packungsbeilage für Sicherheitsinformationen. Wesentliche Warnungen, Kontraindikationen und Arzneimittel-Wechselwirkungs-Daten werden alle in diesem Evidenzpaket als Datenlücken aufgeführt (DDI-Abfragestatus: nicht gefunden) und können derzeit nicht zusammengefasst werden.

## Fazit und nächste Schritte

**Entscheidung: Zurückgestellt**

**Rationale:**
Der mechanistische Zusammenhang zwischen Posaconazol und Pneumocystose ist biologisch schwach (atypisch, Zielzellmembran nicht auf Ergosterol-Basis) und wird durch keine direkte klinische Studie unterstützt; alle identifizierten Studien und Literaturstellen sind indirekte Hintergundinformationen (Evidenzstufe L4, Entscheidungsstufe S1 — „Forschungsfrage"). Darüber hinaus sind Sicherheitsdaten (TFDA/lokale Warnungen und Kontraindikationen) eine **blockierende** Datenlücke (DG001), die an sich die Weiterentwicklung zu einer formalen Sicherheitsevaluierung verhindert (S1).

**Um fortzufahren, wird Folgendes benötigt:**
- Behebung von DG001 (Blockierend): Beschaffung offizielle Produktkennzeichnungs-Warnungen/Kontraindikationen, bevor eine S1-Sicherheitsevaluierung begonnen werden kann
- Behebung von DG002 (Hochpriorisiert): Bestätigung formaler Wirkmechanismus-Daten über DrugBank API, um mechanistische Plausibilität richtig zu bewerten
- Identifizierung oder Durchführung einer Studie, die Posaconazol direkt bei Pneumocystose testet (Wirksamkeit und Sicherheit), da derzeit keine solche Studie existiert
- Klarstellung der pharmakologischen Rationale angesichts der atypischen (Cholesterin-basierten) Membranbiologie von *Pneumocystis jirovecii* im Vergleich zum Ergosterol-Targeting-Mechanismus von Posaconazol

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

