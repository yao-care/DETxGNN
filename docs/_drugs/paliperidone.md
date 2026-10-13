---
layout: default
title: Paliperidone
parent: Nur Modellvorhersage (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidon: Von Schizophrenie zu retinaler Dystrophie (mit oder ohne extraokulare Anomalien)

## Zusammenfassung

Paliperidon wurde ursprünglich zur Behandlung von Schizophrenie und psychotischen Störungen zugelassen. Das TxGNN-Modell sagt für den Spitzenrang eine Wirksamkeit bei **retinaler Dystrophie mit oder ohne extraokulare Anomalien** voraus, jedoch gibt es dafür **keine klinischen Studien und keine Publikationen**. Die Vorhersage beruht ausschließlich auf dem Modell (Evidenzstufe L5).

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Schizophrenie; psychotische Störungen |
| Vorhergesagte neue Indikation | Retinale Dystrophie mit oder ohne extraokulare Anomalien |
| TxGNN-Vorhersagewert | 99,92 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Detaillierte Daten zum Wirkmechanismus liegen derzeit nicht vor. Bekannt ist, dass Paliperidon ein Antagonist an Dopamin-D2- und Serotonin-5-HT2A-Rezeptoren ist und als Antipsychotikum bei Schizophrenie eingesetzt wird.

Ein plausibler Wirkweg von dieser Rezeptorblockade zu erblich bedingter Netzhautdegeneration ist anhand der vorliegenden Daten nicht erkennbar. Der hohe Vorhersagewert (0,999) ist eine reine Modellvorhersage und kein Hinweis auf klinische Wirksamkeit. Die Ähnlichkeit zur ursprünglichen Indikation wurde bislang nicht bewertet.

Auch die weiteren Top-Vorhersagen wirken mechanistisch wenig überzeugend: mehrere Myopie-Formen (X-chromosomal, syndromisch), strukturelle Hirnfehlbildungen (Hydranenzephalie, Polymikrogyrie), eine Glykosylierungsstörung, eine demyelinisierende Neuropathie (Charcot-Marie-Tooth Typ 1G) und die atypische Glycin-Enzephalopathie. Bei Myopie könnte eine D2-Blockade sogar nachteilig sein, da retinales Dopamin als schützend gegen das Fortschreiten der Myopie gilt.

Die einzige inhaltlich nahe Vorhersage ist die **therapierefraktäre Schizophrenie** (Rang 10, Score 99,80 %). Sie ist praktisch eine Erweiterung der zugelassenen Population und kein echtes Repurposing. Clozapin bleibt hier der Standard.

---

## Klinische Evidenz

Für die Hauptvorhersage (retinale Dystrophie) sind derzeit keine relevanten klinischen Studien registriert.

Der Vollständigkeit halber die Studien zur naheliegendsten Vorhersage, therapierefraktäre Schizophrenie:

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unbekannt | 244 | Randomisierter, offener Vergleich von Aripiprazol vs. Paliperidon mit Multi-Omics-Daten bei Erstepisode-Psychose |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Aktiv, nicht rekrutierend | 84 | Pharmakotherapie plus zwei recovery-orientierte Programme bei therapieresistenter Schizophrenie bzw. bipolarer Störung; Beitrag von Paliperidon unklar |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Abgebrochen | 5 | Explorative Analyse von Immun- und Entzündungsreaktionen unter Clozapin vs. Nicht-Clozapin-Antipsychotika; wegen 5 Teilnehmern kaum aussagekräftig |

Keine dieser Studien prüft Paliperidon als primäre Intervention in einer therapierefraktären Population.

---

## Literaturevidenz

Für die Hauptvorhersage liegen derzeit keine relevanten Publikationen vor.

Zur therapierefraktären Schizophrenie (indirekte Evidenz):

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Übersicht zur Psychopharmakologie der schizoaffektiven Störung; Behandlung beruht hauptsächlich auf Antipsychotika, spezifische Leitlinien fehlen |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Wirksamkeit und Verträglichkeit psychosozialer und psychopharmakologischer Interventionen bei früh beginnender Schizophrenie |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000746 | Invega | – | Schizophrenie; psychotische Störungen (Status: erloschen) |

Es besteht derzeit keine gültige Zulassung in Deutschland.

---

## Sicherheitsaspekte

**Kontraindikationen/Risikokonstellationen aus der Wissensdatenbank** (Kontraindikationsbeziehungen im TxGNN-Wissensgraphen, nicht aus dem Beipackzettel):
- Herz-Kreislauf: Long-QT-Syndrom (auch familiär), Torsades de pointes, Myokardinfarkt, Koronarthrombose, orthostatische Hypotonie, Hypotonie, posturales orthostatisches Tachykardiesyndrom, Multisystematrophie
- Neurologisch: Epilepsie, Erkrankungen der Basalganglien, fokale Handdystonie, Blepharospasmus
- Stoffwechsel: Diabetes mellitus, Hyperglykämie, diabetische Ketoazidose, Hyperlipidämie (auch familiär), Adipositas (auch monogen), Kaliummangel
- Blut: Neutropenie, Agranulozytose, Hämoglobinopathie
- Weitere: Morbus Crohn, chronisch-entzündliche Darmerkrankungen, Crohn-Kolitis, Nierenfunktionsstörung, Mammakarzinom bei Frauen

**Arzneimittelwechselwirkungen** (100 Einträge insgesamt, Auswahl):
- **Schwerwiegend (Major):** Bupropion, Morphin
- **Moderat:** u. a. Acarbose, Metformin, Pioglitazon, Canagliflozin, Chlorpropamid, Albiglutid, Alogliptin (Antidiabetika); Famotidin; Epinephrin; Hydrocortison; Amphotericin B; Hyoscyamin, Atropin, Glycopyrronium (Anticholinergika); Loperamid; Bisacodyl; Lorcaserin

Hinweise und Gegenanzeigen aus der Fachinformation liegen nicht vor; bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage zur retinalen Dystrophie beruht allein auf einem Modellwert ohne Studien, Publikationen oder plausiblen Wirkmechanismus. Auch die übrigen Top-Vorhersagen sind mechanistisch kaum nachvollziehbar. Die einzige naheliegende Indikation (therapierefraktäre Schizophrenie) ist eine Erweiterung der Zulassungspopulation, für die keine Studie Paliperidon als Hauptprüfpräparat untersucht.

**Für ein Weiterkommen wären erforderlich:**
- Daten zum Wirkmechanismus (aktuell nicht verfügbar) sowie eine Prüfung der mechanistischen Verbindung zur Netzhaut
- Präklinische Untersuchungen zur Plausibilität der Vorhersage
- Fachinformation mit Warnhinweisen und Gegenanzeigen (derzeit blockierende Datenlücke für die Sicherheitsprüfung)
- Für therapierefraktäre Schizophrenie: direkte Studien mit Paliperidon als Prüfpräparat im Vergleich zu Clozapin
- Klärung des Zulassungsstatus in Deutschland, da die einzige Zulassung erloschen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

