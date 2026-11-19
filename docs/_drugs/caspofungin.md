---
layout: default
title: Caspofungin
parent: Nur Modellvorhersage (L5)
nav_order: 102
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Caspofungin: vorhergesagte neue Indikation Gastrin-Sekretionsstörung (Evidenzstufe L5). Ursprüngliche Indikation: Candidiasis"
monitor_inn: "CASPOFUNGIN"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Caspofungin: Von Candidiasis/Aspergillose zu Gastrin-Sekretionsstörung
{: .text-alpha }

## Zusammenfassung in einem Satz

Caspofungin ist ein Antimykotikum aus der Klasse der Echinocandine und wurde ursprünglich zur Behandlung von Candidiasis und Aspergillose zugelassen. Das TxGNN-Modell sagt voraus, dass es bei einer **Gastrin-Sekretionsstörung** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, sie beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Candidiasis; Aspergillose |
| Vorhergesagte neue Indikation | Gastrin-Sekretionsstörung |
| TxGNN-Vorhersagewert | 0,9944 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut den Abschnitten „Mechanism of Action“ und „Microbiology“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Caspofungin (inoffizielle Übersetzung): „Caspofungin ist ein antimykotisches Arzneimittel aus der Klasse der Echinocandine. […] Caspofungin, ein Echinocandin, hemmt die Synthese von Beta-(1,3)-D-Glucan, einem essenziellen Bestandteil der Zellwand empfindlicher Aspergillus-Arten und Candida-Arten. Beta-(1,3)-D-Glucan ist in Säugetierzellen nicht vorhanden.“ Englischer Originalwortlaut: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), Fassung vom 2024-10-11; abgerufen am 2026-11-19). Nach allgemeinem Wissen gehört Caspofungin zu den Echinocandinen und hemmt die β-(1,3)-D-Glucan-Synthase der Pilzzellwand. Seine Wirksamkeit bei Candidiasis und Aspergillose ist belegt.

Für die vorhergesagte Indikation besteht jedoch **kein bekannter mechanistischer Zusammenhang**. Der gastrinbildende Signalweg (G-Zellen, CCK2-Rezeptor, Regulation der Magensäure) besitzt kein bekanntes Glucan-Synthase-Ziel. Der sehr hohe Vorhersagewert (0,9944) stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, keinen biologischen Beleg. Ohne verifizierten Mechanismus lässt sich die Vorhersage biologisch nicht interpretieren.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000379 | Cancidas (zuvor Caspofungin MSD) | – | Candidiasis; Aspergillose |

Hinweis: Für dieses Arzneimittel liegt in den zusammengestellten Daten 1 gültige Zulassung von insgesamt 1 vor; es ist im Handel.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (Wirkstoff-Erkrankungs-Beziehungen aus PrimeKG, kein Packungsbeilagentext): Lebererkrankung, Gallenblasenerkrankung, Kaliummangel.
- **Arzneimittelwechselwirkungen**: Insgesamt wurden 81 Wechselwirkungen erfasst. Die wichtigsten:
  - **Schwerwiegend (Major)**: Dexamethason
  - **Mittelschwer (Moderate)**: Naltrexon
  - Weitere Wechselwirkungen mit nicht eingestuftem Schweregrad, u. a. Amphotericin B, Vancomycin, Prednison, Prednisolon, Hydrocortison, Simvastatin, Omeprazol, Pantoprazol, Lansoprazol und Kaliumchlorid.

Für Warnhinweise und Gegenanzeigen aus der Packungsbeilage wird auf die Fachinformation verwiesen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf dem TxGNN-Modell (Deep Learning) (Evidenzgrad L5), ohne klinische Studien, ohne Literatur und ohne plausiblen Wirkmechanismus. Das Arzneimittel ist in Deutschland mit 1 gültigen Zulassung im Handel.

**Für ein Weiterkommen sind erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der BfArM-Packungsbeilage (derzeit eine Lücke, die die Sicherheitsprüfung blockiert)
- Eine Prüfung, ob ein biologisch begründeter Zusammenhang zwischen β-Glucan-Synthase-Hemmung und Gastrin-Regulation besteht, z. B. durch präklinische Studien
- Klärung der Darreichungsformen und Applikationswege (derzeit offen)
- Klärung des Zulassungs- bzw. Vermarktungsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

