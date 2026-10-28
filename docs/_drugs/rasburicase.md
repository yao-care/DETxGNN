---
layout: default
title: Rasburicase
parent: Nur Modellvorhersage (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Rasburicase: vorhergesagte neue Indikation Renale Hypourikämie (Evidenzstufe L5). Ursprüngliche Indikation: Hyperurikämie"
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "hepatopulmonary syndrome", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

## Rasburicase: Renale Hypourikämie
{: .text-alpha }

## Zusammenfassung

Rasburicase ist eine rekombinante Urat-Oxidase, die ursprünglich zur Behandlung der Hyperurikämie zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass sie bei **renaler Hypourikämie** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, und die mechanistische Plausibilität ist sehr gering.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hyperurikämie |
| Vorhergesagte neue Indikation | Renale Hypourikämie |
| TxGNN-Vorhersagewert | 0,9999 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Für diesen Bericht liegen derzeit keine detaillierten Daten zum Wirkmechanismus aus der Datenbank vor. Bekannt ist: Rasburicase wandelt Harnsäure in Allantoin um und senkt so den Serum-Harnsäurespiegel. Ihre Wirksamkeit bei Hyperurikämie ist belegt.

Die renale Hypourikämie ist jedoch gerade durch einen **zu niedrigen** Serum-Harnsäurespiegel gekennzeichnet, verursacht durch eine gestörte renale Urat-Rückresorption (z. B. Varianten in SLC22A12/URAT1 oder SLC2A9). Eine weitere Harnsäuresenkung hat keine therapeutische Begründung und könnte sogar das Risiko erhöhen. Der hohe Wert von 0.9999 stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, und ist kein biologischer Beleg für einen echten Nutzen.

### Weitere vorhergesagte Indikationen (Rang 2–10)

Alle weiteren Vorhersagen haben ebenfalls Evidenzgrad L5 und die Empfehlung „Hold“:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Partieller HPRT-Mangel | 0,9997 | Indirekt plausibel (akute Harnsäuresenkung), korrigiert aber nicht den Enzymdefekt. Für die Langzeitanwendung wegen Immunogenität ungeeignet; Xanthinoxidase-Hemmer sind der Standard. |
| 3 | Hepatische Porphyrie | 0,9997 | Kein erkennbarer Mechanismus, Wert wahrscheinlich durch vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen, keine biologische Evidenz |
| 4 | Primäre Pfortaderthrombose | 0,9997 | Kein Mechanismus; Behandlung erfolgt durch Antikoagulation |
| 5 | Idiopathische kupferassoziierte Zirrhose | 0,9997 | Kupferakkumulation, unabhängig vom Purinabbau |
| 6 | Früh beginnende familiäre nichtzirrhotische portale Hypertonie | 0,9997 | Kein plausibler Mechanismus, Wert wahrscheinlich durch vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen, keine biologische Evidenz |
| 7 | Hepatoportale Sklerose | 0,9997 | Kein mechanistischer Bezug, gleiches Artefakt |
| 8 | Hepatopulmonales Syndrom | 0,9997 | Urat-Oxidase spielt hier keine bekannte Rolle |
| 9 | Renale tubuläre Azidose | 0,9985 | Nur lose Verbindung über die renale Uratverarbeitung; zusätzlich Risiken (Hämolyse bei G6PD-Mangel, Methämoglobinämie, Überempfindlichkeit) |
| 10 | Störung des Phenylalanin-Stoffwechsels | 0,9983 | Kein Bezug zur Urat-Oxidase-Aktivität |

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
| EMEA/H/C/000331 | Fasturtec | – | Hyperurikämie |

Die einzige Zulassung (Inhaber: Sanofi Winthrop Industrie) ist gültig; das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 13 Wechselwirkungen identifiziert.
  - **Schwerwiegend (Major)**: Prilocain, Salpetrige Säure (Nitrit)
  - **Mäßig (Moderate)**: Lokalanästhetika wie Tetracain (ophthalmisch/topisch), Lidocain (topisch/ophthalmisch), Benzocain, Cocain (topisch/nasal), Proparacain, Oxybuprocain und Cinchocain sowie Idelalisib
- **Hinweise aus dem Wissensgraphen**: Aus dem Wissensgraphen wurden keine Kontraindikationen für Krankheiten abgeleitet.
- **Ergänzende Risiken laut Bewertung**: Bei Rasburicase sind Hämolyse bei G6PD-Mangel, Methämoglobinämie und Überempfindlichkeitsreaktionen zu beachten; die Immunogenität schränkt die chronische Anwendung ein.

Für Warnhinweise und Gegenanzeigen aus der Fachinformation siehe die Packungsbeilage bzw. Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf dem Modell (L5), ohne Studien oder Publikationen. Zudem spricht der Mechanismus gegen den Einsatz bei renaler Hypourikämie, da der Harnsäurespiegel dort bereits zu niedrig ist. Auch bei den übrigen neun Vorhersagen fehlen Evidenz und plausible Mechanismen. Das Arzneimittel ist in Deutschland mit einer gültigen Zulassung im Handel.

**Für ein Weiterverfolgen wären erforderlich:**
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen) als Voraussetzung für eine Sicherheitsprüfung
- Detaillierte Daten zum Wirkmechanismus
- Prüfung der Zulassungs- und Verfügbarkeitssituation (erloschene Zulassung)
- Mechanistische und klinische Belege für jede vorgeschlagene Indikation. Am ehesten kommt der partielle HPRT-Mangel in Frage, und dort nur für die akute Harnsäuresenkung.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

