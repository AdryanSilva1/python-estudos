# =================================
# Exercício ex8 - IMC (Índice de Massa Corporal)
# =================================

# -------- Minha solução --------
altura = float(input('digite a sua altura: (m)'))
peso = float(input('digite o seu peso: (kg)'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('você esta abaixo do peso')
elif imc > 18.5 and imc < 25:      # Erro: 18.5 exato não entra
    print('você esta no peso ideal')
elif imc > 25 and imc < 30:        # Erro: 25.0 exato não entra
    print('você esta sobrepeso')
elif imc > 30 and imc < 40:        # Erro: 30.0 exato não entra
    print('você est á obeso')
else:
    print('seu obsidade e mobida')  # typo + texto confuso
print(f'seu imc e de {imc:.1f}')


# -------- Solução corrigida --------
altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25.0:
    print('Peso ideal')
elif imc < 30.0:
    print('Sobrepeso')
elif imc < 40.0:
    print('Obesidade')
else:
    print('Obesidade mórbida')

print('Seu IMC: {:.1f}'.format(imc))
