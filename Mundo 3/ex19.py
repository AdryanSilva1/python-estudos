# =================================
# Exercício ex19 - Cadastro de alunos com notas e consulta
# =================================

# -------- Minha solução --------

ficha = []
while True:
    Nome = str(input('Nome: '))
    n1 = float(input('nota 1: '))
    n2 = float(input('nota 2: '))
    m = (n1 + n2) / 2
    ficha.append([Nome, [n1, n2], m])
    if input('Quer continuar? [S/N] ').strip().upper()[0] == 'N':
        break

print()
print(f'{"no.":>4}{"nome":<10}{"média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:>4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]}: {ficha[opc][1]}')


# -------- Solução corrigida --------
alunos = []
while True:
    nome = input('Nome: ')
    n1   = float(input('Nota 1: '))
    n2   = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append({'nome': nome, 'notas': [n1, n2], 'media': media})
    if input('Continuar? [S/N]: ').strip().upper() == 'N':
        break

print(f'\n{"Nº":>3} {"Nome":<12} {"Média":>7}')
print('-' * 25)
for i, a in enumerate(alunos):
    print(f'{i:>3} {a["nome"]:<12} {a["media"]:>7.1f}')

while True:
    opc = int(input('\nNotas de qual aluno? (999 = sair): '))
    if opc == 999:
        break
    if 0 <= opc < len(alunos):
        a = alunos[opc]
        print(f'{a["nome"]}: {a["notas"]} | Média: {a["media"]:.1f}')
    else:
        print('Índice inválido.')

