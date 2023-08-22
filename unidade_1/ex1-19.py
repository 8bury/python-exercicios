tamanho = float(input('tamanho do arquivo em MB: '))
velocidade = float(input('velocidade de download em MBps: '))
tempo = (tamanho/velocidade)//60
resto = (tamanho/velocidade)%60
print(tempo, 'min e', resto, 'seg' )