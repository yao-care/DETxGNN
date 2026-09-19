---
layout: default
title: Ropeginterferon Alfa-2B
parent: Nur Modellvorhersage (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Ropeginterferon Alfa-2B
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

# Ropeginterferon Alfa-2b: Fehlende Daten zu ursprünglichen Indikationen → vermeintliches Falsches Positiv-Signal Laubry-Pezzi-Syndrom

## Eine Zeile Zusammenfassung

> Das vorliegende Arzneimittel (DrugBank ID: DB15119) verfügt derzeit über keine umfassenden Daten zu Originalindikationen und Wirkmechanismus und ist in Deutschland noch nicht zugelassen. Das TxGNN-Modell listet **Laubry-Pezzi-Syndrom** (Ventrikelseptumdefekt mit Aortenklappenvorfall) als primäre vorhergesagte Indikation auf, jedoch **ohne jegliche Unterstützung durch klinische Studien oder Literatur**, und die im Evidenzpaket enthaltene Wirkmechanismus-Analyse zeigt eindeutig auf, dass es sich um **ein falsches Positiv-Signal ohne biologische Plausibilität handelt**.

---

## Schnellübersicht

| Posten | Inhalt |
|------|------|
| Ursprüngliche Indikationen | Daten fehlen (`original_indications` ist leer, `original_moa` wird nicht bereitgestellt) |
| Vorhergesagte neue Indikationen | Laubry-Pezzi-Syndrom |
| TxGNN-Vorhersage-Score | 99,93% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine tatsächliche Forschung) |
| Marktstatus in Deutschland | ✗ Not marketed |
| Anzahl der Zulassungsnummern | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage begründet?

Derzeit sind keine Wirkmechanismus-Daten (MOA) für dieses Arzneimittel verfügbar, und das Feld `original_indications` ist ebenfalls leer. Daher ist es nicht möglich, den Wirkmechanismus-Zusammenhang zwischen Originalindikationen und neuen Indikationen nach dem Standardverfahren zu vergleichen.

**Noch wichtiger ist, dass die in der Evidenzbeilage bereitgestellte Wirkmechanismus-Analyse diese Vorhersage bereits eindeutig ablehnt**: Das Laubry-Pezzi-Syndrom ist ein angeborener Herzfehler mit Ventrikelseptumdefekt und Aortenklappenvorfall, der eine strukturelle Anomalie darstellt und in keiner Verbindung zu den bekannten Wirkmechanismen von Interferonen (Immunmodulation, antivirale Wirkung, JAK-STAT-Pfad-Regulation) steht. Der hohe Score von TxGNN (99,93%) spiegelt nur die Ähnlichkeit der Knoten-Einbettungen im Wissensgraphen wider, nicht einen tatsächlichen Wirkmechanismus oder klinischen Zusammenhang, und sollte als **falsches Positiv-Signal** eingestuft werden.

Die Kandidaten mit den Rängen 2–5, 7–10 (Ventrikelseptum-Aneurysma, Pierre-Robin-Syndrom, partielle Deletionen des Chromosoms 7q/22q, Jeune-Syndrom mit Situs inversus totalis, Lippen-Kiefer-Gaumenspalte, Pulmonalklappenkrankheit) sind ebenfalls angeborene strukturelle oder Entwicklungskrankheiten und weisen gleichermaßen keine mechanistische Plausibilität und keine empirische Unterstützung auf; ihre Natur ist identisch mit dem Rang 1.

Besonders hervorzuheben ist **Rang 6 „Störung der Fucoglycosan-Synthese"**: Dies ist eine seltene Erkrankung des Glykosylstoffwechsels, aber die zugehörigen 4 Literaturzitate haben Themen, die **alle auf Polycythemia vera (PV) und IFN-α/JAK2V617F-Pfad-Forschung** beruhen, vollständig unangepasst an den beschrifteten Krankheitsnamen. Dies deutet stark darauf hin, dass im Wissensgraphen eine **Fehlanpassung der Krankheitsentität (Label Mismatch)** vorliegt — die wirklich empirisch gestützte Krankheit sollte PV sein (eine derzeit bekannte klinische Indikation dieses Arzneimittels), nicht dieses seltene Stoffwechselkrankheits-Label. Dieser Fund stellt kein wirksames „Drug Repurposing"-Signal dar, sollte aber als Datenkqualitätsproblem des Wissensgraphen gemeldet werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine klinischen Studieneintragungen für Laubry-Pezzi-Syndrom vorhanden.

---

## Literaturevidenz

Derzeit sind keine Literatur-Daten für Laubry-Pezzi-Syndrom vorhanden.

> Anmerkung: Der Kandidat mit Rang 6 (Störung der Fucoglycosan-Synthese) verfügt zwar über 4 Zitate (PMID 33476571, 32034662, 40770048, 32814349), aber nach Überprüfung beruhen alle Zitate auf PV/IFN-α-Behandlungsstudien und passen nicht zum beschrifteten Krankheitsnamen, daher wird eine Wissensgraph-Label-Fehlanpassung bestätigt und diese Zitate werden nicht als Unterstützungsevidenz für diese Indikation gezählt.

---

## Marktinformationen Deutschland

Dieses Arzneimittel ist in Deutschland derzeit **nicht zugelassen** (Not marketed) und es sind keine Zulassungsnummern oder zugelassenen Indikationsdaten verfügbar.

---

## Sicherheitsüberlegungen

Bitte konsultieren Sie die Arzneimittelgebrauchsinformation für Sicherheitsinformationen.

> Ergänzung: Diese Kandidatenakte verzeichnet BfArM-Gebrauchsinformation Warnhinweise/Kontraindikationen (DG001, Blocking) und Wirkmechanismus (DG002, High) als fehlend, wobei das erstere bereits den Eintritt in die Sicherheits-Vorbewertungsphase (S1) direkt blockiert.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
- Alle 10 vorhergesagten Indikationen der Ränge 1–10 haben eine Evidenzstufe von nur L5 (nur Modellvorhersage, keine tatsächliche Forschungsunterstützung), und die Wirkmechanismus-Analyse des Rangs 1 hat eindeutig ein falsches Positiv identifiziert.
- Der einzige Kandidat mit Literaturzitaten (Rang 6) wurde nach Überprüfung als Wissensgraph-Krankheitslabel-Fehlanpassung bestätigt, wobei der tatsächliche Literaturinhalt der bekannten PV-Indikation dieses Arzneimittels entspricht, nicht einem echten neuen Indikations-Signal.
- Fehlende MOA-, TFDA-Gebrauchsinformation-Warnhinweise und Kontraindikationen sowie weitere wichtige Arzneimittel-Ebene-Daten machen eine Wirkmechanismus-Zusammenhang- und Sicherheits-Vorbewertung unmöglich.

**Sollte die Bearbeitung fortgesetzt werden, sind folgende Informationen erforderlich:**
- Wirkmechanismus-Daten (MOA) (DrugBank-API-Abfrage)
- BfArM-Gebrauchsinformation Warnhinweise/Kontraindikationen-Daten (PDF-Parsing)
- Korrekte Liste ursprünglicher Indikationen (derzeit leer; praktisch gesehen wurde dieses Arzneimittel bereits für Polycythemia vera verwendet, muss mit offiziellen Quellen bestätigt und ergänzt werden)
- Validierung der Krankheitsentitäts-Entsprechung des Wissensgraphen, mit Vorrang auf Korrektur der Label-Fehlanpassung bei Rang 6
- Falls eine Neubewertung durchgeführt werden soll, wird empfohlen, diese 10 Kandidaten auszuschließen und auf die nächste Runde des Modells oder manuell überprüfte Ergebnisse mit biologisch plausibler Begründung zu warten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

