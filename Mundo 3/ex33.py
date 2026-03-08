# =================================
# Exercício ex33 - Função ficha de jogador com parâmetros padrão
# =================================

# -------- Minha solução --------

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n = input('Nome do Jogador: ')
g = input('Número de gols: ')
g = int(g) if g.isnumeric() else 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)


# -------- Solução corrigida --------
def ficha(jogador='<desconhecido>', gols=0):
    if not isinstance(gols, int) or gols < 0:
        gols = 0
    if not jogador.strip():
        jogador = '<desconhecido>'
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'

nome = input('Nome: ')
gols_str = input('Gols: ')
gols = int(gols_str) if gols_str.isnumeric() else 0
print(ficha(nome or '<desconhecido>', gols))
