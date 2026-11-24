---
layout: default
title: Insulin Glargine
parent: Nur Modellvorhersage (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Insulin Glargine: vorhergesagte neue Indikation Autoimmune Oophoritis (Evidenzstufe L5). Ursprüngliche Indikation: Diabetes mellitus"
monitor_inn: "INSULIN GLARGINE"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
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

## Insulin glargine: Von Diabetes mellitus zu autoimmune Oophoritis
{: .text-alpha }

## Zusammenfassung in einem Satz

Insulin glargine ist ein lang wirksames Basalinsulin-Analogon, das ursprünglich zur Behandlung von **Diabetes mellitus** (einschließlich Typ 2) zugelassen wurde. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **autoimmuner Oophoritis** voraus, doch dafür liegen **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht ausschließlich auf einer Modellberechnung.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Diabetes mellitus |
| Vorhergesagte neue Indikation | Autoimmune Oophoritis |
| TxGNN-Vorhersagewert | 0,9988 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 6 von 6) |
| Anzahl der Zulassungen | 6 (gültig: 6) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Insulin Glargine (inoffizielle Übersetzung): „Die primäre Wirkung von Insulin, einschließlich Insulin-glargin-Präparaten, ist die Regulation des Glucosestoffwechsels. Insulin und seine Analoga senken den Blutzucker, indem sie die periphere Glucoseaufnahme, insbesondere durch Skelettmuskulatur und Fettgewebe, stimulieren und die hepatische Glucoseproduktion hemmen.“ Englischer Originalwortlaut: "The primary activity of insulin, including insulin glargine products, is regulation of glucose metabolism. Insulin and its analogs lower blood glucose by stimulating peripheral glucose uptake, especially by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Langlara (insulin glargine-aldy) prescribing information, Lanexa Biologics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5328761e-59d3-ca7a-e063-6394a90ae810), Fassung vom 2026-10-15; abgerufen am 2026-11-19). Bekannt ist: Insulin glargine ist ein lang wirksames Basalinsulin-Analogon, das am Insulinrezeptor wirkt und die Blutzuckerkontrolle bei Diabetes verbessert.

Die autoimmune Oophoritis ist eine immunvermittelte Erkrankung der Eierstöcke. Für Insulin glargine ist keine Rolle bei der Modulation dieses Autoimmunprozesses bekannt. Ein mechanistischer Zusammenhang ist nicht belegt. Wahrscheinlich spiegelt die Vorhersage lediglich das gemeinsame Auftreten mit autoimmunen polyendokrinen Syndromen (z. B. Typ-1-Diabetes) wider und keinen therapeutischen Effekt.

Auch die übrigen Vorhersagen unter den zehn bestbewerteten Kandidaten sind überwiegend rein rechnerisch:

- **Stiff-Person-Syndrom (klassisch und fokal):** Zusammenhang über gemeinsame Autoimmunität (Anti-GAD65) und Komorbidität mit Typ-1-Diabetes, kein plausibler Behandlungseffekt. Identische Scores stammen vom TxGNN-Modell (Deep Learning) und können vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen widerspiegeln, keine biologische Evidenz.
- **Thiamin-responsives Dysfunktionssyndrom:** Insulin könnte die diabetische Komponente symptomatisch behandeln, jedoch ohne krankheitsmodifizierende Wirkung.
- **Opsismodysplasie:** Spekulative Verbindung über INPPL1 (SHIP2) als negativen Regulator der Insulin-/PI3K-Signalwege, ohne Belege.
- **Pankreasagenesie:** Insulinersatz ist mechanistisch schlüssig, entspricht aber der bestehenden Diabetes-Indikation und ist kein echtes Repurposing.
- **Lipodystrophien und Lipoatrophie (lokalisiert, zentrifugal, druckinduziert, idiopathisch):** Lokale Lipodystrophie ist eine bekannte Nebenwirkung wiederholter Insulininjektionen. Insulin glargine ist hier eher Ursache als Therapie. Diese Vorhersagen sind vermutlich Artefakte und als mögliches Sicherheitssignal zu werten.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Für die Top-Vorhersage (autoimmune Oophoritis) liegt keine Literatur vor.

Für den Kandidaten auf Rang 6 (Pankreasagenesie, Evidenzlevel L4) wurden indirekte Publikationen gefunden. Keine davon ist eine Studie bei Pankreasagenesie:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Übersicht zur zunehmenden Insulintherapie bei Typ-2-Diabetes und zur praktischen Einleitung |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Sekundärer Diabetes bei endokrinen Grunderkrankungen (z. B. Akromegalie, Cushing-Syndrom) |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Fallbericht | Medicine | MODY 5 (monogener Diabetes mit Pankreasdysfunktion), behandelt mit GLP-1-Rezeptoragonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Kohorte (veterinärmedizinisch) | J Vet Intern Med | Pankreasenzyme und Ultraschallbefunde bei diabetischen Katzen |

---

## Marktinformationen Deutschland

Laut EMA-Daten (Stand 2026-11-09) waren alle Zulassungen gültig; den aktuellen Status zeigt die Tabelle bei den Marktinformationen. Es handelt sich um zentrale EU-Zulassungen (EMA-Nummern):

<!-- review:begin de-lic-20261106-insulin_glargine-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Eine sechste Zulassung (Suliqua, EMEA/H/C/004243, Diabetes mellitus Typ 2) ist ebenfalls erloschen.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-insulin_glargine-2 -->

<!-- review:begin de-lic-20261112-insulin_glargine-1 -->

> **Prüfkorrektur (2026-11-12)**: Ursprünglich stand hier: „Fünf der sechs Zulassungen sind gültig.“ Laut den EMA-Daten (Stand 2026-11-09) waren alle erfassten Zulassungen gültig („Authorised“), auch Suliqua (EMEA/H/C/004243); Zahl und aktueller Status stehen in der Schnellübersicht und in der Tabelle. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261112-insulin_glargine-1 -->

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000284 | Lantus | insulin glargine | Diabetes Mellitus | Gültig |
| EMEA/H/C/000309 | Toujeo (previously Optisulin) | insulin glargine | Diabetes Mellitus | Gültig |
| EMEA/H/C/002835 | Abasaglar (previously Abasria) | insulin glargine | Diabetes Mellitus | Gültig |
| EMEA/H/C/004243 | Suliqua | insulin glargine; lixisenatide | Diabetes Mellitus, Type 2 | Gültig |
| EMEA/H/C/004280 | Semglee | insulin glargine | Diabetes Mellitus | Gültig |
| EMEA/H/C/006136 | Ondibta | insulin glargine | Diabetes Mellitus | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Die meisten sind von mittlerem Schweregrad. Beispiele:
  - Sympathomimetika/Bronchodilatatoren: Phenylephrin, Epinephrin, Pseudoephedrin, Salbutamol, Formoterol
  - Betablocker: Acebutolol
  - Andere Antidiabetika: Metformin, Pioglitazon, Alogliptin, Albiglutid
  - Weitere: Hydrochlorothiazid, Acetazolamid, Doxycyclin, Ethinylestradiol, Estradiol, Hydrocortison, Alpelisib, Ethanol
  - Geringfügig: topische Kortikosteroide (z. B. Hydrocortison topisch, Alclometason topisch)
- **Sicherheitssignal:** Lokale Lipodystrophie/Lipoatrophie an Injektionsstellen ist eine bekannte Nebenwirkung von Insulin. Mehrere der vorhergesagten Indikationen betreffen genau dieses Krankheitsbild.

Weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die Vorhersage autoimmune Oophoritis gibt es keine klinischen Studien, keine Literatur und keinen plausiblen mechanistischen Zusammenhang (Evidenzlevel L5). Der Score stammt vom TxGNN-Modell (Deep Learning) und kann vom Modell gelernte Ähnlichkeiten zwischen verwandten Erkrankungen (gemeinsame Autoimmun- und Diabetes-Komorbidität) widerspiegeln, keine biologische Evidenz. Das Arzneimittel ist in Deutschland/EU im Handel.

<!-- review:begin de-lic-20261106-insulin_glargine-3 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Das Arzneimittel ist in Deutschland/EU im Handel, 5 von 6 Zulassungen sind gültig.“ Entfernt: Die angegebene Zahl oder der Status der Zulassungen stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-insulin_glargine-3 -->

**Für ein Weiterkommen sind erforderlich:**
- Beschaffung und Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da dieser Datenpunkt derzeit eine blockierende Lücke für die Sicherheitsprüfung darstellt
- Detaillierte Wirkmechanismus-Daten (MOA), z. B. aus DrugBank
- Gezielte Literaturrecherche zur autoimmunen Oophoritis und zu Autoimmun-Komorbiditäten
- Falls weiterverfolgt, wäre allenfalls die Pankreasagenesie (L4) als Forschungsfrage relevant, wobei es sich um Insulinersatz im Rahmen der bestehenden Diabetes-Indikation und nicht um echtes Repurposing handelt

<!-- review:begin de-lic-20261031-insulin_glargine-1 -->

> **Prüfkorrektur (2026-10-31)**: Ursprünglich stand hier: „Klärung des Zulassungs- und Marktstatus in Deutschland (aktuell nur erloschene Zulassungen) / Gezielte Literaturrecherche zur autoimmunen Oophoritis und zu Autoimmun-Komorbiditäten“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-10-31). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261031-insulin_glargine-1 -->

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-10-31 | Entfernt: „Klärung des Zulassungs- und Marktstatus in Deutschland (aktuell nur erloschene Zulassungen)“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „Eine sechste Zulassung (Suliqua, EMEA/H/C/004243, Diabetes mellitus Typ 2) ist ebenfalls erloschen“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „5 von 6 Zulassungen sind gültig“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-12 | Zahl der gültigen Zulassungen: 5 von 6 → alle 6 | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Langlara (insulin glargine-aldy) prescribing information, Lanexa Biologics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5328761e-59d3-ca7a-e063-6394a90ae810) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

