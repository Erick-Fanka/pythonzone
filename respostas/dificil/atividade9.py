# Solução Atividade 9 – Cadastro de pessoas com lista
pessoas = []
while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    pessoas.append({"nome": nome, "peso": peso})
    cont = input("Deseja continuar? (S/N): ").upper()
    if cont != "S":
        break

maior_peso = max(p["peso"] for p in pessoas)
menor_peso = min(p["peso"] for p in pessoas)

print(f"Pessoas mais pesadas:")
for p in pessoas:
    if p["peso"] == maior_peso:
        print(p["nome"], p["peso"])

print(f"Pessoas mais leves:")
for p in pessoas:
    if p["peso"] == menor_peso:
        print(p["nome"], p["peso"])
