from random import shuffle

alunos = 1
lista = []

while alunos <= 5:
    nome = str(input(f'Nome do {alunos}º aluno: '))
    lista.append(nome)
    alunos += 1

shuffle(lista)
print(f'A ordem de aprensentação é {lista}')