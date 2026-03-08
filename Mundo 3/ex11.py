# =================================
# Exercício ex11 - Lista ordenada decrescente e contar ocorrências do 5
# =================================

# -------- Minha solução --------
# Lógica correta. Usa lista.count(5) para contar — mais direto que o Guanabara.
lista = []
numerosDigitados = 0
while True:
    lista.append(int(input('Digite um número: ')))
    numerosDigitados += 1
    if input('Deseja continuar? [S/N] ').strip().upper() == 'N':
        break
print(f'Você digitou {numerosDigitados} números.')
lista.sort(reverse=True)
print(f'Valores em ordem decrescente: {lista}')
print(f'O número 5 aparece {lista.count(5)} vez(es).')


# -------- Solução corrigida --------
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if input('Continuar? [S/N]: ').strip().upper() == 'N':
        break

valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elemento(s).')
print(f'Ordem decrescente: {valores}')
print(f'O valor 5 aparece {valores.count(5)} vez(es).')
