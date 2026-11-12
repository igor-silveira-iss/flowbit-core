# Web (Go)

Aplicação web do FlowBit: interface, autenticação de usuários, cadastro de fontes, destinos e conexões. É dona do banco de dados da aplicação e das migrações.

## Estrutura

```
web/
├── cmd/web/        # ponto de entrada
├── internal/       # regras de negócio, handlers e autenticação
├── migrations/     # migrações do banco (ainda não criadas)
├── templates/      # front-end (a definir)
├── Dockerfile
└── go.mod
```

## Executando localmente

```bash
cd web
go run ./cmd/web            # ouve em :8080 (variável ADDR para mudar)
curl http://localhost:8080/health
```

## Testes e lint

```bash
go vet ./...
gofmt -l .
go test ./...
```

Veja o [CONTRIBUTING.md](../CONTRIBUTING.md) para os padrões de código.
