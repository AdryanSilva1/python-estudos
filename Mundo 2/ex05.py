# =================================
# Exercício ex5 - Aprovação, recuperação ou reprovação
# =================================

# -------- Minha solução --------
nota1 = float(input('digite seu nota em portugues:'))
nota2 = float(input('digite seu nota em matematica:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[31mVocê foi reprovado')
elif media > 5.0 and media < 6.9:   # Erro: 5.0 exato não entra aqui
    print('\033[33mvocê ficou de recuperação')
elif media > 7.0:                   # Erro: 7.0 exato não entra aqui
    print('\033[32mvocê foi aprovado')


# -------- Solução corrigida --------
nota1 = float(input('Digite sua nota em Português: '))
nota2 = float(input('Digite sua nota em Matemática: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[31mReprovado\033[m')
elif media < 7.0:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[32mAprovado\033[m')

print('Média: {:.1f}'.format(media))

