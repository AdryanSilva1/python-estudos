# =================================
# Exercício ex27 - Função escreve mensagem com moldura
# =================================

# -------- Minha solução --------
def esceva(msg):         
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

esceva(str(input('escreva sua mensagem: ')))


# -------- Solução corrigida --------
def escreve(msg):
    linha = '-' * len(msg)
    print(linha)
    print(msg)
    print(linha)

escreve(input('Digite sua mensagem: '))
