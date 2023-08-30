valor = int(input('Digite um número: '))
soma = 0
progressao = 1
for i in range(1, valor+1):
    soma += i/progressao
    progressao += 2
print(soma)