from random import randint #é o comando para escolher um número aleatório
from time import sleep #faz o computador 'dormir'e esperar alguns segundos para responder o restante do cod.
num = randint(0, 5) #faz o computador 'pensar
print('*'*60)
print('Vou pensar em um número entre 0 e 5, tente adivinhar..')
print('*'*60)
jogador = int(input('Em que número eu pensei?')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(4) #o número que colocar dentro do parenteses representa quantos seg.
if jogador == num:
    print('Parabens você acertou, eu pensei em {}'.format(num))
else:
    print('Errou, eu pensei em {}'.format(num))
