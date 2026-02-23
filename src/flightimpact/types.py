from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Airport:
    code: str
    lat: float
    lon: float

    def __post_init__(self) -> None:
        normalized = self.code.strip().upper()
        object.__setattr__(self, "code", normalized)
        if len(normalized) != 3:
            msg = "Airport code must be a 3-letter IATA code."
            raise ValueError(msg)
        if not -90.0 <= self.lat <= 90.0:
            msg = "Latitude must be in [-90, 90]."
            raise ValueError(msg)
        if not -180.0 <= self.lon <= 180.0:
            msg = "Longitude must be in [-180, 180]."
            raise ValueError(msg)


@dataclass(frozen=True)
class Route:
    origin: str
    destination: str

    def __post_init__(self) -> None:
        origin = self.origin.strip().upper()
        destination = self.destination.strip().upper()
        object.__setattr__(self, "origin", origin)
        object.__setattr__(self, "destination", destination)
        if len(origin) != 3 or len(destination) != 3:
            msg = "Route requires 3-letter origin and destination IATA codes."
            raise ValueError(msg)
        if origin == destination:
            msg = "Origin and destination must be different airports."
            raise ValueError(msg)


@dataclass(frozen=True)
class BaselineInputs:
    detour_factor: float = 1.05
    seats: int = 180
    load_factor: float = 0.84

    def __post_init__(self) -> None:
        if self.detour_factor < 1.0:
            msg = "Detour factor should be >= 1.0."
            raise ValueError(msg)
        if self.seats <= 0:
            msg = "Seats must be a positive integer."
            raise ValueError(msg)
        if not 0.0 < self.load_factor <= 1.0:
            msg = "Load factor must be in (0, 1]."
            raise ValueError(msg)


@dataclass(frozen=True)
class FuelModelCoefficients:
    a_kg_per_km: float
    b_kg: float


@dataclass(frozen=True)
class SimulationConfig:
    samples: int = 10_000
    seed: int | None = 7

    def __post_init__(self) -> None:
        if self.samples <= 0:
            msg = "Simulation samples must be positive."
            raise ValueError(msg)


@dataclass(frozen=True)
class ValidationRecord:
    route_id: str
    model_kg_co2_per_pax: float
    benchmark_kg_co2_per_pax: float
