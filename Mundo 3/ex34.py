# =================================
# Exercício ex34 - Função leiaint: input seguro de inteiro
# =================================

# -------- Minha solução --------

def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

n = leiaint('Digite um número: ')
print(f'Você digitou: {n}')


# -------- Solução corrigida --------
def leiaint(msg: str) -> int:
    while True:
        entrada = input(msg).strip()
        if entrada.lstrip('-').isnumeric() and entrada != '-':
            return int(entrada)
        print('Valor inválido. Digite um número inteiro (pode ser negativo).')

n = leiaint('Número inteiro: ')
print(f'Você digitou: {n}')

