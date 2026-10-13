---
layout: default
title: Ivabradine
parent: Nur Modellvorhersage (L5)
nav_order: 251
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Ivabradin: Von Angina pectoris und Herzinsuffizienz zu Hypertrichose

## Zusammenfassung

Ivabradin wurde ursprünglich zur Behandlung von Angina pectoris und Herzinsuffizienz zugelassen. Das TxGNN-Modell sagt voraus, dass es bei **Hypertrichose** wirksam sein könnte. Für diese Vorhersage liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf einer Modellberechnung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Angina pectoris; Herzinsuffizienz |
| Vorhergesagte neue Indikation | Hypertrichose |
| TxGNN-Vorhersagewert | 99,79 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassungen |
| Anzahl der Zulassungen | 5 (alle aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus von Ivabradin liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Ivabradin die HCN-Kanäle (If-Strom, „Funny Current") hemmt, die vor allem in den Schrittmacherzellen des Herzens untersucht werden. Dadurch senkt es die Herzfrequenz.

Ein belegter Zusammenhang zwischen HCN-Kanälen und der Biologie des Haarfollikels oder der Haarwuchsregulation ist in den vorliegenden Daten nicht dokumentiert. Der sehr hohe TxGNN-Wert (0,998) ist eine reine Vorhersage aus dem Wissensgraphen. Hinzu kommt, dass Hypertrichose bei manchen Arzneimitteln als Nebenwirkung auftritt; ob die Vorhersage eine therapeutische oder eine verursachende Richtung meint, ist unklar.

Auch die weiteren Vorhersagen mit hohen Werten wirken mechanistisch nicht nachvollziehbar und sind vermutlich Artefakte der Netzwerknähe im Wissensgraphen:

| Rang | Vorhergesagte Erkrankung | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Ambras-Syndrom (Hypertrichosis universalis congenita) | 99,72 % | Seltene genetische Erkrankung; kein plausibler Mechanismus über HCN-Blockade |
| 3 | Fehlbildungssyndrom mit Zahn- und/oder Parodontalbeteiligung | 99,72 % | Kein erkennbarer Bezug zur Herzfrequenzsenkung |
| 4 | Syndrom mit Dandy-Walker-Malformation | 99,70 % | Strukturelle Fehlbildung; durch HCN-Blockade nicht umkehrbar |
| 5 | Isolierte genetische Haarschaftanomalie | 99,69 % | Kein bekannter Zusammenhang mit HCN-Hemmung |
| 6 | Nephrogenes Syndrom der inadäquaten Antidiurese | 99,08 % | Ivabradin wirkt nicht auf den V2-Rezeptor |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000597 | Procoralan | – | Angina pectoris; Herzinsuffizienz |
| EMEA/H/C/000598 | Corlentor | – | Angina pectoris; Herzinsuffizienz |
| EMEA/H/C/004187 | Ivabradine Anpharm | – | Angina pectoris; Herzinsuffizienz |
| EMEA/H/C/004241 | Ivabradine Accord | – | Angina pectoris; Herzinsuffizienz |
| EMEA/H/C/004117 | Ivabradine Zentiva | – | Angina pectoris; Herzinsuffizienz |

Alle fünf Zulassungen haben den Status „aufgehoben".

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Die Datenbankabfrage ergab insgesamt 100 Wechselwirkungen; im Folgenden sind Beispiele aus den vorliegenden Daten aufgeführt.

- **Schwerwiegend (Major):** Aprepitant, Clarithromycin, Dolasetron, Palonosetron, Cisaprid, Clotrimazol, Granisetron, Levofloxacin, Ondansetron, Papaverin, Cobicistat
- **Moderat (Moderate):** Famotidin, Ranitidin, Dexamethason, Cimetidin, Metreleptin, Miconazol, Nizatidin, Troglitazon

Weitere Sicherheitsinformationen entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzgrad L5) ohne Studien oder Publikationen, und ein plausibler Mechanismus zwischen HCN-Blockade und Haarwuchs fehlt. Zudem sind in Deutschland derzeit keine gültigen Zulassungen vorhanden.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Detaillierte Daten zum Wirkmechanismus (MOA)
- Klärung, ob die Vorhersage therapeutisch oder als Nebenwirkung zu verstehen ist
- Präklinische Daten oder Literaturrecherche zu HCN-Kanälen im Haarfollikel
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen) für die Sicherheitsbewertung
- Klärung des aktuellen Zulassungs- und Vermarktungsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

