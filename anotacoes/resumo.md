# 📌 Resumo de Conceitos Básicos do Python

## 🔹 Sintaxe e Estrutura

* **Indentação**: define blocos de código (não usa `{}` como em outras linguagens).
* **Comentários**:

  * `# comentário de uma linha`
  * `""" comentário de várias linhas """`
* **Case-sensitive**: `variavel`, `Variavel` e `VARIAVEL` são diferentes.
* **Parênteses**: usados em expressões, definição de funções e chamadas.

---

## 🔹 Tipos de Dados Básicos

* **Inteiros (`int`)** → `idade = 25`
* **Flutuantes (`float`)** → `altura = 1.75`
* **Strings (`str`)** → `"Olá"`, `'Mundo'`
* **Booleanos (`bool`)** → `True`, `False`

---

## 🔹 Variáveis

* Criadas com `=` (atribuição).
* Python infere o tipo automaticamente.
* Exemplo:

  ```python
  nome = "João"
  idade = 25
  altura = 1.75
  estudante = True
  ```
* **Atribuição múltipla**: `a = b = c = 10`

**Regras para nomes de variáveis**:
✅ Podem conter letras, números e `_`
❌ Não podem começar com número
❌ Não podem usar palavras reservadas (`if`, `for`, etc.)
✅ Usar nomes descritivos: `nome_completo`, `total_vendas`

---

## 🔹 Operadores

### Aritméticos

* `+` soma
* `-` subtração
* `*` multiplicação
* `/` divisão (float)
* `//` divisão inteira
* `%` módulo (resto)
* `**` potência

### Comparação

* `==` igual
* `!=` diferente
* `>` maior que
* `<` menor que
* `>=` maior ou igual
* `<=` menor ou igual

### Lógicos

* `and` → True se **ambos** forem verdadeiros
* `or` → True se **um** for verdadeiro
* `not` → inverte valor lógico

---

## 🔹 Estruturas de Controle

### Condicionais

```python
if condicao:
    ...
elif outra_condicao:
    ...
else:
    ...
```

### Loops

* **For**: percorre listas, strings ou ranges

  ```python
  for fruta in ["maçã", "banana"]:
      print(fruta)
  ```
* **While**: executa enquanto a condição for verdadeira

  ```python
  contador = 0
  while contador < 5:
      print(contador)
      contador += 1
  ```

### Controle de loops

* `break` → encerra o loop
* `continue` → pula para a próxima iteração
* `pass` → não faz nada (placeholder)

---

## 🔹 Estruturas de Dados

### Listas (`list`)

* Mutáveis, ordenadas, aceitam valores repetidos.
* Métodos principais:

  * `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`
* **List comprehension**:

  ```python
  numeros = [x**2 for x in range(5)]
  ```

### Tuplas (`tuple`)

* Imutáveis, ordenadas.
* Úteis para valores que não devem mudar.
* Exemplo: `cores = ("azul", "verde", "vermelho")`

### Dicionários (`dict`)

* Estrutura chave-valor.
* Exemplo:

  ```python
  pessoa = {"nome": "Ana", "idade": 20}
  print(pessoa["nome"])
  ```

### Conjuntos (`set`)

* Não ordenados, não aceitam valores duplicados.
* Úteis para operações matemáticas de conjuntos: união, interseção.
* Exemplo: `conjunto = {1, 2, 3}`

---

## 🔹 Funções

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))
```

* Argumentos podem ter valores padrão:

  ```python
  ```

def somar(a, b=10):
return a + b

````

---

## 🔹 Entrada e Saída
- **Entrada**: `input("Digite seu nome: ")` → retorna string.  
- **Saída**: `print("Olá")`  

---

## 🔹 Manipulação de Strings
- Métodos comuns:  
- `upper()`, `lower()`, `capitalize()`, `strip()`, `replace()`  
- `split()`, `join()`  
- Fatiamento:  
```python
texto = "Python"
print(texto[0:3])  # Pyt
````

---

## 🔹 Módulos e Bibliotecas

* **Importação**:

  ```python
  import math
  print(math.sqrt(16))
  ```
* **Import específico**:

  ```python
  from math import sqrt
  ```

---

## 🔹 Tratamento de Erros

```python
try:
    numero = int("abc")
except ValueError:
    print("Erro: valor inválido")
finally:
    print("Fim do programa")
```

---

✅ Este resumo cobre os principais fundamentos de **Python Básico** para iniciantes.
