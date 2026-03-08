# =================================
# Exercício ex24 - Menu de operações com dois números
# =================================

# -------- Minha solução --------
# Erro menor: n1/n2 lidos como int mas na opção 4 reatribuídos como float — inconsistência.
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa""")
    opcao = int(input('Digite a sua escolha: '))
    if opcao == 1:
        print(f'a soma de {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'o resultado de {n1} x {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('Os valores são iguais')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))   # inconsistência: era int
        n2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')
sleep(1)
print('fim do programa... volte sempre!')


# -------- Solução corrigida --------
from time import sleep

def ler_numero(msg):
    return float(input(msg))

n1 = ler_numero('Digite o primeiro número: ')
n2 = ler_numero('Digite o segundo número: ')

while True:
    print('\n[1] Somar  [2] Multiplicar  [3] Maior  [4] Novos números  [5] Sair')
    opcao = int(input('Escolha: '))

    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        maior = max(n1, n2) if n1 != n2 else None
        print(f'Maior: {maior}' if maior else 'Os valores são iguais.')
    elif opcao == 4:
        n1 = ler_numero('Novo primeiro número: ')
        n2 = ler_numero('Novo segundo número: ')
    elif opcao == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida!')

sleep(1)
print('Fim do programa.')
