# Solução Atividade 5 – Análise de dados
pessoas = []

for i in range(4):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

media_idade = sum(p["idade"] for p in pessoas) / len(pessoas)
homem_mais_velho = max([p for p in pessoas if p["sexo"] == "M"], key=lambda x: x["idade"], default=None)
mulheres_menos_20 = sum(1 for p in pessoas if p["sexo"] == "F" and p["idade"] < 20)

print(f"Média de idade: {media_idade:.2f}")
if homem_mais_velho:
    print(f"Homem mais velho: {homem_mais_velho['nome']}")
print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")
