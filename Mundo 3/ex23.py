# =================================
# Exercício ex23 - Ficha de jogador com gols por partida (dicionário + lista)
# =================================

# -------- Minha solução --------

jogador = dict()
partidas = list()

jogador['nome'] = str(input('nome do jogador: '))
tot = int(input(f'numero de partidas jogadas pelo {jogador["nome"]}: '))

for c in range(0, tot):
    partidas.append(int(input(f' quantos gols na partida {c + 1}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor de {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador):          # Erro: itera chaves, não gols
    print(f' => na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')


# -------- Solução corrigida --------
jogador = {}
jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Partidas de {jogador["nome"]}: '))
jogador['gols'] = [int(input(f'Gols na partida {c + 1}: ')) for c in range(tot)]
jogador['total'] = sum(jogador['gols'])

print('-=' * 30)
print(f'Jogador : {jogador["nome"]}')
print(f'Partidas: {tot}')
for i, g in enumerate(jogador['gols'], 1):    # corrigido: itera a lista de gols
    print(f'  Partida {i}: {g} gol(s)')
print(f'Total   : {jogador["total"]} gols')

