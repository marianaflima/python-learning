from datetime import date
ano = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano - ano_nasc

print('SITUAÇÃO: ')

if idade < 18:
    print('AINDA VAI SE ALISTAR')
    print(f'TEMPO ATÉ SE ALISTAR: {(18 - idade)} anos')
elif idade == 18:
    print('É HORA DE SE ALISTAR')
else:
    print('JÁ PASSOU O TEMPO')
    print(f'TEMPO DESDE ALISTAMENTO: {idade - 18} anos')