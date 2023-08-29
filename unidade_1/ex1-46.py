#sinceramente, não entendi direito essa questão, o enunciado tava muito vago.

i = 0
while i < 30:
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota = (nota1 + nota2) / 2
    if nota >= 0 and nota <= 10:
        i += 1
        if nota < 4:
            print('Reprovado')
        if nota < 7 and nota > 4:
            print('Recuperação')
        if nota >= 7:
            print('Aprovado')
    else:
        print('Nota inválida')
