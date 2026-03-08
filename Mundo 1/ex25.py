# =================================
# Exercício 25 - Verificar se o nome contém "Silva"
# =================================

# -------- Minha solução --------

name = str(input('digite o nome completo: '))
name.lower()                        # Erro: não reatribui
if 'silva' in name:
    print('seu nome tem silva')
elif 'silva' not in [name]:         # Erro: busca em lista, não na string
    print('seu nome não tem silva')


# -------- Solução corrigida --------
nome = input('Digite o nome completo: ').strip().lower()
if 'silva' in nome:
    print('Seu nome contém "Silva"')
else:
    print('Seu nome não contém "Silva"')
