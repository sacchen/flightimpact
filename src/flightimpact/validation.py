from __future__ import annotations

import csv
from pathlib import Path

from flightimpact.types import ValidationRecord


def mean_absolute_error(records: list[ValidationRecord]) -> float:
    _require_non_empty(records)
    return sum(abs(r.model_kg_co2_per_pax - r.benchmark_kg_co2_per_pax) for r in records) / len(records)


def mean_absolute_percentage_error(records: list[ValidationRecord]) -> float:
    _require_non_empty(records)
    _require_positive_benchmarks(records)
    return (
        sum(
            abs(r.model_kg_co2_per_pax - r.benchmark_kg_co2_per_pax) / r.benchmark_kg_co2_per_pax
            for r in records
        )
        / len(records)
    )


def _require_non_empty(records: list[ValidationRecord]) -> None:
    if not records:
        msg = "At least one validation record is required."
        raise ValueError(msg)


def _require_positive_benchmarks(records: list[ValidationRecord]) -> None:
    if any(r.benchmark_kg_co2_per_pax <= 0 for r in records):
        msg = "Benchmark values must be positive for MAPE."
        raise ValueError(msg)


def load_validation_records(path: Path) -> list[ValidationRecord]:
    records: list[ValidationRecord] = []
    with path.open(newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            model_value = row["model_kg_co2_per_pax"].strip()
            benchmark_value = row["benchmark_kg_co2_per_pax"].strip()
            if not model_value or not benchmark_value:
                continue
            records.append(
                ValidationRecord(
                    route_id=row["route_id"],
                    model_kg_co2_per_pax=float(model_value),
                    benchmark_kg_co2_per_pax=float(benchmark_value),
                )
            )
    return records
