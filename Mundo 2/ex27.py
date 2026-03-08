# =================================
# Exercício ex27 - PA com quantidade de termos dinâmica (pausas)
# =================================

# -------- Minha solução --------
print('gerador de PA')
print('-=' * 10)

primeiro = int(input('primeiro termo: '))
razao = int(input(' digite a razao: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais

    while cont <= total:
        print(f'{termo} - ', end=' ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input(' QUANTOS TERMOS VOCÊ DESEJA ADICIORA?'))  # typo

print(f'progressão finalizada com {total} termos') 


# -------- Solução corrigida --------
print('Gerador de PA com pausas')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
total = 0

while True:
    mais = int(input('Quantos termos deseja gerar? (0 para parar): '))
    if mais == 0:
        break
    total += mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    print('\n--- pausa ---')

print(f'\nProgressão finalizada com {total} termos.')

