aux = ''
varA = input('A = ')
varB = input('B = ')

aux = varA #guardar o valor de varA no aux
varA = varB
varB = aux

print(f'A = {varA}')
print(f'B = {varB}')

