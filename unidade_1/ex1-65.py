soma, cont = 0, 0
i = int(input("Digite o número de temperaturas: "))
while i > cont:
    valor = float(input('Digite uma temperatura: '))
    if cont == 0:
        maiorvalor = valor
        menorvalor = valor
    if valor > maiorvalor:
        maiorvalor = valor
    if valor < menorvalor:
        menorvalor = valor
    soma += valor
    cont += 1
print(f'O maior valor é {maiorvalor} e o menor valor é {menorvalor} e a media é {soma/i}')
 