#020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

name1 = str(input('Digite seu nome 1: '))
name2 = str(input('Digite seu nome 2: '))
name3 = str(input('Digite seu nome 3: '))
name4 = str(input('Digite seu nome 4: '))
lista = [name1, name2, name3, name4]
shuffle(lista)
print('O lista é: {}'.format(lista))
