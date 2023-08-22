saque = int(input('valor do saque: '))
if saque >= 10 and saque <= 600:
    notas100 = saque//100
    resto100 = saque%100
    notas50 = resto100//50
    resto50 = resto100 % 50
    notas10 = resto50//10
    resto10 = resto50%10
    notas5 = resto10//5
    resto5 = resto10%5
    notas1 = resto5//1

    print(f'{notas100} notas de 100, {notas50} notas de 50, {notas10} notas de 10, {notas5} notas de 5, {notas1} notas de 1')
else:
    print('valor inválido')