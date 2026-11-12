# Arquitetura do FlowBit

Este documento descreve a arquitetura planejada do FlowBit. Decisões importantes devem ser registradas aqui ou em `docs/adr/`.

## Visão geral

O FlowBit é dividido em duas camadas, com responsabilidades separadas:

- **Web (Go):** camada de produto. Interface, autenticação de usuários, cadastro de fontes, destinos e conexões, agendamentos. É dona do banco de dados da aplicação e do seu esquema.
- **Engine (Python):** camada de execução. Recebe comandos da Web e executa as ações de fato: descoberta de schema, sincronizações, controle de estado e tratamento de falhas.

A Engine não é exposta ao usuário. Toda comunicação entre as camadas acontece pela API definida em `contracts/openapi.yaml`, protegida por um token de serviço.

## Banco de dados da aplicação

O FlowBit mantém um banco PostgreSQL próprio para seus metadados. Ele **não** é o destino dos dados sincronizados. Armazena:

- Usuários, sessões e permissões.
- Fontes, destinos e conexões cadastrados.
- Credenciais, sempre criptografadas.
- Histórico de execuções e estado incremental (cursores).
- Catálogo de schemas descobertos.

Quem é dono do esquema é a camada Web. A Engine acessa dados apenas pela API.

## Execução local

O `docker-compose.yml` na raiz sobe três serviços:

| Serviço | Imagem | Exposição |
|---------|--------|-----------|
| `db` | PostgreSQL 16 | Interna |
| `engine` | Build de `engine/` | Interna |
| `web` | Build de `web/` | `127.0.0.1:8080` |

Os segredos ficam no `.env`, gerado por `scripts/bootstrap` a partir do `.env.example`.

## Conectores

Cada conector é um pacote independente em `connectors/`. A intenção é que a Engine se comunique com conectores por um protocolo de mensagens padronizado (`spec`, `check`, `discover`, `read`, `write`), o que mantém o núcleo independente da implementação de cada integração.

## Pontos em aberto

- Formato exato das mensagens do protocolo de conectores.
- Execução de conectores em processos separados ou em containers, e a implicação de acesso ao Docker.
- Estratégia de gerenciamento da chave de criptografia (variável de ambiente no início, cofre depois).
- Escolha de biblioteca de fila para os workers (ou uso do próprio PostgreSQL).
- Frameworks de front-end (templates com htmx ou SPA consumindo a API).
