---
layout: default
title: Avapritinib
parent: Nur Modellvorhersage (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: Von nicht dokumentierter ursprünglicher Indikation zur axialen Spondyloemetaphysealen Dysplasie (Signal mit niedriger Konfidenz)

## Kurzzusammenfassung

> Das Evidenzpaket für Avapritinib enthält weder seine ursprüngliche zugelassene Indikation noch seinen Wirkmechanismus (beide sind als Datenlücken gekennzeichnet).
> Die Topvorhersage des TxGNN-Modells ist **Axiale Spondyloemetaphysiale Dysplasie**, aber dies ist eine von 10 Topvorhersagen,
> **keine davon wird durch klinische Studien oder Literatur gestützt** — alle 10 fallen in die Evidenzstufe L5 (nur Modellvorhersage).

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Im aktuellen Evidenzpaket nicht verfügbar (DrugBank `original_indications` und `original_moa` sind beide leer/Datenlücke) |
| Vorhergesagte neue Indikation | Axiale Spondyloemetaphysiale Dysplasie |
| TxGNN-Vorhersage-Score | 99.92% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten für Avapritinib in diesem Evidenzpaket nicht verfügbar (Datenlücke DG002, Schweregrad Hoch). Basierend auf der zu jeder der 10 Vorhersagen beigefügten Rationale wird Avapritinib als **KIT/PDGFRA-Tyrosinkinase-Inhibitor** verstanden. Die Rationale für jede einzelne der 10 besten Vorhersagen besagt jedoch ausdrücklich, dass **keine bekannte mechanistische oder Signalweg-Verbindung** zwischen KIT/PDGFRA-Hemmung und der vorhergesagten Krankheit besteht.

Betrachtet man alle 10 Vorhersagen, zeigt sich ein klares Muster: Sie gliedern sich in zwei Krankheitsgruppen — seltene Skelett-/neurodevelopmentale Syndrome (Ränge 1, 2, 4, 8) und Motoneuronen-Erkrankungen des ALS-Spektrums (Amyotrophe Lateralsklerose) (Ränge 3, 5, 6, 7, 9, 10). Die Rationale für Rang 10 vermerkt dieses Muster direkt und deutet darauf hin, dass das TxGNN-Modell diese Krankheiten nach **phänotypischer/Graph-topologischer Ähnlichkeit zueinander** gruppiert, nicht nach einer echten pharmakologischen Beziehung zu Avapritinib. Ohne Daten zur ursprünglichen Indikation oder zum Wirkmechanismus, um eine Wiederverwendungshypothese zu verankern, und ohne externe Bestätigungsnachweise sollten diese Vorhersagen nur als explorative Signale behandelt werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert

---

## Evidenz aus der Literatur

Derzeit ist keine zugehörige Literatur verfügbar

---

## Marktinformationen für Deutschland

Avapritinib hält derzeit keine Genehmigung für das Inverkehrbringen in Deutschland (0 Lizenzen registriert); keine Angaben zu Darreichungsform oder zugelassener Indikation sind verfügbar.

---

## Zytotoxizität

Avapritinib wird als **KIT/PDGFRA-Tyrosinkinase-Inhibitor** verstanden, ein Wirkstoff aus der Klasse gezielter antineoplastischer Therapien, die in der Onkologie typischerweise eingesetzt werden. Detaillierte Daten zur Zytotoxizitäts-Klassifikation, zum Risiko der Knochenmarks-Suppression, zur Emetogenität und zur Überwachung sind im aktuellen Evidenzpaket nicht verfügbar. Bitte lesen Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage.

---

## Sicherheitsaspekte

Bitte lesen Sie die Warnhinweise und Vorsichtsmaßnahmen in der Packungsbeilage.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Rationale:**
Die 10 am höchsten bewerteten Vorhersagen haben alle Evidenzstufe L5 (nur Modellvorhersage) ohne jegliche Unterstützung durch klinische Studien oder Literatur, und die Wiederverwendungs-Rationale selbst deutet auf einen wahrscheinlichen Mangel an echter mechanistischer Relevanz hin. Darüber hinaus fehlen vollständig Sicherheitsdaten auf Arzneimittel-Ebene (Warnhinweise, Gegenanzeigen, Wirkmechanismus), einschließlich einer blockierenden Datenlücke (DG001), die sogar eine erste Sicherheitsbewertung der Stufe S1 verhindert.

**Um fortzufahren, wird Folgendes benötigt:**
- Packungsbeilage von TFDA/BfArM mit Warnhinweisen und Gegenanzeigen (DG001, Blockierend — erforderlich vor jeder Sicherheits-Vorabprüfung)
- Wirkmechanismus-Daten aus DrugBank (DG002)
- Bestätigung der ursprüngliche(n) zugelassene(n) Indikation(en) von Avapritinib, um eine Wiederverwendungs-Basis zu etablieren
- Unabhängige Literatur- und klinische Studiensuche für die Topvorhersagen mit höchster Rangierung, da das aktuelle Null-Treffer-Ergebnis entweder ein genuines neuartiges Signal oder eine Abdeckungslimitation des Evidenzpakets widerspiegeln kann

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

