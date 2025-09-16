# Solução Atividade 6 – Aprovação de empréstimo
valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário: "))
anos = int(input("Quantidade de anos para pagar: "))

prestacao = valor_casa / (anos * 12)

if prestacao <= salario * 0.3:
    print(f"Empréstimo aprovado! Prestação: R${prestacao:.2f}")
else:
    print(f"Empréstimo negado! Prestação: R${prestacao:.2f} excede 30% do salário")
