# Como contribuir com o FlowBit

Obrigado por considerar contribuir com o FlowBit! Contribuições são bem-vindas, de código, documentação, testes e relatos de bug.

Este guia descreve como preparar o ambiente, os padrões do projeto e o fluxo de Pull Requests. Leia também o [README](README.md) para entender a arquitetura geral.

## Sumário

- [Antes de começar](#antes-de-começar)
- [Ambiente de desenvolvimento](#ambiente-de-desenvolvimento)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Fluxo de contribuição](#fluxo-de-contribuição)
- [Padrões de código](#padrões-de-código)
- [Mudanças no contrato da API](#mudanças-no-contrato-da-api)
- [Como criar um conector](#como-criar-um-conector)
- [Migrações de banco de dados](#migrações-de-banco-de-dados)
- [Testes](#testes)
- [Segurança](#segurança)
- [Conduta e licença](#conduta-e-licença)

---

## Antes de começar

- Procure nas [issues](../../issues) se o problema ou a funcionalidade já foi discutido.
- Para mudanças grandes (novos módulos, alterações na arquitetura, novos modos de sincronização), abra uma issue antes de escrever código. Isso evita retrabalho e alinha a abordagem.
- Para correções pequenas, como erros de digitação ou bugs simples, pode abrir o Pull Request diretamente.

## Ambiente de desenvolvimento

### Pré-requisitos

| Ferramenta | Versão | Uso |
|------------|--------|-----|
| Docker e Docker Compose | Versão recente | Subir a aplicação completa e o banco |
| Go | 1.22+ | Desenvolvimento do módulo `web/` |
| Python | 3.12+ | Desenvolvimento do `engine/` e dos conectores |
| Git | Qualquer versão recente | Controle de versão |

### Subindo tudo com Docker

A forma mais simples de testar a aplicação completa é:

```bash
cp .env.example .env      # ou ./scripts/bootstrap
docker compose up -d
docker compose logs -f    # acompanhar os logs
docker compose down       # parar os containers
```

### Rodando os módulos separadamente

Para quem está trabalhando em apenas uma parte, é possível subir o banco com Docker e rodar o restante localmente:

```bash
# Banco de dados
docker compose up -d db

# Web (Go)
cd web
go run ./cmd/web

# Engine (Python)
cd engine
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn flowbit_engine.api:app --reload
```

> Os comandos exatos podem mudar conforme a estrutura for implementada. Se algo não funcionar, abra uma issue ou atualize este guia junto com a sua mudança.

## Estrutura do repositório

| Diretório | Responsabilidade |
|-----------|------------------|
| `web/` | Aplicação Go: interface, autenticação, cadastro de conexões. Dona do esquema do banco. |
| `engine/` | API e workers Python que executam as sincronizações. |
| `connectors/` | Conectores Python, um pacote independente por integração. |
| `contracts/` | Contrato da API compartilhado entre Web e Engine. |
| `docs/` | Documentação de arquitetura e decisões técnicas. |
| `scripts/` | Scripts de bootstrap e utilitários. |

Regra geral: cada módulo deve ser possível de entender e testar sem conhecer os detalhes internos dos outros. A comunicação entre Web e Engine acontece **somente** pela API definida em `contracts/`.

## Fluxo de contribuição

1. **Faça um fork** do repositório e clone a sua cópia.
2. **Crie uma branch** a partir de `main`, com um prefixo que descreva o tipo de mudança:
   - `feature/nome-da-funcionalidade`
   - `fix/descricao-do-bug`
   - `docs/o-que-mudou`
   - `refactor/o-que-mudou`
3. **Faça commits pequenos e objetivos**, seguindo o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/):
   ```
   feat(engine): adiciona descoberta de schema para o conector postgres
   fix(web): corrige validação do formulário de conexão
   docs: atualiza instruções de instalação
   ```
4. **Mantenha a branch atualizada** com a `main` (via rebase ou merge, conforme preferir).
5. **Abra o Pull Request** descrevendo:
   - O problema que está sendo resolvido, ou a funcionalidade adicionada.
   - Como a mudança foi testada.
   - Se há impacto em contratos, migrações ou configuração.
6. **Aguarde a revisão.** Pode haver pedidos de ajuste. Isso é normal e faz parte do processo.

### Checklist do Pull Request

- [ ] A mudança tem testes, ou a ausência deles está justificada.
- [ ] Os testes e linters passam localmente.
- [ ] A documentação foi atualizada, se necessário.
- [ ] Mudanças em `contracts/` foram feitas antes do código que as consome.
- [ ] Novas migrações foram adicionadas, sem alterar migrações já existentes.
- [ ] Nenhum segredo, credencial ou dado pessoal foi commitado.

## Padrões de código

### Go (`web/`)

- Formatação com `gofmt` (obrigatória).
- Análise estática com `go vet`.
- Lint com `golangci-lint`.
- Erros devem ser tratados explicitamente, não ignorados.

```bash
cd web
gofmt -l .
go vet ./...
golangci-lint run
```

### Python (`engine/` e `connectors/`)

- Formatação e lint com **ruff**.
- Verificação de tipos com **mypy** (tipagem explícita em funções públicas).
- Testes com **pytest**.

```bash
cd engine
ruff format .
ruff check .
mypy src
pytest
```

### Geral

- Nomes em inglês para código (variáveis, funções, classes, arquivos). Mensagens de interface, documentação e mensagens de commit podem ser em português.
- Não deixe código comentado ou `print` de depuração no Pull Request.
- Prefira mudanças pequenas e focadas a grandes refatorações misturadas com funcionalidades.

## Mudanças no contrato da API

O contrato em `contracts/` é o ponto de encontro entre Web e Engine. Para evitar que os dois lados divirjam:

1. **Altere primeiro o contrato** (`contracts/openapi.yaml`) e abra o PR com essa mudança.
2. **Só depois** altere o código que implementa ou consome o endpoint.
3. Mudanças que quebram compatibilidade (remover campo, mudar tipo, mudar significado) devem ser sinalizadas explicitamente no PR e discutidas antes.
4. Prefira adicionar campos opcionais a alterar os existentes.

## Como criar um conector

Conectores são a principal forma de expandir o FlowBit. Cada conector é um pacote Python independente em `connectors/`.

### Estrutura esperada

```
connectors/<nome-do-conector>/
├── src/
│   └── <nome_do_conector>/
│       └── __init__.py     # implementação do conector
├── tests/
├── README.md              # o que o conector faz, configuração e limitações
└── pyproject.toml
```

### Protocolo

Cada conector deve implementar os comandos padronizados do FlowBit:

| Comando | Função |
|---------|--------|
| `spec` | Descreve a configuração necessária (campos, tipos, obrigatoriedade). |
| `check` | Valida se a configuração informada consegue se conectar à fonte ou destino. |
| `discover` | Lista os streams e schemas disponíveis. |
| `read` | Lê registros de streams selecionados, emitindo mensagens padronizadas. |
| `write` | (Destinos) Grava registros recebidos. |

> O formato exato das mensagens será definido em `docs/` e no contrato. Consulte esses documentos antes de implementar.

### Requisitos mínimos para um conector ser aceito

- Implementar `spec`, `check` e `discover`, além de `read` (fontes) ou `write` (destinos).
- Testes unitários cobrindo a lógica principal, e testes de integração quando possível.
- README próprio explicando configuração, limitações e modos de sincronização suportados.
- **Nunca** registrar credenciais em logs ou mensagens de erro.

## Migrações de banco de dados

O esquema do banco é de responsabilidade da camada Web, e as migrações ficam em `web/migrations/`.

- Para criar uma migração nova, adicione um arquivo com o próximo número sequencial.
- **Nunca edite uma migração que já foi mergeada.** Se precisar corrigir algo, crie uma nova migração.
- Migrações devem ser idempotentes sempre que possível e ser testadas em um banco limpo e em um banco com dados.

## Testes

- Toda mudança de comportamento deve vir acompanhada de testes.
- Correções de bug devem incluir um teste que reproduza o problema.
- Antes de abrir o PR, rode os testes do módulo que você alterou. A CI rodará a suíte completa.

## Segurança

O FlowBit lida com credenciais de bancos de dados e APIs de terceiros, então a segurança é prioridade.

- **Não abra issues públicas para vulnerabilidades.** Reporte em privado pelo recurso de *Security Advisory* do GitHub (aba **Security** do repositório) ou entrando em contato com os mantenedores.
- Inclua, quando possível: descrição do problema, passos para reproduzir e impacto esperado.
- Nunca commite segredos reais. Use `.env` (que não vai para o repositório) e mantenha o `.env.example` apenas com valores de exemplo.

## Conduta e licença

- Ao participar, você concorda em manter um ambiente respeitoso e colaborativo. Recomendamos adotar o [Contributor Covenant](https://www.contributor-covenant.org/pt-br/version2/1/code_of_conduct/) como código de conduta.
- O FlowBit é licenciado sob a [Licença MIT](LICENSE). Ao enviar uma contribuição, você concorda que ela será distribuída sob essa mesma licença.
