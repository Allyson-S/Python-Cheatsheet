#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
height = float(input('Digite a altura: '))
width = float(input('digite a largura: '))
area = height * width
print('Sua parede tem Área de: {}m² \n\nPara pintar essa Área é necessario: {}L de tinta'.format(area, (area/2)))