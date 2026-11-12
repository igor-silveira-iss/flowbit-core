# Conectores

Cada conector é um pacote Python independente, com nome no formato `<nome-do-conector>` (por exemplo, `postgres` ou `rest-api`).

Estrutura esperada de um conector:

```
connectors/<nome-do-conector>/
├── src/<nome_do_conector>/
│   └── __init__.py   # implementação
├── tests/
├── README.md         # configuração, modos de sincronização e limitações
└── pyproject.toml
```

Antes de criar um conector, leia a seção "Como criar um conector" no [CONTRIBUTING.md](../CONTRIBUTING.md) e o [documento de arquitetura](../docs/architecture.md).
