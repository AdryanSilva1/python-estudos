# =================================
# Exercício ex31 - Soma de valores até digitar 999 (while True + break)
# =================================

# -------- Minha solução --------
soma = cont = 0
while True:
    num = int(input(' digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'a soma dos {cont} valores foi{soma}, ')   

# -------- Solução corrigida --------
soma = 0
cont = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'A soma dos {cont} valores foi {soma}.')

