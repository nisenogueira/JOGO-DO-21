#biblitecas utilizadas 
import random
from time import sleep

#apresentação d jogo
print("""=== JOGO DO 21 ===
O jogo lhe dará um número,entre 1 a 10 e você decide se continua ou não, a cada rodada esse número será somado.
O objetivo é marcar 21 pontos ou o mais próximo possível sem ultrapassar esse valor.""")
#temporizador para iniciar o jogo dando alguns segundos para o jogador ler a apresentação
sleep(2)
print("*")
sleep(1)
print("**")
sleep(1)
print("***")
sleep(2)

#função para iniciar o jogo
def jogo_21():
    pontos_jogador = 0 
    continuar_jogando = True  
    while pontos_jogador < 21 and continuar_jogando:
        if pontos_jogador == 0:
            escolha_jogador = input("Podemos começar? [S/N] ")
        
        else:
            escolha_jogador = input("Gostaria de continuar? [S/N] ")

        if escolha_jogador.upper() == "S":
            numero = random.randint(1, 10)
            sleep(1)
            print(f"Você recebeu um {numero}")
            pontos_jogador += numero
            print(f"Sua pontuação atual é {pontos_jogador}.")
            sleep(2)
        elif escolha_jogador.upper() == "N":
            continuar_jogando = False
        else:
            print("Escolha inválida. Por favor, digite S ou N.")
    if pontos_jogador == 21:
        print("Parabéns! Você ganhou!")
        sleep(10)
    elif pontos_jogador > 21:
        print("Você perdeu!. Mais sorte na próxima =P")
        sleep(10)
    else:
        print(f"Você parou com uma pontuação abaixo de 21.")
        sleep(10)
#chamada da funcão para que o código (o jogo) inicie
jogo_21()
