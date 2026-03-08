# =================================
# Exercício 23 - Separar dígitos de um número (unidade, dezena, centena, milhar)
# =================================

# -------- Minha solução --------
# Lógica correta; print muito longo em uma linha só.
num = int(input('digite um numero de 0 a 9999: '))
print(' seu numero {} separado ficou \n unidade: {} \n dezena: {} \n centena: {} \n milhar:{}'.format(
    num, num % 10, (num // 10) % 10, (num // 100) % 10, num // 1000))


# -------- Solução corrigida --------
num = int(input('Digite um número de 0 a 9999: '))
unidade = num % 10
dezena  = (num // 10) % 10
centena = (num // 100) % 10
milhar  = num // 1000

print('Analisando o número: {}'.format(num))
print('Milhar  : {}'.format(milhar))
print('Centena : {}'.format(centena))
print('Dezena  : {}'.format(dezena))
print('Unidade : {}'.format(unidade))
