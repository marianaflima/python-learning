'''
faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menor peso lidos.
'''

pesos = []
for c in range(0,5):
    peso = float(input('Digite seu peso (KG): '))
    pesos.append(peso)

print(f'''
Peso máximo: {max(pesos)}
Peso mínimo: {min(pesos)}      
      ''')