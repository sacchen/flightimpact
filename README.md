# flightimpact

`flightimpact` is an educational scaffold for learning quantitative modeling under uncertainty.

The repository is intentionally structured so you implement the key model decisions yourself.

## Learning-first design
- Core pipeline is wired: distance -> fuel -> CO2 -> per-passenger output.
- Critical modeling choices are left as TODOs (especially fuel and uncertainty assumptions).
- Documentation templates are included for assumptions, validation, and reflection.

## Project phases
1. Phase 1: Baseline deterministic model
2. Phase 2: Parameter uncertainty and Monte Carlo
3. Phase 3: Validation against external benchmarks
4. Phase 4: Methods write-up and reflection

## Quickstart
```bash
uv sync
uv run flightimpact hello
```

Run each phase entrypoint:
```bash
uv run flightimpact phase1 --origin SFO --destination JFK
uv run flightimpact phase2
uv run flightimpact phase3
uv run flightimpact phase4
```

## Where to implement your work
- Baseline fuel model TODO: `src/flightimpact/fuel.py`
- Uncertainty simulation TODO: `src/flightimpact/uncertainty.py`
- Validation metrics/plumbing: `src/flightimpact/validation.py`

## Data + docs scaffolding
- Sample airports: `data/airports.sample.json`
- Study routes (20, distance-banded): `data/routes.study.csv`
- Benchmark template: `data/benchmarks.template.csv`
- Data quality notes: `data/README.md`
- Session-based learning modules: `docs/modules.md`
- Methods template: `docs/methods.md`
- Sprint log template: `docs/sprints.md`
- Validation report template: `docs/validation.md`

Check scaffold health:
```bash
uv run flightimpact scaffold-audit
```

## Tooling choices for learning
- Use `pytest` for behavioral testing and experiment-driven checks.
- Keep static typing checks (`mypy` currently) as a separate gate.
- If you want to try Astral `ty`, add it in parallel with `pytest`; do not replace tests with a type checker.

## Suggested working routine
1. Implement one model improvement.
2. Add/adjust tests.
3. Record assumptions and rationale in `docs/methods.md`.
4. Compare against benchmarks and write findings in `docs/validation.md`.
5. Reflect in `docs/sprints.md`.
