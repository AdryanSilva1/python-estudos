# =================================
# Exercício ex30 - Funções: sortear lista e somar pares
# =================================

# -------- Minha solução --------
from random import randint
from time import sleep

def sorteia(lista):
    print('sorteando 5 valores: ', end='')
    for cont in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSoma dos pares de {lista} = {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)


# -------- Solução corrigida --------
from random import randint

def sortear(qtd=5, limite=10):
    return [randint(1, limite) for _ in range(qtd)]

def soma_pares(lista):
    return sum(v for v in lista if v % 2 == 0)

nums = sortear()
print(f'Valores: {nums}')
print(f'Soma dos pares: {soma_pares(nums)}')
