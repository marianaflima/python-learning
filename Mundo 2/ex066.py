'''
Crie um programa que leai vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No
final, mostre quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando a flag).
'''

n = 0
soma = 0
c = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    c += 1

print('Soma:', soma)
print('Nº de valores lidos:', c)
