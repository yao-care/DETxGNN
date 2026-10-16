---
layout: default
title: Cobicistat
parent: Nur Modellvorhersage (L5)
nav_order: 121
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cobicistat: vorhergesagte neue Indikation Felines erworbenes Immundefizienz-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektionen"
---

# Cobicistat
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Cobicistat: Von HIV-Infektion zu felinem erworbenem Immundefizienz-Syndrom

## Zusammenfassung in einem Satz

Cobicistat ist ein pharmakokinetischer Verstärker (Booster), der ursprünglich zur Behandlung von HIV-Infektionen eingesetzt wurde. Das TxGNN-Modell sagt voraus, dass es bei **felinem erworbenem Immundefizienz-Syndrom** wirksam sein könnte. Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor, die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektionen |
| Vorhergesagte neue Indikation | Felines erworbenes Immundefizienz-Syndrom |
| TxGNN-Vorhersagewert | 99,92 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen |
| Anzahl der Zulassungen | 6 (alle erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten nicht vor. Nach allgemeinem Wissen ist Cobicistat ein mechanismusbasierter Hemmer von CYP3A. Es wird als pharmakokinetischer Verstärker für HIV-1-Proteasehemmer und Integrasehemmer (z. B. Atazanavir, Darunavir, Elvitegravir) eingesetzt. Cobicistat besitzt keine eigene antivirale Aktivität.

Das feline Immundefizienzvirus (FIV) ist ein mit HIV verwandtes Lentivirus. Die hohe Vorhersage spiegelt wahrscheinlich die Nähe der Krankheiten in der Krankheitsontologie wider, nicht einen belegten pharmakologischen Zusammenhang. Ein Nutzen setzte die gleichzeitige Gabe eines gegen FIV wirksamen antiretroviralen Partners voraus. Die FIV-Protease unterscheidet sich von der HIV-1-Protease in Substratspezifität und Inhibitorempfindlichkeit, eine Kreuzaktivität geboosteter HIV-Proteasehemmer ist daher ungewiss.

Zwei weitere Vorhersagen mit gleich hohem Score sind für die Einordnung relevant:
- **Simian-Immundefizienzvirus-Infektion** (Score 99,92 %): Hier gilt dieselbe Logik. SIV ist ein Tiermodell für HIV, also eher ein präklinischer Kontext als eine humantherapeutische Indikation.
- **Neuroentwicklungsstörung mit ataktischem Gang, fehlender Sprache und verminderter kortikaler weißer Substanz** (Score 99,91 %): Ein plausibler Mechanismus ist nicht erkennbar. Der hohe Score ist wahrscheinlich ein Artefakt des Wissensgraphen.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

Alle sechs Zulassungen sind erloschen (Status: cancelled). Es besteht aktuell keine gültige Zulassung.

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002572 | Tybost | – | HIV-Infektionen |
| EMEA/H/C/003904 | Evotaz | – | HIV-Infektionen |
| EMEA/H/C/002819 | Rezolsta | – | HIV-Infektionen |
| EMEA/H/C/002574 | Stribild | – | HIV-Infektionen |
| EMEA/H/C/004391 | Symtuza | – | HIV-Infektionen |

Eine sechste Zulassung (Genvoya, EMEA/H/C/004042) ist ebenfalls erloschen und aus Platzgründen nicht aufgeführt.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Die folgenden Beispiele stammen aus den ersten 20 Einträgen:
  - **Schwerwiegend (Major):** Loperamid, Triamcinolon, Cisaprid, Budesonid
  - **Moderat:** Hydrocortison, Aprepitant, Betamethason, Clotrimazol, Dexamethason (auch nasal/ophthalmisch), Dexfenfluramin, Fenfluramin, Metoclopramid, Prednisolon (ophthalmisch), Repaglinid, Hydrocortison (ophthalmisch), Budesonid (nasal), Clarithromycin
  - **Geringfügig (Minor):** Prucaloprid

  Die große Zahl an Wechselwirkungen ergibt sich aus der CYP3A-Hemmung.

Warnhinweise und Gegenanzeigen aus der Fachinformation liegen nicht vor. Bitte die Fachinformation konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (L5), ohne Studien oder Publikationen. Cobicistat hat keine eigene antivirale Wirkung, der Nutzen hinge vom Kombinationspartner ab, und in Deutschland besteht keine gültige Zulassung. Die FIV- und SIV-Indikationen sind zudem tiermedizinische bzw. präklinische Kontexte. Die Vorhersage zur Neuroentwicklungsstörung ist mechanistisch nicht nachvollziehbar.

**Für ein Weiterkommen wären erforderlich:**
- Daten zum Wirkmechanismus (MOA), z. B. aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM), da Voraussetzung für die Sicherheitsprüfung
- Präklinische Daten zur Aktivität geboosteter Proteasehemmer gegen FIV bzw. SIV
- Klärung, ob eine veterinärmedizinische Bewertung überhaupt im Rahmen dieser Prüfung liegt
- Eine Bewertung des Wechselwirkungsrisikos für den vorgesehenen Anwendungskontext
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

