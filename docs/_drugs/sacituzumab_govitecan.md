---
layout: default
title: Sacituzumab Govitecan
parent: Nur Modellvorhersage (L5)
nav_order: 357
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Sacituzumab Govitecan: Von nicht eingetragener ursprünglicher Indikation zu arzneimittelinduzierter Osteoporose

## Zusammenfassung in einem Satz

Die ursprüngliche Indikation und der Wirkmechanismus von Sacituzumab Govitecan sind im aktuellen Datensatz nicht verfügbar. Basierend auf der mit diesem Evidenzpaket bereitgestellten Umwidmungsrationale ist dieses Arzneimittel ein Trop-2-zielgerichtetes Antikörper-Wirkstoff-Konjugat (ADC), dessen Nutzlast SN-38, einen zytotoxischen Topoisomerase-I-Hemmer, freisetzt. Das TxGNN-Modell sagt eine mögliche Wirksamkeit für **arzneimittelinduzierte Osteoporose** voraus, jedoch mit **keinen klinischen Studien und keiner Literatur**, die diese Richtung derzeit unterstützen — dies ist ein Signal aus reiner Modellvorhersage (L5), das die Rationale selbst als biologisch implausibel kennzeichnet.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Im aktuellen Datensatz nicht verfügbar (Arzneimittel noch nicht auf dem Markt; keine eingetragene Indikation vorhanden) |
| Vorhergesagte neue Indikation | Arzneimittelinduzierte Osteoporose |
| TxGNN-Vorhersage-Score | 99.78% |
| Evidenzebene | L5 |
| Marktstatus Deutschland | ✗ Nicht auf dem Markt |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten sind für Sacituzumab Govitecan im Datensatz derzeit nicht verfügbar. Basierend auf der mit diesem Evidenzpaket bereitgestellten Umwidmungsrationale ist das Arzneimittel ein Trop-2-zielgerichtetes Antikörper-Wirkstoff-Konjugat, dessen Nutzlast SN-38 (der aktive zytotoxische Metabolit von Irinotecan) ein Topoisomerase-I-Hemmer — ein konventionelles zytotoxisches Chemotherapie-Arzneimittel — ist. Im Datensatz ist keine ursprüngliche Indikation eingetragen, daher kann ein direkter Vergleich zwischen der ursprünglichen und der vorhergesagten Indikation nicht durchgeführt werden.

Noch wichtiger: Die Rationale argumentiert **gegen** biologische Plausibilität für diese Vorhersage: Es gibt keine bekannte mechanistische Verbindung zwischen Trop-2/SN-38-Aktivität und Knochenumbaupfaden (RANKL/OPG-Signalisierung, Osteoklasten–Osteoblasten-Gleichgewicht). Der TxGNN-Score von 99.78% scheint eine Graph-Einbettungs-Assoziation widerzuspiegeln, anstatt einer mechanistisch begründeten Hypothese. Darüber hinaus repräsentiert das bekannte Nebenwirkungsprofil des Arzneimittels — Myelosuppression und schwerer Durchfall — ein unverhältnismäßiges Risiko für eine nicht lebensbedrohliche Erkrankung wie Osteoporose, was das Nutzen-Risiko-Verhältnis ungünstig macht, selbst wenn später ein mechanistischer Zusammenhang nachgewiesen würde.

Angesichts des Fehlens von unterstützenden klinischen Studien, Literatur und mechanistischer Rationale sollte diese Vorhersage nur als ein exploratives Signal mit niedrigem Vertrauen behandelt werden.

---

## Klinische Studien-Evidenz

Derzeit sind keine damit verbundenen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine damit verbundene Literatur verfügbar.

---

## Marktinformation Deutschland

Dieses Arzneimittel ist derzeit nicht auf dem Markt in der von diesem Datensatz abgedeckten Rechtsprechung (0 Genehmigungen vorhanden). Keine Produktgenehmigungsunterlagen sind verfügbar.

---

## Zytotoxizität

| Element | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie (ADC) mit konventioneller zytotoxischer Nutzlast — SN-38, ein Topoisomerase-I-Hemmer (aktiver Metabolit von Irinotecan) |
| Myelosuppressions-Risiko | Hoch — die Umwidmungsrationale zitiert explizit Myelosuppression als Teil des bekannten Nebenwirkungsprofils |
| Emetogenitäts-Klassifizierung | Moderat (typisch für Irinotecan/SN-38-Klasse Topoisomerase-I-Hemmer) |
| Überwachungselemente | Blutbild mit Differentialzählung (besonders Neutrophilenzahl), Überprüfung auf Durchfall/Dehydration, Nieren- und Leberfunktion |
| Schutzmaßnahmen beim Umgang | Ja — als zytotoxisches ADC gelten institutionelle Protokolle für Umgang mit gefährlichen/zytotoxischen Arzneimitteln, Rekonstitution und Entsorgung |

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. TFDA-Warnungen und Kontraindikationen für diesen Kandidaten wurden noch nicht erfasst (eine kritische Datenlücke), und eine formale S1-Sicherheitsbewertung kann nicht durchgeführt werden, bis dies gelöst ist.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Alle vier am höchsten eingestuften TxGNN-Vorhersagen für dieses Arzneimittel (arzneimittelinduzierte Osteoporose, schwere nichtproliferative diabetische Retinopathie, diabetische Retinopathie, diabetischer Katarakt) sind L5 (rein auf Modellvorhersage gestützt), und jede ist in ihrer Umwidmungsrationale explizit als mechanistisch implausibel und ohne klinische/literarische Unterstützung gekennzeichnet. Das bekannte zytotoxische Nebenwirkungsprofil des Arzneimittels — Myelosuppression, schwerer Durchfall — schafft ein ungünstiges Nutzen-Risiko-Verhältnis für alle vier Kandidaten-Indikationen, von denen keine lebensbedrohlich ist.

**Zum Fortfahren wird folgendes benötigt:**
- TFDA-Warnungen und Kontraindikationen (kritische Datenlücke) — erforderlich vor jeder S1-Sicherheitsbewertung
- Bestätigter Wirkmechanismus und die ursprünglichen genehmigten Indikationen des Arzneimittels
- Präklinische oder mechanistische Evidenz, die speziell Trop-2/SN-38-Aktivität mit Knochenstoffwechsel oder Retinal-/Linsen-Pathologie verknüpft, falls diese Umwidmungsrichtung weiter verfolgt werden soll
- Angesichts der schlechten biologischen Plausibilität über alle vier eingestuften Vorhersagen hinweg sollte erwogen werden, diesen Kandidaten zu deprioritisieren, bis neue mechanistische Evidenz vorliegt

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

