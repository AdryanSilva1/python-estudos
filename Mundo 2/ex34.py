# =================================
# Exercício ex34 - Cadastro de pessoas: maiores de 18, homens, mulheres < 20
# =================================

# -------- Minha solução --------
tot18 = totH = totM20 = 0

while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [F/M]')).strip().upper()
        [0]   # Erro: expressão solta, não aplica [0] ao sexo

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'total de pessoas com mais de 18 anos: {tot18}')
print(f'ao todo temos {totH} homens cadatrados')
print(f'e temos {totM20} mulheres com menos de 20 anos')


# -------- Solução corrigida --------
tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in ('M', 'F'):
        sexo = input('Sexo [M/F]: ').strip().upper()  # [0] aplicado corretamente se necessário

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ''
    while resp not in ('S', 'N'):
        resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break

print(f'Maiores de 18 anos    : {tot18}')
print(f'Homens cadastrados    : {totH}')
print(f'Mulheres com < 20 anos: {totM20}')

