# =================================
# Exercício 15 - Aluguel de carro
# =================================

# -------- Minha solução --------
dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
pago = (60 * dias) + (km * 0.15)
print('o total a se pagar e de {:.2f}'.format(pago))


# -------- Solução corrigida --------
# R$60 por dia + R$0,15 por km rodado
dias = int(input('Quantos dias alugados? '))
km   = float(input('Quantos km rodados? '))
total = (60 * dias) + (km * 0.15)
print('O total a pagar é R$ {:.2f}'.format(total))
