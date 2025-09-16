# Solução Atividade 4 – Maior e menor da sequência
pesos = []

for i in range(5):
    peso = float(input(f"Peso da {i+1}ª pessoa: "))
    pesos.append(peso)

print(f"Maior peso: {max(pesos)}")
print(f"Menor peso: {min(pesos)}")
