---
layout: default
title: Silodosin
parent: Nur Modellvorhersage (L5)
nav_order: 427
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "SILODOSIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
description: "Silodosin: vorhergesagte neue Indikation Ambras type hypertrichosis universalis congenita (Evidenzstufe L5). Ursprüngliche Indikation: Prostatic Hyperplasia"
---

# Silodosin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

## Silodosin: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## Zusammenfassung

Silodosin ist ein Arzneistoff, der ursprünglich zur Behandlung der benignen Prostatahyperplasie zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei der **Ambras-Typ Hypertrichosis universalis congenita** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Prostatic Hyperplasia |
| Vorhergesagte neue Indikation | Ambras type hypertrichosis universalis congenita |
| TxGNN-Vorhersagewert | 0.9999 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 3 von 3) |
| Anzahl der Zulassungen | 3 (gültig: 3) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Silodosin ein selektiver Alpha-1A-Adrenozeptor-Antagonist ist, der zur Behandlung der benignen Prostatahyperplasie eingesetzt wird. Seine Wirksamkeit bei dieser Erkrankung beruht auf der Entspannung der glatten Muskulatur in Prostata und Blasenhals.

Das Ambras-Syndrom ist eine seltene genetische Erkrankung mit übermäßigem Haarwuchs. Sie wird mit Chromosom-8q-Umlagerungen in Verbindung gebracht, die die Regulation von TRPS1 beeinflussen. Ein plausibler Zusammenhang zwischen der Alpha-1A-Blockade und diesem genetischen Mechanismus ist nicht erkennbar. Der sehr hohe TxGNN-Wert (0,9999) ist eine rein graphbasierte Vorhersage und spiegelt vermutlich die Nähe im Netzwerk zu haarbezogenen Phänotypen wider, nicht eine biologische Begründung.

Auch bei der zweitplatzierten Vorhersage, der Hypertrichose allgemein, ist die Wirkrichtung unklar: Einige gefäßerweiternde oder blutdrucksenkende Substanzen (z. B. Minoxidil) verursachen Hypertrichose, sodass ein Effekt eher als Nebenwirkung denn als Therapie zu erwarten wäre.

Weitere vorhergesagte Indikationen (ebenfalls ohne Evidenz): Fehlbildungssyndrom mit Zahn- bzw. Parodontalbeteiligung, Syndrom mit Dandy-Walker-Malformation, isolierte genetische Haarschaftanomalie und familiäre isolierte Trichomegalie (Werte zwischen 0,9923 und 0,9999).

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/001092 | Urorec | – | Benigne Prostatahyperplasie |
| EMEA/H/C/001209 | Silodyx | – | Benigne Prostatahyperplasie |
| EMEA/H/C/004964 | Silodosin Recordati | – | Benigne Prostatahyperplasie |

Alle drei Zulassungen (Inhaber: Recordati Ireland Ltd) sind gültig; das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (aus Arzneimittel-Krankheits-Beziehungen des Modells, nicht aus Fachinformationstexten): Multisystematrophie, posturales orthostatisches Tachykardiesyndrom, orthostatische Hypotonie, Leberversagen, Nierenerkrankung, Pyoureter, intraoperatives Floppy-Iris-Syndrom.
- **Arzneimittelwechselwirkungen**: Insgesamt wurden 99 Wechselwirkungen identifiziert. Eine als **schwerwiegend (Major)** eingestufte Wechselwirkung besteht mit **Clarithromycin**. Beispiele für **moderate** Wechselwirkungen: Bupropion, Aprepitant, Morphin, Dexamethason, Cimetidin, Miconazol, Clotrimazol, Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin, Dronabinol, Nabilon, Eliglustat, Rolapitant, Metreleptin, Glycerolphenylbutyrat und Opium.

Für Warnhinweise und Gegenanzeigen aus der Fachinformation siehe bitte die Packungsbeilage.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Es gibt weder klinische Studien noch Publikationen, und ein biologischer Zusammenhang zwischen Alpha-1A-Blockade und dem Ambras-Syndrom ist nicht erkennbar. Zudem ist das Arzneimittel in Deutschland mit drei gültigen Zulassungen im Handel. Die Vorhersage stützt sich ausschließlich auf den Modellwert des TxGNN-Modells (Deep Learning); dieser kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, und stellt keinen biologischen Beleg dar.

**Für ein Weiterverfolgen sind erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation des BfArM (derzeit fehlend; blockierend für die Sicherheitsprüfung)
- Präklinische Belege (z. B. Haarfollikel-Modelle) für einen plausiblen Wirkzusammenhang
- Klärung der Wirkrichtung (therapeutischer Effekt versus unerwünschte Wirkung)
- Prüfung der Darreichungsform und des Anwendungswegs im Hinblick auf die neue Indikation
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

