# Engine (Python)

API interna e workers que executam as sincronizações. É chamada apenas pela camada Web, pela API definida em `contracts/openapi.yaml`.

## Estrutura

```
engine/
├── src/flowbit_engine/
│   ├── api/        # endpoints (FastAPI)
│   ├── workers/    # execução das syncs (a implementar)
│   └── core/       # protocolo de conectores, estado e logs (a implementar)
├── tests/
├── Dockerfile
└── pyproject.toml
```

## Executando localmente

```bash
cd engine
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn flowbit_engine.api:app --reload
```

Em outro terminal:

```bash
curl http://localhost:8000/health
```

## Testes e lint

```bash
ruff format --check .
ruff check .
mypy src
pytest
```

Veja o [CONTRIBUTING.md](../CONTRIBUTING.md) para os padrões de código.
