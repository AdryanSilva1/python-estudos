# =================================
# Exercício ex22 - Validar entrada de sexo [M/F]
# =================================

# -------- Minha solução --------

sexo = str(input('digite seu sexo [M/F] :')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('dados invalidos,preencha novamente o seu sexo: ')).strip().upper()[0]
print(f'sexo {sexo} registrado co sucesso')  # typo: 'co' → 'com'


# -------- Solução corrigida --------
sexo = input('Digite seu sexo [M/F]: ').strip().upper()
while sexo not in ('M', 'F'):
    sexo = input('Entrada inválida. Digite M ou F: ').strip().upper()
print(f'Sexo "{sexo}" registrado com sucesso.')

