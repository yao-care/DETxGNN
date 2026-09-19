---
layout: default
title: Cemiplimab
parent: Nur Modellvorhersage (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: Von genehmigten Immuno-Onkologie-Indikationen zum Gallenblasen-Adenoplattenzellkarzinom

## Zusammenfassung in einem Satz

Cemiplimab ist ein anti-PD-1-Immuntoleranzpunkt-Inhibitor, dessen Evidence-Pack-Rationale auf vorherige Genehmigungen bei Plattenepithel- und immunogenen Haut-/Lungenkarzinomen verweist. Die Top-Vorhersage des TxGNN-Modells ist **Gallenblasen-Adenoplattenzellkarzinom**, wird derzeit aber durch **0 klinische Studien** und **0 Publikationen** gestützt, was es in die früheste, rein rechnergestützte Evidence-Stufe einordnet.

---

## Schnellübersicht

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Nicht im Evidence Pack verfügbar (keine Einträge zu genehmigten Indikationen; Arzneistoff nicht in diesem Datensatz zugelassen) |
| Vorhergesagte neue Indikation | Gallenblasen-Adenoplattenzellkarzinom |
| TxGNN-Vorhersage-Score | 99,99% |
| Evidence Level | L5 |
| Status auf dem deutschen Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Mechanismus-der-Wirkung-Daten für Cemiplimab sind nicht im strukturierten DrugBank-Datensatz verfügbar, der für diese Evidence Pack verwendet wird (Datenlücke DG002, Schweregrad: Hoch). Allerdings beschreibt der in diese Evidence Pack eingebettete Repurposing-Rationale-Text durchgehend Cemiplimab als **monoklonalen anti-PD-1-Antikörper** und verweist auf seine vorherigen Genehmigungen bei kutanem Plattenepithelkarzinom, Basalzellkarzinom und metastasierendem NSCLC – was darauf hinweist, dass es durch Blockierung des PD-1/PD-L1-Kontrollpunkts wirkt, um die T-Zell-Antitumorreaktion wiederherzustellen.

Für den Top-Kandidaten, Gallenblasen-Adenoplattenzellkarzinom, ist die Rationale explizit schwach: Dies ist ein **Tumor mit gemischter Histologie**, bei dem möglicherweise nur die Plattenepithelkomponente auf PD-1-Blockierung reagieren könnte, während die Reaktionsfähigkeit der Adenokarzinom-Komponente unbekannt ist. Es gibt keine klinischen oder Literaturbelege, die diesen spezifischen Zusammenhang unterstützen – die Vorhersage beruht vollständig auf dem TxGNN-Graph-Embedding-Score.

Im Gegensatz dazu hat unter den anderen neun Kandidaten in dieser Evidence Pack **Basalzellkarzinom des äußeren Ohrs** (Rang 4) eine viel stärkere mechanistische Begründung: Es ist einfach eine anatomisch-lokale Variante des Basalzellkarzinoms, einen Tumortyp, den der Cemiplimab-Rationale als bereits genehmigte Indikation nach Hedgehog-Inhibitor-Versagen anführt, und es wird durch einen Real-World-Fallbericht unterstützt (siehe „Weitere vorhergesagte Indikationen" unten).

---

## Evidenz aus klinischen Studien

Derzeit keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit keine zugehörige Literatur verfügbar.

*Anmerkung: Ein unterstützender Fallbericht (PMID 34157152) existiert für einen anderen Kandidaten in dieser Evidence Pack – Basalzellkarzinom des äußeren Ohrs (Rang 4) – siehe die Tabelle unten.*

---

## Informationen zum deutschen Markt

Keine deutschen Marktgenehmigungen gefunden. Der Marktstatus von Cemiplimab in diesem Datensatz ist **Nicht vermarktet**, mit 0 erfassten Lizenzen.

---

## Weitere in dieser Evidence Pack berücksichtigte vorhergesagte Indikationen

Dieses Kandidaten-Bundle (`TW-DB14707-multi`) enthält 10 TxGNN-vorhergesagte Indikationen. Aus Gründen der Transparenz sind alle unten aufgelistet:

| Rang | Vorhergesagte Indikation | TxGNN-Score | Evidence Level | Entscheidungsstufe | Empfehlung |
|------|--------------------------|-------------|-----------------|---------------------|------------|
| 1 | Gallenblasen-Adenoplattenzellkarzinom | 99,99% | L5 | S0 | Zurückstellen |
| 2 | Glottis-Plattenepithelkarzinom | 99,99% | L5 | S0 | Zurückstellen |
| 3 | Rektales Kloakenkarzinom | 99,99% | L5 | S0 | Zurückstellen |
| 4 | Basalzellkarzinom des äußeren Ohrs | 99,99% | L4 | S1 | Forschungsfrage |
| 5 | Adenoplattenzellkarzinom der Prostata | 99,99% | L5 | S0 | Zurückstellen |
| 6 | Urethrales verruköses Karzinom | 99,99% | L5 | S0 | Zurückstellen |
| 7 | Okkultes Plattenepithelkarzinom der Lunge | 99,99% | L5 | S0 | Zurückstellen |
| 8 | Pankreas-Adenoplattenzellkarzinom | 99,99% | L5 | S0 | Zurückstellen |
| 9 | Nicht-verhorntes sinunasales Plattenepithelkarzinom | 99,99% | L5 | S0 | Zurückstellen |
| 10 | Supraglottis-Plattenepithelkarzinom | 99,99% | L5 | S0 | Zurückstellen |

Rang 4 (Äußeres Ohr BCC) ist der einzige Kandidat mit Belegen aus der Real-World-Praxis (ein Fallbericht, der eine anhaltende Reaktion nach Beendigung der Cemiplimab-Therapie bei fortgeschrittenem BCC beschreibt).

---

## Zytotoxizität

Cemiplimab ist ein onkologisches Therapeutikum (Immuntoleranzpunkt-Inhibitor); dieser Abschnitt ist anwendbar.

| Element | Inhalt |
|---------|---------|
| Zytotoxizitäts-Klassifizierung | Immuntherapie (anti-PD-1-Immuntoleranzpunkt-Inhibitor), basierend auf Mechanismus-Beschreibungen in dieser Evidence Pack |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Überwachungsitems | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |
| Handhabungsschutz | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation |

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

*Anmerkung: BfArM-/TFDA-Warnhinweise und Kontraindikationsdaten sind als Blocking-Datenlücke (DG001) in dieser Evidence Pack gekennzeichnet und konnten nicht abgerufen werden.*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Rationale:**
Die Top-Vorhersage (Gallenblasen-Adenoplattenzellkarzinom) hat keine unterstützenden klinischen Studien oder Literaturbelege und beruht ausschließlich auf einem L5-Model-Score mit einer anerkannten mechanistischen Lücke (gemischte Histologie, unsichere Reaktion). In Kombination mit der Blocking-Schweregrad-Abwesenheit offizieller Sicherheits-/Label-Daten (DG001) und der High-Schweregrad-Abwesenheit von MOA-Daten (DG002) ist die Evidenzbasis unzureichend, um bei diesem Kandidaten voranzukommen.

**Zum Fortschreiten ist Folgendes erforderlich:**
- BfArM-/TFDA-Fachinformationsdaten – Warnhinweise, Kontraindikationen (DG001, Blocking)
- DrugBank-Mechanismus-der-Wirkung-Detail für Cemiplimab (DG002, High)
- Alle präklinischen oder Fall-Level-Belege speziell zum Adenoplattenzellkarzinom der Gallenblase vor Fortschreiten über S0 hinaus
- Erwägen Sie die Umleitung der Forschungspriorität auf **Basalzellkarzinom des äußeren Ohrs** (Rang 4), das bereits L4-Belege und eine „Forschungsfrage"-Entscheidungsstufe hat – dieser Kandidat verdient ein aktualisiertes Literatur-/Registersuche-Review, statt auf Zurückstellen gesetzt zu werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

