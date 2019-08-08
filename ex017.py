#017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Valor cateto oposto: '))
ca = float(input('Valor cateto adjacente: '))

print('valor da hipotenusa: {:.2f}'.format(math.hypot(co, ca)))
