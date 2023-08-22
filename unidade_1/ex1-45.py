altura = float(input('digite sua altura: '))
sexo = input('digite seu sexo (M ou F): ')
if sexo.upper() == 'M':
  pesoideal = (72.7 * altura) - 58
  print(f'seu peso ideal é {pesoideal}')
elif sexo.upper() == 'F':
  pesoideal = (62.1 * altura) - 44.7
  print(f'seu peso ideal é {pesoideal}')
else:
  print('erro')