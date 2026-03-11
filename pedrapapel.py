
import random
opçôes = ["pedra", "papel", "tesoura"]


try: 

    jogador1 = input("Digite pedra, papel ou tesoura: ").lower()
    computador = random.choice (opçôes)  
    print(computador)
    if jogador1 == "pedra" and computador == "tesoura":
        print("Ganhou pedra ", )
    if jogador1 == "papel" and computador == "pedra" :
        print("Gamhou papel ", )
    elif jogador1 == "tesoura" and computador == "papel" :
        print ("Ganha tesoura " ,)
    elif jogador1 == computador:
        print ("Empate")
    elif jogador1 in ["pedra", "papel", "tesoura"] and computador in ["pedra", "papel", "tesoura"]:
        print ("Ganha computador")

except SyntaxError or ValueError:
    print ("Não existe essa opção. ")
