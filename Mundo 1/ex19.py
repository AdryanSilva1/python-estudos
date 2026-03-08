# =================================
# Exercício 19 - Sorteio de aluno (random.choice)
# =================================

# -------- Minha solução --------
from random import choice

n1 = str(input('digite o primeiro aluno:'))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1, n2, n3, n4]
e = choice(lista)
print('O ALUNO ESCOLHIDO FOI: {}'.format(e))


# -------- Solução corrigida --------
from random import choice

n1 = input('Digite o nome do 1º aluno: ')
n2 = input('Digite o nome do 2º aluno: ')
n3 = input('Digite o nome do 3º aluno: ')
n4 = input('Digite o nome do 4º aluno: ')
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('O aluno escolhido foi: {}'.format(sorteado))
