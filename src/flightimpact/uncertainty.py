from __future__ import annotations

from collections.abc import Callable

import numpy as np

from flightimpact.types import SimulationConfig

Sampler = Callable[[np.random.Generator], float]


def monte_carlo_samples(config: SimulationConfig, sampler: Sampler) -> np.ndarray:
    """Small reusable Monte Carlo scaffold for phase 2."""
    rng = np.random.default_rng(config.seed)
    values = np.empty(config.samples)
    for i in range(config.samples):
        values[i] = sampler(rng)
    return values


def summarize_distribution(samples: np.ndarray) -> dict[str, float]:
    if samples.size == 0:
        msg = "Samples array cannot be empty."
        raise ValueError(msg)
    return {
        "mean": float(np.mean(samples)),
        "p05": float(np.quantile(samples, 0.05)),
        "p50": float(np.quantile(samples, 0.50)),
        "p95": float(np.quantile(samples, 0.95)),
        "std": float(np.std(samples, ddof=1)),
    }


def phase2_todo() -> None:
    msg = (
        "Phase 2 TODO: define uncertain parameter distributions, then sample route-level emissions "
        "with monte_carlo_samples()."
    )
    raise NotImplementedError(msg)
