# DESAFIO 012
# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# RESOLUÇÃO 1:
p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 0.05)

print('Seu produto de R${:.2f} sairá por R${:.2f} agora, com 5% de desconto!'.format(p, d))

# RESOLUÇÃO 2:
p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 5 / 100)

print('Seu produto de R${:.2f} sairá por R${:.2f} agora, com 5% de desconto!'.format(p, d))
