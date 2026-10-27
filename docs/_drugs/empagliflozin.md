---
layout: default
title: Empagliflozin
parent: Nur Modellvorhersage (L5)
nav_order: 166
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Empagliflozin: vorhergesagte neue Indikation Klassisches Stiff-Person-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: Diabetes mellitus Typ 2"
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
---

# Empagliflozin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Empagliflozin: Von Diabetes mellitus Typ 2 zu klassischem Stiff-Person-Syndrom
{: .text-alpha }

## Zusammenfassung

Empagliflozin ist ein SGLT2-Hemmer, der ursprünglich zur Behandlung von Diabetes mellitus Typ 2, Herzinsuffizienz und chronischer Niereninsuffizienz zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **klassischem Stiff-Person-Syndrom** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Diabetes mellitus Typ 2; Herzinsuffizienz; chronische Niereninsuffizienz |
| Vorhergesagte neue Indikation | Klassisches Stiff-Person-Syndrom |
| TxGNN-Vorhersagewert | 99,06 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen |
| Anzahl der Zulassungen | 3 (alle erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Für diese Vorhersage ist derzeit keine detaillierte Beschreibung des Wirkmechanismus in den für diesen Bericht zusammengestellten Daten verfügbar. Bekannt ist, dass Empagliflozin den SGLT2-Transporter im proximalen Nierentubulus hemmt und so die renale Glukoserückresorption senkt.

Das Stiff-Person-Syndrom ist eine autoimmune neurologische Erkrankung, die meist mit Anti-GAD65-Antikörpern einhergeht und die GABAerge Hemmung beeinträchtigt. Ein etablierter mechanistischer Zusammenhang mit der SGLT2-Hemmung besteht nicht. Die einzige denkbare Verbindung ist, dass Anti-GAD65-Autoimmunität auch bei Typ-1-Diabetes und anderen Autoimmunerkrankungen auftritt. Dies erklärt jedoch keine Wirkung einer SGLT2-Hemmung.

Der hohe TxGNN-Wert (0,99) ist eine rein rechnerische Vorhersage. Er wird vermutlich durch gemeinsame Nachbarn im Wissensnetzwerk getrieben und ist durch keine Studien- oder Literaturdaten gestützt.

Weitere vom Modell vorhergesagte Indikationen sind ebenfalls rein spekulativ:

| Rang | Erkrankung | TxGNN-Wert | Evidenzlevel | Einschätzung |
|------|------|------|------|------|
| 2 | Fokales Stiff-Limb-Syndrom | 99,06 % | L5 | Seltene Variante des Stiff-Person-Spektrums; kein bekannter Einfluss der SGLT2-Hemmung auf GABAerge oder glycinerge Bahnen; vermutlich Effekt gemeinsamer Netzwerknachbarn |
| 3 | Opsismodysplasie | 99,03 % | L5 | Seltene Skelettdysplasie durch INPPL1-(SHIP2-)Mutationen mit lockerer konzeptioneller Überlappung zum Insulinsignalweg; Empagliflozin moduliert SHIP2 oder die Skelettentwicklung nicht direkt; präklinische Validierung nötig |

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
| EMEA/H/C/002677 | Jardiance | – | Diabetes mellitus Typ 2; Herzinsuffizienz; chronische Niereninsuffizienz | Erloschen |
| EMEA/H/C/003770 | Synjardy | – | Diabetes mellitus Typ 2 | Erloschen |
| EMEA/H/C/003833 | Glyxambi | – | Diabetes mellitus Typ 2 | Erloschen |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Für Empagliflozin wurden insgesamt 100 Wechselwirkungen erfasst (Quelle: DDInter). Die Mehrzahl der ausgewerteten Einträge ist von mittlerem Schweregrad (Moderate), einzelne sind gering (Minor). Beispiele:
- **Mittlerer Schweregrad:** Phenylephrin, Acebutolol, Acetazolamid, Formoterol, Pseudoephedrin, Nifedipin, Epinephrin, Ethinylestradiol, Hydrocortison, Salbutamol, Ethanol, Fosinopril, Furosemid
- **Geringer Schweregrad:** Hydrocortison (topisch), Alclometason (topisch)

Für Warnhinweise und Gegenanzeigen siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Rechenmodell (L5), ohne klinische Studien, Literatur oder plausiblen Wirkmechanismus. Zudem sind alle drei deutschen Zulassungen erloschen.

**Für ein Weiterkommen sind folgende Punkte nötig:**
- Wirkmechanismus-Daten (MOA) und eine tragfähige mechanistische Hypothese für das Stiff-Person-Syndrom
- Präklinische Validierung (z. B. in Modellen der GABAergen Hemmung bzw. Autoimmunität)
- Beschaffung und Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Klärung des aktuellen Zulassungs- und Marktstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

