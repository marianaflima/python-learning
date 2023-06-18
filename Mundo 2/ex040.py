n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
m = (n1 + n2) / 2

print(f'MÉDIA: {m}')
if m < 5:
    print('Aluno REPROVADO')
elif (m >= 5) and (m < 7):
    print('Aluno EM RECUPERAÇÃO')
else:
    print('Aluno APROVADO')