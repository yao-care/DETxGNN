---
layout: default
title: Brolucizumab
parent: Nur Modellvorhersage (L5)
nav_order: 79
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Brolucizumab: vorhergesagte neue Indikation Mitochondriale Störung der oxidativen Phosphorylierung durch nukleäre… (Evidenzstufe L5). Ursprüngliche Indikation: Feuchte Makuladegeneration"
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices without bleeding", "esophageal varices with bleeding", "exocrine pancreatic insufficiency"]
---

# Brolucizumab
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

## Brolucizumab: Von feuchter Makuladegeneration zu mitochondrialer Störung der oxidativen Phosphorylierung (nukleäre DNA-Anomalien)
{: .text-alpha }

## Zusammenfassung

Brolucizumab ist ein gegen VEGF-A gerichtetes Antikörperfragment (scFv), das ins Auge injiziert wird und ursprünglich zur Behandlung der **feuchten Makuladegeneration** zugelassen wurde.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei einer **mitochondrialen Störung der oxidativen Phosphorylierung durch nukleäre DNA-Anomalien** voraus.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Feuchte Makuladegeneration |
| Vorhergesagte neue Indikation | Mitochondriale Störung der oxidativen Phosphorylierung durch nukleäre DNA-Anomalien |
| TxGNN-Vorhersagewert | 99,67 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Detaillierte Daten zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten nicht vor. Bekannt ist, dass Brolucizumab ein VEGF-A-Inhibitor in Form eines Einzelketten-Antikörperfragments ist, der für die intravitreale Anwendung mit sehr geringer systemischer Exposition vorgesehen ist.

Primäre mitochondriale Störungen der oxidativen Phosphorylierung entstehen durch Defekte in nukleär kodierten Untereinheiten oder Assemblierungsfaktoren der Atmungskette. Die Hemmung von VEGF-A greift an dieser Ursache nicht an. Ein klarer mechanistischer Zusammenhang zur ursprünglichen Indikation ist daher nicht erkennbar.

Der sehr hohe TxGNN-Wert spiegelt lediglich eine Vorhersage aus dem Wissensgraphen wider und wird durch keine Studie gestützt. Zudem könnte eine systemische VEGF-Blockade bei metabolisch vulnerablen Patienten eher schaden als nützen.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004913 | Beovu (Novartis Europharm Limited) | – | Feuchte Makuladegeneration |

Diese Zulassung ist erloschen (Status: Cancelled).

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (PrimeKG, nicht aus der Fachinformation):** Uveitis, Iriserkrankung, Ziliarkörpererkrankung, Panuveitis, infektiöse Augenerkrankung, Konjunktivitis.
- **Hinweis zur Klasse:** Anti-VEGF-Wirkstoffe sind mit Blutungs-, Thromboembolie- und Wundheilungsrisiken verbunden; bei einer systemischen Anwendung in einer metabolisch vulnerablen Population ist Vorsicht geboten.
- **Arzneimittelwechselwirkungen:** Keine Einträge gefunden.

Für weitere Sicherheitsinformationen ist die Fachinformation heranzuziehen.

---

## Weitere vorhergesagte Indikationen

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Evidenzniveau | Einschätzung |
|---|---|---|---|---|
| 2 | Ösophagusvarizen ohne Blutung | 99,12 % | L5 | Hold. Spekulativer Zusammenhang über VEGF-getriebene Angiogenese bei portaler Hypertonie; bei intravitrealer Anwendung ist keine relevante splanchnische Wirkung zu erwarten. Etablierte Standardtherapie vorhanden. |
| 3 | Ösophagusvarizen mit Blutung | 99,12 % | L5 | Hold. Gleiche Überlegung, zusätzlich Sicherheitsbedenken (Blutungsrisiko unter Anti-VEGF) bei akuter Varizenblutung. |
| 4 | Exokrine Pankreasinsuffizienz | 99,07 % | L5 | Hold. Kein plausibler mechanistischer Zusammenhang; Therapie erfolgt durch Enzymersatz. |

Für alle drei Indikationen liegen weder Studien noch Literatur vor.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (L5) ohne Studien oder Publikationen. Es gibt keinen plausiblen mechanistischen Zusammenhang, und die einzige deutsche Zulassung ist erloschen. Zudem könnte eine systemische VEGF-Blockade bei dieser Patientengruppe schädlich sein.

**Für ein Weiterverfolgen wären erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Präklinische Belege für einen Zusammenhang zwischen VEGF-A-Hemmung und mitochondrialen Erkrankungen
- Bewertung der Applikationsroute (intravitreal vs. systemisch) und der Sicherheit bei systemischer Exposition
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

