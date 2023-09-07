divida = float(input('Digite o valor da divida: '))
if divida > 0:
    print(f'Valor da dívida     Valor dos juros     Quantidades de parcelas     Valor da parcela')
    print(f'R${divida:.2f}             0                     1                      R${divida:.2f}')
    print(f'R${(divida * 1.10):.2f}            100                    3                      R${(divida * 1.10)/3:.2f}')
    print(f'R${(divida * 1.15):.2f}            150                    6                      R${(divida * 1.15)/6:.2f}')
else:
    print('Valor inválido!')