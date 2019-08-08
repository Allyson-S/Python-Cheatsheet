# Crie um programa que leia o nome completo de uma pessoa e mostre
## - O nome com todas as letras maiúsculas e minúsculas
### - Quantas letras ao todo sem considerar espaços
#### - Quantas letras tem o primeiro nome

name = str(input('Digite seu nome: ')).strip()
print('Analizando..')
print('Seu nome em maiusculas é: {}'.format(name.upper()))
print('Seu nome em minusculas é: {}'.format(name.lower()))

print('Numero de letras o seu nome: {}'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras.'.format((name.find(' '))))
