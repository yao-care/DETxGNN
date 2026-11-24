---
layout: default
title: Brodalumab
parent: Nur Modellvorhersage (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Brodalumab: vorhergesagte neue Indikation Strongyloidiasis (Evidenzstufe L5). Ursprüngliche Indikation: Psoriasis"
monitor_inn: "BRODALUMAB"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "isolated optic neuritis", "recurrent idiopathic neuroretinitis", "optic perineuritis", "chronic relapsing inflammatory optic neuropathy", "nodular episcleritis", "episcleritis periodica fugax"]
---

# Brodalumab
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

## Brodalumab: Von Psoriasis zu Strongyloidiasis
{: .text-alpha }

## Zusammenfassung in einem Satz

Brodalumab ist ein Antikörper gegen den IL-17-Rezeptor A und wurde ursprünglich zur Behandlung der Psoriasis eingesetzt.
Das TxGNN-Modell sagt voraus, dass er bei **Strongyloidiasis** wirksam sein könnte. Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor.
Die Vorhersage beruht allein auf einer Modellberechnung und ist biologisch fraglich.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Psoriasis |
| Vorhergesagte neue Indikation | Strongyloidiasis |
| TxGNN-Vorhersagewert | 0,9984 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Brodalumab (inoffizielle Übersetzung): „Brodalumab ist ein humaner monoklonaler IgG2-Antikörper, der selektiv an humanes IL-17RA bindet und dessen Interaktionen mit den Zytokinen IL-17A, IL-17F, IL-17C, dem IL-17A/F-Heterodimer und IL-25 hemmt. IL-17RA ist ein auf der Zelloberfläche exprimiertes Protein und ein notwendiger Bestandteil von Rezeptorkomplexen, die von mehreren Zytokinen der IL-17-Familie genutzt werden.“ Englischer Originalwortlaut: "Brodalumab is a human monoclonal IgG2 antibody that selectively binds to human IL-17RA and inhibits its interactions with cytokines IL-17A, IL-17F, IL-17C, IL-17A/F heterodimer, and IL-25. IL-17RA is a protein expressed on the cell surface and is a required component of receptor complexes utilized by multiple IL-17 family cytokines." ([DailyMed: Siliq (brodalumab) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a550c33-456a-4833-814e-8591aea7c688), Fassung vom 2026-05-28; abgerufen am 2026-11-19). Bekannt ist, dass Brodalumab den IL-17-Rezeptor A blockiert und damit die Signalwege mehrerer IL-17-Zytokine hemmt. Dies ist bei Psoriasis therapeutisch wirksam.

Bei Strongyloidiasis, einer parasitären Wurminfektion, ist der Zusammenhang jedoch fragwürdig. IL-17 trägt zur antiparasitären Abwehr und zur Schleimhautimmunität bei. Eine Blockade könnte daher die Anfälligkeit für Wurminfektionen eher erhöhen oder den Krankheitsverlauf verschlechtern, statt ihn zu behandeln. Der hohe TxGNN-Wert (0,998) ist eine rein rechnerische Vorhersage und stützt sich nicht auf klinische oder publizierte Belege.

Ein weiterer Hinweis: Auch die übrigen Top-10-Vorhersagen (z. B. Augenerkrankungen, Vitaminmangel, Optikusneuropathien) haben fast identische Scores und überwiegend keinerlei Evidenz. Dies spricht für Artefakte der Graphstruktur. Die einzige Vorhersage mit etwas Literatur ist „Augenerkrankung" (L4), doch weisen die Publikationen eher auf paradoxe Entzündungen als auf einen Nutzen hin.

---

## Evidenz aus klinischen Studien

Derzeit sind keine einschlägigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine einschlägige Literatur zu Strongyloidiasis verfügbar.

---

## Marktinformationen Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/003959 | Kyntheum | brodalumab | Psoriasis | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

- **Wechselwirkungen:** Insgesamt wurden 68 mögliche Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind u. a. Adalimumab, Baricitinib, Certolizumab pegol und der lebende BCG-Impfstoff (Tice-Stamm). Mittelgradig (Moderate) sind u. a. Roflumilast, Alefacept, Alemtuzumab, Anakinra, Canakinumab sowie mehrere Impfstoffe (z. B. Anthrax, Cholera, Tetanustoxoid). Gering (Minor) sind Zinksalze. Insgesamt ist besondere Vorsicht bei Kombination mit anderen Immunsuppressiva/Biologika und Lebendimpfstoffen geboten.
- **Kontraindikationen laut Wissensgraph (keine Packungsbeilagen-Angaben):** Morbus Crohn, chronisch-entzündliche Darmerkrankungen, Crohn-Kolitis.
- **Neuropsychiatrische Warnung:** Im Zusammenhang mit der Bewertung von Optikusneuritis wurde auf das Risiko suizidaler Gedanken hingewiesen.

Für weitere Sicherheitsinformationen, insbesondere Warnhinweise und Kontraindikationen, ist die Fachinformation heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für Strongyloidiasis beruht ausschließlich auf einem Modellwert ohne klinische oder publizierte Belege (L5). Mechanistisch ist eher ein Schaden durch die IL-17-Blockade zu erwarten. Das Arzneimittel ist in Deutschland im Handel; 1 von 1 Zulassung ist gültig.

**Für ein Weiterkommen sind erforderlich:**
- Fachinformation (Warnhinweise und Kontraindikationen) der Europäischen Arzneimittel-Agentur bzw. des BfArM auswerten
- Detaillierte Wirkmechanismus-Daten ergänzen
- Präklinische Daten zur Rolle von IL-17RA bei Strongyloides-Infektionen prüfen
- Bewertung der Zulassungs- und Verfügbarkeitslage
- Gegebenenfalls alternative Kandidaten aus der Vorhersageliste mit besserer biologischer Plausibilität priorisieren

<!-- review:begin de-lic-20261106-brodalumab-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Bewertung der Zulassungs- und Verfügbarkeitslage (erloschene Zulassung)“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-brodalumab-1 -->

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „(erloschene Zulassung)“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Siliq (brodalumab) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a550c33-456a-4833-814e-8591aea7c688) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

