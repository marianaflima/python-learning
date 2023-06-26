'''
faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menor peso lidos.
'''

maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Digite seu peso (KG): '))
    if c == 0:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso


print(f'''
Peso máximo: {maior}
Peso mínimo: {menor}      
      ''')