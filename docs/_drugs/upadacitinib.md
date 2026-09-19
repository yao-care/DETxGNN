---
layout: default
title: Upadacitinib
parent: Nur Modellvorhersage (L5)
nav_order: 417
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Upadacitinib: Von Autoimmun-/Entzündungserkrankungen zum Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## Zusammenfassung in einem Satz

Upadacitinib ist ein selektiver JAK1-Inhibitor, der ursprünglich für autoimmun- und entzündliche Erkrankungen entwickelt wurde; seine detaillierte ursprüngliche Indikation und Wirkmechanismus-Daten sind in diesem Evidenzpaket noch nicht verfügbar. Das TxGNN-Modell weist einen hohen Ähnlichkeitsscore dem **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, einem seltenen angeborenen Skelett-Augen-Malformationssyndrom, zu, aber diese Vorhersage wird derzeit durch **null klinische Studien** und **null Publikationen** gestützt, und die mechanistische Analyse des Evidenzpakets selbst kennzeichnet dies als wahrscheinlich Modellrauschen anstelle einer biologisch plausiblen Hypothese.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Im Evidenzpaket nicht angegeben (JAK1-Inhibitor-Klasse, typischerweise autoimmun-/Entzündungserkrankungen) |
| Vorhergesagte neue Indikation | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN-Vorhersagescore | 99.61% |
| Evidenzgrad | L5 |
| Markt-Status Deutschland | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Hold** |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten in diesem Evidenzpaket nicht verfügbar (`original_moa` ist nicht gefüllt). Basierend auf der bereitgestellten Umwidmungsrationale ist Upadacitinib ein selektiver JAK1-Inhibitor, der die Zytokin-Signalisierung moduliert (IL-6, IFN, IL-2-Familie, etc.), in Einklang mit seiner bekannten Verwendung bei autoimmun-/Entzündungserkrankungen.

Die vorhergesagte Indikation — Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome — ist eine seltene angeborene Störung, die durch embryonale Gendefekte verursacht wird, nicht durch chronische Entzündungen oder JAK-STAT-vermittelte Pathologie. Die mechanistische Bewertung des Evidenzpakets selbst besagt, dass es **keine bekannte biologische Verbindung** zwischen JAK1-Inhibition und diesem strukturellen Entwicklungssyndrom gibt, und führt den hohen TxGNN-Score auf Graph-Embedding-Ähnlichkeitsartefakte zurück anstelle einer echten pharmakologischen Hypothese.

Ein zweiter Kandidat, Brachydaktylie-Syndaktylie-Syndrom (Score 99,58%, Rang 5278), zeigt das gleiche Muster: eine Gliedmaßen-Entwicklungsstörung (typischerweise mit HOX-Gen/BMP-Hedgehog-Weg verknüpft) ohne plausible Verbindung zur JAK1-Inhibition und ohne unterstützende Studien oder Literatur. Beide höher bewerteten Vorhersagen in diesem Batch sollten als Modell-Artefakte mit niedriger Konfidenz und nicht als umsetzbare Umwidmungskandidaten behandelt werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktinformationen Deutschland

Upadacitinib hält derzeit **keine Marktgenehmigung** in diesem Rechtsraum (Markt-Status: Nicht im Handel, 0 Zulassungen). Keine Produkt-/Lizenzdaten verfügbar.

---

## Sicherheitserwägungen

Bitte beziehen Sie sich auf die Fachinformation für Sicherheitsinformationen.

*(Hinweis: TFDA-Etikett-Warnungen/Kontraindikationen und DDI-Daten fehlen derzeit — siehe `DG001`, eine Sicherheitsdaten-Lücke von Blockierendem Schweregrad, die eine S1-Sicherheitsvorab-Bewertung verhindert.)*

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Rationale:**
Die vorhergesagte Indikation weist keine unterstützenden klinischen Studien oder Literatur auf (Evidenzgrad L5), und die mechanistische Analyse des Evidenzpakets selbst bewertet die Wirkstoff-Krankheits-Verbindung als biologisch implausibel, wahrscheinlich Embedding-Ähnlichkeitsrauschen widerspiegelnd anstelle eines echten Signals. Kombiniert mit einer Sicherheitsdaten-Lücke von Blockierendem Schweregrad (TFDA-Etikett nicht verfügbar) und fehlenden MOA-/ursprünglichen-Indikations-Daten gibt es unzureichende Grundlage, um diesen Kandidaten voranzutreiben.

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA-Etikett (Warnungen, Kontraindikationen) zur Auflösung von `DG001` (Blockierend)
- Bestätigte ursprüngliche MOA und genehmigte Indikation(en) via DrugBank/behördliche Quelle (`DG002`)
- Unabhängige mechanistische oder präklinische Rationale, die JAK1-Inhibition mit diesem Syndrom verknüpft, bevor weitere Überprüfungsressourcen zugewiesen werden
- Falls keine solche Rationale auftaucht, deprioritisieren Sie sowohl Rang-1- als auch Rang-2-Kandidaten als Vorhersagen mit niedrigem Wert

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

