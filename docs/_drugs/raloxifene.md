---
layout: default
title: Raloxifene
parent: Nur Modellvorhersage (L5)
nav_order: 377
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Raloxifene"
predicted_indications: ["duodenal ulcer (disease)", "hypoalphalipoproteinemia", "duodenal obstruction", "duodenogastric reflux"]
description: "Raloxifene: vorhergesagte neue Indikation Duodenal ulcer (disease) (Evidenzstufe L5). Ursprüngliche Indikation: Osteoporosis, Postmenopausal"
---

# Raloxifene
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

## Raloxifene: Duodenal ulcer (disease)
{: .text-alpha }

## Zusammenfassung

Raloxifen ist ein selektiver Estrogenrezeptor-Modulator (SERM) und war ursprünglich zur Behandlung der postmenopausalen Osteoporose zugelassen.
Das TxGNN-Modell sagt voraus, dass es bei **Zwölffingerdarmgeschwür (Ulcus duodeni)** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Osteoporosis, Postmenopausal |
| Vorhergesagte neue Indikation | Duodenal ulcer (disease) |
| TxGNN-Vorhersagewert | 0.9972 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 3 von 3) |
| Anzahl der Zulassungen | 3 (gültig: 3) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Raloxifen als SERM an die Estrogenrezeptoren α (ESR1) und β (ESR2) sowie an den G-Protein-gekoppelten Estrogenrezeptor GPER bindet. Seine Wirksamkeit bei postmenopausaler Osteoporose ist belegt.

Ein mechanistischer Zusammenhang zwischen dieser Rezeptoraktivität und dem Schutz der Magen- bzw. Duodenalschleimhaut ist in den vorliegenden Daten **nicht belegt**. Eine solche Verbindung wäre derzeit spekulativ. Der hohe TxGNN-Wert (0,9972) stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat. Er ist kein biologischer Nachweis einer therapeutischen Wirkung.

Weitere vom Modell vorhergesagte Indikationen sind ebenfalls ohne Studien- oder Literaturbelege:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Hypoalphalipoproteinämie | 0,9965 | Raloxifen senkt LDL- und Gesamtcholesterin moderat, erhöht aber nachweislich nicht das HDL-C; Zusammenhang schwach |
| 3 | Duodenalobstruktion | 0,9964 | Überwiegend mechanische Erkrankung; pharmakologischer SERM-Effekt unwahrscheinlich |
| 4 | Duodenogastrischer Reflux | 0,9959 | Kein erkennbarer Mechanismus; präklinische Validierung nötig |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation | Status |
|---------|------|------|-----------|------|
| EMEA/H/C/000185 | Optruma | – | Postmenopausale Osteoporose | Gültig |
| EMEA/H/C/000184 | Evista | – | Postmenopausale Osteoporose | Gültig |
| EMEA/H/C/001075 | Raloxifene Teva | – | Postmenopausale Osteoporose | Gültig |

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph** (Wirkstoff-Erkrankungs-Beziehungen aus PrimeKG, kein Packungsbeilagentext): Bluthochdruck, Lebererkrankung, Gallenblasenerkrankung, Vorhofflimmern, Hypertriglyceridämie, Thrombophlebitis, koronare Herzkrankheit, Schlaganfall, zerebrovaskuläre Erkrankungen, zerebraler Infarkt, Lungenembolie, Netzhautarterienverschluss, Thrombophilie, eingeschränkte Nierenfunktion, transitorische ischämische Attacke, vertebrobasiläre Insuffizienz, Antiphospholipid-Syndrom. Auffällig ist der Schwerpunkt auf thromboembolischen und kardiovaskulären Erkrankungen.
- **Wechselwirkungen / pharmakologische Ziele** (4 Einträge, ohne Schweregrad): GPER (GPER1), Estrogenrezeptor-α (ESR1), Estrogenrezeptor-β (ESR2) und Aldehydoxidase 1 (AOX1). Dabei handelt es sich um Zielstrukturen, nicht um klassische Arzneimittelwechselwirkungen.

Für Warnhinweise und Gegenanzeigen aus der Fachinformation bitte die Packungsbeilage bzw. Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf einen Modellwert (Evidenzstufe L5) ohne klinische Studien, Literatur oder plausiblen Mechanismus.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen) über BfArM bzw. EMA, da die Sicherheitsprüfung sonst nicht fortgeführt werden kann
- Vollständige Wirkmechanismus-Daten (MOA) aus DrugBank
- Präklinische Studien zur Plausibilität eines Effekts auf die Duodenalschleimhaut
- Systematische Literaturrecherche zu Raloxifen und Ulcus duodeni
- Klärung des regulatorischen Status, da alle Zulassungen in Deutschland aufgehoben sind
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

