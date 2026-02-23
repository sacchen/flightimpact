from __future__ import annotations

import csv
import json
from pathlib import Path

from flightimpact.types import Airport, Route

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
AIRPORTS_PATH = DATA_DIR / "airports.sample.json"
BENCHMARK_TEMPLATE_PATH = DATA_DIR / "benchmarks.template.csv"
STUDY_ROUTES_PATH = DATA_DIR / "routes.study.csv"


def load_sample_airports(path: Path = AIRPORTS_PATH) -> dict[str, Airport]:
    payload = json.loads(path.read_text())
    airports: dict[str, Airport] = {}
    for row in payload:
        airport = Airport(code=row["iata"], lat=float(row["lat"]), lon=float(row["lon"]))
        airports[airport.code] = airport
    return airports


def load_routes_from_csv(path: Path) -> list[Route]:
    with path.open(newline="") as fp:
        reader = csv.DictReader(fp)
        return [Route(origin=row["origin"], destination=row["destination"]) for row in reader]


def load_study_routes(path: Path = STUDY_ROUTES_PATH) -> list[Route]:
    return load_routes_from_csv(path)


def count_complete_benchmark_rows(path: Path = BENCHMARK_TEMPLATE_PATH) -> tuple[int, int]:
    """Return (complete_rows, total_rows) for benchmark entries."""
    complete = 0
    total = 0
    with path.open(newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            total += 1
            if row["model_kg_co2_per_pax"].strip() and row["benchmark_kg_co2_per_pax"].strip():
                complete += 1
    return complete, total


def summarize_study_route_bands(path: Path = STUDY_ROUTES_PATH) -> dict[str, int]:
    band_counts: dict[str, int] = {}
    with path.open(newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            band = row["distance_band"].strip().lower()
            band_counts[band] = band_counts.get(band, 0) + 1
    return band_counts
