from flightimpact.types import ValidationRecord
from flightimpact.validation import mean_absolute_error, mean_absolute_percentage_error


def test_validation_metrics() -> None:
    rows = [
        ValidationRecord(route_id="A", model_kg_co2_per_pax=100.0, benchmark_kg_co2_per_pax=120.0),
        ValidationRecord(route_id="B", model_kg_co2_per_pax=80.0, benchmark_kg_co2_per_pax=100.0),
    ]

    mae = mean_absolute_error(rows)
    mape = mean_absolute_percentage_error(rows)

    assert mae == 20.0
    assert abs(mape - ((20.0 / 120.0 + 20.0 / 100.0) / 2.0)) < 1e-9
