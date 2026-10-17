---
layout: default
title: Enzalutamide
parent: Nur Modellvorhersage (L5)
nav_order: 172
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Enzalutamide: vorhergesagte neue Indikation Prostatakrebs-/Hirntumor-Suszeptibilität (Evidenzstufe L5). Ursprüngliche Indikation: Prostatatumoren (Prostatakarzinom)"
monitor_inn: "ENZALUTAMIDE"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Enzalutamide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Enzalutamid: Von Prostatatumoren zu Prostatakrebs-/Hirntumor-Suszeptibilität

## Zusammenfassung

Enzalutamid ist ein Androgenrezeptor-Inhibitor und wurde ursprünglich zur Behandlung von Prostatatumoren zugelassen. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Prostatakrebs-/Hirntumor-Suszeptibilität** voraus. Dafür gibt es derzeit **keine klinischen Studien** und **keine Publikationen**; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Prostatatumoren (Prostatakarzinom) |
| Vorhergesagte neue Indikation | Prostatakrebs-/Hirntumor-Suszeptibilität |
| TxGNN-Vorhersagewert | 99,71 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | ✗ Nur erloschene/aufgehobene Zulassungen |
| Anzahl der Zulassungen | 3 (alle aufgehoben) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Enzalutamid ist ein Androgenrezeptor-(AR-)Inhibitor. Seine Wirksamkeit beim Prostatakarzinom ist etabliert, und der hohe Modellwert spiegelt vermutlich die enge Verbindung zu dieser Erkrankung wider.

Die vorhergesagte „Indikation" ist jedoch ein Begriff für eine **genetische Veranlagung** und kein behandelbarer Krankheitszustand. Es gibt dafür kein klares therapeutisches Ziel, das ein Arzneimittel gezielt angehen könnte. Der hohe Score ist daher wahrscheinlich ein Artefakt der Nähe zum Prostatakarzinom im Wissensgraphen und kein belastbarer Hinweis auf einen neuen Nutzen. Es wurden weder Studien noch Literatur gefunden, die diese Vorhersage stützen.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation | Status |
|---------|------|------|-----------|------|
| EMEA/H/C/002639 | Xtandi (Astellas Pharma Europe B.V.) | nicht angegeben | Prostatatumoren | aufgehoben |
| EMEA/H/C/006612 | Enzalutamide Accordpharma (Accord Healthcare) | nicht angegeben | Prostatatumoren | aufgehoben |
| EMEA/H/C/006299 | Enzalutamide Viatris (Viatris Limited) | nicht angegeben | Prostatatumoren | aufgehoben |

Alle drei Zulassungen sind als aufgehoben geführt. Aktuell gültige Zulassungen liegen nicht vor.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Klassifikation | Zielgerichtete Hormontherapie (Androgenrezeptor-Inhibitor), kein konventionelles Zytostatikum |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Überwachungsparameter | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Schutzmaßnahmen beim Umgang | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |

---

## Sicherheitsaspekte

**Arzneimittelinteraktionen:** In den Daten sind 100 Wechselwirkungen verzeichnet. Als **schwerwiegend (Major)** eingestuft sind:
- Bupropion
- Dolasetron
- Eliglustat

Als **mäßig (Moderate)** eingestuft sind unter anderem:
- Famotidin
- Rabeprazol
- Omeprazol
- Hydrocortison
- Dexamethason
- Clarithromycin
- Aprepitant
- Loperamid
- Empagliflozin
- Linagliptin
- Saxagliptin

Die Einstufungen stammen aus der Datenbank DDInter. Laut der Modellbewertung sind insbesondere Interaktionen über CYP3A4 und CYP2C8 zu prüfen.

Zu Warnhinweisen und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage bezieht sich auf einen Suszeptibilitätsbegriff ohne therapeutisch adressierbares Ziel. Es gibt weder Studien noch Publikationen (Evidenzlevel L5), und alle deutschen Zulassungen sind aufgehoben. Eine Weiterverfolgung dieser Indikation ist derzeit nicht gerechtfertigt.

**Für ein Weiterkommen wären nötig:**
- Klärung, ob der Begriff überhaupt eine behandelbare klinische Indikation abbildet
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM), da ohne sie keine Sicherheitsprüfung möglich ist
- Prüfung des aktuellen Zulassungsstatus, da alle drei Zulassungen als aufgehoben geführt werden
- Bewertung der übrigen Vorhersagen: Die Vorhersage „männlicher Reproduktionsorgankrebs" ist durch Phase-3-Studien wie ENZAMET gestützt (Evidenzlevel L1, Proceed with Guardrails). Sie entspricht aber im Kern der ursprünglichen Indikation Prostatakarzinom und ist daher keine echte Neuindikation.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

