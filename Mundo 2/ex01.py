# =================================
# Exercício ex1 - Financiamento de casa (30% do salário)
# =================================

# -------- Minha solução --------
casa = float(input('digite o valor da casa: R$'))
salario = float(input('quantos você recebe: R$'))
anos = int(input('pretende pagar a casa em quantos anos?'))
messe = casa / (anos * 12)
porcen = salario * 30 / 100
if messe > porcen:
    print('\033[31mCOMPRA NEGADA')
    print('você não pode compra essa casa')
else:
    print('\033[32mCOMPRA APROVADA, PARABENS!')
    print('você vai pagar R${:.2F} por mês'.format(messe))   # Erro: .2F


# -------- Solução corrigida --------
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

parcela = casa / (anos * 12)
limite = salario * 0.30   # máximo 30% do salário

if parcela > limite:
    print('\033[31mCOMPRA NEGADA\033[m')
    print('Parcela R$ {:.2f} > 30% do salário R$ {:.2f}'.format(parcela, limite))
else:
    print('\033[32mCOMPRA APROVADA!\033[m')
    print('Você pagará R$ {:.2f} por mês'.format(parcela))
