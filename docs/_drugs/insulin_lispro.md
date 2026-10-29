---
layout: default
title: Insulin Lispro
parent: Nur Modellvorhersage (L5)
nav_order: 245
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
description: "Insulin Lispro: vorhergesagte neue Indikation Autoimmune Oophoritis (Evidenzstufe L5). Ursprüngliche Indikation: Diabetes mellitus"
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

## Insulin lispro: Autoimmune Oophoritis
{: .text-alpha }

## Zusammenfassung in einem Satz

Insulin lispro ist ein schnell wirksames Insulinanalogon, das ursprünglich zur Behandlung von Diabetes mellitus eingesetzt wird.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **autoimmuner Oophoritis** voraus,
hierfür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor – die Vorhersage beruht ausschließlich auf der Modellrechnung.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Diabetes mellitus |
| Vorhergesagte neue Indikation | Autoimmune Oophoritis |
| TxGNN-Vorhersagewert | 0,9978 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 5 von 5) |
| Anzahl der Zulassungen | 5 (gültig: 5) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus liegen für diesen Bericht derzeit nicht vor. Bekannt ist: Insulin lispro ist ein schnell wirksames Insulinanalogon, das am Insulinrezeptor wirkt und den Glukosestoffwechsel reguliert. Seine Wirksamkeit bei Diabetes mellitus ist gut belegt.

Ein direkter mechanistischer Zusammenhang mit autoimmuner Oophoritis ist nicht erkennbar. Denkbar ist allenfalls eine indirekte Verbindung über die Überlappung autoimmuner polyendokriner Erkrankungen (z. B. gemeinsam mit Typ-1-Diabetes). Diese Verbindung ist spekulativ und stützt Insulin nicht als Therapie der ovariellen Autoimmunität. Der hohe TxGNN-Wert ist eine rein rechnerische Vorhersage.

**Weitere vom Modell vorhergesagte Indikationen (alle ohne belastbare Evidenz):**

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Evidenzniveau | Einordnung |
|---|---|---|---|---|
| 2 | Thiaminabhängiges Dysfunktionssyndrom | 0,9937 | L5 | Insulin kann nur die diabetische Komponente symptomatisch behandeln, nicht die Grunderkrankung |
| 3 | Fokales Stiff-Limb-Syndrom | 0,9936 | L5 | Gemeinsame Anti-GAD65-Autoimmunität, Insulin wirkt nicht auf die Steifigkeit |
| 4 | Klassisches Stiff-Person-Syndrom | 0,9936 | L5 | Behandlung der Begleiterkrankung Diabetes, nicht krankheitsmodifizierend |
| 5 | Opsismodysplasie | 0,9934 | L5 | INPPL1 (SHIP2) reguliert den Insulin-/PI3K-Signalweg, Nutzen von Insulin unklar |
| 6 | Arzneimittelinduzierte lokalisierte Lipodystrophie | 0,9909 | L5 | Insulin ist selbst eine bekannte Ursache, daher keine Therapieoption |
| 7 | Pankreasagenesie | 0,9909 | L5 | Insulinersatz rational, entspricht aber der ursprünglichen Indikation (Diabetes) |
| 8 | Zentrifugale Lipodystrophie | 0,9904 | L5 | Keine etablierte mechanistische Begründung |
| 9 | Druckinduzierte lokalisierte Lipoatrophie | 0,9903 | L5 | Insulininjektionen können selbst Lipoatrophie verursachen, Sicherheitsbedenken |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für die Top-Vorhersage (autoimmune Oophoritis) ist derzeit keine zugehörige Literatur verfügbar.

Für die weiter unten gelistete Vorhersage Pankreasagenesie liegt eine einzelne, nur indirekt relevante Referenz vor:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | Journal of the American Pharmaceutical Association | Übersicht zur zunehmenden Insulintherapie bei Typ-2-Diabetes und zum praktischen Therapiebeginn; betrifft nicht direkt die Pankreasagenesie |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005037 | Lyumjev (zuvor Liumjev) | – | Diabetes mellitus |
| EMEA/H/C/000088 | Humalog | – | Diabetes mellitus |
| EMEA/H/C/000393 | Liprolog | – | Diabetes mellitus |
| EMEA/H/C/006158 | Bysumlog | – | Diabetes mellitus |
| EMEA/H/C/004303 | Insulin lispro Sanofi | – | Diabetes mellitus |

Von den fünf Zulassungen sind derzeit vier gültig; das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Die Abfrage ergab 100 Wechselwirkungen. Unter den ersten 20 Treffern sind überwiegend Wechselwirkungen mittleren Schweregrads (moderat), z. B. mit:
  - Sympathomimetika/Beta-Agonisten: Phenylephrin, Pseudoephedrin, Epinephrin, Formoterol, Salbutamol
  - Betablocker: Acebutolol
  - Weitere Antidiabetika: Metformin, Alogliptin, Albiglutide
  - Hormone: Estradiol, Ethinylestradiol, Levonorgestrel, Hydrocortisol (Hydrocortison)
  - Sonstige: Acetazolamid, Doxycyclin, Hydrochlorothiazid, Alpelisib, Ethanol
  - Geringfügige Wechselwirkungen (minor): topische Kortikosteroide (Hydrocortison topisch, Alclometason topisch)
- **Weitere Hinweise:** Lokalisierte Lipodystrophie an der Injektionsstelle ist eine bekannte Nebenwirkung von Insulin einschließlich Insulinanaloga. Das ist relevant für die vorhergesagten Indikationen Lipodystrophie und Lipoatrophie.

Für Warnhinweise und Gegenanzeigen siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die vorhergesagte Indikation autoimmune Oophoritis gibt es weder klinische Studien noch Literatur, und ein mechanistischer Zusammenhang ist nicht belegt (Evidenzniveau L5). Zudem sind derzeit 4 von 5 Zulassungen gültig, das Arzneimittel ist im Handel. Auch die übrigen Vorhersagen sind entweder mechanistisch nicht plausibel, symptomatisch (Begleiterkrankung Diabetes) oder betreffen Zustände, die Insulin selbst verursachen kann.

**Für ein Weiterverfolgen ist Folgendes erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) zur Sicherheitsbewertung
- Daten zum Wirkmechanismus (MOA)
- Gezielte Literaturrecherche und Studienrecherche zu autoimmuner Oophoritis und Insulin bzw. Autoimmun-Polyendokrinopathie
- Klärung des aktuellen Zulassungs- und Marktstatus in Deutschland
- Prüfung der Anwendungswege und der Plausibilität einer Wirkung auf die ovarielle Autoimmunität
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

