idade = int(input('Digite a idade: '))
if idade >= 18:
    print('adulto')
elif idade >= 14 and idade <=17:
    print('juvenil B')
elif idade >= 11 and idade <=13:
    print('juvenil A')
elif idade >= 8 and idade <=10:
    print('infantil B')
elif idade >= 5 and idade <=7:
    print('infantil A')
else:
    print('Não pode competir/idade inválida')