# =================================
# Exercício 30 - Par ou ímpar
# =================================

# -------- Minha solução --------
num = int(input('digite um numero  inteiro: '))
if num % 2 == 0:
    print('seu numero é par')
else:
    print('seu numero é impar')


# -------- Solução corrigida --------
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
