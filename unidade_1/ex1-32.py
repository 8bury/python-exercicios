conceito = ''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
notamedia = (nota1 + nota2) / 2
if notamedia >= 9 and notamedia <= 10:
    conceito = 'A'
elif notamedia >= 7.5 and notamedia < 9:
    conceito = 'B'
elif notamedia >= 6 and notamedia < 7.5:
    conceito = 'C'
elif notamedia >= 4 and notamedia < 6:
    conceito = 'D'
elif notamedia >= 0 and notamedia < 4:
    conceito = 'E'
else:
    print("Nota inválida")
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print("Aprovado")
else:
    print("Reprovado")