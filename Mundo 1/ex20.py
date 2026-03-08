# =================================
# Exercício 20 - Embaralhar lista
# =================================

# -------- Minha solução --------

from random import shuffle

n1 = str(input('digite o priemiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem da lista será: {}')  # Erro: {} não é substituído (Falta de atenção absurda)
print(lista)


# -------- Solução corrigida --------
from random import shuffle

n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A nova ordem da lista será: {}'.format(lista))

