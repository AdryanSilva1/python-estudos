# =================================
# Exercício ex35 - Controle de compras: total, produtos >= R$1000, produto mais barato
# =================================

# -------- Minha solução -------
total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))

    cont += 1
    total += preco

    if totmil >= 1000:   # Erro: compara contador com 1000, nunca verdadeiro
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? ')).strip().upper()[0]

    if resp == 'N':
        break

print('{:-^40}'.format(' fim do programa '))
print(f'O total de sua compra foi R${total:.2f}')
print(f'em sua compra tem {totmil} produtos custando R$1000')
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')   


# -------- Solução corrigida --------
total = 0
totmil = 0
menor_preco = None
produto_barato = ''
cont = 0

while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco

    if preco >= 1000:    # corrigido: verifica o preço
        totmil += 1

    if menor_preco is None or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    resp = ''
    while resp not in ('S', 'N'):
        resp = input('Continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break

print('{:-^40}'.format(' Fim do programa '))
print(f'Total da compra      : R$ {total:.2f}')
print(f'Produtos >= R$1000   : {totmil}')
print(f'Produto mais barato  : {produto_barato} (R$ {menor_preco:.2f})')

