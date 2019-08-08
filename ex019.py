#019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
name1 = str(input('Digite seu nome 1: '))
name2 = str(input('Digite seu nome 2: '))
name3 = str(input('Digite seu nome 3: '))
name4 = str(input('Digite seu nome 4: '))
lista = [name1, name2, name3, name4]

print('O escolhido é: {}'.format(random.choice(lista)))
