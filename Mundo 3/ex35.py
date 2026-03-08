# =================================
# Exercício ex35 - Função nota() com *args e sit opcional
# =================================

# -------- Minha solução --------
def nota(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

resp = nota(5.5, 2.5, 9, 6, 8.5)
print(nota)   # erro: imprime <function nota at 0x...>, deveria ser print(resp)


# -------- Solução corrigida --------
def nota(*n, sit=False):
    r = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': sum(n) / len(n),
    }
    if sit:
        r['situacao'] = 'BOA' if r['media'] >= 7 else 'RAZOÁVEL' if r['media'] >= 5 else 'RUIM'
    return r

resp = nota(5.5, 2.5, 9, 6, 8.5, sit=True)
print(resp)   # corrigido: imprime o dicionário resultado

