---
layout: default
title: Dantrolene
parent: Nur Modellvorhersage (L5)
nav_order: 129
evidence_level: L5
indication_count: 9
---

# Dantrolene
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Dantrolen: Von Malignem Hyperthermie zu Malignem Hyperthermie (Suszeptibilität)

## Zusammenfassung

Dantrolen wurde ursprünglich zur Behandlung der Malignen Hyperthermie zugelassen. Das TxGNN-Modell sagt als Top-Treffer **Maligne Hyperthermie (Suszeptibilität)** voraus, also im Kern die bereits bestehende Indikation. Für diese Richtung liegen **keine registrierten klinischen Studien**, aber **19 Publikationen** vor, darunter zwei Konsensus-Leitlinien. Es handelt sich daher nicht um ein echtes Repurposing, sondern um eine Bestätigung der Originalindikation.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Maligne Hyperthermie |
| Vorhergesagte neue Indikation | Maligne Hyperthermie, Suszeptibilität (identisch mit der Originalindikation) |
| TxGNN-Vorhersagewert | 99,93 % |
| Evidenzniveau | L1 laut Bewertung der Datenbasis (leitlinienbasiert; es sind jedoch keine Phase-3-RCTs aufgeführt, streng nach den Regeln entspräche dies eher L3) |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl Zulassungen | 1 (0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Proceed with Guardrails |

---

## Warum ist diese Vorhersage plausibel?

Zu Dantrolen liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Wirkmechanismus-Angaben aus DrugBank vor. Aus der Literatur ist jedoch bekannt, dass Dantrolen den Ryanodin-Rezeptor des Skelettmuskels (RyR1) hemmt und die pathologische Ca²⁺-Freisetzung aus dem sarkoplasmatischen Retikulum verringert. Dieser Defekt steht im Zentrum der Malignen Hyperthermie. Eine Studie aus 2017 (PMID 28373535) zeigt zudem, dass Dantrolen Mg²⁺ benötigt, um die Krise zu beenden.

Da die vorhergesagte Erkrankung mit der Originalindikation praktisch identisch ist, ist die Vorhersage plausibel, liefert aber keine neue Therapieoption. Interessanter sind die weiteren Vorhersagen mit RYR1-Bezug: King-Denborough-Syndrom, zentrale Kernmyopathie (Central Core Disease), Multiminicore-Erkrankung und zentronukleäre Myopathie. Hier würde Dantrolen vor allem das MH-Risiko senken, nicht die zugrunde liegende Myopathie behandeln. Für periodische Lähmungen (hypokaliämisch, thyreotoxisch) ist ein Mechanismus anhand der vorliegenden Daten nicht erkennbar.

Hinweis: Der Marktstatus „nur erloschen" sollte geprüft werden, da andere Dantrolen-Formulierungen (z. B. Ryanodex) laut Bewertung erhältlich sind.

---

## Literaturevidenz

Klinische Studien sind nicht registriert (aktuell keine zugehörigen klinischen Studien). Die Literatur besteht überwiegend aus Übersichtsarbeiten und Leitlinien:

| PMID | Jahr | Typ | Journal | Kernaussage |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Leitlinie | Anaesthesia | Leitlinie der Association of Anaesthetists zur Malignen Hyperthermie (2020) |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Konsensus-Leitlinie | Br J Anaesth | Europäische MH-Gruppe: perioperatives Management bei Verdacht oder Suszeptibilität; keine interventionellen Studien verfügbar |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | Übersicht zu Pathophysiologie, Inzidenz (1:10.000 bis 1:250.000 Anästhesien) und Therapie |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Expertenübersicht zu Epidemiologie und Management bei kritisch Kranken |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | Aktuelles zur MH; verbesserte Mortalität |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistisch | PNAS | Dantrolen benötigt Mg²⁺, um die MH-Krise zu beenden |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet J Rare Dis | Klinische Übersicht zur MH |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Review | Korean J Anesthesiol | Autosomal-dominanter Erbgang mit variabler Expression |
| [25989378](https://pubmed.ncbi.nlm.nih.gov/25989378/) | 2015 | Übersicht | Acta Anaesthesiol Scand | Skandinavisches Update; RYR1-Mutationen in der Mehrzahl der Fälle |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Übersicht | Postgrad Med J | Dantrolen-Natrium als wesentliche Therapie |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/006009 | Agilus (Norgine B.V.) | nicht angegeben | Maligne Hyperthermie (Status: erloschen) |

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph (nicht aus Packungsbeilage):** Lebererkrankung, Gallenblasenerkrankung, Myopathie, Muskelerkrankung, Skelettmuskelerkrankung, familiäre periodische Paralyse, Lungenerkrankung, seltene Lungenerkrankung.
- **Arzneimittelwechselwirkungen:** 72 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** eingestuft: Morphin und liposomales Morphin. Als **mäßig (Moderate)** eingestuft u. a.: Dronabinol, Metoclopramid, Nabilon, Naltrexon, Opium, Sibutramin, Ethanol, Promethazin. Weitere (z. B. Pantoprazol, Metformin, Omeprazol, Simvastatin, Clarithromycin, Clopidogrel) sind ohne Schweregrad („unbekannt") geführt.

Für Warnhinweise und Kontraindikationen der Fachinformation bitte die Packungsbeilage konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Dantrolen ist bei Maligner Hyperthermie leitlinienkonform etabliert, die Vorhersage bestätigt jedoch nur die Originalindikation. Kontrollierte Studien fehlen, und die Marktverfügbarkeit in Deutschland ist unklar. Die RYR1-verwandten Myopathien (King-Denborough, Central Core Disease, zentronukleäre Myopathie) bleiben Forschungsfragen. Multiminicore-Erkrankung und die periodischen Lähmungen sind rein rechnerische Vorhersagen (Hold).

**Für das weitere Vorgehen erforderlich:**
- Prüfung der aktuellen Verfügbarkeit von Dantrolen-Präparaten in Deutschland (erloschene Agilus-Zulassung vs. andere Formulierungen)
- Beschaffung und Auswertung der Fachinformation (Warnhinweise, Kontraindikationen); dies ist derzeit eine blockierende Datenlücke für das Sicherheits-Screening
- Ergänzung der Wirkmechanismus-Daten aus DrugBank
- Klärung der Sicherheit bei Leber- und Muskelerkrankungen sowie bei Opioid-Komedikation (insbesondere Morphin)
- Für die RYR1-assoziierten Erkrankungen: gezielte Bewertung des prophylaktischen Nutzens zur MH-Risikominderung
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

