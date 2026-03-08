# =================================
# Exercício 12 - Desconto de 5%
# =================================

# -------- Minha solução --------
# Uso de 'preço' com cedilha no nome de variável (válido em Python 3, mas evitar)
preço = float(input('digite o valor  do produto que quer saber o desconto: r$'))
novo = preço - (preço * 5 / 100)
print('com {:.2f}R$, depois do desconto de 5% você obteve {:.2f}R$'.format(preço, novo))


# -------- Solução corrigida --------
preco = float(input('Digite o valor do produto: R$ '))
desconto = preco * 5 / 100
preco_final = preco - desconto
print('De R$ {:.2f}, com desconto de 5%, você paga R$ {:.2f}'.format(preco, preco_final))


