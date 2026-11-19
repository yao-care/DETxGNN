---
layout: default
title: Sevoflurane
parent: Nur Modellvorhersage (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "SEVOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
description: "Sevoflurane: vorhergesagte neue Indikation Prinzmetal-Angina (Prinzmetal angina) (Evidenzstufe L5). Keine zentrale EU-Zulassung (EMA) erfasst"
---

# Sevoflurane
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

## Sevoflurane: Prinzmetal-Angina (Prinzmetal angina)
{: .text-alpha }

## Zusammenfassung in einem Satz

Sevofluran ist ein inhalatives Narkosemittel (volatiles Anästhetikum), das für die Allgemeinanästhesie eingesetzt wird. Das TxGNN-Modell sagt voraus, dass es bei **Prinzmetal-Angina** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, sie beruht ausschließlich auf der Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | In den lokalen Daten nicht erfasst |
| Vorhergesagte neue Indikation | Prinzmetal-Angina (Prinzmetal angina) |
| TxGNN-Vorhersagewert | 0.9978 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Keine zentrale EU-Zulassung (EMA) erfasst – nationale Zulassungen (BfArM) sind in den hier ausgewerteten Daten nicht enthalten |
| Anzahl der Zulassungen | 0 (gültig: 0) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut ChEMBL (EMBL-EBI) ist für Sevoflurane folgender Wirkmechanismus erfasst (inoffizielle Übersetzung): „Positiver Modulator des Glycinrezeptors (alpha-1/beta); GABA-A-Rezeptor; positiver allosterischer Modulator von Anionenkanälen; Öffner des Kaliumkanals Unterfamilie K Mitglied 10; Öffner des Kaliumkanals Unterfamilie K Mitglied 18“ Englischer Originalwortlaut: "Glycine receptor (alpha-1/beta) positive modulator; GABA-A receptor; anion channel positive allosteric modulator; Potassium channel subfamily K member 10 opener; Potassium channel subfamily K member 18 opener" ([ChEMBL CHEMBL1200694 (sevoflurane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200694), CC BY-SA 3.0; abgerufen am 2026-11-19). Bekannt ist, dass Sevofluran als volatiles Anästhetikum unter anderem GABA-A- und NMDA-Rezeptoren moduliert und gewisse gefäßerweiternde sowie calciumkanalmodulierende Effekte besitzt.

Theoretisch könnten diese vasodilatierenden Eigenschaften mit dem Koronarspasmus bei Prinzmetal-Angina zusammenhängen. Dieser Zusammenhang ist jedoch rein spekulativ und durch keine Studie oder Publikation belegt. Zudem ist ein inhalatives Narkosemittel für die Dauerbehandlung einer vasospastischen Erkrankung nicht geeignet. Die hohe Modellbewertung ist daher mit Vorsicht zu interpretieren.

Weitere Vorhersagen des Modells (jeweils mit Evidenzlevel L4–L5 und Empfehlung „Hold“) betreffen unter anderem das Tourette-Syndrom, Fibromyalgie, Tendinitis, Migräne und die Einschlusskörperchenmyositis. Bei den Vorhersagen mit Literatur handelt es sich ausschließlich um Berichte zur Anästhesieführung, nicht um Therapiestudien.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Zur Prinzmetal-Angina liegen derzeit keine zugehörigen Publikationen vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|

---

## Sicherheitsaspekte

**Kontraindikationen laut Wissensgraph (PrimeKG, nicht aus dem Beipackzettel):** Epilepsie, Nierenerkrankung, Pyoureter, Lebererkrankung, Gallenblasenerkrankung, hypotensive Störung, maligne Hyperthermie bei Anästhesie, belastungsinduzierte maligne Hyperthermie, Pseudotumor cerebri, intrakranielle Hypertonie, Duchenne-Muskeldystrophie, Muskeldystrophie, Becker-Muskeldystrophie, Proteinurie.

**Arzneimittelwechselwirkungen:** Es wurden 100 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft sind:
- Epinephrin
- Dolasetron
- Cisaprid

Zahlreiche weitere Wechselwirkungen sind als moderat eingestuft (z. B. Morphin, Ondansetron, Palonosetron, Clarithromycin, Levofloxacin, Famotidin, Exenatid, Loperamid sowie verschiedene Abführmittel), Metronidazol als geringfügig.

Warnhinweise und Kontraindikationen aus der Fachinformation liegen nicht vor. Bitte die Fachinformation zu den Sicherheitsangaben heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage zur Prinzmetal-Angina beruht allein auf dem Modell (L5) ohne Studien oder Literatur. Zudem ist ein inhalatives Narkosemittel für eine chronische vasospastische Erkrankung pharmakologisch und praktisch kaum geeignet.

**Für ein Weiterkommen erforderlich:**
- Fachinformation (Warnhinweise, Kontraindikationen) der Zulassungsbehörde auswerten; diese Lücke blockiert die Sicherheitsprüfung
- Detaillierte Wirkmechanismus-Daten (MOA) ergänzen
- Präklinische Belege zu einem Effekt auf Koronarspasmen
- Prüfung der Anwendbarkeit des Applikationswegs (Inhalation) für die Zielindikation

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [ChEMBL CHEMBL1200694 (sevoflurane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200694) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

