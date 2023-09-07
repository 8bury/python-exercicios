#serie fettuccine
termo1 = float(input("Digite o primeiro termo: "))
termo2 = float(input("Digite o segundo termo: "))
n = int(input("Digite o número de termos: "))
if n < 3:
    print('O número de termos deve ser maior ou igual a 3!')
else:
    print(termo1, termo2)
    for i in range(3, n+1):
        if i%2 == 0:
            fettucine = termo1 + termo2
        else:
            fettucine = termo2 - termo1
        print(fettucine)
        termo1,termo2 = termo2,fettucine