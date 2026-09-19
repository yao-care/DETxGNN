---
layout: default
title: Sotatercept
parent: Nur Modellvorhersage (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: Von undokumentierter Originalindikation zu akuter lymphoblastischer Leukämie

## Zusammenfassung in einem Satz

> Dieses Evidenzpaket enthält keine bestätigte Originalindikation oder Wirkmechanismus-Daten für Sotatercept (DrugBank-ID DB12118).
> Die Top-Vorhersage des TxGNN-Modells ist **akute lymphoblastische Leukämie** mit einem Score von **99.78%**,
> aber dies wird durch **keine klinischen Studien** und **keine Publikationen** gestützt — die Vorhersage ist nur Modellausgabe (L5), und die eigene Begründung des Arzneistoffs kennzeichnet sie als Schlussfolgerung vom Typ „Datenbankverbindung" mit niedriger Plausibilität, anstatt als mechanistisch begründete Hypothese.

---

## Schneller Überblick

| Eintrag | Inhalt |
|---------|---------|
| Originalindikation | Nicht verfügbar — kein genehmigter Indikationstext in der Datei (Arzneistoff nicht vermarktet, keine Lizenzunterlagen) |
| Vorhergesagte neue Indikation | Akute lymphoblastische Leukämie |
| TxGNN-Vorhersage-Score | 99.78% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten für Sotatercept sind in diesem Evidenzpaket nicht verfügbar (`original_moa` ist leer). Basierend auf dem Begründungstext zu den Vorhersagen wird Sotatercept als **Aktivin-Rezeptor-IIA-Fc-Fusionsprotein (Ligandenfalle)** beschrieben, das die Aktivin/GDF/BMP-Signalisierung innerhalb der TGF-β-Superfamilie hemmt. Dieser Signalweg hat bekannte Rollen bei der hämatopoetischen Differenzierung und der Knochenmarksmikroumgebung — aber die Begründung für die höchstbewertete Vorhersage (akute lymphoblastische Leukämie) besagt explizit, dass es **keinen bekannten direkten mechanistischen Zusammenhang** zur leukämischen Zellproliferation gibt, und charakterisiert den hohen TxGNN-Score eher als Datenbankverbindungs-Artefakt als als biologisch begründetes Signal.

Da sowohl die Originalindikation als auch der Wirkmechanismus hier undokumentiert sind, kann die Beziehung zwischen „was Sotatercept derzeit behandelt" und „was die Vorhersage ist, das es behandelt" nicht bewertet werden. Unter den zehn bewerteten Vorhersagen merken die eigenen Anmerkungen des Modells an, dass **arzneimittelinduzierte Osteoporose** (Rang 4) eine vergleichsweise stärkere mechanistische Plausibilität hat, da bekannt ist, dass Aktivin-Rezeptor-IIA-Ligandenfallen (eine Klasse, die Luspatercept einschließt) den Knochenstoffwechsel beeinflussen — aber auch diese Indikation wird nicht durch klinische Studien oder Literatur gestützt und würde eine Präklinik-Validierung vor weiterer Bewertung erfordern.

---

## Evidenz aus klinischen Studien

Derzeit keine damit verbundenen klinischen Studien registriert

---

## Evidenz aus der Literatur

Derzeit keine damit verbundene Literatur verfügbar

---

## Informationen zum deutschen Markt

Sotatercept ist derzeit in dieser Gerichtsbarkeit **nicht vermarktet** (`market_status: Not marketed`), mit **0 Zulassungen** in der Datei. Keine Lizenzunterlagen sind verfügbar zur Zusammenfassung.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: TFDA/BfArM-Packungsbeilage-Warnhinweise und Kontraindikationen sind als Blockierungsdatenlücke (DG001) gekennzeichnet — dies ist erforderlich, bevor eine S1-Sicherheitsvorprüfung durchgeführt werden kann.)*

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Alle zehn TxGNN-Vorhersagen für Sotatercept sind Evidenzstufe L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur), und die eigene Bewertung des Systems empfiehlt durchgehend „Abwarten". Die am höchsten bewertete Indikation (akute lymphoblastische Leukämie) ist in ihrer eigenen Begründung explizit als biologisch implausibel gekennzeichnet und stellt eher eine Schlussfolgerung vom Typ „Datenbankverbindung" dar als eine gestützte Hypothese.

**Um fortzufahren, ist Folgendes erforderlich:**
- Bestätigte Originalindikation(en) und Zulassungsgeschichte für Sotatercept (derzeit leer)
- Wirkmechanismus-Daten über DrugBank-API (DG002, hoher Schweregrad)
- TFDA/BfArM-Packungsbeilage (Warnhinweise, Kontraindikationen) zur Aufhebung der S1-Sicherheitsvorprüfung (DG001, Blockierung)
- Falls das Osteoporose-Signal verfolgt wird (Rang 4, vergleichsweise stärkere mechanistische Begründung über den Aktivin-Rezeptor/Knochenstoffwechsel-Signalweg): Präklinische Knochendichte-Daten vor jeder klinischen Bewertung
- Zumindest vorläufige Literatur oder Präklinik-Evidenz für jede potenzielle Indikation, bevor über S0 hinausgegangen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

