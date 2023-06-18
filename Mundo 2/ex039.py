from datetime import date

ano = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano - ano_nasc

print('SITUAÇÃO: ')

if idade < 18:
    print('AINDA VAI SE ALISTAR')
    saldo = ano + (18 - idade)
    print(f'ANO PRA SE ALISTAR: {saldo}')
elif idade == 18:
    print('É HORA DE SE ALISTAR')
else:
    print('JÁ PASSOU O TEMPO')
    saldo = ano - (idade - 18)
    print(f'ANO DE ALISTAMENTO: {saldo}')