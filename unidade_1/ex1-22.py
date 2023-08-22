num1 = float(input('primeiro número: '))
num2 = float(input('segundo número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')
else:
    print(f'{num1} e {num2} são iguais')