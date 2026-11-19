---
layout: default
title: Mepolizumab
parent: Nur Modellvorhersage (L5)
nav_order: 290
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Mepolizumab: vorhergesagte neue Indikation Thrombozytopenie durch Immunzerstörung (Evidenzstufe L5). Ursprüngliche Indikation: Asthma"
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
---

# Mepolizumab
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

## Mepolizumab: Von Asthma zu Thrombozytopenie durch Immunzerstörung
{: .text-alpha }

## Zusammenfassung in einem Satz

Mepolizumab ist ein monoklonaler Anti-IL-5-Antikörper, der ursprünglich zur Behandlung von Asthma zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **Thrombozytopenie durch Immunzerstörung** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und nur **1 Publikation** (ein Fallbericht) vor, sodass die Evidenz sehr schwach ist.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Asthma |
| Vorhergesagte neue Indikation | Thrombozytopenie durch Immunzerstörung |
| TxGNN-Vorhersagewert | 0,9966 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Mepolizumab (inoffizielle Übersetzung): „Mepolizumab ist ein IL-5-Antagonist (IgG1 kappa). IL-5 ist das wichtigste Zytokin, das für Wachstum und Differenzierung, Rekrutierung, Aktivierung und Überleben von Eosinophilen verantwortlich ist. Mepolizumab bindet mit einer Dissoziationskonstante von 100 pM an IL-5 und hemmt die Bioaktivität von IL-5, indem es dessen Bindung an die Alpha-Kette des auf der Oberfläche von Eosinophilen exprimierten IL-5-Rezeptorkomplexes blockiert.“ Englischer Originalwortlaut: "Mepolizumab is an IL-5 antagonist (IgG1 kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Mepolizumab binds to IL-5 with a dissociation constant of 100 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil cell surface." ([DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea), Fassung vom 2025-08-06; abgerufen am 2026-11-19). Bekannt ist, dass Mepolizumab ein Anti-IL-5-Antikörper ist, der Eosinophile reduziert. Seine Wirksamkeit bei eosinophilem Asthma ist belegt, und mechanistisch könnte ein indirekter Bezug zu immunvermittelten Zytopenien bestehen, wenn diese teilweise eosinophilengetrieben sind.

Die einzige unterstützende Literatur ist ein Fallbericht, in dem ein steroidresistentes hypereosinophiles Immunsyndrom unter Mepolizumab (mit Begleittherapie) abklang und sich eine gemischte thrombotische Mikroangiopathie besserte. Daraus lässt sich ein plausibler, aber nur indirekter Zusammenhang ableiten.

Es gibt jedoch keinen Beleg dafür, dass eine IL-5-Blockade die primäre Immunthrombozytopenie (ITP) behandelt. Diese beruht hauptsächlich auf Autoantikörper-vermittelter Plättchenzerstörung und gestörter Megakaryopoese. Der sehr hohe TxGNN-Wert ist eine rechnerische Vorhersage und ersetzt keine klinische Evidenz.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Fallbericht | Blood Cells, Molecules & Diseases | Rückbildung eines steroidresistenten hypereosinophilen Immunsyndroms unter Mepolizumab mit gleichzeitiger Besserung einer gemischten thrombotischen Mikroangiopathie (bei atypischem hämolytisch-urämischem Syndrom) |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003860 | Nucala | – | Asthma |

Diese Zulassung ist gültig; es besteht 1 gültige Zulassung von 1.

---

## Sicherheitsaspekte

Bitte die Fachinformation für Sicherheitsinformationen heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich fast ausschließlich auf einen hohen Modellwert und einen einzelnen indirekten Fallbericht. Es gibt keine klinischen Studien, und ein plausibler Mechanismus für die ITP fehlt. Das Arzneimittel ist in Deutschland laut den Daten im Handel, mit 1 gültigen Zulassung von 1.

**Für ein Weiterkommen sind folgende Punkte erforderlich:**
- Daten zum Wirkmechanismus (MOA), z. B. aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM)
- Präklinische oder mechanistische Studien zur Rolle von IL-5/Eosinophilen bei der ITP
- Klärung des aktuellen Zulassungs- und Marktstatus in Deutschland
- Prüfung der Weiterentwicklung in Studien, falls die Evidenz verbessert werden kann

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

