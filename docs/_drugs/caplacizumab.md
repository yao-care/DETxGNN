---
layout: default
title: Caplacizumab
parent: Nur Modellvorhersage (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: Evaluierung zur Umwidmung unterbrochen — kritische Datenlücken

## Zusammenfassung in einem Satz

Caplacizumab (DrugBank ID: DB06081) wurde erfolgreich aus DrugBank abgerufen, aber das aktuelle Evidenz-Paket enthält keine Daten zur ursprünglichen Indikation, keinen Wirkungsmechanismus und keine von TxGNN vorhergesagten neuen Indikationen. Die Evaluierung zur Umwidmung kann nicht abgeschlossen werden, bis die ermittelten kritischen Datenlücken behoben sind – eine **Zurückstellung** wird in diesem Stadium empfohlen.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Nicht verfügbar |
| Vorhergesagte neue Indikation | Nicht verfügbar |
| TxGNN Prediction Score | Nicht verfügbar |
| Evidenzgrad | Unzureichende Daten |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellung |

---

## Warum ist diese Vorhersage angemessen?

Die Wirkmechanismus-Indikations-Analyse kann in diesem Stadium nicht abgeschlossen werden.

Die DrugBank-Abfrage für Caplacizumab (DB06081) ergab einen erfolgreichen Treffer, und eine TFDA-Packungsbeilage-Abfrage lieferte ebenfalls ein Ergebnis – jedoch wurde weder der Wirkungsmechanismus noch die ursprüngliche zugelassene Indikation in das strukturierte Evidenz-Paket extrahiert. Ohne eine Basis-Indikation kann die konzeptionelle Verbindung zwischen der bestehenden klinischen Rolle des Arzneistoffs und einer Umwidmungshypothese nicht hergestellt werden.

Im aktuellen Datenbestand sind keine von TxGNN vorhergesagten neuen Indikationen vorhanden (`predicted_indications: []`). Dies bedeutet, dass es kein Kandidaten-Erkrankungsziel zur Bewertung gibt und keine klinischen Studien- oder Literaturbelege bewertet werden können. Bis die TxGNN-Pipeline für DB06081 ausgeführt wird und die Vorhersageergebnisse zurückgegeben werden, bleibt die Kernfrage – „welche neue Indikation könnte dieses Arzneimittel behandeln?" – unbeantwortet.

---

## Marktstatus Deutschland

Caplacizumab ist derzeit in Deutschland nicht zugelassen. Es gibt keine Produktzulassungen in den Unterlagen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Das Evidenz-Paket für Caplacizumab weist Lücken auf in der ursprünglichen Indikation, den von TxGNN vorhergesagten neuen Indikationen und dem Wirkungsmechanismus – den drei Mindesteingaben, die erforderlich sind, um einen aussagekräftigen Evaluierungsbericht zur Umwidmung zu erstellen.

**Um fortfahren zu können, ist Folgendes erforderlich:**

- **Ursprüngliche Indikation extrahieren** aus dem TFDA-Packungsbeilage-Abfrageergebnis (Abfrage-ID 4 hat bereits 1 Ergebnis zurückgegeben; Datenextraktion ist der ausstehende Schritt)
- **Wirkungsmechanismus (MOA) extrahieren** aus dem DrugBank-Abfrageergebnis (Abfrage-ID 3 hat bereits 1 Ergebnis zurückgegeben; strukturierte Analyse ist der ausstehende Schritt)
- **TxGNN-Vorhersage-Pipeline für DB06081 ausführen**, um Kandidaten-Indikationsziele zu generieren
- **Sicherheitsdaten (Warnungen, Kontraindikationen) extrahieren** aus der TFDA-Packungsbeilage (gleiche Quelle wie oben)
- **Abfrage zu Arzneimittel-Wechselwirkungen (DDI) erneut ausführen**, sobald die Arzneistoffklasse bestätigt ist; aktueller `not_found`-Status kann ein unvollständiges Abfrageergebnis widerspiegeln

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

