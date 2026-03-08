# =================================
# Exercício 10 - Conversão Real para Dólar
# =================================

# -------- Minha solução --------
r = float(input('quantos reais você tem na carteira?  r$'))
d = r / 3.27
print('seus {:.2f}R$ conseguem compras {:.2f}us'.format(r, d))


# -------- Solução corrigida --------
reais = float(input('Quantos reais você tem na carteira? R$ '))
cotacao = 3.27
dolares = reais / cotacao
print('Seus R$ {:.2f} equivalem a US$ {:.2f}'.format(reais, dolares))

