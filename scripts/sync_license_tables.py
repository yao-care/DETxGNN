#!/usr/bin/env python3
"""市場段落的許可證表由程式產生（2026-11-24，用戶決定「程式產生許可證表」；範本 UkTxGNN／SgTxGNN 同名檔、ZaTxGNN sync_license_pages.py）。

為什麼：市場段落的許可證表原本是 AI 寫的自由格式表（多數表頭「Zulassungsnummer | Produktname | Darreichungsform |
Zugelassene Indikation」，少數另有 Status 欄或在號碼格寫「(erloschen)」）。EMA 資料每週變，AI 表不會跟著改，
跟事實矛盾時 checker 擋整頁。改成程式依證據包（data/bundles 的 tfda.records＝EMA 集中許可，人用；獸用 EMEA/V/C 已由
license_adapter.preprocess 移到 veterinary_records，不列）產生，每週排程（license_adapter.sync_tables）自動同步。

表的內容（全程不用 AI；文字照 EMA 原文，不翻譯）：
  | Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
  狀態欄照 EMA Medicine status 轉成本站寫法（Authorised→Gültig、Withdrawn→Zurückgezogen…，STATUS_DE）；
  排序：有效在前，同狀態依 EMA 號碼；最多 MAX_ROWS 列（證據包只收前 20 筆的 partial 頁多一句 SHOW）。
  表後一行來源句（SOURCE）；本藥沒有人用集中許可時整個區塊只有 NONE_LINE 一行。
  區塊前後各一行 <!-- licenses:begin --> <!-- licenses:end -->（查核紀錄、刪句工具與 gate 用來分辨程式寫的字）。
放在哪：本頁市場段落（site_config.MARKET_RE）裡有許可證表的那一段，取代第一張許可證表（表頭含「Zulassung」）；
  都沒有表時放在第一個市場段落（標題不是「<藥>: Bekannte Anwendungen …」的那個）開頭。沒有市場段落的頁不加。
  表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照改寫）。
資料來源：預設讀快照 snapshots/de_licenses.json.gz 的 rows／total（scripts/build_license_snapshot.py 依證據包算好，
  用 rows_of）；--bundles 改讀 data/bundles（每週排程在建新快照前用）。gate（scripts/check_seo_docs.py 的許可證項）
  檢查程式區塊＝快照重算的結果。
誰會跑：scripts/apply_drug_reviews.py（非 --check）結尾、scripts/build_license_snapshot.py 結尾、每週排程
  license_adapter.sync_tables（--bundles）。sync_notes_to_docs.py 整頁重寫後會跑 apply_drug_reviews.py，所以也會重新產生。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--bundles] [--check] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots" / "de_licenses.json.gz"
MARKET_RE = re.compile(r"Markt|Grundlegende Informationen")
SKIP_SEC = re.compile(r"Bekannte Anwendungen")
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
HEAD = ["| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |",
        "|------|------|------|------|------|"]
SOURCE = ("Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet "
          "im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.")
SHOW = "Angezeigt werden {n} von {m} erfassten zentralen EU-Zulassungen (gültige zuerst)."
NONE_LINE = ("In den ausgewerteten EMA-Daten ist für diesen Wirkstoff keine zentrale EU-Zulassung eines Humanarzneimittels erfasst; "
             "nationale Zulassungen (BfArM) sind in diesen Daten nicht enthalten.")
MAX_ROWS = 20
STATUS_DE = {"authorised": "Gültig", "withdrawn": "Zurückgezogen", "lapsed": "Erloschen", "expired": "Abgelaufen",
             "revoked": "Widerrufen", "suspended": "Ruhend (suspendiert)", "refused": "Abgelehnt", "not authorised": "Nicht zugelassen"}
# 每週排程 3b 的自我檢查（license_refresh）：改到的行除了表格列只能是這些（license_adapter.PAGE_NOTE 用同一份）
PAGE_NOTE = r"^(" + "|".join(re.escape(x) for x in ("## Marktinformationen Deutschland", BEGIN, END, SOURCE, NONE_LINE)) + r"|Angezeigt werden \d+ von \d+ erfassten zentralen EU-Zulassungen \(gültige zuerst\)\.)$"


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/").replace(";", "; ")).strip()
    t = re.sub(r"\s+;", ";", t)
    return (t if len(t) <= n else t[:n - 1].rstrip() + "…") or "–"


def status_de(s):
    s = str(s or "").strip()
    return STATUS_DE.get(s.lower(), s or "–")


def rows_of(tf, fc=None):
    """證據包 tfda（人用集中許可）→ (表格列, 總數)。總數＝total_matches 與收錄筆數取大者（partial 頁 total_matches 較大）。"""
    seen, valid, other = set(), [], []
    for r in tf.get("records") or []:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen or k.startswith("EMEA/V/"):
            continue
        seen.add(k)
        st = str(r.get("status") or "").strip()
        row = (k, f"| {k} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'), 60)} | {cell(r.get('ingredients'), 90)} | "
                  f"{cell(r.get('indication'), 110)} | {status_de(st)} |")
        (valid if st.lower() == "authorised" else other).append(row)
    rows = [x[1] for x in sorted(valid)] + [x[1] for x in sorted(other)]
    return rows, max(len(rows), int(tf.get("total_matches") or 0))


def program_block(rows, total):
    if not rows:
        return [NONE_LINE]
    out = HEAD + rows[:MAX_ROWS] + [""]
    if total > min(len(rows), MAX_ROWS):
        out.append(SHOW.format(n=min(len(rows), MAX_ROWS), m=total))
        out.append("")
    return out + [SOURCE]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _is_license_table_head(lines, k):
    return lines[k].startswith("|") and (k == 0 or not lines[k - 1].startswith("|")) and "Zulassung" in lines[k] \
        and k + 1 < len(lines) and re.match(r"\|\s*:?-", lines[k + 1])


def _sections(lines):
    out = []
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and MARKET_RE.search(ln[3:]):
            j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
            out.append((i, j))
    return out


def _splice(lines, x, y, blk):
    """lines[x:y] 換成 blk，前後各留恰好一行空行（只動接縫處的空行）"""
    head, tail = lines[:x], lines[y:]
    while head and not head[-1].strip():
        head.pop()
    while tail and not tail[0].strip():
        tail.pop(0)
    return head + [""] + blk + ([""] + tail if tail else [""])


def process(text, rows, total):
    """回傳新內容（沒有市場段落時原樣）。可重複執行。"""
    lines = text.replace("\r\n", "\n").split("\n")
    blk = wrap(program_block(rows, total))
    if BEGIN in lines and END in lines:
        return "\n".join(_splice(lines, lines.index(BEGIN), lines.index(END) + 1, blk))
    secs = _sections(lines)
    for a, b in secs:
        tb = [k for k in range(a + 1, b) if _is_license_table_head(lines, k)]
        if tb:
            y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            return "\n".join(_splice(lines, tb[0], y + 1, blk))
    a = next((a for a, b in secs if not SKIP_SEC.search(lines[a])), None)
    if a is None:
        return (add_section(text, rows, total) if not secs else None) or text
    return "\n".join(_splice(lines, a + 1, a + 1, blk))


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁整頁沒有市場段落、但證據包有人用集中許可紀錄的，
# 補「## Marktinformationen Deutschland」段落放程式表。位置：「## Zytotoxizität」之前（沒有就「## Sicherheitsaspekte」，
# 再沒有就「## Fazit und nächste Schritte」「## Prüfprotokoll」「## Haftungsausschluss」之前）。noindex 頁與沒有人用紀錄的頁不補。
ADD_SEC = "## Marktinformationen Deutschland"
ADD_BEFORE = ("Zytotoxizität", "Sicherheitsaspekte", "Fazit und nächste Schritte", "Prüfprotokoll", "Haftungsausschluss")


def is_public(text):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    return not re.search(r"^noindex:\s*true", fm, re.M)


def add_section(text, rows, total):
    if not rows or not is_public(text):
        return None
    lines = text.split("\n")
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    k = at - 1
    while k > 0 and not lines[k].strip():
        k -= 1
    if lines[k].strip() == "<!-- review:begin log -->":  # 查核紀錄段的標題在 log 區塊裡：段落放在區塊之前（否則套用查核紀錄時會被當成 log 區塊的內容）
        at = k
    sec = [ADD_SEC, ""] + wrap(program_block(rows, total)) + [""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))


def _snapshot():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def is_redirect(text):
    h = text[:3000]
    return 'http-equiv="refresh"' in h or bool(re.search(r"^layout:\s*id_redirect", h, re.M))


def run(from_bundles=False, check=False, only=None):
    """回傳改到的頁（檔名）。快照或證據包沒有的頁不動。"""
    snap = {} if from_bundles else _snapshot()
    changed = []
    for p in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and p.name not in only and p.stem not in only:
            continue
        raw = p.read_bytes().decode("utf-8")
        if is_redirect(raw):
            continue
        if from_bundles:
            b = _bundle(p.stem)
            if b is None:
                continue
            rows, total = rows_of(b.get("tfda") or {})
        else:
            e = snap.get(p.stem)
            if not e or "rows" not in e:
                continue
            rows, total = e["rows"], e["total"]
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = process(t0, rows, total)
        if new != t0:
            changed.append(p.name)
            if not check:
                p.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


def block_problems(sec_lines, entry):
    """gate 用：段落裡的程式區塊＝快照重算的結果（licenses.page_problems 呼叫）"""
    has_b, has_e = BEGIN in sec_lines, END in sec_lines
    if has_b != has_e:
        return ["程式許可證區塊標記不成對"]
    if not has_b or "rows" not in entry:
        return []
    i, j = sec_lines.index(BEGIN), sec_lines.index(END)
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    want = [x for x in program_block(entry["rows"], entry["total"]) if x.strip()]
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        return [f"程式許可證區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 python3 scripts/sync_license_tables.py）"]
    return []


if __name__ == "__main__":
    a = sys.argv[1:]
    only = {x for x in a if not x.startswith("--")} or None
    ch = run(from_bundles="--bundles" in a, check="--check" in a, only=only)
    print(f"程式許可證表：{'待改' if '--check' in a else '改'} {len(ch)} 頁")
    if "--check" in a:
        sys.exit(1 if ch else 0)
