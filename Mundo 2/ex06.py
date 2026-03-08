# =================================
# Exercício ex6 - Categoria do marinheiro por idade
# =================================

# -------- Minha solução --------
from datetime import date

data = date.today().year
nasc = int(input('para descobrir seu rank de marinheirodigite o ano do seu nascimento: '))
ano = data - nasc
print('o atleta tem {} anos'.format(ano))
if ano <= 9:
    print('você é um marinheiro MIRIN!')
elif ano <= 14:
    print('você é um marinheiro INFANTIL!')
elif ano <= 19:
    print('você é um marinheiro JUNIOR!')
elif ano == 25:             # Erro: idades 20-24 sem categoria
    print('você é um marinheiro SÊNIOR!')
elif ano >= 26:
    print('você é um marinheiro MASTER!')


# -------- Solução corrigida --------
from datetime import date

ano_atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - nasc
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:       # corrigido: cobre 20 a 25
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
