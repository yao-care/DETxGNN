---
layout: default
title: Clomipramine
parent: Nur Modellvorhersage (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomipramine: vorhergesagte neue Indikation Angststörung (Evidenzstufe L5). Ursprüngliche Indikation: Zwangsstörung"
monitor_inn: "Clomipramine"
predicted_indications: ["anxiety disorder", "benign paroxysmal torticollis of infancy", "paranoid personality disorder", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "agoraphobia", "attention deficit-hyperactivity disorder"]
---

# Clomipramine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Clomipramin: Von Zwangsstörung zu Angststörung
{: .text-alpha }

## Zusammenfassung in einem Satz

Clomipramin ist ein trizyklisches Antidepressivum, das ursprünglich zur Behandlung der Zwangsstörung (OCD) eingesetzt wird. Das TxGNN-Modell sagt voraus, dass es bei **Angststörungen** wirksam sein könnte, wobei **8 klinische Studien** und **19 Publikationen** in den für diesen Bericht zusammengestellten Daten vorliegen. Die gefundenen Studien betreffen jedoch überwiegend die Zwangsstörung selbst und stützen die neue Indikation nur indirekt.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Zwangsstörung (Quelle: TxGNN-Wissensgraph; im deutschen Zulassungseintrag ist kein Indikationstext hinterlegt) |
| Vorhergesagte neue Indikation | Angststörung |
| TxGNN-Vorhersagewert | 99,93 % |
| Evidenzlevel | L1 (laut Bewertung in den Daten; die Studien zur Angststörung selbst sind überwiegend indirekt, siehe unten) |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails (mit Auflagen fortfahren) |

---

## Warum ist diese Vorhersage plausibel?

Clomipramin ist ein potenter Serotonin-Wiederaufnahmehemmer mit zusätzlicher noradrenerger Wirkung. Ein detaillierter Mechanismus aus der Arzneimitteldatenbank liegt nicht vor. Die pharmakologischen Daten zeigen jedoch Bindung an den Serotonin-Transporter (SERT), den Noradrenalin-Transporter (NET), den Dopamin-Transporter (DAT) sowie den α1A-Adrenozeptor. Die serotonerge Modulation limbischer und präfrontaler Schaltkreise gilt als plausible gemeinsame Grundlage für die Wirksamkeit bei Zwangsstörung und bei Störungen aus dem Panik- und Angstspektrum.

Zwangsstörung und Angststörungen sind klinisch und pathophysiologisch verwandt. Die Zwangsstörung wurde lange den Angststörungen zugeordnet. Zu beachten ist: Da die Zwangsstörung die ursprüngliche Indikation ist, belegen die meisten gefundenen Studien die Wirkung im Angstspektrum und nicht bei Angststörungen allgemein. Direkte Hinweise zu Panikstörung und Agoraphobie stammen vor allem aus Netzwerk-Metaanalysen und älteren Vergleichsstudien.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Abgeschlossen | 54 | Augmentationsstrategien bei OCD ohne Ansprechen: Fluoxetin allein vs. plus Quetiapin vs. plus Clomipramin |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | Noch nicht rekrutierend | 80 | Hydroxyzin vs. Standardbehandlung bei Panikstörung; nur indirekter Bezug |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Abgeschlossen | 26 | Vorhersage des Medikamentenansprechens bei OCD (Clomipramin vs. Escitalopram) |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Abgeschlossen | 124 | Kognitive Verhaltenstherapie plus SRI bei pädiatrischer OCD |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Unbekannt | 76 | Intravenöses vs. orales Clomipramin bei OCD |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Abgeschlossen | 44 | Quetiapin-Augmentation bei schwerer OCD (Clomipramin nicht Prüfsubstanz) |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Abgebrochen | 407 | Pharmakovigilanz bei gerontopsychiatrischen Patienten; nicht spezifisch für Angststörungen |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Abgeschlossen | 21 | Quetiapin- vs. Clomipramin-Augmentation von SSRI bei OCD |

Keine dieser Studien belegt direkt die Wirksamkeit von Clomipramin bei Angststörungen.

---

## Literaturevidenz

| PMID | Jahr | Typ | Fachzeitschrift | Kernaussagen |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Netzwerk-Metaanalyse | Cochrane Database Syst Rev | Pharmakologische Behandlungen der Panikstörung bei Erwachsenen |
| [40788541](https://pubmed.ncbi.nlm.nih.gov/40788541/) | 2026 | Netzwerk-Metaanalyse | Eur Arch Psychiatry Clin Neurosci | Vergleichende Wirksamkeit und Akzeptanz von Anxiolytika bei Angststörungen |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | Systematische Übersicht | Psychother Psychosom | Behandlungsoptionen bei therapieresistenten Angststörungen |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | Leitlinie | World J Biol Psychiatry | WFSBP-Leitlinien zu Angst-, Zwangs- und posttraumatischen Belastungsstörungen (Teil II) |
| [34582562](https://pubmed.ncbi.nlm.nih.gov/34582562/) | 2021 | Systematische Übersicht | Cochrane Database Syst Rev | Pharmakotherapie der Trichotillomanie |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Übersichtsarbeit | Drugs | Clomipramin: Pharmakologie und Einsatz bei Zwangs- und Panikstörung |
| [18849910](https://pubmed.ncbi.nlm.nih.gov/18849910/) | 2008 | Übersichtsarbeit | CNS Spectrums | Medikamentöse Behandlung von Zwangsstörung und Angst; Clomipramin wirksam, aber mit mehr Nebenwirkungen |
| [2021107](https://pubmed.ncbi.nlm.nih.gov/2021107/) | 1991 | Übersichtsarbeit | Am Fam Physician | Clomipramin bei Zwangsstörung |
| [3887336](https://pubmed.ncbi.nlm.nih.gov/3887336/) | 1985 | Übersichtsarbeit | Psychiatr Clin North Am | Zwangsstörung; Clomipramin als nützlich beschrieben |
| [11801290](https://pubmed.ncbi.nlm.nih.gov/11801290/) | 2001 | Übersichtsarbeit | Neurosci Biobehav Rev | Modellierung von Panikattacken (Tierexperimente mit Clomipramin) |

Hinweis: Für die Agoraphobie (Rang 7) liegen zusätzlich direkte Vergleichsstudien vor, z. B. Clomipramin vs. Diazepam (PMID 6373161) und Clomipramin als Referenzsubstanz bei Panik/Agoraphobie (PMID 22290995).

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/V/C/000039 | Clomicalm | nicht angegeben | nicht angegeben (Status: erloschen) |

Es besteht keine gültige Zulassung. Der einzige Eintrag ist erloschen.

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph** (keine Packungsbeilagen-Angaben): Epilepsie, manische bipolare Störung, Lebererkrankung, Gallenblasenerkrankung, Substanzmissbrauch/-abhängigkeit, maligne Hyperthermie, Phäochromozytom und Paragangliom, Krebserkrankungen (Zwölffingerdarm, Dünndarm, Herz, Nebenniere), Neuroblastom, Glaukom sowie Hyperthyreose (Morbus Basedow, Thyreotoxikose).
- **Pharmakologische Zielstrukturen** (kein klassischer Wechselwirkungsbefund): SERT, NET, DAT, α1A-Adrenozeptor sowie Kir3.2 und Kir3.4 (Maus). Die Daten enthalten keine klassifizierten Arzneimittelwechselwirkungen.
- **Aus der Literatur**: Pancytopenie (Einzelfallbericht), sexuelle Funktionsstörungen, gastrointestinale Effekte, anticholinerge Effekte, kardiale Effekte und Überdosierungstoxizität trizyklischer Antidepressiva sowie Tourette-ähnliche Tics (Einzelfallbericht).

Für verbindliche Angaben zu Warnhinweisen und Gegenanzeigen ist die Packungsbeilage heranzuziehen.

---

## Weitere vorhergesagte Indikationen (Kurzübersicht)

| Indikation | TxGNN-Wert | Evidenz | Empfehlung |
|------|------|------|------|
| Agoraphobie | 99,87 % | L3; Netzwerk-Metaanalyse, Vergleichsstudien, ältere Daten, keine registrierte Studie | Forschungsfrage |
| Majore Depression | 99,77 % | L1; große Netzwerk-Metaanalysen, weitgehend etablierte Anwendung | Proceed with Guardrails |
| Endogene Depression | 99,71 % | L1 (geerbt von MDD-Daten) | Proceed with Guardrails |
| ADHS | 99,58 % | L3; Cochrane-Review zu Trizyklika, nicht Clomipramin-spezifisch | Forschungsfrage |
| Paranoide, schizotypische, schizoide, histrionische Persönlichkeitsstörung; benigner paroxysmaler Torticollis des Säuglings | ca. 99,9 % | L4–L5; keine tragfähige klinische Evidenz | Hold |

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Für das Angstspektrum, insbesondere Panikstörung und Agoraphobia, liegen Netzwerk-Metaanalysen und Vergleichsstudien vor, die Clomipramin als wirksame Referenzsubstanz beschreiben. Die registrierten Studien betreffen jedoch fast ausschließlich die Zwangsstörung, und ein Großteil der klinischen Daten ist älter. Zudem besteht in Deutschland keine gültige Zulassung, und das Sicherheitsprofil der Trizyklika erfordert Vorsicht.

**Für das weitere Vorgehen wird benötigt:**
- Detaillierte Mechanismusdaten (MOA) aus der Arzneimitteldatenbank
- Packungsbeilage mit Warnhinweisen und Gegenanzeigen (derzeit nicht verfügbar; blockiert die Sicherheitsbewertung)
- Prüfung der Zulassungslage in Deutschland (aktuelle Humanarzneimittel mit Clomipramin; der gelistete Eintrag ist ein erloschenes Tierarzneimittel)
- Aktuelle, kontrollierte Studien direkt bei Panikstörung und Agoraphobie
- Sicherheitsüberwachungsplan (EKG, Blutbild, Leberwerte, anticholinerge Effekte) und Abgrenzung zu Erstlinientherapien
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

