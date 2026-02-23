# Learning Modules

Use this file as your return-to-project checklist. Work one module at a time.

## Module 0: Project Orientation
Goal: understand structure and run scaffold commands once.

Tasks:
- [ ] Run `uv run flightimpact hello`
- [ ] Run `uv run flightimpact scaffold-audit`
- [ ] Skim `/Users/goddess/foundry/sandbox/flightimpact/src/flightimpact/cli.py`
- [ ] Skim `/Users/goddess/foundry/sandbox/flightimpact/docs/methods.md`

Done criteria:
- You can explain phase1/phase2/phase3/phase4 commands in your own words.

When you come back next time:
- Start Module 1.

## Module 1: Deterministic Fuel Model
Goal: implement your first baseline fuel-burn model.

Tasks:
- [ ] Implement `estimate_fuel_burn_kg()` in `/Users/goddess/foundry/sandbox/flightimpact/src/flightimpact/fuel.py`
- [ ] Run `uv run flightimpact phase1 --origin SFO --destination JFK`
- [ ] Add at least 2 tests in `/Users/goddess/foundry/sandbox/flightimpact/tests/`
- [ ] Write assumptions in `/Users/goddess/foundry/sandbox/flightimpact/docs/methods.md`

Done criteria:
- `phase1` runs without `NotImplementedError`.
- Tests pass.
- Fuel assumptions are documented.

When you come back next time:
- Compare linear vs piecewise fuel model and note differences.

## Module 2: Sensitivity Before Monte Carlo
Goal: build intuition with one-variable sweeps.

Tasks:
- [ ] Pick one parameter: detour or load factor
- [ ] Sweep low/medium/high values
- [ ] Record output changes in `/Users/goddess/foundry/sandbox/flightimpact/docs/sprints.md`
- [ ] Add one test protecting expected monotonic behavior

Done criteria:
- You can state which parameter has stronger effect for your tested route(s).

When you come back next time:
- Start uncertainty distributions in Module 3.

## Module 3: Monte Carlo Uncertainty
Goal: implement uncertain parameter sampling.

Tasks:
- [ ] Implement phase 2 TODO in `/Users/goddess/foundry/sandbox/flightimpact/src/flightimpact/uncertainty.py`
- [ ] Use `monte_carlo_samples()` and `summarize_distribution()`
- [ ] Run `uv run flightimpact phase2`
- [ ] Document distribution choices in `/Users/goddess/foundry/sandbox/flightimpact/docs/methods.md`

Done criteria:
- You can produce mean/p05/p50/p95/std for at least one route.

When you come back next time:
- Add second route and compare uncertainty width.

## Module 4: Benchmark Collection Protocol
Goal: collect high-quality benchmark rows consistently.

Tasks:
- [ ] Read `/Users/goddess/foundry/sandbox/flightimpact/data/README.md`
- [ ] Fill at least 10 rows in `/Users/goddess/foundry/sandbox/flightimpact/data/benchmarks.template.csv`
- [ ] Set `source` and `captured_at` for each row
- [ ] Keep notes for odd/outlier rows

Done criteria:
- At least 10 complete benchmark rows with provenance fields.

When you come back next time:
- Fill remaining rows to reach 20.

## Module 5: Validation + Error Analysis
Goal: quantify model error and explain it.

Tasks:
- [ ] Run `uv run flightimpact phase3`
- [ ] Review MAE and MAPE
- [ ] Write route-level analysis in `/Users/goddess/foundry/sandbox/flightimpact/docs/validation.md`
- [ ] Identify 2 model changes to test next

Done criteria:
- You can name your biggest error drivers and why.

When you come back next time:
- Implement one targeted model revision.

## Module 6: Methods Write-up
Goal: produce a defensible methods document.

Tasks:
- [ ] Complete all sections in `/Users/goddess/foundry/sandbox/flightimpact/docs/methods.md`
- [ ] Fill sprint reflections in `/Users/goddess/foundry/sandbox/flightimpact/docs/sprints.md`
- [ ] Run tests/lint/type-check

Done criteria:
- Another reader can reproduce your logic and assumptions.

When you come back next time:
- Start an extension module (aircraft-specific, stage-length curve, or radiative forcing).

## Session Template (copy/paste each visit)
Date:
Module:
Today’s objective:
What I changed:
What I learned:
What is still unclear:
Next action for next session:
