---
layout: default
title: Daptomycin
parent: Nur Modellvorhersage (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: Von Gram-positiven Bakterieninfektionen zur Osteoarthritis

## Zusammenfassung in einem Satz

Daptomycin ist ein zyklisches Lipopeptid-Antibiotikum zur Behandlung von Gram-positiven Infektionen (z. B. komplizierte Haut- und Weichteilinfektionen, *S. aureus*-Bakteriämie). Die Top-Vorhersage von TxGNN ist **Osteoarthritis** (Bewertung 99,86%), aber die zugrunde liegende Literatur befasst sich fast ausschließlich mit der Behandlung von *infizierten* Gelenken (Prothesengelenkinfektionen, osteoartikuläre Infektionen) und nicht mit Osteoarthritis selbst – eine wahrscheinliche Vermischung im Knowledge Graph. Ein niedriger bewertetes, aber mechanistisch wesentlich glaubwürdigeres Signal ist **Rheumatoide Arthritis** (Rang 2, Bewertung 99,84%), das durch zwei unabhängige präklinische Studien gestützt wird, die zeigen, dass Daptomycin entzündliche Zytokine und NF-κB-Signalisierung bei Kollagen-induzierten Arthritis-Mäusen unterdrückt. **Es gibt keine klinischen Studien für eine der beiden Indikationen; beide befinden sich auf der Stufe der Hypothesengenerierung.**

---

## Schnellübersicht

| Element | Inhalt |
|---|---|
| Ursprüngliche Indikation | In diesem Evidenzpaket nicht erfasst (Arzneimittel in diesem Markt nicht zugelassen); international zugelassen für komplizierte Haut- und Weichteilinfektionen sowie *S. aureus*-Bakteriämie, einschließlich rechtsseitiger infektiöser Endokarditis |
| Vorhergesagte neue Indikation | Osteoarthritis (oberste TxGNN-Bewertung; **als wahrscheinliches Artefakt gekennzeichnet – siehe unten**) |
| TxGNN-Vorhersagebewertung | 99,86% (Rang 2173) |
| Evidenzstufe | L4 (pro Quellenpaket) – aber Literatur befasst sich größtenteils mit Nicht-Zielindikationen (Infektionsstudien, nicht OA-Pathologie) |
| Marktstatus Deutschland | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückhalten** |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkmechanismus-Daten waren in diesem Evidenzpaket nicht verfügbar (als Datenlücke mit hohem Schweregrad gekennzeichnet, DG002). Basierend auf der allgemeinen Pharmakologie ist Daptomycin ein zyklisches Lipopeptid-Antibiotikum, das sich auf kalziumabhängige Weise an bakterielle Zellmembranen bindet und eine schnelle Membrandepolarisierung sowie bakterizide Abtötung von Gram-positiven Organismen verursacht. Dieser Mechanismus hat keine etablierte, direkte Verbindung zur Knorpelabbau- und Gelenksentzündungs-Pathologie der Osteoarthritis.

Kritisch ist: Wenn die am höchsten bewertete Literatur (10 Arbeiten) untersucht wird, befasst sich praktisch die gesamte Literatur mit **der antimikrobiellen Verwendung von Daptomycin bei infizierten Gelenken** – Prothesengelenkinfektionen, osteoartikuläre Infektionen nach *S. aureus*-Bakteriämie und *in vitro*-Empfindlichkeitstestung – nicht mit Osteoarthritis als degenerativer Erkrankungsentität. Dies deutet stark darauf hin, dass der Knowledge Graph „Gelenkinfektionen" und „Osteoarthritis" als verwandte Gelenkkrankheits-Knoten vermischt hat und dadurch zu einem hohen Ähnlichkeitswert ohne echte mechanistische Relevanz führt. **Wir behandeln daher das OA-Signal als wahrscheinlich falsch.**

### Hinweis zur Signaleinordnung: Rheumatoide Arthritis ist der glaubwürdigere Kandidat

Ein wissenschaftlich haltbareres Signal erscheint auf Rang 2 (Rheumatoide Arthritis, Bewertung 99,84%). Zwei unabhängige, zielgerichtete präklinische Studien (Stufe 2) testeten Daptomycin direkt im Kollagen-induzierten Arthritis (CIA)-Mausmodell:

- **PMID 39571268** (2025) – Daptomycin unterdrückte entzündliche Zytokine und NF-κB-Signalisierung, linderte CIA bei Mäusen und wurde als neuartiger entzündungshemmender Mechanismus unabhängig von seiner antibakteriellen Aktivität vorgeschlagen.
- **PMID 40923559** (2025) – eine Strukturoptimierungsstudie mit synthetisierten Daptomycin-abgeleiteten zyklischen Lipopeptiden mit verbesserter Anti-RA-Aktivität im gleichen Modell.

Dies stellt eine echte neuartige, mechanistisch unterschiedliche Hypothese (Immunomodulation über NF-κB-Hemmung) dar – nicht ein Datenvermischungs-Artefakt – und sollte unserer Ansicht nach eine „Forschungsfrage"-Designierung für weitere präklinische Validierung erhalten – weit vor dem Top-Rang-OA-Signal in Bezug auf biologische Plausibilität.

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert (weder für Osteoarthritis noch für Rheumatoide Arthritis).

---

## Literaturevidenz

*(Primäre Tabelle unten spiegelt predicted_indications[0] = Osteoarthritis wider, pro Evidenzpaketstruktur)*

| PMID | Jahr | Typ | Journal | Hauptergebnisse |
|---|---|---|---|---|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Kohorte | Int Orthop | Hochdosis-Daptomycin + Rifampicin bei Gram-positiven osteoartikulären *Infektionen* |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Kohorte | J Antimicrob Chemother | Daptomycin für Knie-/Hüft-Prothesengelenkinfektionen |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Kohorte | Int J Antimicrob Agents | Hochdosis-Daptomycin für komplizierte Knochen-/Gelenk- und Implantat-assoziierte *Infektionen* |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Kohorte | J Antimicrob Chemother | Daptomycin vs. Standardtherapie bei osteoartikulärer Infektion mit *S. aureus*-Bakteriämie |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Antimikrobielle Empfindlichkeit von Staphylokokken aus Prothesengelenkinfektionen |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Register/Kohorte | Med Clin (Barc) | EU-CORE-Register: Einsatz von Daptomycin in der Realwelt in Spanien über Gram-positive Infektionen |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Fallbericht | Case Rep Orthop | *Corynebacterium* septische Arthritis fälschlicherweise als Osteoarthritis diagnostiziert |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Kohorte | Int J Antimicrob Agents | Umfrage zu Managementmethoden bei Prothesengelenkinfektionen |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Kohorte | Surg Infect | 10-Jahres-Mikrobiologieprofil von Staphylokokken bei osteoartikulären Infektionen |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Fallbericht | ASM Case Rep | *Corynebacterium propinquum* septische Arthritis, erste Isolierung aus Synovialflüssigkeit |

**Anmerkung zu Rheumatoider Arthritis (Rang 2, alternativer Kandidat):**

| PMID | Jahr | Typ | Journal | Hauptergebnisse |
|---|---|---|---|---|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Tierexperimentelle Präklinik (CIA-Maus) | Int Immunopharmacol | Daptomycin unterdrückt entzündliche Zytokine und NF-κB-Signalweg, lindert Kollagen-induzierte Arthritis |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | Tierexperimentelle Präklinik (CIA-Maus) | J Med Chem | Daptomycin-abgeleitete zyklische Lipopeptide mit verbesserter Anti-RA-Aktivität in vitro/in vivo |

---

## Marktinformation Deutschland

Daptomycin ist **derzeit in dieser Gerichtsbarkeit nicht im Handel** (0 Zulassungen vorhanden); keine Lizenzaufzeichnungen sind verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Keine strukturierten Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungsdaten waren in diesem Evidenzpaket verfügbar – als blockierend Datenlücke gekennzeichnet, DG001, die vor jeder Sicherheitsbewertung gelöst werden muss.)

*Kontextueller Hinweis:* ein Fallbericht zu unerwünschtem Ereignis im Evidenzbestand (PMID 36693494) beschreibt Daptomycin-induzierte Rhabdomyolyse, kompliziert durch akute Gichtarthritis – dies ist ein bekanntes Sicherheitssignal (CK-Erhöhung/Myopathie), relevant für die Überwachung des Bewegungsapparats, nicht eine Repurposing-Gelegenheit.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die Top-Rang-Vorhersage (Osteoarthritis) wird durch mechanistisch relevante Evidenz nicht gestützt – die zugrunde liegende Literatur befasst sich mit Gelenk-*Infektionen*, nicht mit Osteoarthritis-Pathologie, und es gibt keine klinischen Studien. Dies ist sehr wahrscheinlich eine Knowledge-Graph-Vermischung, nicht ein echtes Repurposing-Signal.

**Um fortzufahren, wird folgendes benötigt:**
- Blockierend Datenlücke DG001 (Arzneimittelkennzeichnungswarnungen/Kontraindikationen) vor jeder Sicherheitsbewertung lösen
- Hochschweregrad-Datenlücke DG002 (bestätigter Wirkmechanismus) lösen, um mechanistische Begründungsprüfung zu unterstützen
- **Empfehlung, eine separate Forschungsschiene für Rheumatoide Arthritis zu eröffnen** (Rang 2): Beauftragung oder Überprüfung zusätzlicher präklinischer Replikation der CIA-Mausmodell-Befunde (PMID 39571268, 40923559) vor Erwägung einer klinisch-stufigen Investition
- Falls RA weiter verfolgt wird, Dosis-Wirkungs- und Toxizitätsdaten spezifisch für den entzündungshemmenden (nicht-antibakteriellen) Mechanismus beschaffen, da dies einen Off-Label-Immunomodulations-Einsatz darstellen würde, der sich von Daptomycin's zugelassenen antibakteriellen Indikationen unterscheidet

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

