# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
variable = input('Digite algo: ')
print('O tipo dessa variável é: ', type(variable))
print('Só tem espaço: ', variable.isspace())
print('É numero: ', variable.isnumeric())
print('É alfabeto', variable.isalpha())
print('É alfanumerico: ', variable.isalnum())
