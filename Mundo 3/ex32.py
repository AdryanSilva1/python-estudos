# =================================
# Exercício ex32 - Função fatorial com parâmetro show
# =================================

# -------- Minha solução --------
def fatorial(n, show=False):
    """
    --> calcula o fatorial de um número.
    :param n: número a ser calculado o fatorial
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)


# -------- Solução corrigida --------
def fatorial(n: int, show: bool = False) -> int:
    """Calcula o fatorial de n (n >= 0). Se show=True, exibe a operação."""
    if n < 0:
        raise ValueError('n deve ser >= 0')
    if n == 0:
        return 1
    f = 1
    fatores = []
    for c in range(n, 0, -1):
        f *= c
        fatores.append(str(c))
    if show:
        print(' × '.join(fatores) + f' = {f}')
    return f

print(fatorial(5, show=True))
print(fatorial(0))
