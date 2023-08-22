percentualusado = 0
percentual1 = 1.2
percentual2 = 1.15
percentual3 = 1.1
percentual4 = 1.05

salario = float(input('salario: '))

if salario <= 280:
    salarionovo = salario * percentual1
    percentual1 = percentualusado
elif salario > 280 and salario <= 700:
    salarionovo = salario * percentual2
    percentual2 = percentualusado
elif salario > 700 and salario <= 1500:
    salarionovo = salario * percentual3
    percentual3 = percentualusado
elif salario > 1500:
    salarionovo = salario * percentual4
    percentual4 = percentualusado
print(f'salario antigo = {salario} \npercentual de aumento = {percentualusado}\nvalor do aumento = {salarionovo - salario}\nsalário novo = {salarionovo}')