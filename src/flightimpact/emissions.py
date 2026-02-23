from __future__ import annotations

CO2_KG_PER_KG_JET_FUEL = 3.16


def fuel_to_co2_kg(fuel_kg: float, conversion_factor: float = CO2_KG_PER_KG_JET_FUEL) -> float:
    if fuel_kg <= 0:
        msg = "Fuel burn must be positive."
        raise ValueError(msg)
    if conversion_factor <= 0:
        msg = "Conversion factor must be positive."
        raise ValueError(msg)
    return fuel_kg * conversion_factor


def co2_per_passenger_kg(total_co2_kg: float, seats: int, load_factor: float) -> float:
    if total_co2_kg <= 0:
        msg = "Total CO2 must be positive."
        raise ValueError(msg)
    if seats <= 0:
        msg = "Seats must be positive."
        raise ValueError(msg)
    if not 0.0 < load_factor <= 1.0:
        msg = "Load factor must be in (0, 1]."
        raise ValueError(msg)
    passengers = seats * load_factor
    return total_co2_kg / passengers
