'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média acima de 7.0: APROVADO
'''
n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
m = (n1 + n2) / 2

if m < 5:
    print('Aluno REPROVADO')
elif (m >= 5) and (m < 7):
    print('Aluno EM RECUPERAÇÃO')
else:
    print('Aluno APROVADO')