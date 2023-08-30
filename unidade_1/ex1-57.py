idadesoma, bom, regular, otimo = 0, 0, 0, 0
i = 0
while i < 15:
    idade = int(input('Digite a idade: '))
    opiniao = int(input('Digite a sua opinião (1 - regular, 2 - bom, 3 - ótimo): '))
    if opiniao == 1:
        regular += 1
        i += 1
    elif opiniao == 2:
        bom += 1
        i += 1
    elif opiniao == 3:
        otimo += 1
        i += 1
        idadesoma += idade
    else:
        print('Opinião inválida.')
print(f'Média das idades das pessoas que responderam ótimo: {idadesoma/otimo:.2f} anos')
print(f'Quantidade de pessoas que responderam regular: {regular} ou {(regular/15)*100:.2f}%')
print(f'Quantidade de pessoas que responderam bom: {bom} ou {(bom/15)*100:.2f}%')
print(f'Quantidade de pessoas que responderam ótimo: {otimo} ou {(otimo/15)*100:.2f}%')