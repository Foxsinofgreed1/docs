from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TIERS = [
    ("♠", "Singularity"),
    ("♣", "Dualarity"),
    ("♥", "Thetarity"),
    ("♦", "Quadairity"),
    ("⚛", "Quixarity"),
    ("✦", "Hexarity"),
    ("✪", "Septarity"),
    ("✵", "Octarity"),
    ("☯", "Noctararity"),
    ("⟁", "Decatarity"),
]

DIMENSIONS = [
    "Core Intelligence",
    "Market Layer",
    "Revenue Model",
    "Product Offering",
    "Platform/Tech",
    "Sales System",
    "Legal Structure",
    "Team Logic",
    "Scaling Infrastructure",
    "Evolution Outcome",
]

FUNCTIONS = [
    "Concept Genesis",
    "Recursive Design",
    "AI Integration",
    "Tokenization",
    "Smart Contract Logic",
    "UX/UI Deployment",
    "Payment Rails",
    "Feedback Loops",
    "Self-Healing Logic",
    "Ascension Protocol",
]


def slugify(text: str) -> str:
    return (
        text.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("--", "-")
    )


def build_cells() -> list[dict]:
    cells = []
    cell_id = 1
    for tier_index, (symbol, tier_name) in enumerate(TIERS, start=1):
        for dimension_index, dimension in enumerate(DIMENSIONS, start=1):
            for function_index, function in enumerate(FUNCTIONS, start=1):
                tier = f"{symbol} {tier_name}"
                cell_slug = f"cell-{cell_id:04d}-{slugify(tier_name)}-{slugify(dimension)}-{slugify(function)}"
                agent_id = f"agent-{cell_id:04d}"
                cells.append(
                    {
                        "cellId": cell_id,
                        "order": {
                            "tier": tier_index,
                            "dimension": dimension_index,
                            "function": function_index,
                        },
                        "tier": {
                            "symbol": symbol,
                            "name": tier_name,
                            "label": tier,
                        },
                        "dimension": dimension,
                        "function": function,
                        "slug": cell_slug,
                        "agent": {
                            "id": agent_id,
                            "name": f"{tier_name} {dimension} {function} Agent",
                            "role": "Cell operator",
                            "knowledgeScope": [
                                f"Tier strategy: {tier}",
                                f"Dimension playbook: {dimension}",
                                f"Function execution: {function}",
                            ],
                            "operatingDirectives": [
                                "Define the cell objective before execution.",
                                "Operate within your tier and dimension constraints.",
                                "Run the function workflow and capture outcomes.",
                                "Feed outcomes back into improvement loops.",
                            ],
                        },
                    }
                )
                cell_id += 1
    return cells


def write_csv(cells: list[dict]) -> None:
    path = ROOT / "data" / "cell-matrix.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Cell ID", "Tier", "Dimension", "Function"])
        for cell in cells:
            writer.writerow(
                [
                    cell["cellId"],
                    cell["tier"]["label"],
                    cell["dimension"],
                    cell["function"],
                ]
            )


def write_catalog(cells: list[dict]) -> None:
    path = ROOT / "data" / "cell-catalog.json"
    payload = {
        "order": {
            "description": "Cell IDs increment by Tier > Dimension > Function.",
            "tiers": [f"{symbol} {name}" for symbol, name in TIERS],
            "dimensions": DIMENSIONS,
            "functions": FUNCTIONS,
        },
        "cells": cells,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    cells = build_cells()
    write_csv(cells)
    write_catalog(cells)
    print(f"generated {len(cells)} cells")
