# =================================
# Exercício 16 - Parte inteira de um número (trunc)
# =================================

# -------- Minha solução --------
from math import trunc
n = float(input('digite o numero que deseja ver inteiro: '))
print('numero inteiro: {} '.format(trunc(n)))


# -------- Solução corrigida --------
from math import trunc

n = float(input('Digite o número: '))
print('Parte inteira: {}'.format(trunc(n)))
