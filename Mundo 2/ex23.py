# =================================
# Exercício ex23 - Adivinhe o número (com dicas: mais/menos)
# =================================

# -------- Minha solução --------
from random import randint

computador = randint(0, 10)
print('sou seu computador acabei de pensar em um numero entre 0 e 10, ')
print('será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente novamente')

print(f'acertou! com {palpite} de tentativas. parabens')


# -------- Solução corrigida --------
from random import randint

LIMITE = 10
computador = randint(0, LIMITE)
print(f'Pensei em um número entre 0 e {LIMITE}. Tente adivinhar!')

palpite = 0
while True:
    jogador = int(input('Seu palpite: '))
    palpite += 1
    if jogador == computador:
        print(f'Acertou em {palpite} tentativa(s)! O número era {computador}.')
        break
    elif jogador < computador:
        print('Maior! Tente novamente.')
    else:
        print('Menor! Tente novamente.')

