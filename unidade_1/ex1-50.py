cont = 0
vezes = int(input("Digite a quantidade de quadrados: "))
while cont < vezes:
    lado = float(input("Digite o valor do lado: "))
    area = lado**2
    print(area, 'm²')
    cont += 1
