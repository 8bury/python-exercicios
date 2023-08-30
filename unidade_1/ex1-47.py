maiorvalor = 0
menorvalor = 0
for i in range(10):
    valor = float(input('Digite um valor: '))
    if valor > maiorvalor:
        maiorvalor = valor
    if valor < menorvalor:
        menorvalor = valor
print(f'O maior valor é {maiorvalor} e o menor valor é {menorvalor}')
