#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('quanto vc tem na carteira: R$'))
print('A conversão para moeda dolar é : US${:.2f}'.format((real/3.27)))
