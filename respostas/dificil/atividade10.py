# Solução Atividade 10 – Dicionário de aluno
aluno = {}
aluno["nome"] = input("Nome: ")
aluno["media"] = float(input("Média: "))

if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

print(aluno)
