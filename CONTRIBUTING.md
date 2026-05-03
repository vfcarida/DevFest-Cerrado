# Guia de Contribuição

Obrigado pelo seu interesse em contribuir para o **DevFest-Cerrado GenAI Masterclass**! Nós encorajamos melhorias nos notebooks, correções no material de apresentação e otimizações nos scripts do pacote `src`.

## 🛠️ Como Contribuir

### 1. Relatando Bugs (Issues)
Se encontrar um bug em algum notebook ou script:
- Verifique se a *issue* já não foi reportada por outra pessoa.
- Crie uma *Issue* contendo o máximo de detalhes possível: logs de erro, versões das bibliotecas instaladas e passos para reproduzir o problema.

### 2. Contribuindo com Código / Novos Notebooks
1. **Faça um Fork** deste repositório.
2. **Crie uma branch** para a sua modificação:
   ```bash
   git checkout -b feature/minha-nova-funcionalidade
   ```
3. **Desenvolva** a funcionalidade. 
   - Se for uma modificação em código Python da pasta `src/`, escreva testes unitários em `tests/`.
   - Se for um novo notebook, salve-o em `notebooks/` com um nome padronizado.
4. **Verifique** a estabilidade:
   ```bash
   pytest tests/
   black src/ tests/
   ```
5. **Faça o Commit** e o Push para o seu fork:
   ```bash
   git commit -m "feat: adicionando novo notebook sobre embeddings"
   git push origin feature/minha-nova-funcionalidade
   ```
6. Abra um **Pull Request (PR)** descrevendo as alterações.

## Padrões de Código
- Utilizamos o **Clean Code** e os princípios **SOLID**.
- Utilizamos **Type Hinting** obrigatório para funções.
- Utilizamos **Docstrings** para documentar classes e funções públicas do Python.
- Formatamos o código com a ferramenta `black`.
