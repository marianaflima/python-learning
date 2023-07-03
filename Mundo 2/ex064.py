'''
Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag)
'''
n = 0
soma = 0
c = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    soma += n

print(f'''
- FIM! -
Números digitados: {c}
Soma dos números: {soma}
''')
