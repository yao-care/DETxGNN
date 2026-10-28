---
layout: default
title: Miconazole
parent: Mittlere Evidenz (L3-L4)
nav_order: 300
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-28
description: "Miconazole: vorhergesagte neue Indikation Akne (Evidenzstufe L3). Ursprüngliche Indikation: Tinea pedis, Tinea corporis, kutane Candidose, Tinea unguium…"
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
---

# Miconazole
{: .fs-9 }

Evidenzniveau: **L3** | Vorhergesagte Indikationen: **1** 
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

## Miconazol: Von Pilzinfektionen der Haut zu Akne
{: .text-alpha }

## Zusammenfassung

Miconazol ist ein Azol-Antimykotikum, das ursprünglich zur Behandlung von Hautpilzinfektionen (u. a. Fußpilz, Candidose der Haut, Pityriasis versicolor) und vulvovaginaler Candidose eingesetzt wird.
Das TxGNN-Modell sagt voraus, dass es auch bei **Akne** wirksam sein könnte.
Dafür liegen **keine registrierten klinischen Studien** und **4 Publikationen** vor, davon nur eine kleine klinische Studie zu Akne im engeren Sinn.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Tinea pedis, Tinea corporis, kutane Candidose, Tinea unguium, Pityriasis versicolor, vulvovaginale Candidose u. a. |
| Vorhergesagte neue Indikation | Akne |
| TxGNN-Vorhersagewert | 0,9954 |
| Evidenzstufe | L3 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Miconazol zur Klasse der Azol-Antimykotika gehört und die fungale CYP51 (Lanosterol-14-alpha-Demethylase) hemmt, wodurch die Ergosterol-Synthese blockiert wird. Diese Einordnung beruht auf der Klassenpharmakologie und nicht auf einem kuratierten Zielstruktur-Eintrag.

Für Akne sind drei Wege denkbar:
1. **Antibakterielle Wirkung:** Azol-Antimykotika zeigten in vitro Aktivität gegen *Propionibacterium (Cutibacterium) acnes*, den Erreger, der mit Akne vulgaris assoziiert ist (PMID 20045949).
2. **Hemmung von Malassezia-Hefen:** Diese verursachen eine Follikulitis, die klinisch Akne ähnelt und häufig mit ihr verwechselt wird (PMID 8593718). Das ist allerdings keine echte Akne vulgaris.
3. **Entzündungshemmende Effekte:** Für Miconazol wurden antientzündliche und hautbarrierebezogene Wirkungen bei entzündlichen Hauterkrankungen beschrieben (PMID 18627330).

Der sehr hohe TxGNN-Wert ist eine rechnerische Vorhersage und gilt nicht als klinischer Beleg.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Übersicht zu den vielfältigen Wirkungen von Miconazol bei Hauterkrankungen |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Klinische Studie (Split-Face, klein) | Skin Res Technol | Bioinstrumentelle Beurteilung bei leichter entzündlicher prämenstrueller (katamenialer) Akne |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Klinische Studie / Therapiestudie | Clin Exp Dermatol | 62 Patienten mit Pityrosporum-Follikulitis, oft als Akne fehldiagnostiziert; keine echte Akne vulgaris |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In-vitro-Studie | Biol Pharm Bull | In-vitro-Aktivität von Azol-Antimykotika gegen *P. acnes*-Isolate von Akne-Patienten |

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/V/C/000140 | Easotic | – | – (Status: gültig) |

---

## Sicherheitsaspekte

- **Kontraindikationen laut Wissensgraphen-Daten** (keine Angabe aus dem Beipackzettel): Lebererkrankung, Gallenblasenerkrankung.
- **Wechselwirkungen (pharmakologische Zielstrukturen):** Miconazol bindet an TRPM2 und TRPV5 und hemmt humane CYP8B1. Eine klinische Einstufung des Schweregrads liegt nicht vor.

Für weitere Sicherheitsinformationen ist die Fachinformation heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Evidenz für Akne beschränkt sich auf In-vitro-Daten, einen Review und eine kleine Split-Face-Studie, ohne registrierte klinische Studien. Zudem ist die einzige deutsche Zulassung erloschen, und Sicherheitsangaben aus der Fachinformation fehlen.

**Für ein Weiterkommen sind erforderlich:**
- Beschaffung und Auswertung der Fachinformation (Warnhinweise, Kontraindikationen) für die Sicherheitsprüfung
- Kuratierte Daten zum Wirkmechanismus (MOA), z. B. aus DrugBank
- Kontrollierte klinische Studien bei Akne vulgaris (abzugrenzen von Malassezia-Follikulitis)
- Prüfung der Darreichungsform und Applikationswege (topisch vs. systemisch) für die Akne-Indikation
- Klärung des aktuellen Zulassungs- und Marktstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

