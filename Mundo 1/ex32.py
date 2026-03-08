# =================================
# Exercício 32 - Ano bissexto
# =================================

# -------- Minha solução --------
# Erro de lógica: apenas ano % 4 == 0 não é suficiente.
# Ex: 1900 é divisível por 4 mas NÃO é bissexto. 2000 é bissexto.
# Regra completa: (div. por 4 E não div. por 100) OU (div. por 400).
ano = int(input('para saber se é bissexto, digite o ano: '))
if ano % 4 == 0:        # Erro: regra incompleta
    print('é bissexto')
else:
    print('não é bissexto')


# -------- Solução corrigida --------
from datetime import date

ano = int(input('Qual ano quer analisar? (0 = ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
