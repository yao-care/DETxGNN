---
layout: default
title: Agomelatine
parent: Nur Modellvorhersage (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Agomelatine: vorhergesagte neue Indikation Benigne paroxysmale Torticollis des Säuglingsalters (Rang 1) (Evidenzstufe L5). Ursprüngliche Indikation: Major Depression"
---

# Agomelatine
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

# Agomelatin: Von der Major Depression zur benignen paroxysmalen Torticollis des Säuglingsalters

## Zusammenfassung in einem Satz

Agomelatin ist ein Antidepressivum, das ursprünglich zur Behandlung der Major Depression (depressive Episoden bei Erwachsenen) eingesetzt wurde. Das TxGNN-Modell sagt für den Spitzenkandidaten **benigne paroxysmale Torticollis des Säuglingsalters** eine mögliche Wirksamkeit voraus. Dafür liegen jedoch **keine klinischen Studien und keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

Hinweis: Dieser Kandidat hat keinen erkennbaren biologischen Bezug zu Agomelatin. Die Indikationen **Melancholie**, **neurotische Depression** und **dysthymische Störung** haben eine deutlich plausiblere Evidenzbasis (siehe unten).

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Major Depression |
| Vorhergesagte neue Indikation | Benigne paroxysmale Torticollis des Säuglingsalters (Rang 1) |
| TxGNN-Vorhersagewert | 99,96 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Aus der Literatur und den Rezeptordaten ist bekannt: Agomelatin ist ein Agonist an den melatonergen Rezeptoren MT1 und MT2 sowie ein Antagonist am Serotonin-5-HT2C-Rezeptor. Dadurch kann es zirkadiane Rhythmen normalisieren und die Freisetzung von Dopamin und Noradrenalin im präfrontalen Kortex steigern. Die Bindung an 5-HT2A- und 5-HT2B-Rezeptoren ist ebenfalls beschrieben.

Für die benigne paroxysmale Torticollis des Säuglingsalters, eine episodische Erkrankung im Kindesalter (häufig mit CACNA1A-Varianten assoziiert), ist **kein mechanistischer Zusammenhang** erkennbar. Der hohe Modellwert ist wahrscheinlich ein Artefakt der Netzwerknähe im Wissensgraphen.

Mechanistisch deutlich besser begründet sind andere Vorhersagen aus der Liste:

- **Melancholie** (Score 99,88 %): schwere Unterform der Major Depression, also im Wesentlichen eine Überschneidung mit der ursprünglichen Indikation.
- **Neurotische Depression** (99,88 %) und **dysthymische Störung** (99,86 %): mildere bzw. chronische depressive Störungen, auf die sich der antidepressive Mechanismus plausibel übertragen lässt.
- **Agoraphobie** (99,95 %) und **neurotische Störung** (99,90 %): indirekte Begründung über anxiolytische Effekte und gemeinsame serotonerge/zirkadiane Signalwege.
- Seltene genetische Syndrome (Ohdo-Syndrom, Keppen-Lubinsky-Syndrom) und die Conjunctivitis lignosa zeigen keinen biologischen Bezug.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

Zum Vergleich: Für die besser begründeten Alternativkandidaten wurde Literatur gefunden. Für **Melancholie** und **neurotische Depression** sind es überwiegend allgemeine Übersichten und Netzwerk-Metaanalysen zu Antidepressiva (z. B. Cipriani et al., Lancet 2018, [PMID 29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/)) sowie Übersichten zu Agomelatin (z. B. [PMID 24033095](https://pubmed.ncbi.nlm.nih.gov/24033095/)). Für die **dysthymische Störung** liegt eine Metaanalyse placebokontrollierter RCTs zu Antidepressiva vor ([PMID 21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/), 2011), die Agomelatin nicht nachweislich einschließt. Keine dieser Arbeiten ist spezifisch für die jeweilige Diagnose.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000915 | Valdoxan | – | Major Depression (Status: aufgehoben) |

---

## Sicherheitsaspekte

- **Pharmakologische Zielstrukturen** (aus der Wechselwirkungsabfrage): 5-HT2A-, 5-HT2B-, 5-HT2C-, MT1- und MT2-Rezeptor. Das sind Zielstrukturen des Wirkstoffs selbst, keine klassischen Arzneimittelwechselwirkungen mit anderen Wirkstoffen.

Für Warnhinweise und Gegenanzeigen siehe die Packungsbeilage bzw. Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die benigne paroxysmale Torticollis des Säuglingsalters liegt ausschließlich eine Modellvorhersage ohne Studien, Literatur oder mechanistische Begründung vor (Evidenzstufe L5). Zudem ist die deutsche Zulassung aufgehoben.

**Für ein Weiterkommen sind erforderlich:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen); derzeit fehlt diese Information und blockiert die Sicherheitsprüfung.
- Daten zum Wirkmechanismus aus einer verlässlichen Arzneimitteldatenbank.
- Priorisierung der Kandidaten mit plausiblerem Bezug (Melancholie, neurotische Depression, dysthymische Störung) und gezielte Suche nach agomelatin-spezifischen Studien in diesen Subtypen. Diese tragen derzeit die Stufe L4 mit der Einstufung „Forschungsfrage".
- Klärung des Zulassungsstatus in Deutschland, da nur eine aufgehobene Zulassung vorliegt.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

