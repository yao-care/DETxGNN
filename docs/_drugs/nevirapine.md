---
layout: default
title: Nevirapine
parent: Nur Modellvorhersage (L5)
nav_order: 313
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Nevirapin: vorhergesagte neue Indikation felines erworbenes Immundefizienz-Syndrom (Evidenzstufe L4). Ursprüngliche Indikation: HIV-Infektionen"
monitor_inn: "NEVIRAPINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Nevirapine
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

## Nevirapin: Von HIV-Infektion zu felinem erworbenem Immundefizienz-Syndrom
{: .text-alpha }

## Zusammenfassung in einem Satz

Nevirapin ist ein nicht-nukleosidischer Reverse-Transkriptase-Hemmer (NNRTI), der ursprünglich zur Behandlung der HIV-Infektion zugelassen wurde. Das TxGNN-Modell sagt voraus, dass er bei **felinem erworbenem Immundefizienz-Syndrom** wirksam sein könnte. Dafür liegen **keine klinischen Studien** und lediglich **1 präklinische Publikation** vor, die Evidenz ist daher sehr schwach.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | HIV-Infektionen |
| Vorhergesagte neue Indikation | Felines erworbenes Immundefizienz-Syndrom (Katzen-Immundefizienz) |
| TxGNN-Vorhersagewert | 0,9985 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Für diesen Wirkstoff sind derzeit keine detaillierten Daten zum Wirkmechanismus verfügbar. Bekannt ist, dass Nevirapin ein NNRTI ist, der die Reverse Transkriptase von HIV-1 hemmt. Seine Wirksamkeit bei HIV ist belegt, und mechanistisch könnte er auf verwandte Lentiviren übertragbar sein.

Das Felines Immundefizienz-Virus (FIV) ist ein Lentivirus mit einer verwandten Reverse Transkriptase. Das dürfte den hohen TxGNN-Wert erklären. Allerdings zeigen NNRTIs gegen FIV im Allgemeinen nur geringe Aktivität, da sich die NNRTI-Bindungstasche strukturell unterscheidet. Die einzige verfügbare Publikation (2023) ist eine biochemische und strukturelle Vergleichsstudie und belegt keine Wirksamkeit von Nevirapin bei Katzen.

Zu beachten: Es handelt sich um eine veterinärmedizinische Indikation ohne unmittelbare Relevanz für die Humanmedizin. Die weiteren Vorhersagen sind ähnlich schwach begründet:

- **Simian-Immundefizienz-Virus-Infektion** (Score 0,9985): Die Reverse Transkriptase von SIV ist von Natur aus gegen NNRTIs resistent. Nevirapin ist nur in chimären SHIV-Modellen mit HIV-1-RT wirksam, die als Forschungsmodelle dienen, nicht als Therapie.
- **Neuroentwicklungsstörung mit ataktischem Gang, fehlender Sprache und verminderter kortikaler weißer Substanz** (Score 0,9982): Kein erkennbarer mechanistischer Zusammenhang, weder klinische Studien noch Literatur.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Für die erstrangige Vorhersage (felines Immundefizienz-Syndrom):

| PMID | Jahr | Typ | Fachzeitschrift | Kernaussagen |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Präklinische biochemische/strukturelle Studie | Journal of Veterinary Science | Vergleich der NNRTIs Nevirapin, Efavirenz und Rilpivirin gegen die Reverse Transkriptase von FIV und HIV, um das Potenzial für die Behandlung der FIV-Infektion zu prüfen |

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000183 | Viramune | – | HIV-Infektionen (Status: gültig) |

---

## Sicherheitsaspekte

- **Kontraindikationen/Risikokonstellationen laut Wissensgraph (PrimeKG, keine Packungsbeilage):** Leberversagen, Lebererkrankung, Gallenblasenerkrankung, Exanthem, chronische Hepatitis-C-Virusinfektion, Hepatitis-C-Virusinfektion, chronische Hepatitis-B-Virusinfektion, Rhabdomyolyse, noduläre Fasziitis, arzneimittelinduzierte Leberschädigung, Stevens-Johnson-Syndrom, toxische epidermale Nekrolyse, Lyell-Syndrom
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Die aufgeführten Beispiele sind sämtlich als moderat eingestuft: Rabeprazol, Bupropion, Aprepitant, Triamcinolon, Dexamethason, Betamethason, Budesonid, Clarithromycin, Saxagliptin, Eliglustat, Linagliptin, Naldemedin, Naloxegol, Naltrexon, Cisaprid, Granisetron, Nitisinon, Ondansetron, Orlistat und Prednisolon.

Für Warnhinweise und Gegenanzeigen aus der Fachinformation bitte die Packungsbeilage bzw. Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht allein auf einem Modellwert und einer einzigen präklinischen Studie. Es gibt keine klinischen Studien, die Zielindikation ist veterinärmedizinisch bzw. ein Forschungsmodell, und die Zulassung in Deutschland ist erloschen. Zudem besteht ein erhebliches Sicherheitsprofil (Leber- und Hautreaktionen, viele Wechselwirkungen).

**Für ein Weiterverfolgen sind folgende Schritte erforderlich:**
- Daten zum Wirkmechanismus (MOA) ergänzen
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM) beschaffen, da dies derzeit die Sicherheitsprüfung blockiert
- Belastbare Wirksamkeitsdaten gegen FIV in vitro und in vivo erzeugen, da NNRTIs gegen FIV generell schwach wirken
- Klären, ob eine veterinärmedizinische Entwicklung überhaupt angestrebt wird, und Prüfung von Alternativen mit besserem Mechanismus-Fit
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

