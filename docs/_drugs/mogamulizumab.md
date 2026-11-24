---
layout: default
title: Mogamulizumab
parent: Nur Modellvorhersage (L5)
nav_order: 304
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Mogamulizumab: vorhergesagte neue Indikation Urothelkarzinom der prostatischen Harnröhre (Evidenzstufe L5). Ursprüngliche Indikation: Sézary-Syndrom"
monitor_inn: "MOGAMULIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "human herpesvirus 8-related tumor", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor"]
---

# Mogamulizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

## Mogamulizumab: Vom kutanen T-Zell-Lymphom zum Urothelkarzinom der prostatischen Harnröhre
{: .text-alpha }

## Zusammenfassung

Mogamulizumab ist ein Antikörper, der ursprünglich zur Behandlung des Sézary-Syndroms und der Mycosis fungoides (kutane T-Zell-Lymphome) zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **Urothelkarzinom der prostatischen Harnröhre** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht ausschließlich auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Sézary-Syndrom; Mycosis fungoides |
| Vorhergesagte neue Indikation | Urothelkarzinom der prostatischen Harnröhre |
| TxGNN-Vorhersagewert | 0,9944 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Mogamulizumab (inoffizielle Übersetzung): „Mogamulizumab-kpkc ist ein defucosylierter, humanisierter monoklonaler IgG1-kappa-Antikörper, der an CCR4 bindet, einen G-Protein-gekoppelten Rezeptor für CC-Chemokine, der am Transport von Lymphozyten zu verschiedenen Organen beteiligt ist. Nichtklinische In-vitro-Studien zeigen, dass die Bindung von Mogamulizumab-kpkc eine Zelle für die antikörperabhängige zelluläre Zytotoxizität (ADCC) markiert, was zur Depletion der Zielzellen führt.“ Englischer Originalwortlaut: "Mogamulizumab-kpkc is a defucosylated, humanized IgG1 kappa monoclonal antibody that binds to CCR4, a G protein-coupled receptor for CC chemokines that is involved in the trafficking of lymphocytes to various organs. Non-clinical in vitro studies demonstrate mogamulizumab-kpkc binding targets a cell for antibody-dependent cellular cytotoxicity (ADCC) resulting in depletion of the target cells." ([DailyMed: Poteligeo (mogamulizumab-kpkc) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e53960ab-42a1-40d1-9c7d-eb013fe7f18f), Fassung vom 2026-03-02; abgerufen am 2026-11-19). Nach allgemeinem Wissen ist Mogamulizumab ein gegen CCR4 gerichteter monoklonaler Antikörper. Er depletiert CCR4-exprimierende Zellen, darunter regulatorische T-Zellen (Tregs), über verstärkte antikörperabhängige zelluläre Zytotoxizität (ADCC). Diese Angabe wurde nicht anhand der vorliegenden Daten verifiziert.

Die hypothetische Verbindung zur neuen Indikation: Eine Treg-Depletion könnte die Immunsuppression im Tumormikromilieu des Urothelkarzinoms verringern und möglicherweise die Wirkung von Checkpoint-Inhibitoren ergänzen. Für eine CCR4-Expression oder Treg-Abhängigkeit bei diesem Tumortyp liegen in den Daten keine Belege vor. Der hohe Wert stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, keine biologische Evidenz und keine klinische Validierung.

Weitere vorhergesagte Indikationen (jeweils nur Modellvorhersage, L5, Hold):

| Rang | Indikation | TxGNN-Wert | Anmerkung |
|---|---|---|---|
| 2 | Sarkomatoides Übergangszellkarzinom des Nierenbeckens | 0,9942 | Aggressive Variante mit eigener Biologie; kein Beleg für CCR4-Bezug |
| 3 | Infiltrierendes Urothelkarzinom der Blase, sarkomatoide Variante | 0,9940 | Mögliche Ergänzung zur Checkpoint-Hemmung, rein hypothetisch |
| 4 | Papilläres Urothelkarzinom des Nierenbeckens | 0,9937 | Spekulativ; CCR4-Relevanz unbestätigt |
| 5 | Humanes-Herpesvirus-8-assoziierter Tumor | 0,9924 | Biologisch etwas plausibler (Immundysregulation); Sicherheitsfragen bei immunsupprimierten Patienten |
| 6 | Ektomesenchymom | 0,9915 | Kein mechanistischer Bezug erkennbar |
| 7 | Maligner kutaner Granularzelltumor | 0,9915 | Nur Hautbezug gemeinsam, andere Zelllinie (Schwann-Zellen) |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

<!-- review:begin de-lic-20261106-mogamulizumab-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Hinweis: Diese Zulassung ist aufgehoben (Status: cancelled).“ Entfernt: Die Aussage widersprach den Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-mogamulizumab-1 -->

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/004232 | Poteligeo | mogamulizumab | Sezary Syndrome; Mycosis Fungoides | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Klassifikation | Gezielte Therapie (monoklonaler Antikörper gegen CCR4), kein konventionelles Zytostatikum |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Monitoring | Bitte Fachinformation beachten |
| Handhabungsschutz | Bitte Fachinformation beachten |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 83 Wechselwirkungen erfasst. Auswahl:
  - **Schwerwiegend (Major):** Deferipron, Samarium-(153Sm)-Lexidronam, Adalimumab, Baricitinib
  - **Moderat:** u. a. Strontiumchlorid Sr-89, Roflumilast, Chloramphenicol, Zidovudin, Alemtuzumab, Anakinra, Azathioprin, Canakinumab, Alefacept sowie Impfstoffe (Tetanustoxoid, Anthrax)
  - **Gering (Minor):** Zinksalze (Sulfat, Acetat, Gluconat, Chlorid)

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich allein auf das Modell (L5); es gibt weder Studien noch Publikationen, und der mechanistische Bezug ist unbestätigt.

<!-- review:begin de-lic-20261106-mogamulizumab-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Die Vorhersage stützt sich allein auf das Modell (L5); es gibt weder Studien noch Publikationen, und der mechanistische Bezug ist unbestätigt. Zudem ist die einzige deutsche Zulassung aufgehoben.“ Entfernt: Die Aussage widersprach den Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-mogamulizumab-2 -->

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen) zur Sicherheitsprüfung
- Vollständige Wirkmechanismus-Daten (z. B. aus DrugBank)
- Prüfung der CCR4-Expression und Treg-Abhängigkeit in Urothelkarzinomen (präklinisch oder aus der Literatur)
- Literatur- und Studienrecherche zu CCR4-Antikörpern bei soliden Tumoren
- Klärung des Zulassungs- und Verfügbarkeitsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Hinweis: Diese Zulassung ist aufgehoben (Status: cancelled)“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „Zudem ist die einzige deutsche Zulassung aufgehoben“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Poteligeo (mogamulizumab-kpkc) prescribing information, Kyowa Kirin, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e53960ab-42a1-40d1-9c7d-eb013fe7f18f) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

