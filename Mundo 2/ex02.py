# =================================
# Exercício ex2 - Conversor de base numérica (binário, octal, hexadecimal)
# =================================

# -------- Minha solução --------
num = int(input('Digite o numero para a converçao'))
print('''digite a base de conversão
      [1] para binario 
      [2] para octal 
      [3] hexadecimal''')
select = int(input('Digite a converção desejada: '))

if select == 1:
    binario = bin(num)[2:]
    print('Depois da conversão seu numero ficou assim: {}'.format(binario))
elif select == 2:
    octal = oct(num)[2:]
    print('Depois da conversão seu numero ficou assim: {}'.format(octal))
elif select == 3:
    hexadecimal = hex(num)[2:]
    print('Depois da conversão seu numero ficou assim: {}'.format(hexadecimal))
else:
    print("\033[31mOpção inválida! Escolha 1, 2 ou 3.")


# -------- Solução corrigida --------
num = int(input('Digite o número para a conversão: '))
print('Escolha a base:\n[1] Binário\n[2] Octal\n[3] Hexadecimal')
select = int(input('Opção: '))

if select == 1:
    print('Binário     : {}'.format(bin(num)[2:]))
elif select == 2:
    print('Octal       : {}'.format(oct(num)[2:]))
elif select == 3:
    print('Hexadecimal : {}'.format(hex(num)[2:].upper()))
else:
    print('\033[31mOpção inválida!\033[m Escolha 1, 2 ou 3.')