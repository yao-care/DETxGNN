---
layout: default
title: Vortioxetine
parent: Mittlere Evidenz (L3-L4)
nav_order: 430
evidence_level: L4
indication_count: 5
---

# Vortioxetine
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **5** 
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

# Vortioxetin: Von Major Depression zu Neurotischer Störung

## Zusammenfassung in einem Satz

> Vortioxetin ist ein multimodales Serotonin-Antidepressivum, das in der Literatur als für Major Depression zugelassen berichtet wird; es ist kein lokaler behördlicher Indikationstext verfügbar, da das Produkt derzeit nicht vermarktet wird.
> Die Höchstrangbewertung des TxGNN-Modells ist **Neurotische Störung**,
> aber dieses spezifische Label wird derzeit nur durch **1 klinische Studie** und **1 Publikation** gestützt, beide mit geringer direkter Relevanz.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert im behördlichen Dossier (keine Lizenzen auf Datei); gemäß unterstützender Literatur (PMID 29189941) ist Vortioxetin für **Major Depression** zugelassen |
| Vorhergesagte neue Indikation | Neurotische Störung |
| TxGNN-Vorhersageergebnis | 99.24% |
| Evidenzgrad | L4 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten für diesen Kandidaten sind im Evidenzpaket nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der für diesen Kandidaten abgerufenen unterstützenden Literatur (PMID 25016186, PMID 29189941) ist Vortioxetin ein multimodales Antidepressivum, das als Serotonin-Transporter (SERT)-Inhibitor in Kombination mit Antagonismus an den 5-HT3-, 5-HT7- und 5-HT1D-Rezeptoren, Partialagonismus an 5-HT1B und Agonismus an 5-HT1A wirkt — es erhöht die serotoninerge, noradrenerge, dopaminerge, cholinerge, histaminerge und glutamaterge Neurotransmission in Hirnregionen, die an der Stimmungsregulation beteiligt sind. Seine Wirksamkeit bei Major Depression wurde über mehrere Phase-3-Registrierungsstudien demonstriert, die an anderer Stelle in diesem Evidenzpaket zitiert werden.

„Neurotische Störung" ist eine breite, weitgehend veraltete diagnostische Kategorie, die historisch Angst-, depressive und somatoforme Symptomgruppen umfasst. Es gibt konzeptionelle Überschneidungen zwischen dieser Kategorie und Major Depression, die eine plausible — aber nicht spezifische — mechanistische Begründung für TxGNNs Vorhersage bietet. Allerdings kennzeichnet das Evidenzpaket selbst dies: die einzige verknüpfte Studie (NCT04446039) ist eine große retrospektive Kohortenstudie mit Daten aus der realen Welt unter Verwendung nationaler Abrechnungsdaten, die Muster der Medikamentennutzung und Risiken ungünstiger Ergebnisse bei häufig verwendeten Antidepressiva vergleicht — sie wurde nicht speziell um „neurotische Störung" als Einschlusskriterium gestaltet — und die einzige verknüpfte Publikation ist eine einzelne fallbasierte Übersicht der „neurotischen Depression" (ein verwandtes, aber unterschiedliches Label). Das Begründungsfeld des Modells selbst vermerkt explizit, dass die Evidenz „unzureichend ist, um eine spezifische klinische Entscheidung" für dieses Label zu unterstützen.

**Anmerkung:** Innerhalb desselben Evidenzpakets ist der Rang-3-Kandidat — **Melancholie** — wesentlich besser gestützt (6 abgeschlossene Phase-3-RCTs, die Vortioxetin direkt bei Major Depression testen, Evidenzgrad L1, Empfehlung „Mit Schutzmaßnahmen voranschreiten"). Melancholie ist ein anerkannter schwerer/biologischer Major-Depression-Subtyp und kann ein verwertbareres Repurposing-Signal darstellen als das Höchstrangk-Label „Neurotische Störung"; dies sollte bei der Priorisierung der nächsten Schritte berücksichtigt werden.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Rekrutierung | Wesentliche Erkenntnisse |
|---------|------|--------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/V | Abgeschlossen | 370,212 | Retrospektive Kohortenstudie mit realen Daten unter Verwendung nationaler Anspruchsdaten, die Muster der Medikamentennutzung und das Risiko ungünstiger Ergebnisse bei häufig verwendeten Antidepressiva vergleicht; nicht speziell um „neurotische Störung" als Einschlusskriterium herum gestaltet (Relevanzbewertung C). |

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Wesentliche Erkenntnisse |
|------|-----|------|--------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Übersicht (Fallbericht) | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Fallbericht über neurotische Depression mit Diskussion persönlicher Prädisposition und klinischer Merkmale; befürwortet einen kombinierten Ansatz aus Antidepressiva und kognitiver Verhaltenstherapie. Bewertet Vortioxetin nicht direkt. |

---

## Marktinformation Deutschland

Derzeit nicht auf dem deutschen Markt vermarktet — keine Produktzulassungen sind auf Datei für dieses Arzneimittel vorhanden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Anmerkung: Die für eine vollständige S1-Sicherheitsbewertung erforderlichen TFDA/BfArM-Label- und Warnungsdaten stellen derzeit einen Blocking Data Gap in diesem Evidenzpaket dar — siehe Nächste Schritte unten.)*

---

## Schlussfolgerung und Nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die Höchstrangbewertung der TxGNN-Vorhersage („Neurotische Störung") wird nur durch eine nicht spezifische retrospektive Kohortenstudie mit realen Daten und eine einzelne fallbasierte Übersicht gestützt, was Evidenzgrad L4 entspricht. Dies ist unzureichend, um über das anfängliche Screening hinaus für dieses spezifische Indikationslabel voranschreiten zu lassen.

**Um voranschreiten zu können, ist Folgendes erforderlich:**
- Abrufen von TFDA/BfArM-Label-Warnungen und Kontraindikationen (derzeit ein Blocking Data Gap; erforderlich vor jeder S1-Sicherheitsbewertung)
- Erhalten einer bestätigten Wirkmechanismus-Dokumentation von DrugBank (derzeit ein High-Severity Data Gap)
- Klären, ob „Neurotische Störung" einer modernen, verwertbaren diagnostischen Entität entspricht oder ob die Anstrengungen stattdessen zu dem deutlich besseren gestützten **Melancholie**-Kandidaten (L1, 6 Phase-3-RCTs) umgeleitet werden sollten, der im selben Vorhersage-Batch identifiziert wurde
- Falls Neurotische Störung spezifisch verfolgt wird, nach Studien mit Einschlusskriterien suchen, die diesem diagnostischen Label entsprechen, anstelle von allgemeinen Antidepressiva-Vergleichskohorten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

