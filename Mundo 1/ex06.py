# =================================
# Exercício 6 - Dobro, triplo e raiz quadrada
# =================================

# -------- Minha solução --------
n = int(input('digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('seu numero é {}, o seu dobro é {}, o seu triplo {} e por fim sua raiz {}'.format(n, d, t, r))


# -------- Solução corrigida --------
import math

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n) # Um jeito mais simples usando uma bliblioteca
print('Seu número é {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, dobro, triplo, raiz))
