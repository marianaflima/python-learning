
h = float(input('ALTURA (M): '))
p = float(input('PESO (KG): '))

imc = p / pow(h, 2)
print(f'IMC: {imc:.2f}')

if imc < 18.6:
    print('SITUAÇÃO: ABAIXO DO PESO')
elif imc < 25.1:
    print('SITUAÇÃO: PESO IDEAL')
elif imc < 30.1:
    print('SITUAÇÃO: SOBREPESO')
elif imc < 40.1:
    print('SITUAÇÃO: OBESIDADE')
else:
    print('SITUAÇÃO: OBESIDADE MÓRBIDA')