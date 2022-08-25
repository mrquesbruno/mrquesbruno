import emoji
import random
import time
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5= 5
lista = [n1,n2,n3,n4,n5]
lista2 = random.choice(lista)

print("\033[35m-- \033[m" * 19)
print(emoji.emojize("  \033[1;45mBEM VINDO AVENTUREIRO,AO JOGO DE ADIVNHAÇÃO!! :white_flower: \033[m"))
print("\033[35m-- \033[m" * 19)
num = int(input("\033[35mEscolha um número de 1 a 5 e boa sorte!: \033[m"))
print("\033[35mSerá que você acertou?...\033[m")
time.sleep(2)  #determina um tempo de espera do computador pra dar a resposta
if num == lista2:
    print("\033[32m Parabéns!! Você acertou o número de hoje!!! \033[m")
else:
    print("\033[31m Que pena aventureiro,mas tente novamente. \033[m")
    print("\033[35mO número da vez era {}.\033[m".format(lista2))
