#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
variable = float(input('Digite um valor: '))
print('O dobro é: {}.  O triplo é: {}.  E a raiz quadrada é: {:.2f}'.format((variable*2),(variable*3),(variable**(1/2))))
