# =================================
# Exercício ex36 - Sistema de ajuda Python com cores ANSI
# =================================

# -------- Minha solução --------

from time import sleep

c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'      # 6 - branco invertido
    )

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

while True:
    titulo('SISTEMA DE AJUDA PYTHON', 2)
    comando = input('Função ou biblioteca > ').strip()
    if comando.upper() == 'FIM':
        break
    ajuda(comando)

titulo('VOLTE SEMPRE!', 1)


# -------- Solução corrigida --------
from time import sleep

CORES = {
    'reset' : '\033[m',
    'erro'  : '\033[0;31m',
    'verde' : '\033[0;30;42m',
    'azul'  : '\033[0;30;44m',
    'inv'   : '\033[7;30m',
}

def titulo(msg, cor='reset'):
    print(CORES[cor] + '-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4) + CORES['reset'])

while True:
    titulo('SISTEMA DE AJUDA PYTHON', 'verde')
    cmd = input('> ').strip()
    if not cmd:
        continue
    if cmd.upper() == 'FIM':
        break
    titulo(f"Manual: {cmd}", 'azul')
    print(CORES['inv'], end='')
    help(cmd)
    print(CORES['reset'], end='')
    sleep(1)

titulo('ATE LOGO!', 'verde')

