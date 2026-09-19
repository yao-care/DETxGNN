---
layout: default
title: Amifampridine
parent: Nur Modellvorhersage (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Amifampridine
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

# Amifampridine: Von ungeklärter Originalindikation zum Glaukom

## Zusammenfassung in einem Satz

Amifampridine (DrugBank ID: DB11640) ist derzeit **nicht auf dem deutschen Markt zugelassen**, und dieses Datenpaket enthält noch keine verifizierten Daten zu ihrer ursprünglichen zugelassenen Indikation oder zum Wirkmechanismus (gekennzeichnet als blockierende/hochgradige Datenlücke).
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **Glaukom** ist, mit einem Vorhersage-Score von **99.71%**, aber derzeit gibt es **0 klinische Studien** und **0 Publikationen**, die diese Richtung unterstützen — das Evidenzlevel ist ausschließlich Modellvorhersage (L5).
Ein zweites, niedrig priorisiertes Kandidaten-Indikationsgebiet, **Akute Intermittierende Porphyrie**, wurde ebenfalls vorhergesagt (Score 99.32%), ähnlich ohne unterstützende Studien oder Literatur.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Originalindikation | In aktuellen Datenquellen nicht verfügbar (siehe Datenlücken unten) |
| Vorhergesagte neue Indikation | Glaukom |
| TxGNN-Vorhersage-Score | 99.71% |
| Evidenzlevel | L5 (nur Modellvorhersage, keine klinische oder Literaturunterstützung) |
| Marktstatus Deutschland | ✗ Not Marketed (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten (MOA) für Amifampridine in diesem Datenpaket nicht verfügbar (Datenlücke DG002, Schweregrad Hoch), und auch keine ursprüngliche Indikation wurde aufgezeichnet. Dies schränkt erheblich ein, wie zuverlässig die Rationale von ursprünglicher Indikation zu neuer Indikation bewertet werden kann.

Basierend auf der vom TxGNN-Modell selbst generierten Rationale wird Amifampridine als breit wirksamer Blocker von spannungsabhängigen Kalium-(Kv-)Kanälen verstanden, mit seiner etablierten Pharmakologie, die auf der Verbesserung der präsynaptischen Acetylcholin-Freisetzung an der neuromuskulären Verbindung zentriert ist. Die vorgeschlagene Verbindung zum Glaukom ist eine indirekte, systemübergreifende Extrapolation: Die Sekretion von Kammerwasser durch das Ziliarepithel und der Abfluss durch das Trabekelwerk beinhalten ebenfalls verschiedene K+-Kanäle (z.B. Kir, KCa), daher könnte ein Kalium-Kanal-Modulator theoretisch den Augeninnendruck (IOP) beeinflussen. Allerdings ist dies **keine** direkte mechanistische Verbindung zur Glaukom-Pathologie (z.B. Trabekelwerk-Degeneration, Apoptose retinaler Ganglienzellen), und die Wirkungsrichtung von K+-Kanal-Blockade vs. -Aktivierung auf den IOP ist in der Literatur inkonsistent. Es gibt keine Tiermodelle oder ex vivo Augengewebedaten, die diese Verbindung unterstützen — das Modell selbst charakterisiert dies als „stark spekulativ".

Für den zweiten Kandidaten, Akute Intermittierende Porphyrie (AIP), leitet sich die Rationale von einer Analogie zu Amifampridines bekanntem Wirkmechanismus an der neuromuskulären Verbindung (verwendet bei Lambert-Eaton-Syndrom-ähnlichen Indikationen) ab: AIP kann autonome Dysfunktion und axonale Neuropathie mit assoziierter Muskelschwäche verursachen, und die Verbesserung der ACh-Freisetzung könnte theoretisch symptomatischen Nutzen bieten. Allerdings ist die Kernpathologie der AIP ein Defekt in der Hämbiosynthese (Porphobilinogen-Deaminase-Mangel) und axonale Degeneration — keine Störung der präsynaptischen Neurotransmitter-Freisetzung — daher ist dies wiederum eine spekulative mechanistische Analogie statt einer direkten pathologischen Übereinstimmung, ohne verfügbare präklinische oder klinische Daten.

Da beide Kandidaten keine unterstützenden klinischen Studien- oder Literaturbelege haben und sich ausschließlich auf indirekte mechanistische Begründung verlassen, erhebt sich keiner der beiden Vorhersagen über das L5-Evidenzlevel (nur Modellvorhersage).

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Literaturbelege

Derzeit keine verwandte Literatur verfügbar

---

## Informationen zum deutschen Markt

Amifampridine hält derzeit **keine Marktzulassungen in Deutschland** (Marktstatus: Not marketed / Not Marketed; Gesamtzulassungen: 0). Keine Produkt-, Darreichungsform- oder zugelassenen Indikationsdaten sind verfügbar zur Zusammenfassung.

---

## Sicherheitsüberlegungen

Bitte beziehen Sie sich auf die Fachinformation für Sicherheitsinformationen.

> **Hinweis:** Dieses Datenpaket markiert das Fehlen von TFDA-Fachinformations-Warnungen/Kontraindikations-Daten als eine **Blockierend**-Datenlücke (DG001), die verhindert, dass dieser Kandidat in die Standard-Sicherheits-Vorprüfungsphase (S1) eintritt. Keine DDI-Datensätze wurden gefunden (Abfragestatus: not_found).

---

## Weitere vorhergesagte Indikation (nur als Referenz)

| Element | Inhalt |
|---------|--------|
| Erkrankung | Akute Intermittierende Porphyrie |
| TxGNN-Vorhersage-Score | 99.32% |
| Evidenzlevel | L5 |
| Klinische Studien / Literatur | Keine gefunden |
| Empfehlung | Zurückstellen |

Die mechanistische Rationale für diesen Kandidaten ist eine indirekte Analogie zwischen Amifampridines Pharmakologie an der neuromuskulären Verbindung und AIP-assoziierter neuropathischer Schwäche, statt einer Übereinstimmung mit der Kern-Hämbiosynthese-Pathologie der AIP. Keine klinischen, präklinischen oder Literaturbelege unterstützen derzeit diese Richtung.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Beide vorhergesagten Indikationen (Glaukom und Akute Intermittierende Porphyrie) werden nur durch TxGNN-Modell-Scores und spekulative mechanistische Begründung unterstützt, ohne identifizierte klinische Studien oder Literatur für beide. Darüber hinaus verhindert eine **Blockierend**-schweregrad-Datenlücke (fehlende TFDA-Bezeichnung/Warnungen, DG001), dass dieser Kandidat überhaupt die Standard-Sicherheits-Vorprüfungsphase (S1) erreicht, und das Arzneimittel ist derzeit nicht in Deutschland zugelassen.

**Um fortzufahren, wird Folgendes benötigt:**
- TFDA/Regulierungs-Fachinformationen (Warnungen, Kontraindikationen), um den S1-Sicherheits-Vorprüfungsblocker zu beseitigen (DG001)
- Verifizierte Wirkmechanismus- und ursprüngliche zugelassene Indikationsdaten von DrugBank oder einer anderen autoritativen Quelle (DG002)
- Präklinische oder in-vitro-Belege, die Amifampridines K+-Kanal-Aktivität mit der IOP-Regulierung verbinden (für den Glaukom-Kandidaten)
- Alle Fallberichte, Beobachtungsdaten oder mechanistische Studien, die Amifampridine mit AIP-bezogener Neuropathie verbinden (für den sekundären Kandidaten)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

