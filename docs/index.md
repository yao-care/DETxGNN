---
layout: default
title: Vorhersagen zur Arzneimittel-Umwidmung
nav_order: 1
description: "KI-gestützte Vorhersagen zur Arzneimittel-Umwidmung für Deutschland. Evidenzbasierte Analyse zugelassener Arzneimittel auf mögliche neue Anwendungsgebiete."
permalink: /
---

# Vorhersagen zur Arzneimittel-Umwidmung — Deutschland

Dieses Projekt verwendet das TxGNN-Modell (Deep Learning), um potenzielle neue therapeutische Anwendungen für in Deutschland zugelassene Arzneimittel vorherzusagen.

**Haftungsausschluss**: Dieser Inhalt dient ausschließlich Forschungszwecken und stellt keine medizinische Beratung dar. Alle Vorhersagen zur Arzneimittel-Umwidmung erfordern eine klinische Validierung vor der Anwendung.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Deutschland: Umfang dieser Website

Diese Website veröffentlicht Berichte zu **{{ site.data.drug_stats.total_drugs }}** Arzneimitteln aus den Zulassungsdaten von [BfArM](https://www.bfarm.de/) (Deutschland).

Berichte nach Evidenzstufe: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Arzneimittel mit der höchsten Evidenzstufe auf dieser Website

| Arzneimittel | Evidenzstufe |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Grazoprevir](/drugs/grazoprevir/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Oteracil](/drugs/oteracil/) | L1 |
| [Solriamfetol](/drugs/solriamfetol/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |

<!-- local-home:end -->

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care, Unternehmensregisternummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan) entwickelt und betrieben.

DETxGNN ist die Deutschland-Website der Produktlinie „TxGNN Drug Repurposing“ des Unternehmens.
Dasselbe System ist in 30 Ländern und Regionen im Einsatz, jeweils unter dem Namen `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN und so weiter) unter `{cc}txgnn.yao.care`.
Produktübersicht: <https://www.yao.care/medical/txgnn/>.

Das Modell TxGNN selbst wurde vom Zitnik Lab an der Harvard Medical School entwickelt und in
*Nature Medicine* veröffentlicht. Diese Plattform ist das Produktivsystem, das 藥提醒科技有限公司 auf
Basis dieses Modells aufgebaut hat; es umfasst die Integration nationaler Arzneimittelzulassungsdaten,
die Deep-Learning-Vorhersage unter Ausschluss der bereits im Wissensgraphen erfassten Anwendungen, die Evidenzbewertung aus PubMed /
ClinicalTrials sowie die Anbindung an elektronische Patientenakten über SMART on FHIR.
