loop = True
maiorsalario = somasalario = contagemsalario250 = somafilhos = 0
while loop:
    salario = float(input('Digite o salário do habitante: '))
    if salario >= 0:
        filhos = int(input('Digite a quantidade de filhos do habitante: '))
        if filhos >= 0:
            somasalario += salario
            somafilhos += filhos
            if salario > 250:
                contagemsalario250 += 1
            if salario > maiorsalario:
                maiorsalario = salario
        else:
            print('A quantidade de filhos não pode ser negativa.')
    else:
        loop = False
print(f'A média dos salários da população é de R${somasalario / somafilhos:.2f}.')
print(f'A média do número de filhos é de {somafilhos / somafilhos:.2f}.')
print(f'O maior salário é de R${maiorsalario:.2f}.')
print(f'{contagemsalario250} habitantes possuem salário superior a R$250,00.')