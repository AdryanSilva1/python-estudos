# =================================
# Exercício 18 - Seno, Cosseno e Tangente
# =================================

# -------- Minha solução --------
from math import radians, sin, cos, tan

n1 = float(input('digite o angulo que vc dejesa:'))
seno = sin(radians(n1))
print('o angulo de {} tem o seno de {:.2f}'.format(n1, seno))
cosseno = cos(radians(n1))
print(' o angulo de {} tem o cosseno de {:.2f}'.format(n1, cosseno))
tangente = tan(radians(n1))
print('o angulo de {} tem a tangente de {:.2f}'.format(n1, tangente))


# -------- Solução corrigida --------
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo em graus: '))
rad = radians(angulo)

print('O ângulo de {}° tem:'.format(angulo))
print('  Seno     : {:.2f}'.format(sin(rad)))
print('  Cosseno  : {:.2f}'.format(cos(rad)))
print('  Tangente : {:.2f}'.format(tan(rad)))
