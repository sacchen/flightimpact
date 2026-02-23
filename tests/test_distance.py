from flightimpact.distance import effective_distance_km, haversine_km


def test_haversine_equator_one_degree() -> None:
    km = haversine_km(0.0, 0.0, 0.0, 1.0)
    assert 111.0 < km < 112.5


def test_effective_distance_applies_detour_factor() -> None:
    assert effective_distance_km(1000.0, detour_factor=1.05) == 1050.0
