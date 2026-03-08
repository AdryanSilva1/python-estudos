# =================================
# Exercício ex29 - Soma de valores até digitar 999 (padrão sentinela pré-loop)
# =================================

# -------- Minha solução --------

num = cont = soma = 0
num = int(input('digite um numero [ 999 para parar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero [ 999 para parar]: '))
print(f'voce digitou {cont} numeros e sua soma é {soma}')


# -------- Solução corrigida --------
soma = 0
cont = 0
num = int(input('Digite um número (999 para parar): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número (999 para parar): '))

print(f'Você digitou {cont} número(s). Soma: {soma}')

