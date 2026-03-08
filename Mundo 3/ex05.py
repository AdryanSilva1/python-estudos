# =================================
# Exercício ex05 - Listagem de preços com tupla (nome + preço alternados)
# =================================

# -------- Minha solução --------

listagem = ('Notebook', 3500, 'Smartphone', 2500, 'Fone de Ouvido', 200,
            'Teclado Mecânico', 300, 'Monitor', 900, 'Mouse Gamer', 150,
            'Cadeira Ergonômica', 1200, 'Mochila para Notebook', 180,
            'HD Externo 1TB', 400, 'Impressora Multifuncional', 800)

print('LSITAGEM DE PREÇO'.center(40))   
print('-' * 40)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end=' ')
    else:
        print(f'R${listagem[item]:>7.2f}')


# -------- Solução corrigida --------
listagem = ('Notebook', 3500, 'Smartphone', 2500, 'Fone de Ouvido', 200,
            'Teclado Mecânico', 300, 'Monitor 24"', 900, 'Mouse Gamer', 150,
            'Cadeira Ergonômica', 1200, 'Mochila para Notebook', 180,
            'HD Externo 1TB', 400, 'Impressora Multifuncional', 800)

print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<30} R$ {listagem[i + 1]:>7.2f}')
print('-' * 40)

