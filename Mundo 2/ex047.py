'''
Crie um programa que faça o computador jogar pedra, papel e tesoura com você
'''
from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
winner_player = 'VITÓRIA DO JOGADOR'
winner_cpu = 'VITÓRIA DO COMPUTADOR'

#inicio
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
op_player = int(input('DIGITE SUA OPÇÃO:'))

print('VEZ DO COMPUTADOR')
op_cpu = randint(0,2)
print('PROCESSANDO...')
sleep(1.5)

#processo
if op_player == op_cpu:
    msg_winner = 'EMPATE!'
else:
    if op_player == 0: #PEDRA
        if op_cpu == 1: #PAPEL
            msg_winner = winner_cpu
        elif op_cpu == 2: #TESOURA
            msg_winner = winner_player
    
    elif op_player == 1: #PAPEL
        if op_cpu == 0: #PEDRA
            msg_winner = winner_player
        elif op_cpu == 2: #TESOURA
            msg_winner = winner_cpu
    
    elif op_player == 2: #TESOURA
        if op_cpu == 0: #PEDRA
            msg_winner = winner_cpu
        elif op_cpu == 1: #PAPEL
            msg_winner = winner_player

#saída
print(f'''
RESULTADO:
{msg_winner}      
jogador: {itens[op_player]}
computador: {itens[op_cpu]}
''')
