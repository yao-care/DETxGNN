---
layout: default
title: Vismodegib
parent: Nur Modellvorhersage (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: Vom Basalzellkarzinom zum Medulloblastom mit ausgedehnter Nodularität

## Zusammenfassung in einem Satz

Vismodegib ist ein First-in-Class-Inhibitor des Hedgehog- (Hh-) Signalwegs, der ursprünglich für das **Basalzellkarzinom (BZK)** entwickelt wurde. Das TxGNN-Modell sagt voraus, dass es auch wirksam sein könnte für das **Medulloblastom mit ausgedehnter Nodularität** (ein SHH-aktiviertes pädiatrisches Hirntumor-Subtyp), mit sehr hohem Modellvertrauen von **99.93%**. Allerdings enthält dieses Evidenzbündel derzeit **0 klinische Studien und 0 Veröffentlichungen**, die spezifisch mit dieser vorhergesagten Indikation verknüpft sind – die Rationale des Modells selbst kennzeichnet dies als wahrscheinliche **Datenlücke** statt als wahre Evidenzabsenz, da Vismodegib in der realen Welt bei SHH-getriebenen Medulloblastomen untersucht wurde.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Basalzellkarzinom (BZK) – bestätigt durch Literatur in diesem Evidenzbündel (PMID 22653209, PMID 24756807); nicht erfasst in `taiwan_regulatory.licenses`, da das Arzneimittel in Deutschland nicht zugelassen ist |
| Vorhergesagte neue Indikation | Medulloblastom mit ausgedehnter Nodularität |
| TxGNN-Vorhersage-Score | 99.93% |
| Evidenz-Level | L5 |
| Marktstatus Deutschland | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

`drug.original_moa` ist als Datenlücke in DrugBank gekennzeichnet (DG002). Allerdings bestätigt die Literatur in diesem Evidenzbündel (PMID 22653209, *Nature Reviews Drug Discovery*; PMID 24756807) unabhängig den Wirkmechanismus: Vismodegib ist ein oral bioverfügbarer niedermolekularer Antagonist von **Smoothened (SMO)**, einer Schlüsselkomponente der transmembranalen Hedgehog-Signalisierung. Durch die Blockierung von SMO verhindert es die nachgelagerte Aktivierung von GLI-Transkriptionsfaktoren und unterdrückt die signalweggesteuerte Proliferation.

Das Basalzellkarzinom und das SHH-aktivierte Medulloblastom sind mechanistisch eng verwandt: beide sind kanonisch getrieben durch Funktionsverlustmutationen in **PTCH1** oder Funktionsgewinnmutationen in **SMO**, was zu konstitutiver Hedgehog-Signalisierung führt. In der Tat erklärt PMID 24756807 explizit, dass „dysregulierte Hh-Signalisierung zu unkontrollierter Proliferation beim Basalzellkarzinom führt und auch beim Medulloblastom nachgewiesen wurde", was die biologische Plausibilität dieser Vorhersage direkt unterstützt, auch wenn sie an einen anderen Krankheitseintrag in diesem Datensatz gebunden ist (Rang 9, „Hautkrebs").

Angesichts dieser gemeinsamen Treibermutations-Biologie ist SMO-Hemmung eine mechanistisch rationale Behandlungsstrategie für den SHH-aktivierten Subtyp des Medulloblastoms. Die Abwesenheit von Studien-/Literatureinträgen, die speziell dem „Medulloblastom mit ausgedehnter Nodularität" in diesem Evidenzbündel zugeordnet sind, ist höchstwahrscheinlich eine **Datenlücke** – eine Hypothese, die die TxGNN-Rationale selbst aufwirft – statt einer echten Evidenzabsenz, und sollte vor jeder endgültigen Entscheidung manuell anhand von ClinicalTrials.gov und PubMed überprüft werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

*Anmerkung: Dies bezieht sich speziell auf den Eintrag „Medulloblastom mit ausgedehnter Nodularität" in diesem Evidenzbündel. Die Rationale des Evidenzbündels selbst kennzeichnet dies als wahrscheinliche Datenlücke, da eine bekannte Untersuchung von Vismodegib bei SHH-getriebenen Medulloblastomen erfolgte.*

---

## Literaturische Evidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformation für Deutschland

Vismodegib ist derzeit **nicht in Deutschland zugelassen** (0 Zulassungen auf Rekordbasis; `market_status: Not marketed`). Keine BfArM-Lizenzen oder genehmigten Indikationstexte stehen in diesem Evidenzbündel zur Verfügung.

---

## Zytotoxizität

Vismodegib ist ein antineoplastisches Arzneimittel (ursprüngliche Indikation: Basalzellkarzinom; Wirkmechanismus: Hedgehog-/SMO-Signalweg-Inhibitor).

| Element | Inhalt |
|---------|--------|
| Zytotoxizitäts-Klassifizierung | Zielgerichtete Therapie (Hedgehog-Signalweg / Smoothened [SMO] Inhibitor) |
| Risiko für Knochenmarksuppression | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |
| Überwachungspunkte | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |
| Handhabungsschutz | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage |

*Keine Toxizitäts-/Sicherheitsdaten stehen in diesem Evidenzbündel zur Verfügung; das TFDA-Etikett (Warnungen/Kontraindikationen) ist als blockierende Datenlücke (DG001) gekennzeichnet, die eine formale S1-Sicherheitsbewertung verhindert.*

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen der Packungsbeilage.

*Schlüsselwarnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind alle als Datenlücken in diesem Evidenzbündel verzeichnet. DG001 (TFDA-Etikett Warnungen/Kontraindikationen) ist als **blockierende** Datenlücke klassifiziert – sie muss vor der formalen Sicherheitsbewertung (S1) dieses Kandidaten behoben werden.*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Rationale:**
Obwohl die TxGNN-Vorhersage-Score sehr hoch ist (99.93%) und die mechanistische Rationale (gemeinsame PTCH1/SMO-Signalweg-Biologie zwischen BZK und SHH-aktiviertem Medulloblastom) wissenschaftlich stichhaltig ist, enthält dieses Evidenzbündel derzeit **null klinische Studien und null Literatur**, die direkt die Vorhersage „Medulloblastom mit ausgedehnter Nodularität" unterstützen, und eine **blockierende** Sicherheitsdatenlücke (DG001) verhindert jede S1-Bewertung. Evidenz-Level ist L5 (reine Modellvorhersage).

**Um fortzufahren, ist Folgendes erforderlich:**
- Manuelle Suche in ClinicalTrials.gov und PubMed nach „vismodegib" + „SHH medulloblastoma" / „SHH-aktiviertes Medulloblastom", um die vermutete Datenlücke zu schließen
- TFDA/EU-Etikett-PDF für Warnungen, Kontraindikationen und Dosierung (Behebung von DG001)
- DrugBank-MOA-Datenbestätigung (Behebung von DG002)
- Bestätigung des tatsächlichen deutschen/EU-Regulierungsstatus von Vismodegib, da es hier als nicht zugelassen mit 0 Zulassungen verzeichnet ist, obwohl es ein zugelassenes Produkt (Erivedge®) anderswo ist

**Anmerkung für Bewerter:** Das gleiche Evidenzbündel enthält einen separaten, viel besser belegten Eintrag – „Hautkrebs" (Rang 9, 23 klinische Studien inkl. mehrerer abgeschlossener Phase-2-BZK-Studien, 20 Veröffentlichungen) – der der bereits bekannten ursprünglichen Indikation von Vismodegib (BZK) statt eines neuartigen Repurposing-Kandidaten zu entsprechen scheint. Dieser sollte von der Repurposing-Überlegung ausgeschlossen werden, bestätigt aber, dass die Arzneimittel-/Evidenzbindung in diesem Datensatz für Indikationen mit echter Abdeckung korrekt funktioniert.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

