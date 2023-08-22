a = float(input("Digite o valor de a: "))
if a == 0:
    print('Não é uma equação do segundo grau')
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Não existem raízes reais")
    if delta == 0:
        print("Existe uma raiz real")
    if delta > 0:
        print("Existem duas raízes reais")