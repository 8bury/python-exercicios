loop = True
somanumeros = somanumerospares = somanumerosimpares = quantnumerospares = quantnumerosimpares = 0
while loop:
    numero = int(input('numero: '))
    if numero < 0:
        print('número inválido.')
    elif numero != 0:
        somanumeros += numero
        if numero % 2 == 0:
            quantnumerospares += 1
            somanumerospares += numero
        else:
            quantnumerosimpares += 1
            somanumerosimpares += numero
    else:
        loop = False
print(f'quantidade de números pares: {quantnumerospares}')
print(f'quantidade de números ímpares: {quantnumerosimpares}')
print(f'media de números pares: {somanumerospares / quantnumerospares}')
print(f'media geral: {somanumeros / (quantnumerospares + quantnumerosimpares)}')