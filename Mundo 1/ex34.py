# =================================
# Exercício 34 - Aumento de salário com faixa
# =================================

# -------- Minha solução --------

salario = float(input('digite seu salario: '))
if salario >= 1250.00:
    print('seu salario depois do aumento de 10% é:{:.2f} '.format((salario * 0.10) + salario))
else:
    print('seu salario depois do aumento de 10% é:{:.2f} '.format((salario * 0.15) + salario))  # Erro: mensagem diz 10% mas aplica 15%


# -------- Solução corrigida --------
salario = float(input('Digite seu salário: R$ '))
if salario >= 1250.00:
    percentual = 10
    novo = salario * 1.10
else:
    percentual = 15
    novo = salario * 1.15

print('Salário atual  : R$ {:.2f}'.format(salario))
print('Aumento        : {}%'.format(percentual))
print('Novo salário   : R$ {:.2f}'.format(novo))
