# =================================
# Exercício ex17 - Verificar se número é primo
# =================================

# -------- Minha solução --------
num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO NÚMERO {num} FOI DIVISÍVEL {tot} VEZES')
if tot == 2:
    print('esse número é primo')
else:
    print('esse númerO não é primo')


# -------- Solução corrigida --------
num = int(input('Digite um número: '))
divisores = []
for c in range(1, num + 1):
    if num % c == 0:
        divisores.append(c)

print(f'Divisores de {num}: {divisores}')
print(f'O número {num} foi divisível {len(divisores)} vez(es).')

if len(divisores) == 2:
    print(f'{num} É PRIMO.')
else:
    print(f'{num} NÃO é primo.')
