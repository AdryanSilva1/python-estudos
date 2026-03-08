# =================================
# Exercício ex18 - Gerador de jogos da Mega-Sena
# =================================

# -------- Minha solução --------

from random import randint
from time import sleep

lista = []
jogos = []

print('-=' * 20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 20)
print(f'{"SORTEANDO":^40}')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')
print('-=' * 20)
print(f'{"BOA SORTE!":^40}')
print('-=' * 20)


# -------- Solução corrigida --------
from random import sample
from time import sleep

print(f'{"MEGA SENA":^40}')
quant = int(input('Quantos jogos? '))

jogos = []
for i in range(quant):
    jogo = sorted(sample(range(1, 61), 6))  # sample garante unicidade
    jogos.append(jogo)

print('-=' * 20)
for i, jogo in enumerate(jogos, 1):
    sleep(0.5)
    print(f'Jogo {i}: {jogo}')
print('-=' * 20)
print('Boa sorte!')
