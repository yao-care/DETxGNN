---
layout: default
title: Tenecteplase
parent: Nur Modellvorhersage (L5)
nav_order: 453
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
description: "Tenecteplase: vorhergesagte neue Indikation Congenital coronary artery anomaly (Evidenzstufe L5). Ursprüngliche Indikation: Myocardial Infarction"
---

# Tenecteplase
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

## Tenecteplase: Congenital coronary artery anomaly
{: .text-alpha }

## Zusammenfassung

Tenecteplase ist ein fibrinspezifischer Gewebeplasminogenaktivator (Thrombolytikum), der ursprünglich zur Behandlung des Myokardinfarkts zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **posterolateralem Myokardinfarkt** wirksam sein könnte. Hierfür liegen jedoch **keine klinischen Studien** und **keine spezifischen Publikationen** vor. Es handelt sich um einen Untertyp der bereits zugelassenen Indikation und nicht um ein echtes Repurposing-Signal.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Myocardial Infarction |
| Vorhergesagte neue Indikation | Congenital coronary artery anomaly |
| TxGNN-Vorhersagewert | 0.9961 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Tenecteplase (inoffizielle Übersetzung): „Tenecteplase ist eine modifizierte Form des humanen Gewebeplasminogenaktivators (tPA), die an Fibrin bindet und Plasminogen in Plasmin umwandelt. In-vitro-Studien zeigen, dass die Tenecteplase-vermittelte Umwandlung von Plasminogen in Plasmin in Gegenwart von Fibrin im Vergleich zur Umwandlung in Abwesenheit von Fibrin erhöht ist.“ Englischer Originalwortlaut: "Tenecteplase is a modified form of human tissue plasminogen activator (tPA) that binds to fibrin and converts plasminogen to plasmin. In the presence of fibrin, in vitro studies demonstrate that tenecteplase-mediated conversion of plasminogen to plasmin is increased relative to its conversion in the absence of fibrin." ([DailyMed: Tnkase (tenecteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e647640d-c395-4b4b-a0be-1162f9c21d84), Fassung vom 2025-12-15; abgerufen am 2026-11-19). Bekannt ist: Tenecteplase ist ein fibrinspezifischer Plasminogenaktivator, der Koronarthromben auflöst. Seine Wirksamkeit beim Myokardinfarkt ist etabliert, und mechanistisch ist er auf thrombotische Koronarverschlüsse übertragbar.

Der posterolaterale Myokardinfarkt ist ein anatomischer Untertyp des bereits zugelassenen Myokardinfarkts. Der hohe TxGNN-Wert spiegelt vor allem die Nähe zur ursprünglichen Indikation wider und stellt kein eigenständiges Repurposing-Signal dar.

Für Krankheiten wie Chromosom-16-Deletion, Beta-Thalassämie, Pyruvatkinase-Mangel oder hereditäre Pyropoikilozytose besteht kein plausibler Mechanismus; diese Werte stammen vom TxGNN-Modell (Deep Learning) und spiegeln möglicherweise gelernte Ähnlichkeiten zwischen verwandten Krankheiten wider, nicht biologische Evidenz. Beim Koronarstenosen-Kandidaten ist die Evidenz auf Stufe L3 klein und heterogen. Hier ist am ehesten eine intrakoronare Anwendung bei PCI oder Stentthrombose denkbar, nicht aber bei fixierter Stenose.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literatur

Für den posterolateralen Myokardinfarkt liegen derzeit keine zugehörigen Publikationen vor.

Zur Einordnung: Für den septalen Myokardinfarkt (Rang 3) und die Koronarstenose (Rang 5) wurden nur indirekte Arbeiten gefunden. Die relevantesten sind:

| PMID | Jahr | Typ | Journal | Kernaussage |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Randomisierte Machbarkeitsstudie (n=40) | Am J Cardiol | Niedrig dosiertes intrakoronares Tenecteplase während primärer PCI bei STEMI: Machbarkeit und Sicherheit (ICE T-TIMI 49) |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | Klinische Studie | J Am Coll Cardiol | CAPITAL AMI: Tenecteplase-gestützte Angioplastie vs. alleinige Thrombolyse bei Hochrisiko-STEMI |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | Kleine klinische Studie | J Am Coll Cardiol | Intrakoronare fibrinspezifische Lyse zur Erleichterung der Rekanalisation chronischer Totalverschlüsse |
| [23975441](https://pubmed.ncbi.nlm.nih.gov/23975441/) | 2014 | Fallserie | J Thromb Thrombolysis | Wirksamkeit und Sicherheit von Tenecteplase bei Lungenembolie (30 Patienten, indirekt) |
| [42220791](https://pubmed.ncbi.nlm.nih.gov/42220791/) | 2026 | Fallbericht | Cureus | Ventrikelseptumruptur trotz früher pharmako-invasiver Reperfusion bei Vorderwand-STEMI (Sicherheitssignal) |

---

## Marktinformationen Deutschland

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/000306 | Metalyse | tenecteplase | Myocardial Infarction | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Hersteller: Boehringer Ingelheim International GmbH.

<!-- review:begin de-lic-20261106-tenecteplase-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Die Zulassung ist erloschen (Status: cancelled). Hersteller: Boehringer Ingelheim International GmbH.“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-tenecteplase-1 -->

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: In den Daten sind 100 Wechselwirkungen erfasst. Wichtige Beispiele:
  - **Schwerwiegend (Major)**: Abciximab, Apixaban, Betrixaban, Acalabrutinib, Avapritinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab. Meist handelt es sich um Substanzen mit erhöhtem Blutungsrisiko.
  - **Moderat**: Acetylsalicylsäure, Ibuprofen, Ketorolac, Celecoxib, Aminocapronsäure, Omega-3-Fettsäuren, Fenfluramin, Dexfenfluramin, Sibutramin.
- **Sicherheitssignal aus der Literatur**: Ein Fallbericht (2026) beschreibt eine mechanische Komplikation (Ventrikelseptumruptur) nach Reperfusion.

Angaben zu Warnhinweisen und Gegenanzeigen aus der Fachinformation liegen nicht vor; bitte die Fachinformation konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der posterolaterale Myokardinfarkt ist ein Untertyp der bereits zugelassenen Indikation. Es gibt weder Studien noch spezifische Literatur, und der hohe Vorhersagewert ist kein echtes Repurposing-Signal. Die Evidenz beschränkt sich auf eine reine Modellvorhersage (L5).

<!-- review:begin de-lic-20261106-tenecteplase-2 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Zudem ist die deutsche Zulassung erloschen. Die Evidenz beschränkt sich auf eine reine Modellvorhersage (L5).“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). Die aktuelle Zahl und der Status der Zulassungen stehen in der Schnellübersicht und in der Tabelle bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-tenecteplase-2 -->

**Für ein Weiterkommen sind erforderlich:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da dies derzeit die Sicherheitsprüfung blockiert
- Daten zum Wirkmechanismus (z. B. aus DrugBank)
- Klärung, ob der Fokus eher auf Kandidaten mit echtem Repurposing-Potenzial liegen sollte, etwa der intrakoronaren Anwendung bei Koronarverschluss durch Thrombus (Evidenzstufe L3), und gezielte Recherche dazu
- Klärung des Zulassungs- und Marktstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Die Zulassung ist erloschen (Status: cancelled)“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-06 | Entfernt: „Zudem ist die deutsche Zulassung erloschen“ | Korrigiert (überarbeitet am 2026-11-24; frühere Fassung im Protokoll erhalten) | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Tnkase (tenecteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e647640d-c395-4b4b-a0be-1162f9c21d84) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

