# =================================
# Exercício ex15 - Somar apenas os números pares digitados
# =================================

# -------- Minha solução --------
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'voce informou {cont} numeros pares e a soma é a {soma}')


# -------- Solução corrigida --------
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Você informou {cont} número(s) par(es) e a soma é {soma}')
