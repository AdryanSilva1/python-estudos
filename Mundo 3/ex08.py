# =================================
# Exercício ex08 - Maior e menor com todas as posições (duas abordagens)
# =================================

# -------- Minha solução --------

lista = []
for c in range(0, 5):
    lista.append(int(input(f'digite um numero:')))

print(f'os valores digitados foram {lista}')
posicaoMaior = [i for i, v in enumerate(lista) if v == max(lista)]
print(f'o maior valor digitado foi {max(lista)} na posiçao {posicaoMaior}')

posicaoMenor = [i for i, v in enumerate(lista) if v == min(lista)]
print(f'o menor valor digitado foi {min(lista)} na posiçao {lista.index(min(lista))}')  # Erro: deveria usar posicaoMenor


# -------- Solução corrigida --------
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

