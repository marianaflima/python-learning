'''
Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''

nomes = []
idades = []
sexos = []
mul_menos_20 = 0


for c in range(0, 4):
    nome = str(input('NOME: '))
    nomes.append(nome)
    idade = int(input('IDADE: '))
    idades.append(idade)
    sexo = str(input('SEXO: ')).upper()
    sexos.append(sexo)
    if sexo == 'F' and idade < 20:
        mul_menos_20 += 1
    elif sexo == 'M' and idade == max(idades):
        hom_mais_velho = nome

print(f'''
Média de idade: {sum(idades)/len(idades)}
Homem mais velho: {hom_mais_velho}
Nº de mulher de menor: {mul_menos_20}
      ''')

