---
layout: default
title: Downloads
nav_order: 94
permalink: /downloads/
description: "Offene Daten von DETxGNN zum Herunterladen: FHIR-Ressourcen, Vorhersageergebnisse und Suchindex."
---

# Downloads

<div class="key-takeaway">
Die Vorhersagen werden im Format FHIR R4 veröffentlicht und lassen sich unmittelbar in Systeme für elektronische Patientenakten einbinden.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Deutschland: was die Dateien derzeit enthalten

| Datei | Aktueller Inhalt |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} Arzneimittel mit ihren vorhergesagten Indikationen |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} Arzneimittel mit Evidenzstufe und ursprünglicher Indikation |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} MedicationKnowledge-Ressourcen (eine je Arzneimittel) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ClinicalUseDefinition-Ressourcen (eine je vorhergesagter Indikation) |

Weiterverwendung des lokalen Datensatzes: [EMA Medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx), veröffentlicht von European Medicines Agency (EMA); für die Weiterverwendung gelten die Bedingungen des Herausgebers, diese Website räumt keine weiteren Rechte ein.

{% if site.data.local_facts.top_licensed.size > 0 %}Arzneimittel mit den meisten gültigen zentrale EU-Zulassungen (EMA): {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Letzte Korrekturen im Prüfprotokoll: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## FHIR, Suchindex und Weiterverwendung

Das FHIR-R4-CapabilityStatement liegt unter `/fhir/metadata`, alle Vorhersagen gebündelt unter `/fhir/Bundle/all-predictions.json`, und `/data/search-index.json` enthält die Arzneimittel und Indikationen der Websitesuche. Die Daten dienen nur der Forschung; nennen Sie die Website und zitieren Sie die TxGNN-Publikation, Lizenzen der Quellen: [Datenquellen]({{ '/sources/' | relative_url }}).
<!-- local-condensed:end -->

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
