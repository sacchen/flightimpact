# Data Notes

## Purpose
These datasets are intentionally small and transparent for learning workflows.

## Quality assessment
- `airports.sample.json`: good enough for route-distance computation demos, not production-grade global coverage.
- `routes.study.csv`: curated for distance-band coverage (short/medium/long) and benchmarking practice.
- `benchmarks.template.csv`: empty template, quality depends entirely on how carefully you fill it.

## What is high quality vs low quality here
High-quality benchmark collection means:
1. Routes are diverse by stage length and geography.
2. Benchmark values are collected with a fixed protocol and timestamp.
3. Source metadata is logged (tool name, date, assumptions).
4. Outliers are investigated, not silently dropped.

Low-quality benchmark collection means:
1. Only 2-3 familiar routes.
2. Mixed data collection methods across routes.
3. Missing capture dates/sources.
4. No handling notes for suspicious points.

## Recommended protocol for phase 3
1. Start from `routes.study.csv`.
2. Fill `benchmarks.template.csv` with at least 20 routes.
3. Record `source` and `captured_at` for every row.
4. Keep rejected rows in notes instead of deleting them.
