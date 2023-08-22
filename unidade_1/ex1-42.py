litrosvendidos = float(input('litros vendidos: '))
combustivel = input('Combustivel (G ou A): ')
if combustivel.upper() == 'A':
  if litrosvendidos <= 20:
    desconto = (1.9 * 0.97)
    print(desconto)
  if litrosvendidos > 20:
    desconto = (1.9 * 0.95)
    print(desconto)
elif combustivel.upper() == 'B':
  if litrosvendidos <= 20:
    desconto = (2.5 * 0.96)
    print(desconto)
  if litrosvendidos > 20:
    desconto = (2.5 * 0.94)
    print(desconto)
else:
  print('erro')