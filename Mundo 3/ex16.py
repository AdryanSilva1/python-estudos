# =================================
# Exercício ex16 - Preencher e exibir matriz 3x3
# =================================

# -------- Minha solução --------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l},{c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:5^}]', end=' ')   # Erro: formatação inválida
    print()


# -------- Solução corrigida --------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Posição [{l},{c}]: '))
print('-=' * 20)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end=' ')   # corrigido: {:^5}
    print()
print('-=' * 20)
