# =================================
# Exercício 33 - Maior e menor entre três números
# =================================

# -------- Minha solução --------
num1 = int(input('digite o primero numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = int(input('digite o terceiro numero: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num2:   # Erro: segunda condição deveria ser num1<=num3
    menor = num1
elif num2 <= num1 and num2 <= num1: # Erro: segunda condição deveria ser num2<=num3
    menor = num2
else:
    menor = num3

print('seu maior numero: {}'.format(maior))
print('seu menor numero: {}'.format(menor))


# -------- Solução corrigida --------
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:   # corrigido
    menor = num1
elif num2 <= num1 and num2 <= num3: # corrigido
    menor = num2
else:
    menor = num3

print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))

