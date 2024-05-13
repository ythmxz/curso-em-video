# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Quantos metros deseja converter? '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000

print('{} metros equivale(m) a:\n\n{} quilômetros;\n{:.2f} hectômetros;\n{:.1f} decâmetros;'.format(m, km, hm, dam))
print('{:.0f} decímetros;\n{:.0f} centímetros;\n{:.0f} milímetros.'.format(dm, cm, mm))
