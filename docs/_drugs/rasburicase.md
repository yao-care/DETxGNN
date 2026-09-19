---
layout: default
title: Rasburicase
parent: Nur Modellvorhersage (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# RASBURICASE: Von Hyperurikämie bis — Keine TxGNN-Vorhersage verfügbar

## Zusammenfassung in einem Satz

Rasburicase ist ein rekombinantes Uratoxidase-Enzym, das zur Vorbeugung und Behandlung von Hyperurikämie bei Patienten mit Tumorlysesyndrom eingesetzt wird, die sich einer Chemotherapie für hämatologische und Festkörper-Tumorerkrankungen unterziehen. Das TxGNN-Modell gab **keine vorhergesagten neuen Indikationen** für dieses Arzneimittel in der aktuellen Evidenzsammlung zurück, was eine standardmäßige Umnutzungsbewertung verhindert. Mit **null klinischen Studien** und **null Publikationen**, die mit einem Umnutzungsziel verknüpft sind, und dem nicht vermarkteten Arzneimittel in Taiwan erfordert dieser Kandidat erhebliche Datenremediation, bevor die Bewertung fortgesetzt werden kann.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Originalindikation | Hyperurikämie bei Krebspatienten, die sich einer Chemotherapie unterziehen (Prävention des Tumorlysessyndroms) |
| Vorhergesagte neue Indikation | Keine — TxGNN gab keine Vorhersagen zurück |
| TxGNN-Vorhersagepunktzahl | N/A |
| Evidenzgrad | L5 (nur Modellvorhersage — keine Vorhersage generiert) |
| Status auf taiwanischem Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

---

## Warum ist diese Vorhersage angemessen?

Für die Bewertung ist derzeit keine Umnutzungsvorhersage verfügbar.

Derzeit sind detaillierte Wirkmechanismus-Daten in der Evidenzsammlung nicht verfügbar. Basierend auf bekannten pharmakologischen Informationen ist Rasburicase eine rekombinante Form von Uratoxidase — einem Enzym, das natürlicherweise nicht beim Menschen vorkommt — das die Oxidation von Harnsäure zu Allantoin katalysiert, einem viel wasserlöslicheren und renalgängigeren Metaboliten. Dieser Mechanismus ist rein metabolisch, nicht zytotoxisch, was ihn deutlich von antineoplastischen Wirkstoffen unterscheidet.

Da das Array der vorhergesagten Indikationen leer ist, ist es nicht möglich, die mechanistische Anwendbarkeit auf ein neues Krankheitsziel zu begründen. Das Fehlen einer TxGNN-Ausgabe kann auf fehlende Arzneimittel-Graph-Verknüpfungen, unzureichende Wissensgraph-Abdeckung für dieses Molekül oder Upstream-Daten-Pipeline-Probleme zurückzuführen sein, die verhinderten, dass das Modell Kandidaten generierte. Das Beheben der Grundursache der fehlenden Vorhersage ist der erste erforderliche Remediationsschritt.

---

## Evidenz klinischer Studien

Derzeit sind keine verwandten klinischen Studien für ein Umnutzungsziel registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine verwandte Literatur für ein Umnutzungsziel verfügbar.

---

## Taiwan-Marktinformationen

Rasburicase hat derzeit **keine Marktzulassungen** in Taiwan. Das Arzneimittel ist in anderen wichtigen Märkten unter den Markennamen **Fasturtec** (EU/EMA) und **Elitek** (US/FDA) zugelassen, in erster Linie zur Prophylaxe und Behandlung von Hyperurikämie bei Erwachsenen und pädiatrischen Onkologie-Patienten.

---

## Sicherheitsüberlegungen

Alle Sicherheitsfelder in der aktuellen Evidenzsammlung (Hauptwarnungen, Gegenanzeigen, Arzneimittelwechselwirkungen) enthalten keine verwertbaren Daten. Basierend auf etablierter pharmakologischer Literatur sind die folgenden Sicherheitssignale bekannt, klinisch signifikant zu sein und **müssen** eingearbeitet werden, sobald formale Sicherheitsdaten verfügbar sind:

- **Hämolyse / Methämoglobinämie**: Rasburicase ist bei Patienten mit Glucose-6-Phosphat-Dehydrogenase-Defizienz (G6PD-Defizienz) absolut kontraindiziert, da das während der Oxidation von Harnsäure entstehende Wasserstoffperoxid schwere hämolytische Anämie und Methämoglobinämie auslösen kann.
- **Anaphylaxie**: Als Fremdprotein birgt Rasburicase ein Risiko für Überempfindlichkeitsreaktionen, einschließlich Anaphylaxie; Vortestung und Bereitschaft zur Notfallbehandlung sind erforderlich.
- **Handhabung von Harnsäure-Proben**: Blutproben von Patienten, die Rasburicase erhalten, müssen sofort auf Eis gelegt werden, um eine ex-vivo-Degradation der Harnsäure zu verhindern, die zu falsch niedrigen gemessenen Werten führen würde.

> Bitte beachten Sie die Packungsbeilage (EU-Fachinformation / US-Verschreibungsinformationen) für vollständige Warnungen und Vorsichtsmaßnahmen bis zum Verfügbarwerden der TFDA-Packungsbeilage.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die Evidenzsammlung für Rasburicase (DB00049) ist kritisch unvollständig — sie enthält keine Zuordnung der ursprünglichen Indikation, keine Wirkmechanismus-Daten, keine Sicherheitsdaten und am wichtigsten keine TxGNN-vorhergesagte neue Indikation — was es unmöglich macht, eine aussagekräftige Umnutzungsbewertung in diesem Stadium durchzuführen.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[Blockierend — DG001]** TFDA-Packungsbeilage-PDF abrufen und genehmigte Indikationen, Hauptwarnungen und Gegenanzeigen extrahieren, um die Sicherheits-Screening-Phase (S1) freizuschalten
- **[Hoch — DG002]** DrugBank-API für vollständigen Wirkmechanismus, Pharmakodynamik und Arzneimittelkategorien abfragen, um mechanismusbasierte Begründung zu ermöglichen
- **[Kritisch]** Untersuchen Sie, warum `predicted_indications` leer ist — bestätigen Sie, ob der TxGNN-Wissensgraph den Rasburicase-Knoten (DB00049) enthält, und führen Sie die Vorhersage-Pipeline erneut aus; überprüfen Sie fehlende Arzneimittel-Krankheits-Verbindungen in der KG
- **[Hoch]** G6PD-Defizienz-Wechselwirkungsprüfung als obligatorische Sicherheitsvorbedingung für jede potenzielle neue Indikation in Populationen mit erhöhter G6PD-Defizienz-Prävalenz durchführen
- **[Mittel]** Bestätigen Sie EU/US-Zulassungsstatus und Indikationstext von Fasturtec/Elitek-Fachinformation als Referenzverankerung für das derzeit leere Original-Indikations-Feld

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

