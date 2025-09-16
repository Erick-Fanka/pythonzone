# Solução Atividade 4 – Verificador de vogal
letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")
