import pytest

from flightimpact.types import BaselineInputs, Route


def test_route_normalizes_codes() -> None:
    route = Route(origin="sfo", destination="jfk")
    assert route.origin == "SFO"
    assert route.destination == "JFK"


def test_route_rejects_same_airport() -> None:
    with pytest.raises(ValueError, match="different"):
        Route(origin="SFO", destination="SFO")


def test_baseline_inputs_validates_bounds() -> None:
    with pytest.raises(ValueError, match="Detour"):
        BaselineInputs(detour_factor=0.99)

    with pytest.raises(ValueError, match="Load factor"):
        BaselineInputs(load_factor=0.0)
