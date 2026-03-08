# =================================
# Exercício ex12 - Separar lista em pares e ímpares
# =================================

# -------- Minha solução --------
# Lógica correta. Popula 3 listas simultaneamente durante a entrada.
lista = []
listaImpar = []
listaPaar = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        listaPaar.append(numero)
    else:
        listaImpar.append(numero)
    if input('Deseja continuar? [S/N] ').strip().upper() == 'N':
        break
print(f'Números digitados: {lista}')
print(f'Pares   : {listaPaar}')
print(f'Ímpares : {listaImpar}')


# -------- Solução corrigida --------
# Versão Guanabara: separa em pós-processamento com for enumerate
numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    if input('Continuar? [S/N]: ').strip().upper() == 'N':
        break

pares   = [v for v in numeros if v % 2 == 0]
impares = [v for v in numeros if v % 2 != 0]

print(f'Lista completa : {numeros}')
print(f'Pares          : {pares}')
print(f'Ímpares        : {impares}')
