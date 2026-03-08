# =================================
# Exercício ex19 - Contar maiores e menores de 21 anos
# =================================

# -------- Minha solução --------
from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 7):
    nascimento = int(input(f'em que ano a {c}° voce nasceu:'))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'{totalmaior} pessoas de maior\n{totalmenor} pessoa de menor')


# -------- Solução corrigida --------
from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for c in range(1, 7):
    nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - nasc
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'Maiores de 21 anos : {maiores} pessoa(s)')
print(f'Menores de 21 anos : {menores} pessoa(s)')

