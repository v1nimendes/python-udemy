# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Vinicius')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Vinicius')
print(s1)