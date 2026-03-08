# =================================
# Exercício ex17 - Matriz 3x3: pares, 3ª coluna, maior da 2ª linha
# =================================

# -------- Minha solução --------

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l},{c}]: '))
print('-=' * 20)

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:5^}]', end=' ')   # Erro: formatação inválida
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é: {spar}')

for l in range(3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {scol}')

for c in range(3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')


# -------- Solução corrigida --------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'[{l},{c}]: '))

print('-=' * 20)
soma_pares = 0
for linha in matriz:
    for v in linha:
        print(f'[{v:^5}]', end=' ')   # corrigido
        if v % 2 == 0:
            soma_pares += v
    print()
print('-=' * 20)

soma_col3 = sum(matriz[l][2] for l in range(3))
maior_linha2 = max(matriz[1])

print(f'Soma dos pares          : {soma_pares}')
print(f'Soma da 3ª coluna       : {soma_col3}')
print(f'Maior da 2ª linha       : {maior_linha2}')

