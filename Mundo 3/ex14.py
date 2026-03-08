# =================================
# Exercício ex14 - Cadastro de pessoas: maior e menor peso
# =================================

# -------- Minha solução --------

temp = []
princ = []
maior = 0
menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    if input('Quer continuar? [S/N] ').strip().upper()[0] == 'N':
        break

print(f'Ao todo temos {len(princ)} pessoas cadastradas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'o menor peso foi de {menor}kg. Peso de ', end='')  
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()


# -------- Solução corrigida --------
pessoas = []
while True:
    nome = input('Nome: ')
    peso = float(input('Peso (kg): '))
    pessoas.append([nome, peso])
    if input('Continuar? [S/N]: ').strip().upper() == 'N':
        break

maior = max(p[1] for p in pessoas)
menor = min(p[1] for p in pessoas)

print(f'\n{len(pessoas)} pessoas cadastradas.')
print(f'Maior peso: {maior}kg → ' + ', '.join(p[0] for p in pessoas if p[1] == maior))
print(f'Menor peso: {menor}kg → ' + ', '.join(p[0] for p in pessoas if p[1] == menor))
