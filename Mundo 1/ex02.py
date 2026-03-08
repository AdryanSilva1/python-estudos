# =================================
# Exercício 2 - Data de nascimento
# =================================

# -------- Minha solução --------
dia = input('que dia voce nasceu?')
mes = input('que mes voce nasceu?')
ano = input('que  ano voce nasceu?')
print('você nasceu no dia', dia, 'de', mes, 'no ano de', ano, ',correto senhor?')


# -------- Solução corrigida --------
dia = input('Que dia você nasceu? ')
mes = input('Que mês você nasceu? ')
ano = input('Que ano você nasceu? ')
print('Você nasceu no dia {} de {} no ano de {}, correto?'.format(dia, mes, ano))
