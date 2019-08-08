'''018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

import math
an = float(input('Valor do angulo: '))
print('O Seno: {:.2f}. \nO Cosseno: {:.2f}. \nA Tangente: {:.2f}.'.format(math.sin(math.radians(an)), math.cos(math.radians(an)), math.tan(math.radians(an))))
