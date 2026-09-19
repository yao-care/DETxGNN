---
layout: default
title: Ciclesonide
parent: Nur Modellvorhersage (L5)
nav_order: 102
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Ciclesonid: Von Asthma zu Atopischer Dermatitis

## Zusammenfassung in einem Satz

> Ciclesonid ist ein inhaliertes Kortikosteroid (ICS)-Prodrug, das vor allem als Wirkstoff in **Alvesco** zur Asthma-Kontrolle bekannt ist.
> Das TxGNN-Modell prognostiziert, dass es wirksam sein könnte für **Atopische Dermatitis**,
> aber diese Richtung wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — eine auf rein dem Wissensgraph basierende Vorhersage ohne empirische Evidenz.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Asthma (inhaliertes Kortikosteroid; bestätigt nur über die bekannte ICS-Klassifizierung des Arzneimittels, nicht durch formale behördliche Dokumentation) |
| Vorhergesagte neue Indikation | Atopische Dermatitis |
| TxGNN-Vorhersage-Score | 99.96% |
| Evidenzstufe | L5 |
| Taiwan-Marktstatus | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage begründet?

Formale Wirkmechanismus-Daten für Ciclesonid sind nicht aus der behördlichen Datenquelle verfügbar, die zur Erstellung dieses Evidence Packs verwendet wurde (Datenlücke). Das Evidence Pack selbst bestätigt jedoch in seiner Umwandlungsrationale für einen verwandten Kandidaten, dass Ciclesonid ein inhaliertes Kortikosteroid (ICS)-Prodrug ist, das durch pulmonale Esterasen zu seinem aktiven Metaboliten Des-Ciclesonid aktiviert wird, das an den Glucocorticoid-Rezeptor bindet und die Atemwegsentzündung unterdrückt. Dies ist der gut etablierte, bereits zugelassene Wirkmechanismus von Ciclesonid für Asthma (z. B. Alvesco) – keine neue Anwendung.

Atopische Dermatitis und Asthma gehören beide zum atopischen/Th2-gesteuerten Spektrum von Entzündungserkrankungen, und topische Kortikosteroide sind tatsächlich eine Säule der Ekzem-Behandlung, sodass ein Glucocorticoid-Mechanismus für Hautentzündungen nicht grundsätzlich unplausibel ist. Dies gibt der Vorhersage eine oberflächliche theoretische Grundlage.

Die praktische Fallstärke ist jedoch schwach: Ciclesonid ist derzeit nur zur Inhalation formuliert, ohne pharmakokinetische oder Sicherheitsdaten für kutane/topische Anwendung. Das Evidence Pack selbst markiert diese mechanistische Verbindung ausdrücklich als „schwach" (機轉關聯薄弱) aufgrund der Nichtübereinstimmung der Verabreichungsroute. Ohne eine topische Formulierung und ein dermatologisches PK/Sicherheitspaket kann diese Vorhersage derzeit nicht in eine testbare klinische Hypothese übersetzt werden.

---

## Evidenz aus klinischen Studien

Derzeit keine zugehörigen klinischen Studien registriert

---

## Literaturbeweise

Derzeit keine zugehörige Literatur verfügbar

---

## Taiwan-Marktinformationen

Ciclesonid wird in Taiwan derzeit **nicht vermarktet** — keine Produktzulassungen sind dokumentiert (0 Lizenzen). Für dieses Arzneimittel auf diesem Markt sind keine genehmigten Indikationstexte, Darreichungsformen oder Zulassungsnummern-Daten verfügbar.

---

## Sicherheitsaspekte

Weitere Informationen zur Sicherheit finden Sie in der Gebrauchsinformation (für dieses Arzneimittel sind im aktuellen Datensatz keine strukturierten Warnungen, Kontraindikationen oder Wechselwirkungsdaten verfügbar, und es wird in Taiwan nicht vermarktet).

**Beachtenswertes Sicherheitssignal aus der Literatur (nicht spezifisch für die Ekzem-Vorhersage):** Ein Fallbericht (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), *Contact Dermatitis*, 2012) beschreibt systemische allergische Dermatitis verursacht durch inhaliertes **Budesonid**, wobei Epikutantestung **Kreuzreaktivität mit Ciclesonid** als strukturell verwandtes ICS zeigt. Dies ist ein Nebenwirkungs-Signal, kein Nachweis therapeutischen Nutzens, und sollte als Vorsichtsflag behandelt werden – besonders relevant für jede zukünftige dermatologische Umwidmung dieses Arzneimittels.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die Vorhersage der atopischen Dermatitis wird nur durch einen TxGNN-Modell-Score (L5) gestützt, ohne klinische Studien und Publikationen, und das Arzneimittel hat derzeit keine topische/dermatologische Formulierung oder routenkompatible Sicherheitsdaten — die mechanistische Verbindung wird sogar im Evidence Pack selbst ausdrücklich als schwach bewertet.

**Um fortzufahren, ist Folgendes erforderlich:**
- Formale TFDA/Herstellerkennzeichnungsdaten (Warnungen, Kontraindikationen, Wechselwirkungen) — derzeit eine blockierende Datenlücke
- Bestätigte ursprüngliche Indikation und MOA direkt aus DrugBank/behördlichen Unterlagen (derzeit nur aus sekundären Begründungstexten abgeleitet)
- Machbarkeitsbewertung und PK/Sicherheitsdaten für eine topische/dermatologische Formulierung von Ciclesonid, da derzeit keine kutane Route existiert
- Mindestens präklinische oder frühe dermatologische Wirksamkeitsdaten, bevor dieser Kandidat über S0 hinaus vorrücken kann

**Zum Kontext:** zwei weitere Kandidaten in diesem Evidence Pack tragen stärkere, handlungsreife Signale und könnten separate Nachverfolgung rechtfertigen — *Bronchitis* (L4, Entscheidungsstadium S1, Literaturunterstützung über COPD-Leitlinie) und *asthma-bezogene Anfälligkeit* (L1, Entscheidungsstadium S3), wobei letztere im Wesentlichen Ciclesonids bereits genehmigter Asthma-Indikation widerspiegelt statt einer echten neuen Anwendung.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

