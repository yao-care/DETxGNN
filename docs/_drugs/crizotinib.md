---
layout: default
title: Crizotinib
parent: Nur Modellvorhersage (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Crizotinib: vorhergesagte neue Indikation Gingivale Fibromatose (Evidenzstufe L5). Ursprüngliche Indikation: Nicht-kleinzelliges Lungenkarzinom"
---

# Crizotinib
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

# Crizotinib: Von nicht-kleinzelligem Lungenkarzinom zu gingivaler Fibromatose

## Zusammenfassung

Crizotinib ist ein Kinase-Inhibitor, der ursprünglich zur Behandlung des nicht-kleinzelligen Lungenkarzinoms (NSCLC) zugelassen wurde. Das TxGNN-Modell sagt voraus, dass er bei **gingivaler Fibromatose** wirksam sein könnte (Score 99,81 %). Für diese Vorhersage liegen jedoch **keine klinischen Studien und keine Publikationen** vor; sie beruht ausschließlich auf der Modellvorhersage.

Hinweis: Die Vorhersage mit dem höchsten Score ist zugleich die am schlechtesten belegte. Unter den weiteren Kandidaten hat „Lungen-Keimzelltumor" (Rang 6) die relativ beste Datenlage (2 Studien, Evidenzstufe L3). Dieser Kandidat wird am Ende des Berichts kurz erwähnt.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht-kleinzelliges Lungenkarzinom |
| Vorhergesagte neue Indikation | Gingivale Fibromatose |
| TxGNN-Vorhersagescore | 99,81 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/aufgehobene Zulassung |
| Anzahl der Zulassungen | 1 (0 gültig, 1 aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Aus den Informationen zu den Kandidaten ist bekannt, dass Crizotinib die Rezeptor-Tyrosinkinasen ALK, ROS1 und MET hemmt. Seine Wirksamkeit beim ALK- bzw. ROS1-positiven NSCLC ist belegt.

Für die gingivale Fibromatose ist **kein mechanistischer Zusammenhang** dokumentiert. Es gibt keinen bekannten Signalweg, der diese Zielstrukturen mit der hereditären gingivalen Fibromatose verbindet. Der sehr hohe Score ist daher mit Vorsicht zu interpretieren und kann ein Artefakt des Wissensgraphen sein. Auch die Ähnlichkeit zur ursprünglichen Indikation wurde bislang nicht bewertet.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002489 | Xalkori (Pfizer Europe MA EEIG) | – | Nicht-kleinzelliges Lungenkarzinom (Status: aufgehoben) |

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Klassifikation | Zielgerichtete Therapie (Tyrosinkinase-Inhibitor, ALK/ROS1/MET) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten |
| Überwachungsparameter | Bitte Fachinformation beachten; aus den Daten ergeben sich Hinweise auf Leber- und Herzüberwachung (siehe Sicherheit) |
| Handhabungsschutz | Bitte Fachinformation beachten |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Es wurden 100 Wechselwirkungen erfasst. Davon sind in der Auswahl als **schwerwiegend (Major)** eingestuft:
- Clarithromycin
- Cisaprid
- Dolasetron
- Eliglustat
- Granisetron

Als **mäßig (Moderate)** eingestuft sind u. a. Famotidin, Metformin, Loperamid, Bupropion, Aprepitant, Dexamethason, Bisacodyl und Budesonid.

**Sicherheitssignale aus der Literatur:** In den abgerufenen Publikationen werden Fälle von tödlichem fulminantem Leberversagen sowie multiplen kardialen Toxizitäten (Bradykardie, QT-Verlängerung, Kammerflimmern, Perikarditis) unter Crizotinib beschrieben. Dies sind Einzelfallberichte, sie sind bei jeder Umwidmung aber zu berücksichtigen.

Weitere Sicherheitsinformationen (Warnhinweise, Kontraindikationen) entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der Vorhersage fehlen klinische Studien, Literatur und ein plausibler Wirkmechanismus; sie beruht allein auf dem Modellscore. Zudem ist die einzige deutsche Zulassung aufgehoben, und die Fachinformation mit Sicherheitsangaben konnte nicht ausgewertet werden.

**Für ein Weiterkommen sind folgende Schritte erforderlich:**
- Fachinformation des BfArM beschaffen und auswerten (Warnhinweise, Kontraindikationen); dies ist eine blockierende Datenlücke für das Sicherheits-Screening
- Wirkmechanismus (MOA) aus DrugBank ergänzen
- Pathophysiologische Prüfung, ob ALK/ROS1/MET bei gingivaler Fibromatose eine Rolle spielen
- Klärung des Zulassungs- bzw. Verfügbarkeitsstatus in Deutschland

**Hinweis zu den übrigen Kandidaten:** Der Kandidat „Lungen-Keimzelltumor" (Score 99,73 %) erreicht Evidenzstufe L3 und die Einstufung „Research Question". Belegt sind zwei biomarkergesteuerte Basket-Studien (NCT01121588, Phase 1b, abgebrochen; NCT02465060, NCI-MATCH, Phase 2), die jedoch nicht spezifisch für diese Indikation sind. Die meisten übrigen Kandidaten sind entweder reine Vorhersagen (L5) oder stützen sich auf Literatur zum NSCLC, also zur bereits bestehenden Indikation.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

