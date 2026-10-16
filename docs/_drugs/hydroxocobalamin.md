---
layout: default
title: Hydroxocobalamin
parent: Nur Modellvorhersage (L5)
nav_order: 224
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Hydroxocobalamin: vorhergesagte neue Indikation Ösophagusvarizen mit Blutung (zusätzlich vorhergesagt: Ösophagusvariz… (Evidenzstufe L5). Ursprüngliche Indikation: Vergiftung"
monitor_inn: "HYDROXOCOBALAMIN"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding"]
---

# Hydroxocobalamin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Hydroxocobalamin: Von Vergiftung zu Ösophagusvarizen mit Blutung

## Zusammenfassung in einem Satz

Hydroxocobalamin ist eine Form von Vitamin B12 und wird ursprünglich als Antidot bei **Vergiftungen** (insbesondere Cyanidvergiftung) eingesetzt. Das TxGNN-Modell sagt voraus, dass es bei **Ösophagusvarizen mit Blutung** wirksam sein könnte. Für diese Vorhersage liegen **keine klinischen Studien und keine Publikationen** vor, sie beruht ausschließlich auf der Modellvorhersage.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Vergiftung |
| Vorhergesagte neue Indikation | Ösophagusvarizen mit Blutung (zusätzlich vorhergesagt: Ösophagusvarizen ohne Blutung) |
| TxGNN-Vorhersagewert | 99,23 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Ehrlich gesagt: Ein belastbarer mechanistischer Zusammenhang ist nicht erkennbar. Hydroxocobalamin bindet Cyanid und fängt zudem Stickstoffmonoxid (NO) ab, was den Blutdruck erhöhen kann. Die Pathophysiologie der Varizenblutung (portale Hypertonie, Wandspannung der Varizen, Gerinnungsstörungen) wird dadurch nicht adressiert. Detaillierte Daten zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten nicht vor.

Ein spekulatives Argument wäre, dass die NO-Abfangwirkung die splanchnische oder intrahepatische Vasodilatation beeinflusst. Dafür gibt es hier keine Evidenz, und der Effekt könnte sogar kontraproduktiv sein, da eine NO-Reduktion die portale Hypertonie theoretisch verschlechtern könnte.

Der hohe TxGNN-Wert (0,992) ist identisch für beide vorhergesagten Indikationen (mit und ohne Blutung). Das deutet eher auf eine Assoziation auf Ebene der Krankheitsklasse im Wissensgraphen hin als auf ein indikationsspezifisches Signal. Auch bei der nicht blutenden Form beruht die Prophylaxe auf einer Senkung des Portaldrucks (nichtselektive Betablocker, endoskopische Bandligatur), wofür die bekannte Pharmakologie von Hydroxocobalamin nichts beiträgt.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000806 | Cyanokit (SERB SA) | – | Vergiftung |

Diese Zulassung ist als erloschen geführt; es gibt derzeit keine gültige Zulassung in Deutschland.

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph** (aus dem TxGNN-Wissensgraphen, nicht aus dem Beipackzettel): Hypertensive Erkrankung, Hypertonie. Das passt zur bekannten blutdrucksteigernden Wirkung über NO-Abfangen.
- **Arzneimittelwechselwirkungen**: 32 Wechselwirkungen wurden erfasst. Als **moderat** eingestuft sind:
  - Arsentrioxid
  - Chloramphenicol
  - Iodid I-131
  - Iodid I-123

  Weitere Wechselwirkungen (u. a. Omeprazol, Lansoprazol, Simvastatin, Loperamid, Prednisolon, Ranitidin, Acetylsalicylsäure, Budesonid, Folsäure, Valsartan, Ramipril, Lorazepam, Citalopram, Paracetamol, Mirtazapin, Levothyroxin) sind ohne bekannte Schweregradeinstufung.

Angaben aus dem Beipackzettel zu Warnhinweisen und Gegenanzeigen liegen nicht vor; bitte hierzu die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (L5), ohne klinische Studien oder Publikationen. Ein plausibler Wirkmechanismus fehlt, und die blutdrucksteigernde sowie NO-abfangende Wirkung könnte bei portaler Hypertonie sogar nachteilig sein. Zudem besteht in Deutschland derzeit keine gültige Zulassung.

**Für eine Weiterverfolgung sind folgende Schritte nötig:**
- Prüfung, ob der identische Score für beide Indikationen ein Artefakt der Krankheitsklasse im Wissensgraphen ist
- Daten zum Wirkmechanismus ergänzen (DrugBank) und eine fundierte mechanistische Analyse durchführen
- Fachinformation (Warnhinweise, Gegenanzeigen) von der BfArM-Website beschaffen, da dies für ein Sicherheitsscreening zwingend erforderlich ist
- Präklinische Evidenz zum Effekt auf portale Hypertonie bzw. Varizenblutung erheben, bevor klinische Überlegungen angestellt werden
- Klärung der Zulassungs- und Darreichungsformsituation (aktuell nur erloschene Zulassung)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

