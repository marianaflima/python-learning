from random import choice

alunos = 1
lista = []
while alunos <= 5:
    nome = str(input(f'Digite o nome do {alunos}º aluno: '))
    lista.append(nome)
    alunos += 1

print(f'O aluno escolhido foi: {(choice(lista))}')