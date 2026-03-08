# =================================
# Exercício 28 - Jogo de adivinhar número (0 a 5)
# =================================

# -------- Minha solução --------
# Import no meio do código (funciona, mas evitar).
print('voçê deve acertar o numero entre 0 e 5')
import random
numeros = [0, 1, 2, 3, 4, 5]
c = int(input('digite seu chute: '))
num = random.choice(numeros)
if c == num:
    print('voce acertou esta de parabéns o numero era {}'.format(num))
else:
    print('vocẽ errou o numero era {}'.format(num))


# -------- Solução corrigida --------
# A tentativa comentada usava randint + sleep — boa ideia, incorporada aqui.
from random import randint
from time import sleep

print('Tente adivinhar o número entre 0 e 5!')
jogador = int(input('Qual é o número? '))
computador = randint(0, 5)
print('Verificando...')
sleep(1)
if jogador == computador:
    print('Parabéns! Você acertou! O número era {}'.format(computador))
else:
    print('Errou! O número era {} e você chutou {}'.format(computador, jogador))
