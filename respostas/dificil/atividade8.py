# Solução Atividade 8 – Contando vogais em tupla
palavras = ("python", "programacao", "dados", "desenvolvimento")
for palavra in palavras:
    vogais = [letra for letra in palavra if letra.lower() in "aeiou"]
    print(f"{palavra}: Vogais -> {vogais}")
