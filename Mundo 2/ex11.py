# =================================
# Exercício ex11 - Contagem regressiva para o Ano Novo
# =================================

# -------- Minha solução --------
from time import sleep

for c in range(10, -1, -1):
    print('{} '.format(c))
    sleep(1)
print('🎆🎇🎆feliz ano novo🎆🎇🎆')


# -------- Solução corrigida --------
from time import sleep

print('Contagem regressiva:')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('🎆🎇🎆 Feliz Ano Novo! 🎆🎇🎆')

