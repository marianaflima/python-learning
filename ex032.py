from datetime import date

ano = int(input('Digite um ano ou digite 0 para verficar o ano atual: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) or (ano % 400 == 0):
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto')
