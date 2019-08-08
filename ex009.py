# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('digite um valor para a tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('-'*12)