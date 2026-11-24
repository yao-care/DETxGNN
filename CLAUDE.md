# DETxGNN - Claude CLI 使用指引

本 repo 的維運以母 repo（yao-care/txgnn）CLAUDE.md 為準；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用德文，依據是 EMA 集中許可（medicines output report）；在地字樣集中在 `src/detxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/detxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/detxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/de_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/detxgnn/regulatory/licenses.py` | 本站沒有程式產生的許可證表；gate 依快照驗市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 正文裡跟許可證事實矛盾、直接刪掉的子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 329 筆紀錄（218 頁；
其中 6 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
其中 nepafenac、ranibizumab、dantrolene 三頁的原刪句在縮寫「z. B.」處把句子切斷、頁面留下殘句，2026-11-12 依紀錄改成只刪矛盾子句（dantrolene 整句建立在「nur erloschen」錯誤前提上，整句刪），殘句版本留在各筆紀錄的 history。

2026-11-12 正文許可證張數對事實層掃描：meloxicam 正文說 16 張 EMA 集中許可「全部撤銷」，證據包 16 張獸用許可（EMEA/V/C）狀態全是 Authorised，用 3 筆 correct 紀錄更正（`de-lic-20261112-meloxicam-*`）；另 5 頁依事實層與證據包原始狀態更正（fenbendazole、insulin_human 的獸用許可寫成已失效，實際 Authorised；insulin_glargine「6 中 5 有效」→全部 6 張；pertuzumab「3 中 2」→全部 3 張；trastuzumab 刪「目前 1 張有效」），id `de-lic-20261112-*`。

2026-11-12 許可證表格列狀態對事實層（母目錄 check_drug_page.py --row-status）：7 列 EMA 現行許可（Authorised）號碼格標成「(erloschen)」、Natpar 1 列寫「(Status: gültig)」但 EMA 為 Withdrawn，以 8 筆 `de-row-20261112-*` correct 紀錄更正（依證據包原始狀態逐列確認）。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 411 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `de-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（Deutsch）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：384 頁寫入紀錄（美國仿單 336、ChEMBL 48），27 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 48 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 21 筆紀錄、1 頁列待查；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）5 筆改成那句在節錄前（原文不改，只換順序）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Ursprüngliche Indikation: In den lokalen Daten nicht erfasst」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：EMA 集中許可（不含 BfArM 國家許可）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：acetylsalicylic_acid「Ursprüngliche Indikation: In den lokalen Daten nicht erfasst」→「Zentrale EU-Zulassungen (EMA): 3 (gültig: 3)」；2026-11-19 改了 23 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site DETxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數由程式產生（2026-11-24）

用戶 2026-11-24 決定：每週許可證排程只改得到概覽表的狀態列／張數列，AI 寫在市場段落的自由格式許可證表與正文張數句會跟著 EMA 資料過期、讓 checker 擋整頁；改成程式產生、每週自動同步。
- A. 程式許可證表：`scripts/sync_license_tables.py` 依證據包（tfda.records＝EMA 集中許可，人用；獸用 EMEA/V/C 不列）產生
  「| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |」，狀態照 EMA Medicine status（Authorised→Gültig、Withdrawn→Zurückgezogen、Refused→Abgelehnt…），
  有效在前、最多 20 列（partial 頁加「Angezeigt werden N von M …」）、表後來源句；沒有人用集中許可時只放一句說明。前後 `<!-- licenses:begin -->`／`<!-- licenses:end -->`。
  取代市場段落的第一張許可證表（表頭含 Zulassung），段落沒有表時放在段落開頭；沒有市場段落的頁不加（目前 22 頁，多是 noindex）。產品名、成分、治療領域照 EMA 英文原文，不翻譯。
  快照 `snapshots/de_licenses.json.gz` 另存 rows／total（`scripts/build_license_snapshot.py` 用 rows_of 算）；gate（第 18 項，`src/detxgnn/regulatory/licenses.py`）擋程式區塊≠快照重算、市場段落沒有程式表。
  每週排程由 `scripts/license_adapter.py` 的 `sync_tables`（--bundles，所有頁比對、只寫有變的）重排，PAGE_NOTE 讓 3b 自我檢查接受區塊標記與說明句。
- B. 正文張數改寫：`scripts/rewrite_license_counts.py`＋`src/detxgnn/regulatory/count_prose.py`（移植 Kr／My 的做法，德文句型：「X von Y Zulassungen sind gültig」「N gültige Zulassung(en) (von M)」「Von M … sind N gültig」「Alle N Zulassungen sind gültig」、zwei～zwölf、Beide、eine gültige Zulassung）；
  跨過 1 的改動連名詞單複數與主詞動詞一起改（_agree），判斷不了的（冠詞＋數字、單數「Diese／die einzige Zulassung」、改成 0、alle … gültig 而有效≠總數）不改，`--list`／`--uncertain` 列出；
  有保留、講證據包、相對數、劑型或單方／複方、獸用、其他國家或國家許可、講表格顯示筆數的句子不動，partial 頁與事實總數 0 的頁整頁不動。不寫查核框；gate 第 22 項擋「再跑一次會變」。
- 誰會跑：`scripts/apply_drug_reviews.py`（非 --check）結尾依快照跑 A、B；`scripts/build_license_snapshot.py` 寫完快照再跑一次（`--no-rewrite` 不跑）；sync_notes_to_docs.py 整頁重寫後經 apply 也會跑。
- 2026-11-24 套用：程式表取代 466 頁（公開頁 448＋noindex 18；公開頁有市場段落的 464 頁全部有程式表）；正文張數程式改寫 2 句（insulin_lispro、levodopa「fünf … vier gültig」→ 5 張全部有效）；
  被取代表上錨著的 9 筆 `de-row-20261112-*` 標 superseded（superseded_by programmatic-license-table-2026-11-24）；描述舊表「只列其中幾筆」的 7 句以 `de-lic-20261124-*` 更正（aflibercept、denosumab、emtricitabine、formoterol、pioglitazone、telmisartan、tenofovir_disoproxil）。
  另寫一支更寬的獨立偵測全量掃公開頁：改前 21 句、改後 16 句，剩下的都是事實總數 0 的頁（只有獸用許可或沒有 EMA 集中許可，資料範圍外，X_SCOPE）、把「eine Zulassung」當泛稱或同句另有試驗人數的誤中；checker 全量前後都是 P2 2／P6 1（原有、無關）。
- 已知限制：母目錄 license_refresh 的 checker（3c）在站上 apply_drug_reviews（4b）之前跑，資料變動當週正文張數句若矛盾，該頁仍會先被擋下（Kr／My 同樣）。
