---
layout: default
title: Andexanet Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 34
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Andexanet Alfa: vorhergesagte neue Indikation Glanzmann-Thrombasthenie (Evidenzstufe L5). Ursprüngliche Indikation: Arzneimittelbedingte Nebenwirkungen (Drug-Related Side Effects and Ad…"
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Andexanet alfa: Von arzneimittelbedingten Nebenwirkungen zu Glanzmann-Thrombasthenie
{: .text-alpha }

## Zusammenfassung

Andexanet alfa ist ein rekombinantes Protein, das ursprünglich zur Aufhebung der Wirkung von Faktor-Xa-Inhibitoren bei arzneimittelbedingten Nebenwirkungen (Blutungen unter Antikoagulation) zugelassen wurde.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Glanzmann-Thrombasthenie** voraus, jedoch gibt es dafür **0 klinische Studien** und **0 Publikationen**. Die Vorhersage beruht allein auf dem Modell (Evidenzstufe L5).

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Arzneimittelbedingte Nebenwirkungen (Drug-Related Side Effects and Adverse Reactions) |
| Vorhergesagte neue Indikation | Glanzmann-Thrombasthenie |
| TxGNN-Vorhersagewert | 99,77 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung (Cancelled only) |
| Anzahl der Zulassungen | 1 (davon 0 gültig) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Andexanet alfa ist ein rekombinanter, katalytisch inaktiver Faktor-Xa-Köder („Decoy"), der direkte und indirekte FXa-Inhibitoren bindet und neutralisiert.

Die Glanzmann-Thrombasthenie ist eine Thrombozytenerkrankung, die durch einen Defekt des Integrins αIIbβ3 (GPIIb/IIIa) entsteht und die Thrombozytenaggregation beeinträchtigt. Andexanet alfa wirkt auf die Aktivität von FXa-Inhibitoren, nicht auf die Thrombozytenaggregation. Ein mechanistischer Zusammenhang ist daher nicht bekannt.

Der sehr hohe TxGNN-Wert (0,998) ist eine netzwerkbasierte Vorhersage ohne unterstützende Studien- oder Literaturevidenz. Er spiegelt wahrscheinlich gemeinsame Nachbarn im Wissensgraphen aus dem Bereich Gerinnung/Hämostase wider.

Weitere vorhergesagte Indikationen zeigen dasselbe Bild:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Evidenzstufe | Einschätzung |
|---|---|---|---|---|
| 2 | Primäre Thrombozyten-Freisetzungsstörung | 99,76 % | L5 | Kein plausibler Mechanismus; keine Studien oder Literatur |
| 3 | Pseudo-von-Willebrand-Krankheit | 99,65 % | L5 | Kein bekannter Effekt auf die GPIbα-VWF-Achse |
| 4 | Hämophilie | 99,10 % | L4 | Nur indirekte Literaturbezüge; Thromboserisiko wäre ein Sicherheitsproblem |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für die Hauptvorhersage (Glanzmann-Thrombasthenie) liegt keine Literatur vor. Für die viertplatzierte Vorhersage Hämophilie wurden Publikationen gefunden, die jedoch nur indirekt (Mitnennung in Gerinnungsthemen) und nicht als Beleg für einen therapeutischen Nutzen zu verstehen sind:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Kohorte | Circulation | ANNEXA-4-Subanalyse: Wirksamkeit und Sicherheit von Andexanet alfa bei akuten Magen-Darm-Blutungen unter FXa-Inhibitoren |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Leitlinie/Review | Thromb Haemost | Aktualisierte ICSH-Empfehlungen zur Labormessung direkter oraler Antikoagulanzien, inkl. Umkehrmittel |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laborstudie | Haemophilia | DOAC-Interferenz bei Faktor-VIII/IX-Tests; Neutralisierung von Rivaroxaban mit Andexanet alfa im Labor |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Review | Curr Pharm Des | Neue Hämostatika und Antidote: perioperative anästhesiologische Aspekte |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Review | Blood | Aufhebung von Anti-FXa-Wirkstoffen und ungedeckter Bedarf bei Traumapatienten |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Review | Drug Saf | Umkehrstrategien für NOAK: Entwicklungsstand und Perspektiven |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Review | Dtsch Med Wochenschr | Gerinnungsstörungen auf der Intensivstation; Antidote für NOAK |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Review (Protokollerhebung) | EJHaem | Übersicht lokaler Protokolle zur Anwendung von Andexanet alfa in britischen Kliniken |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Positionspapier | Br J Haematol | Positionspapier der British Society for Haematology zur Anwendung von Andexanet alfa |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004108 | Ondexxya (AstraZeneca AB) | – | Arzneimittelbedingte Nebenwirkungen (Drug-Related Side Effects and Adverse Reactions) |

Status dieser Zulassung: erloschen/aufgehoben (cancelled).

---

## Sicherheitshinweise

Bitte die Packungsbeilage für Sicherheitsinformationen beachten. Für die zusammengestellten Daten liegen keine Warnhinweise, Gegenanzeigen oder Wechselwirkungen vor.

Aus der Literatur- und Mechanismusbewertung ergibt sich ein relevanter Hinweis: Wegen der prokoagulatorischen Effekte von Andexanet alfa wäre ein Thromboserisiko bei Patienten mit veränderter Hämostase (z. B. Hämophilie) ein ernstzunehmendes Sicherheitsproblem.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die hohen TxGNN-Werte sind rein rechnerisch; für Glanzmann-Thrombasthenie gibt es weder Studien noch Literatur und keinen plausiblen Wirkmechanismus. Zudem besteht in Deutschland aktuell keine gültige Zulassung des Produkts.

**Für ein Weiterkommen erforderlich:**
- Beschaffung und Auswertung der Packungsbeilage (Warnhinweise, Gegenanzeigen) – derzeit blockierende Datenlücke für die Sicherheitsprüfung
- Daten zum Wirkmechanismus (z. B. aus DrugBank) zur Prüfung eines möglichen mechanistischen Zusammenhangs
- Klärung des Zulassungsstatus in Deutschland bzw. der EU
- Präklinische Evidenz, die einen Effekt auf Thrombozytenfunktion oder Hämostase bei den vorhergesagten Erkrankungen belegt, bevor klinische Studien erwogen werden
- Bewertung des Thromboserisikos in Populationen mit Blutgerinnungsstörungen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

