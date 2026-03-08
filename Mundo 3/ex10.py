# =================================
# Exercício ex10 - Inserção em lista já ordenada
# =================================

# -------- Minha solução --------
# Erro de lógica: 'if c == 0 or n > lista[-1]' adiciona ao final apenas se maior
# que o último. Funciona mas a inserção ordenada no else está correta.
lista = []
for c in range(0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')


# -------- Solução corrigida --------
lista = []
for c in range(1, 6):
    n = int(input(f'Digite o {c}° valor: '))
    inserido = False
    for pos, v in enumerate(lista):
        if n <= v:
            lista.insert(pos, n)
            print(f'Inserido na posição {pos}.')
            inserido = True
            break
    if not inserido:
        lista.append(n)
        print('Adicionado ao final.')
print(f'Lista ordenada: {lista}')
