---
layout: default
title: Cabotegravir
parent: Nur Modellvorhersage (L5)
nav_order: 79
evidence_level: L5
indication_count: 5
---

# Cabotegravir
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

# Cabotegravir: Evaluierung der Umnutzung von Arzneimitteln — Unzureichende Daten für vollständige Bewertung

## Zusammenfassung in einem Satz

Cabotegravir ist ein HIV-1-Integrase-Strang-Transfer-Inhibitor (INSTI), der international für die HIV-1-Behandlung (in Kombination mit Rilpivirin) und die HIV-Prä-Expositions-Prophylaxe (PrEP) zugelassen ist.
Das aktuelle Evidence Pack enthält **keine von TxGNN vorhergesagten neuen Indikationen**, und kritische Datenfelder – einschließlich Wirkmechanismus, Sicherheitswarnungen und Kontraindikationen – sind nicht verfügbar.
Eine vollständige Bewertung der Umnutzung **kann nicht abgeschlossen werden**, bis diese Lücken behoben sind.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|---------|
| Ursprüngliche Indikation | HIV-1-Infektion (Behandlung und PrEP) — basierend auf internationalen Zulassungen; nicht im Evidence Pack berücksichtigt |
| Vorhergesagte neue Indikation | Keine Vorhersage verfügbar in diesem Evidence Pack |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzgrad | L5 — nur Modellvorhersage; keine Umnutzungsevidenz bereitgestellt |
| Taiwan-Markt-Status | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Aussetzen** |

---

## Warum eine vollständige Bewertung nicht abgeschlossen werden kann

Das Evidence Pack für Cabotegravir (DB11751) weist zwei Kategorien von kritischen Datenlücken auf:

**1. Keine von TxGNN vorhergesagten Indikationen**
Das `predicted_indications`-Array ist leer. Ohne eine Kandidaten-Zielerkrankung aus dem Modell gibt es keine Umnutzungshypothese zu bewerten. Es ist unklar, ob dies einen Modelloutput ohne hochzuverlässige Vorhersagen widerspiegelt oder eine Datenpipeline-Lücke, bei der Vorhersagen nicht abgerufen wurden.

**2. Fehlender Wirkmechanismus (MOA)**
Das Feld `original_moa` ist als Datenlücke gekennzeichnet. Aus öffentlich verfügbaren Quellen ist bekannt, dass Cabotegravir als INSTI wirkt – es blockiert das HIV-Integrase-Enzym daran, virale DNA in das Wirtsgenom einzufügen. Da dies jedoch nicht durch die designierte Datenquelle (DrugBank API) bestätigt wurde, kann es in dieser Bewertung nicht formal zitiert werden, entsprechend den Protokollregeln.

**3. Keine Sicherheitsdaten**
Schlüsselwarnungen und Kontraindikationen sind beide als Datenlücken aufgeführt. Arzneistoff-Wechselwirkungs-Abfragen ergaben keine Ergebnisse. Ohne Sicherheitsinformationen kann nicht einmal ein vorläufiges Sicherheits-Screening (S1-Bewertung) fortgesetzt werden.

---

## Taiwan-Marktinformationen

Cabotegravir verfügt derzeit über **keine behördlichen Zulassungen** in Taiwan. Es gibt keine lizenzierten Produkte, keine zugelassenen Darreichungsformen und keine genehmigten Indikationen in der Dokumentation.

> **Anmerkung:** International wird Cabotegravir als **Cabenuva** (mit Rilpivirin, Langzeit-Injektion für HIV-1-Behandlung) und **Apretude** (Langzeit-Injektion für PrEP) vermarktet. Diese werden in den taiwanischen Behördendaten nicht berücksichtigt.

---

## Sicherheitsaspekte

Bitte lesen Sie die Packungsbeilage für Sicherheitsinformationen. Alle Sicherheitsfelder im aktuellen Evidence Pack – einschließlich Schlüsselwarnungen, Kontraindikationen und Arzneistoff-Wechselwirkungen – sind nicht verfügbar.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
Das Evidence Pack enthält nicht die erforderlichen Mindestdaten, um eine Empfehlung zur Umnutzung zu stützen – es gibt keine TxGNN-Vorhersagen, keine MOA-Daten und keine Sicherheitsinformationen. Eine Bewertung ohne diese Eingaben durchzuführen würde zu unzuverlässigen Schlussfolgerungen führen.

**Um fortzufahren, ist Folgendes erforderlich:**

1. **TxGNN-Vorhersage-Pipeline erneut ausführen** — bestätigen, ob das leere `predicted_indications` ein echter Modelloutput (keine zuverlässigen Treffer) oder ein Abrufffehler ist; Ergebnisse abrufen und laden
2. **MOA von DrugBank API abrufen** (DB11751) — Integrase-Inhibitor-Mechanismus und Zielwege bestätigen
3. **TFDA-Packungsbeilage-PDF herunterladen und analysieren** — Schlüsselwarnungen und Kontraindikationen extrahieren, um S1-Sicherheits-Screening zu ermöglichen
4. **DDI-Datenbank erneut abfragen** — aktuelles Ergebnis ist `not_found`; überprüfen, ob dies auf Arzneistoff-Namensformatierung zurückzuführen ist (versuchen Sie "cabotegravir", "CAB", "GSK1265744") oder eine echte Abwesenheit von Wechselwirkungsdaten
5. **Umfang klären** — wenn TxGNN nach der Neuausführung keine Vorhersagen zurückgibt, bestimmen Sie, ob dieser Kandidat aus der Umnutzungs-Pipeline zurückgezogen oder für die manuelle Literaturübersicht gekennzeichnet werden sollte

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

