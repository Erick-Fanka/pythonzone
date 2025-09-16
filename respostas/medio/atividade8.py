# Solução Atividade 8 – Caixa eletrônico
valor = int(input("Digite o valor do saque: "))

cedulas = [50, 20, 10, 1]

for c in cedulas:
    qtd = valor // c
    valor %= c
    if qtd > 0:
        print(f"{qtd} cédula(s) de R${c}")
