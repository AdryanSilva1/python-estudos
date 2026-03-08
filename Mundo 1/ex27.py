# =================================
# Exercício 27 - Primeiro e último nome
# =================================

# -------- Minha solução --------

name = str(input('Digite sue nome: ')).strip().lower()
nome = name.split()
print('seu premeiro nome é: {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[len(nome) - 1]))


# -------- Solução corrigida --------
nome = input('Digite seu nome completo: ').strip().lower()
partes = nome.split()
print('Seu primeiro nome é: {}'.format(partes[0]))
print('Seu último nome é: {}'.format(partes[-1]))   # -1 é mais Pythônico que len-1
