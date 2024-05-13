# DESAFIO 019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome escolhido.

import random

a1 = input('Nomeie o primeiro aluno: ')
a2 = input('Nomeio o segundo aluno: ')
a3 = input('Nomeio o terceiro aluno: ')
a4 = input('Nomeio o quarto aluno: ')

print('Entre {}, {}, {} e {},'.format(a1, a2, a3, a4), end=' ')
print('o aluno escolhido para apagar o quadro foi {}.')
