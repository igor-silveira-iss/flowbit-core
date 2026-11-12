"""API interna da Engine, consumida pela camada Web."""

from fastapi import FastAPI

from flowbit_engine import __version__

app = FastAPI(
    title="FlowBit Engine API",
    version=__version__,
    description="API interna. Contrato em contracts/openapi.yaml.",
)


@app.get("/health", tags=["sistema"])
def health() -> dict[str, str]:
    """Indica que a Engine está pronta para receber requisições."""
    return {"status": "ok"}
