# generate-sn-stories

Automatize a transformação de requisitos em estórias de usuário para ServiceNow, a partir de documentos PDF ou outras fontes, utilizando agentes inteligentes com CrewAI.

---

## ✨ Visão Geral

O **generate-sn-stories** é uma solução que automatiza a análise e extração de requisitos e converte-os em estórias de usuário detalhadas, prontas para implementação em ServiceNow. O projeto emprega agentes especializados em análise de requisitos, arquitetura ServiceNow e gestão de produto, promovendo padronização, rastreabilidade e eficiência em projetos ágeis.

---

## 🚀 Benefícios

- **Automação ponta-a-ponta:** Reduz o esforço manual e subjetividade na conversão de requisitos para user stories.
- **Aderência a melhores práticas:** Garante padrões de ServiceNow e de escrita de estórias de usuário.
- **Rastreabilidade e colaboração:** Organiza o fluxo em etapas claras com agentes dedicados.
- **Escalabilidade:** Adaptável para múltiplos documentos e grandes volumes de requisitos.

---

## 🏗️ Como Funciona

O fluxo principal é composto por quatro etapas, realizadas por diferentes agentes:

1. **Identificação de Requisitos:** Análise inicial dos requisitos extraídos do documento.
2. **Análise Técnica ServiceNow:** Proposta de soluções técnicas alinhadas à plataforma.
3. **Desenvolvimento de Solução:** Detalhamento das ações técnicas e scripts necessários.
4. **Geração de Estórias de Usuário:** Criação de user stories completas e organizadas.

---

## ⚙️ Estrutura do Projeto

```
src/
  generate_sn_stories/
    config/
      agents.yaml      # Definições dos agentes (analista, especialista, PO)
      tasks.yaml       # Definição das tarefas e do fluxo de trabalho
    crew.py            # Lógica personalizada para orquestração dos agentes
    main.py            # Entrada principal e configuração dos inputs
.env                   # Variáveis de ambiente (ex: OPENAI_API_KEY)
README.md              # Este arquivo :)
```

---

## 📝 Pré-requisitos

- Python >= 3.10 e < 3.13
- [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências
- Chave da API OpenAI (para agentes baseados em LLM)

---

## 🛠️ Instalação

1. Instale o UV, caso não tenha:
   ```bash
   pip install uv
   ```

2. Instale as dependências do projeto:
   ```bash
   crewai install
   ```

3. Configure suas credenciais:
   - Adicione sua `OPENAI_API_KEY` ao arquivo `.env`.

---

## ▶️ Como Executar

Execute o pipeline principal:
```bash
crewai run
```

Outputs gerados em:
- `output/report.md` — Detalhamento técnico da solução ServiceNow
- `output/stories.md` — Lista de user stories geradas

---

## 🔧 Personalização

O projeto pode ser customizado através dos seguintes arquivos:

- `src/generate_sn_stories/config/agents.yaml`: Definição dos agentes e seus perfis.
- `src/generate_sn_stories/config/tasks.yaml`: Definição das tarefas, contexto e outputs.
- `src/generate_sn_stories/crew.py`: Lógica customizada, integração de ferramentas e manipulação de argumentos.
- `src/generate_sn_stories/main.py`: Inputs customizados e orquestração do fluxo.

---

## 📚 Documentação e Suporte

- [Documentação CrewAI](https://docs.crewai.com)
- [Repositório CrewAI](https://github.com/joaomdmoura/crewai)
- [Discord da Comunidade](https://discord.com/invite/X4JWnZnxPb)
- [Chat com a documentação](https://chatg.pt/DWjSBZn)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para abrir issues, enviar pull requests ou sugerir melhorias.

---

## 📝 Licença

Este projeto está sob a licença MIT.
