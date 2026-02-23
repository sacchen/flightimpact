from __future__ import annotations

from flightimpact.types import FuelModelCoefficients


def linear_fuel_burn_kg(distance_km: float, coeffs: FuelModelCoefficients) -> float:
    """Simple baseline helper for phase 1: fuel = a*distance + b."""
    if distance_km <= 0:
        msg = "Distance must be positive."
        raise ValueError(msg)
    fuel_kg = coeffs.a_kg_per_km * distance_km + coeffs.b_kg
    if fuel_kg <= 0:
        msg = "Fuel burn must be positive. Check coefficients."
        raise ValueError(msg)
    return fuel_kg


def estimate_fuel_burn_kg(distance_km: float) -> float:
    """TODO(you): implement your own baseline fuel model in phase 1.

    Suggestions:
    - Start with a linear model (a*distance + b).
    - Then compare with a piecewise model by stage length.
    - Calibrate coefficients against a small benchmark set.
    """
    _ = distance_km
    msg = "Implement estimate_fuel_burn_kg() as your phase 1 exercise."
    raise NotImplementedError(msg)
