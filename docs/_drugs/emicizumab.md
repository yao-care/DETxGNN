---
layout: default
title: Emicizumab
parent: Nur Modellvorhersage (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
monitor_inn: "EMICIZUMAB"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
last_modified_at: 2026-11-20
description: "Emicizumab: vorhergesagte neue Indikation Pseudo-von-Willebrand-Krankheit (pseudo-von Willebrand disease) (Evidenzstufe L5). Ursprüngliche Indikation: Hemophilia A"
---

# Emicizumab
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

## Emicizumab: Bispezifischer Antikörper (FVIIIa-Mimetikum) → Pseudo-von-Willebrand-Krankheit (pseudo-von Willebrand disease)
{: .text-alpha }

## Zusammenfassung

Emicizumab ist ein bispezifischer Antikörper, der die Cofaktor-Funktion des aktivierten Faktors VIII nachahmt. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Pseudo-von-Willebrand-Krankheit (pseudo-von Willebrand disease)** voraus, und zwar mit einem Score von 0,9999. Für diese Vorhersage liegen in den zusammengestellten Daten **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf der Modellvorhersage.

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hemophilia A |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Krankheit (pseudo-von Willebrand disease) |
| TxGNN-Vorhersagescore | 0,9999 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage plausibel?

Emicizumab ist ein bispezifischer Antikörper, der den aktivierten Faktor IX und den Faktor X verbindet und damit die Cofaktor-Funktion von FVIIIa im Tenase-Komplex ersetzt. Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Emicizumab (inoffizielle Übersetzung): „HEMLIBRA überbrückt aktivierten Faktor IX und Faktor X und stellt so die Funktion des fehlenden aktivierten Faktors VIII wieder her, der für eine wirksame Hämostase erforderlich ist.“ Englischer Originalwortlaut: "HEMLIBRA bridges activated factor IX and factor X to restore the function of missing activated factor VIII that is needed for effective hemostasis." ([DailyMed: Hemlibra (emicizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2483adba-fab6-4d1b-96c5-c195577ed071), Fassung vom 2025-07-11; abgerufen am 2026-11-19).

Die Pseudo-von-Willebrand-Krankheit ist eine Thrombozytenfunktionsstörung, bei der eine erhöhte Affinität von GPIb-alpha für den von-Willebrand-Faktor vorliegt. Der Defekt liegt also in der Interaktion zwischen Thrombozyten und von-Willebrand-Faktor und nicht im FVIII-abhängigen Tenase-Schritt. Eine klare mechanistische Begründung für den Einsatz von Emicizumab besteht daher nicht. Der hohe Score ist eine rein graphbasierte Modellvorhersage und sollte nicht als Hinweis auf Wirksamkeit gewertet werden.

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004406 | Hemlibra | – | Hämophilie A |

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen** (5 Einträge in den zusammengestellten Daten):
  - **Schwerwiegend (Major):** Anti-Inhibitor-Koagulanzienkomplex (aktivierter Prothrombinkomplex). Die Kombination ist mit Thrombotischen Mikroangiopathien und thromboembolischen Ereignissen assoziiert.
  - **Moderat:** Rekombinanter humaner Antihämophiliefaktor (Faktor VIII) und rekombinanter humaner Gerinnungsfaktor VIIa.
  - Pharmakologische Zielstrukturen: Gerinnungsfaktor IX und Gerinnungsfaktor X (Wirkmechanismus, keine Bewertungsstufe).
- **Hinweis zur vorhergesagten Indikation:** Die Pseudo-von-Willebrand-Krankheit ist keine Thrombotische Mikroangiopathie, jedoch ist Emicizumab als thrombinfördernde Substanz bei Patienten mit Thromboserisiko mit Vorsicht zu bewerten.

Für weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) bitte die Fachinformation heranziehen.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die Pseudo-von-Willebrand-Krankheit gibt es weder klinische Studien noch Publikationen, und der Defekt (Thrombozyten-VWF-Interaktion) wird durch den Wirkmechanismus von Emicizumab nicht adressiert. Der hohe Score allein rechtfertigt keine Weiterverfolgung.

**Für ein Weiterkommen wären erforderlich:**
- Eine belastbare mechanistische Begründung, warum eine Verstärkung der Tenase-Aktivität den GPIb-alpha/VWF-Defekt ausgleichen könnte
- Präklinische Untersuchungen (z. B. Thrombingenerations- oder Blutungsmodelle)
- Detaillierte Daten zum Wirkmechanismus (MOA)
- Auswertung der Fachinformation zu Warnhinweisen und Gegenanzeigen als Grundlage für eine Sicherheitsbewertung

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Hemlibra (emicizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2483adba-fab6-4d1b-96c5-c195577ed071) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

