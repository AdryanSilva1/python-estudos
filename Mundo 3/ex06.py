# =================================
# Exercício ex06 - Vogais em cada palavra de uma tupla
# =================================

# -------- Minha solução --------
nomes = ('casa', 'carro', 'bola', 'computador', 'livro', 'telefone',
         'janela', 'cadeira', 'mesa', 'relogio')
for n in nomes:
    print(f'\nNa palavra {n.upper()} temos: ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nFIM DO PROGRAMA')


# -------- Solução corrigida --------
# Mesma lógica, pequena melhoria na saída
nomes = ('casa', 'carro', 'bola', 'computador', 'livro', 'telefone',
         'janela', 'cadeira', 'mesa', 'relogio')
for palavra in nomes:
    vogais = [l for l in palavra if l in 'aeiou']
    print(f'{palavra.upper():15} → vogais: {" ".join(vogais)} ({len(vogais)})')
print('FIM DO PROGRAMA')

