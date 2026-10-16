---
layout: default
title: Pentosan Polysulfate
parent: Nur Modellvorhersage (L5)
nav_order: 353
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Pentosan Polysulfate: vorhergesagte neue Indikation Primäre Thrombozyten-Freisetzungsstörung (Evidenzstufe L5). Ursprüngliche Indikation: Interstitielle Zystitis"
monitor_inn: "Pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
---

# Pentosan Polysulfate
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Pentosanpolysulfat: Von interstitieller Zystitis zu primärer Thrombozyten-Freisetzungsstörung

## Zusammenfassung in einem Satz

Pentosanpolysulfat wurde ursprünglich zur Behandlung der **interstitiellen Zystitis** zugelassen. Das TxGNN-Modell sagt voraus, dass es bei der **primären Thrombozyten-Freisetzungsstörung** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, sie beruht ausschließlich auf der Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Interstitielle Zystitis |
| Vorhergesagte neue Indikation | Primäre Thrombozyten-Freisetzungsstörung |
| TxGNN-Vorhersagewert | 99,71 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Pentosanpolysulfat ein heparinähnliches, sulfatiertes Polysaccharid mit schwacher gerinnungshemmender und thrombozytenbezogener Aktivität ist. Eine Wechselwirkung mit der Thrombozytenfunktion ist daher biologisch denkbar.

Allerdings würde eine solche Wirkung eine Thrombozytenfunktionsstörung eher **verschlechtern** (erhöhte Blutungsneigung) als behandeln. Zwischen der ursprünglichen Indikation (Erkrankung der Harnblase) und der vorhergesagten Indikation (Störung der Thrombozytenfunktion) besteht kein erkennbarer therapeutischer Zusammenhang. Die hohe Modellbewertung spiegelt möglicherweise nur die Nähe im Netzwerk über gemeinsame Gerinnungs- oder Thrombozytenknoten wider und keinen therapeutischen Effekt.

Weitere vom Modell hoch bewertete Vorhersagen sind:

- **Glanzmann-Thrombasthenie** (Wert 99,65 %): Ursache ist ein Mangel oder eine Funktionsstörung des Integrins αIIbβ3 (GPIIb/IIIa) mit gestörter Thrombozytenaggregation. Ein gerinnungshemmender Wirkstoff würde diese Blutungsstörung voraussichtlich verstärken. Ein plausibler therapeutischer Mechanismus ist nicht erkennbar.
- **Pseudo-von-Willebrand-Erkrankung** (Wert 99,62 %): Ursache ist eine Gain-of-Function-Mutation von GPIbα mit verstärkter Bindung an den von-Willebrand-Faktor. Eine polyanionische, heparinähnliche Substanz könnte theoretisch mit dem VWF oder der GPIb-Bindung interagieren, die Wirkrichtung ist aber unbekannt und könnte die Blutung verschlimmern.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004246 | Elmiron | – | Interstitielle Zystitis |

Diese Zulassung ist erloschen bzw. widerrufen, es gibt derzeit keine gültige Zulassung.

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph** (aus Arzneimittel-Krankheits-Beziehungen des TxGNN-Wissensgraphen PrimeKG, nicht aus dem Beipackzettel): Lebererkrankung, Gallenblasenerkrankung, Thrombozytopenie, Blutgerinnungsstörung, Hämophilie, Heparin-induzierte Thrombozytopenie.
- **Arzneimittelwechselwirkungen**: Insgesamt wurden 58 Wechselwirkungen erfasst, in der Auswertung wurden 20 aufgeführt, alle mit der Einstufung „mäßig“ (Moderate). Es handelt sich überwiegend um Wirkstoffe, die die Blutgerinnung oder Thrombozytenfunktion beeinflussen, z. B.:
  - Acetylsalicylsäure
  - Clopidogrel
  - Warfarin
  - Apixaban
  - Edoxaban
  - Dalteparin
  - Abciximab
  - Alteplase
  - Cilostazol
  - Dipyridamole
  - Bivalirudin
  - Cangrelor

  Weitere genannte Wirkstoffe sind Betrixaban, Caplacizumab, Defibrotid, Antithrombin III (human), Anistreplase sowie die radioaktiven Antikörper Ibritumomab-Tiuxetan und Tositumomab.

Die Kombination aus gerinnungshemmender Wirkung, den Wissensgraph-Kontraindikationen (Blutgerinnungsstörung, Hämophilie, Thrombozytopenie) und den vielen blutungsrelevanten Wechselwirkungen ist für alle drei vorhergesagten Indikationen, also Blutungsstörungen, ein erhebliches Sicherheitssignal. Angaben aus dem Beipackzettel (Warnhinweise, Gegenanzeigen) liegen nicht vor.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf dem Modell (Evidenzgrad L5), es gibt weder klinische Studien noch Publikationen. Zudem spricht die gerinnungshemmende Wirkung eher für eine Verschlechterung der vorhergesagten Blutungsstörungen, und die deutsche Zulassung ist erloschen.

**Für ein Weiterverfolgen ist Folgendes erforderlich:**
- Beipackzettel von BfArM (Warnhinweise und Gegenanzeigen), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Daten zum Wirkmechanismus (z. B. aus DrugBank)
- Eine Literatur- und Studienrecherche, die belegt, ob ein therapeutischer (und nicht nur ein ungünstiger) Effekt auf die Thrombozytenfunktion plausibel ist
- Prüfung der Darreichungsform und Applikationsweg, da diese Angaben für die vorhergesagten Indikationen noch nicht vorliegen
- Klärung, warum die Zulassung erloschen ist, und der aktuellen Verfügbarkeit in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

