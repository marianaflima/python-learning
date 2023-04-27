from random import randint
from time import sleep

chose_num = randint(0, 5)
print('''
---------------------------------------------------------------------
|                       ADIVINHE O NÚMERO                           |
---------------------------------------------------------------------
''')
print('O computador escolheu um número de 0 a 5, descubra qual é!')

chute_num = int(input('Seu palpite: '))
print('PROCESSANDO...')
sleep(3)

if chute_num == chose_num:
    print('Parabéns! Você acertou!')
else:
    print(f'Que pena! Pensei no {chose_num} e não no {chute_num}.')