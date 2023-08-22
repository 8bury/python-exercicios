preco1 = float(input('preço do primeiro produto: '))
preco2 = float(input('preço do segundo produto: '))
preco3 = float(input('preço do terceiro produto: '))
if preco1 < preco2 and preco1 < preco3:
    print(f'compre o primeiro produto que custa R${preco1}')
elif preco2 < preco1 and preco2 < preco3:
    print(f'compre o segundo produto que custa R${preco2}')
elif preco3 < preco1 and preco3 < preco2:
    print(f'compre o terceiro produto que custa R${preco3}')
else:
    print(f'os três produtos custam o mesmo preço: R${preco1}')