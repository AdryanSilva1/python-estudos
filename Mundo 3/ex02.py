# =================================
# Exercício ex02 - Classificação de times (tupla)
# =================================

# -------- Minha solução --------
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio', 'Corinthians', 'São Paulo',
         'Cruzeiro', 'Fluminense', 'Internacional', 'Fortaleza', 'Vasco', 'Bahia',
         'Red Bull Bragantino', 'Atlético Mineiro', 'Vitória', 'Juventude', 'Criciúma',
         'Athletico Paranaense', 'Cuiabá', 'Atlético Goianiense')

print('-=' * 15)
print(f'os 5 primeiros são: {times[:5]}')
print('-=' * 15)
print(f'os 4 últimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'o Corinthians está na {times.index("Corinthians") + 1}ª posição')


# -------- Solução corrigida --------
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio', 'Corinthians', 'São Paulo',
         'Cruzeiro', 'Fluminense', 'Internacional', 'Fortaleza', 'Vasco', 'Bahia',
         'Red Bull Bragantino', 'Atlético Mineiro', 'Vitória', 'Juventude', 'Criciúma',
         'Athletico Paranaense', 'Cuiabá', 'Atlético Goianiense')

sep = '-=' * 15
print(sep)
print(f'5 primeiros   : {times[:5]}')
print(f'4 últimos     : {times[-4:]}')
print(f'Ordem alfab.  : {sorted(times)}')
print(f'Pos. Corinthians: {times.index("Corinthians") + 1}°')
print(sep)

