# =================================
# Exercício ex7 - Tipo de triângulo (equilátero, isósceles, escaleno)
# =================================

# -------- Minha solução --------
r1 = float(input('digite a primeira reta:'))
r2 = float(input('digite a segunda reta:'))
r3 = float(input('digite a terceira reta: '))
if r1 == r2 == r3:
    print('Seu trinẫgulo é equilatero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('seu triẫngulo e isoceles')
else:
    print('seu triangulo é escaleno')


# -------- Solução corrigida --------
r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))

if r1 == r2 == r3:
    print('Triângulo EQUILÁTERO (três lados iguais)')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo ISÓSCELES (dois lados iguais)')
else:
    print('Triângulo ESCALENO (todos os lados diferentes)')
