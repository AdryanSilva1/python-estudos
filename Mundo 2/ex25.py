# =================================
# Exercício ex25 - Fatorial com exibição do cálculo
# =================================

# -------- Solução corrigida --------
n = int(input('Digite um número: '))
c = n
f = 1
print(f' calculando o {n}! =', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(f'x' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'o fatorial de {n} é {f}')

# -------- Minha solução --------
n = int(input('Digite um número: '))
fatorial = 1
cont = 1
while cont <= n:
    fatorial *= cont
    cont += 1
print(f'O fatorial de {n} é {fatorial}')

