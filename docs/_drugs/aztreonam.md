---
layout: default
title: Aztreonam
parent: Nur Modellvorhersage (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aztreonam: vorhergesagte neue Indikation Hyperamylasämie (Evidenzstufe L5). Ursprüngliche Indikation: Gramnegative bakterielle Infektionen"
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
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

# Aztreonam: Von gramnegativen bakteriellen Infektionen zu Hyperamylasämie

## Zusammenfassung in einem Satz

Aztreonam ist ein Monobactam-Antibiotikum, das ursprünglich zur Behandlung gramnegativer bakterieller Infektionen eingesetzt wird (u. a. Harnwegsinfektionen, nosokomial erworbene Pneumonie, Weichteilinfektionen).
Das TxGNN-Modell sagt als Top-Treffer **Hyperamylasämie** voraus, doch hierfür liegen **keine klinischen Studien und keine Publikationen** vor.
Die am besten gestützte Richtung unter den Vorhersagen ist **gonokokkale Urethritis** mit **6 Publikationen** (Evidenzstufe L3).

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Gramnegative bakterielle Infektionen; Harnwegsinfektionen; nosokomial erworbene Pneumonie; Weichteilinfektionen |
| Vorhergesagte neue Indikation | Hyperamylasämie |
| TxGNN-Vorhersagewert | 99,73 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Aztreonam hemmt die bakterielle Zellwandsynthese über das Penicillin-bindende Protein 3 (PBP3) und wirkt gegen gramnegative Aerobier.

Für die Top-Vorhersage **Hyperamylasämie** besteht **kein plausibler mechanistischer Zusammenhang**. Es handelt sich um einen biochemischen Laborbefund und nicht um eine Infektionskrankheit. Der hohe TxGNN-Wert ist sehr wahrscheinlich ein Artefakt der Graphstruktur. Dasselbe gilt für weitere hochrangige Vorhersagen wie polyklonales Hyperviskositätssyndrom, kongenitale Analbuminämie, Blutgruppeninkompatibilität und prämaligne hämatologische Erkrankungen.

Biologisch plausibel sind dagegen die antibakteriellen Vorhersagen:
- **Gonokokkale Urethritis (Rang 4):** *Neisseria gonorrhoeae* liegt im Wirkspektrum. Studien aus den Jahren 1983–1986 und eine einarmige Studie von 2020 (2 g i. m.) berichten über Wirksamkeit. Es handelt sich eher um eine Erweiterung der Antibiotikaklasse als um echtes Repurposing. Berichte über aztreonamresistente Stämme (2001) zeigen ein Resistenzrisiko. Relevanz hätte Aztreonam vor allem bei Betalaktam-Allergie oder resistenten Infektionen.
- **Epiglottitis (Rang 8):** Häufiger Erreger ist *Haemophilus influenzae*. Die Evidenz ist jedoch nur indirekt.
- **Xanthogranulomatöse Pyelonephritis (Rang 10):** Die Erreger (z. B. *Proteus*, *E. coli*) werden abgedeckt, es gibt aber keine spezifische Evidenz.
- **Ureaplasma-Urethritis (Rang 5):** Mechanistisch unplausibel, da Ureaplasma keine Zellwand besitzt.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Zur Top-Vorhersage Hyperamylasämie liegt keine Literatur vor. Die folgende Tabelle zeigt die Literatur zur am besten belegten Vorhersage, **gonokokkale Urethritis** (Rang 4):

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Einarmige, offene klinische Studie | Antimicrob Agents Chemother | Einzeldosis 2 g Aztreonam i. m. bei *N. gonorrhoeae* als mögliche neue Therapieoption bei drohender Ceftriaxon-Resistenz |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Klinische Studie | Antimicrob Agents Chemother | 1 g i. m. vs. Spectinomycin 2 g bei unkomplizierter Gonorrhö: keine Therapieversagen in beiden Gruppen |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Klinische Studie | Genitourin Med | Einzeldosis 1 g i. m.: Eradikation bei 61 Männern und 26 Frauen an allen Orten (Ausnahme: ein Pharynxbefund); wirksam gegen penicillinsensible und -resistente Stämme |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Klinische/epidemiologische Studie | Hinyokika Kiyo | Epidemiologische und therapeutische Untersuchung zur Einmaltherapie mit Aztreonam bei Gonorrhö |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Klinische/In-vitro-Wirksamkeitsstudie | J Infect Dis | Wirksamkeit gegen penicillinresistente Gonokokken (PPNG) |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistenz-/Mikrobiologiestudie | J Infect Chemother | Auftreten cephem- und aztreonam-hochresistenter, nicht β-Laktamase-bildender *N. gonorrhoeae* |

Weitere, nur indirekte Evidenz: Epiglottitis (PMID 3766490, pädiatrische Serie 1986 zu schweren gramnegativen Infektionen) und monoklonale Gammopathie (PMID 4079014, Infektionen bei hämatologischen Erkrankungen, 1985). Die einzige Publikation zu Blutgruppeninkompatibilität (PMID 34956120) ist eine Resistenzgenomik-Studie und für die Indikation nicht relevant.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/006113 | Emblaveo | nicht angegeben | Gramnegative bakterielle Infektionen; Harnwegsinfektionen; nosokomial erworbene Pneumonie; Weichteilinfektionen |

Der Status der Zulassung ist „erloschen/widerrufen“ (cancelled); gültige Zulassungen bestehen nicht.

---

## Sicherheitsaspekte

- **Kontraindikationen/Risikoerkrankungen aus dem Wissensgraphen** (PrimeKG, keine Packungsbeilage): Nierenerkrankung, Pyoureter, Lebererkrankung, Gallenblasenerkrankung, *Clostridium-difficile*-Kolitis, perinatale nekrotisierende Enterokolitis, Bronchialerkrankung.
- **Arzneimittelwechselwirkungen:** Insgesamt 27 Wechselwirkungen erfasst. Als **moderat** eingestuft sind Picosulfursäure, Dicumarol und Warfarin (Beachtung der Gerinnungsüberwachung). Weitere Wechselwirkungen ohne eingestufte Schwere u. a. mit Vancomycin, Amikacin, Amphotericin B, Tacrolimus, Heparin, Morphin, Protonenpumpenhemmern (Omeprazol, Pantoprazol, Lansoprazol), Metronidazol, Fluconazol, Aciclovir, Dexamethason, Hydrocortison, Ondansetron, Salbutamol und Acetylsalicylsäure.

Für Warnhinweise und Gegenanzeigen aus der Fachinformation bitte die Packungsbeilage bzw. Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Top-Vorhersage Hyperamylasämie ist mechanistisch nicht begründbar und durch keine Studie oder Publikation gestützt (reine Modellvorhersage, L5). Die einzige belastbare Richtung, gonokokkale Urethritis (L3), ist eine Erweiterung der antibakteriellen Klassenanwendung mit nicht randomisierter Evidenz, Resistenzrisiko und etablierten Leitlinientherapien. Zudem besteht in Deutschland keine gültige Zulassung.

**Für ein Weiterkommen sind erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) von der BfArM-Seite beschaffen und auswerten, da dies die Sicherheitsprüfung derzeit blockiert
- Daten zum Wirkmechanismus (MOA) aus DrugBank ergänzen
- Gezielte Bewertung von gonokokkaler Urethritis als Forschungsfrage (z. B. Patienten mit Betalaktam-Allergie oder resistenten Stämmen), inklusive Resistenzlage und Vergleich mit Leitlinientherapie
- Klärung der Verfügbarkeit und des regulatorischen Status des Wirkstoffs in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

