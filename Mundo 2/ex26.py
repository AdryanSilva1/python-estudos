# =================================
# Exercício ex26 - Progressão Aritmética com 10 termos (while)
# =================================

# -------- Minha solução --------
print('gerador de PA')
print('-=' * 10)

primeiro = int(input('primeiro termo: '))
razao = int(input(' digite a razao: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} - ', end=' ')
    termo += razao
    cont += 1
print('FIM')


# -------- Solução corrigida --------
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
soma = 0

print('PA gerada:')
while cont <= 10:
    print(termo, end=' ')
    soma += termo
    termo += razao
    cont += 1

print(f'\nSoma dos 10 termos: {soma}')

