from SimpleStack import *
stack = Stack(10)
for word in ['May', 'the', 'force', 'be', 'with', 'you']:
    stack.push(word)

print('Después de agregar', len(stack),
      'palabras a la pila, contiene:\n', stack)
print('¿Está la pila llena?', stack.isFull())
print('Sacando elementos de la pila:')
while not stack.isEmpty():
    print(stack.pop(), end=' ')
print()