---
layout: default
title: Evolocumab
parent: Nur Modellvorhersage (L5)
nav_order: 161
evidence_level: L5
indication_count: 6
---

# Evolocumab
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

# Evolocumab: Von unbestätigter Originalindikation zu symptomatischer Hämophilie bei weiblichen Trägern (Vorhersage mit niedriger Konfidenz)

## Zusammenfassung in einem Satz

> Evolocumab ist ein monoklonaler Anti-PCSK9-Antikörper; seine bestätigte Originalindikation ist nicht in diesem Evidenzpaket vorhanden (Datenlücke), obwohl der bekannte Wirkmechanismus des Arzneistoffs – Verbesserung des LDLR-Recyclings zur Senkung von LDL-C – im Begründungstext des Modells selbst erwähnt wird.
> Die vom TxGNN-Modell am höchsten bewertete Vorhersage ist, dass Evolocumab möglicherweise wirksam gegen **symptomatische Hämophilie bei weiblichen Trägern** ist, aber die Begründung des Modells stellt selbst fest, dass es **keine biologische Plausibilität** gibt und deutet sogar auf eine entgegengesetzte pharmakologische Richtung hin (PCSK9-Hemmung neigt dazu, die thrombotische Tendenz zu verringern, nicht die Hämostase zu fördern).
> Es gibt **0 klinische Studien** und **0 Publikationen**, die diese Vorhersage stützen – dies ist ein reines Modellausgabesignal (Evidenzstufe L5), ohne menschliche oder präklinische Bestätigung.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Originalindikation | Nicht im Evidenzpaket verfügbar (Datenlücke); der Begründungstext deutet darauf hin, dass der bekannte Wirkmechanismus mit der LDL-C-Senkung über den PCSK9/LDLR-Weg zusammenhängt |
| Vorhergesagte neue Indikation | Symptomatische Form der Hämophilie bei weiblichen Trägern |
| TxGNN-Vorhersage-Score | 99.82% |
| Evidenzstufe | L5 |
| Taiwan-Marktstatus | Nicht vermarktet (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Daten zum Wirkmechanismus von Evolocumab sind in diesem Evidenzpaket ausdrücklich als Datenlücke gekennzeichnet (DG002, hohe Schwere). Basierend auf dem Begründungstext, der die Vorhersage selbst begleitet, ist Evolocumab ein monoklonaler Anti-PCSK9-Antikörper, der LDL-C senkt, indem er den PCSK9-vermittelten Abbau des LDL-Rezeptors (LDLR) verhindert, wodurch das LDLR-Recycling und die hepatische Clearance von LDL-Cholesterin erhöht werden.

Es gibt keinen bekannten mechanistischen Weg, der PCSK9/LDLR-Biologie mit Hämophilie verbindet, einer Erkrankung, die durch Mangel oder Dysfunktion von Gerinnungsfaktoren verursacht wird (z. B. Faktor VIII/IX bei klassischer Hämophilie). Der Begründungstext des Evidenzpakets selbst geht noch weiter und merkt an, dass erste Literaturhinweise darauf deuten, dass PCSK9-Hemmung tatsächlich die thrombotische Tendenz **verringern** kann – eine Richtung, die dem widerspricht, was therapeutisch in einer Blutungsgerinnungsstörung nützlich wäre. Dies deutet stark darauf hin, dass der TxGNN-Score ein Graph-Topologie-Artefakt widerspiegelt (z. B. gemeinsame Komorbiditätsknoten oder Proxy-Verbindungen im Wissensgraph) statt eines echten pharmakologischen Signals.

Kurz gesagt: Dies ist eine hochbewertete Modellausgabe mit einer expliziten negativen mechanistischen Bewertung. Sie sollte nicht als Beleg für therapeutisches Potenzial ohne unabhängige Bestätigung behandelt werden.

---

## Klinische Studienbelege

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturbelege

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Taiwan-Marktinformationen

Für Evolocumab liegen in diesem Evidenzpaket keine von der TFDA genehmigten Lizenzen vor (`total_licenses: 0`). Der Marktstatus des Arzneistoffs wird als **Nicht vermarktet (Not marketed)** in Taiwan zum Zeitpunkt des Datenschnitts (2026-09-03) verzeichnet.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*Hinweis: TFDA-Kennzeichnungswarnungen und Gegenanzeigen konnten für diese Bewertung nicht abgerufen werden (DG001, blockierende Schwere) – diese Lücke muss behoben werden, bevor eine Sicherheits-Vorprüfung in Phase S1 durchgeführt werden kann.*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die am höchsten bewertete vorhergesagte Indikation (und alle fünf anderen Kandidaten in diesem Paket) hat null unterstützende klinische Studien oder Literatur, und die Begründung des Modells selbst argumentiert ausdrücklich gegen biologische Plausibilität – in mehreren Fällen wird eine pharmakologisch entgegengesetzte Richtung zitiert. Darüber hinaus verhindert eine blockierende Datenlücke (fehlende TFDA-Kennzeichnung/Warnungen) eine Sicherheits-Vorprüfung. Es gibt derzeit keine Grundlage, um das bloße Modellausgabe-Evidenzniveau zu überschreiten.

**Um fortzufahren, ist folgendes erforderlich:**
- DG001 (blockierend) auflösen: TFDA-Etikett-PDF für Warnungen/Gegenanzeigen abrufen und analysieren
- DG002 (hoch) auflösen: bestätigte Wirkmechanismen und Originalindikation(en) aus der DrugBank-API abrufen
- Falls weiter verfolgt wird, eine gezielte Literatur-/präklinische Suche durchführen, die speziell PCSK9-Hemmung in Blutungsgerinnungsstörungsmodellen testet, angesichts der ausdrücklichen Sorge des Begründungstextes über entgegengesetzten Wirkmechanismus
- Da alle 6 bewerteten Kandidaten in diesem Paket L5-Evidenz und Zurückhalten-Status mit schwacher bis negativer mechanistischer Unterstützung teilen, erwägen Sie, diesen Kandidaten (DB09303) gegenüber anderen Repurposing-Kandidaten mit stärkerer biologischer Begründung zu deprioritisieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

