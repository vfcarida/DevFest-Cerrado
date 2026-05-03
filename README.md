# 🚀 DevFest-Cerrado 2024 - GenAI Masterclass

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/Google-Gemini_API-FDBA18.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Palestra:** Desvendando a GenAI: Da Teoria às Aplicações com Gemini e Gemma
> **Evento:** [DevFest Cerrado 2024](https://devfestcerrado.com.br/)
> **Autor:** Vinicius Caridá

Bem-vindo ao repositório oficial da masterclass sobre Inteligência Artificial Generativa ministrada no DevFest Cerrado 2024! Este projeto explora as aplicações mais avançadas em modelos de linguagem utilizando a família de modelos **Gemini** (Cloud) e **Gemma** (Open-weights), indo desde os fundamentos teóricos até implementações práticas (Multimodalidade, RAG e Prompt Engineering).

---

## 🏛️ Estrutura do Projeto (Refatorada)

Para garantir qualidade, escalabilidade e manutenibilidade, este repositório segue padrões de Engenharia de Software e *Clean Architecture*.

```text
DevFest-Cerrado/
├── docs/                # Material auxiliar (PDF da apresentação)
├── notebooks/           # Notebooks interativos com o conteúdo prático
├── src/                 # Código central reusável (Python scripts)
│   ├── config.py        # Gestão de variáveis de ambiente e loggers
│   ├── llm_client.py    # Abstração de cliente para a API do Gemini
│   └── rag_utils.py     # Lógicas de processamento para RAG (Embeddings, Vector Search)
├── tests/               # Testes unitários do código (Pytest)
├── pyproject.toml       # Dependências e empacotamento moderno
├── requirements.txt     # Alternativa para instação simples com Pip
└── README.md            # Este arquivo
```

---

## 💻 Notebooks Disponíveis

Na pasta `notebooks/`, você encontrará os seguintes laboratórios práticos:

1. **`01_Demo_Gemma.ipynb`:** Demonstração inicial de uso dos modelos Gemma locais.
2. **`02_RAG_Gemma_2B.ipynb`:** Implementação completa de Geração Aumentada por Recuperação (RAG) com Gemma 2B.
3. **`03_Test_GenAI.ipynb`:** Testes de desempenho e experimentação inicial de IA.
4. **`04_Intro_Multimodal.ipynb`:** Casos de uso de análise simultânea de texto, imagens e vídeos usando o Gemini.
5. **`05_Prompt_Engineering_Gemini.ipynb`:** Melhores práticas de engenharia de prompt para obter os resultados desejados.
6. **`06_Primeiros_Passos_PaliGemma.ipynb`:** Utilizando o modelo PaliGemma para tarefas avançadas de visão-linguagem.

---

## ⚙️ Instalação Passo a Passo

Para reproduzir os notebooks ou utilizar os módulos do `src/` em seus próprios projetos, siga as instruções abaixo:

### 1. Clonar e configurar ambiente
```bash
git clone https://github.com/vfcarida/DevFest-Cerrado.git
cd DevFest-Cerrado

# Criar ambiente virtual
python -m venv venv

# Windows
.\venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

### 2. Instalação das dependências
Você pode instalar usando o arquivo moderno de projeto:
```bash
pip install -e .[dev]
```
Ou pelo clássico:
```bash
pip install -r requirements.txt
```

### 3. Configurar API Keys
Renomeie o arquivo de exemplo de ambiente e insira a sua chave da API do Google (obtenha em [Google AI Studio](https://aistudio.google.com/)):
```bash
cp .env.example .env
```
Abra o arquivo `.env` e defina sua chave:
```env
GEMINI_API_KEY=sua_chave_secreta_aqui
```

---

## 🧪 Rodando os Testes

Para garantir que tudo está funcionando perfeitamente (os componentes do `src/`), execute:
```bash
pytest tests/
```

---

## 🤝 Contribuições
Sinta-se à vontade para expandir os laboratórios! Leia o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para saber como enviar um Pull Request, seguir os padrões de formatação e reportar issues.

---
*Apresentado no DevFest Cerrado 2024.*
