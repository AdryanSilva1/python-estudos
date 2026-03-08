# =================================
# Exercício ex20 - Maior e menor peso entre 5 pessoas
# =================================

# -------- Minha solução --------

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'digite o peso da  {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'maior peso é {maior}\n menor peso é {menor}')


# -------- Solução corrigida --------
maior = None
menor = None

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa (kg): '))
    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso

print(f'Maior peso : {maior} kg')
print(f'Menor peso : {menor} kg')

