---
layout: default
title: Tildrakizumab
parent: Nur Modellvorhersage (L5)
nav_order: 464
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Tildrakizumab: vorhergesagte neue Indikation Schwere nichtproliferative diabetische Retinopathie (Evidenzstufe L5). Ursprüngliche Indikation: Psoriasis"
monitor_inn: "TILDRAKIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "drug-induced osteoporosis"]
---

# Tildrakizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

## Tildrakizumab: Von Psoriasis zu Schwere nichtproliferative diabetische Retinopathie
{: .text-alpha }

## Zusammenfassung

Tildrakizumab ist ein monoklonaler Antikörper, der ursprünglich zur Behandlung der Psoriasis zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **schwerer nichtproliferativer diabetischer Retinopathie** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Psoriasis |
| Vorhergesagte neue Indikation | Schwere nichtproliferative diabetische Retinopathie |
| TxGNN-Vorhersagewert | 0,9963 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Tildrakizumab (inoffizielle Übersetzung): „Tildrakizumab ist ein humanisierter monoklonaler IgG1/k-Antikörper, der selektiv an die p19-Untereinheit von IL-23 bindet und dessen Interaktion mit dem IL-23-Rezeptor hemmt. IL-23 ist ein natürlich vorkommendes Zytokin, das an Entzündungs- und Immunreaktionen beteiligt ist.“ Englischer Originalwortlaut: "Tildrakizumab is a humanized IgG1/k monoclonal antibody that selectively binds to the p19 subunit of IL-23 and inhibits its interaction with the IL-23 receptor. IL-23 is a naturally occurring cytokine that is involved in inflammatory and immune responses." ([DailyMed: Ilumya (tildrakizumab-asmn) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6a322bb-51b9-4f0e-8642-62a9682ffcde), Fassung vom 2026-11-02; abgerufen am 2026-11-19). Bekannt ist, dass es sich um einen Antikörper gegen die p19-Untereinheit von Interleukin-23 (IL-23) handelt. Dadurch wird die IL-23/Th17-Achse blockiert, die bei der Psoriasis eine zentrale Rolle spielt.

Mechanistisch wird vermutet, dass chronische, niedriggradige Entzündung und IL-17-vermittelte Signalwege zur Schädigung der Netzhautgefäße bei diabetischer Retinopathie beitragen. Dieser Zusammenhang ist **hypothetisch**. Der hohe TxGNN-Wert ist eine rein rechnerische Vorhersage.

Wichtige Einschränkungen: Für einen großen systemischen Antikörper ist weder eine okuläre Wirkstoffabgabe noch ein Wirksamkeitskonzept etabliert. Zudem sind Anti-VEGF-Therapien der Behandlungsstandard.

Weitere vom Modell vorhergesagte Indikationen (jeweils ebenfalls nur Evidenzniveau L5, Empfehlung Hold):

| Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|------|------|------|
| Diabetische Retinopathie | 0,9953 | Gleiche spekulative Begründung wie oben |
| Diabetische Katarakt | 0,9921 | Kein klarer mechanistischer Zusammenhang; Katarakt wird v. a. durch Polyolweg, osmotischen und oxidativen Stress verursacht |
| Medikamenteninduzierte Osteoporose | 0,9920 | Biologisch plausibel (IL-23/IL-17 beeinflussen den Knochenumbau über RANKL), Wirkrichtung jedoch unklar |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/004514 | Ilumetri | tildrakizumab | Psoriasis | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Das Arzneimittel ist im Handel; die einzige Zulassung (1 von 1) ist gültig.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 78 Wechselwirkungen erfasst. Wichtige Beispiele:
  - **Schwerwiegend (Major)**: Adalimumab, Baricitinib, Certolizumab pegol, Cladribin (jeweils vor allem additive Immunsuppression)
  - **Moderat**: u. a. Roflumilast, Tacrolimus, Azathioprin, Ciclosporin, Anakinra, Canakinumab, Alemtuzumab, Denosumab sowie mehrere Impfstoffe (u. a. Tetanus-Toxoid, Milzbrand, Cholera-Lebendimpfstoff)
  - **Gering (Minor)**: Zinksalze (Sulfat, Acetat, Gluconat, Chlorid)

Zu Warnhinweisen und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (L5), ohne klinische Studien oder Publikationen. Der mechanistische Zusammenhang ist spekulativ, ein okulärer Wirkansatz fehlt, und mit Anti-VEGF-Therapien existiert ein etablierter Standard.

<!-- review:begin de-lic-20261106-tildrakizumab-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Der mechanistische Zusammenhang ist spekulativ, ein okulärer Wirkansatz fehlt, und mit Anti-VEGF-Therapien existiert ein etablierter Standard. Zudem ist die deutsche Zulassung erloschen.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-tildrakizumab-1 -->

**Für ein Weiterkommen sind folgende Punkte erforderlich:**
- Präklinische oder mechanistische Studien zur Rolle der IL-23/IL-17-Achse bei diabetischer Retinopathie
- Detaillierte Wirkmechanismusdaten (MOA)
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen), da diese Sicherheitsdaten derzeit fehlen
- Klärung der Machbarkeit (Applikationsweg, okuläre Verfügbarkeit)
- Klärung des regulatorischen Status in Deutschland/EU

<!-- review:begin de-lic-20261106-tildrakizumab-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Klärung des regulatorischen Status in Deutschland/EU (erloschene Zulassung)“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-tildrakizumab-2 -->

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Zudem ist die deutsche Zulassung erloschen“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „(erloschene Zulassung)“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Ilumya (tildrakizumab-asmn) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6a322bb-51b9-4f0e-8642-62a9682ffcde) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

