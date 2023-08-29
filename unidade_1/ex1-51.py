valorA = int(input('valor A: '))
resultado = valorA
valorB = int(input('valor B: '))
for i in range(1, valorB):
    resultado = resultado * valorA
print(resultado)