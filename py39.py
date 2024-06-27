print('Minha solução')
def duplicar(numero):
    return numero * 2

print(duplicar(2))

def triplicaer(numero):
    return numero * 3

print(triplicaer(2))

def quadriplicar(numero):
    return numero * 4

print(quadriplicar(2))

print('Solução do professor')
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))