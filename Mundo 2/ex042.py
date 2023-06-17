'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
- EQUILÁTERO: Todos os lados iguais
- ISÓSCELES: Dois lados iguais
- ESCALENO: Todos os lados diferentes
'''
c = 0
lista = []

while c != 3:
    lado = int(input(f'Digite o {c + 1}º lado: '))
    lista.append(lado)
    c += 1

a = lista [0]
b = lista[1]
c = lista[2]

if a > b + c and b > a + c and c > a + b:
    print('FORMAM TRIÂNGULO')
    if a == b and b == c:
        print('TIPO DE TRIÂNGULO: EQUILÁTERO')
    elif a == b or b == c and a != c:
        print('TIPO DE TRIÂNGULO: ISÓSCELES')
    else:
        print('TIPO DE TRIÂNGULO: ESCALENO')