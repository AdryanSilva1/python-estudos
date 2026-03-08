# =================================
# Exercício ex13 - Soma dos múltiplos de 3 até 500
# =================================

# -------- Minha solução --------

soma = 0
cont = 0
for c in range(1, 501, 2):     # erro: step = 2 pula os pares
    if c % 3 == 0:
        cont += 1
        soma += c
print(f"a soma de todos os {cont} valortes multiplos de 3 é {soma}")


# -------- Solução corrigida --------
soma = 0
cont = 0
for c in range(1, 501):        # sem step: percorre todos os números
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} múltiplos de 3 até 500 é {soma}')

