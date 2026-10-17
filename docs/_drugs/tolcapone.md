---
layout: default
title: Tolcapone
parent: Nur Modellvorhersage (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tolcapone: vorhergesagte neue Indikation Rasmussen-Enzephalitis (subakute Rasmussen-Enzephalitis) (Evidenzstufe L5). Ursprüngliche Indikation: Morbus Parkinson"
monitor_inn: "TOLCAPONE"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome"]
---

# Tolcapone
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Tolcapon: Von Morbus Parkinson zu Rasmussen-Enzephalitis (subakute Rasmussen-Enzephalitis)

## Zusammenfassung

Tolcapon ist ein COMT-Hemmer, der ursprünglich zur Behandlung der Parkinson-Krankheit eingesetzt wurde.
Das TxGNN-Modell sagt voraus, dass er bei der **Rasmussen-Enzephalitis** (subakute Rasmussen-Enzephalitis) wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Morbus Parkinson |
| Vorhergesagte neue Indikation | Rasmussen-Enzephalitis (subakute Rasmussen-Enzephalitis) |
| TxGNN-Vorhersagewert | 99,93 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Tolcapon ein COMT-Hemmer (Catechol-O-Methyltransferase) ist, dessen Wirksamkeit bei Morbus Parkinson belegt ist. Er verlängert dort die Wirkung von Levodopa.

Ein mechanistischer Zusammenhang zur Rasmussen-Enzephalitis, einer immunvermittelten chronischen Enzephalitis, ist aus den vorliegenden Daten nicht erkennbar. Der hohe Modellwert (0,999) ist eine reine Modellvorhersage ohne Unterstützung durch Studien oder Literatur. Der Weg über Signalwege lässt sich daher nicht überprüfen.

Auch die weiteren vom Modell vorhergesagten Indikationen (z. B. Myelitis, PLA2G6-assoziierte Neurodegeneration, Lewy-Körper-Demenz) sind überwiegend ohne Evidenz. Lediglich bei der Lewy-Körper-Demenz gibt es eine plausible, aber nur präklinisch gestützte Verbindung über die gemeinsame Alpha-Synuclein-Pathologie und dopaminerge Dysfunktion. Dies wäre bei einer Neubewertung eine Option mit vergleichsweise besserer Begründung.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000132 | Tasmar (Viatris Healthcare Limited) | – | Morbus Parkinson |

Diese Zulassung ist erloschen bzw. aufgehoben; es besteht derzeit keine gültige Zulassung.

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph (keine Angaben aus dem Beipackzettel):** Im TxGNN-Wissensgraphen (PrimeKG) sind folgende Erkrankungen als Kontraindikationen verzeichnet: Lebererkrankung, Gallenblasenerkrankung, Melanom, hypotensive Störung, Rhabdomyolyse, noduläre Fasziitis, Spätdyskinesie sowie linguo-fazio-bukkale Dyskinesie.
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 65 Wechselwirkungen erfasst. Als **schwerwiegend (Major)** gilt die Wechselwirkung mit **Methylenblau**. Mehrere Wechselwirkungen sind **mittelschwer (Moderate)**, u. a. mit Epinephrin (auch ophthalmisch/topisch), Morphin (auch liposomal), Opium, Codein, Dronabinol, Nabilon, Naltrexon, Metoclopramid, Ethanol, Promethazin, Chlorphenamin, Cetirizin und Dextromethorphan. Geringfügig (Minor) sind Warfarin und Dicoumarol; bei Omeprazol ist die Einstufung unbekannt.
- **Hinweis zur Hepatotoxizität:** Tolcapon ist für Leberschäden bekannt. Dies ist besonders relevant bei Erkrankungen mit Leberbeteiligung und deckt sich mit der Kontraindikation „Lebererkrankung“ im Wissensgraphen.

Warnhinweise und Kontraindikationen aus der Fachinformation liegen nicht vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (Evidenzgrad L5), ohne klinische Studien, Literatur oder erkennbaren mechanistischen Zusammenhang. Zudem besteht in Deutschland keine gültige Zulassung, und die bekannte Lebertoxizität erhöht die Anforderungen an eine neue Indikation.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Wirkmechanismus-Daten (MOA) ergänzen, z. B. über DrugBank
- Warnhinweise und Kontraindikationen aus der Fachinformation (BfArM) beschaffen und auswerten (derzeit blockierende Datenlücke für das Sicherheitsscreening)
- Gezielte Literaturrecherche und präklinische Prüfung eines möglichen Zusammenhangs mit Rasmussen-Enzephalitis
- Alternativ die Lewy-Körper-Demenz (präklinisch gestützt, Evidenzgrad L4) als aussichtsreichere Indikation prüfen
- Klärung des Zulassungsstatus und der Machbarkeit eines Wiedereinsatzes in Deutschland unter Berücksichtigung des Leberrisikos
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

