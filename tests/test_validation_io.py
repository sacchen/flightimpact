from pathlib import Path

from flightimpact.validation import load_validation_records


def test_load_validation_records_skips_incomplete_rows(tmp_path: Path) -> None:
    path = tmp_path / "bench.csv"
    path.write_text(
        "route_id,origin,destination,model_kg_co2_per_pax,benchmark_kg_co2_per_pax,source,notes\n"
        "r1,SFO,JFK,100.0,120.0,Google Flights,ok\n"
        "r2,LAX,SEA,,80.0,Google Flights,missing model\n"
    )

    records = load_validation_records(path)
    assert len(records) == 1
    assert records[0].route_id == "r1"
