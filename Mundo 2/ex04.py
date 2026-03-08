# =================================
# Exercício ex4 - Serviço militar (já serviu / vai servir / serve esse ano)
# =================================

# -------- Minha solução --------
from datetime import date

nasc = int(input('para saber se você vai servir digite o ano do seu nascimento: '))
data = date.today().year
ano = data - nasc
if ano < 18:
    temp = 18 - ano
    print('você ainda terá que servir quando ficar mais velho\n falta {} anos para você servir'.format(temp))
elif ano == 18:
    print('você ira servir esse ano')
elif ano > 18:
    temp = ano - 18
    print('você serviu á {} anos atras'.format(temp))
print(f'quem nasceu em {nasc} tem {ano} anos em {data}')


# -------- Solução corrigida --------
from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade < 18:
    faltam = 18 - idade
    print('Você ainda não tem idade para servir. Faltam {} anos.'.format(faltam))
elif idade == 18:
    print('Você irá servir este ano.')
else:
    tempo = idade - 18
    print('Você serviu há {} anos.'.format(tempo))

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')
