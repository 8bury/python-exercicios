ganhohora = float(input('ganho por hora: '))
numerohora = float(input('horas trabalhadas no mês: '))
bruto = ganhohora * numerohora
inss = bruto * 0.08
sindicato = bruto * 0.05
descontoir = bruto * 0.11
liquido = bruto - inss - sindicato - descontoir
print(f'bruto = {bruto} \n ir = {descontoir} \n inss = {inss} \n sindicato = {sindicato} \n liquido = {liquido}')