# Parameter Optimization of S-I-R Epidemic Model: Single and Multi-Objective Genetic Algorithm-Based Approaches

This repository implements single- and multi-objective genetic-algorithm based approaches to estimate parameters of the S-I-R (Susceptible–Infected–Recovered) epidemic model. The code provides a simple single-objective Genetic Algorithm (GA) and a multi-objective NSGA-II implementation to find transmission (`beta`) and recovery (`gamma`) rates that best match observed infection/recovery time series.

**Highlights**
- Single-objective optimization using a mean-error fitness with `GeneticAlgorithm`.
- Multi-objective optimization using `MyNSGA2` (NSGA-II) with two objective functions.
- Small, focused utilities for generating synthetic S-I-R datasets.

**Quick Links**
- Single-objective: [src/algorithms/ga.py](src/algorithms/ga.py)
- Multi-objective: [src/algorithms/nsga2.py](src/algorithms/nsga2.py)
- Utilities: [src/utils/utils.py](src/utils/utils.py)

## Features

- Estimate S-I-R parameters (`beta`, `gamma`) from time-series data.
- Option to run a single-objective GA or a Pareto-front NSGA-II optimization.
- Reproducible runs via the `pymoo` optimization framework.

## Requirements

- Python 3.12+ recommended
- numpy
- pymoo

You can install the minimal dependencies with `uv` package manager (recommended):

```bash
# install the `uv` tool (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# add project dependencies using `uv`
uv sync
```

If you don't use `uv`, the equivalent `pip` commands are shown for compatibility.

## Installation

Clone the repository and (optionally) create a virtual environment:

```bash
git clone <repo-url>
cd sir_implementation
# (optional) create a virtual environment if you want an isolated interpreter
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Quickstart / Examples

Generate a synthetic dataset and run the single-objective Genetic Algorithm:

```python
from src.utils.utils import generate_sir_dataset
from src.algorithms.ga import GeneticAlgorithm

# Generate synthetic data (N, I0, days, beta, gamma)
data = generate_sir_dataset(N=1000, I0=1, num_of_days=60, beta=0.3, gamma=0.1)

# Instantiate and run GA
ga = GeneticAlgorithm(data=data, N=1000, I0=1)
best_params = ga.find_optima(verbose=False)
print('Estimated (beta, gamma):', best_params)
```

Run the multi-objective NSGA-II optimizer (Pareto front of solutions):

```python
from src.algorithms.nsga2 import MyNSGA2
from src.utils.utils import generate_sir_dataset

data = generate_sir_dataset(N=1000, I0=1, num_of_days=60, beta=0.3, gamma=0.1)
nsga = MyNSGA2(data=data, N=1000, I0=1)
pareto_solution = nsga.find_optima(verbose=False)
print('One Pareto solution (beta, gamma):', pareto_solution)
```

Notes:
- The optimization objects use `pymoo.minimize(...)` under the hood and return the decision variables (`beta`, `gamma`) in `.X`.
- Adjust `pop_size` and other algorithm settings directly in the classes if you need different search behavior.

## Project structure

- `src/algorithms/ga.py` — single-objective `GeneticAlgorithm` class.
- `src/algorithms/nsga2.py` — multi-objective `MyNSGA2` class (NSGA-II).
- `src/utils/utils.py` — `generate_sir_dataset` utility to create S-I-R time series.
- `pyproject.toml` — project metadata (may contain dependencies).
- `LICENSE` — project license.

## Contributing

Contributions are welcome. Suggestions:

- Open an issue to discuss feature requests or bugs.
- Fork the repository and submit a pull request with tests or examples.

## License

This project is provided under the terms of the LICENSE file in this repository.

---

