# =================================
# Exercício ex003 - Tupla com 5 valores aleatórios
# =================================

# -------- Minha solução --------
from random import randint

num = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))

print(f'(Os vlaores sorteados foram: {num}')   # Erro: '(' sobrando
print(f'o menor valor da tlupla é {min(num)}')
print(f'o maior valor da sua tlupla é {max(num)}')


# -------- Solução corrigida --------
from random import randint

num = tuple(randint(1, 20) for _ in range(5))

print(f'Os valores sorteados foram: {num}')
print(f'Menor valor da tupla: {min(num)}')
print(f'Maior valor da tupla: {max(num)}')

