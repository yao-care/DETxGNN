---
layout: default
title: Alectinib
parent: Nur Modellvorhersage (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alectinib: vorhergesagte neue Indikation Gingivale Fibromatose (Evidenzstufe L5). Ursprüngliche Indikation: Nicht-kleinzelliges Lungenkarzinom (NSCLC)"
monitor_inn: "Alectinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Alectinib
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

## Alectinib: Vom nicht-kleinzelligen Lungenkarzinom zur gingivalen Fibromatose
{: .text-alpha }

## Zusammenfassung in einem Satz

Alectinib ist ein ALK-Inhibitor, der ursprünglich zur Behandlung des nicht-kleinzelligen Lungenkarzinoms (NSCLC) zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **gingivaler Fibromatose** wirksam sein könnte.
Für diese Vorhersage liegen jedoch **keine klinischen Studien und keine Publikationen** vor; sie beruht ausschließlich auf einer graphbasierten Modellvorhersage.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht-kleinzelliges Lungenkarzinom (NSCLC) |
| Vorhergesagte neue Indikation | Gingivale Fibromatose |
| TxGNN-Vorhersagewert | 99,97 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene/widerrufene Zulassung (Cancelled only) |
| Anzahl der Zulassungen | 1 (davon 0 gültig) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus von Alectinib liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist aus den pharmakologischen Daten, dass Alectinib die Rezeptortyrosinkinase **ALK** adressiert (zusätzlich ist in den Daten die Kinase MET als Target aufgeführt). Seine Wirksamkeit beim ALK-positiven NSCLC ist belegt, auch in Zellen, die gegen Crizotinib resistent sind.

Für die hereditäre gingivale Fibromatose ist dagegen **kein ALK-abhängiger Mechanismus** bekannt. Der hohe TxGNN-Wert ist eine reine Vorhersage des Wissensgraphen ohne unterstützende Studien oder Literatur. Eine mechanistische Verbindung zur ursprünglichen Indikation ist derzeit nicht erkennbar.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004164 | Alecensa (Roche Registration GmbH) | – | Nicht-kleinzelliges Lungenkarzinom |

Hinweis: Diese Zulassung ist als erloschen/widerrufen (cancelled) geführt; eine gültige Zulassung besteht laut den Daten nicht.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Klassifikation | Zielgerichtete Therapie (ALK-Tyrosinkinase-Inhibitor), kein klassisches Zytostatikum |
| Myelosuppressionsrisiko | Bitte die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation beachten (in der Literatur wird u. a. hämolytische Anämie als Einzelfallbericht beschrieben) |
| Emetogenität | Bitte die Fachinformation beachten |
| Monitoring | Bitte die Fachinformation beachten |
| Handhabungsschutz | Bitte die Fachinformation beachten |

---

## Sicherheitsaspekte

- **Arzneimittelinteraktionen:** Die Interaktionsabfrage ergab zwei pharmakologische Zielstrukturen (ALK und MET), jedoch keine Wechselwirkungen mit anderen Arzneimitteln mit Schweregradangabe.
- **Weitere Sicherheitssignale aus der Literatur (Einzelfallberichte):** hypertriglyceridämie-induzierte Pankreatitis, hämolytische Anämie, DRESS-Syndrom, Erythema multiforme, Gewichtszunahme.

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf ein Graphmodell (Evidenzlevel L5), ohne klinische Studien, Literatur oder plausiblen ALK-bezogenen Mechanismus. Zudem besteht in Deutschland nur eine erloschene Zulassung.

**Für ein Weiterkommen ist erforderlich:**
- Detaillierte Wirkmechanismusdaten (MOA)
- Fachinformation mit Warnhinweisen und Gegenanzeigen (derzeit fehlend, blockiert die Sicherheitsprüfung)
- Biologische Begründung für eine Rolle von ALK bei der gingivalen Fibromatose sowie präklinische Daten

---

## Weitere Vorhersagen (Kurzüberblick)

Unter den übrigen Vorhersagen ist **Lungen-Keimzelltumor** (Rang 6) die einzige mit einem indirekten Hinweis (Evidenzlevel L4, Einstufung „Forschungsfrage"). Es gibt keine spezifische Evidenz für Keimzelltumoren; Fallberichte zeigen jedoch Ansprechen auf ALK-Inhibitoren bei ALK-rearrangierten Tumoren anderer Histologie (z. B. neuroendokrine Karzinome der Lunge). Die einzige Phase-2-Studie (NCT04644315, ALK-positive solide Tumoren außerhalb der Lunge) wurde mit nur 1 Teilnehmer abgebrochen. Alle übrigen Vorhersagen (Rang 2–5 und 7–10) sind rein modellbasiert oder durch fehlzugeordnete Literatur zum bereits zugelassenen NSCLC gekennzeichnet und gelten als nicht belegt.
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

