---
layout: default
title: Avibactam
parent: Nur Modellvorhersage (L5)
nav_order: 48
evidence_level: L5
indication_count: 4
monitor_inn: "AVIBACTAM"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "hyperamylasemia", "polyclonal hyperviscosity syndrome"]
last_modified_at: 2026-10-28
description: "Avibactam: vorhergesagte neue Indikation Ureter-Tuberkulose (Evidenzstufe L5). Ursprüngliche Indikation: Infektionen durch gramnegative Bakterien, Harnwegsinfektionen…"
---

# Avibactam
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

## Avibactam: Von bakteriellen Infektionen zu Ureter-Tuberkulose
{: .text-alpha }

## Zusammenfassung

Avibactam ist ein Beta-Laktamase-Hemmer, der in Kombination mit Antibiotika zur Behandlung von Infektionen durch gramnegative Bakterien zugelassen ist, darunter Harnwegsinfektionen, Pneumonien und Weichteilinfektionen. Das TxGNN-Modell sagt voraus, dass der Wirkstoff bei **Ureter-Tuberkulose** wirksam sein könnte. Dafür liegen **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Infektionen durch gramnegative Bakterien, Harnwegsinfektionen, nosokomiale Pneumonie, Weichteilinfektionen |
| Vorhergesagte neue Indikation | Ureter-Tuberkulose |
| TxGNN-Vorhersagewert | 0,9911 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl der Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage nachvollziehbar?

Für den Wirkstoff liegen in den für diesen Bericht zusammengestellten Daten derzeit keine detaillierten Angaben zum Wirkmechanismus vor. Bekannt ist: Avibactam ist ein Beta-Laktamase-Hemmer (Diazabicyclooctan-Typ ohne eigene antibakterielle Wirkung) und wird nur in Kombination mit einem Beta-Laktam-Antibiotikum (Ceftazidim bzw. in Emblaveo in der jeweiligen Kombination) eingesetzt.

Ein biochemisch plausibler Ansatz besteht darin, dass *Mycobacterium tuberculosis* eine chromosomal kodierte Klasse-A-Beta-Laktamase (BlaC) bildet, die Avibactam in vitro hemmen kann. In Kombination mit einem Beta-Laktam wäre daher eine Aktivität gegen Tuberkulose denkbar.

Die Einschränkung ist jedoch deutlich: Für urogenitale Tuberkulose wurden keine klinischen oder literaturbasierten Belege geliefert. Der hohe Vorhersagewert stammt vom TxGNN-Modell (Deep Learning) und spiegelt wahrscheinlich Ähnlichkeiten wider, die das Modell zwischen verwandten Erkrankungen gelernt hat, und nicht eine belegte antituberkulöse Wirkung.

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
| EMEA/H/C/006113 | Emblaveo | – | Infektionen durch gramnegative Bakterien, Harnwegsinfektionen, nosokomiale Pneumonie, Weichteilinfektionen |
| EMEA/H/C/004027 | Zavicefta | – | Bakterielle Pneumonie, Weichteilinfektionen, Pneumonie, Harnwegsinfektionen, Infektionen durch gramnegative Bakterien |

---

## Sicherheitshinweise

Bitte entnehmen Sie die Sicherheitsinformationen der Packungsbeilage bzw. Fachinformation.

---

## Weitere vorhergesagte Indikationen (zur Einordnung)

Die übrigen Vorhersagen haben ebenfalls Evidenzlevel L5 und keine Studien oder Publikationen:

| Rang | Erkrankung | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Urinäre Schistosomiasis | 0,9906 | Erreger ist ein Parasit (Trematode), kein Bakterium; kein plausibler Mechanismus. Eine bakterielle Sekundärinfektion wäre eine andere Fragestellung. |
| 3 | Hyperamylasämie | 0,9901 | Laborbefund, kein Infektionsziel; kein Mechanismus erkennbar. Der Score stammt vom TxGNN-Modell (Deep Learning) und kann vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen widerspiegeln, keine biologische Evidenz. |
| 4 | Polyklonales Hyperviskositätssyndrom | 0,9901 | Kein bekannter Einfluss auf Immunglobuline oder Blutviskosität; identischer Wert wie Rang 3 deutet auf unspezifische Vorhersage hin. |

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für Ureter-Tuberkulose gibt es weder Studien noch Publikationen, sodass nur eine Modellvorhersage (L5) vorliegt. Der einzige mechanistische Ansatz (Hemmung der BlaC-Beta-Laktamase) ist rein in-vitro-basiert, und Avibactam wirkt allein nicht antibakteriell.

**Für ein Weiterkommen sind erforderlich:**
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM/EMA)
- Präklinische bzw. In-vitro-Daten zu Beta-Laktam/Avibactam-Kombinationen gegen *M. tuberculosis*
- Literaturrecherche zu urogenitaler Tuberkulose und Beta-Laktamase-Hemmern
- Prüfung der Verabreichungswege und Eignung für die urogenitale Tuberkulose
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

