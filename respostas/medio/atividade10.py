# Solução Atividade 10 – Pedra, Papel e Tesoura
import random

jogador = input("Escolha Pedra, Papel ou Tesoura: ").lower()
opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice(opcoes)

print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")
