nome = input('Informe seu nome: ')
altura = float(input('Informe a sua altura : '))
peso = float(input('Infome seu peso: '))

imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)