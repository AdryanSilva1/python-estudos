# =================================
# Exercício 17 - Hipotenusa (Teorema de Pitágoras)
# =================================

# -------- Minha solução --------
import math

c1 = float(input('digite o cateto oposto: '))
c2 = float(input('digite o cateto adjacente: '))
hi = math.hypot(c1, c2)
print('a hipotenusa fica igual a: {:.2f} '.format(hi))


# -------- Solução corrigida --------
import math

cateto_oposto    = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa       = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa é igual a: {:.2f}'.format(hipotenusa))
