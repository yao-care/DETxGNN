---
layout: default
title: Tasimelteon
parent: Nur Modellvorhersage (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: Von zirkadianen Schlafstörungen zu Insomnie

## Zusammenfassung

Tasimelteon ist ein Melatoninrezeptor-Agonist, der ursprünglich zur Behandlung von zirkadianen Schlafrhythmusstörungen zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **Insomnie** wirksam sein könnte, wobei **1 klinische Phase-3-Studie** (laufend, Rekrutierung) und **6 Publikationen** (ausschließlich Übersichtsarbeiten) diese Richtung stützen.
Abgeschlossene Wirksamkeitsdaten liegen bislang nicht vor.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Schlafstörungen, zirkadiane Rhythmusstörungen |
| Vorhergesagte neue Indikation | Insomnie (Rang 2 der Vorhersagen; siehe Hinweis unten) |
| TxGNN-Vorhersagewert | 99,47 % |
| Evidenzgrad | L1 (vorläufig, da nur eine laufende Phase-3-Studie ohne Ergebnisse) |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails |

**Hinweis zur Auswahl:** Die Vorhersage mit dem höchsten Wert (Rang 1, bilaterale parasagittale parieto-okzipitale Polymikrogyrie, Score 99,48 %) hat keinerlei Studien- oder Literaturgrundlage und keinen erkennbaren mechanistischen Zusammenhang (Evidenzgrad L5, Hold). Dieser Bericht konzentriert sich daher auf die am besten belegte Vorhersage, Insomnie.

---

## Warum ist diese Vorhersage plausibel?

Zu diesem Wirkstoff liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben zum Wirkmechanismus vor. Nach der allgemeinen pharmakologischen Einordnung ist Tasimelteon ein Agonist der Melatoninrezeptoren MT1 und MT2 im Nucleus suprachiasmaticus, dem zentralen Taktgeber der zirkadianen Uhr. Über diese Rezeptoren werden der Tag-Nacht-Rhythmus synchronisiert sowie Einschlafen und Durchschlafen gefördert.

Die ursprüngliche Indikation (zirkadiane Schlafrhythmusstörungen) und Insomnie sind eng verwandt: Beide betreffen die Regulation von Schlaf und Wachheit. Melatonerge Wirkstoffe unterscheiden sich grundlegend von GABAergen Hypnotika, da sie vor allem das Einschlafen erleichtern und die innere Uhr in eine für durchgehenden Schlaf günstige Phase verschieben. Die Übersichtsarbeiten bestätigen diesen Mechanismus, liefern aber keine eigenen Wirksamkeitsdaten für Tasimelteon bei Insomnie.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Rekrutierung | 420 | Multizentrische, doppelblinde, randomisierte Studie zu Tasimelteon vs. Placebo bei pädiatrischer Insomnie; Start 04/2025, geplanter Abschluss 01/2028; noch keine Ergebnisse |

---

## Literaturevidenz

| PMID | Jahr | Typ | Fachzeitschrift | Kernaussagen |
|------|-----|------|------|---------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | Int J Mol Sci | Wirksamkeit und Sicherheit melatonerger Agonisten (u. a. Tasimelteon) bei Schlafstörungen und Begleiterkrankungen |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatr Dis Treat | Vergleich von retardiertem Melatonin und synthetischen melatonergen Agonisten bei Insomnie |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | J Med Chem | MT1/MT2-Rezeptoren, Liganden und therapeutisches Potenzial; Tasimelteon als fortgeschrittener Kandidat |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Curr Drug Saf | Rolle von Melatonin und Tasimelteon bei der Alzheimer-Krankheit (u. a. Insomnie als Symptom) |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Ther Adv Neurol Disord | Melatonin und Analoga bei Parkinson: Fokus auf Schlaf und Neuroprotektion |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinol Lett | Gestörte Chronobiologie des Schlafs bei Adipositas und möglicher Nutzen von Melatonin |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003870 | Hetlioz | – | Schlafstörungen, zirkadiane Rhythmusstörungen (Status: erloschen) |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 99 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind u. a. **Morphin** und **liposomales Morphin**. Als **moderat** eingestuft sind u. a. Aprepitant, Omeprazol, Dexamethason, Cimetidin, Clarithromycin, Difenoxin, Diphenoxylat, Dronabinol, Obeticholsäure, Nabilon, Metoclopramid, Metreleptin, Miconazol, Clotrimazol, Opium, Sibutramin, Troglitazon und Ethanol.

Für Warnhinweise und Gegenanzeigen liegen in den zusammengestellten Daten keine Angaben vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Der Wirkmechanismus (MT1/MT2-Agonismus) passt direkt zu Insomnie, und eine randomisierte Phase-3-Studie (n = 420) prüft die Indikation gezielt. Da diese Studie noch rekrutiert und keine Ergebnisse vorliegen, ist der Evidenzgrad L1 nur vorläufig. Zudem ist die einzige deutsche/EU-Zulassung erloschen.

**Für das weitere Vorgehen werden benötigt:**
- Ergebnisse der Phase-3-Studie NCT06953869 (voraussichtlich ab 2028); die Studie betrifft zudem Kinder, die Übertragbarkeit auf Erwachsene ist zu klären
- Klärung der Studienpopulation (der Studientitel ist in den Daten möglicherweise abgeschnitten)
- Fachinformation mit Warnhinweisen und Gegenanzeigen (Sicherheitsprüfung derzeit nicht abschließbar)
- Detaillierte Wirkmechanismus-Daten, z. B. aus DrugBank
- Klärung der Gründe für das Erlöschen der Zulassung und der aktuellen Verfügbarkeit in Deutschland
- Bewertung der Wechselwirkung mit Morphin (schwerwiegend) für ein Risikomanagement
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

