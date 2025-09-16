# Solução Atividade 11 – Unindo listas
numeros = []
pares = []
impares = []

while True:
    n = int(input("Digite um número: "))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    cont = input("Deseja continuar? (S/N): ").upper()
    if cont != "S":
        break

print("Todos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
