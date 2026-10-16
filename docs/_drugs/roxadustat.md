---
layout: default
title: Roxadustat
parent: Nur Modellvorhersage (L5)
nav_order: 414
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Roxadustat: vorhergesagte neue Indikation Trockenes-Auge-Syndrom (dry eye syndrome) (Evidenzstufe L5). Ursprüngliche Indikation: Anämie"
---

# Roxadustat
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Roxadustat: Von renaler Anämie zu Trockenem-Auge-Syndrom

## Zusammenfassung

Roxadustat ist ein HIF-Prolylhydroxylase-Inhibitor, der ursprünglich zur Behandlung der Anämie bei chronischer Niereninsuffizienz zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er für das **Trockene-Auge-Syndrom** (dry eye syndrome) wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht ausschließlich auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Anämie; chronische Niereninsuffizienz |
| Vorhergesagte neue Indikation | Trockenes-Auge-Syndrom (dry eye syndrome) |
| TxGNN-Vorhersagewert | 99,51 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung (Cancelled only) |
| Anzahl der Zulassungen | 1 (davon 0 gültig) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus liegen derzeit nicht vor. Bekannt ist, dass Roxadustat ein HIF-Prolylhydroxylase-Inhibitor ist: Es stabilisiert HIF-1α/2α und fördert dadurch unter anderem die Erythropoetin-Bildung, was seine Wirksamkeit bei Anämie bei chronischer Niereninsuffizienz erklärt. Die EMA hat Roxadustat im August 2021 für diese Indikation zugelassen.

Zwischen renaler Anämie und Trockenem Auge besteht keine unmittelbare klinische Verwandtschaft. Ein möglicher Zusammenhang ergibt sich nur über die HIF-Signalwege, die Entzündung der Augenoberfläche, die Epithelreparatur und die Angiogenese beeinflussen könnten. Die HIF-Aktivierung kann jedoch auch pathologische Neovaskularisation fördern. Die Verbindung ist daher spekulativ: Der TxGNN-Wert ist eine rein graphbasierte Vorhersage.

Weitere vom Modell genannte Kandidaten (alle ebenfalls nur Evidenzniveau L5, Empfehlung Hold):

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Paget-Krankheit des Knochens | 99,12 % | Theoretischer Bezug über HIF und Knochenumbau; Wirkrichtung unklar |
| 3 | Dentinogenesis imperfecta | 99,06 % | Mechanismus unklar; erbliche Strukturstörung kaum medikamentös korrigierbar |
| 4 | Plattenepithelkarzinom | 99,02 % | HIF-Aktivierung ist eher mit Tumorprogression verbunden; eher Sicherheitsbedenken als Therapieansatz |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004871 | Evrenzo (Astellas Pharma Europe B.V.) | – | Anämie; chronische Niereninsuffizienz (Status: erloschen) |

---

## Sicherheitshinweise

- **Wechselwirkungen / pharmakologische Interaktion:** Roxadustat hemmt das Ziel EGLN2 (egl-9 family hypoxia inducible factor 2), eine HIF-Prolylhydroxylase. Dies ist der pharmakologische Wirkmechanismus; ein Schweregrad ist nicht angegeben.
- **Theoretisches Risiko:** Da die HIF-Aktivierung Angiogenese und Tumorprogression fördern kann, ist bei Indikationen wie Plattenepithelkarzinom oder bei Erkrankungen mit pathologischer Neovaskularisation (z. B. am Auge) besondere Vorsicht geboten.

Für weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für das Trockene-Auge-Syndrom stützt sich allein auf das TxGNN-Modell (Evidenzniveau L5), ohne klinische Studien oder Publikationen. Zudem ist die Zulassung in Deutschland erloschen, und die HIF-Aktivierung birgt theoretische Risiken (Neovaskularisation).

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen) als Voraussetzung für die Sicherheitsprüfung
- Ergänzung der Wirkmechanismus-Daten (z. B. aus DrugBank)
- Präklinische Daten zu HIF-Stabilisierung an der Augenoberfläche, einschließlich Abwägung gegen Neovaskularisationsrisiko
- Prüfung der Anwendungswege (z. B. topische Darreichung), da bisher nur eine systemische Anwendung bekannt ist
- Literatur- und Studienrecherche zu den vorhergesagten Indikationen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

