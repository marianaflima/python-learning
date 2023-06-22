'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
oessoas ainda não atingiram a maioridade e quantas já são maiores.
Maioridade = 21 anos
'''
from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for c in range(0,7):
    ano_nasc = int(input('Ano de Nascimento: '))
    if ano_atual - ano_nasc < 21:
        menores += 1
    else:
        maiores += 1

print(f'''
Maiores de idade: {maiores}
Menores de idade: {menores}
''') 