# Solução Atividade 7 – Cálculo de IMC
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / altura**2

if imc < 18.5:
    print(f"IMC {imc:.2f} – Abaixo do peso")
elif imc < 25:
    print(f"IMC {imc:.2f} – Peso ideal")
elif imc < 30:
    print(f"IMC {imc:.2f} – Sobrepeso")
elif imc < 40:
    print(f"IMC {imc:.2f} – Obesidade")
else:
    print(f"IMC {imc:.2f} – Obesidade mórbida")
