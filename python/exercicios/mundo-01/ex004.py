# DESAFIO 004:
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

a = input('Digite algo: ')

print('O tipo primitivo é:', type(a))

print('É alfanumérico?', a.isalnum())

print('É alfabético?', a.isalpha())

print('É numérico?', a.isnumeric())

print('É minúsculo?', a.islower())

print('É maiúsculo?', a.isupper())

print('É capitalizado?', a.istitle())
