# =================================
# Exercício ex16 - Progressão Aritmética (PA) com 10 termos
# =================================

# -------- Minha solução --------

primeiro = int(input('primeiro termo: '))
razao = int(input(' digite a razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end=' ')
print("babou")   # typo


# -------- Solução corrigida --------
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

print('Progressão Aritmética:')
for i in range(10):
    termo = primeiro + i * razao
    print(termo, end=' ')
print('\nFim da PA.')
