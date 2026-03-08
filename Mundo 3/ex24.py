# =================================
# Exercício ex24 - Cadastro de pessoas com média de idade (dicionário + lista)
# =================================

# -------- Minha solução --------

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
    print('ERRO! por favor, digite apenas S ou N.')  # Erro: fora do while, imprime sempre
    if resp == 'N':
        break

media = soma / len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print(f'Média de idade: {media:.1f} anos')
for p in galera:
    if p['sexo'] == 'F':
        print(f'Mulher: {p["nome"]}')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} | {p["sexo"]} | {p["idade"]} anos')


# -------- Solução corrigida --------
galera = []
soma = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo in ('M', 'F'):
            pessoa['sexo'] = sexo
            break
        print('Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa)
    while True:
        resp = input('Continuar? [S/N]: ').strip().upper()
        if resp in ('S', 'N'):
            break
        print('Digite apenas S ou N.')   # dentro do while correto
    if resp == 'N':
        break

media = soma / len(galera)
print(f'\nTotal: {len(galera)} | Média de idade: {media:.1f} anos')
print('Mulheres:', ', '.join(p['nome'] for p in galera if p['sexo'] == 'F') or 'nenhuma')
print('Acima da média:')
for p in galera:
    if p['idade'] >= media:
        print(f'  {p["nome"]} ({p["idade"]} anos)')

