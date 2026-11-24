---
layout: default
title: Fenofibrate
parent: Nur Modellvorhersage (L5)
nav_order: 193
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Fenofibrate: vorhergesagte neue Indikation Cholesterinester-Transferprotein-Mangel (Evidenzstufe L5). Ursprüngliche Indikation: Dyslipidämien"
---

# Fenofibrate
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

## Fenofibrat: Von Dyslipidämien zu Cholesterinester-Transferprotein-Mangel
{: .text-alpha }

## Zusammenfassung

Fenofibrat wird ursprünglich zur Behandlung von Dyslipidämien eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei **Cholesterinester-Transferprotein-Mangel (CETP-Mangel)** wirksam sein könnte. Dafür liegen **keine klinischen Studien** und **3 Publikationen** (ausschließlich präklinisch bzw. mechanistisch) vor.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Dyslipidämien |
| Vorhergesagte neue Indikation | Cholesterinester-Transferprotein-Mangel |
| TxGNN-Vorhersagewert | 0,9961 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl der Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Fenofibrate (inoffizielle Übersetzung): „Der wirksame Bestandteil von Antara ist Fenofibrinsäure. Die pharmakologischen Wirkungen der Fenofibrinsäure wurden sowohl bei Tieren als auch beim Menschen nach oraler Gabe von Fenofibrat untersucht. Die in der klinischen Praxis beobachteten lipidmodifizierenden Wirkungen der Fenofibrinsäure wurden in vivo an transgenen Mäusen und in vitro an humanen Hepatozytenkulturen durch die Aktivierung des PPAR-alpha-Rezeptors erklärt.“ Englischer Originalwortlaut: "The active moiety of Antara is fenofibric acid. The pharmacological effects of fenofibric acid in both animals and humans have been studied through oral administration of fenofibrate. The lipid-modifying effects of fenofibric acid seen in clinical practice have been explained in vivo in transgenic mice and in vitro in human hepatocyte cultures by the activation of PPAR alpha receptor." ([DailyMed: Antara (fenofibrate) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=24790a18-0291-4b88-a724-acac43b616ce), Fassung vom 2025-10-01; abgerufen am 2026-11-19). Bekannt aus den ausgewerteten Publikationen ist, dass Fenofibrat als PPARα-Agonist das HDL-Cholesterin erhöht und Triglyceride senkt. In Mäusen induziert es zudem die Expression des Phospholipid-Transferprotein-Gens (PLTP), was die Vergrößerung der HDL-Partikel erklärt (PMID 11342537).

Der Zusammenhang zwischen der ursprünglichen und der vorhergesagten Indikation ist nur indirekt: Beide betreffen den Lipoproteinstoffwechsel. Fenofibrat beeinflusst den Umbau von Lipoproteinen über einen verwandten Signalweg, behebt aber nicht den zugrunde liegenden genetischen CETP-Defekt. Eine Studie zur Kombination von CETP-Hemmung und PPARα-Agonismus (PMID 20332533) deutet auf additive Effekte beider Mechanismen hin, nicht darauf, dass Fenofibrat einen CETP-Mangel korrigiert.

Der sehr hohe TxGNN-Wert ist eine rechnerische Vorhersage und spiegelt wahrscheinlich die Nähe im Netzwerk des Lipidstoffwechsels wider, nicht eine therapeutische Begründung. Zudem ist der CETP-Mangel meist ein biochemischer Phänotyp mit erhöhtem HDL, und ein Behandlungsbedarf ist fraglich.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Präklinisch | J Cardiovasc Pharmacol Ther | An Mäusen mit humanem ApoB100/CETP: CETP-Hemmung (Torcetrapib) und PPARα-Agonismus (Fenofibrat) beeinflussen das Lipidprofil, HDL-Cholesterin steigt, LDL-Cholesterin sinkt |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Mechanistisch/präklinisch | J Biol Chem | Induktion des PLTP-Gens erklärt die HDL-Vergrößerung bei mit Fenofibrat behandelten Mäusen |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Mechanistisch/präklinisch | Front Physiol | Keine Korrelation von Plasma-HDL mit fäkaler Cholesterinausscheidung und Cholesterin-Efflux; Bedeutung der HDL-Funktion bei der Atheroskleroseminderung |

Keine dieser Arbeiten untersucht Fenofibrat direkt bei CETP-Mangel beim Menschen.

---

## Informationen zum Markt in Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/001243 | Pravafenix | fenofibrate; pravastatin | Dyslipidemias | Gültig |
| EMEA/H/C/002559 | Cholib | fenofibrate; simvastatin | Dyslipidemias | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

**Kontraindikationen/Risikoerkrankungen aus dem Wissensgraphen (keine Packungsbeilagen-Angaben):** Im Wissensgraphen sind unter anderem folgende Erkrankungen als Kontraindikationsbeziehungen hinterlegt: Leberversagen und Lebererkrankung, Pankreatitis, Gallenblasenerkrankung, Cholelithiasis, Thrombozytopenie, Myopathie und Rhabdomyolyse, Beeinträchtigung der Nierenfunktion, Anämie sowie Leukopenie, Neutropenie und Agranulozytose.

**Arzneimittelwechselwirkungen:** Insgesamt 100 Wechselwirkungen verzeichnet, die aufgeführten sind jeweils von moderatem Schweregrad:
- Sulfonylharnstoffe (Acetohexamid, Chlorpropamid, Glimepirid, Glipizid, Glyburid)
- Verschiedene Insuline (u. a. Humaninsulin, Insulin aspart, degludec, detemir, glargin, glulisin, lispro)
- Chenodeoxycholsäure
- Esomeprazol

Für Warnhinweise und Gegenanzeigen laut Fachinformation siehe die Packungsbeilage.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Es gibt keine Studie, die Fenofibrat direkt bei CETP-Mangel untersucht; die vorhandenen Arbeiten sind präklinisch und betreffen nur verwandte Mechanismen. Der Behandlungsbedarf beim CETP-Mangel ist zudem fraglich, sodass der hohe TxGNN-Wert allein keine Weiterverfolgung rechtfertigt.

**Für ein Weiterkommen sind erforderlich:**
- Klärung, ob beim CETP-Mangel überhaupt ein klinischer Behandlungsbedarf besteht
- Direkte präklinische oder klinische Daten zu Fenofibrat bei CETP-Mangel
- Daten zum Wirkmechanismus (MOA) von Fenofibrat
- Auswertung der Warnhinweise und Gegenanzeigen aus der Fachinformation des BfArM

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Antara (fenofibrate) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=24790a18-0291-4b88-a724-acac43b616ce) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

