# =================================
# Exercício ex28 - Função contador crescente/decrescente
# =================================

# -------- Minha solução --------

from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('inicio: '))
fim = int(input('fim: '))
pas = int(input('passo: '))
contador(ini, fim, pas)


# -------- Solução corrigida --------
def contador(inicio, fim, passo=1):
    """Conta de inicio até fim com o passo fornecido (crescente ou decrescente)."""
    passo = abs(passo) or 1
    if inicio <= fim:
        seq = range(inicio, fim + 1, passo)
    else:
        seq = range(inicio, fim - 1, -passo)
    print(*seq)

contador(1, 10)
contador(10, 1, 2)
