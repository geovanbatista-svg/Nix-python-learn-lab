# Nix + Python Learning Lab

Este repositório documenta minha prática de aprendizado em programação,
utilizando Nix como uma ferramenta para desenvolver raciocínio funcional
e comparar conceitos com Python.

A proposta não é apenas escrever código funcional, mas entender como
operações como map, filter, composição de funções e transformação de
dados se manifestam em linguagens diferentes.

Cada exercício possui versões em Nix e Python, acompanhadas de
documentação explicativa quando necessário.


---

## Objetivo principal

- Aprender **Nix** como linguagem declarativa e funcional
- Usar **Python** como linguagem de execução e prática
- Comparar:
  - imperativo × declarativo
  - estado mutável × imutabilidade
  - funções × POO
- Desenvolver clareza antes de complexidade

---

## Metodologia de aprendizado

Para cada problema:

1. Implemento a lógica em **Python**
2. Reescrevo a mesma ideia em **Nix**
3. Comparo:
   - como os dados são transformados
   - como o resultado é obtido
   - o impacto do estado mutável
4. Documento o raciocínio em `notes.md`

---

## Estrutura do repositório

### `basics/`
Fundamentos de listas e funções:
- Calcular tamanho de lista
- Soma de lista
- Filtro de lista
- Verificar elemento presente em lista

### `functions/`
Criação e uso de funções:
- Funções simples
- Funções de soma
- Composição de funções

### `packages/`
Estudos focados em Nix:
- Criação de repositório local de pacotes
- Geração de pacotes a partir de expressões Nix

### `comparisons/`
Comparações diretas:
- Python vs Nix
- Imperativo vs Funcional
- Funções vs POO

---

## Exemplo de comparação

### Python (imperativo / funcional)
```python
def filter_list(condition, lst):
    return [x for x in lst if condition(x)]
