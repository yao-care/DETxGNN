---
layout: default
title: Glucagon
parent: Nur Modellvorhersage (L5)
nav_order: 182
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Glucagon: Von schwerer Hypoglykämie zum Reizdarmsyndrom

## Zusammenfassung in einem Satz

> Glucagon ist ein endogenes Pankreashormon, das herkömmlich zur Behandlung schwerer Hypoglykämie durch Erhöhung des Blutglukosespiegels verwendet wird.
> Das TxGNN-Modell sagt einen möglichen Zusammenhang mit dem **Reizdarmsyndrom (IBS)** mit einer **99.24%** Vorhersagequote voraus,
> doch die zugrunde liegende Evidenz — **11 klinische Studien** und **20 Veröffentlichungen** — befasst sich fast ausschließlich mit **GLP-1-Rezeptor-Agonisten**
> (ROSE-010, liraglutide, exendin-4), einer mechanistisch gegenteiligen Arzneistoffklasse, nicht mit Glucagon selbst. Dies ist sehr wahrscheinlich ein
> **falsch-positives Signal, das durch Namenähnlichkeit** zwischen „Glucagon" und „Glucagon-Like Peptide-1 (GLP-1)" verursacht wird.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Im vorliegenden Datensatz nicht verfügbar (keine Lizenz oder Indikationstexte vorhanden; Glucagon ist klinisch für die Behandlung schwerer Hypoglykämie etabliert) |
| Vorhergesagte neue Indikation | Reizdarmsyndrom |
| TxGNN-Vorhersagequote | 99.24 % (Rang 8077 unter den modellweit bewerteten Kandidaten) |
| Evidenzstufe | L5 – nur Modellvorhersage, keine tatsächlichen Studien zu Glucagon bei IBS |
| Marktstatus Deutschland | ✗ Nicht vermarktet (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten für Glucagon in diesem Evidenzpaket nicht verfügbar. Der Wirkmechanismus von Glucagon ist jedoch in der Literatur gut etabliert: Es bindet den **Glucagon-Rezeptor** (ein anderer GPCR als der GLP-1-Rezeptor) und erhöht den Blutglukosespiegel durch Stimulation der hepatischen Glykogenolyse und Gluconeogenese — das physiologische Gegenteil von Insulin und von GLP-1.

**Diese Vorhersage hält sich mechanistisch nicht.** Jede klinische Studie und Veröffentlichung, die den IBS-Zusammenhang unterstützt, befasst sich mit **GLP-1 (Glucagon-Like Peptide-1) oder seinen Rezeptor-Agonisten** (ROSE-010, liraglutide, exendin-4, natives GLP-1) — nicht mit Glucagon. Während Glucagon und GLP-1 beide aus der Spaltung desselben Vorläufergens (Proglucagon) stammen, wirken sie auf verschiedene Rezeptoren und erzeugen entgegengesetzte physiologische Effekte (Glucagon erhöht den Blutglukosespiegel und beschleunigt die Magenentleerung; GLP-1 senkt den Blutglukosespiegel und *hemmt* die Magenentleerung/Motilität). Sie als pharmakologisch äquivalent zu behandeln ist wissenschaftlich nicht haltbar.

Die eigene Begründung des Evidenzpakets für das Repurposing kommt zu demselben Ergebnis: Es wurde kein mechanistischer Zusammenhang zwischen Glucagon (DB00040) und IBS gefunden. Dieses Muster ist konsistent mit einem **falsch-positiven Abruf, der durch gemeinsame Teilzeichenfolgen-/Namenüberlappung** verursacht wird („glucagon" erscheint innerhalb von „glucagon-like peptide-1") und nicht mit einem echten Drug-Repurposing-Signal.

---

## Evidenz aus klinischen Studien

⚠️ **Keine der nachfolgenden Studien untersucht Glucagon selbst.** Alle beinhalten GLP-1 oder GLP-1-Rezeptor-Agonisten, die hier der Transparenz halber aufgelistet sind, um deutlich zu machen, welche Evidenz tatsächlich vorhanden ist.

| Studiennummer | Phase | Status | Teilnehmerzahl | Wichtigste Befunde |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Abgeschlossen | 52 | ROSE-010 (GLP-1-Rezeptor-Agonist, **nicht Glucagon**) Auswirkung auf die GI-Motorfunktion bei obstipationsdominanten IBS |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Abgeschlossen | 12 | Natives GLP-1 vs. ROSE-010 Hemmung der oberen GI-Motilität — kein Glucagon-Arm |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Beendet | 8 | liraglutide (GLP-1-RA) für Stuhlfrequenz nach IPAA — mechanistisch entgegengesetzt zu Glucagon |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Abgeschlossen | 66 | Auswirkung von Sport auf GLP-1-Hormon und Dysbiose des Darms bei IBS — keine Arzneimittelintervention |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unbekannt | 110 | Kalorienarme Ernährung + intragastrales Ballonkatheter für Fettleibigkeit — keine getestete Glucagon- oder GLP-1-Arznei |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Abgeschlossen | 12 | Fructo-Oligosaccharid-Auswirkung auf reaktive Hypoglykämie — keine Glucagon-Intervention |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Abgeschlossen | 37 | Butyrat-Mechanismus in der Dickdarmgesundheit (IBS-verbunden) — nicht mit Glucagon verwandt |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Abgeschlossen | 41 | Essensgeschwindigkeit von hochverarbeiteten Lebensmitteln auf metabolische Reaktion — nicht mit Glucagon verwandt |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Abgeschlossen | 33 | Auswirkung von Vollkornroggen-Brot auf die Darm-Hirn-Achsen-Peptide — nicht mit Glucagon verwandt |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Abgeschlossen | 33 | Ernährungsintervention der Darm-Mikrobiota in großer Höhe — nicht mit Glucagon verwandt |

**Bewertung der Relevanz:** Alle als **C** (nicht direkt relevant) bewertet vom zugrunde liegenden Evidenzpaket — keine testete Glucagon als Studienarzneistoff.

---

## Literaturnachweis

⚠️ **Alle nachfolgenden Veröffentlichungen befassen sich mit der GLP-1-Physiologie oder GLP-1-Rezeptor-Agonisten, nicht mit Glucagon.**

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Befunde |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scand J Gastroenterol | ROSE-010 (GLP-1-RA, **nicht Glucagon**) reduzierte Schmerzen während IBS-Anfällen |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | Am J Physiol GI Liver Physiol | Randomisierte doppelblinde Studie von ROSE-010 (GLP-1-Analog) zur GI-Motorfunktion bei IBS-C |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematische Übersicht/Metaanalyse | Front Endocrinol | GLP-1-Rezeptor-Agonisten verbessern IBS-Symptome — Glucagon nicht bewertet |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Übersichtsartikel | Exp Physiol | Endokrine Rolle von GLP-1 (nicht Glucagon) in der IBS-Pathophysiologie |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Kohorte | Ann Gastroenterol | Verschreibungs-/Absetzungsmuster von GLP-1-RAs bei IBS-Patienten |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Übersichtsartikel | Expert Opin Investig Drugs | Übersicht über experimentelle IBS-C-Arzneimittel; Glucagon nicht unter diskutierten Kandidaten |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Präklinisch | Neurogastroenterol Motil | exendin-4 (GLP-1-RA) verbesserte GI-Dysfunktion im Rattenmodell für IBS |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Klinische Korrelation | Clin Res Hepatol Gastroenterol | Serum-GLP-1 (nicht Glucagon) umgekehrt korreliert mit Bauchschmerzen bei IBS-C |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Präklinisch | Int J Mol Med | Rolle von GLP-1 in Rattenmodellen der IBS-Pathogenese |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Übersichtsartikel | Adv Exp Med Biol | Aerosolisiertes GLP-1 (nicht Glucagon) für Diabetes und IBS |

---

## Marktstatus Deutschland

Keine Zulassungsunterlagen sind im aktuellen Register verfügbar (Marktstatus: Nicht vermarktet; 0 Lizenzen vorhanden).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind derzeit nicht in diesem Datensatz verfügbar (gekennzeichnet als Blocking-Datenlücke DG001 — TFDA-Kennzeichnung Warnungen/Kontraindikationen, ausstehende Abrufen).

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Dieser Kandidat ist sehr wahrscheinlich ein **falsch-positives Vorhersageergebnis, das durch Entitätsverwechslung** zwischen „Glucagon" und „Glucagon-Like Peptide-1 (GLP-1)" verursacht wird — zwei Hormone mit gegensätzlichen Rezeptoren und gegensätzlichen physiologischen Effekten. Jedes unterstützende Stück aus klinischen Studien und Literaturbelege befasst sich mit GLP-1 oder GLP-1-Rezeptor-Agonisten, keines befasst sich mit Glucagon selbst, und das Evidenzpaket ist unabhängig als L5 bewertet („nur Modellvorhersage, keine tatsächlichen Studien").

**Um fortzufahren, ist Folgendes erforderlich:**
- Überprüfung und Korrektur der Entitätsdisambiguierung im TxGNN-Wissensgraph (Glucagon vs. GLP-1 Knoten-/Kantentrennung) vor dieser neuen Bewertung des Kandidaten
- Falls eine echte präklinische Begründung für Glucagon (nicht GLP-1) bei IBS existiert, Abruf tatsächlicher glucagonspezifischer Studiendaten
- Lösung der Blocking-Datenlücke DG001 (TFDA-Kennzeichnung Warnungen/Kontraindikationen) und der hochpriorisierten Lücke DG002 (MOA über DrugBank) vor einer weiteren Sicherheitsbewertung
- Da das Arzneimittel im Register nicht vermarktet ist, wäre eine Markterschließungsbewertung nur erforderlich, wenn die obigen mechanistischen Bedenken geklärt werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

