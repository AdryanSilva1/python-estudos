# =================================
# Exercício 22 - Análise de nome com métodos de string
# =================================

# -------- Minha solução --------
nome = str(input('escreva o nome: '))
print('seu nome com maiusculas: {} '.format(nome.upper()))
print('seu nome com minuscuslas: {} '.format(nome.lower()))

nome = nome.strip()
l = len(nome.replace('', ''))   # Erro: deveria ser replace(' ', '')
print('letras sem considerar os epaços: {}'.format(l))

pn = nome.split()[0]
ls = len(pn)
print('seu primerio nome tem {}'.format(ls))


# -------- Solução corrigida --------
nome = input('Escreva o nome completo: ').strip()
print('Maiúsculas : {}'.format(nome.upper()))
print('Minúsculas : {}'.format(nome.lower()))

total_letras = len(nome.replace(' ', ''))   # remove espaços antes de contar
print('Letras (sem espaços): {}'.format(total_letras))

primeiro_nome = nome.split()[0]
print('Seu primeiro nome "{}" tem {} letras'.format(primeiro_nome, len(primeiro_nome)))
