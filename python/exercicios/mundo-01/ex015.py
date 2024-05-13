# DESAFIO 015
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

d = int(input('Dias alugados: '))
km = float(input('Quilômetros rodados: '))
a = (60 * d) + (0.15 * km)

print('Ao utilizar o carro por {} dias e rodar por {:.1f}km, o valor a pagar é R${:.2f}.'.format(d, km, a))
