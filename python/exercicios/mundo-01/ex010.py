# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1.00 = R$3.27

r = float(input('Digite seu saldo em real: R$'))
d = r / 3.27

print('Com o saldo de R${:.2f} você pode comprar US${:.2f}.'.format(r, d))
