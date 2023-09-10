num = int(input('Digite um número: '))
mult1 = 1
mult2 = 2
mult3 = 3
while mult1 * mult2 * mult3 < num:
    mult1 += 1
    mult2 += 1
    mult3 += 1
if mult1 * mult2 * mult3 == num:
    print(f'O número {num} é triangular.')
else:
    print(f'O número {num} não é triangular.')