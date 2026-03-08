# =================================
# Exercício ex20 - Dicionário de aluno com situação
# =================================

# -------- Minha solução --------

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}:  '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


# -------- Solução corrigida --------
aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print(f'Aluno  : {aluno["nome"]}')
print(f'Média  : {aluno["media"]:.1f}')
print(f'Situação: {aluno["situacao"]}')
