'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
30% do salário ou então o empréstimo será negado.
'''
#Variáveis
valor_casa = float(input('Digite o valor da casa: '))
sal_comprador = float(input('Digite seu salário: '))
tempo_pagamento = (int(input('Digite o tempo em anos que você irá pagar: '))) 
taxa_limite = sal_comprador * 0.3

#Código
valor_prestação = valor_casa / (tempo_pagamento * 12)

if valor_prestação > taxa_limite:
    print('\nDesculpe, essa operação não pode ser efetuada. \nO valor da prestação excede 30% do seu salário')
else:
    print(f'Valor da prestação: {valor_prestação:.2f}')