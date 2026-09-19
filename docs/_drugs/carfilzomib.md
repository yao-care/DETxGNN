---
layout: default
title: Carfilzomib
parent: Nur Modellvorhersage (L5)
nav_order: 89
evidence_level: L5
indication_count: 5
---

# Carfilzomib
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

# Carfilzomib: Von [Ursprüngliche Indikation nicht bestätigt] zu CMM7

## Zusammenfassung in einem Satz

> Die ursprüngliche Indikation von Carfilzomib ist in diesem Nachweispaket nicht dokumentiert (eine Datenlücke mit Blockierungsschweregrad – die TFDA-Kennzeichnung wurde noch nicht abgerufen); eine literaturgestützte Evidenz in diesem Paket identifiziert es nebenbei als „Frontline-Anti-Myelom-Medikament".
> Die am höchsten bewertete Vorhersage des TxGNN-Modells ist **CMM7** (ein seltener kutaner Melanom-Malignität-Suszeptibilitäts-Subtyp 7), mit einem Vorhersage-Score von **99.37%**, aber **keine klinischen Studien und keine Literatur** unterstützen derzeit diese spezifische Vorhersage – das Evidenzniveau ist L5 (nur Modellvorhersage).
> Bemerkenswert ist, dass eine niedriger bewertete Vorhersage in dieser selben Gruppe – allgemeines **Melanom** – durch 5 mechanistische/präklinische Veröffentlichungen gestützt wird, was es zu einem stärkeren Kandidaten als das am höchsten bewertete CMM7 für jede weitere Bewertung macht.

---

## Schneller Überblick

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht im Nachweispaket vorhanden (`original_indications` leer; DG002 kennzeichnet fehlende MOA-Daten) |
| Vorhergesagte neue Indikation | CMM7 (Kutanes malignes Melanom, Suszeptibilitätslokus 7) |
| TxGNN-Vorhersage-Score | 99.37% |
| Evidenzniveau | L5 (nur Modellvorhersage, keine Studien/Literatur) |
| Taiwan-Marktstatus | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfehlenswerte Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten für Carfilzomib auf Arzneistoffebene nicht verfügbar (DG002, hoher Schweregrad). Basierend auf Informationen, die an anderer Stelle in diesem Nachweispaket vorhanden sind (mechanistische Notizen, die an die Rang-5-Vorhersage „Melanom" angehängt sind), wird Carfilzomib als ein irreversibler Epoxyketone-Klasse-Proteasom-Inhibitor der zweiten Generation verstanden, der selektiv die Chymotrypsin-ähnliche Aktivität des 20S-Proteasoms blockiert, ER-Stress und Apoptose induziert. Ein Literatureintrag (PMID 27016342) bezeichnet Carfilzomib zusätzlich als „Frontline-Anti-Myelom-Medikament", konsistent mit seiner bekannten klinischen Anwendung, obwohl dies nicht formell in das Feld `original_indications` erfasst wurde.

Für die **am höchsten bewertete Vorhersage, CMM7**, gibt es keine unabhängige Literatur- oder Studienevidence in diesem Paket. Die angegebene Begründung ist, dass TxGNN es hoch unter Melanom-Spektrum-Erkrankungen bewertet hat, und das mechanistische Argument ist durch Analogie vom allgemeinen Melanom (Proteasom-Hemmung → Apoptose-Induktion) geliehen, nicht aus CMM7-spezifischen Daten. Dies ist eine materiell schwächere Grundlage als eine direkt belegte Vorhersage.

Im Gegensatz dazu wird Rang 5 in diesem selben Nachweispaket – **allgemeines Melanom** – durch In-vitro-Evidenz gestützt, dass Carfilzomib in Kombination mit Bortezomib die Apoptose in B16-F1-Melanom-Zellen verstärkt, sowie durch Computational-Docking-Studien und mechanistische Artikel zur Proteasom-Weg-Regulation in der Melanom-Zellüberlebensfähigkeit. Dies deutet darauf hin, dass, wenn eine Melanom-Spektrum-Indikation verfolgt werden soll, die Evidenz derzeit die allgemeine „Melanom"-Entität über den unbelegten CMM7-Subtyp begünstigt.

---

## Evidenz aus klinischen Studien

Derzeit keine damit verbundenen klinischen Studien registriert.

*(Dies gilt für die am höchsten bewertete Vorhersage, CMM7. Für keine der 5 vorhergesagten Indikationen in diesem Paket, einschließlich Melanom, wurde klinische Studien- oder ICTRP-Evidenz gefunden.)*

---

## Literaturbeweise

Derzeit keine damit verbundene Literatur für CMM7 (Rang 1) verfügbar.

**Hinweis – zusammenhängende, aber niedriger bewertete Vorhersage:** die allgemeine „Melanom"-Vorhersage (Rang 5, Score 99.03%) in diesem selben Paket hat Literaturunterstützung:

| PMID | Jahr | Typ | Journal | Wichtigste Erkenntnisse |
|------|-----|-----|--------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro (präklinisch) | Biology | Carfilzomib + Bortezomib verstärkt apoptotischen Zelltod in B16-F1-Melanom-Zellen via Caspase 3/8/9/12-Aktivierung |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational (Docking/MD) | J Biomol Struct Dyn | Molekulares Docking/Dynamik unterstützen Carfilzomib-Bindung über mehrere Krebs-Kinase-Ziele, einschließlich Melanom |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Mechanistisch/in vitro | Matrix Biology | Carfilzomib (mit Bortezomib) aktiviert NF-κB-Weg, auslösend Heparanase-Expression, verknüpft mit aggressivem Tumor-Phänotyp |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Mechanistisch | Mol Cancer Res | ZFAND2A/cIAP2-Regulation der Melanom-Zellüberlebensfähigkeit, relevant für Proteasom-Weg-Medikamente |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Mechanistisch (PROTAC-Design) | Leukemia | Proteasomale-Degradations-zielende Chimäre Moleküle aktiv in präklinischen Myelom-Modellen |

Keines davon sind RCTs oder klinische Studien; alle sind präklinisch/mechanistisch/rechnerisch (Tier 3), was das Evidenzniveau für die am besten unterstützten Vorhersagen in dieser Gruppe auf L4 begrenzt.

---

## Taiwan-Marktinformation

Carfilzomib ist **nicht auf dem Taiwan-Markt verfügbar**. Keine Arzneimittellizenzen sind derzeit registriert (`total_licenses: 0`).

---

## Zytotoxizität

Carfilzomib ist ein antineoplastisches Mittel (Proteasom-Inhibitor-Klasse, etablierte Anti-Myelom-Verwendung pro Literaturkontext in diesem Paket).

| Artikel | Inhalt |
|---------|--------|
| Zytotoxizitäts-Klassifizierung | Zielgerichtete Therapie (Proteasom-Inhibitor) |
| Myelosuppression-Risiko | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Packungsbeilage |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Packungsbeilage |
| Überwachungselemente | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Packungsbeilage |
| Handhabungsschutz | Es wird erwartet, dass Standard-Hazard/Antineoplastikum-Handhabungsvorsichtsmaßnahmen gelten; offizielle Bestätigung steht unter der Auflösung von DG001 aus |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

TFDA-Kennzeichnungsdaten (Warnungen, Gegenanzeigen und Arzneimittelwechselwirkungen) sind derzeit nicht verfügbar und werden als Datenlücke mit **Blockierungsschweregrad** (DG001) gekennzeichnet, was verhindert, dass dieser Kandidat die S1-Sicherheits-Vorabbewertungsphase betritt.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
- Die am höchsten bewertete Vorhersage (CMM7) hat keine klinische Studien- oder Literaturunterstützung (L5, nur Modellvorhersage), und ihre mechanistische Begründung ist indirekt, von einer anderen, niedriger bewerteten Vorhersage (allgemeines Melanom) entlehnt.
- Sicherheits-Vorabbewertung (S1) kann nicht fortgesetzt werden, da TFDA-Kennzeichnungsdaten fehlen (DG001, Blockierungsschweregrad).
- Das Arzneimittel ist derzeit nicht auf dem Taiwan-Markt verfügbar (0 Genehmigungen).

**Um fortzufahren, wird das Folgende benötigt:**
- Erhalten Sie TFDA-Packungsbeilage / Kennzeichnungsdaten, um DG001 zu beheben und S1-Sicherheitsbewertung freizugeben.
- Erhalten Sie bestätigte MOA- und ursprüngliche Indikationsdaten von DrugBank, um DG002 zu beheben.
- Wenn Sie dieses Medikament für Melanom-Spektrum-Umwidmung verfolgen, priorisieren Sie die allgemeine **Melanom**-Vorhersage (Rang 5, L4, „Research Question") über CMM7, da sie die einzige Entität in dieser Gruppe mit tatsächlicher (präklinischer) unterstützender Evidenz ist – und verfolgen Sie in vivo/klinische Validierung, angesichts der Tatsache, dass alle aktuelle Literatur Tier 3 ist (in vitro/rechnerisch).

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

