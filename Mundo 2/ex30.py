# =================================
# Exercício ex30 - Estatísticas de números digitados (média, maior, menor)
# =================================

# -------- Minha solução --------
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'sS':
    num = int(input('digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar? [s/n] ')).upper().strip()[0]
media = soma / quant
print(f'voce digitou {quant} e sua media foi {media}\n o maior numero foi {maior} e o menor foi {menor}')


# -------- Solução corrigida --------
soma = 0
quant = 0
maior = None
menor = None

while True:
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp != 'S':
        break

media = soma / quant
print(f'Você digitou {quant} número(s).')
print(f'Média: {media:.2f} | Maior: {maior} | Menor: {menor}')

