---
layout: default
title: Delamanid
parent: Nur Modellvorhersage (L5)
nav_order: 119
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

# Delamanid: Von Tuberkulose (MDR-TB) zu Rindertuberkulose

## Zusammenfassung in einem Satz

> Delamanid ist ein Nitro-Dihydro-Imidazooxazol-Antimykobakterium, öffentlich bekannt als Behandlung für multiresistente Tuberkulose (MDR-TB), obwohl in diesem Evidenzpaket kein formaler Indikationstext vorhanden ist.
> Das TxGNN-Modell sagt voraus, dass es auch wirksam für **Tuberkulose, Rinder (zoonotische *Mycobacterium bovis*-Infektion)** sein könnte,
> aber derzeit unterstützen **keine klinischen Studien** und nur **1 indirekte Publikation** diese spezifische Richtung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Nicht formal in diesem Evidenzpaket angegeben. Delamanid ist öffentlich bekannt als ein Antimykobakterium zur pulmonalen MDR-TB-Behandlung; die Felder `original_indications` und `original_moa` sind leer/Datenlücke in den Quelldaten. |
| Vorhergesagte neue Indikation | Tuberkulose, Rinder |
| TxGNN-Vorhersage-Score | 99,91% |
| Evidenzstufe | L5 (nur Modellvorhersage — keine klinische Studie, und das einzige verfügbare Papier bewertet nicht die Wirksamkeit von Delamanid) |
| Marktstatus in Deutschland | Nicht im Handel |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten sind in diesem Evidenzpaket nicht verfügbar (`original_moa` = Datenlücke). Basierend auf allgemein bekannten Informationen ist Delamanid ein Nitro-Dihydro-Imidazooxazol-Derivat, das als Antimykobakterium entwickelt wurde und klinisch für multiresistente pulmonale Tuberkulose, verursacht durch *Mycobacterium tuberculosis*, verwendet wird.

Die vorhergesagte neue Indikation, „Tuberkulose, Rinder", wird durch *Mycobacterium bovis* verursacht, ein Mitglied des *Mycobacterium tuberculosis*-Komplexes, der eng mit *M. tuberculosis* verwandt ist und ähnliche Arzneistoff-Ziel-Biologie teilt. Dies macht die TxGNN-Vorhersage auf mechanistischer Ebene biologisch plausibel. Es ist jedoch zu beachten, dass dies nicht so sehr eine völlig neue Erkrankung *bereich* ist, sondern eher eine verwandte Pathogen-/Wirt-Variante der bereits etablierten Anti-Tuberkulose-Anwendung des Arzneistoffs — die Vorhersage spiegelt im Wesentlichen bekannte Pharmakologie wider, anstatt eine echte neue therapeutische Richtung zu sein.

---

## Klinische Studienevidenz

Derzeit keine zugehörigen klinischen Studien registriert.

---

## Literaturbeweise

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|----------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Observational / Genomische (WGS) Studie | BMC Genomics | Whole-Genome-Sequencing-Studie, die genetische Vielfalt und Arzneimittelresistenzmuster von *M. bovis*-Isolaten bei zoonotischer TB charakterisiert; bewertet nicht direkt die Wirksamkeit von Delamanid, bietet aber Pathogen-Hintergrund, der für das Behandlungsziel relevant ist. |

---

## Marktstatus in Deutschland

Delamanid hält derzeit **0 Marktgenehmigungen** im Bestand und hat einen Marktstatus von **Nicht im Handel** — keine Genehmigungstabelle zum Anzeigen.

---

## Sicherheitserwägungen

Bitte beachten Sie die Gebrauchsinformation zur Sicherheitsinformation.

*Hinweis: Formale Sicherheitsdaten (Warnhinweise, Kontraindikationen, Arzneimittelwechselwirkungen) sind derzeit in diesem Datensatz nicht verfügbar und werden als **Blocking**-Datenlücke gekennzeichnet (DG001), was eine vollständige S1-Sicherheits-Vorprüfung verhindert.*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die vorhergesagte Indikation wird nur durch den TxGNN-Score und eine nebensächliche Publikation unterstützt, die Delamanids Wirksamkeit nicht testet; keine klinischen Studien befassen sich direkt mit Rinder-/zoonotischer TB mit diesem Arzneistoff. Eine **Blocking**-Sicherheitsdatenlücke (fehlende Gebrauchsinformations-Warnhinweise/Kontraindikationen) verhindert auch eine ordnungsgemäße Sicherheits-Vorprüfung.

**Um fortzufahren, wird Folgendes benötigt:**
- Gebrauchsinformations-/Fachinformationsdaten (Warnhinweise, Kontraindikationen) — DG001
- Bestätigter Wirkmechanismus von DrugBank — DG002
- Direkte Evidenz (in vitro/in vivo oder klinisch), die Delamanid speziell gegen *M. bovis* bewertet
- Klärung der wahren Neuartigkeit: Bewertung, ob „Rindertuberkulose" eine distinkte regulatorische Indikation darstellt oder sich mit Delamanids bereits bestehender MDR-TB-Zulassung überschneidet
- Bestätigung des regulatorischen/Marktstatus, bevor ein Repurposing-Pfad verfolgt wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

