---
layout: default
title: Lapatinib
parent: Nur Modellvorhersage (L5)
nav_order: 258
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Lapatinib: vorhergesagte neue Indikation Dermatofibrosarcoma protuberans (Evidenzstufe L5). Ursprüngliche Indikation: Brustkrebs (Breast Neoplasms)"
monitor_inn: "LAPATINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Lapatinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Lapatinib: Von Brustkrebs zu Dermatofibrosarcoma protuberans

## Zusammenfassung

Lapatinib wurde ursprünglich zur Behandlung von Brustkrebs (Mammakarzinom) eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei **Dermatofibrosarcoma protuberans (DFSP)** wirksam sein könnte. Für diese Vorhersage liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf der Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Brustkrebs (Breast Neoplasms) |
| Vorhergesagte neue Indikation | Dermatofibrosarcoma protuberans |
| TxGNN-Vorhersagewert | 99,30 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Lapatinib ist ein dualer Tyrosinkinase-Inhibitor, der den EGFR (ErbB1) und HER2 (ErbB2) hemmt. Detaillierte Mechanismusdaten (MOA) liegen in den für diesen Bericht zusammengestellten Daten derzeit nicht vor. Die Wirksamkeit bei HER2-positivem Brustkrebs ist bekannt.

DFSP wird hauptsächlich durch das COL1A1-PDGFB-Fusionsgen getrieben, das zu einer dauerhaften Aktivierung von PDGFRB führt. Die übliche Behandlung besteht aus chirurgischer Entfernung und Imatinib, einem PDGFR-Inhibitor. Ein denkbarer Zusammenhang wäre die gemeinsame Rezeptor-Tyrosinkinase-Signalübertragung (nachgeschaltete PI3K/AKT- und MAPK-Signalwege). Dies ist jedoch spekulativ: Lapatinib wirkt nicht direkt auf PDGFR.

Der hohe Vorhersagewert spiegelt möglicherweise die Nähe zu anderen Kinase-Inhibitoren im Wissensgraphen wider und nicht eine biologische Grundlage speziell für Lapatinib. Die Begründung wird durch die vorliegenden Daten nicht gestützt.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000795 | Tyverb | – | Breast Neoplasms (Brustkrebs); Status: erloschen |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (Tyrosinkinase-Inhibitor, EGFR/HER2) |
| Myelosuppressionsrisiko | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenitätsklasse | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Handhabungsschutz | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |

---

## Sicherheitsaspekte

**Kontraindikationen bzw. Risikokonstellationen aus dem Wissensgraphen** (aus Wirkstoff-Erkrankungs-Beziehungen des TxGNN-Wissensgraphen, nicht aus dem Text der Fachinformation):
- Long-QT-Syndrom (einschließlich familiärer Form)
- Torsade de pointes
- Leberversagen
- Arzneimittelinduzierte Leberschädigung
- Kaliummangel
- Interstitielle Lungenerkrankung
- Herzinsuffizienz

**Arzneimittelwechselwirkungen** (100 Wechselwirkungen erfasst; Auswahl der in den Daten aufgeführten):
- **Schwerwiegend (Major):** Loperamid, Clarithromycin
- **Moderat:** u. a. Famotidin, Ranitidin, Cimetidin, Omeprazol, Rabeprazol, Dexlansoprazol (Säureblocker/Protonenpumpenhemmer), Hydrocortison, Dexamethason, Betamethason, Triamcinolon, Budesonid (Kortikosteroide), Pioglitazon, Saxagliptin, Aprepitant, Bisacodyl, Picosulfat sowie Polyethylenglykol-Elektrolytlösungen

Für weitere Sicherheitsinformationen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf einen hohen TxGNN-Wert (Evidenzniveau L5) ohne klinische Studien oder Literatur. Der biologische Zusammenhang ist spekulativ, da Lapatinib PDGFR nicht direkt angreift und für DFSP bereits ein etablierter, gezielter Therapiestandard (Imatinib) besteht. Zudem ist die einzige deutsche bzw. europäische Zulassung erloschen.

**Für ein Fortschreiten sind folgende Schritte nötig:**
- Beschaffung der Warnhinweise und Kontraindikationen aus der Fachinformation (derzeit blockierende Datenlücke für die Sicherheitsprüfung)
- Ergänzung der Mechanismusdaten (MOA), z. B. über DrugBank
- Präklinische Belege (z. B. Zelllinien- oder Modellstudien bei DFSP), die eine Wirkung von Lapatinib jenseits von PDGFR-Signalwegen plausibel machen
- Systematische Literatur- und Studienrecherche für Lapatinib bei DFSP bzw. Weichteilsarkomen
- Klärung der Zulassungs- und Verfügbarkeitssituation, da keine gültige Zulassung in Deutschland besteht
- Prüfung der Routenkompatibilität und der Ähnlichkeit zur ursprünglichen Indikation (derzeit ausstehend)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

