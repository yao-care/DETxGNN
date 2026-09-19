---
layout: default
title: Fenofibrate
parent: Nur Modellvorhersage (L5)
nav_order: 165
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Fenofibrat: Von Dyslipidämie zu homozygoter familiärer Hypercholesterinämie

## Zusammenfassung in einem Satz

Fenofibrat ist ein Fibrat-Wirkstoff aus der Klasse der Lipidsenker, dessen etablierte Verwendung gemäß der Literatur in diesem Evidence-Paket Dyslipidämie und Mischtyp-Dyslipidämie ist (einschließlich Reduktion der Nüchtern-Triglyceride zur Pankreatitis-Prävention). Das TxGNN-Modell sagt voraus, dass es auch bei **Homozygoter familiärer Hypercholesterinämie (HoFH)** wirksam sein könnte, mit **1 registrierter klinischer Studie** und **11 Veröffentlichungen**, die derzeit mit dieser Indikation assoziiert sind — obwohl nur ein Teilbereich dieser Literatur Fenofibrat direkt bei HoFH-Patienten untersucht.

---

## Schnelübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Dyslipidämie / Mischtyp-Dyslipidämie (gemäß Literaturbelegen, z.B. PMID 37979722: Fenofibrat-Monotherapie indiziert für Nüchtern-TG >500 mg/dL) |
| Vorhergesagte neue Indikation | Homozygoter familiärer Hypercholesterinämie (HoFH) |
| TxGNN-Vorhersage-Score | 99.91% |
| Evidenzebene | L2 (1 abgeschlossene Phase-3-RCT, die unter dieser Indikation registriert ist — siehe Anmerkung unten) |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

> **Anmerkung zur Evidenzebene**: Die einzige abgeschlossene Phase-3-Studie (NCT03510715) evaluiert **Alirocumab**, nicht Fenofibrat, bei HoFH. Sie wurde eingeschlossen, weil sie dem Krankheitsbegriff entspricht, nicht weil sie den Kandidaten-Wirkstoff testet. Fenofibrat-spezifische Evidenz für HoFH in diesem Evidence-Paket ist auf eine historische Fallserie begrenzt (PMID 6593751), die einen einzelnen HoFH-Patienten beschreibt.

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (DrugBank-MOA-Feld wurde als Datenlücke zurückgegeben). Basierend auf bekannten Informationen aus dem Evidence-Paket gehört Fenofibrat zur Fibrat-Klasse der Lipidsenker. Seine Wirksamkeit bei Dyslipidämie und Mischtyp-Dyslipidämie wurde über Jahrzehnte in der Literatur hinweg gezeigt, und mechanistisch könnte es auf genetische/familiäre Cholesterin-Störungen wie HoFH anwendbar sein.

HoFH und die anderen von TxGNN vorhergesagten Indikationen in diesem Paket (Hyperlipoproteinämie, familiäre Hypercholesterinämie, CETP-Mangel, CYP7A1-Mangel, Mangel an hepatischer Triglycerid-Lipase, autosomal-dominante Hypercholesterinämie) sind keine Abweichung von Fenofibrats bekannter Pharmakologie — sie sind alle genetische oder seltene Subtypen innerhalb der gleichen breiteren Dyslipidämie-Krankheitsfamilie, die der Wirkstoff bereits behandelt. Dies wird im Paket selbst widergespiegelt: mehrere ältere Studien (z.B. PMID 3924068, PMID 3829426, PMID 2918846) dokumentieren direkt die lipidsenkende Wirkung von Fenofibrat bei heterozygoten FH-Patienten, und eine Fallserie (PMID 6593751) umfasst einen HoFH-Patienten, der die größte LDL-C-Reduktion in der Kohorte zeigte.

Die Rationale ist daher weniger „neuartige Umwidmung" und mehr „TxGNN erkennt korrekt einen Wirkstoff, der bereits bei einem angrenzenden, spezifischeren Krankheitsphänotyp wirksam ist." Allerdings ist die spezifische prospektive Evidenz von Fenofibrat bei HoFH dünn — moderne HoFH-Studien in diesem Paket (Alirocumab) widerspiegeln den gegenwärtigen Paradigmenwechsel in der Standardtherapie hin zu PCSK9-Inhibitoren und MTP-Inhibitoren (z.B. Lomitapid, PMID 24734312), statt Fibrat-Monotherapie, was widerspiegelt, dass Fenofibrat heute eher eine Begleittherapie/Triglycerid-fokussierte Therapie darstellt als eine primäre HoFH-Behandlung.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmer | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Abgeschlossen | 18 | Evaluiert Alirocumab (nicht Fenofibrat) Q2W bei Kindern/Jugendlichen (8–17 Jahre) mit HoFH unter Hintergrund-Lipidsenker-Therapie; bewertet LDL-C-Reduktion in Woche 12, 24, 48. Einbezogen wegen Relevanz des Krankheitsbegriffs nur — testet Fenofibrat nicht direkt. |

---

## Literaturbelege

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Fallserie | Pharmacological Research Communications | 22 Patienten mit Typ-II-Hyperlipoproteinämie mit Fenofibrat 300mg/Tag behandelt; ein HoFH-Patient zeigte den größten Rückgang des Gesamt- und LDL-Cholesterins in der Kohorte. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK-Studie | Pharmacotherapy | Charakterisiert PK-Wechselwirkung zwischen Lomitapid (MTP-Inhibitor, zugelassen für HoFH) und häufig gleichzeitig verabreichten Lipidwirkstoffen einschließlich Fenofibrat. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Übersichtsarbeit | Indian Heart Journal | Besagt, dass die eindeutigste Monotherapie-Indikation von Fenofibrat Nüchtern-TG >500 mg/dL zur Pankreatitis-Prävention ist; positioniert Fibrate unter den nicht-Statin-Optionen. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Übersichtsarbeit | Annals of the NY Academy of Sciences | Überprüft pharmakologische Behandlungen dyslipidämischer Kinder mit FH, einschließlich Fenofibrat unter erfolgreichen Regimen. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Fallbericht/Übersichtsarbeit | Internal Medicine Journal | Diskutiert Lebertransplantation für HoFH im Kontext neuer Lipidsenker-Therapien; nicht Fenofibrat-spezifisch. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Leitlinie | Endocrine Practice | AACE/ACE-Dyslipidämie-Managementleitlinien, allgemeiner Rahmen für Fibrat-Klasse-Wirkstoffe. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Übersichtsarbeit | Current Atherosclerosis Reports | Überprüft Dyslipidämie-Management in der Schwangerschaft; tangential zu HoFH. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Übersichtsarbeit | Indian Heart Journal | Übersicht der LDL-C-Reduktionsstrategien (Statine, PCSK9i); allgemeiner Kontext, nicht Fenofibrat-fokussiert. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Übersichtsarbeit | Pharmacotherapy | Überprüft Ezetimib als Cholesterin-Absorptions-Inhibitor; allgemeiner Dyslipidämie-Kontext, nicht Fenofibrat-spezifisch. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Übersichtsarbeit | Drugs | Überprüft Atorvastatin-Pharmakologie und therapeutisches Potenzial bei Hyperlipidämie; allgemeiner Vergleicher-Kontext. |

---

## Marktinformationen Deutschland

Fenofibrat hält derzeit **keine Marktzulassungen** im deutschen Datensatz, der für dieses Evidence-Paket verwendet wurde (`market_status: Not marketed`, `total_licenses: 0`). Keine Zulassungsrecords auf Produktebene sind verfügbar zum Zusammenfassen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Keine wichtigen Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungs-Daten waren in diesem Evidence-Paket verfügbar (DG001: TFDA/BfArM-Kennzeichnungswarnungen und Kontraindikationen sind eine **blockierende** Datenlücke — derzeit nicht in der Lage, eine S1-Sicherheits-Vor-Bewertung abzuschließen).

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Rationale:**
Eine blockierende Datenlücke (fehlende regulatorische Kennzeichnungs-Sicherheits-/Kontraindikationsdaten) verhindert jede S1-Sicherheits-Vor-Bewertung, und der Wirkstoff hat derzeit null Marktzulassungen in Deutschland. Darüber hinaus testet die einzige Phase-3-Studie, die mit dieser Indikation assoziiert ist, einen anderen Wirkstoff (Alirocumab), nicht Fenofibrat — direkte Fenofibrat-spezifische Evidenz für HoFH ist auf eine einzige Fallserie von 1984 begrenzt.

**Um fortzufahren, ist folgendes erforderlich:**
- TFDA/BfArM-Kennzeichnungsdaten: Warnhinweise, Kontraindikationen und DDI-Profil (DG001 beheben, blockierend)
- DrugBank-MOA-Daten zur Unterstützung der mechanistischen Rationale (DG002 beheben)
- Klärung von Fenofibrats deutschem regulatorischem/Marktstatus, angesichts 0 aktueller Zulassungen
- Fenofibrat-spezifische klinische oder Beobachtungsstudien-Evidenz bei HoFH (aktuelle Standardtherapie hat sich zu PCSK9i/MTP-Inhibitoren verschoben), um diese von Studien zu unterscheiden, die zwar der Krankheit entsprechen, aber nicht den Kandidaten-Wirkstoff testen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

