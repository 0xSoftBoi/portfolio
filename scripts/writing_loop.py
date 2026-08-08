#!/usr/bin/env python3
"""Small zero-dependency controller for the research writing loop.

Examples:
  python scripts/writing_loop.py status
  python scripts/writing_loop.py pick
  python scripts/writing_loop.py show when-uncertainty-makes-active-learning-worse
  python scripts/writing_loop.py advance when-uncertainty-makes-active-learning-worse evidence_ledger --note "Primary benchmark artifacts checked"
  python scripts/writing_loop.py park airborne-carrier-delete-scifi-first --note "Waiting for P0 telemetry"
  python scripts/writing_loop.py validate

This script intentionally never runs experiments or calls paid APIs. It only manages
loop state in writing/backlog.json and validates the local graph/backlog contract.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKLOG_PATH = ROOT / "writing" / "backlog.json"
GRAPH_PATH = ROOT / "writing" / "loop-graph.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def items(backlog: dict) -> list[dict]:
    return backlog.get("items", [])


def find_item(backlog: dict, slug: str) -> dict:
    for item in items(backlog):
        if item.get("slug") == slug:
            return item
    raise SystemExit(f"unknown article slug: {slug}")


def is_eligible(item: dict) -> bool:
    if item.get("status") in {"published", "parked"}:
        return False
    return bool(item.get("zero_cost_path", False))


def pick_item(backlog: dict) -> dict | None:
    eligible = [item for item in items(backlog) if is_eligible(item)]
    if not eligible:
        return None
    return max(eligible, key=lambda item: (int(item.get("priority", 0)), item.get("slug", "")))


def add_history(item: dict, node: str, note: str | None) -> None:
    history = item.setdefault("history", [])
    event = {
        "date": dt.date.today().isoformat(),
        "node": node,
    }
    if note:
        event["note"] = note
    history.append(event)


def cmd_status(backlog: dict) -> None:
    rows = sorted(items(backlog), key=lambda item: int(item.get("priority", 0)), reverse=True)
    print(f"{'PRI':>3}  {'STATUS':<16} {'NEXT':<18} TITLE")
    print("-" * 96)
    for item in rows:
        print(
            f"{int(item.get('priority', 0)):>3}  "
            f"{item.get('status', ''):<16} "
            f"{item.get('next_node', ''):<18} "
            f"{item.get('title', item.get('slug', ''))}"
        )


def cmd_pick(backlog: dict) -> None:
    item = pick_item(backlog)
    if not item:
        print("No eligible zero-cost article remains. Parked items require their unblock conditions.")
        return
    print(json.dumps(item, indent=2, ensure_ascii=False))


def cmd_show(backlog: dict, slug: str) -> None:
    print(json.dumps(find_item(backlog, slug), indent=2, ensure_ascii=False))


def cmd_advance(backlog: dict, graph: dict, slug: str, node: str, note: str | None) -> None:
    if node not in graph.get("nodes", {}):
        valid = ", ".join(sorted(graph.get("nodes", {})))
        raise SystemExit(f"unknown graph node: {node}\nvalid nodes: {valid}")
    item = find_item(backlog, slug)
    item["next_node"] = node
    if item.get("status") in {"next", "queued", "queued_bounded"}:
        item["status"] = "in_progress"
    if node == "publish":
        item["status"] = "ready_to_publish"
    elif node == "park":
        item["status"] = "parked"
    add_history(item, node, note)
    backlog["updated"] = dt.date.today().isoformat()
    save_json(BACKLOG_PATH, backlog)
    print(f"{slug}: next_node={node}, status={item['status']}")


def cmd_park(backlog: dict, slug: str, note: str | None) -> None:
    item = find_item(backlog, slug)
    item["status"] = "parked"
    item["next_node"] = "park"
    if note:
        item["blocker"] = note
    add_history(item, "park", note)
    backlog["updated"] = dt.date.today().isoformat()
    save_json(BACKLOG_PATH, backlog)
    print(f"{slug}: parked")


def cmd_publish(backlog: dict, slug: str, note: str | None) -> None:
    item = find_item(backlog, slug)
    item["status"] = "published"
    item["next_node"] = "revision_on_new_evidence"
    add_history(item, "publish", note)
    backlog["updated"] = dt.date.today().isoformat()
    save_json(BACKLOG_PATH, backlog)
    print(f"{slug}: published")


def cmd_validate(backlog: dict, graph: dict) -> None:
    errors: list[str] = []
    slugs: set[str] = set()
    nodes = set(graph.get("nodes", {}))

    if not graph.get("policies", {}).get("no_paid_experiments"):
        errors.append("graph must keep no_paid_experiments=true")
    if not backlog.get("policy", {}).get("no_paid_experiments"):
        errors.append("backlog must keep no_paid_experiments=true")

    for item in items(backlog):
        slug = item.get("slug")
        if not slug:
            errors.append("backlog item missing slug")
            continue
        if slug in slugs:
            errors.append(f"duplicate slug: {slug}")
        slugs.add(slug)

        next_node = item.get("next_node")
        if next_node and next_node not in nodes:
            errors.append(f"{slug}: unknown next_node {next_node}")
        if item.get("status") == "parked" and not item.get("blocker"):
            errors.append(f"{slug}: parked without blocker")
        if item.get("status") == "parked" and not item.get("unblock_condition") and not item.get("allowed_fallback"):
            errors.append(f"{slug}: parked without unblock_condition or allowed_fallback")
        if item.get("status") not in {"published", "parked"} and "zero_cost_path" not in item:
            errors.append(f"{slug}: missing zero_cost_path")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        raise SystemExit(1)

    chosen = pick_item(backlog)
    print(f"OK: {len(slugs)} backlog items, {len(nodes)} graph nodes")
    if chosen:
        print(f"NEXT: {chosen['slug']} — {chosen['title']}")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Control the zero-cost research writing loop")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("pick")
    sub.add_parser("validate")

    show = sub.add_parser("show")
    show.add_argument("slug")

    advance = sub.add_parser("advance")
    advance.add_argument("slug")
    advance.add_argument("node")
    advance.add_argument("--note")

    park = sub.add_parser("park")
    park.add_argument("slug")
    park.add_argument("--note")

    publish = sub.add_parser("publish")
    publish.add_argument("slug")
    publish.add_argument("--note")
    return p


def main() -> None:
    args = parser().parse_args()
    backlog = load_json(BACKLOG_PATH)
    graph = load_json(GRAPH_PATH)

    if args.command == "status":
        cmd_status(backlog)
    elif args.command == "pick":
        cmd_pick(backlog)
    elif args.command == "show":
        cmd_show(backlog, args.slug)
    elif args.command == "advance":
        cmd_advance(backlog, graph, args.slug, args.node, args.note)
    elif args.command == "park":
        cmd_park(backlog, args.slug, args.note)
    elif args.command == "publish":
        cmd_publish(backlog, args.slug, args.note)
    elif args.command == "validate":
        cmd_validate(backlog, graph)


if __name__ == "__main__":
    main()
