# Solução Atividade 9 – Analisador de triângulos
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"Triângulo válido – Tipo: {tipo}")
else:
    print("Não forma triângulo")
