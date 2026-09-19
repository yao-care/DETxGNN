---
layout: default
title: Pyrantel
parent: Nur Modellvorhersage (L5)
nav_order: 321
evidence_level: L5
indication_count: 0
---

# Pyrantel
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **0** 
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

# Pyrantel: Keine TxGNN-Vorhersagen verfügbar

## Ein-Satz-Zusammenfassung

Pyrantel ist ein Anthelmintikum zur Behandlung von intestinalen parasitären Infektionen (Rundwürmer, Hakenwürmer und Fadenwürmer). Das TxGNN-Modell generierte während des aktuellen Pipeline-Durchlaufs keine vorhergesagten neuen Indikationen für dieses Arzneimittel. Eine aussagekräftige Bewertung der Arzneimittelumpositionierung kann nicht abgeschlossen werden, bis Vorhersagedaten und wichtige Datenlücken behoben sind.

---

## Schnellübersicht

| Element | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Im Datensatz nicht verfügbar |
| Vorhergesagte neue Indikation | Keine (keine TxGNN-Vorhersagen generiert) |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | N/A |
| Taiwan-Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage sinnvoll?

Zum jetzigen Zeitpunkt sind keine TxGNN-Vorhersagen für Pyrantel verfügbar. Ohne eine Kandidatenindikation kann die Analyse der mechanistischen Relevanz nicht durchgeführt werden und das grundlegende Rahmenwerk der Arzneimittelumpositionierung ist nicht anwendbar.

Derzeit sind detaillierte Wirkungsmechanismus-Daten nicht in diesem Evidenzpaket verfügbar. Pyrantel (DrugBank: DB11156) ist ein etabliertes Anthelmintikum der Tetrahydropyrimidin-Klasse, das als depolarisierender Neuromuskelblocker wirkt und spastische Lähmung bei empfänglichen Nematoden verursacht. Dieser MOA ist hochgradig parasitspezifisch, was erklären könnte, warum TxGNN – trainiert auf einem menschlichen Krankheitswissensgraph – keine starken Umpositionierungskandidaten hervorbrachte. Der vollständige MOA-Datensatz von DrugBank muss abgerufen werden, bevor diese Schlussfolgerung definitiv gezogen werden kann.

---

## Klinische Studienevidenz

Derzeit sind keine relevanten klinischen Studien für eine neue Umpositionierungsindikation registriert.

---

## Literaturbeweise

Derzeit ist keine relevante Literatur für eine neue Umpositionierungsindikation verfügbar.

---

## Taiwan-Marktinformationen

Pyrantel wird derzeit **nicht vermarktet** in Taiwan. Es gibt keine TFDA-Produktzulassungen in der Akte.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die TxGNN-Pipeline führte zu null vorhergesagten Indikationen für Pyrantel, und zwei blockierende Datenlücken (Packungsbeilage-Sicherheitsdaten und MOA) bleiben ungelöst, was eine Bewertung der Arzneimittelumpositionierung in dieser Phase verfrüht macht.

**Um fortzufahren, wird Folgendes benötigt:**

- **Führen Sie die TxGNN-Vorhersage-Pipeline aus** — bestätigen Sie, ob null Vorhersagen ein echtes Fehlen des Signals oder ein Pipeline-/Mapping-Problem widerspiegeln (z. B. DrugBank-ID nicht mit KG-Knoten verlinkt)
- **Rufen Sie MOA von DrugBank (DB11156) ab** — überprüfen Sie, ob der parasitspezifische Mechanismus Umpositionierungskandidaten für menschliche Erkrankungen wirklich begrenzt
- **Beschaffen Sie die TFDA-Packungsbeilage** — extrahieren Sie Warnungen, Kontraindikationen und genehmigte Indikationen, um die Sicherheitsgrundlinie zu vervollständigen (derzeit blockierender Schweregrad pro DG001)
- **Bewerten Sie die Taiwan-Marktrealisierbarkeit** — Pyrantel ist in Taiwan nicht registriert; eine Analyse des Markteintrittsweges ist erforderlich, bevor ein Umpositionierungsprogramm eingeleitet wird
- **Überprüfen Sie die KG-Abdeckung** — überprüfen Sie, ob Pyrantel im TxGNN-Wissensgraph erscheint; falls nicht vorhanden, muss das Arzneimittel hinzugefügt werden, bevor Vorhersagen generiert werden können

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

