# =================================
# Exercício ex25 - Cadastro de time com gols por jogador (dicionário + lista)
# =================================

# -------- Minha solução --------
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    # partidas.clear() ← FALTOU AQUI: gols do jogador anterior acumulam
    jogador['nome'] = str(input('nome do jogador: '))
    tot = int(input(f'numero de partidas de {jogador["nome"]}: '))

    for c in range(0, tot):
        partidas.append(int(input(f' gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO, responda apenas S ou N')
    if resp == 'N':
        break

print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 = sair)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Código {busca} não encontrado.')
    else:
        print(f'Jogador: {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols'], 1):
            print(f'  Jogo {i}: {g} gols')


# -------- Solução corrigida --------
time = []
while True:
    nome = input('Nome do jogador: ')
    tot  = int(input(f'Partidas de {nome}: '))
    gols = [int(input(f'Gols na partida {c + 1}: ')) for c in range(tot)]
    time.append({'nome': nome, 'gols': gols, 'total': sum(gols)})

    while True:
        resp = input('Continuar? [S/N]: ').strip().upper()
        if resp in ('S', 'N'):
            break
        print('Digite S ou N.')
    if resp == 'N':
        break

print(f'{"Cod":>4} {"Nome":<15} {"Total":>6}')
print('-' * 30)
for i, j in enumerate(time):
    print(f'{i:>4} {j["nome"]:<15} {j["total"]:>6}')

while True:
    cod = int(input('\nVer jogador (999 = sair): '))
    if cod == 999:
        break
    if 0 <= cod < len(time):
        j = time[cod]
        print(f'{j["nome"]}: {j["gols"]} | Total: {j["total"]}')
    else:
        print('Código inválido.')
