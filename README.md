# qec-learn
Personal project for learning quantum computing and quantum error correction.

Install the [uv](https://docs.astral.sh/uv/) package and project manager: `brew install uv`

Update the project's environment: `uv sync`

Run a script: `uv run python scripts/01-measure-aer.py`

Add qiskit

```shell
uv add qiskit
uv add qiskit_aer
```

Add deltakit

```shell
uv add deltakit
uv run python
```

```python
from deltakit.explorer import Client
Client.set_token("<token>")
```

Ref:
https://deltakit.riverlane.com/api/docs/guide/getting_started.html

