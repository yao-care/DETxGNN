---
layout: default
title: Everolimus
parent: Hohe Evidenz (L1-L2)
nav_order: 187
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-28
description: "Everolimus: vorhergesagte neue Indikation Liposarkom (Evidenzstufe L2). Ursprüngliche Indikation: Nierenzellkarzinom, Mammakarzinom, Pankreastumoren (Afinitor)"
monitor_inn: "EVEROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
---

# Everolimus
{: .fs-9 }

Evidenzniveau: **L2** | Vorhergesagte Indikationen: **8** 
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

## Everolimus: Vom Nierenzellkarzinom, Mammakarzinom und Pankreastumor zum Liposarkom
{: .text-alpha }

## Zusammenfassung in einem Satz

Everolimus ist ein mTOR-Inhibitor, der ursprünglich zur Behandlung von Nierenzellkarzinom, Brustkrebs, Pankreastumoren und der Tuberösen Sklerose zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **Liposarkom** wirksam sein könnte.
Dafür liegen derzeit **1 klinische Studie** und **4 Publikationen** vor, von denen jedoch nur eine direkt auf Everolimus bei dieser Erkrankung eingeht.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nierenzellkarzinom, Mammakarzinom, Pankreastumoren (Afinitor); Tuberöse Sklerose (Votubia) |
| Vorhergesagte neue Indikation | Liposarkom |
| TxGNN-Vorhersagewert | 0,9988 |
| Evidenzgrad | L2 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl der Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Proceed with Guardrails |

Hinweis: Die Zulassungen wurden zentral über die EMA erteilt (Nummern EMEA/H/C/…) und sind laut den für diesen Bericht zusammengestellten Daten als erloschen gelistet.

---

## Warum ist diese Vorhersage plausibel?

Zu den Wirkmechanismen liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Nach bekanntem Stand hemmt Everolimus mTORC1 im PI3K/AKT-Signalweg. Seine Wirksamkeit bei Nierenzell-, Brust- und Pankreastumoren ist belegt, und mechanistisch kann er auch bei weiteren Tumorarten anwendbar sein, in denen dieser Signalweg aktiv ist.

Beim dedifferenzierten Liposarkom (CDK4/MDM2-amplifiziert) ist die Kombination von Everolimus mit dem CDK4/6-Inhibitor Ribociclib ein rationaler Ansatz: Sie blockiert gleichzeitig den Zellzyklus (CDK4/6-Rb) und den Wachstums- und Überlebensweg (mTOR). Der hohe TxGNN-Wert passt zu dieser Überlegung.

Die ursprünglichen Indikationen und das Liposarkom sind zwar unterschiedliche Tumorentitäten, haben aber die Aktivierung des mTOR-Signalwegs als gemeinsamen Anknüpfungspunkt.

---

## Klinische Studien

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Aktiv, nicht rekrutierend | 48 | Ribociclib plus Everolimus bei fortgeschrittenem dedifferenziertem Liposarkom und Leiomyosarkom nach mindestens einer Vortherapie; Ziel ist die Bestimmung der Antitumoraktivität. Einarmige Studie, nicht randomisiert. |

---

## Literaturevidenz

| PMID | Jahr | Typ | Fachzeitschrift | Kernaussagen |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase-2-Studienbericht | Clinical Cancer Research | Ergebnisse der Phase-2-Studie zu Ribociclib plus Everolimus bei dedifferenziertem Liposarkom und Leiomyosarkom |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | Präklinische PDOX-Mausmodelle bei Sarkomen mit dem CDK-Inhibitor Palbociclib; nur indirekter Bezug |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Präklinisch | Oncogene | XPO1-Inhibitor KPT-330 bei dedifferenziertem Liposarkom; indirekt für Everolimus |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Präklinisch | Anticancer Research | Eribulin-Kombinationen in Xenograft-Modellen; indirekt |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/001038 | Afinitor (gültig) | – | Nierenzellkarzinom, Mammakarzinom, Pankreastumoren |
| EMEA/H/C/002311 | Votubia (gültig) | – | Tuberöse Sklerose |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtete Therapie (mTOR-Inhibitor) |
| Myelosuppressionsrisiko | Hinweise auf Thrombozytopenie, Neutropenie, Leukopenie und Anämie (aus Wissensgraph-Kontraindikationen); Details bitte der Fachinformation entnehmen |
| Emetogenitätsklasse | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Blutbild, Leber- und Nierenfunktion, Blutzucker und Blutfette |
| Handhabungsschutz | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (keine Fachinformationsangaben, sondern Beziehungen im TxGNN-Wissensgraphen): Leber- und Nierenerkrankungen, Leberversagen, Thrombozytopenie, Neutropenie, Leukopenie, Anämie, Hyperglykämie, Diabetes mellitus, Hyperlipidämie, Hypertriglyceridämie, interstitielle Lungenerkrankung, Stomatitis, Herzinsuffizienz, Perikarderguss, hämolytisch-urämisches Syndrom sowie weitere.
- **Arzneimittelwechselwirkungen** (100 Einträge insgesamt; Auswahl):
  - *Schwerwiegend (Major):* Amphotericin B (auch als Lipidkomplex), Aprepitant, Dexamethason, Clarithromycin
  - *Moderat:* u. a. Metformin, Acarbose, Gliptine, Gliflozine, GLP-1-Agonisten, Glimepiride, Cimetidin
  - *Gering (Minor):* Zinksulfat

Die Fachinformation zu Warnhinweisen und Gegenanzeigen liegt nicht vor und muss ergänzt werden.

---

## Weitere vorhergesagte Indikationen (Kurzüberblick)

| Erkrankung | TxGNN-Wert | Evidenzgrad | Einschätzung |
|------|------|------|------|
| Rhabdomyosarkom | 0,9974 | L2 | Research Question; Phase-1- und Phase-1/2-Studien, überwiegend Kombinationen und gemischte pädiatrische Tumoren |
| Dermatofibrosarcoma protuberans | 0,9982 | L4 | Hold; nur indirekte präklinische Literatur |
| Übrige seltene Sarkom-Subtypen | 99,72–0,9984 | L5 | Hold; reine Modellvorhersage |

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Für das Liposarkom liegt eine prospektive Phase-2-Studie (n = 48) mit veröffentlichten Ergebnissen vor. Sie ist jedoch einarmig und untersucht eine Kombination, sodass der Beitrag von Everolimus allein nicht abgrenzbar ist. Der Evidenzgrad L2 stützt eine weitere Prüfung unter Auflagen, aber keine uneingeschränkte Freigabe. Zudem sind in Deutschland derzeit nur erloschene Zulassungen gelistet.

**Für das weitere Vorgehen wird Folgendes benötigt:**
- Fachinformation (Warnhinweise und Gegenanzeigen), da diese Sicherheitsdaten fehlen und den Übergang zur Sicherheitsprüfung blockieren
- Detaillierte Wirkmechanismus-Daten (z. B. aus DrugBank)
- Auswertung der Ergebnisse von NCT03114527 (Ansprechrate, Verträglichkeit) speziell für das Liposarkom
- Klärung des aktuellen Zulassungs- und Vermarktungsstatus in Deutschland
- Sicherheitsüberwachungsplan, insbesondere für Blutbild, Stoffwechselparameter und Wechselwirkungen mit CYP3A4-Hemmern und -Induktoren
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

