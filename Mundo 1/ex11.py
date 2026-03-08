# =================================
# Exercício 11 - Área da parede e quantidade de tinta
# =================================

# -------- Minha solução --------
l = float(input('qual a largura da sua parede? '))
a = float(input('qual a altura da sua parede? '))
area = a * l
print('as dimensões de {}x{} e sua área é de {}m²,\n para pintar a parede vc precisa de {}l de tinta'.format(l, a, area, area / 2))


# -------- Solução corrigida --------
largura = float(input('Qual a largura da parede (m)? '))
altura  = float(input('Qual a altura da parede (m)? '))
area    = largura * altura
tinta   = area / 2  # 1 litro cobre 2m²
print('Dimensões: {:.1f}m x {:.1f}m'.format(largura, altura))
print('Área: {:.2f}m²'.format(area))
print('Tinta necessária: {:.2f} litros'.format(tinta))
