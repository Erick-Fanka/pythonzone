# Solução Atividade 6 – Validação de dados
while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo in ["M", "F"]:
        print(f"Sexo válido: {sexo}")
        break
    print("Valor inválido! Digite novamente.")
