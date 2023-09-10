#questao dos gols
pontos = 0
placar1 = placar2 = 0
loop = True
while loop:
    placar1 = int(input('Digite o placar do time 1: '))
    placar2 = int(input('Digite o placar do time 2: '))
    if placar1 > placar2:
        pontos += 3
    elif placar1 == placar2:
        pontos += 1
    else:
        pontos += 0
    if placar1 < 0 or placar2 < 0:
        loop = False
print(f'Pontuação do time: {pontos}')