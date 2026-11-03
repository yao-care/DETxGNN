---
layout: default
title: Datenquellen
nav_order: 93
permalink: /sources/
description: "Die Datenquellen hinter DETxGNN: zentrale EU-Zulassungen der EMA, TxGNN, ClinicalTrials.gov, PubMed und DrugBank."
---

# Datenquellen

<div class="key-takeaway">
Jede Schlussfolgerung lässt sich auf eine öffentliche Datenquelle zurückführen — nichts ist eine Blackbox.
</div>

---

## Übersicht der Quellen

<table class="comparison-table">
<thead>
<tr><th>Art</th><th>Quelle</th><th>Verwendet für</th></tr>
</thead>
<tbody>
<tr><td>Zulassungsdaten</td><td><a href="https://www.ema.europa.eu/en/medicines/download-medicine-data">EMA Medicines Report</a></td><td>Zentral zugelassene EU-Arzneimittel (gelten auch in Deutschland), ihre Wirkstoffe und ihr Zulassungsstatus</td></tr>
<tr><td>Vorhersagemodell</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Vorhersage von Zusammenhängen zwischen Arzneimitteln und Krankheiten</td></tr>
<tr><td>Klinische Studien</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidenzeinstufung (NCT)</td></tr>
<tr><td>Literatur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidenzeinstufung (PMID)</td></tr>
<tr><td>Arzneimittelinformationen</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Wirkstoffabbildung und Daten zu Zielstrukturen</td></tr>
<tr><td>Wechselwirkungen</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Daten zu Arzneimittelwechselwirkungen</td></tr>
</tbody>
</table>

---

## Lokale Daten dieser Website

Die Arzneimittel und ihr Zulassungsstatus stammen aus dem Medicines Report der Europäischen
Arzneimittel-Agentur (EMA). Er enthält die **zentralen EU-Zulassungen**, die in allen EU/EWR-Staaten und
damit auch in Deutschland gelten. Nationale Zulassungen des BfArM sind in diesen Daten nicht enthalten.

| Punkt | Angabe |
|------|--------|
| Datensatz | EMA Medicines Report (Excel-Datei, zentral zugelassene Arzneimittel) |
| Herausgeber | Europäische Arzneimittel-Agentur (EMA) |
| Download | <https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx> |
| Kennung | EMA-Produktnummer (EMEA/H/C/…) |
| Aktualisierung | Automatischer wöchentlicher Download (jeden Montag); der Status wird aus dem Feld «Medicine status» übernommen (Authorised, Withdrawn, Lapsed, Expired …); eine Nummer, die nicht mehr in der Datei steht, behält ihren bisherigen Status |

---

## Lizenzen

Jede Quelle hat ihre eigene Lizenz — bitte prüfen Sie diese vor dem Zitieren:

- **TxGNN**: akademische Nutzung; Huang et al. (2024) zitieren
- **ClinicalTrials.gov / PubMed**: öffentliche Daten der US-amerikanischen NIH
- **DrugBank**: nicht-kommerzielle Nutzung nach Maßgabe der Lizenzbedingungen
- **EMA**: nach Maßgabe der Nutzungsbedingungen der Europäischen Arzneimittel-Agentur

---

## Aktualisierungsintervall

| Daten | Intervall |
|------|-----------|
| EMA Medicines Report | Wöchentlich (jeden Montag) |
| Evidenz aus Studien / Literatur | Regelmäßig erneut erhoben |
| Wechselwirkungsdaten | Vierteljährlich überprüft |

---

## Wissenschaftliche Zitierung

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Über den Entwickler

Diese Plattform wird von **藥提醒科技有限公司** (yao.care) entwickelt und betrieben. Den vollständigen
Hintergrund zum Unternehmen und zur Methodik finden Sie auf der Seite <a href="{{ '/about/' | relative_url }}">Über uns</a>.

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschließlich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
