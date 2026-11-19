---
layout: default
title: Bupivacaine
parent: Nur Modellvorhersage (L5)
nav_order: 81
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Bupivacaine: vorhergesagte neue Indikation Acrodermatitis chronica atrophicans (Evidenzstufe L5). Ursprüngliche Indikation: Akuter Schmerz"
monitor_inn: "BUPIVACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
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

## Bupivacain: Von akutem Schmerz zu Acrodermatitis chronica atrophicans
{: .text-alpha }

## Zusammenfassung in einem Satz

Bupivacain ist ein Lokalanästhetikum vom Amid-Typ und wurde ursprünglich zur Behandlung von **akutem Schmerz** eingesetzt. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Acrodermatitis chronica atrophicans** voraus. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, sie beruht ausschließlich auf der Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Akuter Schmerz |
| Vorhergesagte neue Indikation | Acrodermatitis chronica atrophicans |
| TxGNN-Vorhersagewert | 0,9923 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Bupivacaine (inoffizielle Übersetzung): „Lokalanästhetika blockieren die Entstehung und die Weiterleitung von Nervenimpulsen, vermutlich indem sie die Schwelle für die elektrische Erregung im Nerv erhöhen, die Ausbreitung des Nervenimpulses verlangsamen und die Anstiegsgeschwindigkeit des Aktionspotenzials verringern. Im Allgemeinen hängt das Fortschreiten der Anästhesie vom Durchmesser, der Myelinisierung und der Leitungsgeschwindigkeit der betroffenen Nervenfasern ab.“ Englischer Originalwortlaut: "Local anesthetics block the generation and the conduction of nerve impulses presumably by increasing the threshold for electrical excitation in the nerve, by slowing the propagation of the nerve impulse, and by reducing the rate of rise of the action potential. In general, the progression of anesthesia is related to the diameter, myelination, and conduction velocity of affected nerve fibers." ([DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66), Fassung vom 2026-11-09; abgerufen am 2026-11-19). Bekannt ist, dass Bupivacain ein Amid-Lokalanästhetikum ist, das spannungsabhängige Natriumkanäle blockiert. Seine Wirksamkeit bei akutem Schmerz gilt als belegt.

Ein plausibler mechanistischer Zusammenhang mit der neuen Indikation lässt sich aus den vorliegenden Daten **nicht** ableiten. Die Acrodermatitis chronica atrophicans ist das späte Hautstadium der Lyme-Borreliose und erfordert eine antibiotische Behandlung. Ein Lokalanästhetikum hat bei der zugrunde liegenden Infektion keine plausible Rolle. Der hohe TxGNN-Wert (0,9923) ist eine reine Modellvorhersage ohne klinische oder literarische Stützung.

Weitere vom Modell vorhergesagte Indikationen sind ebenfalls ohne belegten mechanistischen Zusammenhang und ohne Studien oder Publikationen:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Evidenzgrad | Einschätzung |
|------|------|------|------|------|
| 2 | Neonatale Dermatomyositis | 0,9915 | L5 | Hold. Immunvermittelte Erkrankung. Bupivacain ist in hohen lokalen Konzentrationen myotoxisch, zudem bestehen Sicherheitsbedenken bei Neugeborenen (systemische Toxizität von Lokalanästhetika). |
| 3 | Sekundäre interstitielle Lungenerkrankung des Kindesalters bei Bindegewebserkrankung | 0,9911 | L5 | Hold. Die Therapie beruht auf Immunsuppression. Der hohe Wert spiegelt vermutlich die Nähe im Netzwerk wider, nicht eine pharmakologische Begründung. |
| 4 | Amyopathische Dermatomyositis | 0,9903 | L5 | Hold. Allenfalls symptomatische Linderung lokaler Schmerzen oder von Juckreiz, keine Repurposing-Indikation. |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004586 | Exparel liposomal | – | Akuter Schmerz |

Der Hersteller ist Pacira Ireland Limited.

<!-- review:begin de-lic-20261106-bupivacaine-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Diese Zulassung ist erloschen. Der Hersteller ist Pacira Ireland Limited.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-bupivacaine-1 -->

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (PrimeKG, keine Angaben aus Fachinformationen):** Für folgende Erkrankungen sind Kontraindikations-Verknüpfungen hinterlegt: Bluthochdruck und Hypotonie, Leberversagen und Lebererkrankung, Epilepsie, COPD, Nierenerkrankung, Gallenblasenerkrankung, Hypothyreose (einschließlich Myxödem und angeborener Hypothyreose), chronisch-entzündliche Darmerkrankung, Kaliummangel, Diabetes mellitus und diabetische Ketoazidose, benigne Prostatahyperplasie, Vorhofflimmern, koronare Herzkrankheit, Myokardinfarkt, Koronarthrombose, plötzlicher Herzstillstand, Erregungsleitungsstörungen des Herzens, Hämoglobinopathie, Atemversagen, Engwinkelglaukom, Substanzmissbrauch/-abhängigkeit sowie Pyoureter.
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 56 Wechselwirkungen erfasst. Als moderat eingestuft sind:
  - Aprepitant
  - Morphin (liposomal)

  Weitere erfasste Wechselwirkungen ohne Schweregrad-Einstufung sind unter anderem Pantoprazol, Omeprazol, Lansoprazol, Vancomycin, Atropin, Prednison, Prednisolon, Dexamethason, Hydrocortison, Triamcinolon, Simvastatin, Kaliumchlorid, Ranitidin, Famotidin, Ondansetron, Metoclopramid, Metronidazol und Naloxon.

Hinweise und Gegenanzeigen aus der Fachinformation lagen nicht vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzgrad L5) ohne Studien oder Publikationen. Ein mechanistischer Zusammenhang ist nicht erkennbar, da die Acrodermatitis chronica atrophicans eine antibiotisch zu behandelnde Infektion ist. In Deutschland ist das Arzneimittel zudem im Verkehr; es besteht 1 gültige Zulassung (von 1).

**Für ein Weiterkommen sind erforderlich:**
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen) für die Sicherheitsprüfung
- Daten zum Wirkmechanismus (MOA), z. B. aus DrugBank
- Präklinische oder klinische Belege für einen plausiblen Wirkzusammenhang
- Prüfung der Anwendungswege und der Verträglichkeit in der Zielpopulation

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Diese Zulassung ist erloschen“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

