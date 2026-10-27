---
layout: default
title: Ezetimibe
parent: Hohe Evidenz (L1-L2)
nav_order: 189
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-14
description: "Ezetimibe: vorhergesagte neue Indikation Hyperlipoproteinämie (Evidenzstufe L1). Ursprüngliche Indikation: Hypercholesterinämie"
monitor_inn: "EZETIMIBE"
predicted_indications: ["hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **4** 
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

## Ezetimib: Von Hypercholesterinämie/Dyslipidämie zu Hyperlipoproteinämie
{: .text-alpha }

## Zusammenfassung

Ezetimib ist ein Hemmstoff der intestinalen Cholesterinaufnahme und wurde ursprünglich zur Behandlung von Hypercholesterinämie und Dyslipidämie eingesetzt.
Das TxGNN-Modell sagt eine Wirksamkeit bei **Hyperlipoproteinämie** voraus, was der bestehenden Indikation sehr nahekommt (bestätigend statt neuartig).
Die Datenlage ist mit **40 klinischen Studien** und **18 Publikationen** für diese Vorhersage umfangreich.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hypercholesterinämie; Dyslipidämie |
| Vorhergesagte neue Indikation | Hyperlipoproteinämie |
| TxGNN-Vorhersagewert | 99,63 % |
| Evidenzgrad | L1 |
| Marktstatus in Deutschland | Nur erloschene Zulassung (Cancelled only) |
| Anzahl der Zulassungen | 1 (davon 0 gültig) |
| Empfohlene Entscheidung | Proceed with Guardrails |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben aus der Arzneimitteldatenbank vor. Nach der vorliegenden Begründung hemmt Ezetimib den NPC1L1-vermittelten Cholesterintransport im Darm und senkt dadurch LDL-Cholesterin und Apolipoprotein B.

Die vorhergesagte Indikation Hyperlipoproteinämie überschneidet sich weitgehend mit der ursprünglichen Indikation (Hypercholesterinämie/Dyslipidämie). Es handelt sich daher eher um eine Bestätigung der bekannten Anwendung als um ein echtes Repurposing.

Weitere Vorhersagen des Modells:
- **Familiäre Hypercholesterinämie** (Wert 99,38 %, L1, Proceed with Guardrails): Ezetimib senkt als Add-on zu Statinen zusätzlich das LDL-C, wenn die LDL-Rezeptorfunktion gestört ist. Leitlinien empfehlen diese Kombination. Bei homozygoter FH ist das Ansprechen wegen des rezeptornegativen Status begrenzt; Langzeitdaten bei Kindern sollten geprüft werden.
- **Hypercholesterinämie durch Cholesterin-7α-Hydroxylase-Mangel** (99,25 %, L5, Hold): mechanistisch plausibel, aber nur eine präklinische Arbeit und keine klinische Evidenz bei dieser sehr seltenen Erkrankung.
- **Cholesterinester-Transferprotein-Mangel** (99,09 %, L5, Hold): Dieser Zustand erhöht das HDL-C und erfordert in der Regel keine LDL-Senkung. Der hohe Wert spiegelt wahrscheinlich Netzwerknähe statt klinischer Begründung wider.

---

## Klinische Evidenz

Die folgende Auswahl zeigt die relevantesten Studien (Bewertung A/B) für die Hauptvorhersage.

| Studiennummer | Phase | Status | Teilnehmer | Kernaussagen |
|---------|------|------|------|---------|
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Abgeschlossen | 511 | Evolocumab vs. Ezetimib bei statinintoleranten Patienten mit Hypercholesterinämie (LDL-C nach 24 Wochen) |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Abgeschlossen | 40 | Ezetimib allein vs. Statin bei Hypercholesterinämie; Wirkung auf LDL-C |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | Abgeschlossen | 127 | Ezetimib/Rosuvastatin plus Candesartan/Amlodipin bei Hypertonie und Hyperlipidämie |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Beendet (terminated) | 49 | Offene Anwendungsstudie mit Ezetimib 10 mg/Tag bei homozygoter FH oder Sitosterolämie |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | Beobachtungsstudie | Abgeschlossen | 1.794 | 52-Wochen-Langzeitanwendung von Zetia in Japan (Sicherheit und Wirksamkeit) |
| [NCT02942602](https://clinicaltrials.gov/study/NCT02942602) | Nicht zutreffend | Abgeschlossen | 58 | Wirkung lipidsenkender Medikamente auf die HDL-Funktion |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Abgeschlossen | 1.220 | Ezetimib/Simvastatin plus Niacin bei Hyperlipidämie Typ IIa/IIb |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Abgeschlossen | 576 | Fenofibrat plus Ezetimib bei gemischter Hyperlipidämie |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Abgeschlossen | 611 | Ezetimib/Simvastatin plus Fenofibrat bei gemischter Hyperlipidämie |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Abgeschlossen | 407 | Obicetrapib/Ezetimib-Fixkombination bei HeFH und/oder ASCVD |

Für die familiäre Hypercholesterinämie liegen zusätzlich Phase-3-Studien vor, darunter [NCT00867165](https://clinicaltrials.gov/study/NCT00867165) (placebokontrolliert, 138 Kinder von 6 bis 10 Jahren), [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) (homozygote FH, 50 Teilnehmer) und [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) (Langzeitsicherheit, 44 Teilnehmer).

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT (Phase 3) | Lancet | TANDEM: Fixkombination Obicetrapib/Ezetimib zur LDL-C-Senkung |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Orales PCSK9-Inhibitor Enlicitide bei heterozygoter FH |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: Evolocumab bei HeFH trotz intensiver Statintherapie ± Ezetimib |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5: Inclisiran bei homozygoter FH |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Kohortenstudie | Lancet | Weltweite Erfahrungen bei homozygoter FH |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Fortschritte bei Medikamenten gegen Hyperlipidämie |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | Neue Therapien zur Senkung von LDL-C und ApoB; Ezetimib als Basis neben Statinen |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug Ther Bull | Ezetimib-Update: senkt LDL-C allein oder mit Statin |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nat Rev Dis Primers | Familiäre Hypercholesterinämie: Ursachen und Management |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Konsensus-Statement | Eur Heart J | FH ist unterdiagnostiziert und untertherapiert; Leitfaden für Kliniker |

Die meisten dieser Arbeiten befassen sich mit anderen Wirkstoffen (z. B. PCSK9-Hemmern), bei denen Ezetimib Hintergrund- oder Vergleichstherapie ist. Direkte Ezetimib-Evidenz liefern v. a. die Studien zur Kombination.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004959 | Nustendi (Daiichi Sankyo Europe GmbH) | – | Hypercholesterinämie; Dyslipidämie |

Die einzige erfasste Zulassung ist erloschen (Status: cancelled). Eine gültige Zulassung besteht laut den zusammengestellten Daten derzeit nicht.

---

## Sicherheitsaspekte

**Kontraindikationen/Risikoerkrankungen (aus dem Wissensgraphen, nicht aus Fachinformation):** Pankreatitis, Lebererkrankung, Gallenblasenerkrankung, Myopathie, Muskelerkrankungen, Skelettmuskelerkrankung, familiäre periodische Paralyse, Substanzmissbrauch/-abhängigkeit, Rhabdomyolyse und noduläre Fasziitis. Diese Angaben stammen aus Beziehungen im Wissensgraphen und müssen mit der Fachinformation abgeglichen werden.

**Arzneimittelwechselwirkungen:** Insgesamt wurden 100 Wechselwirkungen erfasst. Als moderat eingestuft sind:
- Chenodesoxycholsäure
- Eluxadolin
- Rosuvastatin
- Simvastatin

Weitere (Schweregrad unbekannt) u. a.: Calcitriol, Pantoprazol, Glimepirid, Mesalazin, Doxycyclin, Clotrimazol, Acarbose, Morphin, Metformin, Omeprazol.

Für weitere Sicherheitsinformationen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Proceed with Guardrails**

**Begründung:**
Für Hyperlipoproteinämie und familiäre Hypercholesterinämie liegen mehrere abgeschlossene Phase-3-Studien vor (Evidenzgrad L1). Da die Vorhersage der bestehenden Indikation entspricht, ist sie bestätigend. Die beiden seltenen Vorhersagen (CYP7A1- und CETP-Mangel) sind nur durch das Modell gestützt (L5) und sollten zurückgestellt werden (Hold).

**Für das weitere Vorgehen sind erforderlich:**
- Fachinformation (Warnhinweise, Kontraindikationen) aus dem BfArM beschaffen; diese Daten fehlen bislang und blockieren die Sicherheitsprüfung
- Detaillierte Wirkmechanismus-Daten aus der Arzneimitteldatenbank ergänzen
- Klärung des Marktstatus in Deutschland, da die einzige erfasste Zulassung erloschen ist
- Prüfung der Wechselwirkungen mit Statinen (Rosuvastatin, Simvastatin) und Gallensäure-bezogenen Wirkstoffen
- Bei FH: Langzeitdaten bei Kindern prüfen und das eingeschränkte Ansprechen bei homozygoter FH berücksichtigen
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

