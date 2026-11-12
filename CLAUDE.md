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
