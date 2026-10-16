---
layout: default
title: Etravirine
parent: Nur Modellvorhersage (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etravirine: vorhergesagte neue Indikation Felines erworbenes Immundefizienz-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: HIV-Infektionen"
---

# Etravirine
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

# Etravirin: Von HIV-Infektion zu felinem erworbenem Immundefizienz-Syndrom

## Zusammenfassung

Etravirin ist ein nicht-nukleosidischer Reverse-Transkriptase-Inhibitor (NNRTI), der ursprünglich zur Behandlung der HIV-Infektion zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **felinem erworbenem Immundefizienz-Syndrom** wirksam sein könnte. Hierfür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektionen |
| Vorhergesagte neue Indikation | Felines erworbenes Immundefizienz-Syndrom |
| TxGNN-Vorhersagewert | 99,98 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Etravirin ein NNRTI der HIV-1-Reverse-Transkriptase ist und dass seine Wirksamkeit bei HIV-Infektionen belegt ist.

Das feline Immundefizienzvirus (FIV) ist ein mit HIV verwandtes Lentivirus. Seine Reverse Transkriptase ist jedoch in der Regel weniger empfindlich gegenüber NNRTIs, sodass eine artübergreifende Wirkung unsicher ist. Der hohe TxGNN-Wert spiegelt vermutlich die Nähe zu HIV-bezogenen Krankheitsknoten im Wissensgraphen wider und keine nachgewiesene Aktivität.

**Weitere Vorhersagen im Überblick:**

| Rang | Vorhergesagte Indikation | Wert | Evidenz | Einschätzung |
|---|---|---|---|---|
| 2 | Infektion mit dem Simianen Immundefizienzvirus | 99,98 % | L5 | SIV ist wie HIV-2 von Natur aus gegen viele NNRTIs resistent; die einzige Publikation ist indirekt und präklinisch. |
| 3 | Neuroentwicklungsstörung mit ataktischem Gang, fehlender Sprache und verminderter kortikaler weißer Substanz | 99,97 % | L5 | Kein plausibler Mechanismus; vermutlich ein Artefakt des Graphen. |
| 4 | AIDS-related Complex | 99,79 % | L4 | Überschneidet sich mit der zugelassenen HIV-Indikation, daher kein echtes Repurposing. |
| 5 | Kongenitale HIV-Infektion | 99,79 % | L4 | Mechanistisch direkt relevant, aber ebenfalls überlappend mit der HIV-Indikation. |
| 6–10 | Gutartige Tumoren (Prostatafibrom, Brenner-Tumor, gutartige Neoplasie des Reproduktionssystems, benigner Phylloides-Tumor der Prostata) sowie veraltete familiäre kombinierte Hyperlipidämie | 99,64–99,72 % | L5 | Weder Mechanismus noch Evidenz erkennbar. |

Insgesamt sind die Vorhersagen mit HIV-Bezug (Rang 4 und 5) mechanistisch am plausibelsten, stellen aber kaum neue Indikationen dar. Die übrigen Vorhersagen sind überwiegend modellbedingt.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für die Hauptvorhersage (felines erworbenes Immundefizienz-Syndrom) liegt keine Literatur vor. Für die weiteren Vorhersagen wurden folgende Arbeiten gefunden, die jeweils nur indirekten Kontext liefern:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Präklinisch/In vitro | Molecular Pharmaceutics | Nanopartikelbasierte ARV-Kombinationen hemmen die zellfreie und zellvermittelte HIV-Übertragung synergistisch (Bezug zu SIV nur indirekt). |
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Fallserie | Antiviral Therapy | Bericht über zwei Fälle mit Darunavir und Etravirin, mit oder ohne Raltegravir, in der Schwangerschaft. |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Kohortenstudie | AIDS Reviews | Risikofaktoren für gastrointestinale Nebenwirkungen bei behandelten und unbehandelten HIV-Patienten. |
| [27067022](https://pubmed.ncbi.nlm.nih.gov/27067022/) | 2016 | Präklinisch/In vitro | AIDS Research and Human Retroviruses | Neue Mutationen L228I und Y232H in der Reversen Transkriptase führen in Kombination zu NNRTI-Resistenz. |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000900 | Intelence | – | HIV-Infektionen |

Diese einzige Zulassung (Janssen-Cilag International NV) ist erloschen; derzeit gibt es keine gültige Zulassung in den zusammengestellten Daten.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (Krankheits-Wirkstoff-Beziehungen aus PrimeKG, kein Packungsbeilagentext): chronische Hepatitis-C-Virus-Infektion, Hepatitis-C-Virus-Infektion, chronische Hepatitis-B-Virus-Infektion, Erkrankung des peripheren Nervensystems, periphere Neuropathie.
- **Arzneimittelwechselwirkungen**: Insgesamt wurden 100 Wechselwirkungen erfasst, 20 davon liegen vor. Davon ist eine leicht (Ranitidin), die übrigen sind mittelschwer. Zu den genannten Wirkstoffen zählen:
  - Protonenpumpenhemmer und H2-Blocker: Rabeprazol, Omeprazol, Cimetidin
  - Kortikosteroide: Hydrocortison, Dexamethason, Betamethason, Triamcinolon
  - Antidiabetika: Pioglitazon, Saxagliptin, Linagliptin, Glimepirid, Chlorpropamid
  - Weitere: Aprepitant, Clarithromycin, Metronidazol, Dronabinol, Eliglustat, Naldemedin, Naloxegol

Für Warnhinweise und Gegenanzeigen der Fachinformation sind keine Daten verfügbar. Bitte die Packungsbeilage bzw. Fachinformation konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Hauptvorhersage (felines Immundefizienz-Syndrom) beruht ausschließlich auf dem Modell (L5), ohne Studien oder Literatur, und die Empfindlichkeit von FIV gegenüber NNRTIs ist fraglich. Zudem besteht in Deutschland keine gültige Zulassung. Die HIV-nahen Vorhersagen (AIDS-related Complex, kongenitale HIV-Infektion) überschneiden sich mit der bereits zugelassenen Indikation, und die übrigen Vorhersagen entbehren jeder mechanistischen Grundlage.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Daten zum Wirkmechanismus (MOA)
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM), da dies die Sicherheitsprüfung derzeit blockiert
- In-vitro-Studien zur Empfindlichkeit der FIV- und SIV-Reversen-Transkriptase gegenüber Etravirin
- Klärung des aktuellen Zulassungsstatus in Deutschland und der verfügbaren Darreichungsformen
- Bei Interesse an der kongenitalen HIV-Infektion: gezielte Daten zu Sicherheit und Pharmakokinetik in Schwangerschaft und Neugeborenen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

