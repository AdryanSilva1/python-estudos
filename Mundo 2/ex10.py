# =================================
# Exercício ex10 - Jokenpô (Pedra, Papel, Tesoura)
# =================================

# -------- Minha solução --------
from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
jogador = int(input('''digite para escolher:
[0] pedra 
[1] papel 
[2] tesoura 
escolha umas das opções acima para informar sua jogada:'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 0:
    if jogador == 0:
        print('EMPATAMOS')
    elif jogador == 1:
        print('VOCẼ GANHOU')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATAMOS')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATAMOS')
    else:
        print('OPÇÃO INVALIDA')
else:
    print('opção invalida')
print(f'o computador jogou {computador}')  # Erro: exibe número, não o nome


# -------- Solução corrigida --------
from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
jogador = int(input('JO-KEN-PÔ!\n[0] Pedra  [1] Papel  [2] Tesoura\nSua escolha: '))

print('JO'); sleep(1)
print('KEN'); sleep(1)
print('PO!!!')

if jogador not in (0, 1, 2):
    print('Opção inválida!')
elif jogador == computador:
    print('EMPATE!')
elif (jogador == 0 and computador == 2) or \
     (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1):
    print('VOCÊ GANHOU!')
else:
    print('O COMPUTADOR GANHOU!')

print(f'Você: {itens[jogador]} | Computador: {itens[computador]}')

