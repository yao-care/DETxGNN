---
layout: default
title: Oritavancin
parent: Nur Modellvorhersage (L5)
nav_order: 331
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
description: "Oritavancin: vorhergesagte neue Indikation Bacteroidaceae-Infektionen (Evidenzstufe L5). Ursprüngliche Indikation: Weichteilinfektionen"
monitor_inn: "ORITAVANCIN"
predicted_indications: ["Bacteroidaceae infectious disease", "ophthalmic herpes zoster", "Mycoplasma pneumoniae pneumonia"]
---

# Oritavancin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Oritavancin: Von Weichteilinfektionen zu Bacteroidaceae-Infektionen
{: .text-alpha }

## Zusammenfassung in einem Satz

Oritavancin ist ein Lipoglykopeptid-Antibiotikum, das ursprünglich zur Behandlung von Weichteilinfektionen und bakteriellen Hauterkrankungen zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass es bei **Bacteroidaceae-Infektionen** wirksam sein könnte.
Dafür liegen jedoch derzeit **keine klinischen Studien** und **keine Publikationen** vor, die diese Richtung stützen.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Weichteilinfektionen; bakterielle Hauterkrankungen |
| Vorhergesagte neue Indikation | Bacteroidaceae-Infektionen |
| TxGNN-Vorhersagewert | 0,9948 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Laut den Abschnitten „Mechanism of Action“ und „Microbiology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Oritavancin (inoffizielle Übersetzung): „Oritavancin ist ein antibakterieller Wirkstoff. […] Oritavancin besitzt drei Wirkmechanismen: (i) Hemmung des Transglykosylierungsschritts (Polymerisation) der Zellwandbiosynthese durch Bindung an das Stammpeptid von Peptidoglykan-Vorstufen; (ii) Hemmung des Transpeptidierungsschritts (Quervernetzung) der Zellwandbiosynthese durch Bindung an die Peptid-Brückensegmente der Zellwand; und (iii) Störung der Integrität der Bakterienmembran, was zu Depolarisation, Permeabilisierung und Zelltod führt. Diese multiplen Mechanismen tragen zur konzentrationsabhängigen bakteriziden Wirkung von Oritavancin bei.“ Englischer Originalwortlaut: "Oritavancin is an antibacterial drug. […] Oritavancin has three mechanisms of action: (i) inhibition of the transglycosylation (polymerization) step of cell wall biosynthesis by binding to the stem peptide of peptidoglycan precursors; (ii) inhibition of the transpeptidation (crosslinking) step of cell wall biosynthesis by binding to the peptide bridging segments of the cell wall; and (iii) disruption of bacterial membrane integrity, leading to depolarization, permeabilization, and cell death. These multiple mechanisms contribute to the concentration-dependent bactericidal activity of oritavancin." ([DailyMed: Orbactiv (oritavancin) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff09a726-9f9b-4e30-b509-396781293220), Fassung vom 2026-09-15; abgerufen am 2026-11-19). Bekannt ist, dass Oritavancin ein Lipoglykopeptid ist, das die bakterielle Zellwandsynthese (Transglykosylierung und Transpeptidierung) hemmt und die Membranintegrität stört. Seine Wirkung richtet sich in erster Linie gegen grampositive Erreger, was die Zulassung bei Haut- und Weichteilinfektionen erklärt.

Bacteroidaceae (z. B. *Bacteroides* spp.) sind gramnegative Anaerobier mit einer äußeren Membran, die Glykopeptide in der Regel nicht durchdringen können. Die mechanistische Begründung ist daher schwach. Der hohe TxGNN-Wert ist eine rein computergestützte Vorhersage und wird durch keine Studie oder Publikation gestützt.

Auch die weiteren vorhergesagten Indikationen sind mechanistisch fragwürdig:
- **Ophthalmischer Herpes zoster** (Wert 0,9903): Der Erreger ist ein Virus, Oritavancin hat keinen antiviralen Mechanismus. Der hohe Wert stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, nicht biologische Evidenz.
- **Mycoplasma-pneumoniae-Pneumonie** (Wert 0,9901): Mycoplasmen besitzen keine Zellwand, zellwandwirksame Substanzen sind daher voraussichtlich von Natur aus unwirksam.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003785 | Tenkasi (zuvor Orbactiv) | – | Weichteilinfektionen; bakterielle Hauterkrankungen |

Hinweis: Diese Zulassung ist gültig (1 von 1 Zulassung); das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 38 Wechselwirkungen erfasst. Auszug aus den ausgewerteten Einträgen:
  - **Schwerwiegend (Major)**: Heparin
  - **Mäßig (Moderate)**: u. a. Warfarin, Ticagrelor, Cobicistat, Hydrocodon, Ethinylestradiol, Abemaciclib, Acalabrutinib, Alpelisib, Brigatinib, Cabozantinib, Crizotinib, Fostamatinib, Elagolix, Osilodrostat, Nitisinon, Praziquantel, Macimorelin, Natriumpicosulfat
  - **Gering (Minor)**: Bortezomib

  Besondere Vorsicht ist bei gleichzeitiger Gabe von Antikoagulanzien (Heparin, Warfarin) geboten.

Zu Warnhinweisen und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzlevel L5) ohne Studien oder Publikationen. Der Wirkmechanismus von Oritavancin (gegen grampositive Erreger, an der Zellwand angreifend) passt schlecht zu gramnegativen Bacteroidaceae.

**Für ein Weiterkommen erforderlich:**
- Vollständige Daten zum Wirkmechanismus (MOA)
- Fachinformation mit Warnhinweisen und Gegenanzeigen (derzeit blockierende Datenlücke für das Sicherheits-Screening)
- In-vitro-Empfindlichkeitsdaten (MHK) von Oritavancin gegen *Bacteroides* spp.
- Präklinische oder klinische Belege für die Wirksamkeit bei Infektionen mit Bacteroidaceae
- Klärung des Zulassungsstatus und der verfügbaren Applikationswege in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Orbactiv (oritavancin) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff09a726-9f9b-4e30-b509-396781293220) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

