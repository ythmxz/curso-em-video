# DESAFIO 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# RESOLUÇÃO 1:
n = int(input('Digite um número: '))
a = n - 1
s = n + 1

print('O antecessor de {} é {}, e seu sucessor é {}.'.format(n, a, s))

# RESOLUÇÃO 2:
n = int(input('Digite um número: '))

print('O antecessor de {} é {}, e seu sucessor é {}.'.format(n, (n-1), (n+1)))
