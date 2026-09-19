---
layout: default
title: Dasatinib
parent: Hohe Evidenz (L1-L2)
nav_order: 113
evidence_level: L2
indication_count: 10
---

# Dasatinib
{: .fs-9 }

Evidenzniveau: **L2** | Vorhergesagte Indikationen: **10** 
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

# Dasatinib: Von chronischer myeloischer Leukämie zum Ewing-Sarkom

## Zusammenfassung in einem Satz

Dasatinib ist ein Multi-Target-Tyrosinkinase-Inhibitor (BCR-ABL, SRC-Familien-Kinasen, c-KIT, PDGFR); die Anmerkungen des Evidenzpakets deuten darauf hin, dass es derzeit für chronische myeloische Leukämie (CML) und Ph+-positive akute lymphoblastische Leukämie zugelassen ist, obwohl dieses Feld der ursprünglichen Indikation in den Quelldaten leer ist und unabhängig überprüft werden sollte. Die Top-Vorhersage des TxGNN-Modells für eine neue Indikation ist das **Ewing-Sarkom**, unterstützt durch **3 klinische Studien** und **9 Publikationen**, wobei die stärkste klinische Studie (Phase 2, n=366) bereits abgeschlossen ist, aber eine begrenzte Wirksamkeit als Monotherapie zeigt.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht im Evidenzpaket angegeben (`drug.original_indications` ist leer). Kontextuelle Anmerkungen im Begründungstext des Pakets beschreiben Dasatinib als BCR-ABL-Kinase-Inhibitor für CML/Ph+-positive ALL — **dies muss unabhängig gegen TFDA/DrugBank überprüft werden**, da dies inkonsistent mit dem unten angegebenen Status „nicht vermarktet" ist (siehe Datenqualitätsanmerkung) |
| Vorhergesagte neue Indikation | Ewing-Sarkom |
| TxGNN-Vorhersage-Score | 99.90% (Score 0.9990, globales Ranking 1,687) |
| Evidenzgrad | L2 |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage vertretbar?

Detaillierte Daten zum ursprünglichen Wirkmechanismus sind in diesem Evidenzpaket nicht verfügbar (`original_moa`: Datenlücke). Die unterstützende Literatur und die eigene Begründung des Pakets für die Umwidmung beschreiben Dasatinib jedoch als Multi-Kinase-Inhibitor, der neben BCR-ABL, c-KIT und PDGFR auch SRC-Familien-Kinasen (SRC/LCK/YES/FYN) blockiert.

Ewing-Sarkom-Tumorzellen sind stark auf SRC-Signalisierung angewiesen — stromabwärts der krankheitsdefinierten EWS-FLI1-Fusion — für Invasion, Migration und Invadopodia-Bildung. In-vitro-Studien (PMID 17363602, PMID 18202781) zeigen, dass Dasatinib die Proliferation und Migration in Knochensarkom-Zelllinien durch diesen Signalweg hemmt, was eine plausible mechanistische Brücke von Dasatinib's bekannten Kinase-inhibitorischen Aktivitäten zur Ewing-Sarkom-Biologie schafft.

Klinisch wurde diese mechanistische Begründung bereits getestet: Eine abgeschlossene Phase-2-Studie in fortgeschrittenen Sarkomen (NCT00464620, n=366) umfasste eine Ewing-Sarkom-Kohorte, aber Dasatinib als Monotherapie zeigte **begrenzte Wirksamkeit und erreichte nicht die erwartete Ansprechrate**. Dies mindert den ansonsten starken mechanistischen Fall und ist der Hauptgrund, warum der Evidenzgrad bei L2 begrenzt ist und nicht höher.

**Datenqualitätsanmerkung:** Die Rang-2-Vorhersage (Myeloidleukämie) in diesem gleichen Evidenzpaket zeigt eine interne Inkonsistenz — `original_indications` ist leer und `market_status` ist „nicht vermarktet", was nicht der etablierten Zulassungsgeschichte von Dasatinib für CML entspricht. Dies deutet auf eine mögliche Feldmapping-Lücke in der Quelldatenbank für diesen Arzneistoffdatensatz hin. Dies sollte geklärt werden, bevor das Feld „Ursprüngliche Indikation" oben abschließend bestimmt wird.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Anzahl der eingeschriebenen Patienten | Wichtigste Ergebnisse |
|---------|-------|--------|---------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Abgeschlossen | 366 | Ansprechrate und 6-Monats-PFS von Dasatinib in fortgeschrittenen Sarkomen, einschließlich einer Ewing-Sarkom-Kohorte; die Wirksamkeit als Monotherapie war begrenzt und erfüllte nicht die erwartete Ansprechrate. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Beendet | 7 | Pädiatrische Studie von Dasatinib kombiniert mit Ifosfamid/Carboplatin/Etoposid; beendet mit nur 7 eingeschriebenen Patienten, begrenzte Aussagekraft. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Rekrutierung läuft | 41 | Testet B7-H3-CAR-T-Zell-Therapie bei rezidivierenden/therapierefraktären Tumoren (einschließlich Ewing-Sarkom-Population); keine Dasatinib-Studie, nur Populationsebenen-Überlappung. |

---

## Literaturbeweis

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|------|------|--------|---------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Präklinisch/In vitro | Oncology Reports | Dasatinib zeigt antiproliferative und antimigrative Aktivität in Neuroblastom- und Ewing-Sarkom-Zelllinien, konsistent mit c-KIT-/PDGFR-/Src-Beteiligung. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Präklinisch/In vitro | Cancer Research | Dasatinib hemmt Migration/Invasion in verschiedenen Sarkomzelllinien und induziert Apoptose in Src-abhängigen Knochensarkomzellen. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Präklinisch/Mechanistisch | Sarcoma | Überprüft FAK-Src-Komplex-Targeting in DSRCT, Ewing-Sarkom und Rhabdomyosarkom; vermerkt, dass Dasatinib als Monotherapie in einer Phase-2-Studie dieser Subtypen fehlschlug, was Kombinationsstrategien motiviert. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Präklinisch/Mechanistisch | Neoplasia | Tenascin C und Src kooperieren, um die Invadopodia-Bildung und Invasion in Ewing-Sarkomzellen unter mikroumgebungsbedingtem Stress voranzutreiben. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Präklinisch/Mechanistisch | Neoplasia | Mikroumgebungsbedingter Stress induziert Src-abhängige Invadopodia-Aktivierung und Migration in Ewing-Sarkomzellen. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Übersicht | Oncology Letters | Allgemeine Übersicht über die Rolle der Src-Signalisierung in der Sarkombiologie und ihre Machbarkeit als Arzneistoff-Ziel. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Übersicht (indirekt — Chondrosarkom) | Current Treatment Options in Oncology | Übersicht der systemischen Therapie für Chondrosarkom, nicht speziell für Ewing-Sarkom; zur Grundlage einbezogen, geringe direkte Relevanz. |

*Hinweis: 2 zusätzliche Literaturtreffer aus der Suche (PMID 29776413 — Plerixafor, nicht Dasatinib; PMID 32999666 — nicht verwandter CML-Fallbericht) wurden aus dieser Tabelle ausgeschlossen, da sie nicht substanziell relevant für die Dasatinib–Ewing-Sarkom-Frage sind.*

---

## Informationen zum Marktstatus in Deutschland

Dasatinib wird derzeit **nicht in Deutschland vermarktet** gemäß diesem Evidenzpaket (0 Zulassungen auf Datensatz; `market_status`: „Nicht vermarktet"). Keine Lizenzunterlagen sind verfügbar zur Zusammenfassung.

---

## Zytotoxizität

Dasatinib ist ein Onkologie-/Antineoplastikum (Tyrosinkinase-Inhibitor-Klasse, im eigenem Begründungstext des Pakets als Behandlung für CML/Ph+-positive ALL referenziert), daher gilt dieser Abschnitt.

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie (BCR-ABL / SRC-Familien-Kinase-Inhibitor, Tyrosinkinase-Inhibitor-Klasse) |
| Myelosuppressions-Risiko | Siehe Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Emetogenitätsklassifizierung | Siehe Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Überwachungspunkte | Siehe Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |
| Handhabungsschutz | Siehe Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage |

---

## Sicherheitsüberlegungen

Siehe Packungsbeilage für Sicherheitsinformationen. (`key_warnings`, `contraindications` und DDI-Daten sind alle in diesem Evidenzpaket nicht verfügbar — DG001, mit der Kennzeichnung „Blocking"-Schweregrad, verhindert explizit das Fortschreiten zur S1-Sicherheitsbewertungsphase.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die mechanistische Begründung (Src-abhängige Invasion im Ewing-Sarkom) ist glaubwürdig und wird durch In-vitro-Daten unterstützt, aber die einzige relevante klinische Studie (Phase 2, n=366) zeigte bereits begrenzte Wirksamkeit als Monotherapie, und es existieren keine dedizierten Ewing-Sarkom-Studiendaten. In Kombination mit einer **Blocking**-Datenlücke zu TFDA-Labeling/Sicherheitsinformationen (DG001) kann der Kandidat nicht über die S1-Sicherheitstor-Stufe hinausgehen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA-Packungsbeilage (Warnhinweise, Kontraindikationen) — erforderlich, um das S1-Sicherheitstor zu passieren (DG001)
- Bestätigte Wirkmechanismus-Daten aus DrugBank (DG002)
- Klärung der oben gekennzeichneten `original_indications`/`market_status`-Datensatzinkonsistenz, damit die wahre ursprüngliche Indikation und der aktuelle Zulassungsstatus bestätigt werden können
- Falls weiter verfolgt, sollte die Bewertung sich auf Kombinationsregime (z. B. mit Chemotherapie oder FAK-Inhibitoren) konzentrieren anstatt auf Dasatinib-Monotherapie, angesichts des negativen Monotherapie-Signals in NCT00464620

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

