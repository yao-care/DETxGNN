---
layout: default
title: Lapatinib
parent: Nur Modellvorhersage (L5)
nav_order: 222
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: Von HER2-überexprimiertem Mammakarzinom zu Dermatofibrosarcoma Protuberans

## Einleitung in einem Satz

> Lapatinib ist ein dualer EGFR/HER2-Tyrosinkinase-Inhibitor, der ursprünglich für HER2-überexprimierte Mammakarzinome eingesetzt wird.
> Das TxGNN-Modell prognostiziert, dass es wirksam gegen **Dermatofibrosarcoma Protuberans (DFSP)** sein könnte,
> doch diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt, und die zugrunde liegende mechanistische Rationale ist schwach.

## Schnellabriss

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | HER2-überexprimiertes Mammakarzinom *(abgeleitet aus dem Text der Umwidmungsrationale; nicht bestätigt durch formale Zulassungs-/Fachinformationsdaten)* |
| Vorhergesagte neue Indikation | Dermatofibrosarcoma Protuberans |
| TxGNN-Vorhersage-Score | 99.30% |
| Evidenzlevel | L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur) |
| Marktsituation Deutschland | ✗ Nicht im Handel (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

## Warum ist diese Vorhersage nachvollziehbar?

Derzeit sind detaillierte Mechanismus-der-Wirkung-Daten (MOA) nicht in strukturierter Form verfügbar. Basierend auf dem Rationaltext im Evidenzpaket ist Lapatinib ein dualer EGFR/HER2-(ErbB1/ErbB2-)Tyrosinkinase-Inhibitor, der primär für HER2-überexprimierte Mammakarzinome eingesetzt wird.

Jedoch ist die biologische Verbindung zwischen diesem MOA und DFSP schwach. DFSP wird überwiegend durch die **COL1A1-PDGFB-Fusionierung** angetrieben, die zu einer konstitutiven Aktivierung von PDGFRB führt — ein Signalweg, der durch Imatinib (einen PDGFR-Inhibitor) adressiert wird, nicht durch EGFR/HER2-Inhibitoren. Es gibt derzeit keine bekannte Literatur, die eine klinisch bedeutsame EGFR- oder HER2-Überexpression oder Treibermutationen in DFSP-Tumorzellen demonstriert.

Diese Vorhersage sollte daher als **TxGNN-Wissensgraph-Assoziation allein** interpretiert werden, der zu diesem Zeitpunkt unabhängige biologische Plausibilität fehlt, und sollte mit hohem Skeptizismus behandelt werden.

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

## Literaturevidenz

Derzeit keine verwandte Literatur verfügbar.

## Marktsituation Deutschland

Lapatinib wird gemäß diesem Evidenzpaket in Deutschland derzeit **nicht vermarktet** (0 Zulassungen gefunden); keine Produktdaten/Darreichungsform/Indikationsdaten verfügbar.

## Zytotoxizität

Lapatinib ist ein antineoplastisches Mittel (Mammakarzinom-Indikation), klassifiziert als zielgerichtete Therapie statt klassisches Zytostatikum.

| Element | Inhalt |
|---------|---------|
| Zytotoxizität-Klassifizierung | Zielgerichtete Therapie (dualer EGFR/HER2-Tyrosinkinase-Inhibitor) |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Emetogenität-Klassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Überwachungspunkte | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Handhabungsschutz | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |

## Sicherheitsaspekte

Bitte beachten Sie die Sicherheitsinformationen der Fachinformation.

*(Hinweis: Warnhinweise und Kontraindikationen der Fachinformation (TFDA/BfArM) sind derzeit nicht verfügbar — dies wird als Blockierende Datenlücke gekennzeichnet und muss behoben werden, bevor eine Sicherheitsprüfung erfolgen kann.)*

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die Vorhersage wird nur durch einen TxGNN-Modell-Score gestützt (L5, keine klinischen Studien oder Literatur), der vorgeschlagene Mechanismus stimmt nicht mit dem bekannten Treiberpfad von DFSP überein (COL1A1-PDGFB/PDGFRB, nicht EGFR/HER2), und das Arzneimittel wird derzeit nicht in Deutschland vermarktet. Darüber hinaus fehlen die Sicherheitsdaten der TFDA-Fachinformation (Warnhinweise/Kontraindikationen), was eine blockierende Lücke für jede Sicherheitsbewertung darstellt.

**Um voranzukommen, ist Folgendes erforderlich:**
- TFDA-Fachinformation (Warnhinweise/Kontraindikationen) — Blockierende Lücke, erforderlich vor S1-Sicherheitsprüfung
- Bestätigte ursprüngliche MOA- und Indikationsdaten aus DrugBank/behördlicher Quelle
- Präklinische Evidenz der EGFR/HER2-Relevanz in der DFSP-Tumorbiologie, falls vorhanden
- Klinische Studie oder Fallbericht-Evidenz, die Lapatinib speziell in DFSP oder PDGFR-getriebenen Sarkomen bewertet

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

