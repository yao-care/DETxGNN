---
layout: default
title: Deferasirox
parent: Nur Modellvorhersage (L5)
nav_order: 136
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Deferasirox: vorhergesagte neue Indikation HIV-Infektion (Evidenzstufe L5). Ursprüngliche Indikation: Eisenüberladung"
monitor_inn: "DEFERASIROX"
predicted_indications: ["HIV infectious disease", "chronic hepatitis C virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "dermatofibrosarcoma protuberans"]
---

# Deferasirox
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Deferasirox: Von Eisenüberladung/β-Thalassämie zu HIV-Infektion

## Zusammenfassung in einem Satz

Deferasirox ist ein Eisenchelator, der ursprünglich zur Behandlung von Eisenüberladung bei β-Thalassämie eingesetzt wurde.
Das TxGNN-Modell sagt voraus, dass er bei **HIV-Infektion** wirksam sein könnte,
doch bislang gibt es **keine klinischen Studien** und nur **2 Publikationen** (davon nur eine mit indirektem, präklinischem Bezug).

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Eisenüberladung; β-Thalassämie |
| Vorhergesagte neue Indikation | HIV-Infektion |
| TxGNN-Vorhersagewert | 99,40 % |
| Evidenzgrad | L4 (nur präklinische/mechanistische Evidenz) |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen (keine gültige Zulassung) |
| Anzahl der Zulassungen | 3 (alle erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Deferasirox ein Eisenchelator ist; seine Wirksamkeit bei Eisenüberladung ist belegt. Mechanistisch könnte der Eisenstoffwechsel auch bei HIV-1 eine Rolle spielen.

Eine Studie von 2021 (PMID 34550543) berichtet, dass Eisen in Endolysosomen die Tat-vermittelte Transaktivierung des HIV-1-LTR einschränkt, indem es die Tat-Oligomerisierung und die β-Catenin-Expression erhöht. Das ergibt einen plausiblen, aber nur indirekten Zusammenhang zwischen Eisenhomöostase und HIV-1-Transkription.

Wichtig ist die Einschränkung: Ob eine Eisenchelierung die Virusreplikation bei Patienten beeinflusst, ist nicht belegt. Eisenentzug könnte sogar in beide Richtungen wirken, also die Transkription auch verstärken. Die zweite Publikation (PMID 16529348) ist ein allgemeiner Überblick über neue Arzneimittel und liefert keine Evidenz für HIV.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Zeitschrift | Zentrale Aussagen |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Präklinisch/mechanistisch | Journal of Neurovirology | Endolysosomales Eisen schränkt die Tat-vermittelte HIV-1-LTR-Transaktivierung ein (erhöhte Tat-Oligomerisierung, mehr β-Catenin) |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Übersichtsarbeit | Journal of the American Pharmacists Association | Allgemeiner Überblick über neue Arzneimittel (u. a. Deferasirox); kein HIV-Bezug |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005014 | Deferasirox Mylan | – | Eisenüberladung; β-Thalassämie |
| EMEA/H/C/005156 | Deferasirox Accord | – | Eisenüberladung; β-Thalassämie |
| EMEA/H/C/000670 | Exjade | – | β-Thalassämie; Eisenüberladung |

Alle drei Zulassungen sind erloschen.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (PrimeKG, nicht aus dem Beipackzettel):** Leberversagen, Lebererkrankung, Leberzirrhose, Nierenerkrankung, eingeschränkte Nierenfunktion, Thrombozytopenie, Neutropenie (einschließlich angeborener Formen), Agranulozytose, Anämie, Hyperbilirubinämie, Gilbert-Syndrom, Gallenblasenerkrankung, aktives Magengeschwür, okuläre Hypertension, Multiorganversagen und Krebserkrankungen.
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen gefunden; Beispiele für **schwerwiegende (Major)** Wechselwirkungen:
  - Kortikosteroide: Hydrocortison, Dexamethason, Betamethason, Triamcinolon
  - Amphotericin B (konventionell, Lipidkomplex, Cholesterylsulfat, liposomal)
  - Acetylsalicylsäure
  - Mesalazin, Balsalazid
- Beispiele für **moderate** Wechselwirkungen: Rabeprazol, Pioglitazon, Alosetron, Aprepitant, Clarithromycin, Saxagliptin, Aluminiumhydroxid, Cisaprid, Dexfenfluramin.

Angaben zu Warnhinweisen und Kontraindikationen aus der Fachinformation liegen nicht vor; bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich auf einen hohen Modellwert und eine einzelne indirekte präklinische Arbeit. Es gibt keine klinischen Studien, und die Wirkrichtung der Eisenchelierung bei HIV ist unklar. Zudem hat das Präparat in Deutschland keine gültige Zulassung, und die Fachinformation zur Sicherheit fehlt.

**Für das weitere Vorgehen wird Folgendes benötigt:**
- Detaillierte Wirkmechanismus-Daten (MOA)
- Fachinformation mit Warnhinweisen und Kontraindikationen (blockierend für die Sicherheitsprüfung)
- Gezielte präklinische Untersuchungen (Zellkultur), ob Deferasirox die HIV-Replikation hemmt oder fördert
- Prüfung der Sicherheit bei HIV-Patienten, insbesondere bei Leber- und Nierenfunktion sowie Blutbild, und der Wechselwirkungen mit antiretroviraler Therapie
- Klärung des Zulassungsstatus bzw. der verfügbaren Präparate in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

