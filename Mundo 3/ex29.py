# =================================
# Exercício ex29 - Função com *args: máximo de N valores
# =================================

# -------- Minha solução --------
def maximo(*num):
    print('analisando valores passados')
    print(f' {num} foram informados, ao todo {len(num)} valores.')
    print(f'o maior valor informado foi {max(num)}')

maximo(2, 9, 5, 7, 1)
maximo(4, 7)
maximo(1, 2)
maximo(6)


# -------- Solução corrigida --------
def maximo(*nums):
    if not nums:
        print('Nenhum valor informado.')
        return None
    m = max(nums)
    print(f'Valores: {nums} | Maior: {m}')
    return m

maximo(2, 9, 5, 7, 1)
maximo(4, 7)
maximo(6)
