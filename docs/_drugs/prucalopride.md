---
layout: default
title: Prucalopride
parent: Nur Modellvorhersage (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Prucalopride: vorhergesagte neue Indikation Hypoalphalipoproteinämie (Evidenzstufe L5). Ursprüngliche Indikation: Obstipation"
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
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

## Prucalopride: Von Obstipation zu Hypoalphalipoproteinämie
{: .text-alpha }

## Zusammenfassung

Prucalopride ist ein selektiver 5-HT4-Rezeptoragonist, der ursprünglich zur Behandlung der Obstipation (chronische Verstopfung) eingesetzt wird.
Das TxGNN-Modell sagt für den Wirkstoff unter anderem **Hypoalphalipoproteinämie** voraus (höchster Rang). Dafür liegen jedoch **keine klinischen Studien und keine Publikationen** vor, die diese Richtung stützen.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Obstipation |
| Vorhergesagte neue Indikation | Hypoalphalipoproteinämie |
| TxGNN-Vorhersagewert | 0,9982 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage (nicht) plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Prucalopride wirkt als Agonist am 5-HT4-Rezeptor (Gen HTR4) und fördert die Motilität des Magen-Darm-Trakts. Es ist für Erwachsene mit chronischer Obstipation zugelassen, bei denen Abführmittel nicht ausreichend wirken.

Für Hypoalphalipoproteinämie, eine Störung des HDL-Stoffwechsels, besteht nach der Analyse **kein erkennbarer mechanistischer Zusammenhang**. Der hohe TxGNN-Wert scheint eine reine Vorhersage des TxGNN-Modells (Deep Learning) zu sein, ohne unterstützende Studien oder Literatur.

Auch die weiteren Vorhersagen sind überwiegend nicht plausibel (u. a. homozygote familiäre Hypercholesterinämie, orale Candidiasis, Strongyloidiasis, HIV). Eine Ausnahme bilden die **Amyloidose** und die **primäre Amyloidose**: Hier könnte ein Prokinetikum gastrointestinale Dysmotilität (z. B. chronische intestinale Pseudoobstruktion) symptomatisch lindern. Die Grunderkrankung würde dadurch nicht beeinflusst. Diese Indikationen sind als Forschungsfrage (L4) einzustufen.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Für die Top-Vorhersage (Hypoalphalipoproteinämie) liegt derzeit keine zugehörige Literatur vor.

Für die Amyloidose-Vorhersagen (Rang 6 und 9) wurden folgende Arbeiten gefunden, die jedoch **keine Wirksamkeit von Prucalopride belegen**:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Fallbericht | Cureus | Amyloidose, die sich als chronische intestinale Pseudoobstruktion präsentiert (61-jähriger Patient, mehrere erfolglose Laparotomien) |
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Kohortenstudie | Turk J Gastroenterol | Spezifische gastrointestinale Motilitätsstörungen (Gastroparese, CIPO, Kolonträgheit) werden im Frühstadium häufig als funktionelle GI-Störungen fehldiagnostiziert |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/001012 | Resolor | – | Obstipation |

Diese Zulassung ist gültig. In Deutschland ist das Arzneimittel derzeit im Handel (1 von 1 Zulassungen gültig).

---

## Sicherheitshinweise

- **Kontraindikationen aus dem Wissensgraphen** (keine Packungsbeilage-Daten): Colitis ulcerosa, chronisch-entzündliche Darmerkrankung, Darmperforation.
- **Wechselwirkungen**: Es wurde nur die pharmakologische Zielstruktur (5-HT4-Rezeptor) erfasst, keine konkreten Arzneimittelwechselwirkungen.

Für weitere Sicherheitsinformationen ist die Packungsbeilage heranzuziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für die Top-Vorhersage Hypoalphalipoproteinämie gibt es weder einen mechanistischen Zusammenhang noch Studien oder Literatur (Evidenzstufe L5). Zudem ist das Arzneimittel in Deutschland derzeit im Handel (1 von 1 Zulassungen gültig). Lediglich die Amyloidose-bezogene gastrointestinale Dysmotilität wäre als symptomatische Forschungsfrage (L4) weiterverfolgbar.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Daten zum Wirkmechanismus (MOA) ergänzen, z. B. über DrugBank
- Warnhinweise und Gegenanzeigen aus der Packungsbeilage (BfArM) beschaffen und prüfen
- Für die Amyloidose-assoziierte Dysmotilität: gezielte Literaturrecherche und ggf. Pilotstudie zur symptomatischen Wirksamkeit
- Klärung des Zulassungsstatus in Deutschland (erloschene Zulassung)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

