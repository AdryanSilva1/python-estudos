# =================================
# Exercício ex21 - Cadastro de 4 pessoas: média de idade, homem mais velho, mulheres < 20
# =================================

# -------- Minha solução --------
somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulhor20 = 0

for p in range(1, 5):
    print(f'----- {p}° pessoa------')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':          # Erro: só inicializa se 1ª for homem
        maioridadehomen = idade
        nomevelho = nome

    if sexo in 'mn' and idade > maioridadehomen:  # Erro: 'n' não é masculino
        maioridadehomen = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulhor20 += 1

mediaidade = somaidade / 4
print(f'a medida de idade do grupo é {mediaidade}')
print(f'o homen mais velho é {nomevelho} e sua idade e de {maioridadehomen}')
print(f'ha {totmulhor20} mulheres com menos de 20 anos ')


# -------- Solução corrigida --------
soma_idade = 0
maior_idade_homem = -1   # -1 indica "nenhum homem encontrado ainda"
nome_mais_velho = 'Nenhum homem cadastrado'
tot_mulheres_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª pessoa -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo == 'F' and idade < 20:
        tot_mulheres_20 += 1

media = soma_idade / 4
print(f'Média de idade: {media:.1f}')
print(f'Homem mais velho: {nome_mais_velho} ({maior_idade_homem} anos)')
print(f'Mulheres com menos de 20 anos: {tot_mulheres_20}')
