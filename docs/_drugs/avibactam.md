---
layout: default
title: Avibactam
parent: Nur Modellvorhersage (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Avibactam: vorhergesagte neue Indikation Streptokokken-Pneumonie (Evidenzstufe L5). Ursprüngliche Indikation: Infektionen durch gramnegative Bakterien, Harnwegsinfektionen…"
---

# Avibactam
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

# Avibactam: Von bakteriellen Infektionen zu Streptokokken-Pneumonie

## Zusammenfassung in einem Satz

Avibactam ist ein Beta-Lactamase-Inhibitor, der ausschließlich in Kombination mit anderen Antibiotika eingesetzt wird. Er ist ursprünglich zugelassen zur Behandlung von Infektionen durch gramnegative Bakterien, Harnwegsinfektionen, Pneumonien und Weichteilinfektionen. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Streptokokken-Pneumonie** voraus, doch dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Infektionen durch gramnegative Bakterien, Harnwegsinfektionen, nosokomial erworbene Pneumonie, Weichteilinfektionen |
| Vorhergesagte neue Indikation | Streptokokken-Pneumonie |
| TxGNN-Vorhersagewert | 99,70 % |
| Evidenzgrad | L5 (nur Modellvorhersage; in den Daten als L4 geführt, aber ohne konkrete Studien belegt) |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassungen |
| Anzahl der Zulassungen | 2 (beide erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus liegen derzeit nicht vor. Bekannt ist: Avibactam ist ein Nicht-Beta-Lactam-Beta-Lactamase-Inhibitor, der Enzyme der Ambler-Klassen A und C sowie einige der Klasse D hemmt. Er wird nur zusammen mit Ceftazidim vermarktet und besitzt selbst keine nennenswerte antibakterielle Eigenwirkung.

Die Verbindung zur vorhergesagten Indikation ist nur indirekt. Die bestehenden Indikationen umfassen bakterielle Pneumonien (nosokomial und beatmungsassoziiert), und der hohe Modellwert spiegelt vermutlich diese Ähnlichkeit in der Indikationsklasse wider.

Mechanistisch spricht eher wenig für einen Zusatznutzen: *Streptococcus pneumoniae* wird gegen Beta-Lactame vor allem durch veränderte Penicillin-bindende Proteine resistent, nicht durch Beta-Lactamase-Bildung. Ein Beta-Lactamase-Inhibitor trägt hier daher wenig bei.

---

## Klinische Evidenz

Derzeit sind keine einschlägigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine einschlägige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/006113 | Emblaveo | – | Infektionen durch gramnegative Bakterien, Harnwegsinfektionen, nosokomial erworbene Pneumonie, Weichteilinfektionen |
| EMEA/H/C/004027 | Zavicefta | – | Bakterielle Pneumonie, Weichteilinfektionen, Pneumonie, Harnwegsinfektionen, Infektionen durch gramnegative Bakterien |

Beide Zulassungen sind laut den vorliegenden Daten erloschen.

---

## Weitere vorhergesagte Indikationen (zur Einordnung)

| Rang | Erkrankung | Score | Evidenz | Einschätzung |
|---|---|---|---|---|
| 2 | Schwere Influenza (Anfälligkeit) | 99,28 % | L5 | Kein direkter Mechanismus; allenfalls sekundäre bakterielle Pneumonie, die bereits abgedeckt ist. Vermutlich Artefakt des Wissensgraphen. |
| 3 | Ureter-Tuberkulose | 99,11 % | L5 | *M. tuberculosis* besitzt die Beta-Lactamase BlaC, die Avibactam in vitro hemmt; rein präklinische Überlegung. |
| 4 | Urogenitale Schistosomiasis | 99,06 % | L5 | Parasitose, kein antiparasitärer Mechanismus bekannt; vermutlich Assoziation über den Harntrakt. |
| 5 | Hyperamylasämie | 99,01 % | L5 | Laborbefund, kein plausibles Ziel; wahrscheinlich Graph-Artefakt. |
| 6 | Polyklonales Hyperviskositätssyndrom | 99,01 % | L5 | Kein mechanistischer Bezug; unspezifische Modellausgabe. |

---

## Sicherheitsaspekte

Zu den Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) liegen keine Daten vor; bitte die Fachinformation heranziehen. Zu Wechselwirkungen wurden keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für Streptokokken-Pneumonie gibt es weder klinische Studien noch Literatur; der Vorhersagewert beruht vermutlich auf der Ähnlichkeit zu bestehenden Pneumonie-Indikationen. Zudem spricht der Resistenzmechanismus von *S. pneumoniae* gegen einen Zusatznutzen eines Beta-Lactamase-Inhibitors, und in Deutschland sind keine gültigen Zulassungen mehr vorhanden.

**Für ein Weiterkommen sind erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) aus der Quelle des BfArM bzw. der EMA beschaffen und auswerten
- Daten zum Wirkmechanismus (z. B. aus DrugBank) ergänzen
- Klärung des aktuellen Zulassungs- und Verfügbarkeitsstatus in Deutschland
- In-vitro-Daten und systematische Literaturrecherche zur Aktivität von Ceftazidim-Avibactam gegen *S. pneumoniae*
- Ein Vorteil gegenüber den bestehenden Standardtherapien müsste nachgewiesen werden
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

