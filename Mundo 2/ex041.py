from datetime import date
print('''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |   CONFEDERAÇÃO NACIONAL DE NATAÇÃO    |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

ano = date.today().year
ano_nasc = int(input('ANO DE NASCIMENTO: '))
idade = ano - ano_nasc

if idade < 10:
    print('CATEORIA: MIRIM')
elif idade < 15:
    print('CATEGORIA: INFANTIL')
elif idade < 20:
    print('CATEGORIA: JUNIOR')
elif idade < 26:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')