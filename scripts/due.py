#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
due.py — 从 learn skill 的 cards.md 里挑出到期的复习卡片。

用途：learn skill 每次会话开始时跑一次，决定先复习哪些卡。

用法：
    python due.py <cards.md 路径>
    python due.py <cards.md 路径> --days 2        # 预告未来 2 天内到期的
    python due.py <cards.md 路径> --today 2026-01-05   # 指定"今天"（便于测试）
    python due.py <cards.md 路径> --all           # 打印全部卡片

输出：到期卡片列表（按到期日排序）+ 统计。
依赖：仅标准库。
"""

import argparse
import datetime as dt
import re
import sys

# Windows 控制台默认可能是 GBK，强制 UTF-8 输出，避免中文报错
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

COLS = ["ID", "主题", "问题", "答案", "上次复习", "间隔(天)", "下次复习", "等级"]


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def parse_cards(path):
    """解析 markdown 表格。返回 dict 列表。"""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    cards = []
    for lineno, line in enumerate(lines, 1):
        line = line.rstrip("\n")
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(COLS):
            continue
        # 跳过表头行与分隔行
        if cells[0] in ("ID", "") or set(cells[0]) <= set("-: "):
            continue
        if not re.match(r"^[A-Za-z]?\d+$", cells[0]):
            continue
        # 跳过模板占位行（单元格里含 <...>）
        if any(re.search(r"<[^>]*>", c) for c in cells):
            continue

        card = dict(zip(COLS, cells))
        card["_line"] = lineno
        card["_due"] = parse_date(card["下次复习"])
        card["_interval"] = card["间隔(天)"]
        cards.append(card)
    return cards


def main():
    ap = argparse.ArgumentParser(description="找出 cards.md 里到期的复习卡片")
    ap.add_argument("cards", help="cards.md 的路径")
    ap.add_argument("--days", type=int, default=0, help="预告未来 N 天内到期的（默认 0，只看今天及以前）")
    ap.add_argument("--today", help="指定今天日期 YYYY-MM-DD（默认取系统日期）")
    ap.add_argument("--all", action="store_true", help="打印全部卡片")
    args = ap.parse_args()

    today = parse_date(args.today) or dt.date.today()

    try:
        cards = parse_cards(args.cards)
    except FileNotFoundError:
        print(f"找不到文件：{args.cards}")
        print("首次使用请从 assets/cards.md 复制一份作为模板。")
        return 1

    if not cards:
        print(f"卡片文件里还没有卡片：{args.cards}")
        print("（新建主题时这是正常的；新知识点学完后应写入卡片。）")
        return 0

    horizon = today + dt.timedelta(days=max(args.days, 0))

    if args.all:
        show = sorted(cards, key=lambda c: (c["_due"] or dt.date.max))
    else:
        show = [c for c in cards if c["_due"] is not None and c["_due"] <= horizon]
        show.sort(key=lambda c: c["_due"])

    print(f"今天：{today.isoformat()}   卡片总数：{len(cards)}")

    no_date = [c for c in cards if c["_due"] is None]
    if no_date:
        print(f"⚠️ 有 {len(no_date)} 张卡缺少有效日期：{', '.join(c['ID'] for c in no_date)}")

    if not show:
        print("\n✅ 今天没有到期卡片。")
        return 0

    label = "全部卡片" if args.all else ("到期卡片" if args.days == 0 else f"未来 {args.days} 天内到期")
    print(f"\n=== {label}（{len(show)} 张）===\n")
    for c in show:
        due = c["_due"].isoformat() if c["_due"] else "无日期"
        overdue = ""
        if c["_due"] and c["_due"] < today:
            overdue = f"  ⏰逾期 {(today - c['_due']).days} 天"
        grade = c["等级"] or "-"
        print(f"[{c['ID']}] {due}{overdue}  等级:{grade}  间隔:{c['_interval']}天")
        print(f"    主题：{c['主题']}")
        print(f"    问：{c['问题']}")
        print(f"    答：{c['答案']}")
        print()

    if not args.all:
        print("提示：先只给「问」，等他回答后再对照「答」，然后更新 上次复习/间隔/下次复习/等级 四列。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
