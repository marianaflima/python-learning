'''
Melhore o jogo do exercício 28 onde o computador vai "pensar" em um número entre
0 e 10. Só que agora o jogador vai adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
c = 0
cpu = 0
player = 1
print('O COMPUTADOR PENSOU EM UM NÚMERO de 0 a 10!')
print('Tente adivinhar!')

while cpu != player:
    c += 1
    cpu = randint(0, 10)
    player = int(input('Seu palpite (0 a 10): '))
    sleep(1.5)
    if cpu == player:
        
        print(f'''
Amém! Você acertou!
CPU: {cpu}
Você: {player}''')
        print(f'Você precisou de {c} tentativas para acertar.')
        break
    else:
        print(f'''
ERROU! 
CPU: {cpu}
Você: {player}
Tente novamente!''')
