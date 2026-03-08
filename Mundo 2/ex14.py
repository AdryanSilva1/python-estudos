# =================================
# Exercício ex14 - Tabuada com for
# =================================

# -------- Minha solução --------
t = int(input('deseja qual tabuada? '))
for c in range(1, 11):
    print('{} x {} = {}'.format(t, c, t * c))


# -------- Solução corrigida --------
t = int(input('Qual tabuada deseja ver? '))
print('-' * 20)
print(f'   Tabuada do {t}')
print('-' * 20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(t, c, t * c))
print('-' * 20)
