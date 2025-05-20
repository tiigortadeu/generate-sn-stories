# generate-sn-stories

Sistema automatizado para processamento de PDFs e extração de informações para associação com incidentes, utilizando a framework [crewAI](https://crewai.com).

## Sobre o Projeto

Este projeto utiliza Python e CrewAI para:
- Receber arquivos PDF como entrada
- Identificar e extrair conteúdo relevante
- Associar informações extraídas a incidentes
- Automatizar o processo de análise documental

## Requisitos

- Python >=3.10 <3.13
- [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências

## Instalação

1. Instale o UV (se ainda não tiver):
```bash
pip install uv
```

2. Instale as dependências do projeto:
```bash
crewai install
```

3. Configure suas credenciais:
- Adicione sua `OPENAI_API_KEY` no arquivo `.env`

## Como Executar

Para rodar o projeto:
```bash
crewai run
```

## Configuração e Personalização

O projeto pode ser customizado através dos seguintes arquivos:

- `src/generate_sn_stories/config/agents.yaml`: Definição dos agentes
- `src/generate_sn_stories/config/tasks.yaml`: Definição das tarefas
- `src/generate_sn_stories/crew.py`: Lógica personalizada, ferramentas e argumentos específicos
- `src/generate_sn_stories/main.py`: Inputs customizados para agentes e tarefas

## Suporte

Para suporte ou dúvidas:
- [Documentação CrewAI](https://docs.crewai.com)
- [GitHub do CrewAI](https://github.com/joaomdmoura/crewai)
- [Discord da Comunidade](https://discord.com/invite/X4JWnZnxPb)
- [Chat com a documentação](https://chatg.pt/DWjSBZn) 