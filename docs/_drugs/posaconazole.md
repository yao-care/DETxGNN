---
layout: default
title: Posaconazole
parent: Nur Modellvorhersage (L5)
nav_order: 365
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Posaconazole: vorhergesagte neue Indikation Pneumocystose (Evidenzstufe L4). Ursprüngliche Indikation: Candidiasis"
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
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

## Posaconazol: Von Mykosen zu Pneumocystose
{: .text-alpha }

## Zusammenfassung

Posaconazol ist ein Triazol-Antimykotikum, das ursprünglich zur Behandlung von Pilzinfektionen (Candidiasis, Kokzidioidomykose, Aspergillose und weiteren Mykosen) zugelassen wurde. Das TxGNN-Modell sagt voraus, dass es bei **Pneumocystose** wirksam sein könnte. Dafür liegen **1 klinische Studie** (ohne direkten Posaconazol-Bezug) und **5 Publikationen** (überwiegend Leitlinien und Übersichtsarbeiten) vor. Die Evidenz für diese Indikation ist daher sehr schwach.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Candidiasis; Mykosen; Kokzidioidomykose; Aspergillose |
| Vorhergesagte neue Indikation | Pneumocystose |
| TxGNN-Vorhersagewert | 0,9977 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 5 von 5) |
| Anzahl der Zulassungen | 5 (gültig: 5) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Posaconazol gehört zur Klasse der Triazol-Antimykotika und hemmt die fungale Lanosterol-14-alpha-Demethylase (CYP51). Dadurch wird die Ergosterol-Synthese blockiert. Seine Wirksamkeit bei invasiven Mykosen ist belegt, und Pneumocystis jirovecii wird taxonomisch zu den Pilzen gezählt. Daraus ergibt sich eine Plausibilität auf Klassenebene.

Es gibt jedoch ein gewichtiges Gegenargument: Die Membran von Pneumocystis enthält kaum Ergosterol und verwendet stattdessen vor allem Cholesterin und andere Sterole. Azole wie Posaconazol gelten daher allgemein als wenig wirksam gegen diesen Erreger. Der hohe TxGNN-Wert (0,9977) beruht vermutlich eher auf der breiten antimykotischen Annotation des Wirkstoffs als auf einem validierten Mechanismus. Die mechanistische Verbindung ist somit nicht bestätigt und eher skeptisch zu beurteilen.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Zentrale Ergebnisse |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Abgeschlossen | 602 | Rezafungin i.v. versus Standardregime zur Prävention invasiver Pilzinfektionen nach allogener Blut- und Knochenmarktransplantation. Kein Posaconazol-Prüfarm erkennbar; nur als Hintergrund zum Design antimykotischer Prophylaxestudien relevant. |

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Zentrale Ergebnisse |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Leitlinie/Review | The Lancet Infectious Diseases | Aktualisierte Empfehlungen der British Society for Medical Mycology zur Diagnostik schwerer Pilzerkrankungen |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Leitlinie/Review | Zhonghua Jie He He Hu Xi Za Zhi | Chinesische Leitlinie zu Diagnose und Management invasiver pulmonaler Pilzerkrankungen |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Überblick über Candidiasis, Aspergillose, Kryptokokkose und Pneumocystis-Pneumonie; Posaconazol-Prophylaxe senkte invasive Candidiasis und Aspergillose bei Hochrisiko-Patienten |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (Pharmakokinetik) | Clinical Pharmacokinetics | Penetration von Antiinfektiva, darunter Antimykotika, in die pulmonale Epithelflüssigkeit |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Kohorte/Beobachtungsstudie | Transplant Infectious Disease | Infektiöse Komplikationen bei akuter GVHD nach Lebertransplantation |

Keine dieser Arbeiten liefert direkte Wirksamkeitsdaten für Posaconazol bei Pneumocystose.

---

## Marktinformationen Deutschland

Alle 5 Zulassungen sind gültig (europäische Zentralzulassungen); das Arzneimittel ist im Handel.

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000610 | Noxafil | – | Candidiasis; Mykosen; Kokzidioidomykose; Aspergillose |
| EMEA/H/C/005028 | Posaconazole AHCL | – | Mykosen |
| EMEA/H/C/005005 | Posaconazole Accord | – | Mykosen |
| EMEA/V/C/004987 | Mometamax Ultra | – | – |
| EMEA/V/C/000122 | Posatex | – | – |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Die Abfrage ergab 100 Wechselwirkungen; ausgewertet wurden die ersten 20. Als **schwerwiegend (Major)** eingestuft sind:
- Loperamid
- Triamcinolon
- Budesonid

Als **moderat** eingestuft sind unter anderem:
- Säureblocker/Protonenpumpenhemmer: Famotidin, Ranitidin, Cimetidin, Omeprazol, Rabeprazol
- Kortikosteroide: Hydrocortison, Dexamethason, Betamethason
- Weitere: Aprepitant, Clarithromycin, Saxagliptin, Bisacodyl, Picosulfat, Polyethylenglykol

Zu Warnhinweisen und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation zu Rate ziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der hohe TxGNN-Wert wird durch keine direkte klinische Evidenz gestützt. Die einzige Studie prüft einen anderen Wirkstoff, die Literatur besteht aus allgemeinen Übersichten. Zudem spricht die Biologie von Pneumocystis (kaum Ergosterol) gegen eine Azol-Wirksamkeit. Alle 5 deutschen Zulassungen sind gültig, das Arzneimittel ist im Handel.

**Für ein Weiterverfolgen sind erforderlich:**
- Fachinformation mit Warnhinweisen und Gegenanzeigen (derzeit blockierende Datenlücke für die Sicherheitsbewertung)
- Mechanistische Daten (MOA), insbesondere zur In-vitro-Aktivität von Posaconazol gegen Pneumocystis
- Präklinische oder klinische Daten, die direkt Posaconazol bei Pneumocystose untersuchen
- Klärung des aktuellen Zulassungs- und Vertriebsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

