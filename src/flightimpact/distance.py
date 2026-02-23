from __future__ import annotations

import math

from flightimpact.data import load_sample_airports

EARTH_RADIUS_KM = 6371.0088


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance in km between two lat/lon points."""
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2.0) ** 2
    c = 2.0 * math.asin(math.sqrt(a))
    return EARTH_RADIUS_KM * c


def great_circle_km(origin_iata: str, destination_iata: str) -> float:
    """Look up sample airport coordinates and compute great-circle distance."""
    airports = load_sample_airports()

    origin = origin_iata.strip().upper()
    destination = destination_iata.strip().upper()

    if origin not in airports:
        msg = f"Unknown origin airport code in sample data: {origin}"
        raise KeyError(msg)
    if destination not in airports:
        msg = f"Unknown destination airport code in sample data: {destination}"
        raise KeyError(msg)

    a = airports[origin]
    b = airports[destination]
    return haversine_km(a.lat, a.lon, b.lat, b.lon)


def effective_distance_km(gc_km: float, detour_factor: float = 1.05) -> float:
    if gc_km <= 0:
        msg = "Great-circle distance must be positive."
        raise ValueError(msg)
    if detour_factor < 1.0:
        msg = "Detour factor must be >= 1.0."
        raise ValueError(msg)
    return gc_km * detour_factor
