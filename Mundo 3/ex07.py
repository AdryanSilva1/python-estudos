# =================================
# Exercício ex07 - Maior e menor valor de uma lista com posição
# =================================

# -------- Minha solução --------
# Erro: l.index() retorna apenas a PRIMEIRA ocorrência — se o valor repetir,
# as demais posições são ignoradas. Funciona para o caso geral.
l = []
for c in range(0, 5):
    l.append(int(input(f'Digite o {c + 1}° valor: ')))
print(f'Você digitou os valores {l}')
print(f'O maior valor digitado foi {max(l)} nas posições {l.index(max(l))} ')
print(f'O menor valor digitado foi {min(l)} nas posições {l.index(min(l))} ')


# -------- Solução corrigida --------
# Mostra TODAS as posições do maior e menor (caso de empate)
lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}° valor: ')))

maior = max(lista)
menor = min(lista)
pos_maior = [i for i, v in enumerate(lista) if v == maior]
pos_menor = [i for i, v in enumerate(lista) if v == menor]

print(f'Valores: {lista}')
print(f'Maior: {maior} nas posições {pos_maior}')
print(f'Menor: {menor} nas posições {pos_menor}')

