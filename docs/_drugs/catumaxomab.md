---
layout: default
title: Catumaxomab
parent: Nur Modellvorhersage (L5)
nav_order: 104
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
description: "Catumaxomab: vorhergesagte neue Indikation Schwere nicht-proliferative diabetische Retinopathie (Evidenzstufe L5). Ursprüngliche Indikation: Aszites"
monitor_inn: "CATUMAXOMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "drug-induced osteoporosis", "diabetic retinopathy"]
---

# Catumaxomab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Catumaxomab: Schwere nichtproliferative diabetische Retinopathie
{: .text-alpha }

## Zusammenfassung in einem Satz

Catumaxomab ist ein trifunktionaler bispezifischer Antikörper (anti-EpCAM x anti-CD3), der ursprünglich zur Behandlung von malignem Aszites eingesetzt wurde.
Das TxGNN-Modell sagt voraus, dass er bei **schwerer nicht-proliferativer diabetischer Retinopathie** wirksam sein könnte,
jedoch liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor, die diese Vorhersage stützen.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Aszites |
| Vorhergesagte neue Indikation | Schwere nicht-proliferative diabetische Retinopathie |
| TxGNN-Vorhersagewert | 0,9964 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Catumaxomab ein trifunktionaler bispezifischer Antikörper ist, der T-Zellen (über CD3E) und Fc-Rezeptor-tragende Zellen zu EpCAM-exprimierenden Zellen rekrutiert. Seine Wirksamkeit bei malignem Aszites bei EpCAM-positiven Tumoren beruht auf dieser Immunumlenkung.

Ein plausibler biologischer Zusammenhang zur diabetischen Retinopathie ist nicht erkennbar. Deren Pathophysiologie (VEGF-getriebene Gefäßpermeabilität, Perizytenverlust, retinale Ischämie, Entzündung) hat keine erkennbare Verbindung zu einer EpCAM-gerichteten T-Zell-Aktivierung. Der hohe TxGNN-Wert scheint auf einer graphbasierten Nähe im Wissensnetz zu beruhen, nicht auf einer pharmakologischen Begründung. Zudem wäre eine Immunaktivierung mit einem zur Zytokinfreisetzung neigenden Wirkstoff in einem Netzhautkontext sicherheitskritisch.

Weitere vorhergesagte Indikationen sind **medikamenteninduzierte Osteoporose** (Score 0,9958) und **diabetische Retinopathie** (Score 0,9947). Auch hierfür gibt es weder Studien noch Literatur und keinen erkennbaren Mechanismus. Eine T-Zell-Aktivierung mit Zytokinfreisetzung (z. B. TNF-alpha, IL-6) könnte den Knochenabbau theoretisch eher verstärken. Die Vorhersage zur diabetischen Retinopathie ist weitgehend redundant zur spezifischeren Vorhersage der schweren nicht-proliferativen Form.

---

## Evidenz aus klinischen Studien

Derzeit sind keine relevanten klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine relevante Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005697 | Korjuny | – | Aszites |

Diese Zulassung ist als erloschen/zurückgezogen geführt. Hinweis: Die EMA-Zulassung für maligne Aszites bei EpCAM-positiven Tumoren wurde 2017 auf Antrag des Zulassungsinhabers aus kommerziellen Gründen zurückgezogen und Anfang 2025 erneut erteilt.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifikation | Immuntherapie (bispezifischer Antikörper, T-Zell-Engager) |
| Myelosuppressionsrisiko | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Emetogenität | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Überwachungsparameter | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |
| Schutzmaßnahmen beim Umgang | Bitte Warnhinweise und Vorsichtsmaßnahmen in der Fachinformation beachten |

---

## Sicherheitsaspekte

- **Arzneimittelinteraktionen**: Dokumentiert ist lediglich die pharmakologische Zielstruktur CD3E (CD3-epsilon) als primäres molekulares Target; klinisch relevante Wechselwirkungen mit anderen Arzneimitteln sind nicht angegeben.
- Eine Immunaktivierung mit Neigung zur Zytokinfreisetzung wäre bei einer Anwendung am Auge oder systemisch bei Netzhauterkrankungen besonders kritisch zu bewerten.

Für weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzniveau L5) ohne klinische Studien, Literatur oder plausiblen biologischen Mechanismus.

**Für ein Weiterkommen sind folgende Schritte erforderlich:**
- Beschaffung und Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da ohne diese kein Sicherheitsscreening möglich ist
- Vollständige Wirkmechanismus-Daten (MOA), z. B. aus DrugBank
- Präklinische Belege für einen biologischen Zusammenhang mit diabetischer Retinopathie
- Prüfung des aktuellen Zulassungsstatus in Deutschland nach der EMA-Wiederzulassung 2025
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

