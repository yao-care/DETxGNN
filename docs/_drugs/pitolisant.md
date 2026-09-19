---
layout: default
title: Pitolisant
parent: Mittlere Evidenz (L3-L4)
nav_order: 309
evidence_level: L4
indication_count: 3
---

# Pitolisant
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **3** 
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

# Pitolisant: Von Narkolepsie zu Insomnie (Signal erfordert Verifikation)

## Zusammenfassung in einem Satz

> Pitolisant ist ein Histamin-H3-Rezeptor-inverser Agonist, der aus der Literatur für Narkolepsie und OSA-bezogene excessive Tagesschläfrigkeit bekannt ist — d. h. ein **Wach-förderndes** Medikament.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam für **Insomnie** ist, aber dies wird nur durch **1 zurückgezogene Studie** (für eine nicht verwandte Indikation) und **8 Publikationen** unterstützt, von denen die meisten tatsächlich den gegenteiligen klinischen Effekt beschreiben.
> Diese Vorhersage zeigt einen direkten mechanistischen Widerspruch und sollte als Forschungsfrage behandelt werden, nicht als umsetzbares Signal.

---

## Kurzübersicht

| Element | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | Narkolepsie mit/ohne Kataplexie (nur nach Literaturbelegen; keine formale regulatorische Eintragung in diesem Datensatz) |
| Vorhergesagte neue Indikation | Insomnie (Krankheit) |
| TxGNN-Vorhersage-Score | 99.71% |
| Evidenzstufe | L4 |
| Marktstatus in Deutschland | ✗ Nicht im Handel |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Formale DrugBank-MOA-Daten sind für dieses Medikament nicht verfügbar (Datenlücke). Basierend auf den in diesem Kandidaten beigefügten Literaturbelegen ist Pitolisant ein **selektiver Histamin-H3-Rezeptor-inverser Agonist/Antagonist**. Durch Blockade von H3-Autorezeptoren erhöht es histaminerge, noradrenerge und dopaminerge Signalgebung im Gehirn und erzeugt einen **Wach-fördernden** Effekt. Dieser Mechanismus ist die Grundlage für seine zugelassene Anwendung bei Narkolepsie (mit oder ohne Kataplexie) und seine Untersuchungsanwendung für residuale excessive Tagesschläfrigkeit (EDS) bei OSA-Patienten unter CPAP.

Dies ist genau der Grund, warum die Vorhersage „Insomnie" mechanistisch kontraintuitiv ist: ein Medikament, das entwickelt wurde, um die Wachheit zu erhöhen, würde man erwarten, dass es Insomnie *verschlimmert*, nicht heilt. Sieben der acht an diese Indikation angehängten Literaturzitate beschreiben tatsächlich die Anwendung von Pitolisant für **Narkolepsie oder EDS in OSA** — das klinische Gegenteil von Insomnie — und die einzige zugehörige klinische Studie (ebenfalls zurückgezogen, null Einschlüsse) zielte auf Alkoholvergiftungsstörung ab, nicht auf Schlafeinschlaf-/Schlaferhaltungsprobleme.

Die plausibelste Erklärung, konsistent mit der Begründung, die bereits in diesem Evidenzpaket gekennzeichnet ist, ist, dass der TxGNN-Wissensgraph-Knoten mit der Bezeichnung „Insomnie (Krankheit)" möglicherweise einbettungs-benachbart zu Narkolepsie-/Hypersomnie-/EDS-Krankheitsknoten ist und eine **falsch-positive Assoziation** erzeugt, anstatt eine echte therapeutische Hypothese. Dies muss vor weiterer Evaluierung manuell gegen die Krankheits-Ontologie des KG verifiziert werden.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Einschlüsse | Wichtigste Befunde |
|---------|------|--------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Zurückgezogen | 0 | Entwickelt zur Evaluierung von Pitolisant für **Alkoholvergiftungsstörung** (starke Trinkertage als primärer Endpunkt), nicht Insomnie. Zurückgezogen mit null Einschlüssen — es wurden keine Wirksamkeits- oder Sicherheitsdaten generiert, und die Zielindikation entspricht nicht der vorhergesagten. |

---

## Literaturbeweise

| PMID | Jahr | Typ | Journal | Wichtigste Befunde |
|------|-----|-----|--------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | Lancet Neurology | Phase-3-RCT von Pitolisant in pädiatrischer Narkolepsie mit/ohne Kataplexie — bestätigt Wach-fördernde Wirksamkeit, nicht eine Insomnie-Indikation. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | RCT bei OSA-Patienten mit residueller excessiver Tagesschläfrigkeit trotz CPAP — Pitolisant verwendet zur *Erhöhung* der Wachheit. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | RCT für Tagesschläfrigkeit bei OSA-Patienten mit CPAP-Verweigerung — erneut eine Wach-fördernde Anwendung, klinisch das Gegenteil von Insomnie-Behandlung. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Kohorte | Revista de Neurología | Realwelt-Studie von Pitolisant in behandlungsresistenter Typ-1-Narkolepsie mit Kataplexie. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Übersicht | Handbook of Clinical Neurology | Allgemeine Übersicht der Histamin-Rezeptor-Pharmakologie (H1–H4); nur mechanistischer Hintergrund, nicht indikationsspezifisch. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Übersicht | Drug Design, Development and Therapy | Übersicht der Entwicklung und des therapeutischen Stellenwerts von Pitolisant bei Narkolepsie. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Übersicht | Current Neuropharmacology | Bespricht Veränderungen des histaminergen Systems bei neuropsychiatrischen Erkrankungen; vermerkt, dass Pitolisant für EDS in Narkolepsie verwendet wird, im Gegensatz zu H1-Antagonist Doxepin, der eigentlich für Insomnie verwendet wird. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Übersicht/Mechanistisch | Clinical Neuropharmacology | Frühe mechanistische Übersicht von Pitolisant als Stimulans für Narkolepsie-Kataplexie bei Jugendlichen. |

**Anmerkung:** Keine Publikation in dieser Evidenzmenge untersucht tatsächlich Pitolisant zur Behandlung von Insomnie. Mehrere Quellen beschreiben ausdrücklich den gegenteiligen pharmakologischen Effekt (Wach-Förderung).

---

## Marktinformation zu Deutschland

Pitolisant wird derzeit **nicht** in dieser Rechtsordnung vermarktet, und es sind keine Zulassungsrecords im Datensatz verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die vorhergesagte Indikation (Insomnie) ist mechanistisch nicht plausibel angesichts der gut dokumentierten Wach-fördernden Pharmakologie von Pitolisant, und die einzige beigefügte klinische Studie ist nicht verwandt und zurückgezogen. Der Großteil der Literaturbeweise unterstützt tatsächlich die gegenteilige klinische Anwendung (EDS/Narkolepsie), was darauf hindeutet, dass das TxGNN-Signal eher ein Wissensgraph-Artefakt als eine echte Umwidmungsmöglichkeit ist.

**Um fortzufahren, ist Folgendes erforderlich:**
- Manuelle Verifikation der Definition des Knotens „Insomnie (Krankheit)" und seiner Nachbarn im TxGNN-Wissensgraph, um Verwechslungen mit Narkolepsie-/Hypersomnie-/EDS-Knoten auszuschließen
- Formale DrugBank-MOA-Bestätigung (derzeit eine Datenlücke, DG002)
- TFDA/BfArM-Etikett-Warnungen und Kontraindikationen (derzeit eine blockierende Datenlücke, DG001), bevor eine sicherheitsrelevante Evaluierung stattfinden kann
- Falls der KG-Knoten als echte Insomnie bestätigt wird (nicht ein falsch beschrifteter Hypersomnie-benachbarter Knoten), würden spezifische präklinische oder klinische Insomnie-Daten erforderlich sein, bevor dieser Kandidat erneut in Betracht gezogen werden könnte

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

