# =================================
# Exercício ex04 - Operações com tupla (busca, contagem, pares)
# =================================

# -------- Minha solução --------

n1 = int(input('digite um numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceirto numero: '))   
n4 = int(input('digite o quarto numero: '))

t = (n1, n2, n3, n4)

if 9 in t:
    print(f'o numero 9 apareceu {t.count(9)} vezesz')   
if 3 in t:
    print(f'o numero 3 apareceu na {t.index(3) + 1}° posição')
else:
    print('o numero 3 não foi digitado')
even_numbers = [num for num in t if num % 2 == 0]
if even_numbers:
    print(f'os numeros pares são: {even_numbers}', end=' ')


# -------- Solução corrigida --------
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
t = (n1, n2, n3, n4)

print(f'Tupla digitada: {t}')

if 9 in t:
    print(f'O número 9 apareceu {t.count(9)} vez(es).')
else:
    print('O número 9 não foi digitado.')

if 3 in t:
    print(f'O número 3 está na posição {t.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')

pares = [n for n in t if n % 2 == 0]
print(f'Números pares: {pares}' if pares else 'Nenhum número par digitado.')

