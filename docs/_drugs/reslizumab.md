---
layout: default
title: Reslizumab
parent: Nur Modellvorhersage (L5)
nav_order: 395
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Reslizumab: vorhergesagte neue Indikation Thrombozytopenie durch Immunzerstörung (immunvermittelte Thrombozytop… (Evidenzstufe L5). Ursprüngliche Indikation: Asthma"
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
---

# Reslizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

## Reslizumab: Thrombozytopenie durch Immunzerstörung
{: .text-alpha }

## Zusammenfassung

Reslizumab ist ein Anti-IL-5-Antikörper, der ursprünglich zur Behandlung von Asthma zugelassen wurde. Das TxGNN-Modell sagt voraus, dass er bei **immunvermittelter Thrombozytopenie** wirksam sein könnte. Dafür liegen jedoch **keine klinischen Studien** und **keine relevanten Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Asthma |
| Vorhergesagte neue Indikation | Thrombozytopenie durch Immunzerstörung (immunvermittelte Thrombozytopenie) |
| TxGNN-Vorhersagewert | 0,9953 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Reslizumab (inoffizielle Übersetzung): „Reslizumab ist ein Interleukin-5-Antagonist (IgG4, kappa). IL-5 ist das wichtigste Zytokin, das für Wachstum und Differenzierung, Rekrutierung, Aktivierung und Überleben von Eosinophilen verantwortlich ist. Reslizumab bindet mit einer Dissoziationskonstante von 81 pM an IL-5 und hemmt die Bioaktivität von IL-5, indem es dessen Bindung an die Alpha-Kette des auf der Oberfläche der Eosinophilen exprimierten IL-5-Rezeptorkomplexes blockiert.“ Englischer Originalwortlaut: "Reslizumab is an interleukin-5 antagonist (IgG4, kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Reslizumab binds to IL-5 with a dissociation constant of 81 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil surface." ([DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33), Fassung vom 2020-02-29; abgerufen am 2026-11-19). Bekannt ist, dass Reslizumab ein monoklonaler Antikörper gegen Interleukin-5 (IL-5) ist, der die Überlebens- und Aktivierungssignale eosinophiler Granulozyten reduziert. Seine Wirksamkeit bei eosinophilem Asthma ist belegt.

Die immunvermittelte Thrombozytopenie (ITP) wird dagegen hauptsächlich durch autoantikörpervermittelten Abbau von Thrombozyten und eine gestörte Megakaryopoese verursacht. Eine etablierte Rolle von IL-5 oder Eosinophilen ist nicht bekannt. Ein direkter mechanistischer Zusammenhang ist anhand der vorliegenden Daten daher **nicht erkennbar**. Der hohe TxGNN-Wert ist eine rein graphbasierte Vorhersage und sollte nicht als Hinweis auf Wirksamkeit gewertet werden.

Als weitere Vorhersage mit Rang 2 nennt das Modell die „primäre Freisetzungsstörung der Thrombozyten" (Score 0,9925). Auch hier fehlt ein plausibler Bezug zu IL-5, da es sich um intrinsische Thrombozytenfunktionsstörungen handelt.

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Literaturevidenz

Für die Hauptvorhersage (immunvermittelte Thrombozytopenie) ist derzeit keine zugehörige Literatur verfügbar.

Für die zweite Vorhersage (primäre Freisetzungsstörung der Thrombozyten) wurde lediglich eine Publikation zugeordnet, die inhaltlich nicht relevant ist:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Review | Current Medical Research and Opinion | Übersicht zur Behandlung des hypereosinophilen Syndroms, einschließlich Mepolizumab. Stützt den Einsatz von Anti-IL-5 bei eosinophilen Erkrankungen, nicht bei Thrombozytenfunktionsstörungen. |

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003912 | Cinqaero | – | Asthma (Status: gültig) |

## Sicherheitshinweise

Bitte die Packungsbeilage für Sicherheitsinformationen heranziehen.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das TxGNN-Modell (Evidenzstufe L5). Es gibt weder klinische Studien noch relevante Literatur, und ein plausibler mechanistischer Zusammenhang zwischen IL-5-Hemmung und ITP ist nicht erkennbar.

<!-- review:begin de-lic-20261106-reslizumab-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Es gibt weder klinische Studien noch relevante Literatur, und ein plausibler mechanistischer Zusammenhang zwischen IL-5-Hemmung und ITP ist nicht erkennbar. Zudem ist die einzige deutsche bzw. europäische Zulassung erloschen.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-reslizumab-1 -->

**Für ein Weiterverfolgen sind folgende Schritte erforderlich:**
- Detaillierte Wirkmechanismus-Daten (MOA) ergänzen und prüfen, ob ein biologischer Bezug zwischen IL-5/Eosinophilen und Thrombozytopenie besteht
- Systematische Literatur- und Studienrecherche zu Anti-IL-5-Therapien bei ITP
- Sicherheitsinformationen aus der Fachinformation beschaffen (Warnhinweise, Gegenanzeigen)
- Klärung des Zulassungs- und Verfügbarkeitsstatus

<!-- review:begin de-lic-20261106-reslizumab-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Klärung des Zulassungs- und Verfügbarkeitsstatus, da die Zulassung erloschen ist“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-reslizumab-2 -->

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Zudem ist die einzige deutsche bzw. europäische Zulassung erloschen“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „da die Zulassung erloschen ist“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

