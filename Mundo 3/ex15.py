# =================================
# Exercício ex15 - Separar 7 números em pares e ímpares com matriz 2D
# =================================

# -------- Minha solução --------
num = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}º número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os números pares são: {sorted(num[0])}')
print(f'Os números ímpares são: {sorted(num[1])}')


# -------- Solução corrigida --------
pares = []
impares = []
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'Pares   : {sorted(pares)}')
print(f'Ímpares : {sorted(impares)}')
