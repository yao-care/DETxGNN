---
layout: default
title: Tagraxofusp
parent: Nur Modellvorhersage (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tagraxofusp: vorhergesagte neue Indikation Esotropie (Evidenzstufe L5). Ursprüngliche Indikation: Lymphom"
monitor_inn: "TAGRAXOFUSP"
predicted_indications: ["esotropia", "pre-malignant neoplasm", "inner ear neoplasm", "benign neoplasm of tongue", "non-seminomatous lesion", "chondroid hamartoma", "bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "cystic neoplasm", "thyroglossal duct cyst"]
---

# Tagraxofusp
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

## Tagraxofusp: Von Lymphom zu Esotropie
{: .text-alpha }

## Zusammenfassung in einem Satz

Tagraxofusp ist ein gegen CD123 gerichtetes Fusionsprotein (Interleukin-3 gekoppelt an ein verkürztes Diphtherietoxin). Laut den für diesen Bericht zusammengestellten Daten war es ursprünglich für die Behandlung von **Lymphomen** zugelassen. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Esotropie** (Schielen nach innen) voraus, allerdings gibt es dafür **keine klinischen Studien** und **keine Publikationen**; die Vorhersage beruht allein auf dem Graphmodell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Lymphom |
| Vorhergesagte neue Indikation | Esotropie |
| TxGNN-Vorhersagewert | 0,9973 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Detaillierte Daten zum Wirkmechanismus liegen in den zusammengestellten Daten nicht vor. Bekannt ist, dass Tagraxofusp ein CD123-gerichtetes Zytotoxin ist: Es bindet an CD123-exprimierende Zellen und tötet sie durch das Toxinanteil ab. Dieser Mechanismus passt zu Erkrankungen mit CD123-positiven Zellpopulationen, wie sie bei bestimmten hämatologischen Neoplasien vorkommen.

Esotropie ist dagegen eine Störung der okulären Motorik und Ausrichtung der Augen. Eine CD123-exprimierende Zielzellpopulation ist dabei nicht bekannt. Ein plausibler mechanistischer Zusammenhang zur ursprünglichen Indikation besteht daher nicht. Der hohe TxGNN-Wert ist eine rein graphbasierte Vorhersage ohne klinische oder literaturbasierte Untermauerung.

Auch die weiteren Top-10-Vorhersagen (u. a. prämaligne Neoplasie, Neoplasie des Innenohrs, gutartige Zungenneoplasie, Schilddrüsen-Zungengang-Zyste) sind mechanistisch schwach bis nicht begründbar. Allenfalls bei der prämalignen Neoplasie ist theoretisch denkbar, dass CD123-exprimierende prämaligne Klone getroffen werden; die Kategorie ist jedoch unspezifisch. Die systemische Toxizität (u. a. Kapillarlecksyndrom, Hepatotoxizität) ließe sich in solchen Situationen kaum rechtfertigen.

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
| EMEA/H/C/005031 | Elzonris | – | Lymphom |

Hinweis: Dieses Arzneimittel ist in Deutschland im Handel; die 1 vorhandene Zulassung ist gültig (1 von 1).

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Zielgerichtetes Zytotoxin (CD123-gerichtetes Fusionsprotein mit Diphtherietoxin-Anteil) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage beachten |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen der Packungsbeilage beachten |
| Überwachungsparameter | Bitte Packungsbeilage beachten; aufgrund der bekannten Risiken (Kapillarlecksyndrom, Hepatotoxizität) sind insbesondere Leberwerte und Flüssigkeitsstatus relevant |
| Schutzmaßnahmen bei der Handhabung | Bitte Packungsbeilage beachten |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 66 Wechselwirkungen gefunden (Schweregrad jeweils „moderat“, Quelle: DDInter). Beispiele in den ausgewerteten Daten betreffen v. a. Antidiabetika:
  - Orale Antidiabetika: Acarbose, Metformin, Pioglitazon, Glimepirid, Chlorpropamid
  - DPP-4-Hemmer: Alogliptin, Saxagliptin, Linagliptin
  - SGLT2-Hemmer: Canagliflozin, Dapagliflozin, Empagliflozin
  - GLP-1-Rezeptoragonisten: Albiglutid, Dulaglutid, Semaglutid
  - Insuline: Insulin aspart, degludec, detemir, glargin, glulisin, Humaninsulin (Isophan)

Weitere Sicherheitsinformationen entnehmen Sie bitte der Packungsbeilage; Warnhinweise und Gegenanzeigen aus der Fachinformation lagen für diesen Bericht nicht vor.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für Esotropie stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, nicht biologische Evidenz (Evidenzgrad L5); es liegen keine Studien oder Publikationen und kein plausibler mechanistischer Zusammenhang vor. Hinzu kommt das ernste Sicherheitsprofil des Toxins. In Deutschland besteht eine gültige Zulassung (1 von 1).

**Für ein Weiterverfolgen sind erforderlich:**
- Auswertung der Warnhinweise und Gegenanzeigen aus der Fachinformation (derzeit blockierende Datenlücke für das Sicherheits-Screening)
- Detaillierte Daten zum Wirkmechanismus (MOA)
- Nachweis einer relevanten CD123-Expression oder eines anderen biologischen Ansatzpunkts in der vorhergesagten Zielerkrankung
- Prüfung des Zulassungsstatus und der Verfügbarkeit in Deutschland
- Gegebenenfalls Priorisierung biologisch plausiblerer Kandidaten, z. B. CD123-positive hämatologische Erkrankungen, statt der aktuell vorhergesagten Indikationen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

