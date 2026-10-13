---
layout: default
title: Caffeine
parent: Nur Modellvorhersage (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Koffein: Von Apnoe zu Erkrankungen der Nasenhöhle

## Zusammenfassung

Koffein wurde ursprünglich zur Behandlung der Apnoe (Atempausen bei Frühgeborenen) eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei **Erkrankungen der Nasenhöhle** wirksam sein könnte. Für diese Richtung liegen jedoch **keine klinischen Studien** und nur **3 Publikationen** mit indirektem Bezug vor, sodass die Vorhersage derzeit rein modellbasiert ist.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Apnoe |
| Vorhergesagte neue Indikation | Erkrankung der Nasenhöhle (nasal cavity disease) |
| TxGNN-Vorhersagewert | 99,91 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassungen |
| Anzahl der Zulassungen | 2 (beide aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zu Koffein liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben zum Wirkmechanismus vor. Bekannt ist, dass Koffein ein Antagonist an Adenosinrezeptoren (A1, A2A, A2B, A3) ist und zudem auf Ryanodin-Rezeptoren (RyR1–3) sowie den IP3-Rezeptor (ITPR1) wirkt. Seine Wirksamkeit bei Apnoe von Frühgeborenen ist belegt.

Als Bitterstoff kann Koffein Bitterrezeptoren (TAS2R) im Atemwegsepithel aktivieren. Dies schafft eine spekulative Verbindung zur angeborenen Immunabwehr und zur mukoziliären Funktion der Nasennebenhöhlen. Die Verbindung zur ursprünglichen Indikation Apnoe (Atemwegs- bzw. Atemantriebsthema) ist nur lose.

Die einzige nasenbezogene Arbeit betrifft ein intranasales Koffein-Gel zur Verbesserung der Kognition und hat mit einer Nasenerkrankung nichts zu tun. Der hohe TxGNN-Wert wird durch klinische Daten nicht gestützt.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Pharmakologie der Bitterrezeptoren (T2R) und ihre Rolle in den menschlichen Atemwegen, einschließlich der Nasenhöhle |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Präklinische Formulierungsstudie | Current Drug Delivery | Thermosensitives nasales In-situ-Gel mit Koffein zur Verbesserung der Kognition nach Schlafentzug (kein Bezug zu Nasenerkrankungen) |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Tierstudie | Cancer Research | Schwarzer Tee und Koffein hemmen die durch NNK induzierte Lungenkarzinogenese bei Ratten (kein Bezug zu Nasenerkrankungen) |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005435 | Gencebok | – | Apnoe |
| EMEA/H/C/001014 | Peyona (zuvor Nymusa) | – | Apnoe |

Beide Zulassungen sind aufgehoben (Status: cancelled).

---

## Sicherheitsaspekte

Die Packungsbeilage mit Warnhinweisen und Gegenanzeigen lag für diesen Bericht nicht vor. Bitte die Fachinformation zu Sicherheitsaspekten heranziehen.

- **Kontraindikationen aus dem Wissensgraphen (nicht aus Beipackzetteln):** Das TxGNN-Wissensnetz (PrimeKG) verzeichnet für Koffein Kontraindikations-Verknüpfungen mit u. a. folgenden Erkrankungen:
  - Herz-Kreislauf: Bluthochdruck, orthostatische Hypotonie, posturales orthostatisches Tachykardiesyndrom, Multisystematrophie, Long-QT-Syndrom (auch familiär)
  - Leber und Niere: Leberversagen, Lebererkrankung, Nierenerkrankung
  - Magen-Darm: Magengeschwür, Ulkuskrankheit, Pankreatitis, Gallenblasenerkrankung, chronisch-entzündliche Darmerkrankung
  - Neurologie/Psyche: Epilepsie, Schlaflosigkeit, Angststörung, neurotische Störung, dysthyme Störung
  - Lunge: COPD
  - Stoffwechsel/Endokrinologie: Porphyrie, Hypothyreose (auch angeboren), Myxödem
  - Sonstige: Thrombozytopenie, Pyoureter
- **Wechselwirkungen:** Die Abfrage ergab 8 pharmakologische Zielstrukturen: Adenosinrezeptoren A1, A2A, A2B und A3, IP3R1 sowie RyR1, RyR2 und RyR3. Dies sind Wirkorte, keine klassischen Arzneimittelwechselwirkungen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der hohe TxGNN-Wert (99,91 %) für Erkrankungen der Nasenhöhle wird weder durch klinische Studien noch durch direkte Literatur gestützt (Evidenzlevel L5). Zudem bestehen in Deutschland derzeit keine gültigen Zulassungen, und die Sicherheitsdaten aus der Fachinformation fehlen.

**Für ein Weiterkommen sind erforderlich:**
- Beschaffung und Auswertung der Fachinformation mit Warnhinweisen und Gegenanzeigen (Sicherheitsprüfung)
- Daten zum Wirkmechanismus aus DrugBank
- Präklinische oder klinische Studien zu Koffein bei Nasen- bzw. Nasennebenhöhlenerkrankungen (z. B. zur Rolle der Bitterrezeptoren)
- Klärung des regulatorischen Status, da keine gültige Zulassung besteht

---

### Hinweis zu weiteren vorhergesagten Indikationen

Unter den weiteren Vorhersagen mit eigener Literatur zeigen **Neuralgie** (Rang 5, L4), **trigeminoautonome Kopfschmerzen** (Rang 8, L4) und **Hypnic Headache** (Rang 9, L4, Fallberichte und Übersichtsarbeiten, ohne RCTs) mehr indirekte Evidenz als die Nasenhöhle. Sie werden als Forschungsfragen („Research Question") eingestuft. Beim Hypnic Headache ist zugleich das Risiko eines Medikamentenübergebrauch-Kopfschmerzes zu bewerten.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

