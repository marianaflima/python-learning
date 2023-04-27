from time import sleep

print('''
------------------------------------------
|                  DETRAN                |
------------------------------------------''')

vel = int(input('Velocidade registrada (km/h): '))
print('PROCESSANDO...')
sleep(1.5)
print('-' * 20)
if vel >= 80:
    multa = float(7 * (vel - 80))
    print('Velocidade ultrapassada!')
    print(f'Multa: R${multa}')
else:
    print('Velocidade dentro dos limites!')
    print('Liberado pra passagem.')
print('-' * 20)