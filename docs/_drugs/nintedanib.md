---
layout: default
title: Nintedanib
parent: Nur Modellvorhersage (L5)
nav_order: 315
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Nintedanib: vorhergesagte neue Indikation Dermatofibrosarcoma protuberans (Evidenzstufe L4). Ursprüngliche Indikation: Nicht-kleinzelliges Lungenkarzinom (Vargatef)"
monitor_inn: "NINTEDANIB"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
---

# Nintedanib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Nintedanib: Von nicht-kleinzelligem Lungenkarzinom und idiopathischer Lungenfibrose zu Dermatofibrosarcoma protuberans
{: .text-alpha }

## Zusammenfassung

Nintedanib ist ein Multi-Tyrosinkinase-Inhibitor, der ursprünglich zur Behandlung des nicht-kleinzelligen Lungenkarzinoms und fibrosierender Lungenerkrankungen (u. a. idiopathische Lungenfibrose) zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **Dermatofibrosarcoma protuberans** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **eine Publikation** (ein Übersichtsartikel zu PDGFR-Inhibitoren) als indirekte Evidenz vor.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht-kleinzelliges Lungenkarzinom (Vargatef); idiopathische Lungenfibrose und interstitielle Lungenerkrankungen (Ofev und Generika) |
| Vorhergesagte neue Indikation | Dermatofibrosarcoma protuberans |
| TxGNN-Vorhersagewert | 0,9915 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 4 von 4) |
| Anzahl der Zulassungen | 4 (gültig: 4) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Nintedanib hemmt gleichzeitig mehrere Rezeptor-Tyrosinkinasen: PDGFR alpha/beta, VEGFR 1–3 und FGFR 1–3. Diese Signalwege sind an Tumorwachstum, Angiogenese und Fibrose beteiligt, was die Zulassung sowohl in der Onkologie als auch bei Lungenfibrose erklärt.

Das Dermatofibrosarcoma protuberans (DFSP) wird in der Regel durch die COL1A1-PDGFB-Fusion getrieben, die zu einer dauerhaften Aktivierung von PDGFR-beta führt. Eine PDGFR-Hemmung ist daher biologisch plausibel; Imatinib ist bereits eine etablierte PDGFR-gerichtete Therapie bei DFSP.

Es liegen jedoch keine nintedanibspezifischen klinischen Daten vor. Die einzige Referenz ist ein Übersichtsartikel zu niedermolekularen PDGFR-Inhibitoren, also indirekte Evidenz auf Klassenebene. Der hohe TxGNN-Wert ist eine rein computergestützte Vorhersage.

Die Plätze 2 und 3 der Vorhersageliste (Liposarkom, 0,9913; ovarielles myxoides Liposarkom, 0,9912) beruhen ausschließlich auf dem Modellwert, ohne Studien oder Literatur. Zudem sind Liposarkome häufig durch MDM2/CDK4-Amplifikationen getrieben, also durch Signalwege, die sich von den Nintedanib-Zielstrukturen weitgehend unterscheiden.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Übersichtsartikel | Pharmacological Research | Überblick über die Rolle niedermolekularer PDGFR-Inhibitoren bei neoplastischen Erkrankungen; indirekte Evidenz auf Klassenebene |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002569 | Vargatef | – | Nicht-kleinzelliges Lungenkarzinom (gültig) |
| EMEA/H/C/003821 | Ofev | – | Idiopathische Lungenfibrose, interstitielle Lungenerkrankungen, systemische Sklerose (gültig) |
| EMEA/H/C/006179 | Nintedanib Accord | – | Idiopathische Lungenfibrose, interstitielle Lungenerkrankungen, systemische Sklerose (gültig) |
| EMEA/H/C/006486 | Nintedanib Viatris | – | Idiopathische Lungenfibrose, interstitielle Lungenerkrankungen (gültig) |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (Multi-Tyrosinkinase-Inhibitor) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage beachten |
| Emetogenitätsklassifikation | Bitte Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage beachten |
| Überwachungsparameter | Bitte Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage beachten |
| Handhabungsschutz | Bitte Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage beachten |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen** (in den zusammengestellten Daten 100 Einträge; Auswahl):
  - **Schwerwiegend (Major):** Dexamethason
  - **Moderat:** Acetylsalicylsäure, Clarithromycin, Naltrexon, Rolapitant, Cobicistat
  - **Moderat, Gerinnungs- bzw. Thrombozytenfunktions-bezogene Substanzen:** Abciximab, Alteplase, Antithrombin III, Apixaban, Dipyridamol, Betrixaban, Bivalirudin, Cangrelor, Caplacizumab, Cilostazol, Clopidogrel, Dalteparin, Defibrotid, Desirudin

Für Warnhinweise und Gegenanzeigen liegen keine Daten vor. Bitte die Packungsbeilage zu Rate ziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für DFSP gibt es keine klinischen Studien und nur indirekte Klassenevidenz (ein Übersichtsartikel); der hohe TxGNN-Wert ist eine reine Modellvorhersage. Zudem ist Nintedanib in Deutschland im Handel und besitzt 4 gültige Zulassungen (von 4), und die Sicherheitsdaten aus der Packungsbeilage fehlen.

**Für ein Weiterkommen sind folgende Punkte erforderlich:**
- Präklinische Daten oder Fallserien zu Nintedanib bei DFSP (z. B. in vitro an COL1A1-PDGFB-positiven Zellen) sowie Vergleich mit Imatinib
- Detaillierte Daten zum Wirkmechanismus (MOA) aus DrugBank
- Beschaffung und Auswertung der Packungsbeilage (Warnhinweise, Gegenanzeigen) für ein Sicherheitsscreening
- Klärung des Zulassungs- und Marktstatus in Deutschland
- Bei Liposarkom und ovariellem myxoidem Liposarkom: zunächst keine weiteren Schritte ohne unterstützende Daten
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

