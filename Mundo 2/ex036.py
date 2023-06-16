#Variáveis
valor_casa = float(input('Digite o valor da casa: '))
sal_comprador = float(input('Digite seu salário: '))
tempo_pagamento = (int(input('Digite o tempo em anos que você irá pagar: '))) 
taxa_limite = sal_comprador * 0.3
valor_prestação = valor_casa / (tempo_pagamento * 12)

if valor_prestação > taxa_limite:
    print(f'\nDesculpe, essa operação não pode ser efetuada. \nO valor da prestação (R${valor_prestação:.2f}) excede 30% do seu salário')
else:
    print(f'\nEmpréstimo Concedido! \nValor da prestação: {valor_prestação:.2f}')