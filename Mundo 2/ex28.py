# =================================
# Exercício ex28 - Sequência de Fibonacci
# =================================

# -------- Minha solução --------
print('-' * 30)
print('sequencia de fibonacci')
print('-' * 30)

n = int(input('digite quantos termo você quer  mostrar: '))
t1 = 0
t2 = 1

print('~' * 30)
print(f'{t1} - {t2}', end=' ')

cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'- {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1

print('- FIM')


# -------- Solução corrigida --------
# Tratar caso n < 2 para evitar saída incompleta
n = int(input('Quantos termos da sequência de Fibonacci deseja ver? '))

t1, t2 = 0, 1
print('Fibonacci:')

for i in range(n):
    print(t1, end=' ')
    t1, t2 = t2, t1 + t2

print()

