nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
media = (nota1 + nota2) / 2
if media == 10:
    print(f'aprovado com distinção com média {media}')
elif media >= 7:
    print(f'aprovado com média {media}')
else:
    print(f'reprovado com média {media}')
