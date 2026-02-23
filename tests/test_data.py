from flightimpact.data import count_complete_benchmark_rows, load_study_routes, summarize_study_route_bands


def test_study_routes_load() -> None:
    routes = load_study_routes()
    assert len(routes) >= 20


def test_study_route_bands_present() -> None:
    bands = summarize_study_route_bands()
    assert set(["short", "medium", "long"]).issubset(set(bands))


def test_benchmark_template_starts_empty() -> None:
    complete, total = count_complete_benchmark_rows()
    assert total >= 3
    assert complete == 0
