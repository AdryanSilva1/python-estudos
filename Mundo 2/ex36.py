# =================================
# Exercício ex36 - Caixa eletrônico: cédulas para um saque
# =================================

# -------- Minha solução --------
valor = int(input('Informe o valor que deseja sacar: R$ '))
total = valor
ced = 50
cedtotal = 0

while True:
    if total >= ced:
        total -= ced
        cedtotal += 1
    else:
        if cedtotal > 0:
            print(f'Total de {cedtotal} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedtotal = 0
    if total == 0:
        if cedtotal > 0:
            print(f'Total de {cedtotal} cédulas de R$ {ced}')
        break

print('Fim do programa')


# -------- Solução corrigida --------
valor = int(input('Valor do saque: R$ '))
cedulas = [50, 20, 10, 1]
restante = valor

print(f'Saque de R$ {valor}:')
for ced in cedulas:
    quantidade = restante // ced
    if quantidade > 0:
        print(f'  {quantidade} cédula(s) de R$ {ced}')
        restante -= quantidade * ced
    if restante == 0:
        break

if restante > 0:
    print(f'Não foi possível sacar R$ {restante} com as cédulas disponíveis.')
print('Fim.')

