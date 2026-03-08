# =================================
# Exercício ex18 - Palíndromo
# =================================

# -------- Minha solução --------
frase = str(input('digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'o inveso de {junto} é {inverso}')
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('não temos u m palíndromo')


# -------- Solução corrigida --------
frase = input('Digite a frase: ').strip().upper()
# Remove espaços para comparar apenas as letras
junto = ''.join(frase.split())
inverso = junto[::-1]

print(f'Frase (sem espaços): {junto}')
print(f'Inverso            : {inverso}')

if inverso == junto:
    print(' É um PALÍNDROMO!')
else:
    print(' Não é um palíndromo.')
