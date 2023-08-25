num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, x ou /): ")
if operacao == '+':
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')
    if resultado == 0:
        print('O número é neutro')
    else:
        if resultado % 2 == 0:
            print('O número é par')
        else:
            print('O número é ímpar')
        if resultado > 0:
            print('O número é positivo')
        else:
            print('O número é negativo')
        if resultado % 1 == 0:
            print('O número é inteiro')
        else:
            print('O número é decimal')
elif operacao == '-':
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')
    if resultado == 0:
        print('O número é neutro')
    else:
        if resultado % 2 == 0:
            print('O número é par')
        else:
            print('O número é ímpar')
        if resultado > 0:
            print('O número é positivo')
        else:
            print('O número é negativo')
        if resultado % 1 == 0:
            print('O número é inteiro')
        else:
            print('O número é decimal')
elif operacao == 'x':
    resultado = num1 * num2
    print(f'{num1} x {num2} = {resultado}')
    if resultado == 0:
        print('O número é neutro')
    else:
        if resultado % 2 == 0:
            print('O número é par')
        else:
            print('O número é ímpar')
        if resultado > 0:
            print('O número é positivo')
        else:
            print('O número é negativo')
        if resultado % 1 == 0:
            print('O número é inteiro')
        else:
            print('O número é decimal')
elif operacao == '/':
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}')
    if resultado == 0:
        print('O número é neutro')
    else:
        if resultado % 2 == 0:
            print('O número é par')
        else:
            print('O número é ímpar')
        if resultado > 0:
            print('O número é positivo')
        else:
            print('O número é negativo')
        if resultado % 1 == 0:
            print('O número é inteiro')
        else:
            print('O número é decimal')
