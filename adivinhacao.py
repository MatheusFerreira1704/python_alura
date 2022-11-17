import random

# Joguiniho para se adaptar a linguagem
def jogar():
    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    num_secreto = random.randrange(1,101)
    numero_tentativas = 0
    rodada = 1
    pontos = 100

    # Input sempre devolve uma instring, por esse motivo é necessário "tipar" o input.
    #Declarar variasveis para deixar o código mais legivel
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina um nível: "))

    #Tratamento adicionado por mim caso o usario force um erro, digitando um número que não esteja entre 1 e 3.
    while(nivel < 1 or nivel > 3):
        print("Digite um número válido, entre 1 e 3.")
        nivel = int(input("Defina um nível: "))

    if (nivel == 1):
        numero_tentativas = 20
    elif (nivel == 2):
        numero_tentativas = 10
    elif (nivel == 3):
        numero_tentativas = 5
    else:
        print("Digite um número entre 1 e 3")

    for rodada in range(1, numero_tentativas + 1):

        print(f"Tentativa {rodada} de {numero_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue # Continua no laço, mas invalida a etapa.
        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if (acertou):
            print("PARABÉNS! Você acertou.")
            print(f"Sua pontuação foi de {pontos}")
            break # Utilizado para sair do laço
        else:
            pontos_perdidos = abs(chute - num_secreto)
            pontos = abs(pontos_perdidos - pontos)
            if (maior):
                print("Você errou, seu chute foi maior que o número secreto.")
                if (rodada == numero_tentativas):
                    print(f"O numero secreto era {num_secreto}. Sua pontunção foi: {pontos}")
            elif (menor):
                print("Você errou, seu chute foi menor que o número secreto.")
                if (rodada == numero_tentativas):
                    print(f"O numero secreto era {num_secreto}. Sua pontunção foi: {pontos}")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()