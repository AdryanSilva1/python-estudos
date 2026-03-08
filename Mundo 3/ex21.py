# =================================
# Exercício ex21 - Dado para 4 jogadores + ranking (dicionário)
# =================================

# -------- Minha solução --------
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)


# -------- Solução corrigida --------
from random import randint

jogo = {f'jogador{i}': randint(1, 6) for i in range(1, 5)}
ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)

for k, v in jogo.items():
    print(f'{k}: {v}')
print('-' * 30)
for pos, (nome, pts) in enumerate(ranking, 1):
    print(f'{pos}º {nome} — {pts} pontos')

