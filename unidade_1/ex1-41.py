#vou fazer uso de lista
cont = 0
perguntas = ['telefonou para a vitima? ', 'esteve no local do crime? ', 'mora perto da vitima? ', 'devia para a vitima? ', 'ja trabalhou com a vitima? ']
for i in range(0, len(perguntas)):
    resposta = input(perguntas[i])
    if resposta == 's':
        cont += 1
if cont == 2:
    print('Suspeita')
elif cont == 3 or cont == 4:
    print('Cúmplice')
elif cont == 5:
    print('Assassino')
else:
    print('Inocente')