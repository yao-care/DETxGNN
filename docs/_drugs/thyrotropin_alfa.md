---
layout: default
title: Thyrotropin Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 461
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Thyrotropin Alfa: vorhergesagte neue Indikation Migräne (migraine disorder) (Evidenzstufe L5). Ursprüngliche Indikation: Schilddrüsenneoplasien"
monitor_inn: "THYROTROPIN ALFA"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
---

# Thyrotropin Alfa
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

## Thyrotropin alfa: Vom Schilddrüsenkarzinom zur Migräne
{: .text-alpha }

## Zusammenfassung

Thyrotropin alfa ist ein rekombinantes TSH (Thyreoidea-stimulierendes Hormon). Es wurde ursprünglich im Zusammenhang mit Schilddrüsenneoplasien eingesetzt. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Migräne** voraus. Dafür liegen **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Schilddrüsenneoplasien |
| Vorhergesagte neue Indikation | Migräne (migraine disorder) |
| TxGNN-Vorhersagewert | 0,9998 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Thyrotropin alfa ist ein rekombinantes TSH und wirkt am TSH-Rezeptor, vor allem an Schilddrüsenfollikelzellen. Seine Rolle bei Schilddrüsenneoplasien ist etabliert.

Ein mechanistischer Zusammenhang zur Migräne ist nicht belegt. Der sehr hohe Modellwert (0,9998) ist eine reine Vorhersage des TxGNN-Modells (Deep Learning). Ein möglicher Bezug wäre allenfalls indirekt, etwa über schilddrüsenbezogene hormonelle oder vaskuläre Effekte, wofür es keine Hinweise gibt.

Auch die übrigen Vorhersagen unter den Top 10 sind überwiegend nicht plausibel:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 1 | Migräne | 0,9998 | Kein belegter Mechanismus |
| 2 | Migräne mit Hirnstamm-Aura | 0,9998 | Der Wert stammt aus dem TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, kein biologischer Beleg |
| 3 | Raynaud-Krankheit | 0,9996 | Nur Assoziation mit Schilddrüsenautoimmunität, kein Therapieansatz |
| 5 | Atrophoderma vermiculata | 0,9986 | Kein plausibler Mechanismus |
| 6 | Ulerythema ophryogenes | 0,9984 | Kein bekannter Mechanismus |
| 7 | Pulmonale Hypertonie | 0,9984 | Möglicherweise schädlich bei kardiopulmonaler Erkrankung |
| 8 | Kyphoskoliotische Herzerkrankung | 0,9981 | Kein Mechanismus |
| 9 | Posturales orthostatisches Tachykardiesyndrom | 0,9969 | Könnte durch Tachykardie verschlechtern |
| 10 | Hyperthyreose | 0,9965 | Biologisch widersprüchlich, eher kontraindiziert |

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000220 | Thyrogen (Sanofi B.V.) | – | Schilddrüsenneoplasien |

Diese Zulassung ist gültig; es besteht 1 gültige Zulassung von 1.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 45 Wechselwirkungen erfasst. Die aufgeführten Einträge sind durchweg von **mäßigem** Schweregrad und betreffen überwiegend Antidiabetika:
  - Biguanide: Metformin
  - Sulfonylharnstoffe: Chlorpropamid, Glimepirid, Glipizid, Glibenclamid (Glyburide), Acetohexamid
  - SGLT2-Hemmer: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin
  - GLP-1-Rezeptoragonisten: Albiglutid, Dulaglutid, Semaglutid, Exenatid
  - DPP-4-Hemmer: Alogliptin, Saxagliptin
  - Alpha-Glucosidase-Hemmer: Acarbose
  - Insuline: Humaninsulin, Insulin aspart (auch als Protaminform)
- **Hinweise aus den Vorhersagen**: Thyrotropin alfa kann vorübergehend die Schilddrüsenhormone erhöhen und Tachykardie oder Palpitationen auslösen. Bei Hyperthyreose, pulmonaler Hypertonie und POTS ist daher eher mit einer Verschlechterung zu rechnen.

Weitere Sicherheitsinformationen entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das TxGNN-Modell (Deep Learning, Evidenzstufe L5) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, kein biologischer Beleg; es gibt weder Studien noch Publikationen, und ein plausibler Mechanismus fehlt. Die einzige deutsche Zulassung ist gültig.

**Für ein Weiterkommen erforderlich:**
- Daten zum Wirkmechanismus (MOA)
- Warnhinweise und Gegenanzeigen aus der Fachinformation (zugänglich über BfArM), da diese für die Sicherheitsprüfung fehlen
- Eine systematische Literaturrecherche und präklinische Hinweise zu einem möglichen Zusammenhang zwischen TSH-Rezeptor-Signalweg und Migräne
- Klärung der Darreichungswege und der Zulassungssituation, da das Produkt nur injizierbar bekannt ist und die Zulassung erloschen ist
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

