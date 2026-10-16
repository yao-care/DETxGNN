---
layout: default
title: Maraviroc
parent: Nur Modellvorhersage (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Maraviroc: vorhergesagte neue Indikation Multiple endokrine Neoplasie (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektionen"
monitor_inn: "MARAVIROC"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

# Maraviroc: Von HIV-Infektion zu multipler endokriner Neoplasie

## Zusammenfassung

Maraviroc ist ein CCR5-Antagonist, der ursprünglich zur Behandlung von HIV-Infektionen zugelassen wurde. Das TxGNN-Modell sagt voraus, dass es bei **multipler endokriner Neoplasie** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf einer Modellberechnung.

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektionen |
| Vorhergesagte neue Indikation | Multiple endokrine Neoplasie |
| TxGNN-Vorhersagewert | 99,82 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene/gelöschte Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Maraviroc den Chemokinrezeptor CCR5 blockiert, was seine Wirkung bei HIV erklärt. Für eine Rolle von CCR5 in der Pathogenese der multiplen endokrinen Neoplasie gibt es in den vorliegenden Daten keinen Beleg.

Zwischen der ursprünglichen Indikation (Virusinfektion) und der vorhergesagten Indikation (hereditäre endokrine Tumorerkrankung) besteht keine erkennbare mechanistische Verbindung. Der sehr hohe Modellwert (0,998) ist daher mit Vorsicht zu interpretieren: Er ist ein rein rechnerisches Ergebnis ohne experimentelle oder klinische Bestätigung.

**Weitere vorhergesagte Indikationen (zur Einordnung):**

| Rang | Erkrankung | TxGNN-Wert | Evidenz | Anmerkung |
|---|---|---|---|---|
| 2 | Akne | 99,76 % | L5 | Spekulativ (CCR5-vermittelte Entzündung), keine Belege |
| 3 | Primäres kutanes T-Zell-Lymphom | 99,72 % | L5 | Plausible Rolle von Chemokinrezeptoren beim T-Zell-Homing; nur ein allgemeiner Übersichtsartikel |
| 4 | Pädiatrischer systemischer Lupus erythematodes | 99,71 % | L5 | Nur Modellvorhersage |
| 5 | Primäres kutanes T-Zell-Non-Hodgkin-Lymphom | 99,50 % | L5 | Gleiche Evidenz wie Rang 3 |
| 6 | Primäres kutanes B-Zell-Lymphom | 99,38 % | L5 | Nur Modellvorhersage |
| 7 | Candidiasis | 99,28 % | L5 | Kein antimykotischer Mechanismus erkennbar |
| 8 | Komplement-C4A-Mangel | 99,24 % | L5 | Kein plausibler Mechanismus |
| 9 | Zytomegalievirus-Infektion | 99,23 % | L4 | Nur indirekte Evidenz aus einer HIV-Kohortenstudie |
| 10 | HER2-positives Mammakarzinom | 99,22 % | L4 | Präklinischer Hinweis: CCL5/CCR5 und Trastuzumab-Resistenz |

Am plausibelsten erscheint mechanistisch das HER2-positive Mammakarzinom: Eine präklinische Studie zeigt, dass autokrines CCL5 über den ERK-Signalweg zur Trastuzumab-Resistenz beiträgt. Da CCL5 über CCR5 signalisiert, wäre eine CCR5-Blockade durch Maraviroc denkbar. Klinische Wirksamkeit ist damit nicht belegt.

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Literaturevidenz

Für die Hauptvorhersage (multiple endokrine Neoplasie) liegt keine Literatur vor. Für die weiteren Vorhersagen gibt es nur wenige, überwiegend indirekte Publikationen:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Präklinische/mechanistische Studie | Molecular Cancer Therapeutics | Autokrines CCL5 vermittelt Trastuzumab-Resistenz über ERK-Aktivierung beim HER2-positiven Mammakarzinom (relevant für Rang 10) |
| [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/) | 2023 | Review | Frontiers in Immunology | Übersicht zur Zielstruktur ACKR1 bei Krebs und anderen Erkrankungen; kein maravirocspezifischer Beleg (Rang 3 und 5) |
| [25397464](https://pubmed.ncbi.nlm.nih.gov/25397464/) | 2014 | Kohortenstudie | Journal of the International AIDS Society | Angeborene Immunität und lösliche Marker bei HIV-Patienten unter ART; nur indirekte Evidenz (Rang 9) |
| [21671545](https://pubmed.ncbi.nlm.nih.gov/21671545/) | 2011 | Review | American Family Physician | Häufige Nebenwirkungen der antiretroviralen Therapie; keine Evidenz für Maraviroc bei Candidiasis (Rang 7) |

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000811 | Celsentri | – | HIV-Infektionen |

Die einzige Zulassung (ViiV Healthcare B.V.) ist erloschen bzw. gelöscht; es gibt derzeit keine gültige Zulassung.

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (nicht aus dem Beipackzettel):** Im TxGNN-Wissensgraphen (PrimeKG) sind unter anderem folgende Erkrankungen als Kontraindikationen hinterlegt: Multisystematrophie, posturales orthostatisches Tachykardiesyndrom, orthostatische Hypotonie, Nierenerkrankung (einschließlich chronischer Niereninsuffizienz und terminalem Nierenversagen), Lebererkrankung (einschließlich arzneimittelinduzierter Leberschädigung), Gallenblasenerkrankung, chronische Hepatitis-B- und Hepatitis-C-Infektion, koronare Herzkrankheit, Myokardinfarkt, Myokardischämie, Koronarthrombose, Hämoglobinopathie sowie Pyoureter und Infektionskrankheiten.
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 93 Wechselwirkungen identifiziert. Als **schwerwiegend (Major)** gilt die Kombination mit **Clarithromycin**. Beispiele für Wechselwirkungen mit **mittlerem (Moderate)** Schweregrad: Aprepitant, Dexamethason, Cimetidin, Eliglustat, Naltrexon, Mannitol, Clotrimazol, Miconazol, Papaverin, Rolapitant, Troglitazon, Cobicistat, Deferasirox, Diazoxid, Phentolamin, Promethazin, Amylnitrit, Epoprostenol und Fostamatinib.

Angaben aus der Fachinformation zu Warnhinweisen und Gegenanzeigen liegen nicht vor. Bitte die Fachinformation ergänzend heranziehen.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für die multiple endokrine Neoplasie beruht ausschließlich auf einem Modellwert (Evidenzniveau L5), ohne Studien, Literatur oder erkennbaren Mechanismus. Zudem ist in Deutschland keine gültige Zulassung vorhanden, und die Sicherheitsdaten der Fachinformation fehlen. Das HER2-positive Mammakarzinom könnte als Forschungsfrage weiterverfolgt werden (präklinische Hinweise, L4).

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Fachinformation (Warnhinweise, Gegenanzeigen) beschaffen und auswerten, da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Daten zum Wirkmechanismus ergänzen (z. B. aus DrugBank)
- Prüfung einer mechanistischen Verbindung zwischen CCR5 und multipler endokriner Neoplasie in der Literatur
- Für das HER2-positive Mammakarzinom: weitere präklinische Studien zur CCR5-Blockade bei Trastuzumab-Resistenz
- Klärung der regulatorischen Situation, da die deutsche Zulassung erloschen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

