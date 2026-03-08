# =================================
# Exercício 8 - Converter metros para centímetros
# =================================

# -------- Minha solução --------
m = int(input('digite o valor em metros: '))
c = m * 100
print('seu {}m convertido para centimetros fica {}cm'.format(m, c))


# -------- Solução corrigida --------
# Usar float para aceitar valores decimais (ex: 1.5m)
metros = float(input('Digite o valor em metros: '))
centimetros = metros * 100
print('{}m convertido para centímetros fica {:.0f}cm'.format(metros, centimetros))

