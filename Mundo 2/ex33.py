# =================================
# Exercício ex33 - Jogo Par ou Ímpar
# =================================

# -------- Minha solução --------
from random import randint

v = 0

while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR: [p/i]')).strip().upper()[0]

    print(f'você jogou {jogador} e o computador jogou{computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu!')
            v += 1
        else:
            print('você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você venceu!')
            v += 1
        else:
            print('você perdeu')
            break
    print('vamos jogar novamente...')
(f'game over, você venceu {v} vezes ')  # Erro: f-string solta, não imprime nada


# -------- Solução corrigida --------
from random import randint

v = 0

while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador

    tipo = ''
    while tipo not in ('P', 'I'):
        tipo = input('Par ou Ímpar? [P/I]: ').strip().upper()

    print(f'Você: {jogador} | Computador: {computador} | Total: {total}')

    par = total % 2 == 0
    ganhou = (tipo == 'P' and par) or (tipo == 'I' and not par)

    if ganhou:
        print('VOCÊ GANHOU! Vamos jogar novamente...')
        v += 1
    else:
        print('VOCÊ PERDEU! Game over.')
        break

print(f'Você venceu {v} vez(es).')  # corrigido: agora usa print()

