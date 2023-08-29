maiorvalor = 0
for i in range(10):
    valor = float(input('Digite um valor: '))
    if valor > maiorvalor:
        maiorvalor = valor
print(f'O maior valor é {maiorvalor}')
