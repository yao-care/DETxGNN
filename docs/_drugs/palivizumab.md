---
layout: default
title: Palivizumab
parent: Nur Modellvorhersage (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Palivizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Palivizumab: Von RSV-Prophylaxe zu benignem Zungenneoplasma

## Zusammenfassung in einem Satz

> Palivizumab ist ein humanisierter monoklonaler Antikörper gegen das RSV-F-Glykoprotein und wird zur Vorbeugung von Atemwegsinfektionen durch das Respiratorische Synzytialvirus (RSV) bei gefährdeten Säuglingen verwendet.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam sein könnte für **Benigne Neoplasie der Zunge**,
> aber **keine klinischen Studien** und **keine Literatur** unterstützen derzeit diese Richtung — die mechanistische Begründung des Modells selbst besagt explizit, dass es keine bekannte biologische Verbindung gibt.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht dokumentiert im Evidenzpaket (Datenlücke — DG001/DG002). Basierend auf dem internen Begründungstext ist Palivizumab ein humanisierter monoklonaler Antikörper gegen das RSV-F-Glykoprotein und wird zur RSV-Prophylaxe verwendet. |
| Prognostizierte neue Indikation | Benigne Neoplasie der Zunge |
| TxGNN-Prognosewert | 99.94% |
| Evidenzebene | L5 (nur Modellvorhersage, keine klinischen oder Literaturhinweise) |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfehlenswerte Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage begründet?

Derzeit sind detaillierte Daten zum Wirkungsmechanismus nicht im Evidenzpaket verfügbar (original_moa = Data Gap; DG002). Nach den mechanistischen Anmerkungen, die jedem prognostizierten Einsatzgebiet beigefügt sind, wird Palivizumab konsistent als humanisierter monoklonaler Antikörper beschrieben, der das RSV-F-(Fusions-)Glykoprotein neutralisiert und so den viralen Eintritt in Atemwegsepithelzellen blockiert. Dies ist ein hochspezifischer antiviraler Mechanismus ohne bekannte Rolle bei Zellproliferation, Onkogenese oder Tumorbiologie.

Entscheidend ist, dass die für diesen Kandidaten angegebene Umnutzungsbegründung die Vorhersage **nicht** unterstützt — sie besagt explizit: *"Palivizumab為抗RSV F醣蛋白之人源化單株抗體，僅作用於RSV感染細胞表面抗原，與舌部良性腫瘤之增生／腫瘤生物學機轉無已知關聯。無腫瘤免疫或抗病毒交叉機轉支持此連結。"* (d. h., es gibt keine bekannten Tumor-Immunologie- oder antiviralen Kreuzwirkungsmechanismen, die Palivizumab mit der Biologie von Zungenneoplasien verbinden). Das gleiche Muster gilt für alle 10 bewerteten Vorhersagen für dieses Medikament — jede Begründung verneint unabhängig jede plausible mechanistische Verbindung zur gekoppelten Krankheit (Epiglottisneoplasie, zervikales Neuroblastom, Hodentumor, Schwannom usw.).

Dies ist also ein Fall, in dem ein hoher TxGNN-Ähnlichkeitswert **nicht** durch mechanistische, klinische oder Literaturhinweise korroboriert wird. Die Vorhersage sollte eher als Graph-Ähnlichkeitsartefakt denn als biologisch begründete Umnutzungshypothese behandelt werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktstatus in Deutschland

Palivizumab hat derzeit keine Marktgenehmigungen im überprüften Datensatz (total_licenses = 0; market_status = Not Marketed). Es sind keine Lizenzunterlagen vorhanden, die zusammengefasst werden könnten.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Hinweis: Warnhinweise und Kontraindikationen des TFDA/BfArM-Labels für Palivizumab sind eine **blockierende** Datenlücke — DG001 — und die Sicherheitsüberprüfung kann nicht zur Stufe-1-Bewertung übergehen, bis dies behoben ist.)

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die Vorhersage beruht nur auf einem TxGNN-Ähnlichkeitswert (L5, keine klinischen Studien, keine Literatur), und die beigefügte mechanistische Begründung lehnt jede biologische Plausibilität zwischen dem RSV-neutralisierenden Mechanismus von Palivizumab und der Pathophysiologie von Zungenneoplasien ab. Es gibt keine evidenzgestützte Grundlage, um diesen Kandidaten voranzubringen.

**Um fortzufahren, ist Folgendes erforderlich:**
- Behebung von DG001 (TFDA/BfArM-Label-Warnhinweise und Kontraindikationen) vor jeder Sicherheitsstufen-Bewertung
- Behebung von DG002 (bestätigter Wirkungsmechanismus aus DrugBank), um die mechanistische Verbindung formal zu unterstützen oder auszuschließen
- Unabhängige Bestätigung der ursprünglichen Indikation und Genehmigungsgeschichte (original_indications ist derzeit leer)
- Falls dieser Kandidat weiter verfolgt werden soll, würde eine neue mechanistische Hypothese unabhängig von der aktuellen TxGNN-Begründung erforderlich sein, da die bestehende Begründung gegen die Umnutzung argumentiert

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

