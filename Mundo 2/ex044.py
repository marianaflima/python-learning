preço = float(input('VALOR: R$'))

print('''[1] À VISTA (DINHEIRO/PIX)
[2] À VISTA (CARTÃO)
[3] 2x - CARTÃO
[4] 3x OU MAIS - CARTÃO ''')

forma_pag = int(input('FORMA DE PAGAMENTO: '))

if forma_pag == 1:
    valor_final = preço * 0.9
elif forma_pag == 2:
    valor_final = preço * 0.95
elif forma_pag == 3:
    valor_final = preço
    parcelas = preço / 2
    msg = 'Mesmo valor'
elif forma_pag == 4:
    n_parcelas = int(input('Nº PARCELAS: '))
    parcelas = (preço / n_parcelas) + preço * 0.2
    valor_final = preço
else:
    print('ERRO! Digite uma opção válida.')

print(f'\nVALOR DA COMPRA:{preço}')
print(f'VALOR FINAL: {valor_final}')
if forma_pag == 3 or forma_pag == 4:
    print(f'PARCELAS: {parcelas}')
