turno = input('qual turno você estuda (M - matutino, V - vespertino ou N - noturno): ')
if turno.upper() == 'M':
    print('Bom dia!')
elif turno.upper() == 'V':
    print('Boa tarde!')
elif turno.upper() == 'N':
    print('Boa noite!')
else:
    print('Turno inválido')