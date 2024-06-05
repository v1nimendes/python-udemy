numero = int(input('Digite um número: '))
nome = input('Digite a primeira letra do alfabeto: ')

resultado = 'O número é 10' if numero == 10 else "outro valor"
nomeResultado = 'Está correta' if nome == 'a' or nome == 'A' else "errado"
print(resultado)
print(nomeResultado)
