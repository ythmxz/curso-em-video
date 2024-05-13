# DESAFIO 006
# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# RESOLUÇÃO 1:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {:.1f}.'.format(n, d,n, t,n, r))

# RESOLUÇÃO 2:
n = int(input('Digite um número: '))

print('O dobro de {} é {}.\nO triplo de {} é {}.'.format(n, (n*2), n, (n*3)))
print('A raiz quadrada de {} é {:.1f}.'.format(n, (n**(1/2))))
