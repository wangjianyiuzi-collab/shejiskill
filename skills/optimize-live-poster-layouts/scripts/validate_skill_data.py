#!/usr/bin/env python3
"""Validate cross-file invariants for optimize-live-poster-layouts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
EXPECTED_IDS = {
    "T01_HERO_CAMPAIGN", "T02_WEEKLY_SCHEDULE", "T03_LIVE_TIME_CAPSULE",
    "T04_SINGLE_PRODUCT_STORY", "T05_MULTI_PRODUCT_CATALOG",
    "T06_THEMATIC_LONGFORM", "T07_INTERACTION_BENEFIT",
}
REQUIRED_FILES = {
    ROOT / "SKILL.md", ROOT / "agents" / "openai.yaml",
    REFERENCES / "design-system.json", REFERENCES / "template-library.json",
    REFERENCES / "aesthetic-system.md", REFERENCES / "prompt-templates.md",
    REFERENCES / "quality-rubric.md", REFERENCES / "dataset-manifest.json",
    REFERENCES / "evaluation-cases.json",
}
FORBIDDEN_DATASET_KEYS = {
    "source_article_title", "source_article_url", "source_asset_url", "ocr_text",
    "brand_name", "product_name",
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def nested_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from nested_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from nested_keys(child)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    missing = sorted(str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file())
    if missing:
        fail(f"missing required files: {', '.join(missing)}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill, flags=re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing or malformed")
    keys = [line.split(":", 1)[0].strip() for line in match.group(1).splitlines() if ":" in line]
    if keys != ["name", "description"]:
        fail(f"SKILL.md frontmatter must contain only name and description; got {keys}")

    templates = load_json(REFERENCES / "template-library.json")["templates"]
    template_ids = {item["template_id"] for item in templates}
    if template_ids != EXPECTED_IDS:
        fail(f"template IDs differ from expected set: {sorted(template_ids)}")

    dataset = load_json(REFERENCES / "dataset-manifest.json")
    distribution = dataset["template_distribution"]
    distribution_ids = {item["template_id"] for item in distribution}
    if distribution_ids != EXPECTED_IDS:
        fail("dataset distribution and template library IDs differ")
    if sum(item["count"] for item in distribution) != dataset["summary"]["retained_posters"]:
        fail("template counts do not sum to retained poster count")
    if abs(sum(item["share"] for item in distribution) - 1.0) > 0.001:
        fail("template shares do not sum to approximately 1.0")
    leaked = FORBIDDEN_DATASET_KEYS.intersection(nested_keys(dataset))
    if leaked:
        fail(f"aggregate dataset contains forbidden raw keys: {sorted(leaked)}")

    evaluations = load_json(REFERENCES / "evaluation-cases.json")["cases"]
    if len(evaluations) < 14:
        fail("expected at least two evaluation cases per template")
    covered = {case["expected_template"].split(" + ")[0] for case in evaluations}
    if covered != EXPECTED_IDS:
        fail("evaluation cases do not cover every template")

    prompts = (REFERENCES / "prompt-templates.md").read_text(encoding="utf-8")
    if prompts.count("Typesetting specification:") != 7:
        fail("prompt templates must define one typesetting specification per template")
    if "No letters, words, numerals" not in prompts:
        fail("prompt templates are missing the shared no-text constraint")

    print("OK: skill structure, JSON, privacy, template coverage, and prompt contracts are valid")


if __name__ == "__main__":
    main()
