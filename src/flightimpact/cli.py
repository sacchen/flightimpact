from __future__ import annotations

from pathlib import Path

import typer

from flightimpact.data import (
    BENCHMARK_TEMPLATE_PATH,
    STUDY_ROUTES_PATH,
    count_complete_benchmark_rows,
    summarize_study_route_bands,
)
from flightimpact.model import FlightImpactModel
from flightimpact.types import BaselineInputs, Route
from flightimpact.uncertainty import phase2_todo
from flightimpact.validation import load_validation_records, mean_absolute_error, mean_absolute_percentage_error

app = typer.Typer(no_args_is_help=True, help="flightimpact: educational scaffold for quantitative modeling")


@app.command()
def hello() -> None:
    """Smoke test for CLI wiring."""
    print("flightimpact scaffold ready")


@app.command()
def phase1(
    origin: str = typer.Option(..., help="Origin IATA code, e.g. SFO"),
    destination: str = typer.Option(..., help="Destination IATA code, e.g. JFK"),
    detour_factor: float = typer.Option(1.05),
    seats: int = typer.Option(180),
    load_factor: float = typer.Option(0.84),
) -> None:
    """Run baseline deterministic pipeline (fuel model intentionally left for you)."""
    model = FlightImpactModel()
    route = Route(origin=origin, destination=destination)
    inputs = BaselineInputs(detour_factor=detour_factor, seats=seats, load_factor=load_factor)

    try:
        result = model.estimate_deterministic(route, inputs)
    except NotImplementedError as exc:
        print(f"Phase 1 TODO: {exc}")
        print("Edit: src/flightimpact/fuel.py")
        raise typer.Exit(code=2) from exc

    print(f"route={result.route.origin}-{result.route.destination}")
    print(f"great_circle_km={result.great_circle_km:.1f}")
    print(f"effective_distance_km={result.effective_distance_km:.1f}")
    print(f"fuel_kg={result.fuel_kg:.1f}")
    print(f"co2_kg_total={result.co2_kg_total:.1f}")
    print(f"co2_kg_per_passenger={result.co2_kg_per_passenger:.2f}")


@app.command()
def phase2() -> None:
    """Entry point for uncertainty quantification work."""
    try:
        phase2_todo()
    except NotImplementedError as exc:
        print(f"Phase 2 TODO: {exc}")
        print("Start with: src/flightimpact/uncertainty.py")
        raise typer.Exit(code=2) from exc


@app.command()
def phase3() -> None:
    """Entry point for validation and benchmark analysis."""
    complete, total = count_complete_benchmark_rows(BENCHMARK_TEMPLATE_PATH)
    records = load_validation_records(BENCHMARK_TEMPLATE_PATH)

    print("Phase 3 scaffold:")
    print(f"1) Fill benchmark data in {BENCHMARK_TEMPLATE_PATH} (complete rows: {complete}/{total})")
    print("2) Analyze route-level errors in docs/validation.md")
    print("3) Keep source/date notes for each benchmark point")

    if records:
        mae = mean_absolute_error(records)
        mape = mean_absolute_percentage_error(records)
        print("")
        print("Current metrics from completed rows:")
        print(f"MAE={mae:.3f} kg CO2/pax")
        print(f"MAPE={mape:.3%}")
    else:
        print("")
        print("No complete benchmark rows yet; metrics will appear once both model+benchmark fields are filled.")


@app.command()
def phase4() -> None:
    """Entry point for documentation and reflection."""
    methods_path = Path("docs/methods.md")
    sprints_path = Path("docs/sprints.md")
    print("Phase 4 scaffold:")
    print(f"1) Complete methods doc: {methods_path}")
    print(f"2) Complete sprint log: {sprints_path}")
    print("3) Summarize extensions and limitations")


@app.command("scaffold-audit")
def scaffold_audit() -> None:
    """Quick learning-health audit for datasets and workflow readiness."""
    bands = summarize_study_route_bands(STUDY_ROUTES_PATH)
    complete, total = count_complete_benchmark_rows(BENCHMARK_TEMPLATE_PATH)

    print("Scaffold audit:")
    print(f"- Study routes file: {STUDY_ROUTES_PATH}")
    print(f"- Distance-band coverage: {bands}")
    print(f"- Benchmark completeness: {complete}/{total} rows complete")

    minimum_rows = 20
    if total < minimum_rows:
        print(f"- Action: increase benchmark template to >= {minimum_rows} rows for stronger validation.")
    if any(band not in bands for band in ("short", "medium", "long")):
        print("- Action: ensure short/medium/long bands are all present.")
    if total >= minimum_rows and complete == 0:
        print("- Action: start entering benchmark values to unlock error metrics.")
