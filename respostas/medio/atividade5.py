# Solução Atividade 5 – Alistamento Militar
from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano_nascimento

if idade < 18:
    print(f"Ainda vai se alistar. Faltam {18 - idade} anos")
elif idade == 18:
    print("Hora de se alistar!")
else:
    print(f"Já passou do tempo de alistamento por {idade - 18} anos")
