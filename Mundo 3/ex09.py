# =================================
# Exercício ex09 - Lista sem duplicatas
# =================================

# -------- Minha solução --------
# Lógica correta. Validação de 'S/N' com loop interno — mais robusta que a versão Guanabara.
lista = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if continuar in ['S', 'N']:
            break
        print('Opção inválida! Tente novamente...')

    if continuar == 'N':
        break

lista.sort()
print(f'\nOs valores digitados foram: {lista}')


# -------- Solução corrigida --------
# Versão Guanabara: mais simples, sem validação de S/N — correta para o exercício
numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado!')
    else:
        print('Duplicado! Ignorado.')
    if input('Continuar? [S/N] ').strip().upper() == 'N':
        break

numeros.sort()
print(f'Valores únicos: {numeros}')

