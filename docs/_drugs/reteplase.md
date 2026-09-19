---
layout: default
title: Reteplase
parent: Nur Modellvorhersage (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: Bewertung der Arzneimittelumwidmung — Unzureichende Evidenz für die Evaluierung

## Zusammenfassung in einem Satz

Reteplase (DB00015) ist ein rekombinanter Gewebetyp-Plasminogenaktivator (tPA), der in der Thrombolysetherapie eingesetzt wird. Das aktuelle Evidence Pack enthält **keine von TxGNN prognostizierten Indikationen**, kombiniert mit kritischen Datenlücken bei Sicherheitsinformationen und Wirkmechanismus, was bedeutet, dass eine aussagekräftige Arzneimittelumwidmungsbewertung **in dieser Phase nicht abgeschlossen werden kann**. Eine Zurückstellung ist gerechtfertigt, bis kritische Datenlücken behoben sind.

---

## Kurzübersicht

| Element | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Nicht dokumentiert im aktuellen Evidence Pack |
| Prognostizierte neue Indikation | Keine — TxGNN hat keine Vorhersagen zurückgegeben |
| TxGNN-Prognosewert | N/A |
| Evidenzstufe | L5 (keine Vorhersagen, keine unterstützenden Studien identifiziert) |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellung** |

---

## Warum keine Vorhersage verfügbar ist

Das TxGNN-Modell hat für Reteplase in diesem Evidence Pack null prognostizierte Indikationen zurückgegeben. Dies tritt typischerweise aus einem der folgenden Gründe auf:

1. **Lücke in der Knowledge-Graph-Abdeckung**: Reteplase ist möglicherweise nicht ausreichend als Knoten im TxGNN-Wissensgraph repräsentiert, was die Fähigkeit des Modells einschränkt, Krankheitsassoziationen zu verbreiten.
2. **Begrenztes Wirkprofil**: Da Reteplase als Thrombolytikum spezifisch auf Fibringerinnsel über Plasminogenaktivierung wirkt, kann sein pharmakologischer Fußabdruck bei der aktuellen Vorhersageschwelle möglicherweise nicht mit Knoten von nicht-kardiovaskulären Krankheiten im Diagramm überlappen.
3. **Unvollständigkeit der Dateneingabe**: Das Evidence Pack listet `original_indications` als leer und `original_moa` als nicht verfügbar auf. Ohne diese Ankerpunkte kann das Modell die Assoziationsdurchquerung nicht initiieren.

Derzeit sind detaillierte Wirkmechanismus-Daten nicht im Evidence Pack verfügbar. Basierend auf der bekannten pharmakologischen Klasse ist Reteplase eine rekombinante Deletionsmutante des menschlichen Gewebetyp-Plasminogenaktivators; seine thrombolytische Wirksamkeit beim akuten Myokardinfarkt ist klinisch etabliert, und jede mechanistische Anwendbarkeit auf neue Indikationen würde von der vorherigen Behebung der MOA-Datenlücke abhängen.

---

## Marktstatus in Deutschland

Reteplase hat zum Zeitpunkt dieses Berichts **keine Zulassungen für den Markt** in Deutschland. Es gibt keine lizenzierten Produkte, Darreichungsformen oder genehmigten Indikationen in den aktuellen Aufzeichnungen des Evidence Pack.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Im aktuellen Evidence Pack wurden keine Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungsdaten zurückgegeben.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Das Evidence Pack für Reteplase ist kritisch unvollständig — TxGNN hat keine prognostizierten Indikationen hervorgebracht, Wirkmechanismus-Daten fehlen, alle Sicherheitsfelder sind leer, und das Arzneimittel hat keine Zulassung für den deutschen Markt. Es gibt derzeit kein bewertbares Arzneimittelumwidmungssignal.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[Blocking]** Vollständige Packungsbeilage abrufen (TFDA / BfArM / SmPC), um Warnungen, Kontraindikationen und genehmigte Indikationen auszufüllen — dies ist eine Voraussetzung für jede Sicherheitsbewertung
- **[High]** MOA-Daten von der DrugBank-API abrufen (Abfrage hat 1 Ergebnis zurückgegeben, aber MOA wurde nicht extrahiert) — erforderlich für die Analyse der mechanistischen Plausibilität
- **[High]** TxGNN-Prognosepipeline erneut ausführen, nachdem bestätigt wurde, dass Reteplase korrekt als Knowledge-Graph-Knoten repräsentiert ist; Knoten-ID-Zuordnung zwischen DrugBank DB00015 und der KG-Entität überprüfen
- **[Medium]** Bestätigen Sie, ob Reteplase behördliche Zulassungen außerhalb Deutschlands hat (z. B. EMA, FDA), die das Feld der ursprünglichen Indikation verankern und eine länderübergreifende Arzneimittelumwidmungsanalyse unterstützen könnten
- **[Medium]** Überprüfen Sie die TxGNN-Prognoseschwellenwerteinstellungen — wenn der Score-Cutoff hoch gesetzt ist, kann dessen Senkung unterschwellige Kandidaten-Indikationen für explorative Überprüfung zu Tage fördern

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

