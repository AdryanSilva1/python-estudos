# =================================
# Exercício ex32 - Tabuada em loop (sai com número negativo)
# =================================

# -------- Minha solução --------

while True:
    n = int(input('digite um valor para saber a sua: '))
    print('-' * 30)
    if n < -0:
        break
    print("PROGRAMA DE TABUADA ENCERRADA, VOLTE SEMPRE!")  # Erro: posição errada
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)


# -------- Solução corrigida --------
print('=== TABUADA ===')
print('Digite um número negativo para sair.')

while True:
    n = int(input('\nNúmero: '))
    if n < 0:
        break
    print('-' * 25)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 25)

print('Programa encerrado. Até mais!')
