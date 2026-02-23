from __future__ import annotations

from dataclasses import dataclass

from flightimpact.distance import effective_distance_km, great_circle_km
from flightimpact.emissions import co2_per_passenger_kg, fuel_to_co2_kg
from flightimpact.fuel import estimate_fuel_burn_kg
from flightimpact.types import BaselineInputs, Route


@dataclass(frozen=True)
class DeterministicEstimate:
    route: Route
    great_circle_km: float
    effective_distance_km: float
    fuel_kg: float
    co2_kg_total: float
    co2_kg_per_passenger: float


class FlightImpactModel:
    """Educational model orchestrator.

    This class wires distance -> fuel -> CO2 -> per-passenger accounting,
    while intentionally leaving fuel modeling strategy for you to implement.
    """

    def estimate_deterministic(self, route: Route, inputs: BaselineInputs) -> DeterministicEstimate:
        gc_km = great_circle_km(route.origin, route.destination)
        distance_km = effective_distance_km(gc_km, detour_factor=inputs.detour_factor)

        fuel_kg = estimate_fuel_burn_kg(distance_km)
        co2_total_kg = fuel_to_co2_kg(fuel_kg)
        co2_per_pax_kg = co2_per_passenger_kg(
            total_co2_kg=co2_total_kg,
            seats=inputs.seats,
            load_factor=inputs.load_factor,
        )

        return DeterministicEstimate(
            route=route,
            great_circle_km=gc_km,
            effective_distance_km=distance_km,
            fuel_kg=fuel_kg,
            co2_kg_total=co2_total_kg,
            co2_kg_per_passenger=co2_per_pax_kg,
        )
