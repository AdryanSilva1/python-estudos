# =================================
# Exercício 31 - Preço de viagem por distância
# =================================

# -------- Minha solução --------
# Erro: '{:.2f500}' — formato inválido (o '500' não faz parte da sintaxe de format) - Falta de atenção enorme.
#      Deveria ser apenas '{:.2f}'.
distancia = float(input('digite a distância de sua viagem: '))
if distancia <= 200:
    print('a taxa cobrada é de 0,50R$, o preço de sua viagem é:{:.2f500}'.format(distancia * 0.50))  # BUG
else:
    print('a taxa cobrada é de 0,45R$,o preço da seua viagem é:{:.2f}'.format(distancia * 0.45))


# -------- Solução corrigida --------
distancia = float(input('Digite a distância da viagem (km): '))
if distancia <= 200:
    preco = distancia * 0.50
    print('Taxa: R$ 0,50/km | Preço da viagem: R$ {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Taxa: R$ 0,45/km | Preço da viagem: R$ {:.2f}'.format(preco))
