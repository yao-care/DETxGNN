---
layout: default
title: Levodopa
parent: Nur Modellvorhersage (L5)
nav_order: 269
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Levodopa: vorhergesagte neue Indikation Rasmussen-Enzephalitis (Rasmussen subacute encephalitis) (Evidenzstufe L5). Ursprüngliche Indikation: Morbus Parkinson"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
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

## Levodopa: Von Morbus Parkinson zu Rasmussen-Enzephalitis
{: .text-alpha }

## Zusammenfassung

Levodopa ist eine Vorstufe von Dopamin und wird ursprünglich zur Behandlung der Parkinson-Krankheit eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei der **Rasmussen-Enzephalitis** (subakute Enzephalitis) wirksam sein könnte. Hierfür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Morbus Parkinson |
| Vorhergesagte neue Indikation | Rasmussen-Enzephalitis (Rasmussen subacute encephalitis) |
| TxGNN-Vorhersagewert | 0,9906 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 5 von 5) |
| Anzahl der Zulassungen | 5 (gültig: 5) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Levodopa (inoffizielle Übersetzung): „Levodopa, die Stoffwechselvorstufe von Dopamin, überwindet die Blut-Hirn-Schranke und wird vermutlich im Gehirn zu Dopamin umgewandelt. Man nimmt an, dass dies der Mechanismus ist, über den Levodopa die Symptome der Parkinson-Krankheit lindert.“ Englischer Originalwortlaut: "Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease." ([DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb), Fassung vom 2026-07-20; abgerufen am 2026-11-19). Bekannt ist: Levodopa ist ein Dopamin-Vorläufer, der im nigrostriatalen Signalweg wirkt. Seine Wirksamkeit bei Morbus Parkinson ist gut belegt.

Die Rasmussen-Enzephalitis ist eine seltene, chronische, meist einseitige entzündliche Hirnerkrankung. Sie ist gekennzeichnet durch T-Zell-vermittelte Neuroinflammation, fortschreitende Atrophie einer Hirnhälfte und schwer behandelbare fokale Krampfanfälle. Ein mechanistischer Zusammenhang mit der ursprünglichen Indikation ist nicht belegt. Eine Modulation der Neuroimmunaktivität durch Dopamin ist bestenfalls eine theoretische Verbindung. Es gibt keinen Hinweis darauf, dass Levodopa die immunvermittelte Pathologie oder die Anfallskontrolle beeinflusst.

Der hohe TxGNN-Wert (0,9906) ist eine reine Modellvorhersage ohne Rückhalt in Studien oder Literatur. Zudem können dopaminerge Substanzen in manchen Situationen die Krampfschwelle senken, sodass ein Sicherheitsrisiko nicht auszuschließen ist.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000511 | Stalevo | levodopa; carbidopa; entacapone | Parkinson Disease | Gültig |
| EMEA/H/C/002441 | Levodopa/Carbidopa/Entacapone Orion | levodopa; carbidopa; entacapone | Parkinson Disease | Gültig |
| EMEA/H/C/002785 | Corbilta (previously Levodopa/Carbidopa/Entacapone Sandoz) | levodopa; carbidopa; entacapone | Parkinson Disease | Gültig |
| EMEA/H/C/004786 | Inbrija | levodopa | Parkinson Disease | Gültig |
| EMEA/H/C/006429 | Onerji | levodopa; carbidopa | Parkinson Disease | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Von fünf Zulassungen sind fünf gültig; das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph (PrimeKG, keine Packungsbeilagen-Angaben):** Im Wissensgraphen sind u. a. folgende Erkrankungen als Kontraindikationen hinterlegt:
  - Neurologisch/psychiatrisch: Multisystematrophie, medikamenteninduzierte Dyskinesie, Epilepsie, Angststörung, neurotische Störung, dysthyme Störung, psychotische Störung, schizophreniforme Störung, schizoaffektive Störung, psychische Störung
  - Kardiovaskulär: orthostatische Hypotonie, posturales orthostatisches Tachykardiesyndrom (POTS), Myokardinfarkt, Koronarthrombose, plötzlicher Herzstillstand, Erregungsleitungsstörung des Herzens
  - Augen: Offenwinkelglaukom, Engwinkelglaukom
  - Magen-Darm/Leber/Niere: Magengeschwür, Ulkuskrankheit, Nierenerkrankung, Pyoureter, Lebererkrankung, Gallenblasenerkrankung, Durchfallerkrankung
  - Stoffwechsel/Sonstige: Diabetes mellitus, diabetische Ketoazidose, Melanom, Hämoglobinopathie
- **Arzneimittelwechselwirkungen:** Die Abfrage ergab 100 Wechselwirkungen. Folgende Beispiele sind aufgeführt:
  - Moderat: Epinephrin, Ephedrin, Methscopolamin, Hyoscyamin, Atropin, Glycopyrronium, Clidinium, Dicyclomin, Mepenzolat, Bupropion, Metronidazol, Pyridoxin, Eisen, Metoclopramid
  - Gering: Aluminiumhydroxid, Calciumcarbonat, Magaldrat, Magnesiumcarbonat, Magnesiumhydroxid, Magnesiumoxid
- Warnhinweise und Gegenanzeigen aus der Packungsbeilage liegen nicht vor und müssen ergänzt werden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (Evidenzstufe L5); es gibt weder Studien noch Publikationen, und ein plausibler mechanistischer Zusammenhang fehlt. Hinzu kommen eine mögliche Senkung der Krampfschwelle.

<!-- review:begin de-lic-20261106-levodopa-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Hinzu kommen eine mögliche Senkung der Krampfschwelle, die fehlende gültige Zulassung in Deutschland sowie fehlende Daten zu Warnhinweisen und Gegenanzeigen.“ Entfernt: Die angegebene Zahl oder der Status der Zulassungen stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 5 Zulassungen erfasst, davon 5 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-levodopa-1 -->

**Für ein Fortschreiten ist Folgendes erforderlich:**
- Packungsbeilage des BfArM mit Warnhinweisen und Gegenanzeigen (blockierende Datenlücke für die Sicherheitsprüfung)
- Daten zum Wirkmechanismus von Levodopa (z. B. aus DrugBank)
- Präklinische oder mechanistische Belege für einen Nutzen bei der Rasmussen-Enzephalitis (Neuroimmunmodulation, Anfallskontrolle)
- Bewertung des Anfallsrisikos dopaminerger Therapie bei dieser Erkrankung
- Prüfung der Darreichungsformen/Applikationswege und der Zulassungssituation in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „die fehlende gültige Zulassung in Deutschland sowie fehlende Daten zu Warnhinweisen und Gegenanzeigen“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

