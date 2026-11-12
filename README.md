<h2 align="center">FlowBit</h2>

<p align="center"><i>O próximo passo da ingestão de dados</i></p>

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Conceitos principais](#conceitos-principais)
- [Funcionalidades](#funcionalidades)
- [Arquitetura](#arquitetura)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Primeiros passos](#primeiros-passos)
- [Uso](#uso)
- [Como contribuir](#como-contribuir)
- [Colaboradores](#colaboradores)
- [Licença](#licença)

---

## Sobre o projeto

O FlowBit é uma ferramenta de ingestão de dados open-source, inspirada em plataformas como o Airbyte. Ele conecta **fontes** (APIs, bancos de dados, arquivos e serviços SaaS) a **destinos** (data warehouses, data lakes e bancos relacionais), copiando os dados de forma padronizada e, quando possível, incremental.

A ideia central é que construir e manter pipelines de ingestão não precise ser um trabalho repetido para cada time. Cada integração vira um **conector** reutilizável, que qualquer pessoa pode usar ou melhorar.

> **Status:** projeto em fase inicial. Partes deste README descrevem o escopo planejado e serão atualizadas à medida que as funcionalidades forem entregues.

---

## Conceitos principais

| Termo | Significado |
|-------|-------------|
| **Source (fonte)** | De onde os dados são lidos. |
| **Destination (destino)** | Para onde os dados são enviados. |
| **Connector (conector)** | Implementação que sabe conversar com uma fonte ou um destino. |
| **Connection (conexão)** | Ligação entre uma fonte e um destino, com agenda e regras de sincronização. |
| **Stream** | Conjunto de registros de uma mesma entidade, como a tabela `customers`. |
| **Sync (sincronização)** | Uma execução de movimentação de dados entre fonte e destino. |

---

## Funcionalidades

Escopo planejado:

- **Conectores extensíveis:** uma interface comum para criar novas fontes e destinos.
- **Modos de sincronização:** carga completa (*full refresh*) e incremental (*append* e deduplicação).
- **Agendamento:** sincronizações recorrentes com controle de frequência.
- **Controle de schema:** detecção e registro de mudanças nas estruturas dos dados.
- **Tratamento de falhas:** reexecução segura de syncs, sem duplicar registros.
- **Observabilidade:** logs e histórico de execuções.
- **Interfaces:** aplicação web, linha de comando e API.

---

## Arquitetura

O FlowBit é dividido em duas camadas, dentro de um único repositório (monorepo):

- **Web (Go):** aplicação web com interface, autenticação de usuários, cadastro de fontes, destinos e conexões. É dona do banco de dados da aplicação e do esquema (migrações).
- **Engine (Python):** API que executa as ações de fato: descoberta de schema, sincronizações, controle de estado e tratamento de falhas. É chamada apenas pela camada Web, não diretamente pelo usuário.
- **Banco de dados (PostgreSQL):** armazena usuários, configurações, conexões, histórico de execuções e estado incremental. Não é o destino dos dados sincronizados.
- **Conectores (Python):** pacotes independentes, um por integração, que implementam a comunicação com fontes e destinos.

```
 Navegador
    │
    ▼
┌─────────┐   API interna   ┌─────────┐
│   Web   │ ──────────────▶ │ Engine  │ ──▶ Fontes / Destinos
│  (Go)   │                 │(Python) │     (via conectores)
└────┬────┘                 └─────────┘
     │
     ▼
┌─────────┐
│Postgres │  metadados da aplicação
└─────────┘
```

> *Este diagrama descreve a arquitetura planejada e será atualizado conforme a implementação avançar.*

---

## Estrutura do repositório

```
flowbit/
├── web/           # Aplicação Go (UI, autenticação, configurações)
├── engine/        # API e workers Python (execução das syncs)
├── connectors/    # Conectores Python, um pacote por integração
├── contracts/     # Contrato compartilhado entre Web e Engine (OpenAPI)
├── docs/          # Arquitetura e decisões técnicas
├── scripts/       # Bootstrap e utilitários
├── docker-compose.yml
└── .env.example
```

---

## Primeiros passos

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e Docker Compose
- Para desenvolvimento local, sem Docker: Go 1.22+ e Python 3.12+

### Instalação

```bash
git clone https://github.com/<usuario>/flowbit.git
cd flowbit
cp .env.example .env      # ou ./scripts/bootstrap, que gera os segredos automaticamente
docker compose up -d
```

Depois de subir os containers, acesse [http://localhost:8080](http://localhost:8080).

> *Os comandos acima serão válidos após a estrutura inicial ser implementada.*

---

## Como contribuir

Contribuições são bem-vindas, de código, documentação, testes e relatos de bug.

Antes de começar, leia o **[CONTRIBUTING.md](CONTRIBUTING.md)**, que descreve o ambiente de desenvolvimento, os padrões de código, o fluxo de Pull Requests e como criar novos conectores.

Resumidamente:

1. Faça um fork do repositório.
2. Crie uma branch para a sua mudança:
   ```bash
   git checkout -b feature/minha-feature
   ```
3. Faça commits claros e objetivos, seguindo o padrão do projeto.
4. Envie a branch e abra um Pull Request descrevendo o problema e a solução.

Para mudanças grandes, abra uma *issue* antes para alinharmos a abordagem.

Vulnerabilidades de segurança devem ser reportadas em privado, conforme descrito no CONTRIBUTING.md, e não em issues públicas.

---

## Colaboradores

Obrigado às pessoas que ajudam a construir o FlowBit:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/igor-silveira-iss">
        <img src="https://github.com/igor-silveira-iss.png" width="100" height="100" style="border-radius: 50%;" alt="igor-silveira-iss"/><br />
        <sub><b>igor-silveira-iss</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/luandzanon">
        <img src="https://github.com/luandzanon.png" width="100" height="100" style="border-radius: 50%;" alt="luandzanon"/><br />
        <sub><b>luandzanon</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).