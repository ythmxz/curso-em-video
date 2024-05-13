# DESAFIO 002:
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Olá, qual é o seu nome? ')

# RESOLUÇÃO 1:
print('É um prazer te conhecer,', nome, '!')

# RESOLUÇÃO 2:
print('É um prazer te conhecer, {}!'.format(nome))

# RESOLUÇÃO 3:
print(f'É um prazer te conhecer, {nome}!')
