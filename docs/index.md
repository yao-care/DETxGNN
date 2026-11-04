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

Diese Website veröffentlicht Berichte zu **{{ site.data.drug_stats.total_drugs }}** Arzneimitteln mit zentraler EU-Zulassung aus dem [EMA Medicines Report](https://www.ema.europa.eu/en/medicines/download-medicine-data) (gelten auch in Deutschland).

### Lokale Daten dieser Website

| Punkt | Angabe |
|------|--------|
| Datensatz | EMA Medicines Report (Excel-Datei, zentral zugelassene Arzneimittel) |
| Herausgeber | Europäische Arzneimittel-Agentur (EMA) |
| Download | <https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx> |
| Kennung | EMA-Produktnummer (EMEA/H/C/…) |
| Aktualisierung | Automatischer wöchentlicher Download (jeden Montag); der Status wird aus dem Feld «Medicine status» übernommen (Authorised, Withdrawn, Lapsed, Expired …); eine Nummer, die nicht mehr in der Datei steht, behält ihren bisherigen Status |

Details: [Datenquellen]({{ '/sources/' | relative_url }}).

Berichte nach Evidenzstufe:

| Evidenzstufe | Berichte | Anteil |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

### Arzneimittel mit der höchsten Evidenzstufe auf dieser Website

| Arzneimittel | Evidenzstufe |
|---|---|
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Grazoprevir](/drugs/grazoprevir/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |

<!-- local-home:end -->

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care) entwickelt und betrieben. Den vollständigen
Hintergrund zum Unternehmen und zur Methodik finden Sie auf der Seite <a href="{{ '/about/' | relative_url }}">Über uns</a>.
