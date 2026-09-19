---
layout: default
title: Bempedoic Acid
parent: Nur Modellvorhersage (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic acid: Von der LDL-Cholesterin-Senkung zur homozygoten familiären Hypercholesterinämie

## Zusammenfassung in einem Satz

> Bempedoic acid ist ein ATP-Citrat-Lyase-Inhibitor (ACL), der zur Senkung des LDL-Cholesterins bei Patienten mit Hypercholesterinämie und erhöhtem kardiovaskulärem Risiko eingesetzt wird.
> Bei den Top-10-Vorhersagen des TxGNN-Modells weisen die meisten (Hyperthyreose, veterinärmedizinische Infektionen, onkogene Syndrome usw.) **keine plausible mechanistische Verbindung** auf und werden als wahrscheinliches Wissensdiagramm-Rauschen annotiert.
> Die einzige Vorhersage mit echtem biologischen Grund und realen Evidenzen ist **Homozygote familiäre Hypercholesterinämie (HoFH)**, unterstützt durch **1 Real-World-Kohortenstudie** und **17 weitere Publikationen**, obwohl **derzeit keine klinischen Studien** für diese spezifische Population registriert sind.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in strukturierten Daten erfasst (`original_indications` leer). Basierend auf mechanistischen Evidenzen in diesem Paket wird Bempedoic acid zur LDL-C-Senkung / primären Hypercholesterinämie eingesetzt |
| Vorhergesagte neue Indikation | Homozygote familiäre Hypercholesterinämie (HoFH) |
| TxGNN-Vorhersage-Score | 99.48% (Rang 6040 im Krankheitsspektrum) |
| Evidenzgrad | L3 (Real-World-Kohorte + Review-Literatur, keine RCTs) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Fortfahren mit Schutzmaßnahmen |

**Anmerkung zur Rangliste:** Die höchstbewertete TxGNN-Vorhersage (#1, Hyperthyreose, Score 99.61%) und die meisten anderen Top-10-Vorhersagen wurden aus diesem Bericht ausgeschlossen – das Evidenzpaket selbst kennzeichnet sie als keine „plausiblen Mechanismen" aufweisend oder nicht zu nicht verwandten Arzneimitteln (z. B. Tiratricol) oder veterinärmedizinischen Krankheiten passsend. Dieser Bericht konzentriert sich auf Rang 6 (HoFH), den einzigen Kandidaten mit kohärentem Mechanismus und unterstützender Literatur.

---

## Warum ist diese Vorhersage sinnvoll?

Aktuell ist im Evidenzpaket kein strukturierter Datensatz zum Wirkmechanismus (MOA) für Bempedoic acid verfügbar (`original_moa: [Datenlücke]`). Die mit der HoFH-Vorhersage verbundene Rationale zur Arzneistoffumpositionierung bietet jedoch ausreichend mechanistische Details zur Bewertung der Plausibilität.

Bempedoic acid ist ein ATP-Citrat-Lyase-Inhibitor (ACL), der upstream von HMG-CoA-Reduktase im Cholesterin-Biosynthesepfad wirkt. Es ist ein Prodrug, das selektiv in der Leber aktiviert wird (über VLACS1, ein Enzym, das nicht in Skelettmuskulatur exprimiert wird), was sein günstiges Nebenwirkungsprofil bezüglich muskulärer Probleme im Vergleich zu Statinen erklärt. Diese leberselektive Inhibition führt zu einer Upregulation der LDL-Rezeptor-Expression (LDLR), wodurch das zirkulierende LDL-Cholesterin gesenkt wird.

HoFH-Patienten tragen in der Regel zusammengesetzte heterozygote oder homozygote *LDLR*-Mutationen, die die Rezeptorfunktion reduzieren – aber nicht immer vollständig aufheben. Da der Wirkmechanismus von Bempedoic acid von residueller LDLR-Aktivität abhängt, können Patienten mit Non-Null-*LDLR*-Genotypen eine teilweise pharmakologische Antwort bewahren. Dies macht Bempedoic acid mechanistisch plausibel als **Add-On-Therapie** für HoFH-Patienten, die trotz Statinen und PCSK9-Inhibitoren über den LDL-C-Zielwerten bleiben, anstatt als Monotherapie oder First-Line-Behandlung.

---

## Klinische Studienbelege

Aktuell sind keine verwandten klinischen Studien registriert.

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|-------------|----------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-World-Kohorte | J Clin Lipidol | Direkte Real-World-Bewertung der Wirksamkeit und Verträglichkeit von Bempedoic acid speziell bei HoFH-Patienten |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Expertenkonsens | J Clin Lipidol | National Lipid Association-Update zur FH-Behandlung, das aktuelle LDL-C-Senkungsstrategien einschließlich Bempedoic acid widerspiegelt |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Übersichtsarbeit | J Atheroscler Thromb | Übersicht über Behandlungsfortschritte bei HoFH, Positionierung von Bempedoic acid unter Add-On-LDL-C-Senkungsoptionen |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Übersichtsarbeit | Exp Mol Pathol | Innovative Therapien für HoFH-Management, Abdeckung von LDLR-gezielten und adjuvanten Pharmakotherapien |
| [41694628](https://pubmed.ncbi.nlm.nih.gov/41694628/) | 2026 | Fallbericht + Übersichtsarbeit | Clin Case Rep | Fall von katastrophaler HoFH-Progression nach unterbrochener Nachverfolgung; unterstreicht Notwendigkeit kontinuierlicher aggressiver LDL-C-Kontrolle |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Präklinisch | Arterioscler Thromb Vasc Biol | Bempedoic acid senkt LDL-C und mildert Atherosklerose in LDLR-defizienten (LDLR+/- und LDLR-/-) Miniaturschwein-Modellen, direkt relevant für HoFH-Pathophysiologie |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Übersichtsarbeit (Vergleichsmedikament) | Cardiol Rev | Erörtert Evinacumab zur HoFH-Behandlung, verweist auf Bempedoic acid unter adjuvanten Lipidsenkungsmitteln |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Übersichtsarbeit | J Am Coll Cardiol | JACC-Seminar zu aufstrebenden LDL-C/ApoB-Senkungstherapien, erörtert Wirkmechanismus und klinische Rolle von Bempedoic acid |
| [35754818](https://pubmed.ncbi.nlm.nih.gov/35754818/) | 2022 | Übersichtsarbeit | Front Genet | Übersicht über Behandlungsfortschritte bei therapieresistenter Hypercholesterinämie einschließlich HoFH |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Übersichtsarbeit | Curr Cardiol Rep | Übersicht über Managementaktualisierungen über Statine/PCSK9i hinaus für familiäre und therapieresistente Hypercholesterinämie |

---

## Marktinformationen Deutschland

Bempedoic acid ist aktuell nicht in Deutschland gemäß diesem Evidenzpaket vermarktet (`market_status: Not marketed`, `total_licenses: 0`); keine Zulassungsdatensätze sind verfügbar.

---

## Sicherheitsaspekte

Strukturierte Sicherheitsdaten für dieses Arzneimittel sind aktuell eine **blockierende Datenlücke** (`DG001`, Schweregrad: Blocking) – TFDA/behördliche Packungsbeilage-Warnungen und Kontraindikationen wurden noch nicht abgerufen, und DDI-Screening ergab keine Ergebnisse (`query_status: not_found`). Diese Lücke muss vor dem Fortschreiten des Kandidaten über die anfängliche Sicherheitsüberprüfung (S1) geschlossen werden.

> Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen, sobald verfügbar.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Fortfahren mit Schutzmaßnahmen** (speziell für die HoFH-Indikation; alle anderen TxGNN-Top-10-Vorhersagen für dieses Arzneimittel sind **Halt** aufgrund fehlender mechanistischer Rationale und fehlender unterstützender Evidenzen)

**Begründung:**
Der leberselektive, LDLR-abhängige Wirkmechanismus von Bempedoic acid ist biologisch mit HoFH als Zusatztherapie kompatibel, und dies wird durch eine Real-World-Kohortenstudie plus konsistente Review-Level-Literatur unterstützt – aber keine dedizierte randomisierte, kontrollierte Studie existiert in dieser Population, was die Evidenz auf L3 begrenzt.

**Zum Fortfahren ist folgendes erforderlich:**
- Blockierende Datenlücke DG001 lösen: TFDA/behördliche Packungsbeilage-Warnungen und Kontraindikationen erhalten, bevor eine Sicherheitsüberprüfung (S1) durchgeführt wird
- Arzneimittel-Wechselwirkungsdaten (DDI) erhalten (aktuelle Abfrage ergab keine Ergebnisse)
- Strukturierte Wirkmechanismus-Daten über DrugBank-API bestätigen (DG002)
- Prospektive oder kontrollierte Studiendaten in HoFH-Populationen suchen (aktuell existieren nur Real-World/Beobachtungsdaten)
- Da das Arzneimittel aktuell nicht in Deutschland vermarktet wird, Klarheit bezüglich regulatorischer Wege/Importstatus erhalten, bevor eine lokale Entwicklung angestrebt wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

