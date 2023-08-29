soma = 0
valor = int(input('Digite um número: '))
for i in range(1,101):
    soma = soma + (valor + i)
    print(soma)
print(soma)