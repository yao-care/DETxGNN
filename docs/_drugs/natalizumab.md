---
layout: default
title: Natalizumab
parent: Nur Modellvorhersage (L5)
nav_order: 263
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab: Von Multipler Sklerose / Morbus Crohn zu Bronchitis

## Zusammenfassung in einem Satz

> Natalizumab ist ein monoklonaler Antikörper, der bei Multipler Sklerose und Morbus Crohn eingesetzt wird und durch Blockierung der α4-Integrin-vermittelten Leukozytenmigration über die Blut-Hirn-Schranke und die Darmmukosa wirkt.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam bei **Bronchitis** ist, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** unterstützt, und der Mechanismus weist in die entgegengesetzte Richtung – eine Immunsuppression würde voraussichtlich das Risiko für Atemwegsinfektionen *erhöhen* und nicht behandeln.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Original-Indikation | Multiple Sklerose / Morbus Crohn (in der mechanistischen Begründung erwähnt; nicht durch offizielle Etikettierung bestätigt – dieses Arzneimittel hat keinen Zulassungseintrag in diesem Evidenzpaket) |
| Vorhergesagte neue Indikation | Bronchitis |
| TxGNN-Vorhersagepunktzahl | 99.46% |
| Evidenzstufe | L5 (nur Modellvorhersage) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Daten zum Wirkmechanismus sind in diesem Evidenzpaket nicht verfügbar (ursprüngliches Wirkmechanismus-Feld ist leer). Basierend auf den verfügbaren Informationen ist Natalizumab ein monoklonaler Antikörper gegen α4-Integrin, der den Leukozytentransport über die Blut-Hirn-Schranke und die Darmmukosa hemmt und bei Multipler Sklerose und Morbus Crohn eingesetzt wird – beide Erkrankungen, die durch pathologische Infiltration von Immunzellen in das Gewebe gekennzeichnet sind.

Bronchitis hingegen ist typischerweise eine infektiöse oder reizbedingte Atemwegsentzündung. Es gibt keinen bekannten mechanistischen Zusammenhang zwischen α4-Integrin-Blockade und der Auflösung von Bronchitis. Wenn überhaupt, würde die immunsuppressive Wirkung von Natalizumab voraussichtlich die Clearance von Atemwegserregern *beeinträchtigen* und könnte plausibel die Anfälligkeit für Bronchitis erhöhen, anstatt sie zu behandeln.

Diese Vorhersage scheint daher ein hochbewertetes Artefakt des TxGNN-Modells zu sein, ohne dass stützende mechanistische, präklinische oder klinische Belege vorhanden sind, und die verfügbare Evidenzrichtung für dieses Arzneimittel (siehe Literaturbelege für verwandte Hauterkrankungen, z. B. PMID 32470781, PMID 35646438) zeigt im Allgemeinen, dass Natalizumab entzündliche Erkrankungen **auslöst oder verschlimmert** und nicht behebt – was verstärkt, dass dieser Kandidat ohne weitere Untersuchung nicht als biologisch plausibel interpretiert werden sollte.

---

## Belege aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit ist keine verwandte Literatur verfügbar.

---

## Informationen zum deutschen Markt

Natalizumab hat derzeit keine Zulassung, die in diesem Evidenzpaket verzeichnet ist (0 Lizenzen; Marktstatus: nicht vermarktet). Für den deutschen Markt sind keine Informationen zu Darreichungsform, Produktname oder zugelassenen Indikationen verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

*(Anmerkung: Offizielle TFDA/BfArM-Etikettenwarnungen, Kontraindikationen und DDI-Daten sind als kritische Datenlücke gekennzeichnet – siehe Schlussfolgerung unten.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die höchstbewertete Vorhersage (Bronchitis) hat keine unterstützenden klinischen Studien oder Literatur, und der vorgeschlagene Mechanismus widerspricht direkt der bekannten immunsuppressiven Pharmakologie von Natalizumab – es ist mechanistisch wahrscheinlicher, dass ein Immunsuppressivum Atemwegsinfektionen/Entzündungen *verursacht oder verschärft* als dass es sie behandelt. Dieser Kandidat erfüllt nicht einmal die Mindestschwelle (L4/S1), um das Stadium der reinen Modellvorhersage zu überschreiten.

**Zur Fortsetzung ist Folgendes erforderlich:**
- Offizielle Arzneimittel-Etikettierung / TFDA-Warnungen und Kontraindikationen (derzeit eine kritische Datenlücke – DG001)
- Bestätigter Wirkmechanismus aus DrugBank oder Primärliteratur (derzeit eine hochgradige Datenlücke – DG002)
- Alle präklinischen oder mechanistischen Belege, die speziell die α4-Integrin-/VLA-4-Blockade mit der Auflösung von Atemwegsentzündungen verbinden, bevor dieser Kandidat über „Halten" hinaus voranschreiten kann
- Hinweis: Unter den 5 bewerteten Vorhersagen hat **Psoriasis** (Rang 3) umfangreichere Literatur (18 Arbeiten), zeigt aber *richtungsmäßig widersprüchliche* Signale (hauptsächlich arzneimittelinduziert/verschärfte Psoriasis, eine Fallserie mit Verbesserung) – dies könnte eine separate, gezielte Sicherheits-Wirkmechanismus-Forschungsfrage rechtfertigen, ist aber keine Grundlage, um die obige Entscheidung zu Bronchitis zu ändern.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

