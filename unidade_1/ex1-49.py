soma = 0
cont = 0
vezes = float(input("Digite a quantidade de vezes: "))
while cont < vezes:
    valor = float(input("Digite o valor: "))
    if valor <= 1000 and valor >= 0 and valor%2 == 0:
        soma += valor
        cont += 1
    else:
        print("Valor inválido (maior que 1000, negativo ou ímpar)")
print(soma)