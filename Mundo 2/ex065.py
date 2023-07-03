'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
yes_no = str(input('Quer ler um número [S/N]: ')).upper()
menor = maior = c = soma = 0

while yes_no != 'N':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    yes_no = str(input('Quer ler um número [S/N]: ')).upper()

print(f'''
Média: {soma / c}
Maior nº: {maior}
Menor nº: {menor}
''')