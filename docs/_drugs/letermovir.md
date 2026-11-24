---
layout: default
title: Letermovir
parent: Nur Modellvorhersage (L5)
nav_order: 267
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Letermovir: vorhergesagte neue Indikation Vulvovaginale Candidose (Evidenzstufe L5). Ursprüngliche Indikation: Cytomegalovirus-Infektionen"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

## Letermovir: Vulvovaginale Candidose
{: .text-alpha }

## Zusammenfassung

Letermovir ist ein antiviraler Wirkstoff, der ursprünglich zur Behandlung von Cytomegalovirus-Infektionen zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **vulvovaginaler Candidose** wirksam sein könnte.
Für diese Richtung liegen in den für diesen Bericht zusammengestellten Daten jedoch **keine klinischen Studien** und **keine Publikationen** vor.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Cytomegalovirus-Infektionen |
| Vorhergesagte neue Indikation | Vulvovaginale Candidose |
| TxGNN-Vorhersagewert | 0,9988 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Laut den Abschnitten „Mechanism of Action“ und „Microbiology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Letermovir (inoffizielle Übersetzung): „PREVYMIS ist ein antivirales Arzneimittel gegen CMV. […] Letermovir hemmt den CMV-DNA-Terminase-Komplex (pUL51, pUL56 und pUL89), der für die Prozessierung und Verpackung der viralen DNA erforderlich ist. Biochemische Charakterisierung und Elektronenmikroskopie zeigten, dass Letermovir die Bildung von Genomen korrekter Einheitslänge beeinträchtigt und die Virionreifung stört.“ Englischer Originalwortlaut: "PREVYMIS is an antiviral drug against CMV. […] Letermovir inhibits the CMV DNA terminase complex (pUL51, pUL56, and pUL89) which is required for viral DNA processing and packaging. Biochemical characterization and electron microscopy demonstrated that letermovir affects the production of proper unit length genomes and interferes with virion maturation." ([DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b), Fassung vom 2026-01-14; abgerufen am 2026-11-19). Bekannt ist, dass Letermovir ein CMV-spezifischer Virostatikum ist, das den viralen Terminase-Komplex (pUL56/pUL51/pUL89) hemmt. Seine Wirksamkeit bei Cytomegalovirus-Infektionen ist belegt.

Für diesen Angriffspunkt ist in Candida-Arten (Pilzen) kein bekanntes Homolog beschrieben. Ein mechanistischer Zusammenhang zwischen der ursprünglichen und der vorhergesagten Indikation wird durch die vorliegenden Daten daher nicht gestützt. Der sehr hohe TxGNN-Wert (0,9988) stammt vom TxGNN-Modell (Deep Learning) und kann vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen widerspiegeln. Er ist kein biologischer Beleg und wird durch keine präklinischen oder klinischen Belege bestätigt.

Eine mögliche indirekte Erklärung wären vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen, etwa über gemeinsame Wechselwirkungs- oder CYP-bezogene Nachbarn (z. B. Azol-Antimykotika wie Voriconazol und Fluconazol, die mit Letermovir interagieren). Das ist spekulativ und keine therapeutische Begründung. Zudem stehen für diese Erkrankung bereits wirksame und kostengünstige Standardtherapien zur Verfügung (topische Azole, orales Fluconazol), was den Anlass für ein Repurposing weiter verringert.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/004536 | Prevymis | Letermovir | Cytomegalovirus Infections | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Hinweis: Diese Zulassung hat den Status „gültig“. Das Arzneimittel ist im Handel.

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** In den zusammengestellten Daten sind 100 Wechselwirkungen verzeichnet (Quelle: DDInter). Auszug:

- **Schwerwiegend (Major):** Eliglustat, Naloxegol, Cisaprid
- **Mäßig (Moderate):** u. a. Hydrocortison, Dexamethason, Betamethason, Triamcinolon, Budesonid, Omeprazol, Lansoprazol, Aprepitant, Clarithromycin, Pioglitazon, Saxagliptin, Glimepiride, Chlorpropamid, Acetohexamid, Naldemedin, Nitisinon

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (Evidenzlevel L5). Es gibt weder klinische Studien noch Publikationen, einen plausiblen Mechanismus gegen Candida gibt es nicht, und wirksame Standardtherapien existieren bereits. Das Arzneimittel ist in Deutschland im Handel (1 von 1 Zulassung gültig).

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen) für das Sicherheitsscreening
- Daten zum Wirkmechanismus (MOA)
- Präklinische In-vitro-Daten zur Aktivität gegen Candida-Arten
- Klärung des Zulassungsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

