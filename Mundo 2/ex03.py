# =================================
# Exercício ex3 - Maior entre dois números
# =================================

# -------- Minha solução --------
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo  numero: '))
if num1 > num2:
 print('o mairo e o primeiro valor')
elif num2 > num1:
  print('o mairo e o segundo valor')
else:
     print('os valores são iguais')


# -------- Solução corrigida --------
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O maior é o primeiro valor: {}'.format(num1))
elif num2 > num1:
    print('O maior é o segundo valor: {}'.format(num2))
else:
    print('Os valores são iguais: {}'.format(num1))
