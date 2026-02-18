# flightimpact

flightimpact implements a flight emissions model with uncertainty and validates against Google Flight's Travel Impact Model.

### Our scope
- great-circle distance and detour factor
- fuel burn curve per distance bucket
- convert fuel to CO2 using standard factor
- allocate by cabin
- apply load factor
- add monte carlo uncertainty

We will not do
- browser extension overlap for google flights
- average vs marginal model
- better physics-based model with climb, cargo, trajectory, wind

some ideas
- uncertainty: load factor, routing detour, fuel curve coefficient. monte carlo + stats
- validate against google
- methods doc: model formulation, assumptions, parameter uncertainty, validations results, limitations

assumptions:
- distance = great-circle distance * detour factor
- fuel burn = function(distance)
- per passenger emissions = total CO2 / (seats * load factor)
