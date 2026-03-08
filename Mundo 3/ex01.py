# =================================
# Exercício ex01 - Número por extenso (0 a 20) usando tupla
# =================================

# -------- Minha solução --------
cont = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
        'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
        'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('tenete novamente.', end='')   #
print(f'voce digitou o numero {cont[num]}')


# -------- Solução corrigida --------
NUMEROS = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Valor inválido. Tente novamente.')
print(f'Você digitou o número {NUMEROS[num]}.')

