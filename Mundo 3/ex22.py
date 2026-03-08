# =================================
# Exercício ex22 - Cadastro de funcionário com aposentadoria (dicionário)
# =================================

# -------- Minha solução --------

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year)

print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')


# -------- Solução corrigida --------
from datetime import date

ano_atual = date.today().year
dados = {}
dados['nome'] = input('Nome: ')
dados['idade'] = ano_atual - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))

if dados['ctps'] != 0:
    ano_cont = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    anos_trabalhados = ano_atual - ano_cont
    dados['anos p/ aposentar'] = max(0, 35 - anos_trabalhados)

print('-=' * 30)
for k, v in dados.items():
    print(f'{k:>20}: {v}')
