# =================================
# Exercício 00 - Verificador de voto (introdução a funções)
# =================================

# -------- Minha solução --------

from time import sleep

def voto(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    if idade < 18:
        return 'você ainda não pode votar'
    elif idade > 70:           # Erro: 70 anos exatos fica sem retorno no else (obrigatório)
        return 'você já pode votar, mas não é obrigatório'
    else:
        return 'você já pode votar e é obrigatório'

print('==' * 20)
print('verificador de idade para voto')
print('==' * 20)
nascimento = int(input('Digite o ano de seu nascimento: '))
sleep(1)
print('Verificando...')
sleep(2)
print(voto(nascimento))


# -------- Solução corrigida --------
from time import sleep
from datetime import date

def situacao_voto(nascimento):
    idade = date.today().year - nascimento
    if idade < 16:
        return 'Não pode votar ainda.'
    elif idade < 18:
        return 'Voto facultativo (16-17 anos).'
    elif idade <= 70:
        return 'Voto obrigatório.'
    else:
        return 'Voto facultativo (acima de 70 anos).'

nascimento = int(input('Digite o ano de seu nascimento: '))
sleep(1)
print(situacao_voto(nascimento))
