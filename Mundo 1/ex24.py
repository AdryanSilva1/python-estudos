# =================================
# Exercício 24 - Verificar se cidade começa com "Santos"
# =================================

# -------- Minha solução --------

cdd = str(input('digite o nume da cidade que você mora: '))
cdd.lower()                     # Erro: não reatribui
if 'santos' in [cdd]:           # Erro: busca em lista, não na string
    print(' sua cidade comeca com santos')
elif 'santos' not in [cdd]:
    print('sua cidade não começa com santos')


# -------- Solução corrigida --------
cdd = input('Digite o nome da cidade que você mora: ').strip().lower()
if cdd.startswith('santos'):
    print('Sua cidade começa com "Santos"')
else:
    print('Sua cidade não começa com "Santos"')