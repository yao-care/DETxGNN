---
layout: default
title: Phenylephrine
parent: Hohe Evidenz (L1-L2)
nav_order: 305
evidence_level: L2
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

Evidenzniveau: **L2** | Vorhergesagte Indikationen: **3** 
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

# Phenylephrin: Vom etablierten Abschwellungsmittel zur Nasenhöhlenerkrankung

## Zusammenfassung in einem Satz

Phenylephrin ist ein topisches α1-adrenerges Agonist, dessen ursprüngliche Indikation in diesem Evidenzpaket nicht erfasst ist (Arzneimittel derzeit nicht auf diesem Register vermarktet, 0 Lizenzen). Das TxGNN-Modell weist eine sehr hohe Konfidenz (**99.97%**) auf **Nasenhöhlenerkrankung** zu, und die Rationale des Evidenzpakets selbst vermerkt, dass dies weitgehend eine *bereits etablierte* klinische Anwendung (nasale Dekongestion) widerspiegelt und nicht eine wirklich neuartige Hypothese – gestützt durch **8 klinische Studien** und **8 Publikationen**, die derzeit identifiziert sind.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Nicht in den Unterlagen – keine Lizenz-/Indikationsdaten vorhanden (Arzneimittel nicht vermarktet) |
| Vorhergesagte neue Indikation | Nasenhöhlenerkrankung |
| TxGNN-Vorhersage-Score | 99.97% |
| Evidenzgrad | L2 |
| Marktstatus in Deutschland | ✗ Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Fortfahren unter Vorkehrungen |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte formale Wirkmechanismus-Dokumentation (DrugBank-Feld) wurde für diesen Datensatz nicht ermittelt (gekennzeichnet als Datenlücke DG002). Allerdings liefert die Rationale des Evidenzpakets selbst die pharmakologische Grundlage: Phenylephrin ist ein **selektiver α1-adrenerger Rezeptor-Agonist**, der direkt auf die nasale Mukosa-Gefäßmuskulatur einwirkt, Vasokonstriktion erzeugt und Mukosaschwellung und Stauung reduziert – ein Wirkmechanismus, der sich direkt auf die Vorhersage „Nasenhöhlenerkrankung" abbildet.

Wichtig ist: Dies ist **nicht im üblichen Sinne eine neuartige Umzweckung**. Wie in der Rationale des Evidenzpakets ausdrücklich vermerkt, spiegelt das leere Feld `original_indications` eine Datenlücke wider und nicht das vollständige Fehlen dieser Indikation – die Rolle von Phenylephrin als Abschwellungsmittel ist klinisch lange etabliert (z. B. in Co-Phenylcain-Nasenspray). Die TxGNN-Vorhersage hier funktioniert eher als *Bestätigung bekannter Pharmakologie* als als Entdeckung neuer Therapiepotenziale.

Die unterstützende Evidenz ist eine Mischung aus direkten Quellen (Grad A: Co-Phenylcain-Nasenspray-Studien) und klassenanaloger Evidenz (Grad B: Oxymetazolin, ein weiterer α-Agonist-Abschwellungsmittel, ähnlich in der Nasennebenhöhlen-Chirurgie verwendet), die zusammengenommen pharmakologisch kohärent sind, obwohl mehrere ermittelte Studien (z. B. Esmolol/Lidocain, Kokain/Xylometazolin-Vergleiche) Phenylephrin tatsächlich nicht beinhalten und als niedrig-relevante Suchergebnisse (Grad C) bewertet wurden.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschluss | Wichtigste Befunde |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Abgeschlossen | 106 | Co-Phenylcain (enthält Phenylephrin) Nasenspray vs. Vernebelung zur Abschwellung/lokale Anästhesie vor Nasoendoskopie – direkt relevant (Grad A) |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Abgeschlossen | 20 | Topisches Oxymetazolin vs. Epinephrin (gleiche Klasse α-Agonisten) zum Vergleich für Blutungskontrolle/chirurgische Sichtbarkeit in der Nasennebenhöhlen-Chirurgie – Evidenz auf Klassenebene (Grad B) |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Abgeschlossen | 21 | Vierfach-Crossover-RCT zur nasalen Stauung nach Allergen-Provokation; ob Phenylephrin das tatsächliche Studienmedikament war, ist aus öffentlichen Daten unbestätigt (Grad B) |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Aktiv, nicht rekrutierend | 60 | IV Esmolol vs. Lidocain für Genesungsqualität nach Nasennebenhöhlen-Chirurgie – kein Phenylephrin verwendet (Grad C) |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Beendet | 3 | Kovanaze (Tetracain/Oxymetazolin) Nasal-Spray vs. Articain für zahnärztliche Anästhesie – kein Phenylephrin (Grad C) |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Zurückgezogen | 0 | Zurückgezogenes Duplikat der Kovanaze vs. Articain-Studie – kein Datenbeitrag (Grad C) |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | NA | Unbekannt | 120 | Endoskopische vs. externe Dacryocystorhinostomie-Technik-Vergleich – keine bestätigte Phenylephrin-Verwendung (Grad C) |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Abgeschlossen | 16 | Kokain vs. Lidocain/Xylometazolin vs. Kochsalzlösung zur intranasalen Analgesie vor nasotrachealem Intubation – kein Phenylephrin (Grad C) |

---

## Literaturevidence

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Befunde |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Doppelblind-RCT: Cophenylcain-Spray vs. Placebo vor flexibler Nasenendoskopie – minimale Schmerzen/Unbehagen in beiden Gruppen, keine signifikanten Unterschiede gefunden |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | Dreifach-verblindete RCT zur topischen Tranexamsäure bezüglich Blutung/Operationsfeld-Qualität während FESS bei chronischer Rhinosinusitis |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Kohorte | Int J Pediatr Otorhinolaryngol | Akustische Rhinometrie der Nasenhöhle/Nasopharynx-Geometrie vor und nach Adenotonsillektomie |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Kohorte | Vestnik Otorinolaringologii | Sicherheits-/Wirksamkeitsbewertung von Polydexa-Spray mit Phenylephrin bei akuter Rhinosinusitis |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Übersicht | Vestnik Otorinolaringologii | Differenzialdiagnose chronischer Nasenhöhlenerkrankung nach Operation und topischer Antibiotika-Therapie (inkl. Phenylephrin-haltiges Polydexa) |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Übersicht | Vestnik Otorinolaringologii | Pathogenetischer Ansatz zur Behandlung entzündlicher Erkrankungen der Nase und Nasennebenhöhlen |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Fallbericht | Arch Ophthalmol | Fallbericht: Kokain-Toxizität während Dacryocystorhinostomie, wobei ein Patient auch auf intranasales Phenylephrin reagierte |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In-vitro | Clin Otolaryngol Allied Sci | In-vitro-Studie zu Arzneimittelwirkungen (inkl. nasal-aktiver Substanzen) auf die Zilienschlagfrequenz |

---

## Marktsituation in Deutschland

Es sind keine Genehmigungsunterlagen für die Vermarktung in diesem Evidenzpaket verfügbar – `market_status` ist **Nicht vermarktet (Nicht vermarktet)** mit **0 Lizenzen** auf Datei für diese Arzneimitteleinheit.

---

## Sicherheitsüberlegungen

Bitte verweisen Sie auf die Packungsbeilage für Sicherheitsinformationen. (Wichtige Warnungen, Kontraindikationen und Daten zu Arzneimittelwechselwirkungen konnten für diesen Datensatz nicht ermittelt werden – gekennzeichnet als blockierende Datenlücke DG001.)

---

## Schlussfolgerung und Nächste Schritte

**Entscheidung: Fortfahren unter Vorkehrungen**

**Rationale:**
Evidenzgrad L2 wird durch eine direkt relevante Grad-A-Studie/RCT (Co-Phenylcain-Nasenspray) plus konsistente Evidenz auf Klassenebene aus Vergleichs-α1-Agonisten unterstützt, aber dies bestätigt weitgehend eine *bereits etablierte* Abschwellungsmittel-Anwendung eher als eine neuartige Indikation, und kritische Sicherheits-/Regulierungsdokumentation fehlt vollständig.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Packungsbeilage – Warnungen, Kontraindikationen, DDI-Daten (DG001, **Blockierend**)
- Bestätigte Wirkmechanismus-Dokumentation aus DrugBank (DG002, **Hoch**)
- Klärung des wahren Urindikations-/Lizenzstatus, da das Arzneimittel 0 aktuelle Marktgenehmigungen aufweist
- Verifikation des tatsächlichen Studienmedikaments in NCT00562120, da öffentliche Unterlagen nicht bestätigen, dass Phenylephrin die Intervention war

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

