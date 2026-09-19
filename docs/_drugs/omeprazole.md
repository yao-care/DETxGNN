---
layout: default
title: Omeprazole
parent: Nur Modellvorhersage (L5)
nav_order: 281
evidence_level: L5
indication_count: 2
---

# Omeprazole
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

# Omeprazol: Von Säurestörungen zur duodenogastralen Reflux

## Zusammenfassung in einem Satz

> Omeprazol ist ein Protonenpumpenhemmer (PPI), der für säurebezogene gastrointestinale Erkrankungen wie Ulkuskrankheit, GERD und *H. pylori*-Eradikation etabliert ist.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **Duodenogastrale Reflux** ist,
> wobei aktuell **1 klinische Studie** und **20 Publikationen** bezüglich dieser Richtung identifiziert wurden — die Evidenz ist jedoch gemischt, mit einigen Studien, die auch ein Sicherheitssignal zur Karzinogenese aufwerfen (siehe unten).

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht dokumentiert in deutschen Zulassungsdaten (Arzneimittel nicht in Deutschland vermarktet). Gemäß etablierter PPI-Pharmakologie und unterstützender Literatur in diesem Paket (z. B. PMID 18679668) wird Omeprazol für Ulkuskrankheit, *H. pylori*-Infektion, GERD, NSAID-induzierte GI-Läsionen und Zollinger-Ellison-Syndrom verwendet |
| Vorhergesagte neue Indikation | Duodenogastrale Reflux |
| TxGNN-Vorhersage-Score | 99.64% |
| Evidenzebene | L3 (beobachtende/klinische Studien, keine abgeschlossenen RCTs spezifisch für diese Indikation) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückgestellt |

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (DrugBank MOA-Feld ist eine Datenlücke). Basierend auf bekannter Pharmakologie ist Omeprazol ein Protonenpumpenhemmer, der die H+/K+-ATPase in gastrischen Parietalzellen irreversibel blockiert und die Säuresekretion unterdrückt — ein Mechanismus, der sich über Ulkuskrankheit, GERD und *H. pylori*-bezogene Erkrankungen hinweg bewährt hat.

Duodenogastrale Reflux (DGR) beinhaltet einen retrograden Fluss duodenaler Inhalte (Galle, Pankreasenzyme) in den Magen, oft koexistent mit säurebezogenen GI-Störungen und beitragend zu Mukosaläsionen bei Erkrankungen wie Barrett-Ösophagus. Mehrere klinische Studien in diesem Evidenzpaket (z. B. PMID 9824338, 10994616, 19491829) untersuchten direkt die Wirkung von Omeprazol auf DGR/DGOR in Reflux-Populationen und bieten eine plausible mechanistische Brücke von der ursprünglichen Säuresuppressions-Indikation zu diesem neuen Ziel.

Das mechanistische Bild ist jedoch nicht durchweg günstig: Mehrere Tierstudien (PMID 10389684, 8943968, 33027361, 15052437) berichten, dass die Blockade der Magensäure mit Omeprazol (und anderen PPIs) die Mukosawachstumsstimulierung und Magenkarzinogenese potenzieren kann, wenn sie mit DGR kombiniert wird, da ein höherer intragastraler pH die Gallenzytotoxizität erhöhen kann. Diese Nuance sollte sorgfältig abgewogen werden, anstatt sie als ein unkompliziertes „Wirksamkeits"-Signal zu behandeln.

## Evidenz aus klinischen Studien

| Trial-Nummer | Phase | Status | Einschreibungen | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | NA | Abgeschlossen | 157 | Untersuchte endoskopische Tri-Modal-Bildgebung (NBI/AFI/WLI) zur Unterscheidung von funktioneller Dyspepsie von Säure-/Gallenreflux-Erkrankung; keine Behandlungs-Wirksamkeitsstudie für Omeprazol selbst |

## Literaturbeweise

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Klinische Studie | Gut | Auswirkung von Omeprazol 20 mg 2×täglich auf duodenogastrale und duodenogastro-ösophageale Gallenreflux bei Barrett-Ösophagus |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Klinische Studie | Scand J Gastroenterol | Auswirkung von Omeprazol auf antrale duodenogastrale Reflux bei Barrett-Ösophagus |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Klinische Studie | Am J Gastroenterol | Vergleich des Ausmaßes von DGER/Säurereflux zwischen PPI-Respondern und Nicht-Respondern |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Klinische (prospektiv) | J Pediatr Gastroenterol Nutr | Prospektive Studie von Omeprazol für ösophageale Gallenreflux bei Kindern |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Fallserie | Eur J Pediatr | Beschreibung der primären duodenogastralen Reflux bei Kindern/Jugendlichen |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Übersichtsarbeit | Eur J Clin Pharmacol | Übersicht über klinische PPI-Verwendung und Pharmakokinetik (kontextualisiert ursprüngliche Indikationen) |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Präklinisch (Ratte) | Acta Cir Bras | Untersuchung, ob Omeprazol schützend gegen Magenkarzinom unter induzierter DGR wirkt |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Präklinisch (Ratte) | Dig Dis Sci | ⚠️ Blockade der Magensäure mit Omeprazol potenzierte durch DGR induzierte Magenkarzinogenese |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Präklinisch (Ratte) | Dig Dis Sci | ⚠️ Durch DGR induzierte Vorderdarm-Mukosawachstumsstimulierung potenziert durch Blockade der Magensäure (Omeprazol-Arm) |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Präklinisch (Ratte) | Gastric Cancer | ⚠️ Verwandter PPI (Lansoprazol) förderte Magenkarzinogenese bei Ratten mit DGR — Vorsicht vor Klassenwirkung |

## Marktinformation für Deutschland

Omeprazol verfügt derzeit über keine Zulassungseinträge in dem bereitgestellten deutschen Zulassungsdatensatz (0 Lizenzen, Marktstatus: Nicht vermarktet).

## Sicherheitsüberlegungen

> Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

**Wichtiger Vorbehalt:** Das Evidenzpaket kennzeichnet eine **Blockierend**-Datenlücke (DG001) — TFDA/behördliche Etikettwarnungen und Kontraindikationen wurden noch nicht abgerufen — die per Definition diese Kandidatin daran hindert, in das obligatorische S1-Sicherheits-Screening einzutreten. Darüber hinaus gab die DrugBank-DDI-Abfrage keine Ergebnisse zurück (`query_status: not_found`), daher konnten zu diesem Zeitpunkt keine Wechselwirkungsdaten ausgewertet werden.

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückgestellt**

**Begründung:**
Während der duodenogastrale Reflux plausible mechanistische Rationale und moderate (L3) beobachtende klinische Evidenz zeigt, hindert eine Datenlücke von **Blockierend**-Schweregrad bei behördlichen Sicherheitsetiketten (Warnungen/Kontraindikationen) die Vervollständigung des obligatorischen S1-Sicherheits-Screenings. Dies wird durch ein bemerkenswertes Sicherheitssignal in der präklinischen Literatur verstärkt, das nahelegt, dass Säuresuppression die Magenkarzinogenese in Gegenwart chronischer DGR potenzieren kann — ein Risiko, das vor dem Fortschreiten gelöst werden muss.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA (oder gleichwertiges) Produktetikett für Warnungen/Kontraindikationen abrufen (DG001, Blockierend)
- DrugBank MOA-Daten abrufen zur Unterstützung der formalen mechanistischen Link-Bewertung (DG002, Hoch)
- Vollständige DDI-Datenbankabfrage durchführen (aktueller Status: nicht gefunden)
- Formal die widersprüchliche Evidenzbasis abstimmen — klinische Studien, die symptomatischen Nutzen nahelegen, versus Tierstudien, die ein langfristiges Karzinogenese-Risiko unter chronischer Säuresuppression mit DGR nahelegen
- Anmerkung: die sekundäre vorhergesagte Indikation (Duodenale Obstruktion, Rang 2) wurde bereits intern als L4/S0/**Zurückgestellt** in diesem Evidenzpaket bewertet, konsistent mit der insgesamt konservativen Empfehlung für diesen Kandidaten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

