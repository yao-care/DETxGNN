---
layout: default
title: Enfortumab Vedotin
parent: Nur Modellvorhersage (L5)
nav_order: 146
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Enfortumab vedotin: Von Urothelkarzinom (Blasenkrebs) zu Lepra

## Zusammenfassung in einem Satz

> Enfortumab vedotin ist ein Antikörper-Wirkstoff-Konjugat (ADC), dessen etablierter klinischer Anwendungskontext in diesem Nachweispaket **fortgeschrittener/metastasierter Blasenkrebs (Urotheltumoren)** ist.
> Die Top-Vorhersage des TxGNN-Modells für dieses Arzneimittel ist **Lepra**, mit einem Rohwert von 99.53%,
> aber **null klinische Studien und null Veröffentlichungen** unterstützen derzeit diese spezifische Arzneimittel-Erkrankungs-Paarung, und die eigene mechanistische Begründung des Modells stellt ausdrücklich fest, dass **keine plausible biologische Verbindung** vorhanden ist.

---

## Schnelle Übersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht in strukturierten `original_indications`/Zulassungsdaten vorhanden (Datenlücke). Kontextuelle Literaturbelege in diesem Paket (PMID 41341429) identifizieren Enfortumab vedotin als ein ADC, das bei **Patienten mit fortgeschrittenem Blasenkrebs** verwendet wird — dies ist der einzige verfügbare Indikationskontext. |
| Vorhergesagte neue Indikation | Lepra |
| TxGNN-Vorhersage-Score | 99.53% (Rohwert 0.9953; globale Kandidatenrang 5.642) |
| Evidenzstufe | L5 — nur Modellvorhersage, keine unterstützenden klinischen Studien oder Literatur |
| Marktstatus Deutschland | ✗ Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückhalten** |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit ist das strukturierte Feld für den Wirkmechanismus von Enfortumab vedotin eine dokumentierte Datenlücke (DG002, hoher Schweregrad). Jedoch beschreibt die Begründung für die Arzneimittelrepositonierung des Modells das Arzneimittel konsistent und unabhängig über mehrere Kandidateneintragungen hinweg als **anti-Nectin-4-Antikörper-Wirkstoff-Konjugat (ADC)**: Ein Antikörper, der auf das Tumor-Oberflächenantigen Nectin-4 abzielt, liefert ein Mikrotubuli-störendes Zytotoxin (MMAE, Monomethyl-Auristatin E) in antigenexprimierende Zellen, wodurch direkte Zytotoxizität erzeugt wird.

Lepra hingegen ist eine Infektionskrankheit, die durch *Mycobacterium leprae* verursacht wird und durch antimykobakterielle Chemotherapie behandelt wird (z. B. Multidrug-Therapie mit Dapson, Rifampicin, Clofazimin), nicht durch gezielte zytotoxische Freisetzung. Es gibt keine bekannte Nectin-4-Beteiligung an der Pathophysiologie von *M. leprae*, und es gibt keine Rezeptor- oder Signalweg-Überschneidung zwischen einem antimykobakteriellen Mechanismus und einer Tumor-Antigen-gerichteten zytotoxischen Fracht.

**Dies wird direkt im Begründungstext für die Arzneimittelrepositonierung des Nachweispakets angegeben**: „Enfortumab vedotin ... zeigt keine bekannte Assoziation mit antimykobakteriellen Infektionsmechanismen, und es existiert kein Rezeptor-/Signalweg-Überlapungsnachweis." Mit anderen Worten: Die Quelldaten selbst schlussfolgern, dass die mechanistische Hypothese nicht unterstützt wird — dies ist reine Ähnlichkeits-basierte Modellausgabe (TxGNN-Rang 5.642, weit außerhalb des typischen hochzuverlässigen Vorhersage-Bereichs) ohne korroborierende klinische, präklinische oder Literatur-Signale. Diese Vorhersage sollte als explorativ/Rausch-Ebene behandelt werden, nicht als echter Arzneimittel-Repositionierungs-Kandidat.

---

## Belege aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktstatus Deutschland

Enfortumab vedotin hält derzeit **keine Marktzulassungen** für diesen Markt auf Datensatz (0 Lizenzen; Marktstatus: Nicht vermarktet). Eine Zulassungstabelle kann nicht erstellt werden.

---

## Zytotoxizität

Die zugrunde liegende Arzneimittelklasse von Enfortumab vedotin (gemäß Text der Repositionierungs-Begründung, eingebettet in dieses Nachweispaket) ist ein Antikörper-Wirkstoff-Konjugat, das eine Mikrotubuli-Inhibitor-Fracht liefert, d. h. ein zytotoxisches Antikrebsmittel, daher ist dieser Abschnitt enthalten.

| Element | Inhalt |
|------|------|
| Klassifizierung der Zytotoxizität | Zielgerichtete Therapie — Antikörper-Wirkstoff-Konjugat (anti-Nectin-4-Antikörper + MMAE-Mikrotubuli-Inhibitor-Fracht) |
| Myelosuppressionsrisiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Überwachungselemente | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Handhabungsschutz | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |

*(Detaillierte Toxizitäts-/Warnungsdaten konnten nicht abgerufen werden — dies ist eine dokumentierte blockierende Datenlücke, DG001: TFDA/Packungsbeilage-Warnhinweise und Kontraindikationen, erforderlich vor einer Sicherheitsbewertung in Phase 1.)*

---

## Sicherheitsaspekte

Bitte lesen Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
- Die Vorhersage hat keine klinische, präklinische oder Literaturunterstützung (0 Studien, 0 Veröffentlichungen), liegt auf Evidenzstufe L5, und die eigene mechanistische Begründung des Modells stellt ausdrücklich fest, dass es keine bekannte biologische Verbindung zwischen dem zytotoxischen Mechanismus eines anti-Nectin-4-ADC und dem Infektions-/antimykobakteriellen Behandlungsparadigma der Lepra gibt. Es gibt keine Grundlage, diesen Kandidaten über die erste Sichtung hinaus vorzubringen.

**Zum Fortfahren ist folgendes erforderlich:**
- Formale DrugBank/regulatorische Wirkmechanismus (WM) -Daten (DG002)
- TFDA/Packungsbeilage-Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten (DG001, blockierend — erforderlich vor jeder Sicherheitsbewertung, für dieses Arzneimittel allgemein, unabhängig von der Indikation)
- Unabhängige biologische Begründung (z. B. Nectin-4-Expression oder relevante Zielexpression in von Lepra betroffenen Geweben, oder beliebige veröffentlichte Fallberichte) vor dieser Paarung, die weitere Investitionsbemühungen wert ist
- Angesichts des völligen Mangels an unterstützenden Belegen wird dieser Kandidat derzeit nicht zur weiteren Bewertung empfohlen

---

### Anhang: Andere vom Modell vorhergesagte Indikationen, die überprüft wurden (Ränge 2–9)

Zur Vollständigkeit wurden die verbleibenden Top-9-TxGNN-Vorhersagen in diesem Nachweispaket ebenfalls überprüft und zeigen das gleiche Muster — keine unterstützenden Studien, und mechanistische Begründungen, die konsequent *gegen* biologische Plausibilität argumentieren:

| Rang | Vorhergesagte Erkrankung | Score | Anmerkung |
|------|------|------|------|
| 2 | Multiple endokrine Neoplasie | 99.43% | Genetisches (MEN1/RET) endokrines Tumorsyndroms; kein Nachweis von Nectin-4-Expressions-Relevanz |
| 3 | Cytomegalovirus-Infektion | 99.36% | Virale Infektion; zytotoxischer ADC-Mechanismus hat keine antivirale Begründung und könnte theoretisch das Infektionsrisiko durch Myelosuppression verschlimmern |
| 4 | Candidiasis | 99.30% | Einziger Literatur-Hit (PMID 41341429) ist ein FAERS-Pharmakovigilanz-Signal, das Candidiasis als **Nebenwirkung** bei ADC-behandelten Blasenkrebspatienten beschreibt — d. h. Nachweis von Schaden, nicht Wirksamkeit; dies sollte nicht als unterstützend interpretiert werden |
| 5 | Zerebraler Infarkt | 99.23% | Ischämische Gefäßerkrankung; keine mechanistische Überschneidung, und ADC-bezogene Toxizitäten (Myelosuppression, Neuropathie) sprechen gegen diese Indikation |
| 6 | HIV-Infektionskrankheit | 99.19% | Antiretroviraler Mechanismus unabhängig von ADC-Zytotoxizität |
| 7 | Homozygote familäre Hypercholesterinämie | 99.18% | Lipidstoffwechsel-/LDL-Rezeptor-Störung; keine pharmakologische Überschneidung |
| 8 | Bösartiger Katarrh (Bösartiges Katarrhalfieber) | 99.13% | **Veterinärkrankheit** (bovines/Rinderherpesvirus) — wahrscheinlich ein Ontologie-Mapping-Artefakt zwischen Arten, kein zulässiger Indikation beim Menschen |
| 9 | Infektiöse bovine Rhinotracheitis | 99.13% | **Veterinärkrankheit** (Rinderherpesvirus-1) — selbes wahrscheinliches Ontologie-Artefakt wie Rang 8 |

**Empfehlung:** Keiner der Top-9-Kandidaten in diesem Batch erfüllt auch nur vorläufige Plausibilitätsschwellen. Besonders die Ränge 8–9 deuten auf ein Datenqualitäts-/Ontologie-Mapping-Problem hin (Veterinär- vs. menschliche Krankheitsbegriffe), das möglicherweise ein Wissens-Graphen-Datenbereinigungs-Review garantiert, anstatt klinische Nachfolgearbeit.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

