'''
Escreva um número que compare dois núemros inteiros e compare-os, mostrando na
tela uma mensagem: 
- O primeiro valor é o maior
- O segundo vallor é o maior
- Não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro é maior que o segundo')
elif n2 > n1:
    print('O segundo é maior que o primeiro')
else:
    print('Não existe MAIOR. Os dois são IGUAIS.')