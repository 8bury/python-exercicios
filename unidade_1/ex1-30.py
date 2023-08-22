valorhora = float(input("Digite o valor da hora trabalhada: "))
horasmes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salariobruto = valorhora * horasmes
if salariobruto <= 900:
    ir = 0
elif salariobruto <= 1500:
    ir = 5
elif salariobruto <= 2500:
    ir = 10
else:
    ir = 20
inss = salariobruto * 0.1
fgts = salariobruto * 0.11
irdesconto = salariobruto * (ir / 100)
descontos = inss + irdesconto
salarioliquido = salariobruto - descontos
print(f"Salário Bruto: R$ {salariobruto}")
print(f'IR ({ir}%): R$ {irdesconto}')
print(f'INSS (10%): R$ {inss}')
print(f'FGTS (11%): R$ {fgts}')
print(f'Total de descontos : R$ {descontos}')
print(f'Salário Líquido : R$ {salarioliquido}')