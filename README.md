<h2 align="center">FlowBit</h2>

<p align="center"><i>O próximo passo da ingestão de dados</i></p>

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Conceitos principais](#conceitos-principais)
- [Funcionalidades](#funcionalidades)
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
- **Interfaces:** linha de comando e API.

---

## Primeiros passos

### Pré-requisitos

- *A definir: linguagem, versão mínima e dependências do projeto.*

### Instalação

```bash
git clone https://github.com/<usuario>/flowbit.git
cd flowbit
# Instruções de instalação e build a definir
```

---

## Como contribuir

Contribuições são bem-vindas, de código, documentação, testes e relatos de bug.

1. Faça um fork do repositório.
2. Crie uma branch para a sua mudança:
   ```bash
   git checkout -b feature/minha-feature
   ```
3. Faça commits claros e objetivos.
4. Envie a branch e abra um Pull Request descrevendo o problema e a solução.

Para mudanças grandes, abra uma *issue* antes para alinharmos a abordagem.

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