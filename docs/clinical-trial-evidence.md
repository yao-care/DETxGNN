---
layout: default
title: "Arzneimittel mit Studienevidenz für eine neue Indikation"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Zentral zugelassene EU-Arzneimittel (EMA), deren von TxGNN vorhergesagte neue Indikation Studienevidenz (L1-L2) hat: Indikation, Level, Studien."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「siehe Bericht」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Vorhergesagte neue Indikation" | split: "|" -%}
{%- assign lev_labels = "Evidenzgrad|Evidenzstufe|Evidenzniveau|Evidenzlevel" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Arzneimittel in Deutschland mit Studienevidenz für eine neue Indikation

<p class="key-answer" data-question="Welche Arzneimittel in Deutschland haben Evidenz aus klinischen Studien für eine neue Indikation?">
<strong>{{ trial_drugs.size }}</strong> der {{ listed.size }} Arzneimittel mit einem DETxGNN-Bericht haben eine von TxGNN vorhergesagte neue Indikation mit Evidenzlevel <strong>L1 oder L2</strong> ({{ l1.size }} mit L1, {{ l2.size }} mit L2); dafür wurde also Evidenz aus klinischen Studien gefunden (randomisierte Studien, Phase-2–3-Studien oder systematische Übersichtsarbeiten).
</p>

Die Arzneimittel stammen aus den zentralen EU-Zulassungen im [EMA Medicines Report](https://www.ema.europa.eu/en/medicines/download-medicine-data) (gelten auch in Deutschland; der Zulassungsstatus steht im jeweiligen Arzneimittelbericht); die Liste gibt den Stand der Arzneimittelberichte vom {{ latest_date }} wieder.

<div class="key-takeaway">
Studienevidenz für eine vorhergesagte Indikation ist kein Wirksamkeitsnachweis. Jeder Kandidat unten <strong>erfordert weiterhin eine klinische Validierung</strong> und eine behördliche Prüfung, bevor er klinisch eingesetzt werden kann.
</div>

---

## Arzneimittel mit Studienevidenz (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Arzneimittel</th><th>Vorhergesagte neue Indikation</th><th>Evidenzlevel</th><th>Zitierte registrierte Studien (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}siehe Bericht{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(mit Vorbehalt)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## So lesen Sie diese Liste

- **Evidenzlevel** folgt den [Kriterien]({{ '/evidence-high/' | relative_url }}) der Website: L1 = Mehrere Phase-3-RCTs / systematische Übersichtsarbeiten; L2 = Einzelne RCT oder mehrere Phase-2-Studien. „(mit Vorbehalt)“ bedeutet, dass der Bericht die Einstufung einschränkt; lesen Sie den Hinweis im Bericht, bevor Sie sich darauf stützen.
- **Vorhergesagte neue Indikation** ist die Hauptvorhersage des jeweiligen Berichts. Indikationen und Kontraindikationen, die im TxGNN-Wissensgraphen bereits erfasst sind, werden ausgeschlossen; einzelne Vorhersagen können sich dennoch mit einer etablierten Anwendung überschneiden, was der Bericht dann erläutert.
- **Zitierte registrierte Studien** zählt die im Bericht zitierten ClinicalTrials.gov-Nummern (NCT). Die Berichte zitieren eine Auswahl der gefundenen Studien; 0 bedeutet, dass der Bericht keine registrierte Studie zitiert – die Grundlage der Einstufung steht dann im Abschnitt zur Literaturevidenz.
- Alle Level und die vollständige Methode finden Sie unter [Hohe Evidenz (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Alle Arzneimittel]({{ '/drugs/' | relative_url }}) und [Methodik]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Haftungsausschluss</strong><br>
Dieser Bericht dient ausschließlich als Referenz für die akademische Forschung und <strong>stellt keine medizinische Beratung dar</strong>. Befolgen Sie stets die Anweisungen Ihrer Ärztin oder Ihres Arztes; ändern Sie Ihre Medikation niemals eigenmächtig. Jede Entscheidung zur Arzneimittel-Umwidmung erfordert eine vollständige klinische Validierung und eine regulatorische Prüfung.
<br><br>
<small>Geprüft von: 藥提醒科技有限公司 (yao.care)</small>
</div>
