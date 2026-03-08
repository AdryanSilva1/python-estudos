# =================================
# Exercício 14 - Conversão Celsius para Fahrenheit
# =================================

# -------- Minha solução --------
c = float(input('informe a temperatura em celcius: '))
f = ((9 * c) / 5) + 32
print(' a temperatura de {}c corresponde a {}f!'.format(c, f))


# -------- Solução corrigida --------
celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = ((9 * celsius) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(celsius, fahrenheit))
