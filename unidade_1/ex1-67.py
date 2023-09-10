mesesmin = numeromesesmin = float('inf')
mesesmax = numeromesesmax = 0

loop = True

while loop:
    numero = int(input('Digite o número do empregado: '))
    meses = int(input('Digite o número de meses trabalhados: '))
    if numero and meses > 0:
        if meses > mesesmax:
            mesesmax = meses
            numeromesesmax = numero
        elif meses < mesesmin:
            mesesmin = meses
            numeromesesmin = numero
    else:
        loop = False

print(f'O empregado que trabalhou mais meses foi o número {numeromesesmax} com {mesesmax} meses trabalhados.')
print(f'O empregado que trabalhou menos meses foi o número {numeromesesmin} com {mesesmin} meses trabalhados.')