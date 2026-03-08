# =================================
# Exercício 7 - Média de notas escolares
# =================================

# -------- Minha solução --------
l = float(input('Qual é sua nota em Língua Portuguesa ?'))
m = float(input('Qual é sua nota em Matemática ?'))
h = float(input('Qual é sua nota em História?'))
g = float(input('Qual é sua nota em Geografia ?'))
c = float(input('Qual é sua nota em Ciências ?'))
a = float(input('Qual é sua nota em Arte ?'))
e = float(input('Qual é sua nota em Educação Física ?'))
f = float(input('Qual é sua nota em Filosofia ?'))
s = float(input('Qual é sua nota em Sociologia ?'))
i = float(input('Qual é sua nota em inglês ?'))

s = l + m + h + g + c + a + e + f + s + i  # Erro: 's' (Sociologia) é sobrescrito aqui
div = s / 10
print('sua media é {:.2f}.'.format(div))


# -------- Solução corrigida --------
port = float(input('Qual é sua nota em Língua Portuguesa? '))
mat  = float(input('Qual é sua nota em Matemática? '))
hist = float(input('Qual é sua nota em História? '))
geo  = float(input('Qual é sua nota em Geografia? '))
cien = float(input('Qual é sua nota em Ciências? '))
arte = float(input('Qual é sua nota em Arte? '))
edfi = float(input('Qual é sua nota em Educação Física? '))
filo = float(input('Qual é sua nota em Filosofia? '))
soci = float(input('Qual é sua nota em Sociologia? '))
ingl = float(input('Qual é sua nota em Inglês? '))

soma = port + mat + hist + geo + cien + arte + edfi + filo + soci + ingl
media = soma / 10
print('Sua média é {:.2f}.'.format(media))