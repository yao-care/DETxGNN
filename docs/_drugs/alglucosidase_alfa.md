---
layout: default
title: Alglucosidase Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alglucosidase Alfa: vorhergesagte neue Indikation Adulte Polyglucosan-Körper-Krankheit (adult polyglucosan body disease) (Evidenzstufe L5). Ursprüngliche Indikation: Glykogenspeicherkrankheit Typ II"
monitor_inn: "ALGLUCOSIDASE ALFA"
predicted_indications: ["adult polyglucosan body disease", "glycogen storage disease due to glycogen branching enzyme deficiency, fatal perinatal neuromuscular form", "glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form", "congenital entropion", "congenital ectropion", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "epiblepharon", "ptosis-strabismus-ectopic pupils syndrome"]
---

# Alglucosidase Alfa
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

# Alglucosidase alfa: Von Glykogenspeicherkrankheit Typ II zur Adulten Polyglucosan-Körper-Krankheit

## Zusammenfassung in einem Satz

Alglucosidase alfa ist eine rekombinante saure alpha-Glucosidase, die ursprünglich zur Behandlung der Glykogenspeicherkrankheit Typ II (Morbus Pompe) eingesetzt wurde. Das TxGNN-Modell sagt voraus, dass sie bei der **adulten Polyglucosan-Körper-Krankheit** (APBD) wirksam sein könnte. Diese Vorhersage beruht jedoch ausschließlich auf einer Netzwerkanalyse: Es liegen **keine klinischen Studien** und **keine Publikationen** vor.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Glykogenspeicherkrankheit Typ II |
| Vorhergesagte neue Indikation | Adulte Polyglucosan-Körper-Krankheit (adult polyglucosan body disease) |
| TxGNN-Vorhersagewert | 99,47 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Alglucosidase alfa ist eine rekombinante saure alpha-Glucosidase als Enzymersatztherapie. Sie baut Glykogen im Lysosom ab, und ihre Wirksamkeit bei Morbus Pompe gilt als etabliert.

Die APBD wird durch einen Mangel am Glykogen-Verzweigungsenzym (GBE1) verursacht. Dadurch häuft sich schlecht verzweigtes, unlösliches Polyglucosan in Neuronen und anderen Geweben an. Eine denkbare, aber unbelegte Überlegung ist, dass das Enzym die Glykogenlast senken könnte. Die Vorhersage ergibt sich aus der gemeinsamen Nachbarschaft im Glykogenstoffwechsel-Netzwerk, nicht aus klinischen Daten.

Die mechanistische Passung ist **schwach**:
- Polyglucosan sammelt sich überwiegend im Zytoplasma an, nicht im Lysosom, wo das Enzym wirkt.
- Das Enzym überwindet die Blut-Hirn-Schranke nur unzureichend, obwohl die APBD vor allem das Nervensystem betrifft.

---

## Klinische Evidenz

Derzeit sind keine einschlägigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine einschlägige Literatur verfügbar.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000636 | Myozyme (Sanofi B.V.) | – | Glykogenspeicherkrankheit Typ II (Status: erloschen) |

---

## Sicherheitsaspekte

Bitte entnehmen Sie die Sicherheitsinformationen der Packungsbeilage. Für Wechselwirkungen wurden keine Einträge gefunden.

---

## Weitere Vorhersagen (zur Einordnung)

Neben der APBD wurden neun weitere Indikationen mit ähnlich hohen Scores vorhergesagt (jeweils 99,1–99,3 %). Für keine liegen Studien oder Literatur vor (alle L5):

| Rang | Vorhergesagte Indikation | Einschätzung |
|------|------|------|
| 2–3 | Glykogenspeicherkrankheit durch GBE1-Mangel (letale perinatale und kongenitale neuromuskuläre Form) | Primärdefekt liegt in der Glykogenverzweigung, nicht im lysosomalen Abbau; nur indirekter Zusammenhang. Bei der perinatalen Form zudem kaum Zeitfenster für eine Intervention. |
| 4–6, 9 | Kongenitales Entropium, kongenitales Ektropium, kongenitales Horner-Syndrom, Epiblepharon | Strukturelle bzw. neurogene Fehlbildungen ohne plausiblen Mechanismus; wahrscheinlich Artefakte der Netzwerktopologie. |
| 7, 8, 10 | Ptosis-Stimmbandlähmung-Syndrom, Camptodaktylie-Myopie-Fibrose des M. rectus medialis, Ptosis-Strabismus-ektope-Pupillen-Syndrom | Seltene Entwicklungs- bzw. neurogene Syndrome; Überschneidungen betreffen nur Symptome, nicht die Ursache. Wahrscheinlich falsch-positive Vorhersagen. |

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich allein auf Netzwerkähnlichkeit (Evidenzniveau L5). Es gibt weder Studien noch Publikationen, die mechanistische Passung ist schwach, und die einzige deutsche Zulassung ist erloschen.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Daten zum Wirkmechanismus (MOA) ergänzen
- Warnhinweise und Gegenanzeigen aus der Packungsbeilage ergänzen; diese Lücke blockiert aktuell das Sicherheitsscreening
- Präklinische Belege prüfen, ob die Enzymersatztherapie zytoplasmatisches Polyglucosan erreichen und die Blut-Hirn-Schranke überwinden kann
- Systematische Literatur- und Studienrecherche zur APBD
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

