# =================================
# Exercício 26 - Contar e localizar a letra 'a' em uma frase
# =================================

# -------- Minha solução --------
frase = str(input('digite sua frase: ')).lower().strip()
print('você tem tantos {} a.'.format(frase.count('a')))
print('ele aparece a primeira vez na posição {}'.format(frase.find('a') + 1))
print('ele aparece a ultima vez na posição {}'.format(frase.rfind('a') + 1)) 

# -------- Solução corrigida --------
frase = input('Digite sua frase: ').lower().strip()
quantidade = frase.count('a')
primeira   = frase.find('a') + 1    # +1 para posição humana (começa em 1)
ultima     = frase.rfind('a') + 1

print('A letra "a" aparece {} vez(es).'.format(quantidade))
print('Primeira ocorrência na posição {}.'.format(primeira))
print('Última ocorrência na posição {}.'.format(ultima))
