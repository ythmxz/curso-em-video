# DESAFIO 003:
# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um valor: '))
n2 = int(input('Agora digite outro: '))
s = n1 + n2

# RESOLUÇÃO 1:
print('A soma de', n1, 'e', n2, 'é', s, '!')

# RESOLUÇÃO 2:
print('A soma de {} e {} é {}!'.format(n1, n2, s))

# RESOLUÇÃO 3:
print(f'A soma de {n1} e {n2} é {s}!')
