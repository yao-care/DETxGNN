---
layout: default
title: Tipranavir
parent: Nur Modellvorhersage (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tipranavir: vorhergesagte neue Indikation Felines erworbenes Immundefizienz-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektionen"
---

# Tipranavir
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

# Tipranavir: Von HIV-Infektion zu felinem erworbenem Immundefizienz-Syndrom

## Zusammenfassung in einem Satz

Tipranavir ist ein Proteaseinhibitor, der ursprünglich zur Behandlung von HIV-Infektionen zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **felinem erworbenem Immundefizienz-Syndrom** (einer Tierkrankheit) wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektionen |
| Vorhergesagte neue Indikation | Felines erworbenes Immundefizienz-Syndrom |
| TxGNN-Vorhersagewert | 99,99 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 aufgehoben) |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage nachvollziehbar?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Tipranavir ein nicht-peptidischer Inhibitor der HIV-1-Protease ist. Seine Wirksamkeit bei HIV-Infektionen war Grundlage der Zulassung.

Das Feline Immundefizienzvirus (FIV) ist ein Lentivirus mit einer Protease, die der HIV-1-Protease strukturell verwandt ist. Ein mechanistischer Ansatz ist daher denkbar. Allerdings unterscheiden sich Substratspezifität und Inhibitor-Empfindlichkeit der FIV-Protease, und es liegen keine belegenden Daten vor. Der hohe TxGNN-Wert spiegelt sehr wahrscheinlich die Nähe zu HIV-bezogenen Knoten im Wissensgraphen wider.

Wichtig: Es handelt sich um eine veterinärmedizinische Indikation, die für die Arzneimittelneuausrichtung beim Menschen nicht relevant ist. Auch die weiteren Vorhersagen sind überwiegend wenig plausibel:

- **Simian-Immundefizienzvirus-Infektion** (Rang 2): im Wesentlichen ein Tiermodell, nur als präklinisches Modell von Wert.
- **Kongenitale HIV-Infektion** und **AIDS-related complex** (Rang 5 und 6): Varianten der bereits zugelassenen Indikation, daher keine echte Neuausrichtung.
- **Obsolete familiäre kombinierte Hyperlipidämie** (Rang 4): Tipranavir/Ritonavir erhöht bekanntermaßen Triglyceride und Cholesterin. Die Vorhersage dürfte ein Nebenwirkungssignal statt eines Therapieeffekts abbilden.
- **Neurologische Entwicklungsstörung, Prostatafibrom, Brenner-Tumor, gutartige Neoplasien des Reproduktionssystems, gutartiger Prostata-Phyllodes-Tumor** (Ränge 3 und 7–10): kein erkennbarer mechanistischer Zusammenhang, wahrscheinlich Artefakte des Graphen.

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Evidenz aus der Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000631 | Aptivus | – | HIV-Infektionen |

Die einzige Zulassung (Boehringer Ingelheim International GmbH) ist aufgehoben.

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (TxGNN/PrimeKG, nicht aus dem Beipackzettel): Leberversagen, Lebererkrankung, Gallenblasenerkrankung, Hyperglykämie, Diabetes mellitus, diabetische Ketoazidose, chronische Hepatitis C und B, Hepatitis C, Hepatitis, Blutgerinnungsstörungen, Hämophilie (einschließlich symptomatischer Form bei weiblichen Trägerinnen), Hypertriglyceridämie, Hyperbilirubinämie (auch hereditär), Gilbert-Syndrom, Verletzungen, Hirntumor/Hirnneoplasma und intrakranielle Blutungen.
- **Arzneimittelwechselwirkungen** (100 Einträge gefunden, Auswahl):
  - **Schwerwiegend:** Acetylsalicylsäure, Eluxadolin.
  - **Moderat:** Antidiabetika (Acarbose, Albiglutid, Alogliptin, Metformin, Pioglitazon, Canagliflozin, Chlorpropamid, Dapagliflozin, Dulaglutid, Empagliflozin, Linagliptin), außerdem Loperamid, Dexamethason, Cholsäure, Clarithromycin, Magnesiumoxid, Eliglustat und topisches Metronidazol.

Warnhinweise und Gegenanzeigen aus der Fachinformation liegen nicht vor. Bitte hierzu die Fachinformation heranziehen.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die vorhergesagte Indikation gibt es weder klinische Studien noch Literatur (Evidenzlevel L5). Die Indikation ist veterinärmedizinisch, und die Zulassung in Deutschland ist aufgehoben. Die übrigen Vorhersagen sind entweder Varianten der bestehenden HIV-Indikation oder mechanistisch nicht plausibel.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) aus BfArM-Quellen, da dies derzeit ein blockierendes Datenelement für die Sicherheitsprüfung ist
- Detaillierte Daten zum Wirkmechanismus
- Präklinische Daten zur Aktivität gegen die FIV-/SIV-Protease, falls die Tiermodell-Richtung weiterverfolgt werden soll
- Prüfung, ob eine Neuausrichtung beim Menschen überhaupt sinnvoll ist, auch angesichts der Stoffwechsel- und Leberrisiken sowie des Nebenwirkungssignals bei Blutfetten
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

