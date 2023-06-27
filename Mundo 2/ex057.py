'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite valores
como 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter
o valor correto
'''
sex = ''
while 'MF' not in sex:
    sex = str(input('Digite seu sexo [M/F]: ')).upper()
    if sex not in 'MF':
        print('Digite uma opção válida!!')
        print('')
    else:
        if sex == 'M':
            print('Sexo: Masculino')
        elif sex == 'F':
            print('Sexo: Feminino')
        break