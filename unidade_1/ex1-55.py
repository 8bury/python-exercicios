resultado = 0
varA = 0
termos = int(input('Digite o número de termos: '))
x = float(input('Digite um valor: '))
for i in range(1, termos+1):
    if i == 1:
        resultado -= x
        varA += 3
    if i % 2 == 0:
        resultado += (x**varA)/varA
        varA += 2
    else:
        resultado -= (x**varA)/varA
        varA += 2
print(resultado)