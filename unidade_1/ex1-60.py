divisiveis = 0
cont = 2
numero = int(input('Digite um número: '))
while cont < numero:
    teste = numero % cont
    cont += 1
    if teste == 0:
        divisiveis += 1
if divisiveis == 0:
    print('O número é primo')
else:
    print('O número não é primo') 
