'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
final, mostre:

a) quantas pessoas são maiores de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos
'''

c = 0
maiores_18 = 0
homens = 0
mulheres_menores_20 = 0
while True:
    c += 1
    print(f'''
PESSOA {c}''')
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [Masculino/Feminino]: ')).strip().upper().split()
    while sexo[0][0] not in 'MF':
        sexo = str(input('Opção inválida! Digite seu sexo [Masculino/Feminino]: ')).strip().upper().split()
    
    if sexo[0][0] == 'M':
        homens += 1
    if idade >= 18:
        maiores_18 += 1
    if sexo[0][0] == 'F' and idade < 20:
        mulheres_menores_20 += 1
    quer_continuar = str(input('Quer continuar [SIM/NÃO]? ')).upper().split()
    if quer_continuar[0][0] == 'N':
        break

print(f'''
Maiores de 18: {maiores_18}
Homens cadastrados: {homens}
Mulheres menores de 20: {mulheres_menores_20}
''')