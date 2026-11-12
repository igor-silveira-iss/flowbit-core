# Imagem da Engine (Python)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install .

RUN useradd --create-home --uid 10001 flowbit
USER flowbit

EXPOSE 8000
CMD ["uvicorn", "flowbit_engine.api:app", "--host", "0.0.0.0", "--port", "8000"]
