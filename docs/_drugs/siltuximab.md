---
layout: default
title: Siltuximab
parent: Nur Modellvorhersage (L5)
nav_order: 428
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Siltuximab: vorhergesagte neue Indikation Extrakutanes Mastozytom (Evidenzstufe L5). Ursprüngliche Indikation: Riesenlymphknotenhyperplasie (Giant Lymph Node Hyperplasia)"
monitor_inn: "SILTUXIMAB"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "Kaposi's sarcoma (disease)", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "autosomal dominant familial periodic fever"]
---

# Siltuximab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **8** 
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

## Siltuximab: Extrakutanes Mastozytom
{: .text-alpha }

## Zusammenfassung

Siltuximab ist ein chimärer monoklonaler Antikörper gegen Interleukin-6 (IL-6) und wurde ursprünglich zur Behandlung der Riesenlymphknotenhyperplasie (Castleman-Krankheit) zugelassen.
Das TxGNN-Modell sagt voraus, dass der Wirkstoff bei **extrakutanem Mastozytom** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien und keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Riesenlymphknotenhyperplasie (Giant Lymph Node Hyperplasia) |
| Vorhergesagte neue Indikation | Extrakutanes Mastozytom |
| TxGNN-Vorhersagewert | 0,9964 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Siltuximab ist ein gegen IL-6 gerichteter chimärer monoklonaler Antikörper. Seine Wirksamkeit bei der Castleman-Krankheit, einer IL-6-getriebenen lymphoproliferativen Erkrankung, ist belegt.

Die Verbindung zum Mastozytom stützt sich ausschließlich auf die Vorhersage des TxGNN-Modells (Deep Learning, Score 0,9964). Dieser Score kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, und stellt keinen biologischen Beleg dar. Weder klinische Studien noch Literatur belegen eine IL-6-Blockade bei dieser Erkrankung, und die mechanistische Begründung ist nicht etabliert. Der Zusammenhang zur ursprünglichen Indikation wurde bisher nicht bewertet.

### Weitere vorhergesagte Indikationen

| Rang | Erkrankung | Score | Evidenzgrad | Einschätzung |
|------|------|------|------|------|
| 2 | Leberinfarkt | 0,9944 | L5 | IL-6 hat hepatoprotektive Funktionen; eine Blockade könnte schädlich sein. |
| 3 | Hepatische venookklusive Erkrankung | 0,9940 | L5 | Plausible, aber nicht validierte Hypothese (Endothelschaden, Zytokine nach Stammzelltransplantation). |
| 4 | Peliosis hepatis | 0,9929 | L5 | Kein direkter mechanistischer oder klinischer Beleg. |
| 5 | Kaposi-Sarkom | 0,9928 | L5 | Biologisch plausibler indirekter Link über KSHV/HHV-8 und virales sowie humanes IL-6. |
| 6 | Familiäres Mittelmeerfieber (autosomal-rezessiv) | 0,9922 | L5 | Haupttreiber ist IL-1; IL-1-Blockade und Colchicin sind Standard. |
| 7 | Aggressive systemische Mastozytose | 0,9916 | L5 | KIT-getrieben; IL-6 ist eher Biomarker als Therapieziel. |
| 8 | Autosomal-dominantes familiäres periodisches Fieber | 0,9905 | L5 | IL-1-Blockade ist Standard; kein direkter Beleg für Siltuximab. |

---

## Literaturevidenz

Für die Hauptindikation (extrakutanes Mastozytom) liegt derzeit keine relevante Literatur vor.

Für die Alternativindikation Kaposi-Sarkom wurde eine Publikation gefunden:

| PMID | Jahr | Typ | Journal | Zentrale Aussage |
|------|-----|------|------|---------|
| [39970477](https://pubmed.ncbi.nlm.nih.gov/39970477/) | 2024 | Review | AIDS Reviews | Übersicht zu den Ursachen der Castleman-Krankheit (u. a. virale Infektionen) und ihren Subtypen; keine Wirksamkeitsstudie zum Kaposi-Sarkom. |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003708 | Sylvant (Recordati Netherlands B.V.) | – | Riesenlymphknotenhyperplasie |

Die Zulassung ist aufgehoben (Status: cancelled).

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Beispiele aus der Auswertung:

- **Schwerwiegend (Major):** Deferipron
- **Mäßig (Moderate):** Simvastatin, Apixaban, Warfarin, Rivaroxaban, Dicoumarol, Lidocain, Hydrocodon, Theophyllin, Roflumilast, Aminophyllin, Oxtriphyllin, Tacrolimus, Fentanyl, Nifedipin, Tetanus-Toxoid-Impfstoff
- **Gering (Minor):** Zinksalze (Sulfat, Acetat, Gluconat, Chlorid)

Viele dieser Wechselwirkungen betreffen Substrate von Cytochrom-P450-Enzymen. IL-6-Blockade kann die Enzymaktivität normalisieren, daher ist bei Wirkstoffen mit enger therapeutischer Breite (z. B. Warfarin, Theophyllin, Tacrolimus) eine Überwachung sinnvoll.

Angaben zu Warnhinweisen und Gegenanzeigen aus der Fachinformation liegen nicht vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für extrakutanes Mastozytom beruht ausschließlich auf dem Modell (L5), ohne klinische Studien oder Literatur. Mastzellerkrankungen sind primär KIT-getrieben, und IL-6 gilt dort eher als Biomarker. Zudem ist die deutsche Zulassung aufgehoben.

**Für ein Weiterkommen erforderlich:**
- Mechanismusdaten (MOA) aus DrugBank ergänzen
- Warnhinweise und Gegenanzeigen aus der Fachinformation einholen (derzeit blockierende Datenlücke für die Sicherheitsprüfung)
- Präklinische Daten zu IL-6 bei Mastzellerkrankungen prüfen
- Das Kaposi-Sarkom (L4, plausibler KSHV/IL-6-Link) als aussichtsreichere Forschungsfrage vertiefen
- Klärung des Zulassungs- und Versorgungsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

