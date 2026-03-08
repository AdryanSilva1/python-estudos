# =================================
# Exercício ex13 - Validador de parênteses (pilha/stack)
# =================================

# -------- Minha solução --------
# Solução do curso (não consegui fazer sozinho). Usa pilha para verificar balanço.
# Lógica correta.
expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')


# -------- Solução corrigida --------
# Mesma lógica, versão mais clara
expr = input('Digite uma expressão: ')
pilha = []
valida = True

for char in expr:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if pilha:
            pilha.pop()
        else:
            valida = False
            break

if pilha:
    valida = False

print('Expressão VÁLIDA!' if valida else 'Expressão INVÁLIDA!')