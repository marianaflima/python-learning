nome = str(input('Digite seu nome:'))
nome1 = nome.split()[0] 
print(f'''
Seu nome em maiúsculas: {nome.upper()}
Seu nome em minúsculas: {nome.lower()}
Quantas letras: {len(nome) - nome.count(' ')}
Primeiro nome: {len(nome1)}''')
