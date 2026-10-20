---
layout: default
title: Benazepril
parent: Nur Modellvorhersage (L5)
nav_order: 57
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril: vorhergesagte neue Indikation Maligne hypertensive Nierenerkrankung (Evidenzstufe L5). Ursprüngliche Indikation: Hypertonie (arterielle Hypertonie)"
monitor_inn: "Benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Benazepril
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Benazepril: Von Hypertonie zu maligner hypertensiver Nierenerkrankung

## Zusammenfassung in einem Satz

Benazepril ist ein ACE-Hemmer, der ursprünglich zur Behandlung von Bluthochdruck (Hypertonie) eingesetzt wird.
Das TxGNN-Modell sagt voraus, dass er bei **maligner hypertensiver Nierenerkrankung** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hypertonie (arterielle Hypertonie) |
| Vorhergesagte neue Indikation | Maligne hypertensive Nierenerkrankung |
| TxGNN-Vorhersagewert | 99,65 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassungen |
| Anzahl der Zulassungen | 2 (beide aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Benazepril das Angiotensin-konvertierende Enzym (ACE) hemmt. Es senkt dadurch den Blutdruck und verringert den Druck in den Nierenglomeruli. Die klinische Anwendung gilt Bluthochdruck, Herzinsuffizienz und chronischer Niereninsuffizienz.

Die vorhergesagte Indikation liegt sehr nah an der ursprünglichen: Die maligne hypertensive Nierenerkrankung ist eine Folge schwerer, beschleunigter Hypertonie. ACE-Hemmer werden bei hypertensiver Nephropathie breit eingesetzt. Es handelt sich daher eher um eine Erweiterung der bestehenden Indikation als um ein echtes Repurposing. Für diese spezielle maligne (akzelerierte) Verlaufsform liegen jedoch keine Studien oder Publikationen vor.

Weitere vom Modell hoch bewertete Vorhersagen (jeweils ohne belastbare Evidenz):
- **Maligne renovaskuläre Hypertonie** (99,65 %): mechanistisch schlüssig (Aktivierung des Renin-Angiotensin-Systems), aber ACE-Hemmer bergen bei beidseitiger Nierenarterienstenose oder Stenose bei Einzelniere das Risiko eines akuten Nierenfunktionsverlusts. Entscheidung: Hold.
- **Pulmonale Hypertonie, unklarer multifaktorieller Mechanismus** (99,60 %): Eine Wirksamkeit von ACE-Hemmern bei pulmonaler Hypertonie ist nicht belegt. Entscheidung: Hold.
- **Pulmonale Hypertonie bei Lungenerkrankung/Hypoxie** (99,60 %): Keine direkte Evidenz. Vasodilatatoren können hier das Ventilations-Perfusions-Verhältnis verschlechtern. Entscheidung: Hold.
- **Braddock-Syndrom** (99,44 %): sehr seltene Erkrankung ohne erkennbare mechanistische Begründung; der hohe Wert ist vermutlich ein Artefakt des Wissensgraphen. Entscheidung: Hold.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Für die Hauptindikation (maligne hypertensive Nierenerkrankung) liegen derzeit keine zugehörigen Publikationen vor.

Für die pulmonale Hypertonie bei Lungenerkrankung/Hypoxie wurden zwar drei Publikationen gefunden, diese sind jedoch nicht relevant. Sie betreffen präklinische Studien zu traditionellen chinesischen Kräuterformeln bei Nieren- bzw. Herzfibrose im Tiermodell. Weder Benazepril noch pulmonale Hypertonie wurden untersucht; die Treffer entstanden offenbar über Stichwörter wie „Hypoxie“ und „Fibrose“.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/V/C/002524 | Cardalis | – | – (aufgehoben) |
| EMEA/V/C/002804 | Fortekor Plus | – | – (aufgehoben) |

Beide Zulassungen sind EU-Zentralzulassungen (EMEA/V = Tierarzneimittel) und wurden aufgehoben. Es besteht keine gültige Zulassung.

---

## Sicherheitshinweise

**Kontraindikationen laut Wissensgraph** (aus Wirkstoff-Krankheits-Beziehungen, nicht aus Packungsbeilagentext):
- Leber- und Gallenerkrankungen: Leberversagen, Lebererkrankung, Gallenblasenerkrankung, hepatische Enzephalopathie/Leberkoma, Pankreatitis
- Nierenerkrankungen: Nierenerkrankung, Anurie, Pyoureter
- Angioödeme: einschließlich hereditärem, erworbenem und durch RAAS-Blocker ausgelöstem Angioödem
- Stoffwechsel/Elektrolyte: Kaliummangel, Diabetes mellitus, diabetische Ketoazidose, Hyperurikämie, Hyperparathyreoidismus
- Blutbild: Neutropenie, Agranulozytose
- Weitere: systemischer Lupus erythematodes (auch pädiatrisch), Bindegewebserkrankungen, Knochen- und Knorpelerkrankungen, Hypotonie, Neugeborenenikterus

**Arzneimittelwechselwirkungen:** Im Datensatz ist nur das pharmakologische Target ACE verzeichnet; konkrete Wechselwirkungen mit anderen Arzneimitteln sind nicht aufgeführt.

Weitere Sicherheitsinformationen entnehmen Sie bitte der Packungsbeilage. Die Warnhinweise und Gegenanzeigen aus der Fachinformation liegen bislang nicht vor.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage ist mechanistisch plausibel, liegt aber sehr nah an der bestehenden Hypertonie-Indikation. Es gibt weder klinische Studien noch relevante Literatur (Evidenzgrad L5). Zudem besteht in Deutschland keine gültige Zulassung, und die vorhandenen aufgehobenen Zulassungen betreffen Tierarzneimittel.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Fachinformation/Packungsbeilage des BfArM beschaffen und auswerten (Warnhinweise, Gegenanzeigen); diese Lücke blockiert derzeit die Sicherheitsprüfung
- Daten zum Wirkmechanismus ergänzen (z. B. aus DrugBank)
- Gezielte Literaturrecherche zu ACE-Hemmern bei maligner hypertensiver Nephropathie
- Klären, ob ein humanes Benazepril-Präparat in Deutschland verfügbar ist
- Sicherheitsbewertung zu Nierenarterienstenose, Hyperkaliämie und Angioödem
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

