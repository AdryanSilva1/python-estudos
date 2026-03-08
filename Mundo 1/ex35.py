# =================================
# Exercício 35 - Verificar se três retas formam triângulo
# =================================

# -------- Minha solução --------
# Lógica correta (condição de existência do triângulo).
# Tipos nos inputs: 'primera/segunda/terceira reta numero' — texto confuso.
r1 = float(input('digite o primera reta numero: '))
r2 = float(input('digite o segunda reta numero: '))
r3 = float(input('digite o terceira reta numero: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode formar um triangulo')
else:
    print('não pode formar um triangulo')


# -------- Solução corrigida --------
print('-=' * 20)
print('Analisando um triângulo')
print('-=' * 20)

r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os lados {}, {} e {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('Os lados {}, {} e {} não podem formar um triângulo.'.format(r1, r2, r3))

