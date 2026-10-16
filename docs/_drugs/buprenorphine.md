---
layout: default
title: Buprenorphine
parent: Nur Modellvorhersage (L5)
nav_order: 82
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Buprenorphine: vorhergesagte neue Indikation Akute intermittierende Porphyrie (Evidenzstufe L5). Ursprüngliche Indikation: Opioid-bezogene Störungen (Opioidabhängigkeit)"
---

# Buprenorphine
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

# Buprenorphin: Von Opioidabhängigkeit zu akuter intermittierender Porphyrie

## Zusammenfassung in einem Satz

Buprenorphin ist ein Opioid, das bisher zur Behandlung von Opioidabhängigkeit zugelassen war (Opioid-bezogene Störungen).
Das TxGNN-Modell sagt voraus, dass es bei **akuter intermittierender Porphyrie** wirksam sein könnte, doch dafür gibt es **keine klinischen Studien** und nur **eine Publikation** (einen Fallbericht zum Narkosemanagement), die keine therapeutische Wirkung belegt.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Opioid-bezogene Störungen (Opioidabhängigkeit) |
| Vorhergesagte neue Indikation | Akute intermittierende Porphyrie |
| TxGNN-Vorhersagewert | 99,41 % |
| Evidenzniveau | L4 (laut den für diesen Bericht zusammengestellten Daten; faktisch liegt nur eine Modellvorhersage ohne therapeutische Studien vor) |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassungen |
| Anzahl der Zulassungen | 4 (alle aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus von Buprenorphin liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Buprenorphin ein partieller Agonist am μ-Opioidrezeptor ist und bei Opioidabhängigkeit eingesetzt wird. Ein mechanistischer Zusammenhang mit der akuten intermittierenden Porphyrie ist nicht erkennbar.

Die einzige gefundene Publikation (1993) beschreibt die Narkoseführung bei einer Patientin mit Porphyrie. Sie betrifft den sicheren perioperativen Einsatz von Arzneimitteln, nicht die Behandlung der Erkrankung. Buprenorphin gilt bei Porphyrie allgemein als Wirkstoff, der Vorsicht erfordert. Der hohe TxGNN-Wert ist daher sehr wahrscheinlich ein Artefakt der Graphstruktur und kein Hinweis auf einen therapeutischen Nutzen.

### Weitere vorhergesagte Indikationen (zur Einordnung)

| Rang | Indikation | TxGNN-Wert | Evidenz | Einschätzung |
|---|---|---|---|---|
| 2 | Lingual-faziale-bukkale Dyskinesie | 99,32 % | L4 | Nur indirekte Hinweise (Opioide bei Agitation bei Demenz, Rezeptorwechselwirkungen im Tiermodell); mehrere Treffer thematisch irrelevant |
| 3 | Chronische Tic-Störung | 99,13 % | L5 | Nur Vorhersage, keine Studien oder Literatur |
| 4 | Kontinuierliche Spike-Waves im Schlaf | 99,05 % | L5 | Opioide können prokonvulsiv wirken; Sicherheitsbedenken |
| 5 | Benigne Shuddering-Attacken | 99,03 % | L5 | Gutartige, selbstlimitierende Erkrankung; ungünstiges Nutzen-Risiko-Verhältnis |
| 6 | Extrapyramidale und Bewegungsstörungen | 99,03 % | L5 | Sehr breite Kategorie, vermutlich Graphnähe statt spezifischer Mechanismus |

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Fachzeitschrift | Kernaussagen |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Fallbericht | Masui (Jpn J Anesthesiol) | Narkosemanagement bei einer Patientin mit akuter intermittierender Porphyrie bei einer Operation wegen eines Ovarialtumors; betrifft keine Therapie der Erkrankung |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004651 | Buvidal | – | Opioid-bezogene Störungen |
| EMEA/H/C/006188 | Buprenorphine Neuraxpharm | – | Opioid-bezogene Störungen |
| EMEA/H/C/004407 | Zubsolv | – | Opioid-bezogene Störungen |
| EMEA/H/C/000697 | Suboxone | – | Opioid-bezogene Störungen |

Alle vier Zulassungen sind aufgehoben.

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraph (PrimeKG, keine Angaben aus Fachinformationen):** Unter anderem Long-QT-Syndrom, Torsades de pointes, orthostatische Hypotonie, chronisch obstruktive Lungenerkrankung, Atemversagen, Lebererkrankungen, Hepatitis B/C, Nebenniereninsuffizienz, Hypothyreose, paralytischer Ileus, Darmverschluss, benigne Prostatahyperplasie, Gallenwegserkrankungen, Harnröhrenstriktur, erhöhter Hirndruck (Pseudotumor cerebri), Drogenabhängigkeit/Substanzmissbrauch.
- **Arzneimittelwechselwirkungen (100 Einträge, Auswahl der Einstufung „schwerwiegend“):** Alvimopan, Bupropion, Morphin, Cisaprid, Dolasetron. Weitere Wechselwirkungen mittleren Schweregrades bestehen u. a. mit Famotidin, Loperamid, Atropin, Dexamethason, Clarithromycin und Cimetidin.
- **Besonderer Hinweis:** Buprenorphin gilt bei Porphyrie als vorsichtig einzusetzender Wirkstoff; die vorhergesagte Indikation ist daher sicherheitlich kritisch zu sehen.

Für Warnhinweise und Gegenanzeigen aus der Fachinformation ist die Packungsbeilage heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die vorhergesagte Indikation gibt es weder klinische Studien noch eine belastbare mechanistische Grundlage; die einzige Publikation betrifft das Narkosemanagement. Zudem ist Buprenorphin bei Porphyrie nur mit Vorsicht anzuwenden, und in Deutschland bestehen derzeit keine gültigen Zulassungen. Auch die übrigen vorhergesagten Indikationen sind nicht ausreichend belegt.

**Zum Fortfahren sind folgende Schritte erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) vom BfArM beschaffen und auswerten, da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Detaillierte Wirkmechanismus-Daten (MOA) aus DrugBank ergänzen
- Prüfung der Sicherheit bei Porphyrie (Porphyrinogenität) anhand von Fachliteratur und Datenbanken
- Systematische Literaturrecherche zur Wirksamkeit bei den vorhergesagten Indikationen, insbesondere bei Dyskinesien
- Klärung des aktuellen Zulassungs- und Vertriebsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

