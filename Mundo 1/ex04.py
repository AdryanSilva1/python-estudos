# =================================
# Exercício 4 - Análise de string com métodos
# =================================

# -------- Minha solução --------
n = input('digite algo: ')
print(type(n))
print('so tem espaço?', n.isspace())
print('e um  numero?', n.issnumeric()) #erro de digitação
print('e alfabetico?', n.isalpha())
print('e alfanumerico?', n.isalnum())
print('é maiuscula?', n.isupper())
print('é minuscula?', n.islower())
print('esta capitalizada?', n.istitle())


# -------- Solução corrigida --------
n = input('Digite algo: ')
print(type(n))
print('Só tem espaço?', n.isspace())
print('É um número?', n.isnumeric())   # corrigido: isnumeric()
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('É maiúscula?', n.isupper())
print('É minúscula?', n.islower())
print('Está capitalizada?', n.istitle())

