import forca
import adivinhacao

print("**********************************")
print("*********** Bem vindo ************")
print("******* Escolha seu jogo *********")
print()

print("(1) Forca (2) Adivinhação")
escolha = int(input("Qual jogo deseja jogar? "))


# Tratamento de erro
while(escolha < 1 or escolha > 2):
        print("Digite um número válido, entre 1 e 2.")
        escolha = int(input("Qual jogo deseja jogar? "))

if(escolha == 1):
    forca.jogar()
elif(escolha == 2):
    adivinhacao.jogar()
