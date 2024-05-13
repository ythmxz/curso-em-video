# DESAFIO 013
# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# RESOLUÇÃO 1:
s = float(input('Digite seu salário atual: R$'))
a = s + (s * 0.15)

print('Seu salário passou de R${:.2f} para R${:.2f}, com um aumento de 15%!'.format(s, a))

# RESOLUÇÃO 2:
s = float(input('Digite seu salário atual: R$'))
a = s + (s * 15 / 100)

print('Seu salário passou de R${:.2f} para R${:.2f}, com um aumento de 15%!'.format(s, a))
