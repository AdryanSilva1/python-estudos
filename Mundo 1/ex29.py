# =================================
# Exercício 29 - Multa por excesso de velocidade
# =================================

# -------- Minha solução --------
# Usar float para aceitar velocidades decimais.
velocidade = int(input('digite a velocidade do carro:  '))
if velocidade > 80:
    print('você foi multado!')
    print('o valor de sua multa e de {}'.format((velocidade - 80) * 7))
else:
    print('parabéns vocẽ esta no limite de velocidade!')


# -------- Solução corrigida --------
LIMITE    = 80
MULTA_KM  = 7  # R$ por km acima do limite

velocidade = float(input('Qual a velocidade do carro (km/h)? '))
if velocidade > LIMITE:
    excesso = velocidade - LIMITE
    multa   = excesso * MULTA_KM
    print('MULTADO! Você excedeu o limite de {}km/h'.format(LIMITE))
    print('Excesso: {:.1f}km/h | Multa: R$ {:.2f}'.format(excesso, multa))
else:
    print('Parabéns! Você está dentro do limite de velocidade.')

