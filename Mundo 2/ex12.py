# =================================
# Exercício ex12 - Imprimir números pares até 50
# =================================

# -------- Minha solução --------

for n in range(2, 51, 2):
    print(n, end=' ')
print('acabou')


# -------- Solução corrigida --------
print('Números pares de 1 a 50:')
for n in range(2, 51, 2):
    print(n, end=' ')
print('\nFim!')

