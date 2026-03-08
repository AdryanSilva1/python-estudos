# =================================
# Exercício 13 - Aumento de salário 15%
# =================================

# -------- Minha solução --------
s = float(input('digite o salario para calcular o aumento: R$'))
sn = s + (s * 15 / 100)
print('seu salario de {:.2f}R$, com o aumento de 15%,ficou {:.2f}R$'.format(s, sn))


# -------- Solução corrigida --------
salario = float(input('Digite o salário para calcular o aumento: R$ '))
salario_novo = salario + (salario * 15 / 100)
print('Seu salário de R$ {:.2f}, com aumento de 15%, ficou R$ {:.2f}'.format(salario, salario_novo))

