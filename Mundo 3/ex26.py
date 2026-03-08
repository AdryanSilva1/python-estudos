# =================================
# Exercício ex26 - Função área de terreno
# =================================

# -------- Minha solução --------
def area(larg, comp):
    print(f'a area de {larg}x{comp} = {larg * comp}m²')

l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)


# -------- Solução corrigida --------
def area(largura, comprimento):
    return largura * comprimento

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
print(f'Área: {area(l, c):.2f} m²')
