soma = 0 
conttentativa = 0
pessoas = int(input("Digite o número de pessoas: "))
while conttentativa < pessoas:
    idade = int(input("Digite a idade da pessoa: "))
    if idade >= 0:
        soma += idade
        conttentativa += 1
    else:
        print("Idade inválida!")
media = soma / pessoas
print(f'A média das idades é {media:.2f}')
if media >= 0 and media <=25:
    print("Turma jovem!")
elif media >= 26 and media <=60:
    print("Turma adulta!")
else:
    print("Turma idosa!")