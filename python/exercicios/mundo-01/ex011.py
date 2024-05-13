# DESAFIO 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Qual é a largura da sua parede? '))
alt = float(input('Qual é a altura da sua parede?'))
area = larg * alt
tinta = area / 2

print('A dimensão da sua parede é de {:.1f}m x {:.1f}m. A área dela é de {:.1f}m².'.format(larg, alt, area))
print('Para pintá-la você usará {:.1f}L de tinta.'.format(tinta))
