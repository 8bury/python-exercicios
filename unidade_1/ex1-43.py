precomorango = 2.50
precomorangodesconto = 2.20
precomaca = 1.80
precomacadesconto = 1.50
quilosmorango = float(input('quilos de morango: '))
quilosmaca = float(input('quilos de maçã: '))
if quilosmorango <= 5:
  valormorango = quilosmorango * precomorango
else:
  valormorango = quilosmorango * precomorangodesconto
if quilosmaca <= 5:
  valormaca = quilosmaca * precomaca
else:
  valormaca = quilosmaca * precomacadesconto
valortotal = valormorango + valormaca
if (quilosmorango + quilosmaca) > 8 or (valormorango + valormaca) > 25:
  valortotal = (valortotal) * 0.9
print(f'valor total: {valortotal}')