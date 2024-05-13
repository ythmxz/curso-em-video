# DESAFIO 014
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

# RESOLUÇÃO 1:
c = float(input('Digite a temperatura em °C: '))
f = (c * 1.8) + 32

print('A temperatura de {:.1f}°C equivale a {:.1f}°F.'.format(c, f))

# RESOLUÇÃO 2:
c = float(input('Digite a temperatura em °C: '))
f = ((9 * c) / 5) + 32

print('A temperatura de {:.1f}°C equivale a {:.1f}°F.'.format(c, f))
