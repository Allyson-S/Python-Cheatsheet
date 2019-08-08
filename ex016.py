#016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
value = float(input('Digite um valor: '))
print('O valor inteiro é: {}'.format(trunc(value)))

''' ou
print('O valor inteiro é: {}'.format(int(value)))'''
