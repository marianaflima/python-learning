'''
- Apos a sopa
- A sacada da casa
- A torre da derrota
- O lobo ama o bolo
- Anotaram a data da maratona
'''

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letras in range((len(frase) - 1), -1, -1):
    inverso += junto[letras]

if inverso == junto:
    print('A frase É palíndroma!')
else:
    print('A frase NÃO É palíndroma')