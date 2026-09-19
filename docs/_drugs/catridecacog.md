---
layout: default
title: Catridecacog
parent: Nur Modellvorhersage (L5)
nav_order: 92
evidence_level: L5
indication_count: 3
---

# Catridecacog
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Catridecacog: Von angeborenem Faktor-XIII-A-Untereinheit-Mangel zu primärer Plättchenfreisetzungsstörung

## Zusammenfassung in einem Satz

> Catridecacog (DB09310) ist eine rekombinante Faktor-XIII-A-Untereinheit, die für die prophylaktische Behandlung des angeborenen Faktor-XIII-A-Untereinheit-Mangels verwendet wird.
> Das TxGNN-Modell sagt vorher, dass es möglicherweise wirksam für **Primäre Plättchenfreisetzungsstörung** ist,
> aber derzeit unterstützen **keine klinischen Studien** und **keine veröffentlichte Literatur** diese Richtung — dies ist eine reine Modellvorhersage (L5).

---

## Schnelüberblick

| Artikel | Inhalt |
|------|------|
| Ursprüngliche Indikation | Angeborener Faktor-XIII-A-Untereinheit-Mangel *(nicht im Evidenzpaket erfasst — Feld original_indications leer; basierend auf bekanntem Arzneimittelprofil von catridecacog)* |
| Vorhergesagte neue Indikation | Primäre Plättchenfreisetzungsstörung |
| TxGNN-Vorhersage-Score | 99.29% (Rang 7629) |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage begründet?

Derzeit sind detaillierte Daten zum Wirkungsmechanismus in diesem Evidenzpaket nicht verfügbar (MOA-Feld gekennzeichnet als Datenlücke, Schweregrad Hoch). Basierend auf der Umpositionierungs-Rationale, die der Vorhersage selbst beigefügt ist, ist catridecacog eine rekombinante Faktor-XIII-A-Untereinheit, die weit nachgelagert in der Gerinnungskaskade wirkt — sie stabilisiert die Fibrin-Quervernetzung, nachdem sich bereits ein Blutgerinnsel gebildet hat. Sie wirkt nicht auf die Plättchengranulafreisetzung, die Plättchenrezeptorfunktion oder die Plättchenaggregationswege.

Primäre Freisetzungsstörung von Plättchen (z. B. Speicherpoolerkrankung) wird durch einen Mangel an δ/α-Granula-Inhaltsfreisetzung aus Plättchen verursacht — ein Mechanismus, der vollständig vorgelagert gegenüber und unabhängig von der Fibrin-Stabilisierung ist. Die mechanistische Bewertung des Evidenzpakets selbst erklärt ausdrücklich, dass es **keine direkte mechanistische Verbindung** gibt, und dass diese Assoziation „rein datengesteuert" ist, ohne Unterstützung durch biologische Plausibilität.

Der Vollständigkeit halber wurden zwei weitere Kandidaten mit ähnlich hohen TxGNN-Scores vorhergesagt, aber mit gleichermaßen schwacher mechanistischer Grundlage: **Pseudo-von-Willebrand-Krankheit** (Rang 2, Score 99.29%, Mismatch — Pathologie ist eine GPIbα-Rezeptor-Gain-of-Function-Mutation) und **Glanzmann-Thrombasthenie** (Rang 3, Score 99.15%, Mismatch — Pathologie ist GPIIb/IIIa-Integrin-Mangel). Alle drei Vorhersagen teilen die gleiche Einschränkung: Sie sind Plättchenfunktionsstörungen, während catridecacogs Mechanismus streng am Fibrin-Quervernetzungsschritt wirkt, nachgelagert der Plättchenbeteiligung.

---

## Klinische Studien-Evidenz

Derzeit keine zugehörigen klinischen Studien registriert

---

## Literatur-Evidenz

Derzeit keine zugehörige Literatur verfügbar

---

## Marktinformation Deutschland

Catridecacog hat derzeit keine Marktgenehmigung in Deutschland (0 Zulassungen, Marktstatus: Nicht vermarktet/Nicht vermarktet). Keine Lizenzdatensätze sind für dieses Evidenzpaket verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Derzeit keine Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungsdaten verfügbar — TFDA/BfArM-Kennzeichnungsdaten gekennzeichnet als blockierende Datenlücke, DG001.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die Vorhersage wird durch keine klinischen Studien, keine Literatur und die mechanistische Rationale, die explizit gegen biologische Plausibilität argumentiert, unterstützt — catridecacogs nachgelagerte Fibrin-stabilisierende Wirkung behebt nicht die vorgelagerten Plättchen-Granula-Freisetzungs-, Rezeptor- oder Aggregationsmängel, die bei den drei vorhergesagten Indikationen beobachtet werden. Dies ist ein L5, nur Modell-Score-basiertes Signal.

**Zur Fortsetzung ist Folgendes erforderlich:**
- TFDA/BfArM-Packungsbeilage-Daten (Warnungen, Kontraindikationen) — derzeit eine blockierende Datenlücke (DG001)
- Bestätigter Wirkungsmechanismus (DrugBank-API-Abfrage) — derzeit eine Datenlücke mit hohem Schweregrad (DG002)
- Präklinische oder Fall-Level-Evidenz, die direkt Faktor-XIII-Supplementation mit Plättchen-Freisetzungsstörungen, Pseudo-von-Willebrand-Krankheit oder Glanzmann-Thrombasthenie verknüpft, bevor über S0 hinaus voranschreitet
- Angesichts des oben identifizierten mechanistischen Mismatch sollte geprüft werden, ob diese Kandidaten überhaupt weitere Verfolgung rechtfertigen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

