fatorial = int(input("Digite um número para calcular seu fatorial: "))
resultado = 1
for i in range(1, fatorial + 1):
    resultado *= i
print(f'O fatorial de {fatorial} é {resultado}')
