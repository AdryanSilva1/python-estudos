# =================================
# Exercício ex9 - Lojinha: formas de pagamento com desconto/juros
# =================================

# -------- Minha solução --------
print('{:=^40}'.format(' LOGINHA '))
produto = float(input('digite o preço das compras'))
pagamento = int(input('''para escolher a forma de pagamento digite: 
[1] avista no dinheiro/cheque 
[2] cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão 
escolha umas das opções acima:'''))
if pagamento == 1:
    p = produto - (produto * 10 / 100)
    print(f'com 10% de desconto o novo valor é de {p}')
elif pagamento == 2:
    p = produto - (produto * 5 / 100)
    print(f'com 5% de desconto o novo valor é de {p}')
elif pagamento == 3:
    print(f'o valor do seu pagamento e de {produto}')
elif pagamento == 4:
    p = produto + (produto * 20 / 100)
    print(f'com os juros de 20% os valor total será de {p}')
else:
    print('\033[31mForma de pagamento recusada você deve escolher entre as opções listadas')


# -------- Solução corrigida --------
print('{:=^40}'.format(' LOGINHA '))
produto = float(input('Preço das compras: R$ '))
print('''Forma de pagamento:
[1] À vista dinheiro/cheque (-10%)
[2] Cartão à vista (-5%)
[3] 2x no cartão (sem juros)
[4] 3x ou mais no cartão (+20%)''')
pagamento = int(input('Escolha: '))

if pagamento == 1:
    total = produto * 0.90
    print('Desconto de 10% | Total: R$ {:.2f}'.format(total))
elif pagamento == 2:
    total = produto * 0.95
    print('Desconto de 5% | Total: R$ {:.2f}'.format(total))
elif pagamento == 3:
    parcela = produto / 2
    print('2x de R$ {:.2f} | Total: R$ {:.2f}'.format(parcela, produto))
elif pagamento == 4:
    total = produto * 1.20
    print('Juros de 20% | Total: R$ {:.2f}'.format(total))
else:
    print('\033[31mOpção inválida!\033[m')
